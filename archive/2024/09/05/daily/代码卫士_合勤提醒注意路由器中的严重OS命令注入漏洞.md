---
title: 合勤提醒注意路由器中的严重OS命令注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=2&sn=a47864fc0328391d921ce4629b3bac8b&chksm=ea94a0f6dde329e023f990c89d3f4b6a44d09f2026fcdb3ad4e8deed8958ffe6ef4fa464fc38&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-05
fetch_date: 2025-10-06T18:26:59.320333
---

# 合勤提醒注意路由器中的严重OS命令注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQFiaibvHLibibPhJbHJslBahJym8ccAfSSzfaMuJBxNcXRBLByQmeIz9PvNhDHIyN2UDMThcWiavkLGNQ/0?wx_fmt=jpeg)

# 合勤提醒注意路由器中的严重OS命令注入漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**合勤科技发布安全更新，修复了影响多款商业路由器中的一个严重漏洞 (CVE-2024-7261)，可能导致未认证攻击者执行OS命令注入。**

该漏洞的CVSSv3评分为9.8，是一个因用户提供数据处理不当引发的输入验证漏洞，可导致远程攻击者在主机操作系统上执行任意命令。

合勤科技提醒称，“某些AP和安全路由器版本的CGI程序的 ‘host’ 参数中的特殊元素中和不当，可导致未认证攻击者通过向易受攻击设备发送构造 cookie 的方式执行OS命令。”

受该漏洞影响的合勤科技访问点包括：

* NWA 系列：NWA50AX、NWA50AX PRO、NWA55AXE、NWA90AX、NWA90AX PRO、NWA110AX、NWA130BE、NWA210AX和NWA220AX-6E，所有7.00及以下版本均易受攻击，需升级至7.00(ABYW.2) 及后续版本；
* NWA1123-AC PRO，所有6.28及以下版本均易受攻击，需升级至6.28(ABHD.3) 及后续版本；
* NWA1123ACv3、WAC500、WAC500H：所有6.70及以下版本均易受攻击，需升级至6.70(ABVT.5)及后续版本；
* WAC 系列：WAC6103D-I、WAC6502D-S、WAC6503D-S、 WAC6552D-S、WAC6553D-E，所有6.28及以下版本均易受攻击，需升级至6.28(AAXH.3) 及后续版本；
* WAX 系列：WAX300H、WAX510D、WAX610D、WAX620D-6E、WAX630S、WAX640S-6E、WAX650S和WAX655E，所有7.00及以下版本易受攻击，需升级至upgrade to 7.00(ACHF.2) 及后续版本；
* WBE 系列：WBE530、WBE660S，所有7.00及以下版本均易受攻击，需升级至7.00(ACLE.2) 及后续版本

合勤科技表示，运行V2.00 (ACIP.2) 的安全路由器 USG LITE 60AX也受影响，但该机型通过云自动更新至 V2.00 (ACIP.3)，即执行了相关补丁。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQFiaibvHLibibPhJbHJslBahJyDAp2wYLB3397bxYzXIAAw8rtZwen7vEugbsibB6kLayjD5ibpcBGeBKg/640?wx_fmt=gif&from=appmsg)

**更多修复方案**

合勤科技还未位于APT和USG FLEX 防火墙中的多个高危漏洞发布安全更新，概览如下：

* CVE-2024-6343：CGI 程序中的缓冲区溢出漏洞，可被认证管理员通过发送构造HTTP请求的方式触发DoS。
* CVE-2024-7203: 认证后命令注入漏洞，可导致认证管理员通过构造的CLI命令执行OS命令。
* CVE-2024-42057：IPSec VPN中的命令注入漏洞，可导致未认证攻击者通过在 User-Based-PSK模式中构造的长用户名执行OS命令。
* CVE-2024-42058：空指针解引用漏洞，可通过未认证攻击者发送的构造数据包引发DoS。
* CVE-2024-42059：认证后命令注入漏洞，可导致认证管理员通过FTP上传构造的压缩语言文件，执行OS命令。
* CVE-2024-42060：认证后命令注入漏洞，可导致认证管理员上传构造的内部用户协议文件执行OS命令。
* CVE-2024-42061： Reflected XSS in "dynamic\_script.cgi" 中的反射型XSS，可导致攻击者诱骗用户访问构造的URL，泄露基于浏览器的信息。

其中最值得注意的是CVE-2024-42057（CVSS v3 8.1，“高危”）。它是位于IPSec VPN特性中的一个命令注入漏洞，可在无需认证的情况下遭远程利用。其严重性因为利用所需的特定配置要求而减轻，包括在 User-Based-PSK 认证模式下配置设备并拥有一个用户名超过28个字符的用户。

关于受影响防火墙的更多详情，可见合勤科技发布的安全通告。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[合勤紧急修复NAS设备中的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519665&idx=1&sn=16f68838d4899ea09b8df2f5f96357ab&chksm=ea94bcdbdde335cdc94e76fa3278e8af36adadc6af065778ed4f389d32ac7d826a4ad944c89f&scene=21#wechat_redirect)

[合勤科技修复防火墙产品中的远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518947&idx=2&sn=8758a5f5ef83a075fb61fbed63159da1&chksm=ea94bb89dde3329f7456dbac7c02de7915e34069451108f060250d64c23c6f9145d80e39bcc4&scene=21#wechat_redirect)

[合勤提醒注意 NAS 设备中的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518251&idx=2&sn=e34aa255b21da7352d4cee7ee282c3a2&chksm=ea94b941dde330570cdee756bdd509db2cfbd20562651fa3418a04f3424d1d19ff98455b0ee8&scene=21#wechat_redirect)

[合勤科技修复NAS 设备中的高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516649&idx=2&sn=8568497e673e6061401b953a0bb37e2d&chksm=ea94b083dde3399587e9f570cb506e4f4d17d2f23280a147343bc96a5a1c55eaa427de1dffb0&scene=21#wechat_redirect)

[合勤科技防火墙和VPN设备中存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516588&idx=2&sn=9de12fd66aca0db1dd5cf6843cf5172b&chksm=ea94b0c6dde339d067936cdf6ad3806f1669be3d65022c613d8544726872d4dca7d3377e4a9f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/zyxel-warns-of-critical-os-command-injection-flaw-in-routers/

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