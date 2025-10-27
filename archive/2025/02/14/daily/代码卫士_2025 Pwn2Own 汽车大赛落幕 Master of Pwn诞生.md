---
title: 2025 Pwn2Own 汽车大赛落幕 Master of Pwn诞生
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522224&idx=2&sn=125d997bc554beb7f8976b4e7d5fb526&chksm=ea94a6dadde32fcc069d6a17a0e1e6da0f5a961f05f5443b68859a6ecfc52b7050793911a62a&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-14
fetch_date: 2025-10-06T20:36:59.798937
---

# 2025 Pwn2Own 汽车大赛落幕 Master of Pwn诞生

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQX37nv0icdfE4wTaPlovRic4Z4ic1ehic927Y3ppbRqeHCnFxUMk7hHCGTe9aKonDuLJw6QreONcNyAA/0?wx_fmt=jpeg)

# 2025 Pwn2Own 汽车大赛落幕 Master of Pwn诞生

ZDI

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**2025年1月底，Pwn2Own 汽车大赛落下帷幕。大赛共发现49个0day漏洞，颁发886250美元的赏金。Sina Kheirkhah 最终以222250美元的赏金和30.5的积分问鼎“破解之王”桂冠。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQX37nv0icdfE4wTaPlovRic4Otwy4NzR5ibBibnJlUWHxbVf4Ld756bpBySMUw2EqTyT0ibAhGibiafkANw/640?wx_fmt=png&from=appmsg)

**0****1**

**第一天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQX37nv0icdfE4wTaPlovRic40zncaLcjQochTabBib403F3mfPZG3fbg0TuFtlKPaO9d4XAWJIsjbaA/640?wx_fmt=png&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 成功 | PCAutomotive | 通过一个基于栈的缓冲溢出漏洞在 Alpine IVI 上获得代码执行权限，获得2万美元赏金和2个积分点。 |
| 成功+成功 | Viettel Cyber Security | （1）     通过一个OS命令注入漏洞利用 Kenwood IVI实现代码执行，获得2万美元赏金和2个积分点。  （2）     通过一个基于栈的缓冲溢出利用漏洞，成功利用 Alpine IVI，获得1万美元赏金和2个积分点。 |
| 成功 | ANHTUD | 团队成员 Cong Thanh 和 Nam Dung通过一个整数上溢漏洞在 索尼 XAV-AX8500上获得代码执行权限，获得2万美元赏金和2个积分点。 |
| 成功/撞洞 +成功 +失败 | Summoning | （1）     Sina Kheirkhah组合利用3个漏洞，成功利用 Phoenix Contact CHARX SEC-3150，但其中一个漏洞为公开已知，不过他仍获得41750美元的赏金和4.25个积分点。  （2）     成功利用Ubiquiti 充电器中的一个硬编码密钥漏洞，获得5万美元赏金和5个积分点。  （3）     未能在规定时间内成功利用索尼 IVI。 |
| 成功/撞洞 + 成功 | Synacktiv | （1）     利用一个基于栈的缓冲溢出漏洞以及OCPP中的一个已知漏洞，成功利用通过连接器操纵信号的 ChargePoint，因此获得47500美元的赏金和4.75个积分点。  （2）     利用一个OS 命令注入漏洞成功利用 Kenwood DMX958XR并播放了Doom 游戏原始视频，获1万美元赏金和2个积分点。 |
| 成功 | PHP Hooligans | 利用一个基于堆的缓冲溢出漏洞成功利用Autel充电器，获得5万美元赏金和5个积分点。 |
| 成功 | Ierae 公司团队GMO Cybersecurity | 通过一个基于栈的缓冲溢出漏洞成功利用Kenwood IVI，获得1万美元赏金和2个积分点。 |
| 成功 | Confused | 该团队虽然进行了三次尝试，但最终通过一个基于堆的缓冲溢出漏洞成功利用索尼IVI，共获得1万美元赏金和2个积分点。 |
| 成功 +成功 | Fuzzware.io | （1）     通过电钻访问了一个开放端口，成功利用Autel MaxiCharger 上的一个基于栈的缓冲溢出漏洞，获得2.5万美元赏金和5个积分点。  （2）     通过一个源验证错误漏洞成功利用 Phoenix Contact CHARX SEC-3150，为此获得2.5万美元赏金和5个积分点。 |
| 撞洞 | SK Shieldus | 通过一个OS命令注入漏洞成功实施利用，但遗憾的是该漏洞是去年比赛中已经演示的。Alpine 当时表示“根据ISO21434标准，该漏洞被评估为‘风险共享’”，因此选择不修复。该团队最终获得5000美元的赏金和1个积分点。 |
| 成功/撞洞 | Technical Debt Collectors | 通过多个漏洞利用 Automotive Grade Linux，但其中一个漏洞此前已知，该团队首秀获得3.35万美元的赏金和3.5个积分点。 |
| 失败 | Quarkslab | Riccardo Mori 未能在规定时间内成功运行Autel MaxiCharger AC Wallbox Commercial。 |
| 撞洞 | STEALIEN | Bongeun Koo 也利用了Alpine 去年的漏洞，获得5000美元赏金和1个积分点。 |

