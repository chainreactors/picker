---
title: NSA 的开源员工培训平台 SkillTree 中存在CSRF漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=2&sn=921e2fe11a431d8a458188b65d0a3b9d&chksm=ea94be4cdde3375abbf6e79690d31fd0c1e2f7bdc02b738a8fc06afa426d4a95adedea7492d3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-12
fetch_date: 2025-10-06T17:44:09.702461
---

# NSA 的开源员工培训平台 SkillTree 中存在CSRF漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTOOu5Wt1qhVfe70pvkLt3Um6TUe1EARldQ5rgq1wOXLhmsnkKlYGxiaPTLicGyqIIg7YvzuBPYAhcg/0?wx_fmt=jpeg)

# NSA 的开源员工培训平台 SkillTree 中存在CSRF漏洞

Nate Nelson

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国国家安全局 (NSA) 修复了位于开源的员工培训平台 SkillTree 上的一个跨站请求伪造 (CSRF) 漏洞，证明了在生产发布前捕获这类漏洞的难度所在。**

SkillTree 是通过游戏元素如积分和成就等，实现学习目标的在线教育平台。该平台由NSA自研设计并于2020年在 GitHub 平台发布。该平台的目标是“提升用户与自研的复杂应用的交互方式”，“拉通并现代化NSA的软件开发和DevOps最佳实践”。

6月12日，Contrast 公司的研究人员发现并报送了该漏洞。之后该漏洞获得编号 CVE-2024-39326，CVSS 4.4，级别为“中危”。在CSRF攻击中，黑客将认证用户用作向目标网站或app 发送恶意请求的中转站。在该案例中，由于多个SkillTree 端点使用一些易受攻击的内容类型，黑客能够诱骗管理员级别的用户点击恶意链接，操纵与在线课程相关的视频、标题和文本。攻击者需要了解SkillTree 平台上的目标技能和项目名称，这类攻击将不会泄露其它的用户数据或系统。

NSA 已在7月2日发布补丁，修复了该问题。用户应部署该补丁，避免网站被操纵。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTOOu5Wt1qhVfe70pvkLt3U3nPC8jnldDgSSJvZib3MjePwYAQCOhpuGvfwYK8CEmbA5iajWa4wG2xg/640?wx_fmt=gif&from=appmsg)

**不易察觉的CSRF**

研究报告提到，“很多时候，CSRF漏洞被忽视，在代码发布到生产环境之前不会被修复。开发人员和应用安全团队关注更高阶的可导致敏感数据被泄露的攻击活动，因此CSRF漏洞不会得到修复，导致恶意人员获得成功利用这些漏洞的机会。”

而这些漏洞面临的不仅仅是被忽视的问题，它们实际上难以被发现。其中一个主要原因是这类漏洞不会破坏应用的正常功能。不像完全存在于应用代码中的漏洞，CSRF源自认证和会话中的设计问题。

Contrast 公司的研究员 Joseph Beeton 提到，“SQL漏洞将是开发人员非常熟知的漏洞，因为要触发这种漏洞，开发人员必须向数据库发送数据，因此开发人员在有意识地做一些操作。和SQL注入不同，CSRF几乎存在于应用之外，它存在于浏览器中。”

他还提到，“有很多种请求并不易受CSRF攻击。SkillTree 应用拥有数十个，也有可能数百个端点，而只有几个是易受攻击的。”好在，现代浏览器使用多种限制和策略保护站点免受攻击。同站cookie 可避免cookie 遭XSS 攻击，严格的跨源资源共享（CORS）策略可抵御越权跨源请求等，从而模糊了应用和浏览器的责任界限。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[1.4GB的NSA机密数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520021&idx=2&sn=694e77ee0ab92103cad4f3e0d1ad5a8c&chksm=ea94be7fdde337697f22a519c7599222567b8d5a4c460482a532eb7609ffd04faa814f5458b2&scene=21#wechat_redirect)

[CSRF防御机制反被CSRF误，csurf 开源NPM包被弃](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513786&idx=2&sn=74891678697b0e36ed3f5b2dfae35425&chksm=ea9487d0dde30ec613ae86e4fd96e0551be1aad357990007323a016cfa483e3249a5b24f75d1&scene=21#wechat_redirect)

[Jenkins 披露插件中未修复的XSS、CSRF等18个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513380&idx=3&sn=643da5e5ad5ec30250e2a3e9dca17e51&chksm=ea94844edde30d581814ce1b634ebb01aa1bda2917e2a9fc451329302585db1df9aa7b51fd8d&scene=21#wechat_redirect)

[对 \*.google.com/\* 产品进行大规模的 CSRFing 研究，意外获得3万美元奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495477&idx=1&sn=cb12680623a86c8eee315a0056257e59&chksm=ea94de5fdde357490e1a55ef97ac8df295d9a4ccd1e4765e93b0bc0575029a476c05521f059d&scene=21#wechat_redirect)

[开源框架 Drupal 修复多个访问绕过和 CSRF 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507917&idx=3&sn=a5e6b685fcaf76b58f720609ada0811d&chksm=ea94eea7dde367b119ed6bd4f027df950bc26346003fd0856da0552e2d751a2dbfa55893361b&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/application-security/whats-buggging-the-nsa-a-vuln-in-its-skilltree-training-platform

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