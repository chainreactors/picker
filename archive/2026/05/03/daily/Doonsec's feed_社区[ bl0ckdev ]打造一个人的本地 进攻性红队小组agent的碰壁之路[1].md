---
title: 社区[ bl0ckdev ]打造一个人的本地 进攻性红队小组agent的碰壁之路[1]
url: https://mp.weixin.qq.com/s/0YVFFU8zONLiCE_DcZ4S3Q
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:00.516510
---

# 社区[ bl0ckdev ]打造一个人的本地 进攻性红队小组agent的碰壁之路[1]

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16VehYq5DVwqacbBdVibUIx1ofVnM6udYMsicnhp9EVuwbY1yvYkbLoohpibpK3g2dxLzA23NMCLDvM0sx61nQyCpxHkPAczV2gERtRI/0?wx_fmt=jpeg)

# 社区[ bl0ckdev ]打造一个人的本地 进攻性红队小组agent的碰壁之路[1]

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vej0Rp5AUaFOWxTMUEpgcB2AArQ4YPeHYX5Fsr4csHarDEAj1driaA7ouOhzlHFTJjaICIRRPKfbv6JcK7DWKww0NWQ2mIF5y810/640?wx_fmt=png&from=appmsg)

本文对应的是这篇文章的后续：[对AI-gent的冷漠是一种悲剧 ，“落后即是一种罪过”-2026](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492634&idx=1&sn=85b6be17b6424f5cd2e4bcf1609e732d&scene=21#wechat_redirect)

[继RTX-5090研究了以后,我又入手了一个新的显卡 RTX3090](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492697&idx=1&sn=da3eab33858a13a9a4bf0d6e731b1e05&scene=21#wechat_redirect) 显卡又霍霍我1W,

因为显卡的缘故我只能在本地配备了3个离线模型用于辅助我微调和配置自己的#agent

* GPT-5（40）mini （数据是2024年6月之前的）
* Claude Haiku 4.5  （数据是2024年4月之前的）
* 也在本地进行量化 自己的微调版主要对接自己的学习的mcp服务器,基于Qwen的量化微调,后续可能会换谷歌的最小模型进行微调。

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16Vehiaia30VTHMkkGR11ojFagnbJ0cbYKRhrrwXcYXN2vepqW5EcbC7jicAeUMZDHOjKZgtDu7o4xKyAeZrWqO4P4zbbnjl6U5LOicLA/640?wx_fmt=png&from=appmsg)

我(我们)的研究领域将会中心放在设计与构建用于挖掘漏洞/逆向工程-Ai的工作流,用#MCP服务器 接管并代替一切可自动化的并重复的内容。

现在#进攻性红队 爱好者面对着即将席卷而来的 AI 浪潮，与其抗拒，我相信最善于驾驭/构建这一工具的黑客必将占据显著的竞争优势。

2026-2030年红队不会消失,但是传统的渗透测试和漏洞复现都会被#Openclaw claw [1]号员工代替。

目前很多程序已经在github上进行看本笨重的开源逻辑实现,现在做的就是利用自己的助手进行修改后适配本地Agent执行。以下三个必须经过修改才能完整的进行本地私用.

[参考1：可自动红队侦察到漏洞利用的完整本地/在线模型](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492628&idx=1&sn=67e1cd59fde6d0158949973c103d5900&scene=21#wechat_redirect)[Decepticon]

[参考2：适配(鹦鹉)](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492526&idx=1&sn=af2bafaef3667e6bab7b8a851d0b4c80&scene=21#wechat_redirect)[Parrot OS 操作系统）](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492526&idx=1&sn=af2bafaef3667e6bab7b8a851d0b4c80&scene=21#wechat_redirect)[Metatron是一款基于 CLI 的 AI 渗透测试助手](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492526&idx=1&sn=af2bafaef3667e6bab7b8a851d0b4c80&scene=21#wechat_redirect)

[参考3：](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492569&idx=1&sn=b3cca872f10a22a2e6a13c1f10a168d7&scene=21#wechat_redirect)[这款工具名为PentAGI，是一个无需人工干预就能协调发起攻击的自主AI系统。](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492569&idx=1&sn=b3cca872f10a22a2e6a13c1f10a168d7&scene=21#wechat_redirect)

目前研究的结构如下:

1. 构造一套属于自己本地的 Ai红队#Agent ,当前借着DeePseek和Qwen模型可以完成对于有目标有目的针对性的电脑和服务器进行获取最高权限,因为硬件的问题目前只能做到百分之50的不被发现。但因为bash和PowerShell个人认知问题现在百分之百被可以被日志抓到你行动轨迹。（注意针对钓鱼网站和违法网站的Rm-r权限）

* bash — Windows日记清除
* PowerShell — linux痕迹清除

2.本地的Agent相关的部署

* Openclaw claw [1] 号员工用来反馈对手的基础环境的部署是否被发现。
* Openclaw claw [\*] 号员工主要用来：#执行层熔断机制
* Openclaw claw [2] 号员工用来识别目标和扫描漏洞
* Openclaw claw [3] 号员工用来汇总\*+1+2的所有内容进行提交方案最后交给本地模型进行编写完整的流程提交给 Agent\*\*\* 进行执行方案,并且自己拿下这些数据进行训练。

3.持续学习的内容

* MCP  — 定义了应用程序和 AI 模型之间交换上下文信息的方式
* json(给机器看的语言)
* RAG—而是给现有 AI 装的“外接知识库”——让 AI 在回答问题前，先主动去你指定的“资料库”里查资料，再基于真实、最新的资料生成答案，从根源上杜绝“一本正经地胡说八道”。

4.后续添加硬件：

GPU：48Gb（双24）或更换Macbook,不过这都是以后的事,现在社区的重心是#逆向工程和漏洞利用开发 ，编程语言C++和python修改成懂完整的逻辑。懂得审核代码即可。

5.目前正在学习.[B站搜名字/我估计应该有很多人转播] ，现在需要向前辈们学习太多的东西,我主要的时间都活跃在了Disocrd之中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vej1vJVQicADGDzVv2iaia4OmoJY2nQ7fiby3x2dIhCjWib1aH5SwiaNxS1icoqoVApoYIw81T4tIw25jHp3LBpP43MoxYfiajwB62dZSTg/640?wx_fmt=png&from=appmsg)

6.Discord 如何登录

微软商店：用 Watt Toolkit（原 Steam++）\*\* 专门加速 Discord、Steam 等，免费且简单。

我的ID：bl0ckdev   (持续逆向技术交流+Ai)、

我的微博ID：bl0ckdev  （微博只谈生活不谈技术）、

我的VX: 目前使用的是华为平板登录,解除一次异常第二天就继续触发异常,基本上已经放弃治疗了、

[https://discord[ . ]gg/KWFrnnqBQu [ 我们欢迎大家一起进行交流学习,也欢迎大家赞助公众号作者 ]](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492484&idx=1&sn=4d255ad16ee773dacbfc42ae020a73ab&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaRiaPeAygl22It9EzZHGJ4ic0DKgbfF1OtNNdg7FgKLB09D7q1ibfIIZGfia2oUYxukpcIm20acOWVudZQHhFgCS6uNa2t16mia71Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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