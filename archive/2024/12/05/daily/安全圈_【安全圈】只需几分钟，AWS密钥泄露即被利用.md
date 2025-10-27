---
title: 【安全圈】只需几分钟，AWS密钥泄露即被利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=4&sn=9cbfcbbf89fbee51aff80ed24c0d0684&chksm=f36e7e27c419f731e0b4ac17ca19a1aa48c01287a72f77cdac037d155f4d42aa4684ba1420a4&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-05
fetch_date: 2025-10-06T19:38:55.996799
---

# 【安全圈】只需几分钟，AWS密钥泄露即被利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgPwOGp0Z0tQfy1NqUD8SN8GkvzNsMTptB5KPORoBwqTt0nZpnHiaUawusjfq1lDHRh3GfAwqQBTOA/0?wx_fmt=jpeg)

# 【安全圈】只需几分钟，AWS密钥泄露即被利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安数据泄露

开发者经常无意中在网上暴露AWS访问密钥，这已不是秘密，这些密钥在组织有机会撤销它们之前，就被攻击者抓取并滥用。Clutch Security的研究人员进行了一项测试，以查看这种情况发生的速度有多快。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgPwOGp0Z0tQfy1NqUD8SN8EqK3xMFUJfLY7bR1APZOFLpV9iaSLuxFAhbSwJ8xKLOqEeG5R3EpyFA/640?wx_fmt=jpeg&from=appmsg)他们将AWS访问密钥（在不同场景下）散布在：

代码托管和版本控制平台：

* GitHub和GitLab 公共代码仓库：Docker Hub（用于容器）、npm（用于JavaScript包）、PyPI（用于Python软件）、Crates.io（用于Rust crates）
* 托管和测试代码片段的仓库：JSFiddle、Pastebin以及公共和私有GitHub Gists
* 开发者论坛：Stack Overflow、Quora、Postman社区和Reddit 。

这项测试的结果显示，攻击者倾向于在几分钟内发现并利用在GitHub和DockerHub上泄露的AWS访问密钥，而在PyPI、Pastebin和Postman社区上暴露的密钥则在几小时内被利用。

在GitLab、Crates.io、公共GitHub Gists、JSFiddle、Stack Overflow、Reddit和Quora上发布的AWS秘密在1到5天内被利用。只有在npm和私有GitHub Gists上泄露的密钥未被使用。

如何自动撤销暴露的AWS密钥 研究人员发现，攻击者通常足够快，能够在AWS（如果客户使用AWS的安全中心和信任顾问服务）发送的关于暴露密钥的警报之前行动。

尽管AWS将暴露的密钥自动放入“隔离区”，但这并不足以阻止所有滥用：它只是限制了攻击者创建一些AWS资源的能力。研究人员泄露的AWS访问密钥允许攻击者登录到公司的沙盒云环境，进行侦察，提升权限和进行横向移动，甚至试图利用公司的基础设施进行资源密集型操作。

Clutch Security 公司对此表示，“这不是机会主义；而是自动化和意图。我们观察到的行动描绘了一幅有方法、高度组织的操作流程。”

正如Clutch研究人员所看到的，当前泄露的AWS密钥的问题在于，这些密钥的撤销留给了客户，而大多数客户未能迅速行动。“现实很清楚：暴露和轮换之间的时间窗口足以让攻击者造成重大损害。”

## AWS密钥泄露事件愈演愈烈

就目前来看，AWS密钥泄露呈现出愈演愈烈的趋势。

AWS密钥泄漏已在一些主要应用程序中被发现，例如Adobe Photoshop Fix，Adobe Comp，Hootsuite，IBM的Weather Channel以及在线购物服务Club Factory和Wholee。这些结果是对提交给CloudSEK的移动应用安全搜索引擎BeVigil的1万多个应用程序进行分析后得出的。

总部位于班加罗尔的网络安全公司分析的应用程序中，公开的AWS密钥可以访问多个AWS服务，包括S3存储服务的凭据，这反过来又可以访问88个存储桶，其中包含10073444个文件和数据，总计5.5 tb。存储桶中还包括源代码、应用程序备份、用户报告、测试工件、配置和凭据文件，这些文件可以用来深入访问应用程序的基础设施，包括用户数据库。

除此之外，近年来AWS密钥泄露事件屡屡发生。据媒体11月14日报道，自2021年以来，一个名为“fabrice”的恶意Python包在PyPI中被发现，该软件包窃取了Amazon Web Services凭据，已被下载超过37000次。

大量下载是由于fabrice 对合法的SSH 远程服务器管理包“fabric”进行错字造成的，这是一个非常受欢迎的库，下载量超过2 亿次。该 Fabrice 之所以长期未被检测到，是因为在 PyPI 上首次提交后就部署了先进的扫描工具，而且很少有解决方案进行追溯扫描。

值得一提的是，这个软件包通过执行特定脚本，在Linux和Windows系统上窃取AWS密钥，并将其传递给VPN服务器，使得追踪变得更加困难。

在另外一起假冒LockBit勒索软件的事件中，攻击者滥用AWS S3 Transfer Acceleration功能实施勒索软件攻击，将Golang勒索软件伪装成LockBit，以迫使受害者支付赎金。已确认的AWS访问密钥和账户已被暂停，趋势科技检测到30多个嵌入了AWS访问密钥ID和秘密访问密钥的样本。

CloudSEK研究人员表示：在移动应用程序源代码中硬编码的AWS密钥可能是一个巨大的漏洞，特别是如果(身份和访问管理)角色具有广泛的范围和权限。误用的可能性非常大且攻击的危害性非常大，因为攻击可以链接，攻击者可以进一步访问整个基础设施，甚至代码库和配置。

参考来源：https://www.helpnetsecurity.com/2024/12/02/revoke-exposed-aws-keys/

***END***

阅读推荐

[【安全圈】知名开源监控系统Zabbix存在SQL 注入漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=1&sn=ac63bf158d1e3e33b69fbab49a5ae214&scene=21#wechat_redirect)

[【安全圈】湖南网信办对某公司因数据泄露开出20万罚单](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=2&sn=e4d7346c9f48f96841de32189c2af0d1&scene=21#wechat_redirect)

[【安全圈】因软件更新，丹麦第一电信运营商宕机超过24小时](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=3&sn=4bd4e17312fffb19d18d2c8dd94b44f1&scene=21#wechat_redirect)

[【安全圈】新型恶意软件能利用LogoFAIL漏洞感染Linux系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=4&sn=b1e7b15689fa221569f9a1cad7eff071&scene=21#wechat_redirect)

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