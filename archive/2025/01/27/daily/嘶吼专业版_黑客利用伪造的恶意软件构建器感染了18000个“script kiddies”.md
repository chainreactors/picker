---
title: 黑客利用伪造的恶意软件构建器感染了18000个“script kiddies”
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580992&idx=1&sn=d64510306e9db3532091d13213d4b0ef&chksm=e9146d7ade63e46c7077b4b663c858f41dc3369b4ed1d4dadd5718249441857a6a2dbd2bc693&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-27
fetch_date: 2025-10-06T20:09:02.963591
---

# 黑客利用伪造的恶意软件构建器感染了18000个“script kiddies”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSg98tHbUgT933rBo9X9SHrbdFibicC5iaBZtKlvJZEIaqv52ic1RzMEMb5Q/0?wx_fmt=jpeg)

# 黑客利用伪造的恶意软件构建器感染了18000个“script kiddies”

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

黑客分子利用伪造的恶意软件构建器，以被称为 “script kiddies（脚本小子）” 的低技能黑客为目标，通过后门秘密感染他们，以窃取数据并接管其计算机。

CloudSEK 的安全研究人员报告称，该恶意软件感染了全球 18,459 台设备，其中大部分位于俄罗斯、美国、印度、乌克兰和土耳其。CloudSEK 报告中写道：“XWorm RAT 构建器的木马版本已被武器化并传播。” CloudSEK 发现该恶意软件包含一个终止开关，该开关被激活以从许多受感染的计算机上卸载恶意软件，但由于实际限制，某些计算机仍然受到损害。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaS35qFX9mibyC0Uc0WLm3S7N3ntbuILR9Y2UrM3Vh1ciboh1hfawSbdu2g/640?wx_fmt=png&from=appmsg)

受感染设备的位置

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSic0j7jJvZYAeNz2mh4T8bDpNeUpNJ7FQkHVekKaFjibWh8m4KoPCibAKA/640?wx_fmt=png&from=appmsg)假 RAT 构建器安装恶意软件

研究人员表示，他们最近发现了一个木马化的 XWorm RAT 构建器通过各种渠道分发，包括 GitHub 存储库、文件托管平台、Telegram 频道、YouTube 视频和网站。这些消息来源宣传了 RAT 构建器，称它将允许其他威胁者利用该恶意软件而无需付费。

它是用恶意软件感染受害者设备，一旦计算机感染了机器，X虫恶意软件就会检查Windows注册表是否有迹象是否在虚拟化环境上运行，如果结果为正面，则停止。如果主机有资格获得感染，则恶意软件会执行所需的注册表修改，以确保系统启动之间的持久性。每个受感染的系统都使用硬编码的电报机器人ID和令牌注册为基于电报的命令和控制服务器（C2）服务器。

恶意软件还会自动窃取Diskord令牌，系统信息和位置数据（来自IP地址），并将其删除到C2服务器。然后，它等待运营商的命令。在总共支持的56个命令中，以下特别危险：

**·**/machine\_id\*browsers – 从网络浏览器窃取保存的密码、cookie 和自动填充数据

**·**/machine\_id\*keylogger – 记录受害者在计算机上输入的所有内容

**·**/machine\_id\*desktop – 捕获受害者的活动屏幕

**·**/machine\_id\*encrypt\*

**·**/machine\_id\*processkill\*

**·**/machine\_id\*上传\*

**·**/machine\_id\*uninstall – 从设备中删除恶意软件

CloudSEK 发现恶意软件操作者从大约 11% 的受感染设备中窃取了数据，主要是截取受感染设备的屏幕截图（如下所示）并窃取浏览器数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSHiaaPcIPSiaoeicyy6HaG8qPaOz2UaqrfERnGgrkno4pu8vAcj37dria1Q/640?wx_fmt=png&from=appmsg)

来自黑客桌面的屏幕截图

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSic0j7jJvZYAeNz2mh4T8bDpNeUpNJ7FQkHVekKaFjibWh8m4KoPCibAKA/640?wx_fmt=png&from=appmsg)利用开关破坏僵尸网络

Cloudsek的研究人员通过使用硬编码的API令牌和内置的杀伤开关来破坏僵尸网络，从而从受感染的设备中卸载了恶意软件。

为此，他们向所有听众客户端发送了一个大规模卸载命令，遍历以前从电报日志中提取的所有已知机器ID。他们还假设一个简单的数字模式，从1到9999刻录了机器ID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSFTI94HgeeQNmewLfDDLXRaIdB1sGVb8JNb0YVVdaXmyluguUDFMZDg/640?wx_fmt=png&from=appmsg)

发送卸载命令

尽管这导致恶意软件被从许多受感染的机器中删除，但在发出命令时未在线的机器仍被操控。此外，某些卸载命令可能在运输中丢失，这是一种常见情况。

参考及来源：https://www.bleepingcomputer.com/news/security/hacker-infects-18-000-script-kiddies-with-fake-malware-builder/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSGgwttq0zs7BVkyC3YACmQ5RFmCpxfe45BhooDdVEibLicJCVbiak1Xia9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSuQG6kCJppBXs6DM1Cz0LwbgCniag7Psiaf9IEqCqn4bicTlAJl8Pfbvtw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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