---
title: 1&2月份重点关注的API安全漏洞一览
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247497205&idx=1&sn=0df5b8681134d24706d84a2712fef404&chksm=c0075869f770d17f2bc1aaea39310d5a05183bcbdeca87e99cbcef268fe717f459ea1fb598e6&scene=58&subscene=0#rd
source: 星阑科技
date: 2023-03-03
fetch_date: 2025-10-04T08:32:40.162629
---

# 1&2月份重点关注的API安全漏洞一览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBduqGt7WHPrmJEK1eqVHibLyibOsVj9Q9MvibRic7D8jVhg0nTs0cq93ibgA/0?wx_fmt=jpeg)

# 1&2月份重点关注的API安全漏洞一览

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

为了让大家的API更加安全

致力于守护数字世界每一次网络调用

小阑公司 PortalLab实验室的同事们

给大家整理了

1&2月份的一些API安全漏洞报告

希望大家查漏补缺

及时修复自己API可能出现的漏洞

***No.1***

**一个允许远程控制现代和创世纪车辆的API关键漏洞**

**漏洞详情：**近期，研究人员披露了现代和创世纪汽车的一个关键漏洞，这个API漏洞可以远程控制汽车。

**漏洞危害：**在车辆门户网站上进行有效的注册后，可以调整电子邮件地址，然后可以使用“假的”电子邮件发布JWT。因此，只需了解用户的电子邮件，攻击者就可以欺骗登录，并获得允许完全访问车辆的令牌。

**影响范围：**该漏洞能够远程控制2012年后制造的车辆的锁、发动机、喇叭、大灯和后备箱。

**小阑修复建议**

1. 不要相信用户输入：攻击者可以提供未经充分确认的“假的”电子邮件地址。

2. 采用硬编码/受信任的正则表达式：避免电子邮件验证方法接受无效的电子邮件地址。

3. 对访问控制进行分割：向现有令牌添加并启用更多权限，或使用更高权限的令牌。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBG8ziaRZDCE9GHbRR2sVpGAdY5jIuRTKg7xl0K5KRTn1iaoMIfwgoiavqw/640?wx_fmt=png)

***No.2***

**奔驰、宝马等知名汽车品牌恐存在API漏洞**

**漏洞详情：**近期，Bleeping Computer 网站披露，近 20 家汽车制造商和服务机构存在 API 安全漏洞，这些漏洞允许黑客进行远程解锁、启动车辆、跟踪汽车行踪，窃取车主个人信息的恶意攻击活动。

**漏洞危害：**这些漏洞受到 SSO（单点登录）漏洞的影响，攻击者可以利用并访问内部业务系统。例如在对梅赛德斯-奔驰的测试中，研究人员可以访问多个私有GitHub实例、Mattermost上的内部聊天频道、服务器、Jenkins和AWS实例，并成功连接到客户汽车的XENTRY系统等。

**影响范围：**此API漏洞主要影响宝马、罗尔斯、奔驰、法拉利、保时捷、捷豹、路虎、福特、起亚、本田、英菲尼迪、日产、讴歌、现代、丰田和创世纪等其知名汽车品牌。此外，漏洞还影响汽车技术品牌 Spireon 和 Reviver 以及流媒体服务 SiriusXM。

**小阑修复建议**

目前所有安全漏洞，都已在披露后由各自的制造商进行了修复，但纵深防御策略仍很重要，可以遏制漏洞威胁并降低安全风险。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDB2PRdH0ibKM3vORd8yP6iasWPYUIkz8JZicDJYEiarg2D9COTudic5F4Pyvw/640?wx_fmt=png)

***No.3***

**IBM API 云平台的供应链漏洞**

**漏洞详情：**发现该漏洞的云安全Wiz公司研究员将它命名为“Hell’s Keychain”，是“影响云提供商基础设施的第一个供应链攻击向量”。

**漏洞危害：**特权升级漏洞（CVSS 得分：8.8）。一旦恶意攻击者成功利用该漏洞可能会在客户环境中远程执行代码，甚至读取或修改存储在 PostgreSQL 数据库中的数据。

**影响范围：**所有 IBM Cloud Databases for PostgreSQL 实例都可能受到该漏洞的影响。目前，IBM 发布安全公告指出，该缺陷已被修复且已自动应用，客户无需采取任何措施，且并未发现漏洞遭恶意利用的证据。

**小阑修复建议**

作为广泛攻击链的一部分，这些漏洞可能被恶意攻击者利用，最终导致对平台的供应链攻击。为了减轻此类威胁，建议组织监控其云环境中分散的凭据，强制实施网络控制以防止访问生产服务器，并防止容器注册表损坏。

***No.4***

**Algolia门户中的硬编码API密钥漏洞**

**漏洞详情：**Algolia成立于2012年，为网站及APP的开发者提供搜索功能接口，可以提供发现和推荐功能，用户超过11万。新加坡网络安全公司CloudSEK研究人员发现其有1,550个移动APP，会泄露Algolia API密钥，让内部服务的敏感信息和存储的用户信息有泄露的风险。

**漏洞危害：**组织可以随意使用Algolia有问题的API，将搜索、发现和推荐等功能整合到其应用程序中。该API被超过11,000家公司使用，有问题的应用程序的下载量超过250万次，这可能使其用户数据受到恶意的攻击。黑客可利用这些漏洞读取用户信息（包括 IP 地址、访问详细信息和分析数据），或删除用户信息。

**小阑修复建议**

开发人员应删除所有暴露的密钥，生成新的密钥，并安全备份它们。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBb53YBd9P5SUK4FFnKicyUOSU4Y7Zia6vl0ABwJKAZibiczwzr63MvIAdOQ/640?wx_fmt=png)

***No.5***

**Shopify API密钥存在严重的安全漏洞**

