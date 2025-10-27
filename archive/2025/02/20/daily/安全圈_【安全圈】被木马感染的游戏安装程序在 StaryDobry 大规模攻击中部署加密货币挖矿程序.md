---
title: 【安全圈】被木马感染的游戏安装程序在 StaryDobry 大规模攻击中部署加密货币挖矿程序
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067894&idx=2&sn=c3dd926101ca05dd6242c9cbe87ad61b&chksm=f36e7476c419fd6059ea066ee8069cb363713483c9ed665dcc85ff5ac3167807021757742913&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-20
fetch_date: 2025-10-06T20:35:52.714329
---

# 【安全圈】被木马感染的游戏安装程序在 StaryDobry 大规模攻击中部署加密货币挖矿程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6YEXMOuDCXJeSqSYCzWLjwRtOG5JM4AygLorZh6IzicicQAIyncG4BpAw/0?wx_fmt=jpeg)

# 【安全圈】被木马感染的游戏安装程序在 StaryDobry 大规模攻击中部署加密货币挖矿程序

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6gPbIqhdiabO6Mgp9cibvlz5yPe9ib055zbduLicEkBvfdNWK1CzichaPCeg/640?wx_fmt=other&from=appmsg)

俄罗斯网络安全公司卡巴斯基（Kaspersky）于2024年12月31日首次发现了一场代号为“StaryDobry”的大规模网络攻击活动。该活动通过诱骗用户下载带有木马的流行游戏安装程序，在受感染的Windows主机上部署加密货币挖矿软件。攻击持续了一个月，主要针对全球个人和企业用户，其中俄罗斯、巴西、德国、白俄罗斯和哈萨克斯坦的感染集中度较高。

攻击手法与流程
根据卡巴斯基研究人员Tatyana Shishkova和Kirill Korchemny的分析，此次攻击利用流行的游戏和模拟器（如BeamNG.drive、Garry's Mod、Dyson Sphere Program、Universe Sandbox和Plutocracy）作为诱饵，发起复杂的攻击链。攻击者于2024年9月将使用Inno Setup制作的有毒游戏安装程序上传至多个种子网站，显示其精心策划的性质。

用户在下载这些被篡改的安装程序后，会看到一个看似正常的安装界面。然而，安装过程中，系统会提取并执行一个名为“unrar.dll”的dropper文件。该文件具备高度规避行为，首先会检测是否在调试或沙盒环境中运行。如果未被发现，它将通过访问api.myip[.]com、ip-api[.]com和ipwho[.]is等网站获取用户IP地址以估算其位置。若此步骤失败，系统默认将用户所在地标记为中国或白俄罗斯。

随后，dropper会收集设备指纹，并解密另一个可执行文件“MTX64.exe”，将其内容写入系统文件夹中名为“Windows.Graphics.ThumbnailHandler.dll”的文件中。此文件基于开源项目EpubShellExtThumbnailHandler，通过修改Windows Shell扩展缩略图处理程序功能，加载下一阶段的有效负载“Kickstarter”。Kickstarter进一步解密并执行嵌入的加密文件“Unix.Directory.IconHandler.dll”，将其存储在用户应用程序数据目录中。

最终，该DLL文件会从远程服务器检索二进制文件，启动挖矿程序植入。攻击者还设置了反检测机制，若检测到任务管理器（taskmgr.exe）或进程监视器（procmon.exe）正在运行，立即终止挖矿程序。

挖矿机制与目标
植入的挖矿程序为XMRig的定制版本，仅在具有8个或更多CPU核心的设备上启动挖矿过程。值得注意的是，攻击者使用自己的基础设施而非公共挖矿池服务器，进一步隐藏其活动。

攻击者身份
目前尚无法确定StaryDobry活动背后威胁行为者的确切身份。然而，样本中发现的俄语字符串暗示其可能与讲俄语的攻击者有关。

影响与启示
此次攻击凸显了恶意行为者通过合法软件和流行内容诱骗用户的复杂手段。用户应保持警惕，仅从官方渠道下载软件，并确保系统安全防护工具的实时更新。企业也应加强网络威胁监测，以避免类似攻击对其基础设施造成损害。

卡巴斯基表示，将继续监控StaryDobry活动的动态，并呼吁全球用户提高网络安全意识，共同应对日益复杂的威胁环境。

来源：https://thehackernews.com/2025/02/trojanized-game-installers-deploy.html

***END***

阅读推荐

[【安全圈】短视频平台“封号圈”乱象猖獗，IP查询如何助力防范](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=1&sn=77b78d28e626bb57cf51f82d0c472aa6&scene=21#wechat_redirect)

[【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=2&sn=634853ba2d9852cc240a7d5d46ce82c5&scene=21#wechat_redirect)

[【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=3&sn=b875bcdbb815582bbc7966d6ebc3a164&scene=21#wechat_redirect)

[【安全圈】马斯克与 OpenAI 的交锋：收购提案遇冷，立场分歧引争议](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=4&sn=38c4e0921e00478f77d52173d75865fa&scene=21#wechat_redirect)

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