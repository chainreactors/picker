---
title: 美国CISA最新收录高危漏洞，系与甲骨文有关
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247532999&idx=2&sn=72d37dbdeb4d2742b0442b6155d37740&chksm=c1e9cd96f69e4480371336b17b1c1884751ec266185c54fcbac1ce79528d998bbbc60455509d&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-02
fetch_date: 2025-10-04T00:18:10.203546
---

# 美国CISA最新收录高危漏洞，系与甲骨文有关

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsNlbfMR8ZAxZSG1RDcynoUmrQFXnL0JbQbzdd46adQLiaiaWt351RTWes3ZVkcjZo9omBKSRSL8BVA/0?wx_fmt=jpeg)

# 美国CISA最新收录高危漏洞，系与甲骨文有关

关键基础设施安全应急响应中心

近日，美国网络安全和基础设施安全局 （CISA） 将一个影响美国甲骨文（Oracle）公司融合中间件的严重漏洞跟踪为CVE-2021-35587（CVSS 3.1 基本分数 9.8）。该漏洞是由于yizhi Access Manager（Oracle融合中间件）未对HTTP请求进行有效的验证，攻击者可利用该漏洞在未授权的情况下，构造恶意数据进行远程代码执行漏洞攻击，最终获取服务器最高权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6y0HPo7G1hgaN1VQNaOZq01XxPEbg6PcpYPTwfX9GwBU1GKpzBLLhECiaib8WQMHYzhHpdSNrA2GyHQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

美国甲骨文（Oracle）公司

Oracle Access Manager是Oracle公司出品的一款单点登陆认证管理系统。提供了基于Web的身份4管理，以及对运行于异类环境中的Web应用程序和资源的访问控制。它提供用户和组管理、委托管理、口令管理和自助服务功能，以便在复杂的、以目录为中心的环境中管理大量用户。据统计，全球总计30000以上的资产使用了Oracle Fusion Middleware。国内使用地区主要在广西、北京、辽宁等省份。

目前受影响的版本为Oracle Access Manage 11.1.2.3.0、Oracle Access Manage 12.2.1.3.0 和Oracle Access Manage 12.2.1.4.0在漏洞被发现后不久，Oracle公司就发布了针对该漏洞的补丁，及时修复系统。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6y0HPo7G1hgaN1VQNaOZq01MFn6hQeibw0O92Sdckyqqjuet3jXbLO9nE7daAuyia2nhEw2dEHPCGZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Nguyen Jang 发布的视频 PoC

据悉，该漏洞是由安全研究员 Nguyen Jang ( Janggggg ) 与peterjson一起报告的： “这个漏洞是我和Peterjson在我们为另一个mega-0day 分析和构建 PoC 时偶然发现的（目前仍未修复）。访问入口点并利用漏洞非常容易，因此建议立即应用补丁！它可能会让攻击者访问 OAM 服务器，创建具有任何权限的任何用户，或者只是在受害者的服务器上执行代码。”

目前，CISA 已将该漏洞列入已知利用漏洞目录。据统计，该目录目前列出了近四百个漏洞，其中一些老漏洞是2010年就被发现，但现在仍在外部被利用。这其中还包括思科、Google、微软、苹果、甲骨文、Adobe、Atlassian、IBM和其他许多大小公司的产品的漏洞。

CISA在一个具有约束力的操作指令中说："这个漏洞和之前记录的漏洞一项，给各机构带来了重大风险。必须积极补救已知的被利用的漏洞，以保护联邦信息系统和减少网络事件，"为此，CISA已命令联邦机构在 2022 年 12 月 19 日之前修复这些漏洞。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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