---
title: 从单次 LLM Call 到 Learning Loop - HUB 在安全运营的实践
url: https://mp.weixin.qq.com/s/Mn8iGkA6LGtLE4Rytl3Qjw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:25:51.179663
---

# 从单次 LLM Call 到 Learning Loop - HUB 在安全运营的实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/haeEa6u0cicC301hHmEBosZX7hfCpzjica9BkHIag6dBWkjRlwLYjJv8P2XlwHp0Kj7jpUJicdqoX5kia3cTFJTXawSuZ9ic85SM8BIUz9OFNlps/0?wx_fmt=jpeg)

# 从单次 LLM Call 到 Learning Loop - HUB 在安全运营的实践

原创

EBwill
EBwill

灾难控制 局

![]()

在小说阅读器中沉浸阅读

**1. 背景**

在公司反入侵的建设中安全运营是极为关键的一环，安全运营工程师需要针对部署的各类安全产品的告警进行及时响应与研判。

但是各类入侵检测产品底层是各类黑名单策略、行为分析策略、ML 策略组成，如果策略质量较差那么会产生较多误报，且在告警准确度差的情况下，想要实现 7x24 小时的告警响应也是有困难的。

在 LLM 出现后，利用大模型的能力做告警运营是一个非常成熟的实践路径。

接下来将会给大家展示如何借助 HUB 从一开始的简单告警自动化研判的辅助操作，到自动化添加白名单排除误报，到最后的 Learning Loop 的设计和落地的。

**2. 单次告警分析**

AgentSmith-HUB 是一款 SDPP（Security Data Pipleline Platform）产品，即用该产品可以消费各类安全日志、安全告警，然后在该平台内进行统一的数据处理、规则配置、规则沉淀、告警响应的配置，优点是能够高性能的、统一的满足安全场景下的入侵检测规则制定、数据分析需求，统一使用 HUB 平台降低了大家各自开发工具或脚本带来的维护成本。

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicAdEgu1wKIAr3X1xyO9wCh8UMLfCf5Eo1O6Qaw7ticncIKyiajdtCMTFibmX9OP0lZ9kIRLKjYQTmmd94XT5akAxLvgXEOBkQarCk/640?wx_fmt=png&from=appmsg)

如图所示，我们通过 HUB 的配置可以消费多个 WAF 实例的告警（通过 HUB 的 INPUT 模块，可以消费如 Kafka、SLS 等这类日志通道），并进行统一的告警推送或单独针对某 WAF 实例进行特殊数据处理和分析后再进行告警推动。

因此面对告警运营的需求，我们首先设计了一个和 RULESET 同级别的组件：AGENT，这样我们可以直接在 HUB 数据流中引入 AGENT 作为一个数据处理单元：

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicBhC18J4p7H7icpV0iciapibIJjb839VoicPgn9BHicqHibGRHkl0KJIld8O725VxK0ibwMO2lGQZeib8ogf83ZyvewVp0Uib95Zjn4RQVDI/640?wx_fmt=png&from=appmsg)

我们新建了一个 'alert\_review' AGENT 实例，让 AI 分析告警以及原始数据，并给出置信度评分和评估内容：

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicDibm5TCpglBUkOj2XaPqPP7O0cO4cA8nc3C0sicxr3vvfmetZicLicl7KRX1XTnibcRsMgXFGrXfdPwIA7ia067qGLpK3JicfNFicGXa0/640?wx_fmt=png&from=appmsg)

于是告警可以在 HUB 内先经过 'alert\_review' AGENT 模块，输出的告警数据会增加 AI 的分析结果后再推送到群里，这样安全运营人员可以只评估高置信度的告警：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicD4FpYCZQYVjI4XHTocpBibJia81lhC5rNWG5DgEKQD9jzs6cUW9WToL1cH5KqDSqrx1yxSLbuMAZicA5fNAZrJY71kXcaCXHA6fg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicD2kE5iclzvIEbjtHEbKtAAAgkHXKDWLxVrRYtgbdQWoJaoJL6vyIMmo1diaaZfvEkZL8YC9qglE4eUFBw2c1ut5ibClUy3SDfjLI/640?wx_fmt=png&from=appmsg)

到这一阶段，基本完成了 AI 告警自动化 Review 的工作，根据 3 周的实际验证效果来看，置信度的分析整体还是比较准确的。

**3. 自动化生成白名单**

但是很快我们就发现：部分正常的操作且会触发低置信度的告警如果没有白名单的话每日告警量会很大，这会带来很多无效的告警进入 AI 进行评估浪费算力，我们思考应当让 AGENT 具备自动化针对低置信度告警添加白名单的功能。

首先 HUB 支持自定义插件功能，该插件一般会在 RULSET 规则引擎组件使用，实现复杂策略、告警自动化响应等功能，我们将插件能力也抽象出来，允许 AGENT 调用，实现 AGENT TOOLS 的效果。

另一方面，我们也新增了 SKILLS 组件，该组件可以挂载在 AGENT 下，渐进披露。

