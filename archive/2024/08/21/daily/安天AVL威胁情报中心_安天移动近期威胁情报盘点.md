---
title: 安天移动近期威胁情报盘点
url: https://mp.weixin.qq.com/s?__biz=Mzk0NDM1MDkyNw==&mid=2247546908&idx=2&sn=2b79eb404f713bd73f54cf2c65bb52a5&chksm=c3278bbcf45002aa25b9bd7986bc718571aff6be97501bb9e5e4403a0a2eab0cfdad6288ce0d&scene=58&subscene=0#rd
source: 安天AVL威胁情报中心
date: 2024-08-21
fetch_date: 2025-10-06T18:05:09.285222
---

# 安天移动近期威胁情报盘点

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yqiahzBqjR7gLeUMhw0DCcNHHMhGe4a60FYibdlAp3DyhEW4tNQibPxhfMJDERicTfPONQuCD9nq6U6E8n5UlRH1zw/0?wx_fmt=jpeg)

# 安天移动近期威胁情报盘点

AVL威胁情报团队

安天AVL威胁情报中心

![](https://mmbiz.qpic.cn/mmbiz_gif/LianbibNTn3Ns455IPTPVwfkoibGedrmpxn8FnwlbKLur87Z6HRrjYicNN8lhdgzTEPiak9AYO5HslVhvNXicKAgWeGA/640?wx_fmt=gif)

本期导读：

**移动安全**

● Mandrake间谍软件再次潜入Google Play长达两年之久

● 变色龙银行木马伪装成CRM应用程序卷土重来

● Android 间谍软件 LianSpy 使用 Yandex Cloud 逃避检测

● 新的安卓木马“BlankBot”针对土耳其用户的财务数据

● 动态进化的短信窃取者威胁全球Android用户

**APT事件**

●  加密货币诱饵和 Pupy RAT针对中国实体经济攻击活动

● 摩诃草 (APT-Q-36) Spyder下载器新变种及后续组件分析

● 韩国“伪猎者”APT组织利用多款国产化软件漏洞对中国的攻击活动

● Konni APT利用AutoIt技术针对特定领域展开精密攻击

● APT 组织 Kimsuky 瞄准大学研究人员

● Kimsuky和Andariel瞄准首尔的建筑业

**漏洞新闻**

● 微软发现 OpenVPN 漏洞，可通过连锁实现 RCE 和 LPE

● 研究人员发现谷歌文件传输工具中的 10 个漏洞

● 研究人员称黑客可利用 5G 基带漏洞监视手机用户

**IoT安全**

**●**中国科沃斯家用机器人可能被黑客入侵，用来监视主人

**●**Sonos智能扬声器存在窃听用户的漏洞

**数据安全**

● 前美国国家安全局工作人员：美国国家安全局数据泄露的幕后黑手可能是流氓内部人士

● 韩国国防公司无意泄露朝鲜军事机密

● 黑客泄露了27亿条带有社会安全号码的数据记录

● 以色列士兵泄露绝密军事基地数据及风险分析

##

01

移动安全

**01 Mandrake间谍软件再次潜入Google Play长达两年之久**

从2022年到2024年，多达5个携带Mandrake间谍软件的应用程序在Google Play上可用，总安装量已超3.2万次，却未被任何其他供应商发现。这些新样本采用了高级混淆与规避技术，包括将恶意功能转移到使用OLLVM混淆的本地库中，实施证书绑定以确保与命令与控制（C2）服务器的安全通信，以及进行广泛检查以判断Mandrake是否在已获取root权限的设备或模拟环境中运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yqiahzBqjR7hPDAAKqDINLElbsG8nXVUkpwzGG99p9PMdlibxlOOhfJYxc2ugPaUb6P2wGgWw8kXpxCT381KJ5LQ/640?wx_fmt=png&from=appmsg)

详细信息：

http://www.freebuf.com/articles/paper/407904.html

**02 变色龙银行木马伪装成CRM应用程序卷土重来**

变色龙安卓银行木马重新回到威胁现场，配备了新的Android安全绕过功能。该恶意软件伪装成客户关系管理（CRM）应用程序，针对加拿大和欧洲的酒店业员工和其他商业员工。新变种使用了一种滴管，可以绕过Android 13+Accessibility Service的限制。

