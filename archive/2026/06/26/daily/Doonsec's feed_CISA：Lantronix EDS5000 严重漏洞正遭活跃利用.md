---
title: CISA：Lantronix EDS5000 严重漏洞正遭活跃利用
url: https://mp.weixin.qq.com/s/RrlwDTY1WRhGWCKDTd2G_w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:46.799981
---

# CISA：Lantronix EDS5000 严重漏洞正遭活跃利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfVJkpG0bBBZjQZtey6ic8fTUUYbnHBtnFDSfriaoUrXWSm4e6ay0MnplicaVpB0ibOjyiau4ibykloQAXAeP4uIJ9lgSTpTFnLHv6JXM/0?wx_fmt=jpeg)

# CISA：Lantronix EDS5000 严重漏洞正遭活跃利用

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周二，美国网络安全和基础设施安全局 (CISA) 提醒称，Lantronix EDS5000系列设备受严重的代码注入漏洞（CVE-2026-67038，CVSS 评分9.8）影响，可能导致攻击者以高权限执行任意命令，目前已遭活跃利用，敦促联邦民事行政部门（FCEB）机构在2026年6月26日前应用修复方案。**

根据CVE.org上对该漏洞的描述：“当用户身份验证失败时，HTTP RPC模块会执行一个shell命令来写入日志。用户名未经任何清理处理，直接与命令拼接，导致攻击者能够将任意操作系统命令注入到用户名参数中。注入的命令将以root权限执行。”

该漏洞由Forescout Research Vedere Labs于2026年4月披露，是影响Lantronix和Silex串口转IP转换器的一组漏洞（被统称为BRIDGE:BREAK）的一部分。目前尚无关于该漏洞如何被利用或幕后攻击者的详细信息。

在该漏洞披露发布之际，CISA还确认了Ubiquity UniFi OS中三个CVSS评分为满分的漏洞已遭活跃利用。数天前，Defused Cyber公司表示检测到由CVE-2026-34908、CVE-2026-34909和CVE-2026-34910组成的远程代码执行链已被滥用于部署常见恶意软件。其中，CVE-2026-34908 是输入验证不当漏洞，可导致能够访问网络的恶意攻击者执行命令注入。CVE-2026-34909是一个路径遍历漏洞，可导致能够访问网络的恶意攻击者访问底层系统上的文件，这些文件可能被操纵以获取底层帐户的访问权限。CVE-2026-34910 是一个访问控制不当漏洞，可导致能够访问网络的恶意攻击者对系统进行未经授权的更改。本月早些时候，Bishop Fox详细披露了将这三个漏洞组合利用的概念验证（PoC），可通过单个请求获取具有完全root权限的反向shell。Ubiquiti已于上月末发布补丁。

比利时网络安全中心表示：“这些漏洞可能导致远程攻击者在受影响系统上进行未经授权的系统更改、访问敏感文件、泄露信息或执行任意命令，对目标设备的机密性、完整性和可用性造成严重影响。鉴于UniFi OS设备通常集中集成在网络中，成功入侵可能使攻击者进行横向移动并导致更广泛的网络攻陷。”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[CISA 要求联邦机构在本周五前修复Joomla 插件满分漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526330&idx=1&sn=42e983016d623f7d964bffc4b9b3466e&scene=21#wechat_redirect)

[CISA：SolarWinds Serv-U 高危漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526239&idx=1&sn=b82af1b66a48bb2e151a8dbfe889d0b8&scene=21#wechat_redirect)

[CISA：须在周日前修复已遭利用的 Ivanti EPMM 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525686&idx=2&sn=a7cb71292f83e55b49f1e23a7f775864&scene=21#wechat_redirect)

[CISA要求三天内修复这个严重的 F5 BIG-IP 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525571&idx=1&sn=3596dc720ddc3cfdb3245a4b7597f249&scene=21#wechat_redirect)

[CISA：Wing FTP 已遭利用漏洞可泄露服务器路径](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525482&idx=2&sn=92844a4f59d7d7b8344f344ed41a3600&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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