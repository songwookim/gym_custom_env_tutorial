import gymnasium as gym
from stable_baselines3.common.env_checker import check_env
import halfcheetah_test

# env = HalfCheetahEnv(render_mode="human")
env = gym.make('halfcheetah_test/halfcheeatah_hello-v0',render_mode="human")
check_env(env)