详细信息：

https://www.darkreading.com/endpoint-security/chameleon-banking-trojan-makes-a-comeback-cloaked-as-crm-app

**03 Android 间谍软件 LianSpy 使用 Yandex Cloud 逃避检测**

LianSpy使用俄罗斯云服务 Yandex Cloud 进行命令和控制 （C2） 通信，作为避免拥有专用基础设施和逃避检测的一种方式。带有恶意软件的应用程序伪装成支付宝或 Android 系统服务。LianSpy 一旦激活，它就会确定它是否作为系统应用程序运行，以使用管理员权限在后台运行，或者请求广泛的权限，允许它访问联系人、通话记录和通知，并在屏幕上绘制叠加层。

详细信息：

https://www.anquanke.com/post/id/298909

**04 新的安卓木马“BlankBot”针对土耳其用户的财务数据**

BlankBot于2024年7月24日被发现，据说正在积极开发中，该恶意软件滥用Android的可访问性服务权限，以获得对受感染设备的完全控制。该木马具有一系列恶意功能，包括客户注入、键盘记录、屏幕录制，并通过WebSocket连接与控制服务器通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yqiahzBqjR7hPDAAKqDINLElbsG8nXVUkmbAYvaep1icJibFjFfkq80UjWiaN1XPJKM8lJoWdq1keI3z6nUZBGU0zg/640?wx_fmt=png&from=appmsg)

详细信息：

https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html

**05 动态进化的短信窃取者威胁全球Android用户**

一种新型恶意软件，拥有超过107000个样本，已被针对Android设备两年多来，黑客一直在窃取短信以获取一次性密码（OTP）和其他敏感用户数据，以进行进一步的恶意活动。这些被盗凭证成为进一步欺诈活动的跳板，例如在流行服务上创建虚假帐户发起网络钓鱼活动或者社会工程攻击。

详细信息：

https://www.darkreading.com/endpoint-security/dynamically-evolving-sms-stealer-threatens-global-android-users

02

APT事件

**01 加密货币诱饵和 Pupy RAT针对中国实体经济攻击活动**

最近发现了与 UTG-Q-010 相关的样本，该样本针对加密货币爱好者，采用复杂的网络钓鱼攻击，涉及包含恶意 LNK 文件的 zip 文件。此 LNK 文件伪装成与 Michelin 合作举办的加密货币相关会议的诱人活动邀请，执行命令以解密并在系统中释放加载程序 DLL。加载程序配备了先进的规避技术，可检测沙盒环境并确保稳定的互联网连接，然后下载和解密最终有效载荷（该有效载荷被标识为 Open Source PupyRAT）

详细信息：

https://cyble.com/blog/analysing-the-utg-q-010-campaign/

**02摩诃草 (APT-Q-36) Spyder下载器新变种及后续组件分析**

近期发现 Spyder 下载器出现新变种，并观察到攻击者借助 Spyder 下发两款窃密组件，分别用于截屏和收集文件信息。虽然 Spyder 下载器的核心功能没变，仍是从远程下载的加密 ZIP 包中释放出后续组件并执行，但在代码结构和 C2 通信格式等方面做了一些改动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yqiahzBqjR7hPDAAKqDINLElbsG8nXVUkphV7uJT43px3Dfibwp7S7icHFHZVXoxxWzCm4libR7VFF1G07etFqsIkg/640?wx_fmt=png&from=appmsg)

详细信息：

https://mp.weixin.qq.com/s/M6xoCfqMCSDsv32S0vrGEw

**03 韩国“伪猎者”APT组织利用多款国产化软件漏洞对中国的攻击活动**

在本次攻击过程中，攻击者使用的漏洞，或是Windows平台下，中国大陆地区流行的办公软件漏洞：WPS表格漏洞和Foxmail邮件程序漏洞，或是中国大陆地区广泛使用的163邮箱的漏洞。这些漏洞对大陆地区用户针对性强，影响范围广泛；所用漏洞是逻辑漏洞，漏洞触发稳定，危险程度高。

详细信息：

