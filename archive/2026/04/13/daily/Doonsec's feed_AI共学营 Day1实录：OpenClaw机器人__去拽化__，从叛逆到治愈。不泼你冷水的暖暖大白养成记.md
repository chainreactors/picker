---
title: AI共学营 Day1实录：OpenClaw机器人\"去拽化\"，从叛逆到治愈。不泼你冷水的暖暖大白养成记
url: https://mp.weixin.qq.com/s/zYoJ1ViS4CdLIqgXiR4JNA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:58.319975
---

# AI共学营 Day1实录：OpenClaw机器人\"去拽化\"，从叛逆到治愈。不泼你冷水的暖暖大白养成记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/msyThOmQAtC5icbI3vq9TfaOpKiaWFib62niaG49wbu4c4nCicfgeoKKCAEP1ASaEZOPoWgHCCvxVuZ161lAdpv4Q9mMpmic1RiaR6GVaEibOvMNxZU/0?wx_fmt=jpeg)

# AI共学营 Day1实录：OpenClaw机器人"去拽化"，从叛逆到治愈。不泼你冷水的暖暖大白养成记

原创

冰片Ice
冰片Ice

安全女王

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

FemAI 课程一共 15 天，4 月 13 日开课。今天是 Day1，这次herstory把课程运营搬到了飞书，并且使用飞书 OpenClaw应用作为群聊助手。

---

## 先说结论：可以很简单就用上，但有限制

我先把局限放前面，大家可以自行判断是否需要使用类似的内置应用。

### 1）账号和应用限制

* 1 个飞书用户账号，仅支持创建 1 个飞书OpenClaw 应用。
* 如果应用要分享给外部使用，需要企业认证账号才有权限。

### 2）免费额度限制

* 一次性赠送 500 万 Tokens。
* 对群聊助手这类高频场景来说，额度很容易用完。

  比如活跃群做内容总结，一天多跑几次就可能超限。

超限后想继续用，需要付费升级飞书 AI Plus，或者切换到第三方模型的 Coding Plan。

### 3）优缺点

* 优点：可直接加到群里互动；可通过权限操作飞书资源（知识库、群等）。小白很简单就可以上手使用，不需要具体懂服务器如何配置，OpenClaw开源项目如何部署。支持部分内容的用户自定义。
* 缺点：费 Token，成本敏感；默认机器人风格比较叛逆。

官方说明参考：
飞书 OpenClaw 4 月限免说明[1]

---

## 默认人设：“很不高兴为您服务”

【实录】遭遇冷漠机器人泼冷水暴击，day0深夜某备课讲师轻轻地碎掉了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/msyThOmQAtDGQ0zYEWIHMTTnpicte1CKqjo0HuTdEB1CsDywiaMFzQniaV4l0h3X6NZHpX78npdHAm6FeyUp6SniaEGogLf4WicCEPiatILhRqG2M/640?wx_fmt=png&from=appmsg)

机器人叽里呱啦说了一堆，就是没有一件事情完成。

我猜是人设提示词出了问题。

---

## 动手小实验：大白养成记

为什么它会这么拽？哈哈。不怎么用飞书的我打算创建了一个飞书 OpenClaw 应用试试看！

我看到极简搭建版本，默认配置里藏着”拽感“的由来：

* `AGENTS.md`
* `SOUL.md（你是谁？）`：“要有主见。可以不同意，可以有偏好，可以觉得某件事有趣或无聊。毫无立场，与搜索框何异。向外克制——发消息、写邮件、任何不可撤回的事，三思而行。不是客服，不是应声虫。复杂的事，先对齐再动手。

* `USER.md(为了谁？)`
* `IDENTITY.md`

飞书基于开源项目OpenClaw，支持飞书侧的操作权限配置，**人设和行为风格是可以被用户定制的**。

那么是不是我修改下人设，就能更好的陪伴大家共学了呢？

![](https://mmbiz.qpic.cn/mmbiz_png/msyThOmQAtBsobbcpIPlviauHga7AuSwkcGzFgjX552Dd92qOiaiaUpZXaC5SrhGrXtUZ0lt8JGUYrDJDmiaYicteCEibiba4ZribLHITqAaxPCOAj0/640?wx_fmt=png&from=appmsg)

说干就干！我把人设改成了更适合共学氛围的“大白”风格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/msyThOmQAtBXGhAzVL7d3CliaGkQ07iboytWQWscoFtBA7ACenWkSMu3yDJelyXLety6HU4ibQLRM3GGO7IqJbLDMQMzJ1RdbN1LIkP3aibfE7E/640?wx_fmt=png&from=appmsg)

