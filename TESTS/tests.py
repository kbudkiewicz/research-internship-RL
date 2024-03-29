import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as tfunc
import gym
env = gym.make("LunarLander-v2")
from collections import deque, namedtuple

### This file is for testing/learning pytorch and gym functions and how to apply them correctly

### Loop testing whether a condition in the environment (both legs touching the ground // True) is met. Then break the loop and return total score
# total_reward = 0.0
# total_steps = 0
# env.reset()
# while True:
#     action = env.action_space.sample()
#     obs, reward, f1 ,f2, _ = env.step(action)
#     total_reward += reward
#     total_steps += 1
#     if f1 and f2 == True:
#         break
# print("Episode done in %d steps. Total score: %s" % (total_steps,total_reward))

# m = nn.Softmax(dim=1)
# input = torch.randn(2,3)
# print(input, m(input), sep="\n")

### Environment of the Lunar Lander
# env = gym.make("LunarLander-v2")
# obs = env.reset(seed=0)
# print(env.step(0),"\nLength: ", len(env.step(0)))
# print(obs, "\n")
# print(env.action_space)
# action = env.action_space.sample()
# print(action, "\n")
# print(env.observation_space)
# print(env.step(0))

### squeeze(), flatten() as opposites
# x = torch.tensor([1,2,3,4])
# x = torch.unsqueeze(x,1)
# x = torch.unsqueeze(x,0)
# print(x)
# x = torch.flatten(x)
# x = torch.flatten(x)
# print(x)

### handling of PyTroch NN
N1 = nn.Linear(8, 16)
N2 = nn.Linear(16,4)
input = torch.from_numpy( gym.make('LunarLander-v2').reset()[0] )
print('State from reset environment:\n', input)
output = N1(input)
print('\nState in between the NN:\n', output)
output = N2(output)
print('\nOutput of the NN:\n', output)

### torch.from_numpy() - convert a numpy array into a torch.tensor()

### neural networks
# net = nn.Linear(6, 30)
# net2 = nn.Linear(30,2)
# T = torch.randn(2, 6)
# T2 = torch.tensor([[1,2,3,4,5,6],[-1,2,-3,4,-5,6]])
# print('\nTensor with ReLU applied:')
# T = tfunc.relu(T)
# T2 = tfunc.relu(T2)
# print(T, '\n',T2)
# print('\nTensor goes through NN:')
# print( net(T) )
# print( net2( net(T) ) )
# # print( net(T2) )
# print('\nReLU applied to NN:')
# print( tfunc.relu( net(T) ) )

### putting values into a tensor
# memory = namedtuple('Memory',('s','a','r','s_next'))
# brain = []
# for i in range(10):
#     state = env.reset()
#     obs, r, _, _, _ = env.step(1)
#     brain.append(memory(state, 1, r, obs))
# print('Brain content:')
# for i in brain:
#     print(i)
#
# T = torch.randn(10,8)
# net = nn.Linear(8,32)
# net2 = nn.Linear(32,4)
# print(net2(net(T)))

# print(brain.__class__)
# for i in range( len(brain) ):
#     T[i] = torch.tensor( brain[i].s_next )
# print('\nNew T:\n', T)

# net1 = nn.Linear(4,32)
# net2 = nn.Linear(32,32)
# net3 = nn.Linear(32,6)
# T = torch.rand(5,4)
# a = torch.randn(5).unsqueeze(1).long().abs()
# print('T: ',T)
# TT = net3(net2(net1(T)))
# print( 'T -> NN -> T: \n', TT)
# print( TT.gather(1, a) )
#
# print( torch.max(TT, dim=1)[0] )

##### Gym
import gym
env = gym.make("LunarLander-v2")

# observation, info = env.reset(seed=0)
# print(observation, "\n", info)

for runs in range(3):
    env.reset()
    for i in range(1000):
        observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
        # print("Obs: %s\nr = %s\nTerm: %s\nTrunc: %s\nInfo: %s"%(observation,reward,terminated,truncated,info))

        if terminated:
            break

### multiplying tensors
# T1 = torch.tensor(np.eye(5))
# print(T1)
# for i in range(5):
#     for j in range(5):
#         T1[i] = j
# print(T1.size())
# T2 = torch.tensor([1,2,3,4,5])#.unsqueeze(1)
# print(1 - T2)
# T3 = T1 * T2
# print(T3.size(), T3)