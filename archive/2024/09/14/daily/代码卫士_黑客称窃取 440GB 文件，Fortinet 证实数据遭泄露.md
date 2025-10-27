---
title: 黑客称窃取 440GB 文件，Fortinet 证实数据遭泄露
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=2&sn=d02acbabe690ef64658cea5df0e53131&chksm=ea94a375dde32a6384aa152fe7048a3f9417baa24bf139d055ab7d59550f25dcc400556bfde4&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-14
fetch_date: 2025-10-06T18:27:40.151846
---

# 黑客称窃取 440GB 文件，Fortinet 证实数据遭泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTfLbX6nWbEgIoIYUH9hASkyia61voS6nzF5GzV9hTJQvUescBoV3G4h57E5o4yryZ2lOvIzFwic4iaA/0?wx_fmt=jpeg)

# 黑客称窃取 440GB 文件，Fortinet 证实数据遭泄露

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**威胁行动者声称从网络安全巨头 Fortinet 的微软 SharePoint 服务器中窃取440GB 的文件后，Fortinet 证实数据遭泄露。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTfLbX6nWbEgIoIYUH9hASkpW8yd6zhQcQKibRlPbNL8t4AcQ2fRYm25n5OYvHcVQJenldRiageZPpA/640?wx_fmt=png&from=appmsg)

Fortinet 是全球最大的网络安全公司之一，出售安全网络产品如防火墙、路由器和VPN设备等，另外还提供 SIEM、网络管理和 EDR/XDR 解决方案和咨询服务。

今天早上早些时候，一名威胁行动者在一个黑客论坛上表示从Fortinet 的 Azure Sharepoint 实例中窃取了440GB 大小的数据，之后与一个S3存储桶共享了凭据，而该存储桶内还包括与其他可供威胁行动者下载的被盗数据。目前尚无法访问该存储桶。

该威胁行动者名为 “Fortibitch”，声称试图要求 Fortinet 支付赎金，以阻止数据被公布，但 Fortinet 予以拒绝。Fortinet 公司证实称，一家“第三方云共享文件驱动”中的客户数据遭泄露，“一名人员访问了存储在第三方云共享文件驱动的 Fortinet 实例尚的数量有限的文件，其中包括与少数 Fortinet 客户相关的有限数据。”

今天早些时候，Fortinet 并未披露受影响的客户数量或者被攻陷数据的类型，但表示“以适当的方式直接与客户沟通”。后续网站上的更新表示，该事件影响的客户数量不足0.3%，并不存在针对客户的任何恶意活动。另外该公司还证实称该事件并不涉及任何数据加密、勒索软件或其企业网络遭访问。

威胁行动者曾在2023年5月攻陷了Panopta 公司的 GitHub 仓库并将其数据泄露在一个俄语黑客论坛。Fortinet 公司在202年收购 Panopta。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Fortinet 修复 FortiOS 中的代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519734&idx=2&sn=e2956d27d020b75520e84dc6e02b483a&chksm=ea94bc9cdde3358a09b0520a5e8b66690030282303eda23770be759f6755bff0fd841526d768&scene=21#wechat_redirect)

[Fortinet 修复严重的 FortiClientLinux 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519274&idx=1&sn=0db6fdb46bf03ada98af3901110ee37b&chksm=ea94bd40dde3345638c4a1918ae58b2b830c15fa030942af921b1d39679824af6b8da3f82d60&scene=21#wechat_redirect)

[Fortinet 提醒注意端点管理软件中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519060&idx=1&sn=bd31e9a884e83396402ed8ca25c23ecd&chksm=ea94ba3edde333283d9736a8148c06430f74a8742642b854653fb130487618d9bdd7fb00804c&scene=21#wechat_redirect)

[Fortinet 提醒注意严重的FortiSIEM命令注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518159&idx=1&sn=44370db9677abd274914bebd182e5446&chksm=ea94b6a5dde33fb3b7fce9d16af88a593ad5cafb43671cb75c4eb3e9d6055b3812e8a12d2e68&scene=21#wechat_redirect)

[Fortinet 修复影响多款产品中的高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517693&idx=2&sn=ee2f37800cd4fde8239f203b3abcd5d3&chksm=ea94b497dde33d818a22818925aba4c372988566412b75f81318126b467d62a54093436d6e12&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fortinet-confirms-data-breach-after-hacker-claims-to-steal-440gb-of-files/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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