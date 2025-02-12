class StaticFns:
    @staticmethod
    def termination_fn(obs, act, next_obs):
        #assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2
        # baseically never ends.
        done = (obs[:, 0] == 0)
        return done
