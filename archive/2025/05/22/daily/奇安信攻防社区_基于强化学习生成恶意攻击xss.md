---
title: 基于强化学习生成恶意攻击xss
url: https://forum.butian.net/share/4305
source: 奇安信攻防社区
date: 2025-05-22
fetch_date: 2025-10-06T22:23:16.440100
---

# 基于强化学习生成恶意攻击xss

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 基于强化学习生成恶意攻击xss

本文提出了一种基于DQN强化学习的XSS载荷自动生成方法，通过神经网络替代Q表格，结合经验回放和目标网络优化训练。系统包含特征提取（257维向量）、WAF检测（正则规则）和免杀变形（6种字符级操作）三大模块，在Gym框架下实现智能体与WAF的对抗训练。实验表明，经过100轮训练后，智能体可生成有效绕过WAF的XSS载荷，为AI驱动的Web安全测试提供了新思路。

基于强化学习的DQN智能体自动生成XSS
====================
前言
--
本文提出了一种基于DQN强化学习的XSS载荷自动生成方法，通过神经网络替代Q表格，结合经验回放和目标网络优化训练。系统包含特征提取（257维向量）、WAF检测（正则规则）和免杀变形（6种字符级操作）三大模块，在Gym框架下实现智能体与WAF的对抗训练。实验表明，经过100轮训练后，智能体可生成有效绕过WAF的XSS载荷，为AI驱动的Web安全测试提供了新思路。
Q learning 和 DQN
----------------
最开始我们还是来细细了解一下原理吧
### Q learning
DQN实际上就是Q learning+network
那先来看看Q learning，公式如下：
![IjkfKD2oGOEMASu.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e7eda130bb7eae3032c3e93b333fdc1829fd1bde.png)
```php
Q(S\_t, A\_t)即当前状态下动作A\_t的Q值,为待更新值
alpha即学习率
R\_t+1即奖励值
Gamma代表折扣率
Q(S\_t+1,a)代表下一状态选择动作a的Q值
```
Q learning和DQN的区别在于，Q learning的Q值是用Q表格来储存的，DQN使用神经网络来储存的
\*\*Q learning的工作流程大概：\*\*
​ 1.初始化：Q值通常开始随机被初始化，然后在训练的过程中更新
​ 2.探索与利用：在每个时间步智能体都要选择一个动作。这里使用epsilon-greedy策略来完成，该方法会在随机选择动作和选择但前最高Q值的动作之间权衡
​ 3.学习更新：一旦智能体选择了一个行动，环境返回了结果，智能体会根据结果，基于贝尔曼公式和时序差分来更新Q值
那我们来看看Q learning简单的代码实现
```py
import numpy as np
import pandas as pd
class QLearningTable:
def \_\_init\_\_(self, actions, learning\_rate=0.01, reward\_decay=0.9, e\_greedy=0.9):
self.actions = actions # a list
self.lr = learning\_rate
self.gamma = reward\_decay
self.epsilon = e\_greedy
self.q\_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
def choose\_action(self, observation):
self.check\_state\_exist(observation)
if np.random.uniform() < self.epsilon:
state\_action = self.q\_table.loc[observation, :]
action = np.random.choice(state\_action[state\_action == np.max(state\_action)].index)
else:
action = np.random.choice(self.actions)
return action
def learn(self, s, a, r, s\_):
self.check\_state\_exist(s\_)
q\_predict = self.q\_table.loc[s, a]
if s\_ != 'terminal':
q\_target = r + self.gamma \* self.q\_table.loc[s\_, :].max()
else:
q\_target = r
self.q\_table.loc[s, a] += self.lr \* (q\_target - q\_predict)
# 这个没什么好说的就是建立Q值表
def check\_state\_exist(self, state):
if state not in self.q\_table.index:
self.q\_table=pd.concat([
self.q\_table,
pd.DataFrame([[0]\*len(self.actions)], columns=self.q\_table.columns, index=[state])
])
```
可以看到
```py
def choose\_action(self, observation):
self.check\_state\_exist(observation)
if np.random.uniform() < self.epsilon:
state\_action = self.q\_table.loc[observation, :]
action = np.random.choice(state\_action[state\_action == np.max(state\_action)].index)
else:
action = np.random.choice(self.actions)
return action
```
在实现选择动作着这个函数这里，可以看到epsilon-greedy策略，如果随机数小于epsilon，那就选择基于当前状态下Q值最大的那个动作，否则就是随机选择一个动作并返回
```py
def learn(self, s, a, r, s\_):
self.check\_state\_exist(s\_)
q\_predict = self.q\_table.loc[s, a]
if s\_ != 'terminal':
q\_target = r + self.gamma \* self.q\_table.loc[s\_, :].max()
else:
q\_target = r
self.q\_table.loc[s, a] += self.lr \* (q\_target - q\_predict)
```
这段代码就是公式![IjkfKD2oGOEMASu.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e7eda130bb7eae3032c3e93b333fdc1829fd1bde.png)
的具体实现过程，让我着重关注一下q\\_target和q\\_predict，q\\_target 是下一个状态的最大Q值，q\\_predict是当前状态的Q值，这个公式的目的就是使当前状态尽可能的去你和下一状态，计算下一状态和当前状态Q值的差，再乘以折扣率Gamma（即是这个误差存在一定损失），再乘上学习率alpha，这样就可以逐步的去拟合下一状态的Q值，讲到这里是不是有神经网络梯度下降那味儿了
### DQN
在传统的Q-learning中，我们用一个表（Q-table）来存储每个状态-动作对的Q值。然而，当状态和动作的数量非常大时，用表格存储的方式就会变得不现实，因为需要的存储空间和计算资源会非常巨大
那就顺势提出了使用神经网络来充当Q值函数，通过这种方式，我们就可以在连续的状态空间和大规模的动作空间中工作
提到DQN就不得不提提他的两个关键技术：
​ 1.经验回放\*\*（Experience Replay）\*\*：为了打破数据之间的关联性和提高学习效率，DQN会将智能体的经验（状态、动作、奖励、新状态、新动作）储存起来，之后从中随机抽样进行学习
​ 2.\*\*目标网络（Target Network）\*\*：DQN使用了两个神经网络，一个是在线网络，用于选择动作；一个是目标网络，用于计算TD目标（Temporal-Difference Target），这两个网络的结构是完全一样的，只是参数不同，在学习过程中，每个一段时间，会用在线网络的参数去更新目标网络
怎么理解这个target network呢？我这里引用两个师傅的例子
A.把在线网络做一只猫。把监督数据 Q Target 看做是一只老鼠，现在可以把训练的过程看做猫捉老鼠的过程（不断减少之间的距离，类比于在线网络拟合 Q Target 的过程）。现在问题是猫和老鼠都在移动，这样猫想要捉住老鼠是比较困难的
那么让老鼠在一段时间间隔内不动（固定住），而这期间，猫是可以动的，这样就比较容易抓住老鼠了。在 DQN 中也是这样解决的，有两套一样的网络，分别是 在线网络和 Q Target 网络。要做的就是固定住 Q target 网络，那如何固定呢？比如可以让 在线网路训练10次，然后把 在线 网络更新后的参数 w 赋给 Q target 网络。然后再让在线网路训练10次，如此往复下去，试想如果不固定 Q Target 网络，两个网络都在不停地变化，这样 拟合是很困难的，如果让 Q Target 网络参数一段时间固定不变，那么拟合过程就会容易很多
B.同样的道理，把在线网络去拟合target网络这个过程比作是打靶，如果靶子一直动来动去，那肯定加大了打中的难度，那我们使用target网络把靶子固定起来，那打中的概率是不是就会大很多了呢
介绍一下DQN的整体工作流程：
其实就是在线网络和目标网络的相互配合
1.\*\*在线网络训练\*\*：在线网络和环境交互，在线网络执行了一个动作，环境会返回（状态、动作、奖励、新状态、新动作）然后使用这些数据来更新网络参数，我们希望在线网络的预测值接近于目标值，我们可以使用梯度下降算法来最小化在线网络预测的Q值和目标网络的目标值之间的差距（通常使用平方损失函数）。
![FZt1Hq2438Glywb.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e241d6ae4e53852ae597a5dc5f6e9f9750de719e.png)
Q值的更新公式为：
```powershell
Q(S\_t, A\_t) = r + γ \* max(Q\_target(S\_t+1, A\_t+1))
```
\*\*DQN工作的整体流程：\*\*
​ 1.初始化：初始化在线网络和目标网络，创建一个经验回放储存区
​ 2.探索与利用：在每个时间步智能体都要选择一个动作。这里使用epsilon-greedy策略来完成，该方法会在随机选择动作和选择但前最高Q值的动作之间权衡
​ 3.交互与储存：智能体与环境进行交互，产生的（状态、动作、奖励、新状态、新动作）储存在经验回放区中
​ 4.学习：从经验回放储存区中随机抽取一些样本来训练在线网络，通过最小化网络预测的Q值和这个目标值之间的差距来更新网络的参数
​ 5.更新网络：每个一定的时间会将在线网络的参数直接拷贝给目标网络，是目标网络的参数保持相对稳定，使学习过程更相对稳定
​ 6.迭代：重复2～5步骤
最后贴一下我项目的部分代码吧
```py
import tensorflow as tf
import gym
from envs.env import Env
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers.legacy import Adam
class DQNAgent:
def \_\_init\_\_(self, state\_size, action\_size, learning\_rate=0.001, gamma=0.95, epsilon=0.9, epsilon\_decay=0.995,
epsilon\_min=0.01, update\_target\_freq=10):
self.state\_size = state\_size
self.action\_size = action\_size
self.memory = []
self.gamma = gamma # 折扣因子
self.epsilon = epsilon # 探索率
self.epsilon\_decay = epsilon\_decay
self.epsilon\_min = epsilon\_min
self.learning\_rate = learning\_rate
self.update\_target\_freq = update\_target\_freq # 目标网络更新频率
self.model = self.build\_model() # 在线网络（Q 网络）
self.target\_model = self.build\_model() # 目标网络
self.target\_model.set\_weights(self.model.get\_weights()) # 初始化目标网络权重
self.train\_step = 0
def build\_model(self):
model = Sequential([
Input(shape=(self.state\_size,)),
Dense(64, activation='relu'),
Dense(64, activation='relu'),
Dense(self.action\_size, activation='linear')
])
model.compile(loss='mse', optimizer=Adam(learning\_rate=self.learning\_rate))
return model
def remember(self, state, action, reward, next\_state, done):
self.memory.append((state, action, reward, next\_state, done))
def act(self, state):
if np.random.rand() <= self.epsilon:
return np.random.choice(self.action\_size)
act\_values = self.model.predict(state, verbose=0)
return np.argmax(act\_values[0]) # 选择 Q 值最大的动作
def replay(self, batch\_size):
minibatch = np.random.choice(len(self.memory), batch\_size, replace=False) # 随机选取 batch\_size 个样本
for idx in minibatch:
state, action, reward, next\_state, done = self.memory[idx]
# Double DQN：用在线网络选择动作
next\_action = np.argmax(self.model.predict(next\_state, verbose=0)[0])
# 用目标网络计算 Q 值
target\_q\_value = self.target\_model.predict(next\_state, verbose=0)[0][next\_action]
# 计算目标 Q 值
target = reward if done else reward + self.gamma \* target\_q\_value
# 计算新 Q 值
target\_f = self.model.predict(state, verbose=0)
target\_f[0][action] = target
# 训练模型
self.model.fit(state, target\_f, epochs=1, verbose=0)
# \*\*减少探索率\*\*
if self.epsilon > self.epsilon\_min:
self.epsilon \*= self.epsilon\_decay
# \*\*定期更新目标网络\*\*
self.train\_step += 1
if self.train\_step % self.update\_target\_freq == 0:
self.target\_model.set\_weights(...