于是首先，我们在告警 Review 链路中增加了一个专门做白名单的 RULESET，在 AGENT 前面，告警如果不被白名单匹配，才会继续向后到 'alert\_review' AGENT 进行告警的分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicAXiaIZ55EM4QcpnOR84hwCcOCBjPT3q5W1SnI4XBYDzT3NnRWTV2zCv3HH9Nx3WFv1fSgeolu3w2AbCxRDQJpnZd0UfA0icrrmY/640?wx_fmt=png&from=appmsg)

然后我们新增了一个插件：addRule，该插件可以实现向 RULSET 添加规则：

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicCQ0TaiavF4laHLyFEoN2Lqdp07OfgT1cniabp90feYcVZbDg6GxDeQiataeCpYF593ZFPhO9a1juIGV8YPwrNJLVRMBJcbEhuUJI/640?wx_fmt=png&from=appmsg)

由于 HUB RULESET 是有特定语法约束的，于是我们添加了特定的 SKILL：hub\_ruleset\_expert，AGENT 可以通过该 SKILL 知道如何正确的编写一条 RULE：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicDn9f7zUH1pNpFuAMmph6gpGVOiasd1wxeq6InOIItIDTIiaHI22yxKxHtJp1855P2o7wBTy4pPJoY0u3Rj1hpkJutsj1rJhLnoY/640?wx_fmt=png&from=appmsg)

于是我们重新设计了'alert\_review' AGENT 流程，并从一开始仅做告警分析变成了：

```
告警置信度分析，0-1；告警的置信度如果低于 0.2，那么调用 'hub_ruleset_expert' SKILL 生成对应白名单；通过调用'addRule' 工具进行自动化添加白名单。
```

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicAq3uedhnuGtxUkAWrQWyQ9Xevcq4RRnMPUma20rZft7ogc6dxjDey5eyjhhPArl85OaiapSVN6HpM3uGaZEQETdmXoJ3vJwlgg/640?wx_fmt=png&from=appmsg)

最后，我们不希望 AGENT 的所有操作都是黑盒完成的，我们增加了 Agent Logs 功能，可以看到 AGENT 的每次调用细节：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicDek8OY2lbcKXiaHDdAz38k67VLdM0aEwCCOHEeF80glibu0LoXrZVDmvqNRHY9zE5lvL3TIUoxb6knJqbiaxy5j79w3p52jMrkcU/640?wx_fmt=png&from=appmsg)

至此，我们借助 AI 的能力，完整完成了告警分析、自动化添加白名单的动作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicATroYopzzhoKg7juH7Kbf6Z6R7v70gNUyhRkLHDauX1LenbZZurh4bAibIL2Lr40eg2EeqlYZxBvomGKdMpwDltsR8oUjEceKg/640?wx_fmt=png&from=appmsg)

(自动添加的白名单)

**4. Learning Loop**

但是这依然不够，AI 能力虽强，但是依然会有操作不够优雅的情况，并且 AI 也不能完全掌握公司内的各种业务信息，很容易在告警研判、白名单生成方面有误判，人类的介入还是必要的，我们基于该需求进行了进一步设计。

我们针对 Agent Logs 增加了一个功能：Comments，允许安全工程师针对每次 Agent 调用进行评论，并且在 HUB 底层开发了一个专门分析 Comments 和生成 Memory 的 Agent：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicAXKKlWOxVb5DHicPO19rYXh3T082BKCrPbHkOP9FE3xMraXcrYoypzZr2hlnrV7tiasLCPcib18X455Ocy31FfMkzq0oYSlRjQjo/640?wx_fmt=png&from=appmsg)

当安全工程师发现 Agent 存在误判等其他问题时，我们可以在对应的操作下进行评论，HUB Memory Agent 会针对评论以及当前操作的上下文进行分析，提取出约束性的 Memory，追加到 Agent 内，Memory 会在 Agent 每次调用的时候都追加进去，这样简单的设计就完成了：评论-生成 Memory-注入到 Agent 运行时 的效果，实现了极简化的 Learning Loop 的效果。

**5. 总结**

该告警运营机制极大地减少了安全运营的工作，安全运营工程师长期头疼的误报问题得到了极大的缓解，每日研判的告警数量从一开始的几十到个位数，而 Learning Loop 也确保该功能并不是一个玩具属性的功能，而是可以持续提升准确度的生产可用的功能；Tools、Skills 的能力也赋予了 Agent 更多的可能，当 Agent 可以通过 Tools、Skills 获取更多外部信息来辅助判断告警的时候，准确度也会得到进一步的提升，甚至未来也完全可以完成一些基础的应急响应操作。

项目地址：https://github.com/EBWi11/AgentSmith-HUB

文章中使用的Skills、Agent、Tools均已开源。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jEESHeKDyVxhtbAawicDNOVJB5zLyiaibU8WAjT97QyuTCNoCXIlq0o7fYIMu3Tp1Pw7fZQicTYGHKOib7EmCa4tUVA/0?wx_fmt=png)

灾难控制 局

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jEESHeKDyVxhtbAawicDNOVJB5zLyiaibU8WAjT97QyuTCNoCXIlq0o7fYIMu3Tp1Pw7fZQicTYGHKOib7EmCa4tUVA/0?wx_fmt=png)

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