---
title: Zyxel发现不良签名更新导致防火墙关键错误
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581007&idx=1&sn=d816fadcd7aacae25c4e6df6c203c7ce&chksm=e9146d75de63e46300ac77d7944c1196eb7ffb29dced21613686efb2d745b28150ff8e9c1efa&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-06
fetch_date: 2025-10-06T20:36:27.212282
---

# Zyxel发现不良签名更新导致防火墙关键错误

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28nkJxr1hib0duLABkWodJVdEoDTicJWF4xzIOkSiaNXpibcIdTpH1zurq2ZxNbhNOEoWpgpo2K14bEOA/0?wx_fmt=jpeg)

# Zyxel发现不良签名更新导致防火墙关键错误

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Zyxel 发现不良的安全签名更新正在引起USG Flex或ATP系列防火墙的关键错误，包括将设备放入启动循环中。

Zyxel 表示，这些问题是由于其网络安全功能的应用程序签名更新失败造成的。收到错误更新的设备现在的问题包括：

**·**设备错误：CLI 命令错误、设备超时或设备注销。

**·**无法通过 Web GUI 登录 ATP/USG FLEX：504 网关超时。

**·**CPU 使用率高。

**·**在“监控”>“日志”中，出现消息“ZySH daemon is busy”。

**·**无法在控制台上输入任何命令。

**·**Coredump 消息出现在控制台上。

Zyxel 表示，只有具有有效安全许可证的 USG FLEX 或 ATP 系列（ZLD 固件版本）防火墙受到影响，Nebula平台或USG FLEX H（uOS）系列设备不受影响。解决该问题的唯一方法是物理访问防火墙并通过 RS232 串行电缆连接到控制台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28nkJxr1hib0duLABkWodJVdkqG6GIhySFgczRT9fpNrL1Amjwk1XafNibEspbDR2vQS0JbnX9MKsWg/640?wx_fmt=png&from=appmsg)

错误更新后 Zyxel 上显示错误

管理员现在需要进行一系列步骤来恢复防火墙，包括备份配置，下载和应用特殊固件，然后通过Web GUI连接以恢复后面的配置文件。

随后，Zyxel 分享了详细的步骤，并强烈建议用户在尝试恢复设备之前对其进行安全审查。

参考及来源：https://www.bleepingcomputer.com/news/security/zyxel-warns-of-bad-signature-update-causing-firewall-boot-loops/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28nkJxr1hib0duLABkWodJVdZnPE22x4iaubniaHUKE8ZPS531fH5xIVeiaPqgK93xiaZbj1EJ0aYc9Ang/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28nkJxr1hib0duLABkWodJVdbPaalIX3G3Rk6L82AGXBt1Pe6WzsyoVTNx155eF0Ylp1CePOcJpq9Q/640?wx_fmt=png&from=appmsg)

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