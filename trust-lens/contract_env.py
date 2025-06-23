import gym
import torch
import numpy as np
from gym import spaces

class SmartContractEnv(gym.Env):
    """Custom Reinforcement Learning Environment for Smart Contract Security"""
    
    def __init__(self):
        super(SmartContractEnv, self).__init__()
        self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)
        self.action_space = spaces.Discrete(3)  # 3 Actions: Safe, Medium Risk, High Risk
        self.state = np.random.rand(10)  # Randomized contract security features
        self.contracts_scanned = 0

    def step(self, action):
        """Simulate AI detecting vulnerabilities"""
        reward = -1  # Default penalty
        if action == 2:  # High-risk contracts
            reward = 10 if np.sum(self.state) > 5 else -5  # Reward if detected correctly
        elif action == 1:  # Medium-risk contracts
            reward = 5 if 3 < np.sum(self.state) <= 5 else -2
        elif action == 0:  # Safe contracts
            reward = 10 if np.sum(self.state) <= 3 else -3

        self.state = np.random.rand(10)  # Generate new contract features
        self.contracts_scanned += 1
        done = self.contracts_scanned >= 1000  # Stop training after 1000 iterations

        return self.state, reward, done, {}

    def reset(self):
        """Reset environment after training episode"""
        self.state = np.random.rand(10)
        self.contracts_scanned = 0
        return self.state
