import torch
import gym
import numpy as np
from stable_baselines3 import DQN
from contract_env import SmartContractEnv

env = SmartContractEnv()

model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, buffer_size=50000, batch_size=64)

model.learn(total_timesteps=1000000)

model.save("smart_contract_auditor_dqn")
print("Training complete! AI auditor model saved.")
