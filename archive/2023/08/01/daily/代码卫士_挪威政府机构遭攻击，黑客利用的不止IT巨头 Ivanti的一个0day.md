---
title: 挪威政府机构遭攻击，黑客利用的不止IT巨头 Ivanti的一个0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517282&idx=1&sn=92bc54d50120e90cdb14ffdc9575e7e5&chksm=ea94b508dde33c1eb06b110c0e5f8a197bfcb980488faddce9fee996ea1be88dc50821b49082&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-08-01
fetch_date: 2025-10-06T17:01:57.556121
---

# 挪威政府机构遭攻击，黑客利用的不止IT巨头 Ivanti的一个0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS3kMtma1MyEpvsUGYCafm6UvUxqTrdicbe897lApfibg9br7aR0IUlkJgl2w4JoVvenicCnSEia9l2sA/0?wx_fmt=jpeg)

# 挪威政府机构遭攻击，黑客利用的不止IT巨头 Ivanti的一个0day

Jonathan Greig

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**IT 巨头 Ivanti 发布公告称发现了影响其移动端点管理软件中的另外一个漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS3kMtma1MyEpvsUGYCafm64pQVNOictla6FFey2zJGh8IQIcUNiaaEB0E23evVck6BU9H12RVcChkg/640?wx_fmt=png)

Ivanti 公司在上周五发布了关于CVE-2023-35081的安全公告，该0day漏洞不同于攻击者用于攻陷十几家挪威政府机构的漏洞。该公司指出，“Ivanti Endpoint Manager Mobile（EPMM，此前被称为 MobileIron Core）中存在一个漏洞，影响所有受支持版本即11.10、11.9和11.8。更老旧版本/发布也面临风险。该漏洞不同于7月23日发布的CVE-2023-35078。截止目前，我们发现，和受CVE-2023-35078影响的客户数量一样，受CVE-2023-35081影响的客户数量同样有限。”

该公告提到，该漏洞可导致攻击者在受害者设备上采取多种措施并与CVE-2023-35078组合利用来绕过管理员认证机制。

美国网络安全和基础设施安全局 (CISA) 发布提醒称，鉴于这两个漏洞均已遭利用，督促该公司客户立即修复 。挪威政府证实称多个机构遭攻击后，CISA已在上周二将 CVE-2023-35078添加至其“已知早利用漏洞”分类表。

挪威国家安全局总监 Sofie Nystrøm 提到，“该漏洞是唯一的，是在挪威发现的首个类似漏洞。如果我们过早发布该漏洞信息，则可能被滥用于挪威其它地方以及世界其它地方。”

EPMM 广泛用于包括美国政府在内的多个政府机构中。Shodan 安全平台搜索发现，位于美国和欧洲的数十个机构受该漏洞影响，另外还有数千个其它潜在受害者。

CISA提到，该漏洞可导致黑客远程访问受害者的个人可识别信息如姓名、电话号码和其它移动设备详情。攻击者还可做出其它配置变更，包括创建管理员账户，进一步修改易受攻击系统等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《静态应用安全测试全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516678&idx=1&sn=5b9e480c386161b1e105f9818b2a5a3d&chksm=ea94b36cdde33a7a05cafa9918733669252a02611c222b02bc6e66cbb508ee3fbf748453ee7a&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[谷歌发布2022年在野利用0day年度回顾报告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517276&idx=1&sn=4af5856a408590c04f66b8cf7944909b&chksm=ea94b536dde33c20a349d0ce168088e20f1710c32321c5af387665d68fc566998f5763f5cf27&scene=21#wechat_redirect)

[新Windows?! 苹果再修复已遭利用的新0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=2&sn=cfa4e9c7c012a88ff6a1ca8ada75564c&chksm=ea94b543dde33c556be2fcb984ebb556ca8d5f6654c7938d9996636b045518ace000eb82f2b6&scene=21#wechat_redirect)

[美国关基组织机构遭 Netscaler ADC 0day 漏洞利用攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517155&idx=2&sn=30be43df22f528bba04a0cd70d6a2ea4&chksm=ea94b289dde33b9fd4f00eb77a3c8e077ed183392537ff008a5de3ebbe0e9ea9994ad36c7a0d&scene=21#wechat_redirect)

[苹果员工在CTF大赛发现谷歌0day秘而不报 $10000赏金由他人获得](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517155&idx=1&sn=9af2d4f8742d395b46b7d44e219d9b05&chksm=ea94b289dde33b9f559073d1207e8437f82e8b6acf046825ee7f690fcbe59f72977119ba7dae&scene=21#wechat_redirect)

[Reddit替代品 Lemmy 开源软件遭 0day 利用攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517076&idx=2&sn=7062958ef499c9d253edf70f467f8bde&chksm=ea94b2fedde33be891e7da5d57174e952f57f47382684f02bd3d5e2c37370e44dce20a358785&scene=21#wechat_redirect)

**原文链接**

https://therecord.media/ivanti-warns-of-second-vulnerability-norway-government-attack

题图：Pexels License

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