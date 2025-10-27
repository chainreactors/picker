---
title: 警惕！黑客组织正在假冒CrowdStrike公司进行恶意攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546023&idx=4&sn=2ecf368b0143f5e3d1a0ccf7831d4065&chksm=fa938266cde40b70e3078d873a51eac355dbd2aa125c9cd8a32f6de4602e6cf1dc0cde2edc9c&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-25
fetch_date: 2025-10-06T17:44:15.030356
---

# 警惕！黑客组织正在假冒CrowdStrike公司进行恶意攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nVLdoSAZoGfib9OFhdy7p7jeJFdfAP5q6fnMnicH0BeUkibknas6fXiciavXznfibKvE5xCPY7CzUftJvQ/0?wx_fmt=jpeg)

# 警惕！黑客组织正在假冒CrowdStrike公司进行恶意攻击

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176nVLdoSAZoGfib9OFhdy7p7jatGzbDI8zcuVQjWnkibZwa1ImVYqpWJ44ec5IMakibtiaCxiaxqfQY0aZw/640?wx_fmt=png&from=appmsg)

7月19日，CrowdStrike的故障更新造成了大规模业务中断。威胁行为者正在使用数据清除工具和远程访问工具并假冒CrowdStrike。

研究人员和政府机构发现，由于企业正在寻求帮助来修复受影响的Windows主机，近期利用这种情况的网络钓鱼电子邮件有所增加。

# **1、官方渠道建立沟通**

7月21日，CrowdStrike表示，公司“正在积极协助客户”解决更新错误带来的影响。公司提醒客户，确保他们是通过官方渠道与合法代表沟通，因为“对手和不良行为者可能会试图利用此类事件。"

“我鼓励每个人保持警惕，并确保你与官方CrowdStrike代表接触。我们的博客和技术支持将继续提供最新更新的官方渠道。”

——CrowdStrike CEO乔治·库尔茨（George Kurtz）英国国家网络安全中心（NCSC）也发出警告，指出他们观察到网络钓鱼邮件的数量有所增加。自动化恶意软件分析平台AnyRun注意到“模仿CrowdStrike的尝试有所增加，这可能会导致网络钓鱼。”

# **2、恶意软件伪装成修复和更新**

7月20日，网络安全研究人员g0njxa首次报告首次报告了一起针对BBVA银行客户的恶意软件攻击活动。

这次攻击活动假冒CrowdStrike修复更新来诱骗用户下载，而实际安装一个名为Remcos的远程访问木马（Remote Access Trojan，简称RAT）。这个假冒的修补程序是通过一个钓鱼网站portalintranetgrupobbva[.] com，它伪装成西班牙对外银行的内联网门户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6ywmbUibGWM265NG5CcuVNWWDjWTicO4ib6drdJ9L4HX1PvwWt5tLR6wE60a7VkebgjZibicxvweJGZIhQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

恶意软件加载器伪装CrowdStrike公司的hotfix

AnyRun也在推特上发布了类似的活动信息。攻击者通过一个伪装的热修复程序分发了HijackLoader恶意软件，该恶意软件随后在受感染的系统上释放了Remcos远程访问工具，使得攻击者能够远程控制受影响的计算机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6ywmbUibGWM265NG5CcuVNWWYqEZwNe5lvicYhkWFQ7nphzmKUgW77d0GnBia5kvvk750bAcAAUPldWg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

恶意附件推送数据擦除器

图片来源：BleepingComputer

在另一个警告中，AnyRun表示攻击者正在分发一个数据擦拭器，声称产品提供CrowdStrike的更新。AnyRun提示，“它通过删除零字节的文件来破坏系统，然后通过Telegram报告。”

另外，一个叫Handala的黑客组织称他们在给以色列公司的电子邮件中冒充CrowdStrike分发数据擦拭器。

该组织通过从域名“crowdstrike.com.vc”发送电子邮件来冒充CrowdStrike，让客户创建新工具来使Windows系统重新在线。执行假CrowdStrike更新后，数据擦除器将被提取到%Temp%下的文件夹中，并启动从而销毁存储在设备上的数据。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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