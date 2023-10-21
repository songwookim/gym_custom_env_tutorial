from gymnasium.envs.registration import register

register(
    id="halfcheetah_test/halfcheeatah_hello-v0",
    entry_point="halfcheetah_test.envs:HalfCheetahEnv",
    max_episode_steps=1000,
    reward_threshold=4800.0,
)