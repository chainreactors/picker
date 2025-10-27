---
title: 成果分享 | [NDSS'25]复旦大学研究团队发现国内数万款小程序存在严重安全风险
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247491959&idx=1&sn=168138298f43dd7f1713ced2fddb151e&chksm=fde86509ca9fec1fe47c9e06691fcbe8309a98e035deebdd3b1a235da4a9a3b00e0b19809612&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-11-23
fetch_date: 2025-10-06T19:19:15.282219
---

# 成果分享 | [NDSS'25]复旦大学研究团队发现国内数万款小程序存在严重安全风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZkpAOqLKHicno8ibImrCbRnolRfIdPJEty4jPM2YQJZMzWyWQ5UHicMjSg/0?wx_fmt=jpeg)

# 成果分享 | [NDSS'25]复旦大学研究团队发现国内数万款小程序存在严重安全风险

原创

11、yst

复旦白泽战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZgs9JgASQcZvgVNg923mx9A3cs1XszIrYZHv8TYVtFMh866urjOgV7Q/640?wx_fmt=jpeg&from=appmsg)

近年来，依托于超级应用（如微信、支付宝）的小程序逐渐普及，为人们提供出行、购物、娱乐等一系列生活服务，许多政务、医疗平台也开发了小程序提供便民服务。在小程序提供如此多丰富功能时，开发者经常需要调用敏感的API获取敏感信息，这时超级应用会通过“密钥”对开发者的身份进行检验。如果密钥被泄露，那么恶意的攻击者就可以通过该密钥伪装成开发者，从而造成账户劫持、隐私窃取、虚假交易等一系列危害。

【账户劫持】是指攻击者无需输入正确密码即可登录受害者账户。在本文中，攻击者获取小程序泄露的加密密钥后，相当于破解了登录过程中传输的加密数据。由此，攻击者可以使用任意手机号加密发送给服务端，进而劫持小程序内任意用户的账户。

为剖析这一机制，复旦大学杨哲慜老师带领的研究团队对小程序的密钥机制进行了系统研究，并设计和实现了基于语义相似性的密钥泄露自动化检测工具KeyMagnet，对全球6大超级应用平台的40多万个小程序进行了分析，发现了54728个小程序的密钥泄露案例，揭示了目前小程序生态中普遍存在的安全问题。

目前，**该论文已被网络安全领域四大顶会之一NDSS接收**。这项研究系统地分析了小程序的密钥管理生态，及时发现了在小程序快速发展中的密钥泄露风险并提出相应的治理措施，为学界提供了超级应用和小程序之间新的安全研究视角。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZs25djPwPialPMFRNQWvBM7I7YXVTHDsPicZpu114edNu0C7NW9sYShpg/640?wx_fmt=png&from=appmsg)

01

**小程序密钥生态系统**

小程序开发过程中有一套独特的密钥机制，用于身份验证和安全通信。这套机制通常包括三类密钥：访问密钥（用于服务调用）、加密密钥（用于数据通信）以及根密钥（用于生成和管理其他密钥）。

这些密钥的功能贯穿小程序与超级应用平台的交互流程，从生成到使用的每一步都至关重要。然而，小程序生态的复杂性和新颖性，使得密钥的管理和保护面临显著挑战。如果开发者在密钥管理的任何环节出现问题，都可能导致敏感数据暴露，甚至危及整个系统的安全。

密钥机制的安全性是小程序生态赖以运作的基石，但其设计、管理和应用在开发者间的认识参差不齐，使得系统面临复杂的潜在风险。这也是当前研究和实践亟需解决的重要方向。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZQyIfaEKU4mNJJ3faSicTARIcibsCT6hb1jxOTncIGZf4uM9Sy1eKEbKQ/640?wx_fmt=png&from=appmsg)

图

小程序密钥系统及攻击面

**02**

**威胁模型**

