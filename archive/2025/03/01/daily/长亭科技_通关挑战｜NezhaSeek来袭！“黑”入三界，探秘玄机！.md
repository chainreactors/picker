---
title: 通关挑战｜NezhaSeek来袭！“黑”入三界，探秘玄机！
url: https://mp.weixin.qq.com/s?__biz=MzIwNDA2NDk5OQ==&mid=2651388927&idx=1&sn=3bfd5f7f3c3b5348b19c1a4811270838&chksm=8d398a77ba4e036199fbee63146c760cc8310fb9f27758e30409834144d757134e34ad8cc5f8&scene=58&subscene=0#rd
source: 长亭科技
date: 2025-03-01
fetch_date: 2025-10-06T21:59:19.703119
---

# 通关挑战｜NezhaSeek来袭！“黑”入三界，探秘玄机！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Fuleibl6qMuqa5FUEENthvqTBseKjjibMMXzm7kpBIxQNllCeugI9GGPMbyt9x1hwsYaO0nnRt9kFXBtMQELcvkQ/0?wx_fmt=jpeg)

# 通关挑战｜NezhaSeek来袭！“黑”入三界，探秘玄机！

长亭科技

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Fuleibl6qMuqa5FUEENthvqTBseKjjibMM496cMBZj53GhZWkmfronwF1iaIEfic7iavlNBny7iaGiajRVlCJq5icwVrCw/640?from=appmsg)

**大冒险后的真心话**

朋友，不知道你有没有发现，当你每一次发起对话、尝试突破暗藏玄机的关卡的时候，就已经踏入了大模型应用中的安全雷区——看起来普通的对话可能就藏着诱导AI“说错话”的“陷阱”。接下来，我们就和安全大佬聊聊NezhaSeek背后的故事吧～

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAMCU5Ak2VCXbS1fQZ9NPLXK8mWRKZLvapvDZjicu9AGj9AUdEFQ49kzw/640?from=appmsg "undefined")

**市场小编：****怎么想到的开发这个游戏呢？**

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAIib7XRO7wFUj5c0CDkCH6eLyT8DN5icofSFR0340uoBcuxgtjR9iaoszg/640?from=appmsg "undefined")

**🌟 安全研究大佬**：

这事儿还要从「矛与盾」说起……

年初，长亭的年度保留项目「矛与盾」内部攻防演练如期而至。「矛与盾」是出了名的长亭内卷修罗场，今年再出奇招，搞了个“大模型安全专项赛”，将近200位来自安全策略、安全研究、安服、研发等部门的师傅在这个赛道大展身手，最终，大家共提交了近1200个flag、 超千种越狱思路并成功挖掘出多个大模型应用系统 0day。

其中，我们发现了很多有意思的“提示词注入”攻击方式，这些攻击方式在很多常见的模型应用场景中都存在！为了让大家更直观地感知它，我们就想着设计一个智能NPC游戏大家一起“以身试险”hhh～

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAMCU5Ak2VCXbS1fQZ9NPLXK8mWRKZLvapvDZjicu9AGj9AUdEFQ49kzw/640?from=appmsg "undefined")

**市场小编：****啥是“提示词注入”？**

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAIib7XRO7wFUj5c0CDkCH6eLyT8DN5icofSFR0340uoBcuxgtjR9iaoszg/640?from=appmsg "undefined")

**🌟 安全研究大佬**：

2023 年*OWASP Top 10 for LLMs 2023 - 24* 提出了**“提示词注入”攻击手法**，这是一种针对大型语言模型的网络攻击方式，简单说就是**黑客将恶意输入伪装成合法提示，诱使生成式 AI 系统泄露敏感数据，传播错误信息。**

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAMCU5Ak2VCXbS1fQZ9NPLXK8mWRKZLvapvDZjicu9AGj9AUdEFQ49kzw/640?from=appmsg "undefined")

**市场小编：****可以举个例子吗？**

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAIib7XRO7wFUj5c0CDkCH6eLyT8DN5icofSFR0340uoBcuxgtjR9iaoszg/640?from=appmsg "undefined")

**🌟 安全研究大佬**：

咱们就用NezhaSeek来举例，整个游戏其实涉及了模型应用场景中多个常见的安全问题，不同的关卡设计使用到不同参数的模型、提示词限制、关键词过滤、复杂流程编排等限制方式来对信息进行保护，玩家可以通过提示词注入的手法，让模型实现越狱、绕过应用编排的逻辑或是触发编排中的关键词等多种方式来获取每关所保护的信息内容。

