---
title: WGS-804HPT 交换机中存在多个严重漏洞，可导致RCE和网络利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522124&idx=1&sn=8b928d650502c3cebc7b2ae0e85282a2&chksm=ea94a626dde32f303236d54cf10c68cbf25ac8104fe9a6280306ddbcce4f3ce7624240d24d9d&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-21
fetch_date: 2025-10-06T20:10:55.303636
---

# WGS-804HPT 交换机中存在多个严重漏洞，可导致RCE和网络利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR6ZOFfCoxsatfJYRKOJRvxtdIT6PIHMScY4FQIWgj7C0E9lfOXmJuRp7VkNWicKggAVAxT3kISO5Q/0?wx_fmt=jpeg)

# WGS-804HPT 交换机中存在多个严重漏洞，可导致RCE和网络利用

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究员在 Planet技术公司的 WGS-804HPT工业交换机中存在三个漏洞，它们可被用于在可疑设备上实现预认证远程代码执行。**

上周四，Claroty 公司的研究员 Tomer Goldschmidt发布报告提到，“这些交换机广泛用于多种联网应用的楼宇和家庭自动化系统。攻击者如能远程控制其中一台设备，则可利用这些漏洞进一步利用内网中的设备并进行横向移动。”

研究人员对使用QEMU框架的交换机中的固件进行了大规模分析发现，这些漏洞位于用于提供web服务的 dispatcher.cgi接口中，这些漏洞如下：

* CVE-2024-52558（CVSS 5.3）：整数下溢漏洞，可导致未认证攻击者发送恶意HTTP请求，导致崩溃。
* CVE-2024-52320（CVSS 9.8）：操作系统命令注入漏洞，可导致未认证攻击者通过恶意HTTP请求发送命令，导致远程代码执行后果。
* CVE-2024-48871（CVSS 9.8）：基于栈的缓冲溢出漏洞，可导致未认证

攻击者发送恶意HTTP请求，导致远程代码执行后果。

成功利用这些漏洞可导致攻击者在HTTP请求中嵌入一个 shellcode，劫持执行流，获得执行操作系统命令的能力。厂商收到负责任的披露后，已在2024年11月15日发布的1.305b241111版本中推出补丁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[引导加载程序存在高危漏洞，影响思科100多个交换机机型](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521713&idx=1&sn=7bdde63b35fa4a28908581f18c38883e&scene=21#wechat_redirect)

[CISA提醒修复RAD SecFlow-2 工业交换机中的路径遍历漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519815&idx=1&sn=39b57daed4e444ed2e6237921fc44ab3&scene=21#wechat_redirect)

[Juniper Networks 修复交换机、防火墙中的多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518790&idx=2&sn=8654a2f71be0f352dbd073de6482ef88&scene=21#wechat_redirect)

[Westermo 交换机存在多个漏洞，可攻击工业机构](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518768&idx=2&sn=7e5a15f8e434a2cc30a909c178e962e5&scene=21#wechat_redirect)

[Juniper 提醒注意防火墙和交换机中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=2&sn=0cbdae2b9be2d7406ffaea5ba7dc47d1&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/01/critical-flaws-in-wgs-804hpt-switches.html

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