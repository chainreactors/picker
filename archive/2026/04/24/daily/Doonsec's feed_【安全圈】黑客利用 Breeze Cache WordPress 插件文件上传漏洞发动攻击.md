---
title: 【安全圈】黑客利用 Breeze Cache WordPress 插件文件上传漏洞发动攻击
url: https://mp.weixin.qq.com/s/Sj8YUCbO9jxeDaTxsypuPA
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:26.008227
---

# 【安全圈】黑客利用 Breeze Cache WordPress 插件文件上传漏洞发动攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFPVMiabO8uOpfchuVpmqnniaXuQLMM4gFPNaINfCQDZovY41h7E7uhLVlavD43F1rSOTRfCu4JiaeE5ZgMD0u0BmNtKibwvibwH8I0/0?wx_fmt=jpeg)

# 【安全圈】黑客利用 Breeze Cache WordPress 插件文件上传漏洞发动攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

黑客正在积极利用 WordPress 的 Breeze Cache 插件中的一个严重漏洞，该漏洞可让攻击者在无需身份验证的情况下，在服务器上上传任意文件。

此安全漏洞编号为 CVE - 2026 - 3844，WordPress 生态系统的安全解决方案 Wordfence 已监测到超 170 次利用该漏洞的攻击尝试。

Cloudways 开发的 Breeze Cache 是一款 WordPress 缓存插件，拥有超 40 万活跃安装量，旨在通过缓存、文件优化和数据库清理减少页面加载频率，从而提升网站性能和加载速度。

该漏洞被评定为严重级别，在 10 分制中获 9.8 分，由安全研究员洪阮（Hung Nguyen，网名 bashu）发现并报告。

Wordfence 的开发商、WordPress 安全公司 Defiant 的研究人员表示，问题源于 “fetch\_gravatar\_from\_remote” 函数中缺少文件类型验证。

这使得未经身份验证的攻击者能够向服务器上传任意文件，进而可能导致远程代码执行（RCE），实现对网站的完全控制。

不过，研究人员称，只有在启用 “本地托管文件 - Gravatars” 附加组件（默认未开启）的情况下，攻击才可能成功。

CVE - 2026 - 3844 影响 2.4.4 及之前的所有 Breeze Cache 版本。Cloudways 已于本周早些时候发布的 2.4.5 版本中修复该漏洞。

据WordPress.org的统计数据，自最新版本发布以来，该插件约有 13.8 万次下载。但尚不清楚有多少网站存在漏洞，因为没有关于启用 “本地托管文件 - Gravatars” 功能的网站数量数据。

鉴于该漏洞正被积极利用，建议依赖 Breeze Cache 提升性能的网站所有者 / 管理员尽快将插件升级到最新版本，或暂时停用该插件。

如果目前无法升级，管理员至少应禁用 “本地托管文件 - Gravatars” 功能。

***END***

阅读推荐

[【安全圈】《王者荣耀》惊现逆天bug](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=1&sn=87382d2f57b8f0b6d5e7f3203b830e4d&scene=21#wechat_redirect)

[【安全圈】理想汽车严正声明：系统遭黑客破解、配合走私均为不实信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=2&sn=ef4ca71b65ec892a68ab6e5aeb1ab6df&scene=21#wechat_redirect)

[【安全圈】Claude Mythos 发现 271 个火狐浏览器漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=3&sn=d88245ccf278317f520a1fdb52cbc91b&scene=21#wechat_redirect)

[【安全圈】未受保护的 Perforce 服务器暴露主要组织的敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075943&idx=1&sn=473119abec6a4c6ed316801316b3723b&scene=21#wechat_redirect)

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