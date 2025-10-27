---
title: 【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=3&sn=b875bcdbb815582bbc7966d6ebc3a164&chksm=f36e7462c419fd74485e8ebdb3defa2fd94bb38ffe4cb647dd2e95a725273325e9a817afdddb&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-19
fetch_date: 2025-10-06T20:47:36.839172
---

# 【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhgoXt2hbpqmqppK1kkAMhYtpJlnAbWnY8SDY9V1vwOel8iaNGeUibaZICQ9bItYicpU7BPaGrXmE0yw/0?wx_fmt=jpeg)

# 【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhgoXt2hbpqmqppK1kkAMhYHsru2uBHEicibiciaib6lb1fzr9XKFHVbawZRydwPQlIQoib7KW9oaiaxxNJA/640?wx_fmt=jpeg&from=appmsg)

XCSSET macOS 模块化恶意软件的新变种出现在针对用户敏感信息的攻击中，包括数字钱包和合法 Notes 应用程序的数据。

该恶意软件通常通过受感染的 Xcode 项目进行传播。它已经存在至少五年了，每次更新都代表着 XCSSET 开发的一个里程碑。目前的改进是自 2022 年以来首次观察到的改进。

微软威胁情报团队在有限的攻击中发现了最新变种，并表示与过去的 XCSSET 变种相比，新变种具有增强的代码混淆、更好的持久性和新的感染策略。

2021 年 5 月，Apple 修复了一个被 XCSSET 积极利用的零日漏洞，这表明了该恶意软件开发人员的能力。

## 新的 XCSSET 变种

微软今天警告称，新的攻击使用了 XCSSET macOS 恶意软件的变种，该变种进行了全面改进。研究人员发现的一些关键修改包括：

* 通过依赖于 Base64 和 xxd（十六进制转储）方法的编码技术进行新的混淆 ，这些方法的迭代次数各不相同。代码中的模块名称也被混淆，这使得分析其意图变得更加困难
* 两种持久性技术（zshrc和dock）
* 新的 Xcode 感染方法：恶意软件使用 TARGET、RULE 或 FORCED\_STRATEGY 选项将有效载荷放置在 Xcode 项目中。它还可能将有效载荷插入构建设置中的 TARGET\_DEVICE\_FAMILY 键中，并在稍后阶段运行它

对于zshrc 持久化方法，新的 XCSSET 变体会创建一个名为 ~/.zshrc\_aliases 的文件，其中包含有效负载，并在 ~/.zshrc 文件中附加一条命令。这样，每当启动新的 shell 会话时，创建的文件就会启动。

对于dock方法，从攻击者的命令和控制 (C2) 服务器下载已签名的 dockutil 工具来管理 dock 项目。

然后，XCSSET 会利用该负载创建一个恶意的 Launchpad 应用程序，并将合法应用程序的路径更改为指向该虚假应用程序。因此，当 dock 中的 Launchpad 启动时，真正的应用程序和恶意负载都会被执行。

Xcode 是 Apple 的开发工具集，它带有集成开发环境 (IDE)，允许为所有 Apple 平台创建、测试和分发应用程序。

Xcode 项目可以从头开始创建，也可以根据从各种存储库下载/克隆的资源构建。通过针对这些资源，XCSSET 的运营者可以接触到更多的受害者。

XCSSET 有多个模块来解析系统数据、收集敏感信息并窃取数据。目标数据类型包括登录信息、聊天应用程序和浏览器信息、Notes 应用程序、数字钱包、系统信息和文件。

微软建议检查和验证从非官方存储库克隆的 Xcode 项目和代码库，因为它们可能隐藏混淆的恶意软件或后门。

来源：https://www.bleepingcomputer.com/news/security/microsoft-spots-xcsset-macos-malware-variant-used-for-crypto-theft/

***END***

阅读推荐

[【安全圈】仿冒DeepSeek的手机木马病毒被捕获！相关部门提示](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=1&sn=00cebc4413ae6b74430262bd93033252&scene=21#wechat_redirect)

[【安全圈】航空公司客服倒卖艺人航班信息，被判刑！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=2&sn=49a6b4aa641e56248143edcac248d76d&scene=21#wechat_redirect)

[【安全圈】Steam 平台上的 PirateFi 游戏被发现安装了密码窃取恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=3&sn=22a5fdac878492e3eb605cf3133cb536&scene=21#wechat_redirect)

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