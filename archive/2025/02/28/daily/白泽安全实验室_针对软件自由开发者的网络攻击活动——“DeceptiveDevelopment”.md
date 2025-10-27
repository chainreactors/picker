---
title: 针对软件自由开发者的网络攻击活动——“DeceptiveDevelopment”
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492556&idx=1&sn=caeb4bd6ed9e5101b86a176c28f728bf&chksm=e90dc9e6de7a40f0379b92fde69b9941c22cb102b3b936546c0ead5678b0498466f2273f2d93&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-02-28
fetch_date: 2025-10-06T20:39:21.939634
---

# 针对软件自由开发者的网络攻击活动——“DeceptiveDevelopment”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 针对软件自由开发者的网络攻击活动——“DeceptiveDevelopment”

BaizeSec

白泽安全实验室

**一、事件概述**

近期，ESET研究团队发现了一起针对自由软件开发者的网络攻击活动，代号为“DeceptiveDevelopment”。该攻击活动疑似由朝鲜相关的网络犯罪分子发起，主要通过伪装成招聘人员，利用虚假的工作机会引诱受害者，进而传播恶意软件，窃取加密货币钱包信息以及浏览器和密码管理器中的登录信息。

自2023年11月以来，DeceptiveDevelopment攻击活动一直活跃至今。该攻击活动主要针对全球范围内的自由软件开发者，尤其是那些参与加密货币和去中心化金融项目的专业人士。攻击者通过在招聘和自由职业网站上发布虚假招聘信息或直接联系受害者，诱导他们参与所谓的“编程测试”或“修复漏洞任务”，并提供带有恶意代码的项目文件。一旦受害者下载并执行这些文件，其计算机就会被植入初始阶段的恶意软件——BeaverTail。

#### **二、技术分析**

DeceptiveDevelopment攻击活动主要涉及两种恶意软件家族：BeaverTail（信息窃取器和下载器）和InvisibleFerret（信息窃取器和远程访问木马）。以下是该活动的技术分析细节：

**（1）初始入侵**

* 攻击者通过创建虚假的招聘人员资料，在LinkedIn、Upwork、Freelancer.com等招聘和自由职业网站上发布虚假招聘信息或直接联系目标受害者。
* 他们以“招聘挑战”或“修复漏洞任务”为由，向受害者提供带有恶意代码的项目文件。这些文件通常托管在GitHub、GitLab或Bitbucket等平台的私有仓库中。
* 受害者被要求下载文件、添加功能或修复漏洞，并在执行项目时触发初始入侵。恶意代码通常被隐藏在项目中，通过长注释将代码推到屏幕外，使其难以被发现。

**（2）恶意软件分析**

* BeaverTail：作为初始阶段的恶意软件，BeaverTail用于窃取浏览器保存的登录信息和加密货币钱包数据，并下载第二阶段的恶意软件——InvisibleFerret。
* InvisibleFerret：这是一款模块化的Python恶意软件，具有信息窃取和远程控制功能。它包括主模块、负载模块、浏览器模块和AnyDesk模块，能够窃取浏览器数据、执行远程命令，并通过AnyDesk实现持久化访问。

**（3）网络基础设施**

* DeceptiveDevelopment的C2（命令与控制）服务器主要由商业托管提供商托管，使用的端口包括1224、1244和1245等非标准端口。
* 该活动的C2服务器通过HTTP和TCP套接字与受感染系统通信，用于数据窃取和恶意软件模块的分发。

**三、影响与建议**

DeceptiveDevelopment攻击活动展示了网络犯罪分子如何利用招聘平台和自由职业者的信任来传播恶意软件。研究人员提醒自由软件开发者在参与在线招聘和项目合作时保持警惕，避免下载和执行未经验证的项目文件。此外，建议开发者使用安全工具和反病毒软件来检测和防范此类攻击。

参考链接：

https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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