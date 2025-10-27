---
title: 【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=3&sn=42ec007bcefb5e73b814bbd77c03cb62&chksm=f36e7b3ac419f22c0aa5f3c78e3e31516b294c0da5d9a1a774b2f775fabec0b7b1f7b067ad5d&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-09
fetch_date: 2025-10-06T20:37:08.746144
---

# 【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNIicU8Liak4UJJprYjiaAZVuI8bw0CT0Lggg1qTiaKz6HicibnXF9ld0LM5dfDhuNECONDjVQJGwsq0qA/0?wx_fmt=jpeg)

# 【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

科技媒体 bleepingcomputer 昨日（2 月 6 日）发布博文，报道称微软发出示警，**有攻击者正利用网上公开的 ASP.NET 静态密钥，通过 ViewState 代码注入攻击部署恶意软件。**

微软威胁情报专家近期发现，一些开发者在软件开发中使用了在代码文档和代码库平台上公开的 ASP.NET validationKey 和 decryptionKey 密钥（这些密钥原本设计用于保护 ViewState 免遭篡改和信息泄露）。

然而，攻击者也利用这些公开的密钥进行代码注入攻击，通过附加伪造的消息认证码（MAC）创建恶意 ViewState（ViewState 由 ASP.NET Web 窗体用于控制状态和保存页面信息）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNIicU8Liak4UJJprYjiaAZVuxFd7xsRZLSRCmFEhWA4WIMdWhr65rRagk2zsrmzMENNBrqjhLnOxUw/640?wx_fmt=jpeg&from=appmsg)

攻击者通过 POST 请求将恶意 ViewState 发送到目标服务器，目标服务器上的 ASP.NET Runtime 使用正确的密钥解密，并验证了攻击者伪造的 ViewState 数据，随后将恶意 ViewState 加载到工作进程内存中并执行，让攻击者得以在 IIS 服务器上远程执行代码并部署其他恶意载荷。

IT之家援引博文介绍，微软于 2024 年 12 月观察到一起攻击事件，攻击者使用公开的密钥向目标互联网信息服务（IIS） Web 服务器部署了 Godzilla 后渗透框架，该框架具有恶意命令执行和 Shellcode 注入功能。

微软已识别出超过 3000 个公开的密钥，这些密钥都可能被用于 ViewState 代码注入攻击。以往已知的 ViewState 代码注入攻击多使用从暗网论坛购买的被盗密钥，而这些公开的密钥存在于多个代码库中，开发者可能直接将其复制到代码中而未进行修改，因此风险更高。

微软还分享了使用 PowerShell 或 IIS 管理器控制台在 web.config 配置文件中移除或替换 ASP.NET 密钥的详细步骤，并从其公开文档中删除了密钥示例，以进一步阻止这种不安全的做法。

微软警告，如果已经发生利用公开密钥的攻击，仅仅轮换密钥不足以解决攻击者可能建立的后门或持久化机制以及其他后渗透活动，可能需要进一步调查。

***END***

阅读推荐

[【安全圈】Hail 和 Rapper 僵尸网络是 DeepSeek 网络攻击的幕后主谋](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=1&sn=a6e07f45327351c84ccc70652f2e8f8e&scene=21#wechat_redirect)

[【安全圈】2024 年全球账户被盗用超 50 亿，中国成为首要目标](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=2&sn=0ceab7353bcbe2903411efcaa698035d&scene=21#wechat_redirect)

[【安全圈】Cloudflare对象存储服务R2出现故障导致多个网站无法正常访问](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=3&sn=b4bcff9fa2ad79fcb9370d738673957c&scene=21#wechat_redirect)

[【安全圈】CISA将Microsoft Outlook、Sophos XG Firewall等漏洞列入已知被利用漏洞目录](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=4&sn=76887cf1be0295b8075d662f2451e94d&scene=21#wechat_redirect)

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