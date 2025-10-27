---
title: 【安全圈】针对安全人员，攻击者窃取了39万个WordPress凭证
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=3&sn=06b72f6bc788395990f167cdbed88121&chksm=f36e7f0ec419f618fafe674960452b3bcc4f36f0c3b1a01a1f414269c1640b39f4dc66a51ed1&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-17
fetch_date: 2025-10-06T19:40:17.007993
---

# 【安全圈】针对安全人员，攻击者窃取了39万个WordPress凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYHhMHXia2XIiak0sWv68QgxicvFctibbicMXhAjollEVX6FSJ0gctx9MasDg/0?wx_fmt=jpeg)

# 【安全圈】针对安全人员，攻击者窃取了39万个WordPress凭证

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

据BleepingComputer消息，一个被标记为 MUT-1244 的攻击者利用植入木马的 WordPress 凭证检查器进行了一次规模庞大、长达一年的攻击活动，盗取了超过 39 万个 WordPress 凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYicojVniaylO3D9JwdsCht5hTQALtrC0QpvojpMS8oznKr6n1f8KGmUeg/640?wx_fmt=jpeg&from=appmsg)

Datadog Security Labs 的研究人员发现了这些攻击，并表示被感染系统中有数百名受害者的 SSH 私钥和 AWS 访问密钥也被盗取，这些受害者很可能包括红队成员、渗透测试员、安全研究人员甚至其他一些黑客。

被感染者通过相同的第二阶段恶意载荷进行感染，该恶意载荷通过数十个植入了木马的 GitHub 代码库传播，这些代码库提供了针对已知安全漏洞的恶意的概念验证（PoC）漏洞利用代码以及一项钓鱼活动，引导目标安装伪装成 CPU 微码升级的虚假内核升级。

虽然钓鱼电子邮件诱使受害者执行命令安装恶意软件，但虚假代码库则欺骗了寻求特定漏洞利用代码的安全专业人员和其他一些黑客。在此之前，攻击者曾利用虚假的概念验证漏洞来攻击研究人员，希望窃取有价值的研究成果或者获得对网络安全公司网络的访问权限。

研究人员表示，由于它们的命名方式，其中几个代码库会自动包含在 Feedly Threat Intelligence 或Vulnmon 等合法来源中，作为这些漏洞的概念验证代码库，这增加了它们的合法性和被运行的可能性。

这些恶意载荷通过 GitHub 代码库使用多种方法进行传播，包括带有后门的配置编译文件、恶意 PDF 文件、 Python 样本传播程序以及包含在项目依赖项中的恶意 npm 包。

正如 Datadog Security Labs 发现的那样，这次攻击与Checkmarkx 在 11 月发布的一份报告中提到的一次为期一年的供应链攻击有重叠之处，这次攻击通过在"hpc20235/yawp" GitHub 项目中使用"0xengine/xmlrpc" npm 包中的恶意代码来窃取数据和挖掘 Monero 加密货币。

攻击中部署的恶意软件包括一个加密货币挖矿程序和一个后门，帮助 MUT-1244 收集和窃取私有 SSH 密钥、 AWS 凭证、环境变量以及密钥目录内容，比如"~/.aws"。

第二阶段的恶意载荷托管在一个独立的平台上，使攻击者能够将数据导出到像 Dropbox 和file.io 这样的文件共享服务中，调查人员在恶意载荷中找到了这些平台的硬编码凭证，使攻击者能够轻松访问被窃取的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYXYgTYVM3BbgNnDkIiaDicxAwpWtP8wD1CY5hSziaDcYScMicVN70ianTGicQ/640?wx_fmt=jpeg&from=appmsg)攻击流程

Datadog Security Labs 的研究人员表示，MUT-1244 成功获取了超过 39 万个WordPress凭证，并高度确信这些凭证在被导出到 Dropbox 之前就已经落入了攻击者手中。

攻击者成功利用了网络安全界的互信关系，通过目标在无意中执行攻击者的恶意软件而侵入了数十台白帽和黑帽黑客的机器，导致包括 SSH 密钥、 AWS 访问令牌和命令历史在内的数据被窃取。

Datadog Security Labs 估计，数百台系统仍然会受到攻击，而其他系统仍在遭受这次持续攻击带来的感染。

参考来源：390,000 WordPress accounts stolen from hackers in supply chain attack

***END***

阅读推荐

[【安全圈】千万悬赏：美国追捕四川黑客关天峰，指控其全球感染8万防火墙](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=1&sn=a53c860727d887307f935b429a2162da&scene=21#wechat_redirect)

[【安全圈】最高人民检察院：三名小伙「变相换汇」USDT 与人民币，遭判处五年徒刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=2&sn=7387c9bfc5ce3c826968c7e7dc0ec037&scene=21#wechat_redirect)

[【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=3&sn=e357cb32259162fcaa4e589951d9e4ea&scene=21#wechat_redirect)

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

阅读原文

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