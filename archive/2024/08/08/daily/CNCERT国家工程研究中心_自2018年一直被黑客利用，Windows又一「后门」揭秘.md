---
title: 自2018年一直被黑客利用，Windows又一「后门」揭秘
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546245&idx=2&sn=f040c5ad0c562ff543109e6474ee7300&chksm=fa938344cde40a52d75f2d8f9b91249de7d2e63aeb5708f8a1390e1db92d8a961da7a1eed207&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-08
fetch_date: 2025-10-06T18:06:14.294965
---

# 自2018年一直被黑客利用，Windows又一「后门」揭秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kokm4dqoKYS2VZKXK15tS2ZVCpV3xiajmXHOfVLWic0EsccWUnuEFeuddicC9HL6nvN1IJWicfZBzA4g/0?wx_fmt=jpeg)

# 自2018年一直被黑客利用，Windows又一「后门」揭秘

网络安全应急技术国家工程中心

Elastic安全实验室发现，Windows智能应用控制（Smart App Control）和智能屏幕（SmartScreen）存在一个设计缺陷，该缺陷允许攻击者在不触发安全警告的情况下启动程序，至少自2018年以来一直在被利用。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38Ou3mfGINxMLmXljMblav3NchXXZic5HB2iaU70ObgCl4RLibwlvlibgoeTniaGxjZuAPIicxpico5y3XMA/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

智能应用控制是一项基于信任的安全功能，它使用微软的应用智能服务进行安全预测，并利用Windows的代码完整性功能来识别和阻止不受信任的（未签名的）或潜在危险的二进制文件和应用程序。

它在Windows 11中取代了智能屏幕（Windows 8中引入的一个类似功能），旨在保护用户免受潜在恶意内容的侵害（当智能应用控制未启用时，智能屏幕将接管）。当用户尝试打开带有「Web标记」（MotW）标签的文件时，这两个功能都会被激活。

正如Elastic安全实验室所发现的，LNK文件处理中的一个错误（被称为LNK踩踏）可以帮助威胁行为者绕过智能应用控制的安全控制，这些控制旨在阻止不受信任的应用程序。

LNK踩踏包括创建具有非标准目标路径或内部结构的LNK文件，当用户点击这样的文件时，explorer.exe会自动修改LNK文件以使用正确的规范格式。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38Ou3mfGINxMLmXljMblav3ticTKZXhmuItJibyagb8GMeY0Com0ibZtZovyGxHC5wpHnuL37SfNpB2w/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

打开下载文件时的警告(BleepingComputer)

但是，这也从下载的文件中移除了MotW（Web标记），Windows安全功能使用该标签来触发安全检查。

要利用这个设计缺陷，可以向目标可执行文件路径添加一个点或空格（例如，在二进制文件的扩展名后加一个点，如「powershell.exe.」），或创建一个包含相对路径的LNK文件，如「.\target.exe」。

当用户点击链接时，Windows资源管理器将查找并识别匹配的.exe名称，修正完整路径，通过更新磁盘上的文件来移除MotW，并启动可执行文件。

Elastic安全实验室认为，这一漏洞多年来一直被滥用，因为他们在VirusTotal中发现了多个利用此漏洞的样本，其中最早的提交时间超过六年。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38Ou3mfGINxMLmXljMblav3py1PfWrYU4oYRVWVH769ibuLBc0I7ZvAkWRWTNWw2ukKk9ChrVhKzuA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

智能应用控制LNK踩踏演示（Elastic安全实验室）

他们已经将这些发现与微软安全响应中心共享，后者表示问题可能在未来的Windows更新中得到解决。

此外，Elastic安全实验室还描述了其他可以被攻击者利用来绕过智能应用控制和SmartScreen的弱点，包括：

* 签名恶意软件：使用代码签名或扩展验证（EV）签名证书签署恶意负载
* 信誉劫持：寻找并重新利用信誉良好的应用程序以绕过系统
* 信誉种植：在系统中部署攻击者控制的二进制文件（例如，带有已知漏洞的应用程序或仅在满足特定条件时才会触发的恶意代码）
* 信誉篡改：在不丢失相关信誉的情况下向二进制文件注入恶意代码

Elastic安全实验室警告说，智能应用控制和智能屏幕存在一些基本设计缺陷，可以允许在没有安全警告和用户交互最少的情况下进行初始访问。

安全团队应该仔细审查他们的检测堆栈中的下载内容，而不是仅仅依赖操作系统的原生安全功能来提供这方面的保护。

Elastic安全实验室发布相关信息及检测逻辑和应对措施，旨在帮助防御者在补丁可用之前识别这种活动。该实验室的研究员Joe Desimone已经发布了一个开源工具，用于检查文件的智能应用控制信任级别。

**参考资料：**

https://www.bleepingcomputer.com/news/microsoft/windows-smart-app-control-smartscreen-bypass-exploited-since-2018/

原文来源：FreeBuf

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