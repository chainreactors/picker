---
title: 谷歌：黑客利用零日漏洞监控 iPhone、Android 用户
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535857&idx=1&sn=e79309521140afaf024690bd0cf4887b&chksm=fa93fa30cde4732621590ab4c1eef494a20392471fa14710c44c9db3b7bec4876efed4f14dce&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-04-01
fetch_date: 2025-10-04T11:24:35.966760
---

# 谷歌：黑客利用零日漏洞监控 iPhone、Android 用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lKa7J8hhicfibgDneGggvibfg8ydKJT90rartOSlo1h1YeJyiaXWyjqjLdvdeyMc02dWH9EbSvTyaXWQ/0?wx_fmt=jpeg)

# 谷歌：黑客利用零日漏洞监控 iPhone、Android 用户

网络安全应急技术国家工程中心

近日，谷歌的威胁分析小组 (TAG) 发现了两个具有高度针对性的移动间谍软件活动，它们使用零日漏洞针对 iPhone 和 Android 智能手机用户部署监控软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6xUY1MbBO56qeEV1sVHYlgFyHAH6C2mTvc2ic8Wte264kWicusUdtOrI1RG7DyhSqlkiceq4uIFFbD5A/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic)

Google TAG 发现了两个针对移动设备上的 Android、iOS 和 Chrome 用户的“不同的、有限的和高度针对性的”活动。这些活动使用零日和 N日漏洞，利用供应商发布漏洞修复程序和硬件制造商使用这些补丁更新最终用户设备之间的时间，为未打补丁的平台创建漏洞。

这些发现凸显了供应商和最终用户及时修补软件以防止恶意行为者利用已知漏洞的重要性。这些活动还表明，监控软件供应商共享漏洞和技术，以促进具有潜在危险的黑客工具的扩散。

第一个活动（CVE-2022-42856；CVE-2022-4135）分别针对 15.1 之前的 iOS 和 Android 版本,以及运行 106 之前的 Chrome 版本的 ARM GPU。

此类攻击活动中的攻击负载包括一个简单的 stager，它可以回测设备的 GPS 位置，并允许攻击者将 .IPA 文件安装到受影响的手机上，该文件可用于窃取信息。

该活动针对 Android 和 iOS 设备，初始访问尝试通过 Bit.ly URL 短链接通过短信发送给位于以下三个国家/地区的用户：

* 意大利
* 马来西亚
* 哈萨克斯坦。

第二个活动（CVE-2022-4262；CVE-2023-0266）包括使用零日和 n 日的完整漏洞利用链，目标是三星互联网浏览器的最新版本。

此类攻击活动的有效载荷是一个基于 C++ 的“功能齐全的 Android 间谍软件套件”，其中包括用于解密和捕获来自各种聊天和浏览器应用程序的数据的库。

谷歌研究人员怀疑，涉案人员可能是商业间谍软件供应商 Variston 的客户、合作伙伴或其他密切关联方。

值得注意的是，据Hackread.com去年报道，Variston 是一家总部位于巴塞罗那的公司，被谷歌 TAG 曝光，利用 Chrome、Firefox 和 Microsoft Defender 中的 n-day 漏洞，冒充定制网络安全解决方案提供商。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6xUY1MbBO56qeEV1sVHYlgF4gReic9mGbRvLQ68yQF0zp0nycibsSMNpeRJFaErDiaC7gJ1piaGxlSCJA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

来自针对意大利用户的恶意网站之一的示例屏幕截图（来源：谷歌）

TAG 积极跟踪商业间谍软件供应商，目前正在观察 30 多家，并确定出售给国家支持的参与者的漏洞利用或监视功能。这些危险的黑客工具为政府提供了他们无法在内部开发的监视能力。

这些工具，包括间谍软件，经常被用来针对持不同政见者、记者、人权工作者和反对党政客，构成危及生命的风险。

尽管根据大多数国家或国际法律，监视技术的使用通常是合法的，但政府滥用这些法律和技术来针对不符合其议程的个人。

自从政府滥用NSO Group 的 Pegasus 移动间谍软件针对 iPhone 用户的行为受到国际关注后，监管机构和供应商一直在打击商业间谍软件的生产和使用。

3 月 28 日，拜登政府发布了一项行政命令，限制联邦政府使用商业监控工具，但谷歌的调查结果表明，这些努力并未阻止商业间谍软件的出现。

必须加强有关商业间谍软件生产和使用的法规，以确保它们不会被用于侵犯个人基本权利的目标。

这些发现表明，那些创建漏洞的人正在密切关注他们可以为邪恶目的利用的漏洞，并且很可能串通以最大限度地利用它们来破坏目标设备。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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