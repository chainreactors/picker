---
title: 从 OpenClaw 到 HiClaw：普通人的 AI Agent 避坑与实战复盘
url: https://mp.weixin.qq.com/s/TdHozeXqNMNWVqJWJWJv3Q
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:45.841224
---

# 从 OpenClaw 到 HiClaw：普通人的 AI Agent 避坑与实战复盘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImmXvH3SzdR77iaADiatbfy9cBjrJaEM2OPKdwsmN0tkR2iaVSMfRRdotACd4FyjmiclPP3hMoU9dw0icmibB83wn9ZxvzI91x1amKYmM/0?wx_fmt=jpeg)

# 从 OpenClaw 到 HiClaw：普通人的 AI Agent 避坑与实战复盘

原创

鸿渐
鸿渐

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

> "接触 AI 从最初的提示词工程，到现在的上下文工程、驾驭工程。与此同时，人的浮躁也逐渐被放大。持续上头，每天输出给硅基看的流水账。是时候停下来，做一些真正有意义的事情了。"

---

## 🛤️ 折腾之路：从跟风到落地

回想从 3 月初 OpenClaw 爆火，到后来安装失败投入 HiClaw 的怀抱，再到版本从 1.0.2 迭代至 1.0.9。架构上，经历了从单人多 Agent 到多人、多 Leader、多 Team、多 Agent 的复杂演进。

这期间，我折腾了很多，也学到了很多。但也意识到，随着技术门槛的降低，人的浮躁被放大了。为了技术而技术的“折腾”，往往只是一场给机器看的狂欢。

## 💰 AI 赚钱的冷思考

     OpenClaw 爆火时，我也在思考：普通人到底能做什么？真的都能赚钱吗？其实，目前的变现路径无外乎这几种：

* **金融量化交易**

  做量化工具，门槛极高。
* **卖课/私域**

  纯粹教别人“怎么赚钱”，收智商税。
* **场景教程**

  将 AI 应用于生活、学习、工作的具体场景。
* **技术服务**

  安装、卸载、卖 Token，以及少数成功的自媒体/短剧/绘本案例。

大多数人都还在摸索：如何在合规、稳定的前提下获得收益，或者在工作中真正提效？

## ⚖️ 机会与风险并存

#### 🚀 机会：

|  |  |
| --- | --- |
| 提效 | 替代重复性工作，提升产出效率。 |
| 防裁员 | 掌握 AI 提效工具，降低被优化的风险。毕竟 AI 再强，也需要人来配置、调优。 |

#### ⚠️ 风险：

|  |  |
| --- | --- |
| 学习成本 | 不仅是部署的时间/金钱成本，更是“培养龙虾”的知识成本。AI 是基于现有资料推演，如果你自己都描述不清楚需求，神级 AI 也无能为力。 |
| 隐私泄露 | 非本地模型联网使用，数据（身份证、住址等）会被大模型“扫”一遍，合规风险极大。 |
| 环境破坏 | Agent 具备修改环境的能力，目前的护栏和安全加固在复杂场景下仍显脆弱。 |
| 幻觉崩溃 | 以为可以“撒手不管”，结果收回的是半成品，返工修改时的心态崩溃。 |

## 💡 给普通人的避坑建议

针对上述风险，结合我的折腾经验，总结以下几点建议：

1. 数据脱敏，本地优先

      涉及个人隐私和企业机密的数据，优先使用本地部署模型（如 Qwen），或在交互前进行严格脱敏。不要拿公司的核心数据去训练公有模型。

2. 环境隔离，安全第一

     强烈建议在 Docker 容器或虚拟机中运行 Agent。不要在主力机上裸跑，防止 Agent 误操作破坏系统环境。

3. 人机协同 (Human-in-the-loop)

     不要完全放权。对于关键产出（如代码提交 PR、文章发布），必须设置“人工确认”环节。AI 是副驾驶，你才是机长。

4. 深耕场景，拒绝焦虑

     不要为了折腾而折腾。找到一个痛点（如文档管理、代码辅助），用 AI 深度解决它，比浅尝辄止跑 10 个 Agent 更有价值。

---

## 📝 我的 HiClaw 实战清单

     写给自己的记录，也分享给认真看文章的朋友们。后续的文章我会坚持手写，沉下心来做有意义的事。以下是我目前用 HiClaw 落地的案例：

1. **代码提交辅助**

   通过任务分配，Manager 自动优化官方仓库安装脚本并提 PR，已成功 2 个，待审核 2-3 个。
2. **团队工具开发**

   带领 Dev-Team 开发了像素工厂、模型切换、日志检索等工具。目前自用稳定，对外分享体验待优化。
3. **Wiki 知识库管理**

   Manager 学习 Wiki Skill，实现定时写入 Wiki 并同步到 MinIO。解决了 Agent 记忆痛点。还开发了 Obsidian 插件方便本地查看。
4. **Skill 蒸馏**

   基于 nuwa.Skil 蒸馏出行业 Skill。“遇事不决，问下行吗？”，也许它能告诉你答案！

行吗.skill使用说明:

```
https://github.com/nillikechatchat/xingma-skill，阅读理解一下，帮我安装这个skill
```

Demo

![](https://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImkWichsmcuxjekkiaRJbZEAICfnibicjiaQiat4qMfibNjeFhMvZhcbhsAXRqC67qXFqjOJN89UAdgwCz1jP4082bgIaRVNoG7kLgb8ZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImmfTZbNkBQ5pkLfyiacqC4Hz5yzMhRKwCE4KQwntAK8iccSicp82lYG2SYUT41a6eBWtLRHbqtqh645dRNFb5L5FMh0ml2ZjeeByQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CBe66ugaImm2N4DFyOHs5NONJ6KGZfGicIAOR4L9E2ACMtNFjmmEbO6X3ia6e7gKictOVibibVd5xbaBZpLvKOahu18ulj2Tib7xpiauDlK72JL65U/640?wx_fmt=png&from=appmsg)

感谢每一位认真读完的朋友！后续我会分享更多真正能用于工作生活中的实操案例。

     有时候更新缓慢，不是代表停更或者停止，而是为了重构，为了涅槃，为了更好的提升用户体验！

![](https://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImnF1iam87tu4ibMiaZuSbYnhMYjl8wJnyTgB8w6raYQ9X7iaRV7cO8NwxduJF0LkP7j4wy8gwjibQuQ86mDdHDCMnekZ39aXUwISDWI/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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