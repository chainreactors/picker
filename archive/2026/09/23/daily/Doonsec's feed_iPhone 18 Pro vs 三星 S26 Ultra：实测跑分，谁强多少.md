---
title: iPhone 18 Pro vs 三星 S26 Ultra：实测跑分，谁强多少
url: https://mp.weixin.qq.com/s/RqMhHhRrYq8KoRbImo-ArA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:57:40.916370
---

# iPhone 18 Pro vs 三星 S26 Ultra：实测跑分，谁强多少

# iPhone 18 Pro vs 三星 S26 Ultra：实测跑分，谁强多少

梓陌说科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

别看厂商怎么吹。梓陌 跑了实测，结论有惊喜，也有反常识。

最近「iPhone 18 Pro 和三星 S26 Ultra 谁更快」的对比视频又冒出来一拨。

有人秒开应用快半秒，有人加载网页快几帧。看着都挺热闹，但都是「我的方法最厉害」的循环论证。

这次不一样。Tom's Guide 拿两台量产机，做了完整跑分。
今天不站队，把数据摆出来，谁强哪儿、强多少，**以及一处你可能没想到的反常识结论**。

---

## 一、CPU 部分：iPhone 全线领先

A20 Pro 这代，账面升级很猛：两个性能核心比上代快 20%，四颗能效核心，7 核 GPU（上一代是 6 核），神经网络引擎从 16 核翻到 32 核。

Geekbench 6 是行业里最常被引用的综合跑分，数字如下：

| 机型 | 单核 | 多核 |
| --- | --- | --- |
| **iPhone 18 Pro** | 4,735 | 12,800 |
| **iPhone 18 Pro Max** | 4,741 | 12,789 |
| **Galaxy S26 Ultra** | 3,785 | 11,563 |
| **iPhone 17 Pro（上代）** | 3,834 | 9,988 |

几个能用的结论：

* **单核方面**

  ，iPhone 18 Pro 比 S26 Ultra 高 **25%**，比自家上代也提升 25%
* **多核方面**

  ，iPhone 18 Pro 比 S26 Ultra 高 **10%**，比自家上代提升 28%
* 这一代 iPhone 比上一代提升幅度，比三星旗舰之间的代差还大

Apple Silicon 在单核上一骑绝尘，这事持续很多代，没什么意外。
真正有意思的是下面两项。

---

## 二、GPU 部分：差距最大的一项

3DMark Solar Bay Unlimited 测的是手机的实时光追和图形性能。数字是这样的：

| 机型 | 平均 fps | 相对差异 |
| --- | --- | --- |
| **iPhone 18 Pro** | 61.93 | 比 S26 Ultra 高 **25%** |
| **iPhone 18 Pro Max** | 67.9 | 比 S26 Ultra 高 **37%** |
| **Galaxy S26 Ultra** | 49.37 | — |
| **iPhone 17 Pro Max（上代）** | 46.6 | 比上代快 **46%** |

**GPU 这一项，差距拉到了 37%。**这在旗舰对决里很少见。

更值得注意的是「持续性能稳定度」——3DMark Wild Life Extreme Stress Test 跑 20 轮后还能保持多少峰值性能：

* iPhone 18 Pro Max：79.4%（上代 65.2%）
* iPhone 18 Pro：62.8%
* Galaxy S26 Ultra：53.9%

通俗讲，Pro Max 打半小时游戏后，还能维持八成的峰值输出；三星 S26 Ultra 已经降速一半。

💭 这里的关键不是「苹果数字大」，是 A20 Pro 的散热重新设计了——均热板面积扩到上代 3 倍，SoC 和内存并排封装，热量导出路径更短。结果是**性能不容易撞温度墙，长时间游戏比上代凉快 1℃、性能还多 14%**。

---

## 三、AI 部分：反常识的来了

Geekbench AI 跑分结果是这样的：

| 机型 | AI 跑分 | 实现路径 |
| --- | --- | --- |
| **Galaxy S26 Ultra** | 83,047 | TensorFlow Lite QNN |
| **iPhone 18 Pro Max** | 71,974 | Core ML（神经引擎） |
| **iPhone 18 Pro** | 69,245 | Core ML（神经引擎） |
| **iPhone 17 Pro（上代）** | 49,050 | — |

**iPhone 这一项输给了三星**。14% 的差距，不能装看不见。

但——这里有个关键前提。

💭 **两家跑的不是同一个东西。**三星用的是 TensorFlow Lite 路径，调用的是高通 Hexagon NPU；苹果用的是 Core ML，调用的是自家的神经引擎。**软件栈不同，分数不能直接相加减**。

这个反常识的结论说明一件事：**「AI 跑分」现在还在早期，标准没统一。**各家都在自己最擅长的路径上拿分。等明年 AI 测试规范成熟，再来比较会更靠谱。

不过有一项实打实的进步：iPhone 18 Pro Max 跑 27B 大模型（PrismML 的 Bonsai），速度从上代的 33.5 tokens/秒提升到 **55.4 tokens/秒**，涨幅 65%。这是端侧大模型能跑起来的关键指标，比 8% 还是 14% 这种账面数字更有用。

---

## 四、几个数字放一起看

把上面分散的数据汇总：

| 维度 | iPhone 18 Pro | S26 Ultra | 差距 |
| --- | --- | --- | --- |
| Geekbench 6 单核 | 4,735 | 3,785 | iPhone +25% |
| Geekbench 6 多核 | 12,800 | 11,563 | iPhone +10% |
| 3DMark Solar Bay | 61.93 fps | 49.37 fps | iPhone +25% |
| 持续性能稳定度 | 62.8% | 53.9% | iPhone 更稳 |
| Geekbench AI | 69,245 | 83,047 | S26U 账面领先 |

传统性能：iPhone 全面领先，GPU 项拉得最开。

AI 跑分：S26U 账面更高，但软件栈不同，可比性弱。

真正的胜负手是「持续性能」——打游戏半小时之后，两台机的体感差距，远比跑分表的瞬间数字大。

---

## 五、最后：账面数字和使用体感

看完跑分，有些事得说清楚：

**① 跑分领先不等于日常快很多**
CPU 单核高 25%，反映在日常可能是「App 启动快 0.2 秒」。绝对值在，但日常很难察觉。

**② GPU 持续性能是真的体感差距**
半小时游戏后帧率不掉的手机，比账面跑分高的手机更有用。这点 iPhone 18 Pro Max 比较占优。

**③ AI 这事还没法比**
等测试标准统一了再说。现在各家都挑自己最顺手的路径跑分。

一句话总结这一轮：**CPU 单核 iPhone 领先；GPU 持续 iPhone 领先；AI 跑分账面三星领先，但软件栈不同不能直接比；端侧 AI 推理速度 iPhone 领先。**

按需挑就行，不必硬站队。

**📌 你更在意哪个数字？**

CPU 单核？GPU 持续？AI 跑分？还是根本不在乎？
评论区说说你的购机优先级。

跑分数据来源：Tom's Guide、iPhone 18 Pro 实测、Gadgets Now
AI 跑分基于不同软件栈（Core ML vs TensorFlow Lite），不能直接相减

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icvDMZl2IHQwDs9rQsBP3sFULS2rUtaH6NIUyF2Dy7EOoLsxiaYicwUXcoyfeAW2tvdkuibZqyNU8GmupQ1U7Q7yIR43Hmq905DlzHtA4VRIplQ/0?wx_fmt=png)

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