https://mp.weixin.qq.com/s/F8hNyESBdKhwXkQPgtGpew

**04 Konni APT利用AutoIt技术针对特定领域展开精密攻击**

攻击的初始入口是通过一封伪装成税务调查的钓鱼邮件，邮件中附带的ZIP压缩包看似包含税务相关的文件，实则隐藏着一个经过精心伪装的LNK文件，一旦用户点击，便触发了攻击的序幕。LNK文件内部嵌入的AutoIt脚本是此次攻击的核心。AutoIt是一款功能强大的自动化工具，它能够模拟用户的各种输入操作。攻击者通过AutoIt编写的脚本，不仅实现了对受害者计算机的远程控制，还巧妙地规避了安全软件的检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yqiahzBqjR7hPDAAKqDINLElbsG8nXVUkdS530l4TFWM3OOjLhyp7BgxwNibe2symCxlwS8v7iaEBx3Fib7wvheNTQ/640?wx_fmt=png&from=appmsg)

详细信息：

https://www.genians.co.kr/blog/threat\_intelligence/autoit

**05 APT 组织 Kimsuky 瞄准大学研究人员**

2024 年 7 月下旬，分析师发现威胁行为者 Kimsuky 犯了一个操作安全 (OPSEC) 错误，从而利用这一点集了大量源代码、登录凭据、流量日志和内部笔记。根据我们收集的数据，我们评估 Kimsuky 正在钓鱼大学员工、研究人员和教授进行间谍活动。一旦进入大学网络，Kimsuky 就可以窃取朝鲜政府的研究和情报。

详细信息：

https://www.cyberresilience.com/threatintel/apt-group-kimsuky-targets-university-researchers/

**06 Kimsuky和Andariel瞄准首尔的建筑业**

韩国政府机构警告称，自1月以来，两个著名的朝鲜黑客组织Kimsuky和Andariel一直针对韩国的建筑和机械行业，窃取机密信息，以帮助该国实现城市和工厂的现代化。包括国家警察局、国家情报局和网络作战司令部在内的几个韩国机构，说在一份联合网络安全咨询中，朝鲜两个网络间谍组织Kimsuky和Andariel利用网站和软件供应链漏洞感染了建筑和机械组织的系统。

详细信息：

https://www.govinfosecurity.com/kimsuky-andariel-target-seouls-construction-industry-a-25961

03

漏洞新闻

**01 微软发现 OpenVPN 漏洞，可通过连锁实现 RCE 和 LPE**

研究人员披露了开源项目 OpenVPN 中多个中等严重性的 bug，这些 bug 可以链接以实现远程代码执行 （RCE） 和本地权限提升 （LPE）。攻击者可以利用这些漏洞来完全控制目标端点，从而可能导致数据泄露、系统泄露和未经授权访问敏感信息。

详细信息：

https://www.anquanke.com/post/id/299054

**02 研究人员发现谷歌文件传输工具中的 10 个漏洞**

在 Google 适用于 Android 和 Windows 的 Quick Share 数据传输实用程序中发现了多达 10 个安全漏洞，这些漏洞可能被塑造成一个“创新和非常规”的 RCE 攻击链，以在 Windows 主机上运行任意代码。RCE 攻击链的代号为 QuickShell。这些缺点包括六个远程拒绝服务 （DoS） 漏洞、两个未经授权的文件写入错误，每个错误都在 Android 和 Windows 版本的软件中被识别出来，一个目录遍历和一个强制 Wi-Fi 连接的情况。

详细信息：

https://www.anquanke.com/post/id/299027

**03 研究人员称黑客可利用 5G 基带漏洞监视手机用户**

一组研究人员表示，他们发现了不同 5G 基带（本质上是手机用于连接移动网络的处理器）中的一系列安全漏洞，这些漏洞可能让黑客可以秘密入侵受害者并监视他们。

详细信息：

https://techcrunch.com/2024/08/07/hackers-could-spy-on-cellphone-users-by-abusing-5g-baseband-flaws-researchers-say/?guccounter=1

04

IOT安全

**01 中国科沃斯家用机器人可能被黑客入侵，用来监视主人**

