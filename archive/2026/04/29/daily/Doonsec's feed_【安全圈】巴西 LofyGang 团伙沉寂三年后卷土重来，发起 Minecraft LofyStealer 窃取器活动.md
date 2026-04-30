---
title: 【安全圈】巴西 LofyGang 团伙沉寂三年后卷土重来，发起 Minecraft LofyStealer 窃取器活动
url: https://mp.weixin.qq.com/s/KzK57Of1l-GhHE2Kj7EH9g
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:27:03.500213
---

# 【安全圈】巴西 LofyGang 团伙沉寂三年后卷土重来，发起 Minecraft LofyStealer 窃取器活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE3jib8XZHSlXyy23NOIo9cMmicQa6GRsZRk5cDoK2993Uvs7KQnicZ0k4HhYJZSdltBHa0zBXCQNOADfk3L0rKiaCHiaydAqTYxzJo/0?wx_fmt=jpeg)

# 【安全圈】巴西 LofyGang 团伙沉寂三年后卷土重来，发起 Minecraft LofyStealer 窃取器活动

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客攻击

一个源自巴西的网络犯罪团伙在沉寂三年多后卷土重来，策划了一场针对 Minecraft 玩家的活动，使用名为 **LofyStealer**（又名 GrabBot）的新型窃取器。

巴西网络安全公司 ZenoX 在一份技术报告中表示：“该恶意软件伪装成一个名为‘Slinky’的 Minecraft 外挂。它使用官方游戏图标诱导用户自愿执行，利用了游戏场景中年轻用户的信任。”

该活动被高度确信地归因于一个名为 **LofyGang** 的威胁行为者。该团伙曾在 2022 年被观察到利用 npm 注册表中的拼写错误包（typosquatted packages）推送窃取器恶意软件，其具体目的是窃取与 Discord Nitro、游戏和流媒体服务相关的信用卡数据和用户账户。

据信该团伙自 2021 年底开始活跃，在 GitHub 和 YouTube 等平台上宣传其工具和服务，同时还以 DyPolarLofy 的别名参与地下黑客社区，泄露了数千个 Disney+ 和 Minecraft 账户。

ZenoX 联合创始人兼威胁情报主管 Acassio Silva 告诉 The Hacker News：“自 2022 年以来，Minecraft 一直是 LofyGang 的目标。他们曾以 DyPolarLofy 的别名在 Cracked.io 上泄露了数千个 Minecraft 账户。当前的活动则通过一个名为‘Slinky’的虚假外挂直接针对 Minecraft 玩家。”

攻击始于一个 Minecraft 外挂，当启动时，会触发一个 JavaScript 加载器的执行，该加载器最终负责在受感染主机上部署 LofyStealer（“chromelevator.exe”），并直接在内存中执行，旨在窃取多种网络浏览器中的广泛敏感数据，包括 Google Chrome、Chrome Beta、Microsoft Edge、Brave、Opera、Opera GX、Mozilla Firefox 和 Avast Browser。

窃取的数据（包括 cookie、密码、令牌、银行卡和国际银行账号）被外泄到位于 24.152.36[.]241 的命令与控制服务器。

ZenoX 表示：“从历史上看，该团伙的主要攻击向量是 JavaScript 供应链：NPM 包拼写错误攻击、星标劫持（虚假引用合法的 GitHub 仓库以提升可信度），以及嵌入在子依赖项中的载荷以规避检测。其重点是 Discord 令牌窃取、为拦截信用卡而修改 Discord 客户端，以及通过滥用合法服务（Discord、Repl.it、Glitch、GitHub 和 Heroku）作为 C2 进行数据外泄。”

最新进展标志着该团伙与以往观察到的攻击手法不同，转向了**恶意软件即服务**模式，提供免费和付费层级，并使用一个名为 Slinky Cracked 的定制构建器作为窃取器恶意软件的传播载体。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFr4Z2ibbOiaMs4Sxwh3mwC9rL5icYnrTKt9IicibrqlHE5SjOeFCja9RtKADP4dJN7LtYkbwrHHgXJzNmo83D0iaJ9HHxJkOhhpNg9w/640?wx_fmt=jpeg&from=appmsg)

