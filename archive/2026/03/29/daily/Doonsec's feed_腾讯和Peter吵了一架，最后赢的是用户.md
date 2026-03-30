---
title: 腾讯和Peter吵了一架，最后赢的是用户
url: https://mp.weixin.qq.com/s/KUlQ1yDbaRhCNmWOpoY0eg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:54.469764
---

# 腾讯和Peter吵了一架，最后赢的是用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4y2Wc7qNExRdzpE9zL7LR1q8Vp5Em8uOCphs7TZUIWztRDZYG2ecXeqybV05l84ZeROkuicgqJU8TiaRibn72iaCwFBINW8USxopa31WdgTNXA4/0?wx_fmt=jpeg)

# 腾讯和Peter吵了一架，最后赢的是用户

运维帮

![]()

在小说阅读器中沉浸阅读

如果你用过 OpenClaw，你应该知道：它能干这些事，靠的不是模型本身，而是 Skills——AI 的手脚。

问题来了：这些 Skills 去哪儿找？

## 官方市场，中国用户进不去

OpenClaw 有个官方技能市场叫 ClawHub，1.3 万个 Skills，覆盖从写作到开发的几乎一切场景。

听起来很美好。但你真正去用一下，就会发现：加载慢、全英文、有些功能根本打不开。不是你网不好，是它本来就没考虑中国用户。

很多人就卡在这里了——框架装好了，Skills 装不上，AI Agent 成了空架子。

这个痛点，腾讯看到了。

## SkillHub：腾讯云出手做的那件事

2026 年 3 月，腾讯云低调上线了 SkillHub（skillhub.tencent.com）。

说白了，就是 ClawHub 的国内镜像站，同时做成了一个本土化的 AI 技能社区。

但如果你只把它理解成"镜像"，就低估它了。

速度是最直接的差别。依托腾讯云节点，Skills 下载从"等到地老天荒"变成秒级响应。有个数据很说明问题：SkillHub 上线第一周，分发了 180GB 的技能包，但从 ClawHub 官方源实际拉取的只有 1GB——减轻了 99% 的带宽压力。OpenClaw 官方的服务器也跟着松了口气，这倒是个意外之喜。

安全方面，SkillHub 对全量 Skills 做了静态+动态双重扫描，每个技能有安全评级——**SAFE** 或 **CAUTION**。开源生态里随便装一个恶意插件轻则泄露数据重则被当跳板，有这个评级心里踏实一些。说实话，我也不确定这套扫描能拦住多高级的攻击，但总比裸跑强。

还有就是中文优先——技能描述、使用说明、场景标签全部中文，不用再对着英文文档猜半天。另外有个精选 TOP 50，把高频场景里最好用的技能集中列出来，不用自己在 1.3 万个 Skills 里大海捞针。这个功能看起来简单，但对新手来说其实挺重要的，有时候选择太多反而不知道从哪下手。

## 它能帮你干什么

说几个真实场景，不一定适合所有人，但可以感受一下方向。

**内容创作者**用得上的：公众号写作 Skill + AI 去味润色 Skill，从选题到成稿能省不少时间。**职场打工人**的话，日历同步、邮件管理这类重复性事务可以甩给 AI。**开发者**有自动化 GitHub 工作流的 Skill，代码审查、PR 通知、Issue 归档一套带走。还有视频摘要提取——一小时的播客十分钟看完重点，这个我自己用着还行。

这些不是 PPT 上的演示，是装好 OpenClaw + 对应 Skills 之后，明天就能用上的东西。

## 插曲：腾讯和 Peter 吵了一架

这件事值得单独说一说。

SkillHub 上线不久，OpenClaw 创始人 Peter Steinberger 在社区发帖，语气不太好。大概意思是腾讯照搬了他们的生态，事先没有沟通，有点不讲武德。

腾讯的回应没有绕弯子：我们明确标注了来源，而且你看数据——我们帮你减轻了 99% 的带宽压力。

然后事情的走向就有点戏剧性了。摩擦之后，腾讯团队开始积极参与 OpenClaw 社区，提交代码、反馈问题、推动本地化。有消息说腾讯有望成为 OpenClaw 生态的主要赞助商之一——如果最终坐实，这个故事的弧度其实挺完整的：从被骂到被信任。

> 开源世界里，最好的"和解"不是握手言和，而是代码贡献。

## 一行命令，装上它

●●●

curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

兼容腾讯云 Lighthouse、Mac、Windows，零代码，一行搞定。

装完之后去 skillhub.tencent.com 逛逛，从 TOP 50 里挑几个用得上的，跑一遍，感受一下 AI Agent 真正"动起来"是什么感觉。

SkillHub 做的这件事，其实很难说有多大——它没有发明什么新技术，只是把一个对中国用户几乎不可用的生态，变成了触手可及的工具箱。

这种脏活累活，有人愿意做，挺好的。🦞

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/4y2Wc7qNExTy0v01OlxUBwEMdVklUVQ7KHPjfX4mcVzlkMMf2gRvn6r7Lzfz4YoqS6tR0sf2p2Hxf88Mpy5r9Bl34kDzkqITpPCzKmyt5MA/0?wx_fmt=png)

运维帮

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4y2Wc7qNExTy0v01OlxUBwEMdVklUVQ7KHPjfX4mcVzlkMMf2gRvn6r7Lzfz4YoqS6tR0sf2p2Hxf88Mpy5r9Bl34kDzkqITpPCzKmyt5MA/0?wx_fmt=png)

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