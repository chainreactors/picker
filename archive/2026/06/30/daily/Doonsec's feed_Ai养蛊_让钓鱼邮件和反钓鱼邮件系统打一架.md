---
title: Ai养蛊:让钓鱼邮件和反钓鱼邮件系统打一架
url: https://mp.weixin.qq.com/s/_dtrxTxSM1A79ZFax12G6w
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:22:45.426329
---

# Ai养蛊:让钓鱼邮件和反钓鱼邮件系统打一架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkjXcDjibblaul2QPA5wmCStPkjGHXFKF2gicMnDJ2EBCibBgyXNicEl9zyFLDejJSJOrEbOzqAaZ8ibznOKHQFPQkibocvYo5aX5yG5k/0?wx_fmt=jpeg)

# Ai养蛊:让钓鱼邮件和反钓鱼邮件系统打一架

秋名山上的小柠
秋名山上的小柠

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## mab

多臂老虎机，又称为mab

同一个环境，动作，状态下有可能返回1，有可能返回0

也就是说环境反馈它不是一个固定的值

可以假设为有五个函数，也就是相当于五种反馈，第一个函数返回1的概率是20％，返回0的概率是80％

代码实现：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineimport numpy as npimport pandas as pd
class MultiArmedBandit:    def __init__(self, n_arms, true_rewards):        self.n_arms = n_arms        self.true_rewards = true_rewards        self.estimates = np.zeros(n_arms)  # 每个臂的奖励估计        self.action_counts = np.zeros(n_arms)  # 每个臂被选择的次数
    def select_arm(self, epsilon):        if np.random.rand() < epsilon:            return np.random.randint(self.n_arms)  # 探索        else:            return np.argmax(self.estimates)  # 开发
    def update_estimates(self, chosen_arm, reward):        self.action_counts[chosen_arm] += 1        # 更新奖励估计        self.estimates[chosen_arm] += (reward - self.estimates[chosen_arm]) / self.action_counts[chosen_arm]
def simulate_bandit(n_arms, true_rewards, n_rounds, epsilon):    bandit = MultiArmedBandit(n_arms, true_rewards)    rewards = np.zeros(n_rounds)    cumulative_rewards = np.zeros(n_rounds)
    for round in range(n_rounds):        chosen_arm = bandit.select_arm(epsilon)        reward = np.random.normal(true_rewards[chosen_arm], 1)  # 奖励是正态分布        bandit.update_estimates(chosen_arm, reward)        rewards[round] = reward        cumulative_rewards[round] = np.sum(rewards)
    return cumulative_rewards
