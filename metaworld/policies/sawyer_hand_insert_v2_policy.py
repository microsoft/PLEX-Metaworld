import numpy as np

from metaworld.policies.action import Action
from metaworld.policies.policy import Policy, assert_fully_parsed, move


class SawyerHandInsertV2Policy(Policy):
    p = 10.
    num_stages = 4

    @staticmethod
    def sample_xyz():
        return np.random.uniform((-1.0, -1.0, 0.0), (1.0, 1.0, 1.0))

    @staticmethod
    @assert_fully_parsed
    def _parse_obs(obs):
        return {
            'hand_pos': obs[:3],
            'gripper': obs[3],
            'obj_pos': obs[4:7],
            'goal_pos': obs[-3:],
            'unused_info': obs[7:-3],
        }

    def get_action(self, obs):
        o_d = self._parse_obs(obs)

        action = Action({
            'delta_pos': np.arange(3),
            'grab_effort': 3
        })

        stage, goal = self._desired_pos(o_d)
        action['delta_pos'] = move(o_d['hand_pos'], to_xyz=goal, p=self.p)
        action['grab_effort'] = self._grab_effort(o_d)

        return action.array

    @staticmethod
    def _desired_pos(o_d):
        hand_pos = o_d['hand_pos']
        obj_pos = o_d['obj_pos']
        goal_pos = o_d['goal_pos']

        # If error in the XY plane is greater than 0.02, place end effector above the puck
        if np.linalg.norm(hand_pos[:2] - obj_pos[:2]) > 0.02:
            return 0, obj_pos + np.array([0., 0., 0.1])
        # Once XY error is low enough, drop end effector down on top of puck
        elif abs(hand_pos[2] - obj_pos[2]) > 0.05:
            return 1, obj_pos + np.array([0., 0., 0.03])
        # If not above goal, move to be directly above goal
        elif np.linalg.norm(hand_pos[:2] - goal_pos[:2]) > 0.04:
            return 2, np.array([goal_pos[0], goal_pos[1], hand_pos[2]])
        else:
            return 3, goal_pos

    @staticmethod
    def _grab_effort(o_d):
        hand_pos = o_d['hand_pos']
        obj_pos = o_d['obj_pos']

        if np.linalg.norm(hand_pos[:2] - obj_pos[:2]) > 0.02 or abs(hand_pos[2] - obj_pos[2]) > 0.1:
            return 0.
        else:
            return 0.65
