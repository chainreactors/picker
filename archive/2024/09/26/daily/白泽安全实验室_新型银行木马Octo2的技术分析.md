---
title: 新型银行木马Octo2的技术分析
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492340&idx=1&sn=047ecc131f9b71eb8e7d5180bb5c21f8&chksm=e90dc8dede7a41c8749a2faafe9f50b8c321b95de89fed25e2cc7848166e3d1874a6b2a178aa&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-09-26
fetch_date: 2025-10-06T18:30:31.406936
---

# 新型银行木马Octo2的技术分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型银行木马Octo2的技术分析

BaizeSec

白泽安全实验室

**一、背景概述**

Octo恶意软件家族的首个样本可以追溯到2016年，当时它主要通过覆盖攻击和控制电话、短信以及推送通知来实施银行诈骗。这种攻击方式使得用户在不知情的情况下，其银行账户信息被窃取，资金被非法转移。2019年，其轻量级版本“ExobotCompact”在地下论坛上被推广，进一步扩大了其攻击范围和能力。2021年该家族的新变种被发现，2022年一个名为“Octo”的神秘移动恶意软件家族在地下论坛上首次被提及。2024年随着源代码的泄露，一个新的版本“Octo2”被原始威胁行为者发布，其攻击目标直指银行用户。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINAZHrVrZEjbbka1m9w1TiaoicETlHmFUMSOj1VxKUXyoBfbIKjkjsBrnlW716QRTMEKBcdGMjmhmpA/640?wx_fmt=png&from=appmsg)

**二、Octo2新版本技术特点分析**

根据ThreatFabric的最新报告，Octo2具有以下特点：

**稳定性提升：**开发者增强了远程操作的稳定性，以支持设备接管攻击，使得攻击者能够更有效地控制受害者的设备，进行银行转账等操作。

**地理分布：**新的Octo2活动已经在意大利、波兰、摩尔多瓦和匈牙利等欧洲国家被发现，表明其攻击目标已经扩展到全球多个地区的银行用户。

**复杂性增加：**Octo2采用了复杂的混淆技术，包括引入了域名生成算法 （DGA），以确保木马在不被检测的情况下保持活跃，进一步增加了银行用户识别  和防御的难度。

**三、Octo2新版本攻击过程的技术细节分析：**

**初始感染：**Octo2通过Zombinder作为第一阶段的安装，诱导用户安装所谓的“插件”，实际上是Octo2本身，从而绕过了Android 13+的限制。这种策略使得银行用户在下载看似合法的应用程序时，实际上已经安装了恶意软件。

**远程操作：**Octo2更新了其远程访问工具（RAT）的功能，以提高远程会话期间的稳定性和减少连接延迟。开发者引入了一个特定的远程会话设置“SHIT\_QUALITY”，通过减少传输到C2的数据量来提高连接的稳定性，使得攻击者能够更流畅地控制受害者的银行操作。

**反检测与混淆技术：**Octo2在执行过程中采用了多步骤混淆技术，包括解密和动态加载额外的原生库，该库负责解密恶意负载、生成加密密钥和C2域名。这种复杂的技术使得安全软件难以检测和分析其行为。

**C2通信与域名生成算法（DGA）：**Octo2使用DGA生成实际的C2服务器名称，允许网络犯罪分子在不重新生成样本的情况下动态更新域名。此外，Octo2为每个C2请求生成新的加密密钥，提高了通信的安全性。

**拦截通知：**Octo2的设置中包含了多个应用程序和应用的列表，表明攻击者已经准备攻击这些应用的用户。一旦Octo2检测到列表中的应用程序的推送通知，它将拦截该通知，不向受害者显示，从而隐藏其恶意行为。

**四、附录：IOC指标**

|  |  |  |
| --- | --- | --- |
| Hash (SHA256) | 应用名称 | 包名称 |
| 83eea636c3f04ff1b46963680eb4bac7177e77bbc40b0d3426f5cf66a0c647ae | NordVPN | com.handedfastee5 |
| 6cd0fbfb088a95b239e42d139e27354abeb08c6788b6083962943522a870cb98 | Europe Enterprise | com.xsusb\_restore3 |
| 117aa133d19ea84a4de87128f16384ae0477f3ee9dd3e43037e102d7039c79d9 | Google Chrome | com.havirtual06numberresources |

参考链接：

https://securityaffairs.com/168857/malware/octo2-android-banking-trojan.html

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