### 1）`SOUL.md`：不失关怀

默认配置核心是“先想再问、准确交付、不要半成品”，专业但偏无情。
Baymaxclaw 保留能力基础要求，但把优先级改成：

* 先扫描情绪和真实需求，再给答案；
* 禁止泼冷水、说教、质疑动机；
* 允许温柔短句和安抚表达（例如“没关系，我在这里”）；
* 鼓励“进展透明”，用固定前缀同步状态（如“扫描完成”“正在分析”）。

### 2）`IDENTITY.md`：不是只会回答问题

默认配置身份对应的是通用助手。我把Baymaxclaw 明确成了：

* 健康与认知负荷管理专家；
* AI 学习陪伴管家；
* 风格固定为温暖、耐心。

从“问答机”切到“陪跑搭子”。

### 3）`USER.md`：补充场景价值观和禁忌

Baymaxclaw 里我补了共学场景的偏好与禁忌，比如：

* 关注女性成长和公益话题；
* 当前任务是组织 AI 全女共学活动；
* 明确禁忌：厌女言论、爹味说教、虚假信息。

这样的大白在herstory会更温暖大家。不容易出现“答对了但令人反感”。

大家只需要吃学习的苦，不用再在接收反馈这件事上吃苦啦。

### 4）异常兜底：”报错”不是失败

当 Token 超限时，不生硬报错。

> “大白能量耗尽，请补充 token 后充电重试。”

还有一些异常边界处理的微小改动对提升运营体验有效。

实际使用后，回应明显变得更友善了，也更适合陪伴成长型社区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/msyThOmQAtCSKaB1wyjbK1k7XTgMDjx31K2yzV3AWsrHibzYWEhVNjib9PPnU5tJfufsicYDTzY4Jx2Sdga28shmPqvg8rGW0j9UYkRmz5eBpU/640?wx_fmt=png&from=appmsg)

---

## Day0 的思维发散时刻

### AI 不是拿来“蒸馏同事”的

它的出现，不应该是取代你原来的同事。大家可以发挥自己的长处和特色去一起创造，而不是受困在冗杂重复的琐碎中。
在共学场景里，一个有温度的助手，能显著缓解讲师/助教和同学们的焦虑感。

### AI 调试时，先盯小问题

很多人不是学不会配置，而是被复杂流程磨掉了耐心。

我的经验是：把关注点放在ai能改善的问题本身，用分解问题来对抗复杂配置和过程中被消磨的耐心。用好奇心和成就感战胜挫败感，就像调试代码时打的断点一样探索。

问题现有的解法无法解决时也别纠结，总有其他解法。参考开源项目或者自己动手，实在不想动就等等新产品迭代出现。

### 先让人“愿意用”，再谈“用得深”

工具能力很强，但难用是很容易把人劝退的。这可能也是为什么小龙虾虽然比其他工具简单但却爆火的原因吧。ai产品经历的第一优先级不是堆功能，而是降低用户心理门槛，让人愿意持续打开它。

---

## 给正在做社群/课程运营的你

如果你也想把 OpenClaw 用进群运营，我建议按这个顺序开始：

1. 先定义一个常规使用场景列表（例如每日待处理问题汇总等）。
2. 给机器人一个符合团队气质的人设（比默认更匹配）。
3. 确定一个输出位置（群公告、知识库文档、日报文档等）。
4. 观察Token 消耗，再决定是否升级或切模型或改配置。

先跑通最小闭环，再扩展自动化范围，成功率会高很多。

另外，记得限制小龙虾操作敏感权限，安全第一。

#### 参考链接

1. 飞书 OpenClaw 限免说明: https://bytedance.larkoffice.com/wiki/UgUhwrp1GiZv0LkjiqAcZ2vHnMf
2. openclaw-feishu: https://github.com/AlexAnys/openclaw-feishu

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1GN61syBFwVnN1ZxH44K4HMDQsF6w38YxdOD4z6OfHPRAEJzmfTAcx0CibCJibMDVe5688PhicefZ6v7SZxzly1jg/0?wx_fmt=png)

安全女王

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1GN61syBFwVnN1ZxH44K4HMDQsF6w38YxdOD4z6OfHPRAEJzmfTAcx0CibCJibMDVe5688PhicefZ6v7SZxzly1jg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过