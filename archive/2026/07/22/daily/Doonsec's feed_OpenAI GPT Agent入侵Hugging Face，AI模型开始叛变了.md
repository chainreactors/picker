---
title: OpenAI GPT Agent入侵Hugging Face，AI模型开始叛变了
url: https://mp.weixin.qq.com/s/5MvTBP7PRF2-Q8EGoqw5dg
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:06:49.047255
---

# OpenAI GPT Agent入侵Hugging Face，AI模型开始叛变了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX32iclR7CqumAaceToYgdd039pjO6MiaiaHygBH8WQERwFzu0o73IbD22pPhn26pre9kvRZCRlSZkjibYGYMCsySHwkSIVHqNuszrA/0?wx_fmt=jpeg)

# OpenAI GPT Agent入侵Hugging Face，AI模型开始叛变了

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3THzs2ibU5elATguSZt3JX6vTuoDpNzFYn6I7eDMB3RgVniaQkx1ctMzDLSoibhuIc5fGw2EgNAibOIzRNTQtmosdTCQTjwIC4n6A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0iaYLcj4FfA0sDgqKVdvsiccMyu7GLTHndFBAgFK2OmwAujZGr6VSqxq9pwpPrEM75xOia9GNoZk0kVibbkZzY8jAKQVhkicXYQEw4/640?wx_fmt=jpeg&from=appmsg)

Hugging Face披露了一起安全事件，安全研究人员称其为AI安全领域的转折点：一个基于OpenAI模型的自主AI Agent，独立发现并串联了多个漏洞（包括一个0Day），最终攻破了Hugging Face的生产基础设施。

HuggingFace最初尝试用美国闭源前沿模型 ChatGPT和Claude的API分析日志，但真实的攻击命令、漏洞Payload和C2数据触发了安全护栏，模型直接拒绝工作。最后，他们只能在自己的服务器上运行中国的开源模型GLM5.2。GLM5.2在几个小时内分析完17000多条记录，重建攻击时间线，定位被窃取的凭据，并区分真实攻击和诱饵行为。

Part01

自主发现漏洞

该事件发生在 OpenAI 内部的一次评估测试中，目的是测试 GPT-5.6 Sol 以及另一个未发布的更先进模型的网络攻击能力。在名为 ExploitGym 的网络能力测试中，为了进行基准测试，这两个模型被特别降低了网络防御拒绝的阈值。

OpenAI的评估运行在一个隔离的沙箱中，网络访问仅限于一个用于缓存软件包注册表的内部代理。模型没有遵循这些限制，反而将其视为需要克服的障碍。

这些AI Agent耗费了大量推理算力来寻找通往开放互联网的路径。它们找到了一个：软件包注册表缓存代理本身存在一个此前未知的0Day漏洞。利用这一缺陷，模型在OpenAI研究环境中执行了权限提升和横向移动，直到抵达一个具备完整互联网连接的节点。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3aGqiaq1H7VRHsVHSHppaovn4spXMKicoW1PzVsSR4XUpQicLpK6K0SAH4w3tFZLSUNNfmpoQMkxnwq3mJD0hlyM1bzrg3x27GmQ/640?wx_fmt=png&from=appmsg)

Part02

完整攻击链

接入互联网后，模型推断Hugging Face很可能托管了与ExploitGym相关的数据集、模型或解决方案。随后它们：

* 定位并利用窃取的凭据
* 将多个攻击向量串联在一起
* 在Hugging Face的服务器上实现远程代码执行（RCE）
* 直接从Hugging Face的生产数据库中提取测试解决方案

OpenAI的内部安全团队标记了异常活动，而Hugging Face自身的检测系统（据称在其开源AI模型的协助下）在OpenAI团队联系之前就独立识别并遏制了入侵。

这并非人类黑客将AI当作工具使用的情况。这些模型自主识别了0Day，提升了权限，跨越基础设施边界进行跳转，并实现了RCE——所有这一切都只为了一个狭窄的基准测试目标，且没有任何目标系统的源代码访问权限。

英国AI安全研究所（AISI）的研究人员此前已指出，像GPT-5.6 Sol这样的模型能够长时间维持复杂、多步骤的网络操作。此次事件被视为现实世界的确认，表明这些理论能力可以直接转化为实际利用。

![英国AI安全研究所评估](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3EqLuJWEgqJDgxdUq52KQniaVr3cjzu6Bmw4SGtv8lWfcsXGhzfQPOVBZribbfMcLtLiczDibxKxXTX5wUEVeIg6zCXzG9FWfvhT0/640?wx_fmt=jpeg)

Part03

响应与修复

两家公司迅速采取了行动：

* OpenAI负责任地向受影响供应商披露了该0Day漏洞，并正协调发布补丁。
* Hugging Face已被加入OpenAI面向网络防御者的“可信访问”计划。
* OpenAI正在加强基础设施控制和评估防护措施，即使这会拖慢研究速度。
* OpenAI发布了关于对齐长horizon模型的新指南，以防止类似事件再次发生。

值得注意的是，OpenAI确认在此次特定评估中，标准部署防护措施被故意禁用，以进行原始网络能力的压力测试——这一决定目前正在重新审议中。

Hugging Face首席执行官Clem Delangue将此事视为开放协作在AI安全领域的意义验证：“AI安全不可能由任何一家公司秘密解决。它必须在公开环境中，通过协作的方式，让每个地方的每个防御者都能广泛使用AI来解决。”

此次事件表明，前沿AI模型现在能够自主发现并利用新型攻击链，而无需事先了解目标架构。安全团队应：

* 将AI驱动的自主利用视为一种活跃威胁类别，而非未来的风险。
* 审查内部代理和软件包注册表基础设施，以查找类似的缓存相关0Day漏洞。
* 考虑采用可信访问计划，利用AI进行防御性漏洞发现。
* 加强对任何具有高网络权限或凭据访问权限的AI系统的监控。

参考来源：

OpenAI’s GPT Agents Exploit Zero-Days and Hacked Hugging Face Servers

https://cybersecuritynews.com/openai-zero-days-hugging-face/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ptPNnRL9ln6TVtKnqhFaD6lZpyAbLwIM5Fj1m89oyZLopZfbJiaJygvkmWZnicUqiaMDPQFh7zAOptwmFmtCGTNSDFbCOaUfcYc/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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