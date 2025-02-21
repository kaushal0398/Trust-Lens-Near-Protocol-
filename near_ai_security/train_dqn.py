import torch
import gym
import numpy as np
from stable_baselines3 import DQN
from contract_env import SmartContractEnv

# Create AI training environment
env = SmartContractEnv()

