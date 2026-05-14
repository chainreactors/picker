---
title: 【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险
url: https://mp.weixin.qq.com/s/jz2esBqKqwTAu6frORFX9A
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:44:31.938611
---

# 【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGnv14rUZANfx9ZiaibcRKicC4ded2GLib9odsMtdVzApjOmm6hwB65gnTnla5MwibiaWPcqJPl7GvXOGaGEsKH92UbmSGeTkicXv1T4Y/0?wx_fmt=jpeg)

# 【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

Exim 发布了安全更新，以修复一个严重的安全问题。**该问题影响特定配置，可能导致内存损坏和潜在的代码执行。**

Exim 是一款开源邮件传输代理（MTA），专为类 Unix 系统设计，用于接收、路由和传递电子邮件。

此漏洞编号为 CVE - 2026 - 45185，又名 “Dead.Letter”，是 Exim 在通过 GnuTLS 处理 TLS 连接时，其二进制数据传输（BDAT）消息体解析中的一个释放后使用漏洞。

Exim 在今日发布的公告中称：“当客户端在消息体传输完成前发送 TLS 关闭通知警报，随后在同一 TCP 连接上以明文形式发送最后一个字节时，在 BDAT 消息体处理过程中就会触发此漏洞。”

“这一系列事件可能导致 Exim 写入一个在 TLS 会话终止时已释放的内存缓冲区，从而导致堆损坏。攻击者只需能够建立 TLS 连接并使用分块（BDAT）SMTP 扩展即可。”

该问题影响 Exim 从 4.97 到 4.99.2（含）的所有版本。不过，它仅影响使用 “USE\_GNUTLS = yes” 的构建版本，这意味着依赖 OpenSSL 等其他 TLS 库的构建版本不受影响。

自动网络安全测试平台 XBOW 安全实验室负责人费德里科・基尔希鲍姆（Federico Kirschbaum）于 2026 年 5 月 1 日发现并报告了该漏洞。

基尔希鲍姆表示：“在 TLS 关闭期间，Exim 会释放其 TLS 传输缓冲区，但嵌套的 BDAT 接收包装器仍可处理传入字节，并最终调用 ungetc () 函数，该函数会向已释放区域写入单个字符（\n）。这一字节的写入落在 Exim 的分配器元数据上，破坏了分配器的内部结构；随后，攻击者可利用这种破坏获取更多原语。”

XBOW 将该漏洞描述为 Exim 迄今为止发现的 “最高级别漏洞之一”，并补充说触发该漏洞几乎无需在服务器上进行特殊配置。

4.99.3 版本已修复此问题。建议所有用户尽快升级。目前没有其他缓解措施可解决该漏洞。

Exim 指出：“此修复确保在活动的 BDAT 传输期间收到 TLS 关闭通知时，输入处理栈能被彻底重置，防止使用无效指针。”

这并非 Exim 首次被披露存在严重的释放后使用漏洞。2017 年末，Exim 修复了 SMTP 守护进程中的一个释放后使用漏洞（CVE - 2017 - 16943，CVSS 评分：9.8），未经身份验证的攻击者本可通过特制的 BDAT 命令利用该漏洞实现远程代码执行，并控制邮件服务器。

***END***

阅读推荐

[【安全圈】警惕！你的蓝牙可能正被监听 改一个设置就能有效防护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=1&sn=80e79d8ca786f2b8a4f2a23fe7d5bad4&scene=21#wechat_redirect)

[【安全圈】谷歌确认黑客利用 AI 生成零日漏洞攻击 可提升攻击速度](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=2&sn=6ddc9b61db17560810d8e2ede885638d&scene=21#wechat_redirect)

[【安全圈】“Crimenetwork” 平台关停后死灰复燃，再遭德国当局捣毁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=3&sn=cde7250ec4d43b997cf6a5e4993a5c93&scene=21#wechat_redirect)

[【安全圈】cPanel新漏洞可能导致文件泄露与远程代码执行](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076342&idx=1&sn=30dee5e2a1337bda6b57e2ae8e2f3e7b&scene=21#wechat_redirect)

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