import torch
import gym
import numpy as np
from stable_baselines3 import DQN
from contract_env import SmartContractEnv

# Create AI training environment
env = SmartContractEnv()

# Load Deep Q-Network (DQN) model
model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, buffer_size=50000, batch_size=64)

# Train AI agent on 1 million steps
model.learn(total_timesteps=1000000)


