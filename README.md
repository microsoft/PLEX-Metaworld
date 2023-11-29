# PLEX-Metaworld


PLEX-Metaworld is a version of a flavor of Meta-World v2 that was used in the experiments of the [PLEX architecture paper](https://microsoft.github.io/PLEX/) and is installed as a dependency of [PLEX](https://github.com/microsoft/PLEX). PLEX-Metaworld was created by forking the original Meta-World at commit `a0009ed`. PLEX-Metaworld's main difference from the original Meta-World is a wrapper for Meta-World tasks that returns pixel observations, proprioceptive states and, optionally, depth maps as observations.

For more background information on Meta-World, please refer to the Meta-World [website](https://meta-world.github.io) and the accompanying [conference publication](https://arxiv.org/abs/1910.10897).

__Table of Contents__
- [Installation](#installation)
- [Using PLEX-Metaworld](#using-plex-metaworld)
  * [Seeding a benchmark instance](#seeding-a-benchmark-instance)
  * [Constructing a single-task PLEX-Metaworld environment](#constructing-a-single-task-plex-metaworld-environment)
  * [Recording demonstrations from a scripted policy for a given PLEX-MetaWorld task](#recording-demonstrations-from-a-scripted-policy-for-a-given-plex-metaworld-task)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [Trademarks](#trademarks)



## Installation

Meta-World is based on MuJoCo, which has a proprietary dependency we can't set up for you. Please follow the [instructions](https://github.com/openai/mujoco-py#install-mujoco) in the mujoco-py package for help. Once you're ready to install everything, run:

```
pip install metaworld@git+https://github.com/microsoft/PLEX-MetaWorld
```

Alternatively, you can clone the repository and install an editable version locally:

```
git clone https://github.com/microsoft/PLEX-MetaWorld.git
cd metaworld
pip install -e .
```

## Using PLEX-Metaworld


### Seeding a benchmark instance
For the purposes of reproducibility, it may be important to you to seed your benchmark instance.
You can do so in the following way:
```python
import metaworld

SEED = 0  # some seed number here
benchmark = metaworld.BENCHMARK(seed=SEED)
```


### Constructing a single-task PLEX-Metaworld environment

See the [metaworld.mw_gym_make(.)](https://github.com/microsoft/PLEX-Metaworld/blob/23922e14e65ddad0f9681bf4d2932700ef85a2e4/metaworld/__init__.py#L362) method. For an example of how to use it, see the [data/training_data_gen.py](https://github.com/microsoft/PLEX-Metaworld/blob/23922e14e65ddad0f9681bf4d2932700ef85a2e4/metaworld/data/training_data_gen.py#L68) script.


### Recording demonstrations from a scripted policy for a given PLEX-Metaworld task

See the [data/training_data_gen.py](https://github.com/microsoft/PLEX-Metaworld/blob/23922e14e65ddad0f9681bf4d2932700ef85a2e4/metaworld/data/training_data_gen.py#L68) script.


## Acknowledgements

The original Meta-World was a work by [Tianhe Yu (Stanford University)](https://cs.stanford.edu/~tianheyu/), [Deirdre Quillen (UC Berkeley)](https://scholar.google.com/citations?user=eDQsOFMAAAAJ&hl=en), [Zhanpeng He (Columbia University)](https://zhanpenghe.github.io), [Ryan Julian (University of Southern California)](https://ryanjulian.me), [Karol Hausman (Google AI)](https://karolhausman.github.io),  [Chelsea Finn (Stanford University)](https://ai.stanford.edu/~cbfinn/) and [Sergey Levine (UC Berkeley)](https://people.eecs.berkeley.edu/~svlevine/). Currently, the canonical Meta-World version is maintained by [Farama Foundation](https://github.com/Farama-Foundation/Metaworld).

In turn, the code for Meta-World was originally based on [multiworld](https://github.com/vitchyr/multiworld), which is developed by [Vitchyr H. Pong](https://people.eecs.berkeley.edu/~vitchyr/), [Murtaza Dalal](https://github.com/mdalal2020), [Ashvin Nair](http://ashvin.me/), [Shikhar Bahl](https://shikharbahl.github.io), [Steven Lin](https://github.com/stevenlin1111), [Soroush Nasiriany](http://snasiriany.me/), [Kristian Hartikainen](https://hartikainen.github.io/) and [Coline Devin](https://github.com/cdevin). The Meta-World authors are grateful for their efforts on providing such a great framework as a foundation of our work. We also would like to thank Russell Mendonca for his work on reward functions for some of the environments.


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