**0****2**

**第二天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQX37nv0icdfE4wTaPlovRic4PHw78fcPYJbBl5amtH7JWTOcK4DysHZ3U5HQCJCXhuoFU2sUSGoVYg/640?wx_fmt=png&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 成功 + 撞洞 + 成功 + 撞洞 | Summoning | （1）     Sina Kheirkhah 组合两个漏洞成功利用 WOLFBOX 充电器并将其引入Pwn2Own的世界，获得5万美元赏金和5个积分点。  （2）     组合利用六个不同漏洞、访问控制不当和栈缓冲溢出漏洞，利用 Autel MaxiCharger，但其中一个漏洞为此前已知，仍获得2.3万美元赏金和4.75个积分点。  （3）     通过一个命令注入漏洞成功利用 Kenwood DMX958XR，获得1万美元赏金和2个积分点。  （4）     虽然成功利用由2个漏洞组成的利用链成功利用特斯拉Wall Connector，但它们均为此前已知，不过仍然获得1.25万美元赏金和2.5个积分点。 |
| 成功 + 失败 | PHP Hooligans | （1）     该团队利用 Numeric Range Comparison Without   Minimum Check 漏洞 (CWE-839) 成功利用特斯拉 Wall Connector，接管了该设备并导致其崩溃，获得5万美元赏金和5个积分点。  （2）     未能在时间规定内成功利用 WOLFBOX Level 2 电动车充电器。 |
| 成功/撞洞 + 撞洞 | Viettel Cyber Security | （1）     组合利用一个命令注入漏洞和一个已知漏洞，成功利用 ChargePoint Homeflex，因此获得18750美元的赏金和3.75个积分点。  （2）     虽然成功利用索尼 XAV-AX8500，但所用漏洞为此前已知，不过仍获得5000美元赏金和1个积分点。 |
| 成功 | ANHTUD | 通过一个命令注入漏洞成功利用Alpine Ilx-507，因此获得1万美元赏金和2个积分点。 |
| 撞洞 | ZIEN公司团队 | 成功利用了 Kenwood DMX958XR，但其中一个漏洞为此前已知，最终获得5000美元赏金和5个积分点。 |
| 成功 | HT3 Labs | 组合利用一个认证缺失漏洞和一个OS命令注入漏洞，成功利用 Phoenix Contact CHARX，因此获得2.5万美元赏金和5个积分点。 |
| 撞洞 +成功 | PCAutomotive | （1）     虽然成功利用特斯拉 Wall Connector，但所用漏洞为此前已知，不过仍然获得2.25万美元赏金和3.5个积分点。  （2）     组合利用三个不同漏洞（堆缓冲、认证绕过和格力不当），零点击利用索尼 XAV-AX8500，获得1万美元赏金和2个积分点。 |
| 失败 +失败 | Fuzzware.io | （1）     未能在规定时间内成功运行 ChargePoint HomeFlex 利用。  （2）     未能在规定时间内成功运行EMPORIA 电动车充电器 Level 2 电动车充电器的利用。 |
| 撞洞 | Pony 74 | 尽管该团队成功利用 Kenwood DMX958XR，但所用漏洞此前已知，最终获得5000美元赏金和1个积分点。 |
| 成功 | Ierae 公司团队GMO Cybersecurity | 组合利用一个证书验证不当漏洞和一个路径遍历漏洞成功利用 AIpine Ilx-507，获得1万美元赏金和2个积分点。 |
| 成功/撞洞 | PixiePoint Security | 通过由2个漏洞构成的漏洞链成功利用WOLFBOX Level 2 电动车充电器，但其中一个漏洞为此前已知，最终获得18750美元赏金和3.75个积分点。 |
| 成功 | Synacktiv | 通过包含一个逻辑漏洞的利用链，经由充电连接器成功利用特斯拉 Wall Connector，最终获得4.5万美元赏金和7个积分点。 |
| 撞洞 | CIS Team | 虽然成功利用 Alpine IVI 但其中一个漏洞为此前已知。未修复的 Alpine 漏洞（CVE-2024-23924）再次现身，不过仍获得5000美元赏金和1个积分点。 |
| 失败 | Compass Security | 未能在规定时间内成功运行 Alpine iLX-507的利用。 |
| 成功 | Juurin Oy、Elias Ikkelä-Koski 和Aapo Oksman | 通过一个命令注入漏洞成功利用 Kenwood   DMX958XR，但仍然获得1万美元赏金和2个积分点。 |

