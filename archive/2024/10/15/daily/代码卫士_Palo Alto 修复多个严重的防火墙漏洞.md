---
title: Palo Alto 修复多个严重的防火墙漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=1&sn=2987012f618a751eabf08e620add0615&chksm=ea94a259dde32b4f7f4cd4bbb93cd3024cf4fe292975773a34fe5eecddb3c01f64facf63d74e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-15
fetch_date: 2025-10-06T18:51:42.195062
---

# Palo Alto 修复多个严重的防火墙漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSI8e2HoZiaVrnZz0LGW5ibfv7VJEPhHLKFL5kjFVkQZfEGHFSeH31OWP4yzVLrwGQPwUldpOYlblicw/0?wx_fmt=jpeg)

# Palo Alto 修复多个严重的防火墙漏洞

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周三，Palo Alto Networks 公司修复了位于 Expedition 客户迁移工具中的多个严重漏洞，并提醒称攻击者可借此接管防火墙管理员账户。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSI8e2HoZiaVrnZz0LGW5ibfv36OhLHDyfutO4MSVGwKLic0zmDDOyFbxOvicLSxLiaoibOibC3SNHEFmiaibg/640?wx_fmt=png&from=appmsg)

这些漏洞由 Horizon3.ai 发现并记录，可导致攻击者读取 Expedition 数据库内容和任意文件，以及将任意文件写入位于 Expedition 系统中的临时存储位置。从该公司发布的一项公告可知，攻击者能够访问PAN-OS防火墙的用户名、明文密码、设备配置和设备API密钥。

这些已修复漏洞如下：

* CVE-2024-9463（CVSS：9.9）——该OS命令注入漏洞可导致未认证攻击者以 root 身份执行任意OS命令，披露PAN-OS防火墙的用户名、明文密码、设备配置和API密钥。
* CVE-2024-9464（CVSS 9.3）——认证攻击者可利用OS命令注入漏洞，以root身份运行OS命令，导致与CVE-2024-9463一样暴露数据。
* CVE-2024-9465（CVSS 9.2）——SQL注入漏洞可导致未认证攻击者访问 Expedition 数据库内容，如用户名和密码哈希。攻击者还可在系统上创建并读取任意文件。该漏洞的 PoC 已公开。
* CVE-2024-9466（CVSS 8.2）——敏感信息明文存储漏洞，可导致认证攻击者洗了防火墙用户名、密码和API密钥。
* CVE-2024-9467（CVSS 7.0）——该反射型XSS漏洞可导致在认证用户浏览器中执行恶意JavaScript，已进行钓鱼攻击和会话盗取。

该公司表示这些漏洞影响早于1.2.96之前的 Expedition 版本。

Palo Alto Networks 除了提醒用户打补丁外，还提醒修改所有的Expedition 用户名、密码和API密钥以及防火墙用户名和密码。该公司表示，Expedition 的网络访问权限还应当仅限于授权用户、主机或网络。该公司表示目前尚未发现漏洞遭利用的迹象。Horizon3.ai公司已发布PoC 代码以及IoC，帮助防御人员锁定感染迹象。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&chksm=ea94bd53dde33445851c3ec7ca670a0d3c51235d027e8d130593cdc9eabd3a33d9758580655a&scene=21#wechat_redirect)

[合勤科技修复防火墙产品中的远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518947&idx=2&sn=8758a5f5ef83a075fb61fbed63159da1&chksm=ea94bb89dde3329f7456dbac7c02de7915e34069451108f060250d64c23c6f9145d80e39bcc4&scene=21#wechat_redirect)

[Juniper Networks 修复交换机、防火墙中的多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518790&idx=2&sn=8654a2f71be0f352dbd073de6482ef88&chksm=ea94bb2cdde3323a808c47f00e4a82d449bdf6bfa0d08ea05135862eb834e999aafa2ff7b965&scene=21#wechat_redirect)

[Juniper 提醒注意防火墙和交换机中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=2&sn=0cbdae2b9be2d7406ffaea5ba7dc47d1&chksm=ea94b8a7dde331b1ffbd02134c098d7117b1af631461588e39a663cd6ee5834bc93977380167&scene=21#wechat_redirect)

[速修复！开源防火墙软件pfSense 中存在多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518402&idx=3&sn=2287f259ca95d49fdb713843ffc8a1b6&chksm=ea94b9a8dde330bebb3afdf0e531542d025f12326245695da6554d9b7095da964c8f78e62a55&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/palo-alto-patches-critical-firewall-takeover-vulnerabilities/

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