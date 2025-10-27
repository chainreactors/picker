---
title: Apache修复 Struts 2 中的严重 RCE 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521787&idx=1&sn=aa7443d590ca0182f0cbd4386c81152a&chksm=ea94a491dde32d87b3060602978c36b5e8d18e86a58054c857fc9c0ef0807f81f3a326687c1d&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-14
fetch_date: 2025-10-06T19:41:14.909512
---

# Apache修复 Struts 2 中的严重 RCE 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQqrq1zGdg88onVd6RY1iblcd2MkMibRzBnB3UQf9A68W9xvRDyb6vmXdaYWhwZpWpcctwub1W7bTjg/0?wx_fmt=jpeg)

# Apache修复 Struts 2 中的严重 RCE 漏洞

Connor Jones

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache Struts 2 宣布修复11月披露的漏洞CVE-2024-53677。该漏洞的CVSS v3 评分为9.5，CVSS v4 评分为9.8。远程攻击者无需任何权限，即可利用该漏洞，对系统机密性、完整性和可用性造成严重影响。Apache Foundation很可能并未披露该漏洞的最危险之处，以便客户有时间更新至安全版本Struts 6.4.0或更高版本。**

鉴于 Struts 漏洞与2017年爆发的“完全可阻止的” Equifax 泄露事件有关，因此Apache Foundation 这么做也无可厚非。Apache Foundation 在安全公告中称，“攻击者可操控文件上传参数，造成路径遍历后果，而在某些情况下，这样做可导致恶意文件上传，从而进行远程代码执行。”

受影响版本包括：

* Struts 2.0.0至Struts 2.3.37（已达生命周期）
* Struts 2.5.0至Struts 2.5.33
* Struts 6.0.0至Struts 6.3.0.2

未使用 Struts 的File Upload Interceptor 组件的应用并不受影响，因为该组件从6.4.0 起就被弃用并在7.0.0版本中被完全删除。

Apache Foundation 提到，在升级过程中，建议用户将文件上传机制更新为 Action File Upload Interceptor（自6.4.0版本开始就取代了上述提到的 File Upload Interceptor组件）。File Upload Interceptor 被弃用的原因与配置选项、安全性、性能和集成能力等均有关。

升级该机制并不像应用简单的更新那样轻松。用户必须重写操作，确保与 Action File Upload 的兼容性，而继续使用旧版本不可行，正如Apache 提到的，“使用旧的File Upload 机制的用户仍然易受攻击。”

尽管如今web app 开发人员经常选择不同的框架，但Struts 2 仍然热度不减。当 Sonatype 公司在去年分析性质和严重程度都类似于CVE-2024-53677的漏洞CVE-2023-50164时提到，Struts 2 每个月的下载量约为30万次，而其中80%都包含该严重漏洞。

CISA 将8个Apache Struts 漏洞纳入其必修清单，其中7个可导致远程代码执行后果，而CVE-2017-5638（即Equifax事件中涉及的漏洞）更是已被用于勒索攻击活动。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520994&idx=1&sn=0feb249fd14e6b8b07d5d6531f3287c2&scene=21#wechat_redirect)

[CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520886&idx=1&sn=d50fe47ebc8b4ad640aab8d8ead453e4&scene=21#wechat_redirect)

[Apache 修复严重的 OFBiz 远程代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=2&sn=a3784b5b2245f1449edaefa3064d676f&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 授权不当致代码执行漏洞(CVE-2024-38856)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=2&sn=db306ee3ac03c2a6708b7ae1cc72beaf&scene=21#wechat_redirect)

[Apache 修复 Apache HTTP Server 中的源代码泄露漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520009&idx=1&sn=b958a0460ffa3e890f8c189660f04487&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/12/12/apache\_struts\_2\_vuln/

题图：Pexels License

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