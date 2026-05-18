---
title: 【安全圈】黑客利用 Burst Statistics WordPress 插件认证绕过漏洞发动攻击
url: https://mp.weixin.qq.com/s/wxXwtTn6epofgw0Cl-D-gA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:07:39.611841
---

# 【安全圈】黑客利用 Burst Statistics WordPress 插件认证绕过漏洞发动攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyELlmM7bOeibhYDPtKtLX8frETOmYu8nhZwQ7hRcQb5ib5Cg9icHs0n3mHibsEewaI8glVLzjHwyfUZ0My5l6xY2Y7k3YAtGCmzLNk/0?wx_fmt=jpeg)

# 【安全圈】黑客利用 Burst Statistics WordPress 插件认证绕过漏洞发动攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGaXnV0icPgtf2RwQfkJuIdI9p3ibNWSviaU8E8Vf0ewTGSToYAeHuoetBNxkqeicyGy47WV4HfnLviabRgcBhtKOmibTfbVZn8gxDxE/640?wx_fmt=png&from=appmsg)

**黑客正在利用 WordPress 插件 Burst Statistics 中的一个严重认证绕过漏洞，获取网站的管理员级别访问权限。**

Burst Statistics 是一款注重隐私的分析插件，在 20 万个 WordPress 网站上启用，被宣传为谷歌分析的轻量级替代方案。

该漏洞编号为 CVE - 2026 - 8181，于 4 月 23 日插件 3.4.0 版本发布时引入。在后续的 3.4.1 版本中，该漏洞代码依然存在。

5 月 8 日发现 CVE - 2026 - 8181 漏洞的 Wordfence 公司表示，该漏洞使得未经认证的攻击者在进行 REST API 请求时，能够冒充已知的管理员用户，甚至创建恶意管理员账户。

Wordfence 解释称：“此漏洞允许知晓有效管理员用户名的未经认证攻击者，在任何 REST API 请求期间，通过在基本认证头中提供任意错误密码，完全冒充该管理员，包括对 WordPress 核心端点（如 /wp - json/wp/v2/users）的请求。”

“在最糟糕的情况下，攻击者无需任何事先认证，就能利用此漏洞创建一个新的管理员级别账户。”

其根本原因在于对‘wp\_authenticate\_application\_password ()’函数结果的错误解读，具体来说，就是将‘WP\_Error’错误当作认证成功的标志。

然而，研究人员解释称，在某些情况下，WordPress 也可能返回‘null’，而这也被错误地当作已认证的请求。

结果，代码会使用攻击者提供的用户名调用‘wp\_set\_current\_user ()’函数，从而在 REST API 请求期间有效地冒充该用户。

管理员用户名可能会在博客文章、评论中暴露，甚至在公共 API 请求中也能获取，攻击者也可以使用暴力破解技术来猜测用户名。

获得管理员级别访问权限后，攻击者可以访问私人数据库、植入后门、将访问者重定向到不安全的位置、分发恶意软件、创建恶意管理员用户等等。

虽然 Wordfence 在其发布的内容中警告称，“预计此漏洞将成为攻击者的目标，因此尽快更新到最新版本至关重要”，但其追踪数据显示，恶意活动已然开始。

同一平台的数据显示，这家网站安全公司在过去 24 小时内已阻止了超过 7400 次针对 CVE - 2026 - 8181 的攻击，可见此类攻击活动相当猖獗。

建议 Burst Statistics 插件的用户升级到 2026 年 5 月 12 日发布的已修复版本 3.4.2，或者在其网站上禁用该插件。

WordPress.org的统计数据显示，自 3.4.2 版本发布以来，Burst Statistics 已有 8.5 万次下载。假设所有下载的都是最新版本，那么仍有约 11.5 万个网站面临管理员权限被接管的攻击风险。

***END***

阅读推荐

[【安全圈】Linux内核漏洞"ssh-keysign-pwn"允许攻击者窃取SSH密钥与影子密码文件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=1&sn=85724f6aa9c493a3823cc2988e73c7ec&scene=21#wechat_redirect)

[【安全圈】微软 Edge 148 浏览器将增强安全，密码不再明文进入内存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=2&sn=4bce93113ae71c271aa59e2f723b5d8f&scene=21#wechat_redirect)

[【安全圈】微软Exchange Server高危漏洞正遭攻击者积极利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=3&sn=8adfa54adbe431abba673a75db6ad228&scene=21#wechat_redirect)

[【安全圈】新型远程控制木马被披露，黑客伪造苹果与雅虎 CDN 域名攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076488&idx=1&sn=ffae0916c178fdfdfc63e5f205db23f8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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