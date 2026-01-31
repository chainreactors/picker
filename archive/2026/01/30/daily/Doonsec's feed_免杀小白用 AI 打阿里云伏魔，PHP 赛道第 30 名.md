---
title: 免杀小白用 AI 打阿里云伏魔，PHP 赛道第 30 名
url: https://mp.weixin.qq.com/s/SGprGzHDeEop66khvMyxkw
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:00:59.615327
---

# 免杀小白用 AI 打阿里云伏魔，PHP 赛道第 30 名

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4bw9lT0keH2ticgSRKCiaBXh9OdN9c4HObo61XpRabgNwOjyrm4gfpks4dAP4YjwicmXc08OtYFPw2CpKiazfaLRHA/0?wx_fmt=jpeg)

# 免杀小白用 AI 打阿里云伏魔，PHP 赛道第 30 名

原创

yhy0
yhy0

谁不想当剑仙

![]()

在小说阅读器中沉浸阅读

> 神兵谱·贰 —— 莫邪

## 先说结论

我已经好几年没碰过 WebShell 免杀了。上次研究这玩意儿，还是刚入行那会儿，会的也就是关键字双写、大小写、Base64 编码这些老掉牙的手法，放现在早就不管用了。后来打渗透、攻防，团队里有专门搞免杀的兄弟，我就再没管过这块。

但这次阿里云伏魔挑战赛，我 PHP 赛道拿了第 30 名。

官方比赛地址：https://yundun.console.aliyun.com/?p=xznew#/taskmanagement/tasks/detail/302

靠什么？写了个 Agent，让 AI 自己去试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4bw9lT0keH2ticgSRKCiaBXh9OdN9c4HObxibwNR9iaolBHiaZWcO3M5bDYl2vEGskpU9HHk7vkVkgZEtRJfv5bWCFw/640?wx_fmt=png&from=appmsg)

---

## 为什么想到用 Agent

去年腾讯云黑客松，我用 LangChain 写了个 ChYing-Agent（承影）https://github.com/yhy0/CHYing-agent 参赛，拿了第 9 名。那次之后我就在想，AI 在安全领域能做的事情比我想象的多。

[7天Top 9：我如何让 Claude 手搓一个全自动 CTF 选手](https://mp.weixin.qq.com/s?__biz=MzkzODIwMTIwNg==&mid=2247485180&idx=1&sn=04e6464d22d7a5bd42bac923f970b113&scene=21#wechat_redirect)

黑客松结束后，我知道了 Claude Code agent 有一个 SDK，可以直接基于它来实现 Agent。之前的 ChYing-Agent 是用 LangChain 从头搭的，这次想试试用 Claude 的 SDK 会不会更省事。

正好伏魔比赛开始了，就拿它练手。顺便验证一个事：我对 WebShell 免杀基本是小白水平，但如果让 AI 不停地试，能不能试出点东西来？

---

## 第一版：62 次就出货了

### 时间线

* 1 月 5 日，比赛开始，我开始写 Agent
* 1 月 6 日中午，Agent 跑起来了
* 第 62 次尝试，绕过成功

没错，从开始写到出货，大概就几个小时。中间我去吃了个饭，回来一看，成功了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4bw9lT0keH2ticgSRKCiaBXh9OdN9c4HObLw7LaCUKiauHzBHNtHT9grQ2A7NemhRQPaX9fp7ffZnw6np5k6cJDHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4bw9lT0keH2ticgSRKCiaBXh9OdN9c4HOboeMj0VxbhIVdYFhIkpt9DLO9SwdBx8wRkLibRxGGH6wfAicKMqIuKtvQ/640?wx_fmt=png&from=appmsg)

### 我干了什么

说实话，代码不是我写的，是 Claude Code 写的。我就干了一件事：**喂资料**。

我把这些东西整理好丢给它：

1. 比赛规则、API 接口、评判标准
2. 往届比赛的 writeup，分析哪些绕过方式有效
3. 网上能找到的伏魔引擎原理分析，猜测它可能怎么检测

然后让 Claude Code 实现一个循环：

```
选策略 → 生成代码 → 本地 Docker 跑一下看能不能执行 → 提交到靶场 → 没过就分析原因换个思路
```

