---
title: Internet Archive 被黑，影响3100万名用户
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521019&idx=2&sn=86a4934596bdd8f7f29b5505791002b6&chksm=ea94a391dde32a87b2abbabecd393b882a7edbcbfa59ad55da9dc9a9af6a52149d963b90ceb5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-11
fetch_date: 2025-10-06T18:52:40.388434
---

# Internet Archive 被黑，影响3100万名用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTmd846yz8iaLyDtZZqk0sdUd0UjRHwDAViaibHicFyb2GSicQGy8GzNEtaMEuykMfmhPp7Meq1hv5icmnw/0?wx_fmt=jpeg)

# Internet Archive 被黑，影响3100万名用户

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**一名威胁行动者攻陷 “互联网档案馆 (Internet Archive)”的“时间回溯机 (The Wayback Machine)”网站，窃取了包含3100万条唯一记录的用户认证数据库，导致该网站的数据遭泄露。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSAsjnjia0h6rTzh5oDdsH9vf0WibkPfqYxJGHw5Tu0pG6PT1lBNysZPfVppZ8KFvaAeIZvTlGLoJ3A/640?wx_fmt=gif&from=appmsg)

本周三下午，archive.org网站访客看到由该黑客创建的一条 JavaScript 报警信息称 Internet Archive 遭攻陷，“你是不是认为 Internet Archive 以不安全的方式运行且一直在遭受灾难性安全泄露事故的边缘？是的，这种事情刚刚发生了。去HIBP找3100万人的记录吧！”

这里的 “HIBP” 即由 Troy Hunt 创建的“Have I Been Pwned”数据泄露通知服务。威胁行动者们常常会共享被盗数据添加到该服务。Hunt 表示，黑客在九天前共享了 Internet Archive 的认证数据库，是名为 “ia\_users.sql” 的6.4GB 大小的SQL 文件。该数据库包含已注册会员的认证信息如邮件地址、屏幕名称、密码更改时间戳、Bcrypt哈希密码以及其它内部数据。

被盗记录上的最新时间戳是2024年9月28日，它可能是数据被盗的日期。Hunt 提到，该数据库中有3100万条唯一的邮件地址，其中很多人都订阅了HIBP数据泄露通知服务。这些数据随后将被添加到HIBP中，供用户输入邮件并确认数据是否遭暴露。Hunt 联系数据库中所列用户后证实数据是真实的，网络安全研究员 Scott Helme也分享了自己被盗的记录。他张士诚数据记录中的 bcrypt哈希密码匹配其密码管理器中存储的brcrypt哈希密码，他还张士诚数据库记录中的时间戳匹配自己上次在密码管理器中最后更改密码的日期。

Hunt 表示在三天前联系了 Internet Archive 并开始披露流程，表示数据将在72小时内加载到通知中，但目前尚未收到回应。目前尚不清楚黑客如何攻陷网站以及是否还窃取了其它数据。今天早些时候，Internet Archive 遭受DDoS 攻击，黑客主义组织 BlackMeta 生成为此事负责，并表示将发动更多攻击活动。目前，Internet Archive 尚未置评。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[HIBP 网站的Pwned Passwords组件代码开源，且直接收录 FBI 提供的数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504452&idx=1&sn=dc78cf2e4e326856968f493aa1972660&chksm=ea94e32edde36a383e83ea22587d19c30a6abd6a6045aa152ce22ba2abbb8746a3df32ba2ce9&scene=21#wechat_redirect)

[黑客称窃取 440GB 文件，Fortinet 证实数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=2&sn=d02acbabe690ef64658cea5df0e53131&chksm=ea94a375dde32a6384aa152fe7048a3f9417baa24bf139d055ab7d59550f25dcc400556bfde4&scene=21#wechat_redirect)

[1.4GB的NSA机密数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520021&idx=2&sn=694e77ee0ab92103cad4f3e0d1ad5a8c&chksm=ea94be7fdde337697f22a519c7599222567b8d5a4c460482a532eb7609ffd04faa814f5458b2&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/internet-archive-hacked-data-breach-impacts-31-million-users/

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