这一披露正值威胁行为者越来越多地滥用 GitHub 等平台的信誉，托管虚假仓库作为恶意软件家族的诱饵，如 SmartLoader、StealC Stealer 和 Vidar Stealer。毫无戒心的用户通过 SEO 投毒等技术被引导至这些仓库。

在某些案例中，攻击者被发现通过 Reddit 帖子传播 Vidar 2.0，这些帖子宣传虚假的《反恐精英 2》游戏外挂，将受害者重定向到一个恶意网站，该网站会提供包含恶意软件的 ZIP 压缩包。

Acronis 在上个月发布的分析报告中指出：“这次信息窃取器活动突显了一个持续存在的安全挑战：被广泛信任的平台被滥用于分发恶意载荷。通过利用社会信任和常见的下载渠道，威胁行为者通常能够绕过传统安全解决方案。”

这些发现为最近几个月利用 GitHub 的活动清单增添了新内容：

1. **直接在 GitHub 内针对开发者**

   ：通过 Discussions 发布虚假的 Microsoft Visual Studio Code 安全警报，诱使用户点击链接安装恶意软件。Socket 表示：“由于 GitHub Discussions 会向参与者和关注者触发电子邮件通知，这些帖子也会直接发送到开发者的收件箱。这扩大了活动的影响范围，使其警报看起来更加可信。”
2. **针对阿根廷司法系统**

   ：使用鱼叉式钓鱼邮件分发压缩的 ZIP 压缩包，其中包含一个中间批处理脚本，用于检索托管在 GitHub 上的远程访问木马。
3. **创建 GitHub 账户和 OAuth 应用程序**

   ：然后创建一个提及目标开发者的问题，触发电子邮件通知，进而诱骗他们授权 OAuth 应用程序，使攻击者能够获取其访问令牌。这些问题旨在制造虚假的紧迫感，警告用户存在异常访问尝试。
4. **使用欺诈性 GitHub 仓库**

   ：分发伪装成合法 IT 和安全软件的恶意批处理脚本安装程序，导致部署 TookPS 下载器，然后启动多阶段感染链，使用 SSH 反向隧道和 RAT（如 MineBridge RAT，又名 TeviRAT）建立持久远程访问。该活动被归因于 Rift Brigantine（又名 FIN11、Graceful Spider 和 TA505）。
5. **使用假冒的 GitHub 仓库**

   ：伪装成 AI 工具、游戏外挂、Roblox 脚本、电话号码定位追踪器和 VPN 破解工具，分发 LuaJIT 载荷，这些载荷作为通用木马，是名为 TroyDen's Lure Factory 活动的一部分。

Netskope 表示：“诱饵工厂的广度——游戏外挂、开发者工具、电话追踪器、Roblox 脚本、VPN 破解工具——表明攻击者正在针对不同受众优化数量而非精准打击。防御者应将任何托管在 GitHub 上的、将重命名的解释器与不透明数据文件配对的下载视为高优先级排查对象，无论其周围的仓库看起来多么合法。”

***END***

阅读推荐

[【安全圈】“幻影核心” 利用 TrueConf 漏洞入侵俄罗斯网络](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076045&idx=1&sn=d9eecb878e9564d2a2967040fcb4511b&scene=21#wechat_redirect)

[【安全圈】朝鲜黑客通过伪装Excel文件向制药公司投放恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076045&idx=2&sn=f8be4fb89a6e5bb34ae28dd4c3ee5a3e&scene=21#wechat_redirect)

[【安全圈】OpenSSH 漏洞暗藏 15 年，可致完全 root 权限访问](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076045&idx=3&sn=ef57ae6fb805d4a4d501ec4d8c9a61f6&scene=21#wechat_redirect)

[【安全圈】潜伏 8 年的漏洞，WPS 365 轻舟 AI 如何从源头免疫？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076031&idx=1&sn=eabb23f8054d5d871eea7bf9685cea47&scene=21#wechat_redirect)

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