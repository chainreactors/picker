---
title: OpenSSL 高危漏洞可用于中间人攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522210&idx=2&sn=98a6271cd5d293a67b756477a83dfab3&chksm=ea94a6c8dde32fde30498e076c2a0a2bbb7d67be4c5997fcfe7bb831840a9bf6b09dcaf8800e&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-13
fetch_date: 2025-10-06T20:36:22.499246
---

# OpenSSL 高危漏洞可用于中间人攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSfW45cPQRuXVtIXZRHa4ysyicbxEVcxjUsgL26mYbmgqnCN51iat9EnyHYdubTl9YpaQNgvVM4aYnA/0?wx_fmt=jpeg)

# OpenSSL 高危漏洞可用于中间人攻击

do son

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**研究人员在 OpenSSL 中发现了一个高危漏洞CVE-2024-12797，影响传统X.509证书替代方法原始公钥 (RPKs) 的实现。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSfW45cPQRuXVtIXZRHa4ysPnZOLfEsuJPWrCGHs2y6p9bHtQz1jAeqsRCH1VHouxdIbtsTZqCOSg/640?wx_fmt=gif&from=appmsg)

该漏洞可导致攻击者通过模拟服务器的方式执行中间人攻击。OpenSSL 在安全公告中解释称，“使用 RFC7250 RPKs 的客户端认证服务器，可能未能注意到该服务器并未进行认证，因为当设置SSL\_VERIFY\_PEER 验证模式时，握手并未像预期那样中止。”

OpenSSL 默认禁用RPKs，因此该漏洞进影响明确启用该特性的用户。然而，对于确实使用RPKs的用户而言，成功攻击可能造成严重影响，可能导致数据泄露和越权访问后果。

该漏洞影响 OpenSSL 3.4、3.3和3.2版本。OpenSSL已发布更新版本修复该漏洞。上述受影响用户应分别升级至OpenSSL 3.4.1、3.3.2和3.2.4版本。值得注意的是，该漏洞并不影响OpenSSL 任何版本中的FIPS模块，也不影响 OpenSSL 3.1、3.0、1.1.1和1.0.2。

该漏洞是由苹果公司在2024年12月18日报送的。OpenSSL 督促启用 RPKs 的所有用户尽快更新系统，缓解利用风险。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[戴尔、惠普等设备被指使用过期的OpenSSL版本，易引发供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514771&idx=3&sn=c830e03f4b8b8fc4ad7c8ce0406d934a&scene=21#wechat_redirect)

[一个变俩：全网都在焦急等待的OpenSSL“严重”漏洞来了](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514379&idx=1&sn=7f9d9379ef945684fa63b0c57438a2c9&scene=21#wechat_redirect)

[OpenSSL 将修复2016年以来的第一个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514339&idx=1&sn=802d903c6ec13db25ef817d6c17f5427&scene=21#wechat_redirect)

[高危OpenSSL 漏洞可导致远程代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512767&idx=1&sn=b404692db2fa859fc1ee08badadbb004&scene=21#wechat_redirect)

[惠普Teradici PCoIP 受OpenSSL 漏洞影响，波及1500万个端点](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511336&idx=2&sn=fc84814f3a81ed4219673479715a84a6&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/cve-2024-12797-high-severity-openssl-flaw-update-now-to-prevent-mitm-attacks/

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