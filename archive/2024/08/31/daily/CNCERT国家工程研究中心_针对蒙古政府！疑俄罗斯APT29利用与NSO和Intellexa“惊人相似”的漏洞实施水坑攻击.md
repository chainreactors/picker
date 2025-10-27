---
title: 针对蒙古政府！疑俄罗斯APT29利用与NSO和Intellexa“惊人相似”的漏洞实施水坑攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546686&idx=2&sn=a34751fbd2e1c714f9ce9b19ce35fe2c&chksm=fa9381ffcde408e99309575941093b3419ce03b392d240232b9bd2f44ee9aee41602bd0777ec&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-31
fetch_date: 2025-10-06T18:05:23.575791
---

# 针对蒙古政府！疑俄罗斯APT29利用与NSO和Intellexa“惊人相似”的漏洞实施水坑攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176la9qfxh1pQYNUBn2S4e0InGEdNm4VHQ7CAF7uNibspAGmqHBlNib5o2jXyXk4oEtBcvKia0c4JHibFkQ/0?wx_fmt=jpeg)

# 针对蒙古政府！疑俄罗斯APT29利用与NSO和Intellexa“惊人相似”的漏洞实施水坑攻击

网络安全应急技术国家工程中心

谷歌威胁分析小组（TAG）当地时间8月29日发布博文披露，其研究团队在2023年11月至2024年7月期间发现，俄罗斯黑客通过水坑攻击对蒙古政府网站发起了多次攻击。这些攻击首先利用了影响iOS 16.6.1之前版本的WebKit漏洞，然后传播了针对Android设备（m121至m123版本）的Chrome漏洞链。尽管这些漏洞已有补丁，但未打补丁的设备仍然受影响。谷歌评估这些活动与俄罗斯政府支持的APT29有关。攻击中使用的漏洞与商业间谍软件供应商Intellexa和NSO Group开发的漏洞相似。谷歌在发现漏洞时已通知了Apple、Android和Google Chrome的合作伙伴，并修复了受感染的蒙古政府网站。文章强调了水坑攻击对复杂漏洞的持续利用，并展示了政府支持的攻击者和商业间谍软件供应商在漏洞利用中的共同之处。谷歌还指出了Chrome的保护措施，例如站点隔离，需要攻击者利用更多漏洞才能窃取所有cookie。尽管谷歌披露了这些漏洞，但仍不确定俄罗斯政府如何获得这些漏洞代码。此次发现揭示了商业间谍软件与国家黑客之间的潜在联系及其安全隐患。

背景

谷歌在其博客中指出，俄罗斯国家黑客，特别是APT29组织（与俄罗斯对外情报局SVR有关），利用了与NSO Group和Intellexa开发的漏洞非常相似的漏洞。这些漏洞被用来实施“水坑攻击”，即通过伪装的合法网站感染访问者的设备。APT29组织以其对微软、SolarWinds等公司的网络间谍活动和数据窃取行动而闻名。

漏洞利用

谷歌的调查发现，自2023年11月到2024年7月，俄罗斯黑客将恶意代码植入蒙古政府网站。这些网站利用了Safari浏览器和Google Chrome中的漏洞来攻击访问者的设备，窃取个人数据。具体来说：

* iPhone用户遭遇了针对WebKit漏洞（CVE-2023-41993）的攻击，这一漏洞影响了运行iOS 16.6.1及以上版本的设备。
* Android用户则遭遇了Chrome浏览器中的两个漏洞（CVE-2024-5274和CVE-2024-4671），这包括一个沙盒逃逸漏洞，允许攻击者绕过Chrome的站点隔离保护，窃取更多数据。

在水坑攻击活动的每次迭代中，攻击者使用的漏洞与Intellexa和NSO Group的漏洞相同或极为相似。我们不知道攻击者是如何获得这些漏洞的。很明显的是，APT参与者正在使用最初由CSV（商用间谍软件厂商）用作0-day的n-day漏洞。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUshTHctMnz6SL1vDArVbAolOhHtJavXVJPDCnBwU8Qjib1JVH4OjEqkwGh5ngFXPr2ia8A6QsrXcng/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

相似性分析

这些漏洞的利用方式与Intellexa在2023年9月使用的漏洞相似。谷歌指出，iOS漏洞和Chrome漏洞的触发代码与NSO Group和Intellexa开发的漏洞有显著相似之处。这种相似性暗示着俄罗斯黑客可能通过某种方式获得了这些漏洞代码。谷歌的安全研究员克莱门特·莱西涅（Clement Lecigne）表示，漏洞代码的重复使用表明俄罗斯参与其中，但具体如何获得这些漏洞仍然是一个谜。

商业间谍软件供应商的回应

尽管存在相似性，NSO Group否认与俄罗斯的任何联系。NSO Group全球通讯副总裁Gil Lainer表示：“NSO不向俄罗斯销售其产品。我们的技术仅售给经过审查的美国和以色列盟友情报和执法机构。”NSO Group强调其系统和技术受到高度安全保护，并持续监控外部威胁。

小结

尽管目前尚不清楚疑似APT29参与者如何获取这些漏洞，谷歌的研究突显了商业监控行业最初开发的漏洞如何被扩散到危险的威胁行为者手中。此外，水坑攻击依然是一种有效的威胁手段，能够利用复杂漏洞针对频繁访问特定网站的用户，包括使用移动设备的用户。这种攻击方式仍然可以通过利用未打补丁的浏览器进行大规模的n日漏洞攻击。

虽然移动领域的趋势正向复杂的完整漏洞利用链发展，但iOS活动表明，即便是单个漏洞也能造成显著危害并取得成功。在Android上，Google Chrome通过站点隔离等功能为用户提供了强大的默认保护，防止从受感染的渲染器窃取其他网站的数据（包括cookie）。为了取得成功，攻击者必须进一步利用Chrome的沙盒逃逸漏洞以读取其他网站的数据。

谷歌威胁分析小组（TAG）遵循其披露政策，分享了研究成果以提高整个生态系统的安全性和意识。同时，所有已识别的网站和域名已被加入安全浏览系统，以保护用户免受进一步攻击。TAG敦促用户和组织及时应用补丁，保持软件更新，以保护自己免受攻击。TAG将继续致力于检测、分析和防止零日攻击，并在发现漏洞后立即向供应商报告。

**参考资源：**

1.https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/

2.https://thecyberexpress.com/russian-state-hackers-use-spyware-exploits/

原文来源：网空闲话plus

“投稿联系方式：sunzhonghao@cert.org.cn”

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