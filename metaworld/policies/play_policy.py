import numpy as np

from metaworld.policies.action import Action
from metaworld.policies.policy import Policy, move


class PlayPolicy(Policy):
    def __init__(self, base_policy_class, counter_max=100, grip_flip_p=0.005):
        self.base_policy = base_policy_class()
        self.counter_max = counter_max
        self.grip_flip_p = grip_flip_p
        self.reset()

    @property
    def current_stage(self):
        return self._current_stage

    def _parse_obs(self, obs):
        return self.base_policy._parse_obs(obs)

    # Reset at the beginning of each episode
    def reset(self):
        self.switch_stage = np.random.choice(self.base_policy.num_stages)
        self._current_stage = None
        self.set_goal(None)
        self._hold_grab_effort = None

    def set_goal(self, goal):
        self._current_goal = goal
        self._counter = 0

    def set_random_goal(self):
        self.set_goal(self.base_policy.sample_xyz())

    def _desired_pos(self, o_d):
        if self._current_goal is None:
            self._current_stage, goal = self.base_policy._desired_pos(o_d)
            if self._current_stage == self.switch_stage:
                print(f'Reached switch stage ({self.switch_stage})!')
                self.set_random_goal()
                self._current_stage = 'play'

                # Save current grab effort to apply while moving around
                self._hold_grab_effort = self.base_policy._grab_effort(o_d)
            else:
                return goal
        else:
            if self._counter == self.counter_max:
                self.set_random_goal()
            else:
                self._counter += 1
        return self._current_goal

    def _grab_effort(self, o_d):
        if self._hold_grab_effort is None:
            return self.base_policy._grab_effort(o_d)
        else:
            # With probability grip_flip_p, switch gripper open/close
            if np.random.random() < self.grip_flip_p:
                self._hold_grab_effort = 1.0 if self._hold_grab_effort < 0 else -1.0

            return self._hold_grab_effort

    def get_action(self, obs):
        o_d = self._parse_obs(obs)

        pos = self._desired_pos(o_d)
        grab_effort = self._grab_effort(o_d)

        action = Action({
            'delta_pos': np.arange(3),
            'grab_effort': 3
        })
        action['delta_pos'] = move(o_d['hand_pos'], to_xyz=pos, p=self.base_policy.p),
        action['grab_effort'] = grab_effort

        return action.array