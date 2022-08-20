import numpy as np
import matplotlib.pyplot as plt
import gym
import gym_minigrid
from gym_minigrid.wrappers import RGBImgPartialObsWrapper, ImgObsWrapper, RGBImgObsWrapper, FullyObsWrapper, ViewSizeWrapper

env = gym.make('MiniGrid-Empty-5x5-v0')
env = FullyObsWrapper(env)
obs = env.reset()
plt.imshow(obs['image'])
print(1)