---
title: 【安全圈】恶意 Go 软件包利用模块镜像缓存实现持久远程访问
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=3&sn=0a2ed43f7e7eb5e16bbf8a4cf07d0964&chksm=f36e7b15c419f203eac3d6b64bb2979cf5ca88e1b8c3229b9bf761bcc51256b3052176063e90&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-07
fetch_date: 2025-10-06T20:37:42.789900
---

# 【安全圈】恶意 Go 软件包利用模块镜像缓存实现持久远程访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEiaR5VmtkbVZXrQL3ccLCHaFL6IhlU5Micub8fH6tlpxamibJvLmnr9KtQ/0?wx_fmt=jpeg)

# 【安全圈】恶意 Go 软件包利用模块镜像缓存实现持久远程访问

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEsNCU8O6FT65FQsuo9xTLRb6yJAIh1bsEPZQxBiaxUtGzMWXJFVyWbKw/640?wx_fmt=other&from=appmsg)

网络安全研究人员呼吁关注针对 Go 生态系统的软件供应链攻击，该攻击涉及一个恶意软件，可让对手远程访问受感染系统。

根据 Socket 的说法，该软件包名为github.com/boltdb-go/bolt ，是合法 BoltDB 数据库模块 ( github.com/boltdb/bolt )的域名抢注。恶意版本 (1.3.1) 于 2021 年 11 月发布到 GitHub，随后被Go Module Mirror服务无限期缓存。

安全研究员 Kirill Boychenko在分析中表示：“一旦安装，带有后门的软件包就会授予威胁行为者对受感染系统的远程访问权限，从而允许他们执行任意命令。”

Socket 表示，这是恶意行为者滥用 Go Module Mirror 无限期缓存模块来诱骗用户下载软件包的最早案例之一。随后，据说攻击者修改了源存储库中的 Git 标签，以将其重定向到良性版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEE6XZGDnj7ruo2Qg8mKk3RsSWByiawKZxYRGqmicFj3EBVGdUEfQ95g1g/640?wx_fmt=other&from=appmsg)

该公司在与 The Hacker News 分享的声明中指出，这一更改是在 GitHub 存储库中进行的，该存储库是合法 BoltDB 工具的一个分叉版本，威胁行为者重写了 v1.3.1 的 Git 标签，以指向干净的提交，而不是原始的恶意版本。

Socket 表示：“这是可能的，因为除非明确保护，否则 Git 标签是可变的。存储库所有者可以随时删除标签并将其重新分配给不同的提交。但是，Go Module Proxy 已经缓存了原始恶意版本，该版本从未更新或从代理中删除，从而使攻击得以持续。”

这种欺骗性的方法确保对 GitHub 存储库的手动审核不会发现任何恶意内容，而缓存机制意味着使用 go CLI 安装包的毫无戒心的开发人员会继续下载带有后门的变体。

Boychenko 表示：“一旦模块版本被缓存，即使原始源后来被修改，它仍然可以通过 Go Module Proxy 访问。虽然这种设计有利于合法用例，但威胁行为者利用它持续分发恶意代码，尽管随后存储库发生了更改。”

“由于不可变模块既提供了安全优势，也提供了潜在的滥用媒介，开发人员和安全团队应该监控利用缓存模块版本来逃避检测的攻击。”

Cycode详细介绍了三个恶意 npm 包 - serve-static-corell、openssl-node 和 next-refresh-token - 它们包含混淆代码来收集系统元数据并在受感染主机上运行远程服务器（“8.152.163[.]60”）发出的任意命令。

### 更新

在2025 年 2 月 5 日发布的有关 github.com/boltdb-go/bolt 的公告中，Go Module Mirror 服务的维护人员表示：“该模块是恶意域名抢注，试图利用与 github.com/boltdb/bolt 模块的混淆。”

来源：https://thehackernews.com/2025/02/malicious-go-package-exploits-module.html

***END***

阅读推荐

[【安全圈】DeepSeek遭遇大规模网络攻击，暂停新用户注册](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=1&sn=110423832f37fabbb95e2bc014e2efb1&scene=21#wechat_redirect)

[【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=2&sn=c07d521bd863d5ef6b8232fd91c2d58e&scene=21#wechat_redirect)

[【安全圈】Pwn2Own Automotive 2025 黑客因破解 49 个零日漏洞获 886,250 美元奖励](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=3&sn=15fafdc5115ba7e7a871e108304d8284&scene=21#wechat_redirect)

[【安全圈】以色列间谍软件公司Paragon涉嫌利用WhatsApp零点击漏洞发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=4&sn=cee4f0162f4215b03faa784f2a08ca29&scene=21#wechat_redirect)

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