**漏洞详情：**新德里网络安全研究人员，在Shopify应用程序编程接口（API）的密钥中发现了一个严重的安全漏洞，超过400万手机用户的敏感数据面临被黑客攻击的风险。如果攻击者获得了硬编码密钥的访问权限，他们就可以访问相关敏感数据或进行程序执行操作。

**漏洞危害：**网络安全公司CloudSEK旗下的BeVigil（移动应用安全搜索引擎）发现了这一漏洞，该漏洞使400多万移动客户的个人身份信息（PII）面临潜在威胁。在数以百万的安卓应用程序中，有21个电子商务应用程序被识别出有22个硬编码的Shopify API密钥，任何有权访问该代码的人都可以看到该密钥。

**小阑修复建议**

改善API密钥保护状况，需要开发人员、应用程序所有者和安全团队的共同努力。

**• 接口密钥管理：**实施API密钥管理，有助于最大程度地降低风险。

**• 速率限制API密钥：**速率限制可在攻击者成功绕过加密的身份验证和授权过程时，使其过载。

**• 用户身份验证：**为了最简单地抵御攻击者，必须了解谁在使用你的API。

**• 培训开发人员：**了解安全的API编码实践。

**• 采用API规范框架：**可以采用像OpenAPI这样的API规范框架。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBXuvmyn2F0pxicKGrVmgNSv9E99fS2jZGLUMJNwxsp8aUkXVDQvabMjQ/640?wx_fmt=png)

***No.6***

**JSON-based SQL attack on WAFs 漏洞**

**漏洞详情：** 很多企业都将WAFs 作为安全支柱，但WAFs远达不到完美，研究人员和攻击人员能通过很多种方式绕过它们。在安全更新之前，使用基于JSON的黑客攻击可以绕过WAF的保护，以试图窃取数据。

**漏洞危害：**研究人员提到，Amazon Web Services、Cloudflare、F5、Imperva 和 Palo Alto公司，均未能识别出JSON 格式中向后端数据库提出的恶意SQL命令请求。这几家领先供应商的WAF在其SQL注入检查过程中未能支持JSON语法，这使得来自Claroty的Team82的安全研究人员能够将JSON语法添加到SQL语句中，从而使WAF无法检测这些恶意代码。

**小阑修复建议**

企业应当升级WAFs解决方案，获得最新的修复方案，确保他们正在运行最新版本的安全工具，以阻止这些绕过尝试。另外，不要将WAF解决方案作为单一的防御措施，建议使用多种安全机制确保应用程序安全，限制对服务应用程序的访问并启用安全特性。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBusMb96xqDdD1Og6wSbOUQ5phuUt3icibbAoRtGMFPBcaCSEFLBUatViaA/640?wx_fmt=png)

星阑科技“萤火”API安全分析平台可以支持多种API漏洞的检测。有相关需求的可以在公众号进行留言，或添加“小阑本阑”客服微信进行咨询。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBzibCC17J3iaFE0hbmSvl5Ynq9xg43QAmAMEQhdFsTb11TBEeaoH7XAWA/640?wx_fmt=jpeg)

（长按或扫描图中二维码即可添加）

**关于Portal Lab 实验室**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBEKgiaFPf8HlSOjGUEH7tjZPcODyAFiaSC2JmN7lkriaX85Xl7ruX2fv4A/640?wx_fmt=png)

星阑科技 Portal Lab 致力于前沿安全技术研究及能力工具化。主要研究方向为API 安全、应用安全、攻防对抗等领域。实验室成员研究成果曾发表于BlackHat、HITB、BlueHat、KCon、XCon等国内外知名安全会议，并多次发布开源安全工具。未来，Portal Lab将继续以开放创新的态度积极投入各类安全技术研究，持续为安全社区及企业级客户提供高质量技术输出。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBtyEPHqPUhANmQ3cOSdyxOZbTeaqbDy0F3Q464ic3ibqfdSiaAudvWXNOA/640?wx_fmt=jpeg)

**关注“星阑实验室”公众号**

**了解更多关于API安全的技术知识**

**往期 · 推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBt7zHDsok7wml2r02FjYY9de2Q5iaApYtNYtwdSYMrAAFxJauXysxKxA/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247497116&idx=1&sn=5c923d8be68f1cd6e25f919a335f1d6d&chksm=c0075800f770d116c4b88a2af42f99df82da76626874b8a3d985397a7d14b13e4cbeb77f0263&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDB6PAicbDyo7QwG2IgAkf0GticJ8ibQP8WUXriaTgFiblFQW4T5cHhOZcm2Kw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496967&idx=1&sn=365faa1f815f59f9614f8dfa3e3854c3&chksm=c007589bf770d18da031d6d11f97adfa9a6c354db231f6709c9a33725f015adef720920efa89&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDBCfPicrKG0ia0NpKkYIF1f2h26Sn1iaEoVTV5PXkE4b4cxOEzsRWthHQoA/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496954&idx=1&sn=720b26c65b4eb7137d92977d080ad371&chksm=c0075966f770d070417cb747fe8269fd7758517e9852a720450c74ec64c2d9b24aa89a32731c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaUYwnoACgEMPlJlvXtlFDB1jocosxoRgIiacGop1Ze17EZtc3VeDvYRBEcbC2DwNiaSEdzcdibhFTjg/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496905&idx=1&sn=26919ff4d1ad952d8513fc7fecfa4fe5&chksm=c0075955f770d043f4150c3aa4caaa77caa692ea72ea56556d388bdde0c1c1e4ab5279329ba0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOehwcHoxicoOah5mxDjLHMZ9RHUxNeibERphRXOj3AEupxt7JyOt3LF1RmmWQibYmicTv2DxM93iaEJhLxw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

星阑科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

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