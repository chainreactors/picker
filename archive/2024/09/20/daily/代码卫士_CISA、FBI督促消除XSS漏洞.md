---
title: CISA、FBI督促消除XSS漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=2&sn=e42af408ee177430c69f52668c7cc6eb&chksm=ea94a332dde32a247ff4d6cdf023ddf6f8317162ed60c534809d8bcaff0fc7ce94e472f08532&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-20
fetch_date: 2025-10-06T18:27:42.571589
---

# CISA、FBI督促消除XSS漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTeq7TomYdD3GlE3biaxN4btaHBOKXP5fuh5SiabFZajgUIY0Gv0vb4EyY86tll1PNA3830jUkSJ6vA/0?wx_fmt=jpeg)

# CISA、FBI督促消除XSS漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全局CISA和FBI针对普遍存在的XSS漏洞发布“设计即安全”的警告，督促组织机构消除产品中的XSS漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTeq7TomYdD3GlE3biaxN4btickd5amxQWic49yicCxWunRkZpRb948cbVXibfj3G3nibzhQgeuCT7aLtww/640?wx_fmt=png&from=appmsg)

XSS漏洞即跨站点脚本漏洞，CISA和FBI指出，这些漏洞存在的原因是未对用户输入进行正确验证、清理或逃逸，因此导致威胁行动者将恶意脚本注入 web 应用中，从而导致数据操纵、盗取或滥用。

CISA和FBI指出，“尽管一些开发人员使用了输入清理技术来阻止XSS漏洞但这种方法并非一劳永逸，应当通过额外的安全措施进行强化。”它们督促组织机构“审计这些缺陷实例”并执行计划，阻止产品中的XSS漏洞。

CISA和FBI建议组织机构审计所写的威胁模型，确保对软件的结构和意义都进行验证、开展代码审计、执行竞对产品测试以验证代码质量和安全，并使用现代 web 框架确保正确的转义或引用。

FBI和CISA提到，“高管和业务领导应当询问团队如何消除这些缺陷以及是否在产品中实现了设计即安全的方法。”它们同时建议组织机构执行这些设计即安全原则，保护产品免受XSS利用攻击：成为客户安全结果的主人，拥抱快速变化的透明度和责任，并构建组织结构和领导力来实现这些目标。

FBI和CISA提到，“为了展示对构建设计即安全产品的承诺，软件制造商应当考虑做出设计即安全承诺。该承诺表明签署方展现实现七个目标做出的可衡量进步，包括减少如XSS这样的系统性漏洞类型。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA 和 Ivanti：Cloud Services Appliance 高危漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520811&idx=1&sn=890fffef04e0244ca4a0fe359dfb3886&chksm=ea94a341dde32a57534c153b9526fd132574d3fa54a5c70c2bf6fe73dcf1c38e1c35c88ce3d1&scene=21#wechat_redirect)

[CISA提醒注意百特、三菱产品中的多个ICS 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520732&idx=2&sn=080d86bc26683d38189a49ac073be44c&chksm=ea94a0b6dde329a0e47b16a1c1c32be51890c7425e0aca2e0aed1907a6567ce9de33ff378023&scene=21#wechat_redirect)

[CISA：严重的 Jenkins 漏洞已被用于勒索攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=2&sn=c8001046f4088bb94fd3ffcd7e6926b0&chksm=ea94a077dde32961061f5df3f34bcfb998ef7faf4faaf97b0d98fbf993523b5bcb3996850eb0&scene=21#wechat_redirect)

[CISA：多数重要的开源项目未使用内存安全代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519901&idx=1&sn=32d7347010a5e163854477e5c2232e19&chksm=ea94bff7dde336e13576de0daf2daadc290e35b0e3b4c7d7b385038100a61ef8c962de61267a&scene=21#wechat_redirect)

[CISA 的CSA工具遭攻陷 化工厂敏感数据或被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519838&idx=1&sn=de0b2d5074525381fb17b3e0ce5f7bc0&chksm=ea94bf34dde33622a402a66867560237468eaf95fc52683f2e9a0fa44591b58a3324fdf33086&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/cisa-fbi-urge-organizations-to-eliminate-xss-vulnerabilities/

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