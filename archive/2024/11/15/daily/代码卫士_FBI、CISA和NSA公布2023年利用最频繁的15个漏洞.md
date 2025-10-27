---
title: FBI、CISA和NSA公布2023年利用最频繁的15个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521484&idx=2&sn=719611812a4cbf91cb5c976ad2da4620&chksm=ea94a5a6dde32cb0722d7e16df5083beb3411e14f366c8386689fe82083864c14070292098a6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-15
fetch_date: 2025-10-06T19:19:34.567297
---

# FBI、CISA和NSA公布2023年利用最频繁的15个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMThvc6hHEPK2mVsoTrPovNhVjXQvkQgAnrmWtpvpelyluuQ7uiaXUvX0NnMLJ8QV7A7El17dnac05g/0?wx_fmt=jpeg)

# FBI、CISA和NSA公布2023年利用最频繁的15个漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**FBI、NSA和五眼联盟的网络安全当局发布了2023年利用最频繁的15个漏洞清单。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMThvc6hHEPK2mVsoTrPovNhmUSZ4AFWnfOACtXetIsfWQqdOKLg4Zb6Uc0V1geyPbSXr65RCrXyiaw/640?wx_fmt=gif&from=appmsg)

周二，这些机构发布该清单，呼吁全球范围内的组织机构立即修复这些漏洞并不糊打补丁管理系统，将攻击风险降至最低。

这些机构提醒称，“相比2022年，恶意网络人员在2023年利用更多的0day漏洞攻陷企业网络，对更高优先级的目标发动网络攻击。2023年，多数利用频率最高的漏洞是0day状态，而2022年的比例少于一半。”

在这15个在野利用漏洞中，其中12个在去年已得到修复，与这些机构发出的关于恶意人员专注于利用0day的提醒一致。

利用频率最高的15个漏洞如下。

|  |  |  |  |
| --- | --- | --- | --- |
| **CVE** | **厂商** | **产品** | **漏洞类型** |
| CVE-2023-3519 | Citrix | NetScaler ADC/Gateway | 代码注入 |
| CVE-2023-4966 | Citrix | NetScaler ADC/Gateway | 缓冲溢出 |
| CVE-2023-20198 | Cisco | IOS XE Web UI | 提权 |
| CVE-2023-20273 | Cisco | IOS XE | Web UI 命令注入 |
| CVE-2023-27997 | Fortinet | FortiOS/FortiProxy SSL-VPN | 基于堆的缓冲溢出 |
| CVE-2023-34362 | Progress | MOVEit Transfer | SQL注入 |
| CVE-2023-22515 | Atlassian | Confluence Data Center/Server | 访问控制失效 |
| CVE-2021-   44228 (Log4Shell) | Apache | Log4j2 | 远程代码执行 |
| CVE-2023-2868 | Barracuda Networks | ESG Appliance | 输入验证不当 |
| CVE-2022-47966 | Zoho | ManageEngine 多种产品 | 远程代码执行 |
| CVE-2023-27350 | PaperCut | MF/NG | 访问控制不当 |
| CVE-2020-1472 | Microsoft | Netlogon | 提权 |
| CVE-2023-42793 | JetBrains | TeamCity | 认证绕过 |
| CVE-2023-23397 | Microsoft | Office Outlook | 提权 |
| CVE-2023-49103 | ownCloud | graphapi | 信息泄露 |

CVE-2024-3519是位于 NetScaler ADC/Gateway 中的一个代码注入漏洞，可导致攻击者在未修复服务器上获得远程代码执行权限。当黑客滥用该漏洞攻陷美国关键基础设施组织机构时，它是第一个被发现的漏洞。截止到2023年8月初，该漏洞已被用于在全球至少640台 Citrix 服务器上安装后门，且到8月中旬，该数量已超过2000台。

这些网络机构还发布了去年常被用于攻陷组织机构的32个其它漏洞，并且提供了关于防御人员如何减少攻击暴露的信息。今年6月份，MITRE 还披露了去年两年以来25个最危险的软件弱点，且在2021年11月，公布了最重要的硬件弱点清单。

NSA的网络安全技术总监 Jeffrey Dickerson 在本周二表示，“所有这些漏洞都是公开已知的，但很多漏洞首次进入15个利用频率最高的榜单。网络防御人员应特别注意这些趋势并立即采取措施，确保漏洞得到修复和缓解。这种利用将可能在2024年和2025年继续。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[CISA、FBI督促消除XSS漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=2&sn=e42af408ee177430c69f52668c7cc6eb&chksm=ea94a332dde32a247ff4d6cdf023ddf6f8317162ed60c534809d8bcaff0fc7ce94e472f08532&scene=21#wechat_redirect)

[CISA 提出安全新要求，保护政府和个人数据安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521255&idx=1&sn=7f84e630c55856e76ec9a0e7b2ec0166&chksm=ea94a28ddde32b9b80b54b6438afc7968a10eef130f4d3f8459562fc7c312f2479884f8eb523&scene=21#wechat_redirect)

[CISA：不安全软件的生产者就是恶棍的帮凶](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520903&idx=1&sn=768f0341b9f1b3432c6427db84765ddb&chksm=ea94a3eddde32afbb676980f5d5120ed1fb787b9ddb9cfc6e142a34bcdfca2f4780440027c02&scene=21#wechat_redirect)

[CISA：多数重要的开源项目未使用内存安全代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519901&idx=1&sn=32d7347010a5e163854477e5c2232e19&chksm=ea94bff7dde336e13576de0daf2daadc290e35b0e3b4c7d7b385038100a61ef8c962de61267a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fbi-cisa-and-nsa-reveal-most-exploited-vulnerabilities-of-2023/

题图：Pixabay License

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