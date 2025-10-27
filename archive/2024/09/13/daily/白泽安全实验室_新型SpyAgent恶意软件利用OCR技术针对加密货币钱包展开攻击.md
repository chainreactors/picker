---
title: 新型SpyAgent恶意软件利用OCR技术针对加密货币钱包展开攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492321&idx=1&sn=20a27b2ce118647d449508531b6a4451&chksm=e90dc8cbde7a41dd5844476e56bfbe582408b0a63b89bee5ca291607a91bb0806586cc3b7a12&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-09-13
fetch_date: 2025-10-06T18:29:49.056605
---

# 新型SpyAgent恶意软件利用OCR技术针对加密货币钱包展开攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型SpyAgent恶意软件利用OCR技术针对加密货币钱包展开攻击

BaizeSec

白泽安全实验室

**事件概述：**

近日，网络安全厂商McAfee研究人员发现了一种新型恶意软件SpyAgent，它利用光学字符识别（OCR）技术从用户的设备中窃取加密货币钱包的助记词密钥。这一发现揭示了朝鲜黑客组织对加密货币用户的新威胁。

**技术分析过程：**

* **传播机制：**这种恶意软件主要通过精心设计的网络钓鱼活动传播，这些活动通过短信或社交媒体发送带有恶意链接的消息。攻击者通常伪装成用户信任的组织或个人，诱使用户点击链接并下载伪装成合法应用的APK文件，从而在用户设备上安装恶意软件。
* **应用安装与权限请求：**用户在下载并安装这些看似合法的APK文件后，恶意应用会请求访问短信、联系人和存储等敏感信息的权限。这些权限被恶意软件用来窃取用户数据，并在后台运行，以避免用户察觉。
* **恶意软件功能与行为：**SpyAgent一旦安装，便开始秘密收集用户的联系人列表、短信和照片，并将其发送到攻击者控制的远程服务器。此外，该恶意软件还能接收和执行来自远程服务器的指令，包括改变设备设置和发送短信。
* **命令和控制服务器调查：**研究人员在调查中发现，SpyAgent使用的命令和控制服务器存在安全配置弱点，导致服务器的内部组件和受害者的敏感个人数据被公开暴露。服务器的管理页面显示，攻击者的主要目标是获取加密货币钱包的助记词恢复短语。
* **攻击技战术演变：**SpyAgent最初通过简单的HTTP请求与C2服务器通信，但现在已经升级到使用WebSocket连接，以实现更高效的实时双向交互，并规避传统的基于HTTP的网络监控工具的检测。

**SpyAgent的影响范围：**

虽然SpyAgent最初在韩国活动，但其影响范围已经扩展到包括英国在内的其他国家。这种恶意软件的伪装技巧和实时通信能力的增强，使其成为一个全球性的威胁。

**防御策略建议：**

用户在安装应用程序和授予权限时应格外谨慎。建议用户将重要信息安全存储，并与设备隔离。安装可靠的安全软件已成为保护设备免受这类威胁的必要措施。

**附件：Indicators of Compromise**

**SHA256 Hash(es):**

5b634ac2eecc2bb83c0403edba30a42cc4b564a3b5f7777fe9dada3cd87fd761

4cf35835637e3a16da8e285c1b531b3f56e1cc1d8f6586a7e6d26dd333b89fcf

3d69eab1d8ce85d405c194b30ac9cc01f093a0d5a6098fe47e82ec99509f930d

789374c325b1c687c42c8a2ac64186c31755bfbdd2f247995d3aa2d4b6c1190a

34c2a314dcbb5230bf79e85beaf03c8cee1db2b784adf77237ec425a533ec634

f7c4c6ecbad94af8638b0b350faff54cb7345cf06716797769c3c8da8babaaeb

94aea07f38e5dfe861c28d005d019edd69887bc30dcc3387b7ded76938827528

1d9afa23f9d2ab95e3c2aecbb6ce431980da50ab9dea0d7698799b177192c798

19060263a9d3401e6f537b5d9e6991af637e1acb5684dbb9e55d2d9de66450f2

0ca26d6ed1505712b454719cb062c7fbdc5ae626191112eb306240d705e9ed23

d340829ed4fe3c5b9e0b998b8a1afda92ca257732266e3ca91ef4f4b4dc719f8

149bd232175659434bbeed9f12c8dd369d888b22afaf2faabc684c8ff2096f8c

f9509e5e48744ccef5bfd805938bf900128af4e03aeb7ec21c1e5a78943c72e7

26d761fac1bd819a609654910bfe6537f42f646df5fc9a06a186bbf685eef05b

0e778b6d334e8d114e959227b4424efe5bc7ffe5e943c71bce8aa577e2ab7cdb

8bbcfe8555d61a9c033811892c563f250480ee6809856933121a3e475dd50c18

373e5a2ee916a13ff3fc192fb59dcd1d4e84567475311f05f83ad6d0313c1b3b

7d346bc965d45764a95c43e616658d487a042d4573b2fdae2be32a0b114ecee6

1bff1823805d95a517863854dd26bbeaa7f7f83c423454e9abd74612899c4484

020c51ca238439080ec12f7d4bc4ddbdcf79664428cd0fb5e7f75337eff11d8a

**Domain(s):**

ahd.lat

allsdy999.org

etr.lat

gf79.org

goodapps.top

gov24.me

gov24.top

krgoodapp.top

krgov24.top

like1902.xyz

make69.info

messtube999.info

mtube888.info

mylove777.org

oktube999.info

top1114.online

ytube888.info

参考链接：

https://www.mcafee.com/blogs/other-blogs/mcafee-labs/new-android-spyagent-campaign-steals-crypto-credentials-via-image-recognition/

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