---
title: CISA：严重的 Jenkins 漏洞已被用于勒索攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=2&sn=c8001046f4088bb94fd3ffcd7e6926b0&chksm=ea94a077dde32961061f5df3f34bcfb998ef7faf4faaf97b0d98fbf993523b5bcb3996850eb0&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-22
fetch_date: 2025-10-06T18:03:50.889184
---

# CISA：严重的 Jenkins 漏洞已被用于勒索攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQibwR6SUgJumVNbN5C6vI1QVYjkdypme2fnfr3qqXNKfic7AVakYaLIXUMZlfKdVhG1378oFM8WDyw/0?wx_fmt=jpeg)

# CISA：严重的 Jenkins 漏洞已被用于勒索攻击

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全和基础设施安全局 (CISA) 将影响Jenkins的一个严重漏洞 (CVE-2024-23897) 纳入其“已知已遭利用漏洞 (KEV)”分类表中，原因是该漏洞已被用于勒索攻击中。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQibwR6SUgJumVNbN5C6vI1Q0Lfx5wy9xdjBl3Vbf3VbnzqEb7QAUrydNPwficAZJPtwzmtNVwe78Yg/640?wx_fmt=gif&from=appmsg)

该漏洞的CVSS评分为9.8，是一个路径遍历漏洞，可导致代码执行后果。CISA在一份声明中提到，“Jenkins 命令行接口 (CLI) 中包含一个路径遍历漏洞，可导致攻击者将读权限限制到某些文件，从而引发代码执行后果。”该漏洞由Sonar公司的安全研究员首先在2024年1月发现，并在 Jenkins 2.442和LTS 2.426.3版本中通过禁用该命令解析器特性的方式修复。

3月份，趋势科技公司提到，发现位于荷兰、新加坡和德国的多个攻击实例，并发现实例中该漏洞的RCE利用被活跃交易。最近几周，CloudSEK 和 Juniper Networks 公司已披露利用该漏洞的多起网络攻击活动渗透多家公司如 BORN Group 和 Brontoo Technology Solutions。这些攻击活动被指分别由勒索团伙 IntelBroker 和 RansomExx 发动。

CloudSEK 公司提到，“CVE-2024-23897 是一个未认证的LFI漏洞，可导致攻击者读取 Jenkins 服务器上的任意文件。该漏洞是因为输入验证不当造成的，可导致攻击者操控特定参数并诱骗服务器访问并展示敏感文件的内容。”

鉴于该漏洞已遭活跃利用，CISA要求联邦民用行政部门 (FCEB) 在2024年9月9日之前应用修复方案，保护自身网络不受威胁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Jenkins 出现严重漏洞，可导致代码执行攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=2&sn=559cb44fa0529b875f5361b1112c5b60&chksm=ea948fbcdde306aaba8058c93f2a95d0d723359a0d01dee3fa2e873d99d65d6a7d5d0c5bdae4&scene=21#wechat_redirect)

[Jenkins 披露插件中未修复的XSS、CSRF等18个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513380&idx=3&sn=643da5e5ad5ec30250e2a3e9dca17e51&chksm=ea94844edde30d581814ce1b634ebb01aa1bda2917e2a9fc451329302585db1df9aa7b51fd8d&scene=21#wechat_redirect)

[Jenkins 披露多个组件中的29个未修复0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512696&idx=1&sn=5cc055e6e0d20676ecdd7c4f69dbef58&chksm=ea948312dde30a04f59e7b9ce79f1435ebf6d7aca4b7f21aaa31c408a774f19337d54bf0fe68&scene=21#wechat_redirect)

[Jenkins 内部服务器遭访问且被部署密币挖机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507695&idx=3&sn=3890bec24dc2bb2e4b44e15b7968ed68&chksm=ea94ef85dde3669367dbf64c8da66f13ba23fdd84c044f32979b08a03c4d211bfc9f0c6f9ba9&scene=21#wechat_redirect)

[开源自动化服务器软件 Jenkins 被曝严重漏洞，可泄露敏感信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494725&idx=1&sn=6bf29dab175c73db77b72934be87d9a0&chksm=ea94dd2fdde35439bd8c3b7485f574d8020d07f6614e4b0ab18aeb58270939e2f498b50612c0&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/08/cisa-warns-of-critical-jenkins.html

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