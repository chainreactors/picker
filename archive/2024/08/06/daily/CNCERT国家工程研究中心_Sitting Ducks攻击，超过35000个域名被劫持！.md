---
title: Sitting Ducks攻击，超过35000个域名被劫持！
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546198&idx=3&sn=4a6b9caca8f09a167bb201347b0b7899&chksm=fa938397cde40a81b8436400e9d7bf0a3ae466a4f2a8fbacaca6bc290a637b1b299c509381d2&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-06
fetch_date: 2025-10-06T18:05:26.672420
---

# Sitting Ducks攻击，超过35000个域名被劫持！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nEgjXfWXEoxK5GtdYfA4p8d3mgPPjpGqhiba5uQl5rhEzHDU4k9iakpSY1vv1ooZYZYUxhiciaQUO4Qw/0?wx_fmt=jpeg)

# Sitting Ducks攻击，超过35000个域名被劫持！

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nEgjXfWXEoxK5GtdYfA4p8hqc675pMNokAo98SI5y0icnk1MqDsAzMXAGPLQLMtcWyZdGIcibC3eCg/640?wx_fmt=jpeg&from=appmsg)

近期，Infoblox和Eclypsium的网络安全研究人员，在域名系统（DNS）中发现了复杂的攻击媒介“Sitting Ducks”。

Infoblox公司在报告中透露，自2018年以来，Sitting Ducks劫持超过35,000个域名，存在超过100万个易受攻击的目标域。

这次攻击是在研究俄罗斯托管的404TDS（一个流量分配系统）基础设施时发现的，系俄罗斯网络犯罪分子参与其中。

攻击者在伪装下执行恶意活动，包括恶意软件交付、网络钓鱼活动、品牌模仿和数据泄露等。

"Sitting Ducks"攻击与其他控制域名的技术不同，因为它不需要注册商的访问权限，攻击者只需要利用所谓的"无效委托"（lame delegation）即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6zNLB2DH3EFJ61TnVPKPS7ejiamFHjXfQaKz2qgicIfvVymZaOhxFZ8MniaPVC8om3xvv8eHvgfQABbg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Sitting Ducks flow (Infoblox)

无效委托发生在注册的域名或子域名将权威DNS服务委托给不同于域名注册商的其他提供商时，如果权威名称服务器缺少域名信息并且无法解析查询，这种委托就被称为无效的。

当恶意行为者注册了被分配的域名，获得指向该域名的所有域名的访问权限时，就会发生无效委托攻击。

此外，攻击者通过利用DNS提供商的漏洞，扫描互联网上具有无效委托的域名，未经授权就声称拥有所有权。他们把劫持的域名创建恶意记录，将流量定向到恶意服务器，并将用户定向到攻击者的网站。

根据Eclypsium博客文章所述，"Sitting Ducks"现象有多种变体。

它能够利用域名所有者在域名服务器信息中的拼写错误，从而使得攻击者能够注册部分无效域名。Dangling DNS记录，由于配置被遗忘而包含无效信息，可以推广到其他类型的DNS记录。Dangling CNAME攻击将DNS响应重定向到失效的域名，从而允许恶意行为者注册失效的域名并获得血统。

经过对十几个DNS提供商域名授权的分析，结果显示，参与者中最显著的是俄罗斯的网络犯罪分子。

利用这种攻击，每天有数百个域名被劫持，这些域名通常是通过所谓的“品牌保护注册商”注册的，或者是注册了外观相似的域名。

媒体呼吁，为了避免Sitting Ducks攻击，域名所有者应该使用独立于其域名注册商的权威DNS提供商。确保域名和子域将名称服务器委托给有效的服务提供商，并询问DNS提供商缓解措施以降低风险。

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