比如下面这一关，玩家就可以通过提示词注入来获取系统提示词内容，利用获取到的信息来修改初始系统提示词，从而控制模型来输出答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuqa5FUEENthvqTBseKjjibMMFe703uabqwBqLApROxHTL0A2kK3fuLDiciapIxaM2sfwsibu39MdtwdOA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAMCU5Ak2VCXbS1fQZ9NPLXK8mWRKZLvapvDZjicu9AGj9AUdEFQ49kzw/640?from=appmsg "undefined")

**市场小编：****我懂了！所以我们在享受大模型所带来的便捷的同时，也必须留意这些潜在的安全问题！**

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAIib7XRO7wFUj5c0CDkCH6eLyT8DN5icofSFR0340uoBcuxgtjR9iaoszg/640?from=appmsg "undefined")

**🌟 安全研究大佬**：

是的，这不仅局限于**模型本身**可能引发的提示词注入攻击、数据投毒攻击、模型后门攻击、模型漏洞风险，还涉及到**应用编排的各个层面**，比如应用接口安全、应用间数据共享风险、应用权限管理问题，此外还有**基础设施**带来的传统安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAIib7XRO7wFUj5c0CDkCH6eLyT8DN5icofSFR0340uoBcuxgtjR9iaoszg/640?from=appmsg "undefined")

**🌟 安全研究大佬**：

所以最近我们创新发布了**「AIGC安全评估服务」**，通过AI to AI测试、深度对抗测试、渗透测试三种测试方法相互补充，能够帮助企业有效构建多层次的安全防护体系，为大模型各种应用场景的安全与合规性提供全面的保障。

![](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NAMCU5Ak2VCXbS1fQZ9NPLXK8mWRKZLvapvDZjicu9AGj9AUdEFQ49kzw/640?from=appmsg "undefined")

**市场小编：****这个我知道！长亭科技「AIGC安全评估服务」方案在此，欢迎围观！**

**点击下方图片，查看方案详情 👇**

[![tiaozhuan.png](https://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3MjV50TWibfdrhSXGXkk27NA4dFjs7WEUQub0Av0CfVepnqsde08PUeafyxoQS6bicOWJqRZbCEibGTg/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyNDUyNzU1MQ==&mid=2247486891&idx=1&sn=72fa9b91e119e2811e49ae4aa9880cc0&scene=21#wechat_redirect)

作为新生代网络安全领军企业，长亭自创立起，便将 AI 技术融入实战化攻防能力体系。2015年，长亭研发出全球首创、具有独立自主知识产权的智能语义分析技术，大幅提升了未知威胁的发现能力。2023年，长亭“问津”（ChaitinAI）安全大模型发布，全面提升了安全运营效率。同年9月，长亭与趋镜达成战略合作，接入DeepSeek开源模型，使长亭问津（ChaitinAI）参数规模突破千亿量级，实现了能力的代际跨越。

今天，随着大模型在各领域的深度应用，其安全边界的模糊性正衍生出远超传统安全的风险维度，长亭将继续秉持「知攻善防，智能安全」的理念，以 AI 驱动重塑安全运营，护航每一个伙伴在 AI 时代里乘风破浪！

![](https://mmbiz.qpic.cn/mmbiz_png/JaFvPvvA2J1l9248vhzo8jicBPJaBT4ZZCAEicSu7Wu6HvbIJLvlkvl0xBnmX6WSS5h2CTynAvCr9bItG720tCRQ/640?wx_fmt=png)

**彩蛋玩法大搜集**

听说！

已经，已经，有玩家试玩过了NezhaSeek了！🔥🔥🔥

“成功了！！！冷冰冰的敖丙竟然可以如此热情回复！”

“提示词注入，敖丙怎么突然叫我父亲了？”

“一点都忍不了，敖丙开始狂揍太乙真人”

... ...

**「彩蛋****活动」**

* **转发本文至朋友圈（兑奖需提供截图）+ 本文评论区留下你的趣味闯关玩法语录**，我们将在本文评论区pick单条评论获赞最多的10名幸运儿，赠送惊喜礼物！🎁🎉🎉
* 活动即日起，**截止至3月6日24:00时**，逾期不候哦！

**NezhaSeek**

**等你来挑战**

小贴士：NezhaSeek游戏传送门

本文**开篇扫码二维码** 或 点击**“阅读原文”**前往

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Fuleibl6qMuqy3z1PNoOSxgQbUqYibAcIb722vbFGdP1gfxibthFf1IibTtFxgfSv90xVj6dPhV9oRc39O4VGUbYQw/0?wx_fmt=png)

长亭科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Fuleibl6qMuqy3z1PNoOSxgQbUqYibAcIb722vbFGdP1gfxibthFf1IibTtFxgfSv90xVj6dPhV9oRc39O4VGUbYQw/0?wx_fmt=png)

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