在小程序密钥机制中，安全威胁主要来自密钥在生成、传输及使用过程中的不当管理。在威胁模型中，攻击者被假定为具备一定技术能力的恶意用户，能够通过设备控制、小程序代码理解、网络流量拦截等手段获取密钥。一旦获取密钥，攻击者可以通过密钥访问小程序的敏感资源或服务，从而进而实现账户劫持、数据窃取或功能滥用等恶意行为。

**03**

**KeyMagnet设计**

研究团队通过大量人工分析发现，造成小程序密钥泄露的主要原因是部分开发者错误地将本应出现在小程序服务端的密钥行为在客户端使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZRibwicYyFONPEyXWtM3L3CfIicbjrxVicpBdDBj6T2Zib958TwWU4Y8DewA/640?wx_fmt=jpeg&from=appmsg)

图

小程序密钥机制错误实践案例

因此，团队设计并实现了基于语义相似性的密钥泄露自动化检测工具KeyMagent用于检测密钥泄露问题。其设计围绕以下三个核心阶段展开：

**服务器端语义分析：**工具通过解析超级应用开发文档，提取服务器端密钥使用模式，构建“密钥使用语义图”，以揭示密钥的生成、传递和使用逻辑。

**客户端行为分析：**KeyMagnet对小程序客户端代码进行静态与动态分析，提取网络数据流及相关行为，构建“客户端行为图”，捕获潜在的密钥泄露点。

**语义匹配与检测：**工具通过语义图匹配技术，比较服务器端和客户端的密钥语义，识别出客户端中不应存在的敏感操作，进而定位密钥泄露问题。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZxMA2on0FiaoQia1YNg0KDia78z0bbV0dn6JEntibQBavEraVS7NmibHVZ4Q/640?wx_fmt=png&from=appmsg)

图

KeyMagnet工作流

**04**

**实验结果与案例分析**

通过KeyMagnet的检测，团队在413,775个小程序中**发现了54,728个小程序存在密钥泄露问题**，揭示了密钥泄露问题的普遍性和严重性。

 检测的案例中涉及大量高风险场景，例如某支付类小程序的根密钥泄露，攻击者可利用泄露的这些密钥伪造请求，完成未授权支付或窃取用户交易数据。此外，在教育和政务领域，许多小程序的访问密钥泄露，可能导致敏感数据被非法访问和个人账户被直接劫持。甚至，攻击者在获取高权限密钥后，可以调用相关平台API，模仿小程序官方发送虚假公告，进行用户欺诈。

团队在研究过程中，严格遵守学术研究规范，并积极联系相关小程序厂商和超级应用官方，以推动安全漏洞的修复，获得多家厂商感谢。同时团队积极向漏洞平台上报相关漏洞，共获**89个CVE ID、49个CNVD ID。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW85ebDSnFqjgCQ7JFOLoPDFZtwcb44KRic68MXKjdX7bvwxIJRLTPsx22zCvymY7TQmhyPdNQ6sAvJQ/640?wx_fmt=jpeg&from=appmsg)

图

大规模实验数据

**研究团队**

杨哲慜，复旦大学计算机科学技术学院副教授。主要研究方向为程序分析技术和数据与隐私安全。研究领域涉及隐私保护，程序分析和漏洞挖掘技术，操作系统和系统软件，系统安全，程序分析与运行时环境技术。在国际顶级学术会议和重要期刊上发表论文21篇，申报国家发明专利多项。担任IEEE TIFS、ACM CCS 等多个期刊和国际国内学术会议的审稿人。

个人主页：https://yangzhemin.github.io/

史一哲，复旦大学计算机科学技术学院博士研究生，本科毕业于复旦大学计算机科学与技术专业。主要研究方向为新型移动应用的隐私安全与漏洞挖掘等，迄今已发现100多个具有CVE和CNVD编号的零日漏洞。

文案：刘定一

排版：虞舒甜

责编：邬梦莹

审核：张琬琪、洪赓、林楚乔

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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