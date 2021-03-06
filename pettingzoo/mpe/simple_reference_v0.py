from ._mpe_utils.simple_env import SimpleEnv, make_env
from .scenarios.simple_reference import Scenario


class raw_env(SimpleEnv):

    def __init__(self, seed=None, local_ratio=0.5, max_frames=100):
        assert 0. <= local_ratio <= 1., "local_ratio is a proportion. Must be between 0 and 1."
        scenario = Scenario()
        world = scenario.make_world()
        super().__init__(scenario, world, max_frames, seed, local_ratio)


env = make_env(raw_env)
