---
title: MongoDB库中存在多个漏洞，可用于在Node.js服务器上实现RCE
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522334&idx=2&sn=474bb8a99d7a850a95b1ba847ff41044&chksm=ea94a974dde32062c02dec1281a683b8abd8c00fcda80eb383e8ae5b015673dcd949cffc9973&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-26
fetch_date: 2025-10-06T20:37:03.605803
---

# MongoDB库中存在多个漏洞，可用于在Node.js服务器上实现RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS4dMlia1lj2iccRMpO2j3Q8aIKIQ1ia3nHENhxxbw19yvCycw7sV5tEknwTpWIY6Ap2cWX7Y5dxHTAA/0?wx_fmt=jpeg)

# MongoDB库中存在多个漏洞，可用于在Node.js服务器上实现RCE

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全平台 OPSWAT报道称，MongoDB的库 Mongoose Object Data Modeling (ODM) 中存在两个严重漏洞，可导致攻击者在 Node.js 应用服务器尚实现远程代码执行 (RCE)。**

Mongoose 库广泛部署于生产环境中，可将 JavaScript 对象映射到 MongoDB 文档中，使数据管理和验证更加容易。虽然该功能改进了文档之间的工作关系，但可被用于实现RCE。

第一个高危漏洞是CVE-2024-53900，可导致攻击者利用 $where 值在 Node.js上实现RCE。第二个漏洞CVE-2025-23061是对CVE-2024-53900补丁的绕过。

研究人员解释称，$where 是MongoDB的一个查询操作符，可使 JavaScript 直接在 MongoDB 服务器上执行，不过会施加某些限制。在处理被检索的数据时，Mongoose的其中一个函数将把 $where 值传递给从外部库导入的一个函数，在应用服务器上本地处理查询，而无需验证输入。研究人员提到，“缺乏输入验证和限制引入了一个严重的安全漏洞，因为由用户输入直接控制的 “params” 值可遭利用，从而可能导致代码注入攻击。”

CVE-2024-53900的补丁增加了检查，禁止将 $where 操作符传递给易受攻击的函数，从而阻止恶意payload遭执行。然而通过将 $where 操作符嵌入到由 MongoDB和该易受攻击函数支持的 $or 操作符中，可绕过该补丁。

OPSWAT公司的研究人员提到，“因此，攻击者可将 $where 嵌入到 $or 下，躲避补丁单个层面的检查。由于 Mongoose 仅检查配对数组中每个对下给你的顶层属性，因此该绕过payload仍然处于未被检测状态，最终到达 sift 库，从而造成恶意RCE。

OPSWAT已发布针对这两个漏洞的概念验证，并建议将 Mongoose 更新至8.9.5或后续版本，完全修复这两个漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[MongoDB 证实被黑，客户数据被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518402&idx=2&sn=e0b6f6d8b89ce610fc6fce3432021ea2&scene=21#wechat_redirect)

[Spring Data MongoDB SpEL表达式注入漏洞安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512551&idx=3&sn=1d82552fab1461f66ca02457161cf83b&scene=21#wechat_redirect)

[不安全的 MongoDB 数据库爆出大秘密：俄政府拥有访问在俄企业的后门账户](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489157&idx=1&sn=ffae4c8c39b319aa67c2f4bcaacf8228&scene=21#wechat_redirect)

[MongoDB 数据库无凭证保护 近10万 app用户的个人详情遭暴露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487868&idx=1&sn=7e7fc0ace6169cd75995a967527b6146&scene=21#wechat_redirect)

[大规模MongoDB勒索攻击又导致2.6万台服务器受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485472&idx=1&sn=545ccd6571378ad4b8cb4a3481b04887&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vulnerabilities-in-mongodb-library-allow-rce-on-node-js-servers/

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