**0****3**

**第三天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQX37nv0icdfE4wTaPlovRic4Otwy4NzR5ibBibnJlUWHxbVf4Ld756bpBySMUw2EqTyT0ibAhGibiafkANw/640?wx_fmt=png&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 成功 +成功 | Summoning | （1）     通过一个漏洞成功利用 ChargePoint 电动车充电器，获得2.5万美元赏金和5个积分点。  （2）     通过一个命令注入漏洞成功弹出Alpine iLX-507，获1万美元赏金和2个积分点。 |
| 成功 | Synacktiv | （1）     通过一个整数上溢漏洞成功利用索尼IVI，获得1万美元赏金和2个积分点。  （2）     成功通过一个缓冲溢出漏洞利用 Autel MaxiCharger。研究人员还展示了通过Charging Connector 传输信号，获得3.5万美元赏金和6个积分点。 |
| 成功/撞洞 | STEALIEN | 通过由三个漏洞组成的利用链成功利用Ubiquiti 充电器，但其中两个为此前已知，仍获得26750美元的赏金和4.5个积分点。 |
| 成功 | Confused | 通过一个栈缓冲溢出漏洞混淆 Alpine iLX-507，获得1万美元赏金和2个积分点。 |
| 成功 | PHP Hooligans | 通过一个OS命令注入漏洞成功利用 Kenwood DMX958XR，获得1万美元赏金和2个积分点。 |
| 成功/撞洞 | Fuzzware.io | 通过由两个漏洞（其中一个是未初始化变量），成功利用WOLFBOX EV充电器，不过其中一个漏洞为此前已知，仍然获得18750美元赏金和2个积分点。 |
| 撞洞 | Technical Debt Collectors | 虽然成功利用了特斯拉 Wall Connector，但使用了一个此前已知的漏洞，不过仍然获得12500美元和2.5个积分点。 |
| 成功 | Evan Grant | 成功通过一个OS命令注入漏洞利用 Kenwood DMX958XR，获得1万美元赏金和2个积分点。 |

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[2025 Pwn2Own东京汽车大赛公布目标和奖金](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520932&idx=1&sn=92b8d0945843bbf9725d8256c2c2fd46&scene=21#wechat_redirect)

[QNAP修复Pwn2Own大赛利用的多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521736&idx=2&sn=37cc8cc02d4dc7c59168f8bb841938a9&scene=21#wechat_redirect)

[Pwn2Own 2024爱尔兰黑客大赛落下帷幕 Master of Pwn 诞生](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=1&sn=741af621329dcd54f31bdaa6d93a7347&scene=21#wechat_redirect)

[谷歌修复 Pwn2Own 2024大赛发现的两个 Chrome 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519170&idx=1&sn=31612ff9461ff59184a818b76f04c198&scene=21#wechat_redirect)

**原文链接**

https://www.zerodayinitiative.com/blog/2025/1/23/pwn2own-automotive-2025-day-three-and-final-results

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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