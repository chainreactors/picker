---
title: 【安全圈】黑客滥用 Microsoft VSCode 远程隧道绕过安全工具
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067503&idx=3&sn=0b2738a898f48ebbcd35b935ea9b9b9b&chksm=f36e7aefc419f3f9825e2bcdb1346a6a0cfc125b0362317ae276f36f4a15f976800acc71e733&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-21
fetch_date: 2025-10-06T20:11:11.000585
---

# 【安全圈】黑客滥用 Microsoft VSCode 远程隧道绕过安全工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUjBYyx2mCoibB38caI9T1ktAftHe3tdtqCQWOrnUicTEibGlhkTf1tGZFg/0?wx_fmt=jpeg)

# 【安全圈】黑客滥用 Microsoft VSCode 远程隧道绕过安全工具

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUtMLgbLMFDb9BYfUAzMhqHKOFfIF1BA1ibqBjN9Y3icaCbsqXDQPLTELg/640?wx_fmt=jpeg&from=appmsg)

VSCode 远程隧道是流行开发环境的一个合法功能，但越来越多地被恶意行为者所利用。

此功能允许开发人员远程访问其本地编码环境，从而提高参与度和灵活性。

利用此功能，恶意行为者可以安装文件或脚本来安装 VSCode CLI 并在用户不知情的情况下创建远程隧道。

这使得攻击者可以非法访问开发人员的设备，从而窃取机密数据、部署恶意软件并通过网络横向移动。

## **VSCode 隧道如何被威胁行为者滥用？**

根据 On the Hunt 的博客文章，最初传送的恶意 LNK 文件包含一个 PowerShell 命令，允许用户从远程 IP 地址下载并执行 Python 脚本。

VSCode CLI 二进制文件 code-insiders.exe 由 Python 脚本下载并执行。Python 脚本使用 CLI 二进制文件针对 Github 生成并验证VSCode 隧道。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUZpqUUpbt5OUYF9Eedia4uAUu5MF2FyrKQ61jtfQu68jmWYHVY1AkTAQ/640?wx_fmt=jpeg&from=appmsg)

攻击链

创建了 VSCode 的远程隧道，威胁行为者使用通过 Web 浏览器创建的隧道在 Python 有效负载上执行命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcULJnS3HjT8fnA2jyfiaEEuFq81yjicTcISvvtJRpJt6UHqSlm2tMsQjkw/640?wx_fmt=jpeg&from=appmsg)

Python 脚本设置隧道

为了在不使用攻击者的 GitHub 帐户的情况下对 VSCode 进行身份验证，请按下“连接到隧道”按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUUvXAyAu1ADuFVz8grmYuYmJkpCyLL8r2oteUEfwDibBKJm9Ma1VqZAg/640?wx_fmt=jpeg&from=appmsg)

正在连接到隧道

一旦通过账户验证，就可以看到具有活动隧道的远程主机列表。选择在线的受害者主机将连接到该主机上运行的 VSCode 远程隧道。

这使得遍历受害者远程计算机上的目录成为可能。此外，还可以创建新文件或脚本并远程运行它们。

建议组织将远程隧道的访问权限限制在自己的租户范围内。如果不可行，应禁止在庄园内使用隧道，或采取措施防止其滥用。

因此，公司可以采取主动措施来对抗这一新威胁，从而保护其敏感数据并保护其开发环境的完整性。

来源：

https://cybersecuritynews.com/hackers-abusing-microsoft-vscode-remote-tunnels/#google\_vignette

***END***

阅读推荐

[【安全圈】可能对企业产生严重影响：字节跳动飞书海外版Lark也将在美国市场停止运营](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=1&sn=c2d0bb267baf11570d6e3253fa3ff4fe&scene=21#wechat_redirect)

[【安全圈】微软已经修复Microsoft 365在Windows Server 2016/2019上崩溃的问题](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=2&sn=e94b5cb3a624cdca3e6452bf7c79d7a8&scene=21#wechat_redirect)

[【安全圈】FTC 要求通用汽车停止收集和销售驾驶员数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=3&sn=220a3c1eb7166bba53400942dfa9cab1&scene=21#wechat_redirect)

[【安全圈】CL-UNK-0979 利用 Ivanti Connect Secure 中的零日漏洞获取网络访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=4&sn=8dc7094933166fceeb2e467f38e23545&scene=21#wechat_redirect)

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