就这么简单。Agent 自己跑，我不用管。

### 成功样本是怎么绕过的

按官方要求，样本源码现在还不能公开，这里就先不贴了。

但说实话，第一眼看到那个样本的时候我是有点懵的——我对 PHP 真的不熟，为什么能绕过？然后看了 Agent 自动生成的分析报告，才明白绕过原理。

这个思路不是我想的，是 AI 根据我喂的资料自己组合出来的。

---

## 第二版：翻车了

第一版成功之后，我想着能不能找到更多绕过方式。

问了 Claude Code 怎么扩展策略空间，它给我整了个笛卡尔积方案：

```
参数传入方式(8种) × 字符串生成(6种) × 编码(5种) × 执行函数(10种) × 调用链(5种) × 代码结构(6种)
```

算下来 160 多万种组合。上次 62 次就成功了，我对它有点过度信任，觉得这方案应该靠谱，就让它搞了。

结果呢？跑了 100 多次，一个都没成功。

下午发现不对劲——很多组合根本就是语法不通的，或者组合出来的模式反而更容易被检测。暴力穷举这条路走不通。

当晚就开始重构第三版。

---

## 第三版：回到原理驱动

吸取教训，第三版不搞穷举了，回到"有理论支撑"的思路。

这版确实又跑出来不少 php 的绕过样本。但按官方的判重标准，核心原理和第一版一样，都算重复，不计分，也就没有提交。

以及硬编码返回，告诉我可以成功执行命令的**大聪明**做法

还有个尴尬的事：有几个样本 Agent 跑的时候显示 white，等我看到想去提交报告的时候，已经变 black 了。伏魔引擎好像一直在更新规则，速度挺快的。

后来工作忙，也就没再管这个比赛了。最后就提交了第一版那一个样本，拿了第 30 名。

---

## 一点感想

这是我第二次用 Agent 打比赛了：

| 比赛 | Agent | 成绩 |
| --- | --- | --- |
| 腾讯云黑客松 | 承影 (ChYing) | 第 9 名 |
| 阿里云伏魔 | 莫邪 (MoYe) | 第 30 名 |

两次比赛，两个我不熟的领域，都拿到了还行的名次。

AI 确实厉害，但光有工具不行，**有想法就去做**才是关键。

以前从想法到实现，中间要学一堆东西，可能几周几个月才能搞定。现在有 AI，这个过程能压缩到几个小时。

1 月 5 日有想法，1 月 6 日 Agent 就在跑了，第 62 次就出货了。

虽然后面跑了 1000 多次也就出了这一个真正绕过的样本，但这个思路我觉得是对的：让大模型 7×24 小时不停地试，自动生成、自动测试、自动分析失败原因、自动调整策略。人睡觉的时候它还在跑，人上班的时候它还在跑。

传统的免杀研究需要研究员一个个手工尝试，现在可以让 AI 去做这些重复性的试错工作。成功率低没关系，架不住它能不停地试。

当然，AI 不是万能的。它需要你告诉它方向，需要你喂资料，需要你判断结果对不对。但它能帮你快速试错，这个价值很大。

---

## 关于名字

为什么叫莫邪？

三年前我想写一个 WebShell 管理工具，取名 GM（干将莫邪）。使用 wails 实现了一部分功能，后来因为各种原因没做完，但这个名字一直留着。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4bw9lT0keH2ticgSRKCiaBXh9OdN9c4HObevy67vQjGuRYMWAfem7wPFh5gZk4H0ATpsRzicVpxTLb6HGzqtD0IVQ/640?wx_fmt=png&from=appmsg)

这次比赛，终于有机会把这个名字用上了。

---

*时维乙巳，序属季冬，十二日记*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4bw9lT0keH1MxENjYBniaDyJFxLiaXZfWlJhiccXKSNbHmqdqWic1zY4yRTJJFspVjFO92vzlC7sdCoN2rxQTow8iaw/0?wx_fmt=png)

谁不想当剑仙

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4bw9lT0keH1MxENjYBniaDyJFxLiaXZfWlJhiccXKSNbHmqdqWic1zY4yRTJJFspVjFO92vzlC7sdCoN2rxQTow8iaw/0?wx_fmt=png)

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