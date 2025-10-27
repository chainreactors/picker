---
title: 7-Zip 修复高危的 Windows MoTW 安全告警绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522153&idx=1&sn=b0d2973a6eb87e554fb62b7ddfa10dfb&chksm=ea94a603dde32f1580de59ef6a2b8fb600c6cbb237024a672b5a02660c7fc1f7184f617fce4c&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-23
fetch_date: 2025-10-06T20:10:45.247891
---

# 7-Zip 修复高危的 Windows MoTW 安全告警绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT3icUvv91H5am4P8bs3ruPy3VQSthKDzfwY3V6YRTQkmfHEqnpbYzaeTG6ShStZ0dsqtXMltNg0TQ/0?wx_fmt=jpeg)

# 7-Zip 修复高危的 Windows MoTW 安全告警绕过漏洞

SERGIU GATLAN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**7-Zip 文件压缩文档中存在一个高危漏洞，可导致攻击者绕过 MotW Windows 安全特性，从所嵌入的文档中提取恶意文件时在用户计算机上执行代码。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT3icUvv91H5am4P8bs3ruPyTG06PrArS7dHORm3755og3OgKSGwEkbbhw9tGlfENtGibRC34hdRLOQ/640?wx_fmt=gif&from=appmsg)

7-Zip 在2022年6月发布的版本22.00开始引入对 MotW 的支持，之后它在从所下载文档中提取的所有文件中加入 MotW 标记（特殊的 ‘Zone.Id’ 可选数据流）。这一标记通知操作系统、web浏览器和其它应用称，这些文件可能来自不可信来源，应当谨慎处理。

因此，当双击通过7-Zip 提取的风险文件时，用户将会收到告警称打开或运行此类文件可导致潜在危险行为，如在设备上安装恶意软件等。微软 Office 也会检查 MotW 标记，如找到则会在受保护视图中打开文档，自动启用只读模式并禁用所有宏。

然而，正如趋势科技在上周五发布的安全公告中提到的那样，CVE-2025-0411可导致攻击者绕过这些安全告警并在目标计算机上执行恶意代码。趋势科技提到，“该漏洞可导致远程攻击者绕过受影响7-Zip 上的 MotW 防护机制。由于目标必须访问恶意页面或打开恶意文件，因此利用该漏洞时需要用户交互。该漏洞位于对压缩文件处理的方式中。当从配有MotW 的构造文档中提取文件时，7-Zip 并不会将MotW复制到所提取的文件中。攻击者可利用该漏洞在当前用户上下文中执行任意代码。”

幸运的是，7-Zip的开发人员 Igor Pavlov 已在2024年11月30日发布7-Zip 24.09 版本修复该漏洞。Pavlov 表示，“7-Zip File Manager 并未向从所嵌入文档中提取的文件复制到Zone.Identifier 流。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT3icUvv91H5am4P8bs3ruPyfAIepgl6VAfanrQvOIrKI4q0c3lI3l771jDc7PDB0LpHqpiaZibNO6GQ/640?wx_fmt=png&from=appmsg)

**类似漏洞被用于部署恶意软件**

然而，由于7-Zip并不具备自动更新特性，因此很多用户可能仍然运行易受攻击版本，从而易遭恶意软件感染。

鉴于此类漏洞经常被用于恶意攻击中，因此所有7-Zip用户应当尽快修复。例如，去年6月，微软修复了一个MotW 安全绕过漏洞 (CVE-2024-38213)，而恶意软件操纵组织 DarkGate 已从2024年3月起在野利用该0day，规避SmartScreen 防护措施并安装伪装成 Apple iTunes、NVIDIA、Notion 等合法软件的恶意软件。

受经济利益驱动的黑客组织 Water Hydra（即DarkCasino）还利用另外一个 MotW 绕过漏洞 (CVE-2024-21412) 攻击Telegram 股票交易渠道以及通过DarkMe 远程访问木马攻击Forex交易论坛。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[开源压缩软件7-Zip 被曝严重的远程代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487326&idx=2&sn=a6bc76f326cd47c770b8740c7374fa9e&scene=21#wechat_redirect)

[Fortinet：注意这个认证绕过0day漏洞可用于劫持防火墙](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522078&idx=2&sn=a6a418ea6abb9635205b06203e061801&scene=21#wechat_redirect)

[Ivanti：注意这个CVSS 满分的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521758&idx=1&sn=d87a2de8e47def08cf6aca1b91b6e064&scene=21#wechat_redirect)

[用户名太长的坏处：Okta 修复认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521392&idx=1&sn=5ed582159f171db2001138a8ba65e297&scene=21#wechat_redirect)

[GitLab修复严重的 SAML 认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=1&sn=99796b9ba1361fcd9611a05729e2219d&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/7-zip-fixes-bug-that-bypasses-the-windows-motw-security-mechanism-patch-now/

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