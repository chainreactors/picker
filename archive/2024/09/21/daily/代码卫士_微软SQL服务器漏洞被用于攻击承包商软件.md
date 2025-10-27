---
title: 微软SQL服务器漏洞被用于攻击承包商软件
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520876&idx=1&sn=4efce31d5b8659ed3e426f95d90c4384&chksm=ea94a306dde32a10266fe5b357f6ce4e9f8404a2fbef256f7a4ef79b91a3158a225b496f9f09&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-21
fetch_date: 2025-10-06T18:27:24.607740
---

# 微软SQL服务器漏洞被用于攻击承包商软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTpykD45W0P10PNwL7yew4mTPcA4iaPlmSREibPX2JqwBQ8M0v9XCdjKVlObkuuXDjZnCLIB5SbDHLA/0?wx_fmt=jpeg)

# 微软SQL服务器漏洞被用于攻击承包商软件

Dark Reading

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Huntress 公司的安全研究人员提到，威胁行动者们正在利用管路系统、HVAC、混凝土子行业中的活跃利用，攻击建筑行业一般承包商常用的Foundation会计软件。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTpykD45W0P10PNwL7yew4mgvM4FuyRVjyeC8reNesZg0zAxUgtXmzYJVo1P2HAnQR1uviadupYTZw/640?wx_fmt=png&from=appmsg)

研究人员最初在9月14日追踪活动时发现该威胁，他们提到，“引起我们注意的是来自 sqlservr.exe 一个父进程中的主机/域名枚举命令。”该应用使用的软件包括用于处理其数据库操作的微软 SQL Server (MSSQL) 实例。研究人员提到，虽然将数据库服务器放在内网或防火墙下很常见，但Foundation 软件中包含的特性可通过一款手机app进行访问。因此，“TCP 端口4243 可能会被该手机app公开暴露，从而提供对 MSSQL 的直接访问权限。”

同时，微软SQL Server 拥有一个默认的系统管理员账户 “sa”，它对整个服务器拥有完整的管理员权限。这些账号可通过这类高权限使用户运行shell命令和脚本。

瞄准该应用的威胁行动者们被指大规模暴力攻击该应用，并使用默认凭据获得对受害者账户的访问权限。另外，威胁行动者们似乎在使用这些脚本自动化其攻击。

建议组织机构更改与 Foundation 软件相关联的凭据，并将其与互联网断网，以免遭受攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[承包商遭攻击，加拿大政府员工敏感信息被暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518185&idx=1&sn=9576830899e345f45902acb4d644d1fa&chksm=ea94b683dde33f958e17417395954cbe7fdbb09fd790c07bfa91b441217937531563efc21705&scene=21#wechat_redirect)

[美国国防承包商 L3Harris 拟收购以色列监控公司 NSO Group](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512362&idx=1&sn=06bd2eeaadd804ceab0abd0bc5096bd5&chksm=ea948040dde30956dbbb595f39ef95d8e5a254e3c441c891f7534b420ed6c7c297eab5090d81&scene=21#wechat_redirect)

[美国国会合同承包商遭勒索攻击，第三方软件安全亟需保障](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505497&idx=2&sn=2db6139a8951922f2fad96d5e91b42da&chksm=ea94e733dde36e25f5ff544ad2603f5a05300bec594edd4d5eb9aff1e68f0ca33ed355dffa89&scene=21#wechat_redirect)

[美国国防部设立承包商网络漏洞披露计划](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503282&idx=2&sn=7e81a7669ef3ec2303554cf5b56492f6&chksm=ea94fcd8dde375cefd686ef76400c5520a57d332010a1ad50a109249db2c9ad3daf2672f8d13&scene=21#wechat_redirect)

[出于安全考虑，英国防部要求承包商勿回答某些政府普查问题](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502622&idx=2&sn=bc2d05659af78c77c5c8bd48b3e516ca&chksm=ea94fa74dde37362ce1cb87574c85843c1dfa54e6ff9d0ceddaf3f71a2a132d643aec9894547&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/application-security/contractor-software-targeted-mssql-loophole

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