# 参数设置n_arms = 5true_rewards = [1.0, 1.5, 2.0, 0.5, 1.2]  # 每个臂的真实奖励均值n_rounds = 1000epsilon = 0.1
cumulative_rewards = simulate_bandit(n_arms, true_rewards, n_rounds, epsilon)results_df = pd.DataFrame({    'Round': np.arange(1, n_rounds + 1),    'Cumulative Rewards': cumulative_rewards})
results_df
```

> 类定义：MultiArmedBandit

n\_arms   老虎机的数量

true\_rewards 每个臂的真实平均奖励

estimates 目前认为每个臂的平均回报是多少，初始全为0

action\_counts 记录每个臂被拉了多少次，用于更新均值

> 选择臂：select\_arm(self, epsilon)

然后定义一个随机数

以概率 ε 进行探索，也就是随机选一个臂，以概率 **1 - ε** 进行开发（选当前估计奖励最高的臂）。

比如说当 `epsilon = 0.1`：

* 10% 概率随机探索；
* 90% 概率选估计最好的那一个

> 更新估计值：update\_estimates()

![图片](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxY8icwFkycurPVpXNmhRDz8iarYXrbcsrk1FVeC4WE10ETkasS9L00n9LqGxEVrwlicc84FtYBM5GYw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

`R` 是这次的实际奖励；`N` 是该臂被选过的次数；`Q` 是对该臂期望奖励的估计

> 模拟函数：simulate\_bandit()

1. 初始化一个 `MultiArmedBandit` 实例；
2. 进行多轮（`n_rounds`）实验；
3. 每一轮：

* 用 `select_arm()` 决定拉哪一台机器；
* 根据真实均值 `true_rewards[chosen_arm]` 生成一个服从正态分布的奖励；
* 用 `update_estimates()` 更新估计；
* 记录当前的奖励和累计奖励

效果如图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxY8icwFkycurPVpXNmhRDz8iaDRzbcraRCvCdmnnwt9DuUfFibiaxaWcruibuibALaDEVhUAQjzTTvvK7A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

## ucb

UCB算法是一种用于解决探索与利用问题的策略选择方法，广泛应用于多臂老虎机问题

其核心思想是通过估计每个选项的潜在收益来平衡探索新选项和利用已知最佳选项 之间的权衡

基本原理 1. 探索与利用： 探索：尝试新的选项以获取更多的信息，利用：选择当前已知的最佳选项以最大化收益

2. UCB值计算： 对于每个选项，UCB算法计算一个上置信界值也就是UCB值，该值结合了成功率和探索因子

计算公式：

![图片](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxY8icwFkycurPVpXNmhRDz8h0WIgXEluvpdAbwCrG4w3icb6pz5eurxSeBvx2CibpQBfC27SqcHuFtQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

X\_i 是选项 i 的成功率,即平均收益; n 是当前总的尝试次数; n\_i 是选项 i 的尝试次数

第一项是指当前已知的平均成功率；第二项是指置信区间，也就是越没试过的策略，这项越大；比如说你去饭堂吃饭，吃过 10 次的店你知道它一般，但没吃过的店你可能会想试一试，这就是 UCB 的探索机制

应用场景 UCB算法广泛应用于在线广告推荐、A/B测试、动态定价、机器学习模型选择等领域，尤其是在需要实时决策和反馈的环境中

ucb的通俗解释：一个左撇子，用手拿东西的时候，用右手的概率是20% ，用左手的概率是80%由于第一次选择的时候左右都会选，但是概率不同，选择不同手的频率就会影响两边ubc（可以理解为Q表）的值 那么我们就可以根据两边受频率影响的值动态调整我们是否选择高的那边的概率

> 防火墙策略

假设有五个防火墙策略，并且拦截攻击的成功率都不一致

但是在实际项目中，不用都写出成功率出来，毕竟只要知道哪个防火墙拦截的成功率高，那肯定优先选择那个防火墙

现在是不知道概率多少

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineimport numpy as npimport pandas as pd
def check1(payload):    return np.random.rand() < 0.5  # 50%成功率
def check2(payload):    return np.random.rand() < 0.7  # 70%成功率
def check3(payload):    return np.random.rand() < 0.4  # 40%成功率
def check4(payload):    return np.random.rand() < 0.3  # 30%成功率
def check5(payload):    return np.random.rand() < 0.6  # 60%成功率
# 将所有检查函数放入列表中check_functions = [check1, check2, check3, check4, check5]
# 定义防火墙策略选择器类class FirewallPolicySelector:    def __init__(self, n_policies):        self.n_policies = n_policies        self.successes = np.zeros(n_policies)        self.attempts = np.zeros(n_policies)
    def select_policy(self):        total_attempts = np.sum(self.attempts)        if total_attempts == 0:            return np.random.randint(self.n_policies)  # 如果没有尝试过，随机选择        ucb_values = self.successes / (self.attempts + 1e-5) + np.sqrt(2 * np.log(total_attempts) / (self.attempts + 1e-5))        return np.argmax(ucb_values)  # 选择UCB值最高的策略
    def update(self, chosen_policy, success):        self.attempts[chosen_policy] += 1        self.successes[chosen_policy] += success
# 模拟防火墙策略优化过程def simulate_firewall(n_policies, n_rounds):    policy_selector = FirewallPolicySelector(n_policies)    results = []
    for round in range(n_rounds):        chosen_policy = policy_selector.select_policy()        payload = np.random.randint(0, 100)  # 生成随机攻击样本        success = check_functions[chosen_policy](payload)  # 使用选定的check函数        policy_selector.update(chosen_policy, success)        results.append((round + 1, chosen_policy, success))
    results_df = pd.DataFrame(results, columns=['轮次', '选择的策略', '成功拦截'])    return results_df
# 参数设置n_policies = len(check_functions)  # 策略数量n_rounds = 1000
# 运行模拟results_df = simulate_firewall(n_policies, n_rounds)
# 筛选出成功拦截的部分successful_results = results_df[results_df['成功拦截'] == 1]
# 输出每个策略的成功率print("\n每个策略的成功率：")print(results_df.groupby('选择的策略')['成功拦截'].mean())
# 显示成功拦截的结果print("\n成功拦截的结果：")print(successful_results)# 统计每个策略的选择次数policy_counts = results_df['选择的策略'].value_counts()
# 创建 DataFrame 显示所有策略及其选择次数result_df = pd.DataFrame({    '选择次数': policy_counts}).reset_index()
# 重命名列result_df.columns = ['选择的策略', '选择次数']
# 设置行标题result_df.index = [f'策略 {i+1}' for i in range(len(result_df))]result_df
```

> 防火墙策略选择器类 FirewallPolicySelector

`n_policies`: 策略数量;`successes[i]`: 第 i 个策略成功的次数;`attempts[i]`: 第 i 个策略被尝试的次数

> 策略选择核心 select\_policy()

这里用的ucb计算公式，在上述已贴出

> 模拟防火墙运行：simulate\_firewall()

循环共执行 `n_rounds`，比如 1000 轮：

选择一个策略，然后模拟生成攻击，接着判断是否成功拦截，最后更新策略统计

简单来说，这份代码就是模拟了一个基于UCB算法的自适应防火墙策略选择系统，它通过统计每个检测策略的历史成功率和尝试次数，自动在多轮攻击中选择最有效的策略，在“探索新方法”和“利用已知最优”之间取得平衡，最终趋向于选择拦截率最高的策略

效果如图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxY8icwFkycurPVpXNmhRDz8fickBGWoKlt87IU7IAFUGp7WDNeIjKrmYORa0...