存在一个漏洞，任何人只要使用手机，就能通过蓝牙从 450 英尺（约 130 米）远的地方连接并控制科沃斯机器人。一旦黑客控制了该设备，他们就可以远程连接，因为机器人本身通过 Wi-Fi 连接到互联网。

详细信息：

https://techcrunch.com/2024/08/09/ecovacs-home-robots-can-be-hacked-to-spy-on-their-owners-researchers-say/

**02 Sonos智能扬声器存在窃听用户的漏洞**

研究人员在Sonos智能扬声器中发现了多个漏洞，其中包括一个被追踪为CVE-2023-50809的漏洞，该漏洞可能允许窃听用户。供应商在Sonos S2 15.9版本中解决了该漏洞，并通知客户没有可用的解决方法。

详细信息：

https://securityaffairs.com/166823/hacking/sonos-smart-speakers-flaw.html

05

数据安全

**01 前美国国家安全局工作人员：美国国家安全局数据泄露的幕后黑手可能是流氓内部人士**

美国国家安全局相关组织使用的大量黑客工具被泄露，内部人员可能直接从 NSA 窃取这些文件，就像 NSA 前承包商雇员爱德华·斯诺登窃取大量绝密文件一样。而这种理论是由一位自称是 NSA 前内部人员的人提出的。内部人员获取影子经纪人在网上发布的数据要比其他人（甚至是俄罗斯）远程窃取数据容易得多。他辩称，“文件目录的命名约定以及转储中的一些脚本只能在内部访问”，并且“没有理由”将这些文件放在有人可以入侵的服务器上。

详细信息：

https://www.vice.com/en/article/former-nsa-staffers-rogue-insider-shadow-brokers-theory/

**02 韩国国防公司无意泄露朝鲜军事机密**

韩国表示，朝鲜黑客窃取了该国关键军事技术的机密信息。据该国称，网络犯罪分子窃取了K2主战坦克以及Baekdu和Geumgang侦察机的重要数据。泄漏可能会对朝鲜的国防能力造成严重影响，因为朝鲜将能够利用这一信息开发低能见度无人机和有效的规避措施。

详细信息：

https://www.securitylab.ru/news/551070.php

**03 黑客泄露了27亿条带有社会安全号码的数据记录**

一个黑客论坛上泄露了近27亿条美国人民的个人信息记录，暴露了他们的姓名、社会安全号码、所有已知的物理地址和可能的别名。这些数据来自国家公共数据公司，该公司收集和出售个人数据，用于背景调查、获取犯罪记录和私人调查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yqiahzBqjR7hPDAAKqDINLElbsG8nXVUkvl4nJd5Y2H6PyxlsVVtV2fEphUKRln89hiaJHDn7bdnOkhHPib9KevCg/640?wx_fmt=png&from=appmsg)

详细信息：

https://www.bleepingcomputer.com/news/security/hackers-leak-27-billion-data-records-with-social-security-numbers/

**04 以色列士兵泄露绝密军事基地数据及风险分析**

士兵和平民在敏感安全区域使用智能手机和智能手表等可穿戴设备时，无意中泄露了关键的军事基地和人员信息。尽管这些基地的位置已为公众所知，但通过这些设备泄露的信息足以让潜在的敌对势力识别并收集在基地服役的士兵的详细信息。然后可能通过跟踪、监视，甚至采取勒索或伤害等手段来针对这些士兵。

详细信息：

https://www.haaretz.com/israel-news/security-aviation/2024-08-08/ty-article/.premium/israeli-soldiers-at-sensitive-security-sites-reveal-their-identity-and-location-online/00000191-326a-d9ba-a5df-7a7b855a0000

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yqiahzBqjR7gkcgbzzYtOTMXiaY4MswTaLxxfGWQThj4AKTXX6E8tPjZea58tx5DLMnvKt2qOzQkAACGUmLt6YeQ/0?wx_fmt=png)

安天AVL威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yqiahzBqjR7gkcgbzzYtOTMXiaY4MswTaLxxfGWQThj4AKTXX6E8tPjZea58tx5DLMnvKt2qOzQkAACGUmLt6YeQ/0?wx_fmt=png)

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