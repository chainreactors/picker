---
title: 一家AI公司被黑后，九家网络安全公司发生数据泄露
url: https://mp.weixin.qq.com/s/lIWEajVv2Ix2NWZ6CJLIxw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:03:53.587893
---

# 一家AI公司被黑后，九家网络安全公司发生数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88XYrEqYo7nBuTa2iahjNgwqIHj596ia3oc42nZxnmWmib6N9Xk0DRIibibtmV2AfUGrsHbPHNq2F2hCD5Gz1K0kiccYGYqLQgwGJAFJ4/0?wx_fmt=jpeg)

# 一家AI公司被黑后，九家网络安全公司发生数据泄露

安全内参
安全内参

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88XLTEdFoN67VVQ2NwSwRCMDhObtcWWX1ZLmsSo0NZLEqgDgdaRBz1P2uL5K9OQV0vNicbeDsrBWnMl7wXssOs9lTyd2SLTs6lQU/640?wx_fmt=gif&from=appmsg)

一个黑客组织近日声称，对加拿大市场情报提供商Klue遭受的入侵事件负责。攻击者表示从该公司的企业客户窃取了大量数据，多家知名网络安全企业受到影响。

6月19日，Klue在一篇博客文章中表示，一周前发生的一次网络攻击中，黑客从客户处窃取了数据，但公司没有透露具体有多少客户受到影响。Klue提供AI驱动的竞争情报分析平台，允许企业将自身数据连接至其系统，以开展市场研究。

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0NAbG7YmHk1GmHlWpNM4lGSApBKoKXiaxdFvnXToeP1tNFWIMIkQrtWA7AIiaVia2EOQzj4cibskazRm7bwA95iaR7qt8ufI38QrEpZs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)![]()![]()

网络犯罪组织Icarus声称对这起数据泄露事件负责，并在其泄露网站上表示，如果Klue不支付黑客要求的赎金，他们将公开被窃取的数据。

01

至少9家网络安全企业受影响，此类攻击已成趋势

Klue尚未说明其数百家客户中有多少受到影响。已有多家网络安全公司公开确认，其数据在此次攻击中被窃取，其中包括Gong、Jamf、HackerOne、Insurity、OneTrust、Recorded Future、Snyk、Sprout Social和Tanium。

这是近期一系列大规模黑客攻击事件中的最新一起。在这些攻击中，黑客瞄准的是那些拥有其他公司云数据库访问权限的企业。通过入侵Klue这类公司，黑客试图攻破单一关键节点，从而一次性窃取大量组织的数据。仅过去一年，黑客就越来越多地针对类似的中间层提供商，包括Gainsight和Salesloft，以获取数百家公司数据的访问权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NDPnXfDKrgqQE1a1xKt34N5MBqOT9ciapdd7NpDOLwZA16EPHP8hia1QmkGx6mUEUMExbWjQjX5zSJP8RczOWZmUxyicrg6f3BxUM/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=2)![]()![]()

图：网络犯罪组织Icarus的威胁公告

Klue表示，黑客于6月12日通过一个与集成工具相关的“已遭泄露的旧凭证”访问了公司的系统，例如密码或令牌。该集成工具允许客户将其公司的云数据连接至自己的Klue账号。

黑客能够从Klue客户的云环境中窃取数据，例如Salesforce数据库中的数据。企业通常会在Salesforce数据库中存储客户个人信息，因此这些数据库也成为黑客重点攻击的目标。

根据多家受影响公司的说法，被窃取的数据大部分包括业务联系信息，例如姓名、电子邮件地址、电话号码、职位，以及其客户的一些账号信息。

02

暂未发现攻击者如何窃取泄露凭证

目前尚不清楚黑客是如何获取这些泄露的凭证，也不清楚为何Klue未能更早发现数据窃取行为。近期类似的大规模攻击事件，例如针对Snowflake和TanStack的事件，都涉及凭证泄露和滥用，并被认为与员工在工作设备上无意安装窃取密码的恶意软件有关。

Klue表示，该公司已聘请事件响应公司CrowdStrike，并断开了其集成功能，以防止客户数据遭到进一步访问。

昨天，外媒TechCrunch联系Klue寻求置评。Klue首席执行官Jason Smith没有立即回应，也没有回答有关该事件的问题，包括公司是否收到黑客发送的任何通信，例如赎金要求。

Huntress是此次攻击中数据被窃取的安全公司之一。该公司在其事件分析报告中表示，黑客曾使用一家澳大利亚公司的电子邮件地址向其发送勒索通知，这家公司的服务器很可能被滥用于此次攻击活动。

去年6月，Klue表示正在准备裁员约一半员工，约100人，同时加大对AI投资的力度。目前尚不清楚人员削减是否导致该公司的安全措施出现漏洞。除Smith之外，目前尚不清楚还有谁负责该公司的网络安全工作。

目前，Klue在其高管领导页面上没有列出负责网络安全的高管。

**参考资料：bleepingcomputer.com**

来源：安全内参

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[关注｜国家网信办、工业和信息化部、公安部联合公布《网络数据安全风险评估办法》](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538487&idx=1&sn=380e3b5ec7c54f58443980376158f756&scene=21#wechat_redirect)

[中关村实验室首席科学家云晓春：大模型时代下的网络安全形势演变和技术重构](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538510&idx=1&sn=0431ff2e844bfe6b033abcb990eca148&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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