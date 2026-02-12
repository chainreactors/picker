---
title: SandboxJS四大高危漏洞可完全突破沙箱控制宿主系统
url: https://mp.weixin.qq.com/s/JrKaokdFkQpffE0XVcT87Q
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:20:25.883535
---

# SandboxJS四大高危漏洞可完全突破沙箱控制宿主系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2FYojNVicMRX5AmibdKwnibpIjqWGglD1ia8PAavCgWicicxWhZgEqSVRQAsh5qsibrYxfqZgxhcatVyYeLS4U2snTt9adukmAf6a64s/0?wx_fmt=jpeg)

# SandboxJS四大高危漏洞可完全突破沙箱控制宿主系统

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX18BzlRku350jiaH3rpE76rFgBvLDRoaVGl1F2JyGKRb2AeiaUm382L7QWwF22DEAXtpqD6jibBLR9A1C5TQJz7Az1q8lJGTrEcDY/640?wx_fmt=other&from=appmsg)

专为隔离和保护 JavaScript 执行而设计的 SandboxJS 库近期曝出四个高危漏洞（CVE-2026-25520、CVE-2026-25586、CVE-2026-25587 和 CVE-2026-25641），这些漏洞均获得 CVSS 10.0 的最高风险评分，攻击者可借此完全突破沙箱限制，在宿主系统上执行任意代码。

对于依赖 SandboxJS 安全运行非受信代码的开发者而言，这些发现无异于"红色警报"。该库的安全承诺已被多种绕过核心防护的攻击途径彻底瓦解。

**Part01**

## ****漏洞技术细节****

函数返回值处理缺陷（CVE-2026-25520）

该漏洞利用库函数处理返回值时的逻辑缺陷。正常情况下，沙箱会对对象进行封装以防止其与外部环境交互，但此漏洞允许攻击者通过方法调用链访问宿主的 Function 构造函数。安全公告指出："函数返回值未被正确封装"，攻击者可通过 Object.values 或 Object.entries 获取包含宿主构造函数的数组，从而获得引擎控制权。

Map对象安全机制失效（CVE-2026-25587）

该漏洞针对通常被视为安全的 Map 对象，问题源于库的 let 实现存在缺陷，允许攻击者覆写 Map.prototype.has 方法。公告强调："由于 Map 被列入 SAFE\_PROTOYPES，其原型可通过 Map.prototype 获取"，通过覆写这一核心方法，攻击者可操纵沙箱内部逻辑实现逃逸。

宿主原型污染漏洞（CVE-2026-25586）

这是该漏洞组中最危险的漏洞，利用 SandboxJS 使用 hasOwnProperty 进行属性检查的机制。攻击者可对沙箱化对象的 hasOwnProperty 进行"影子替换"或覆写。公告警告："当返回值为真时，白名单检查将被跳过"，这一简单技巧即可绕过对 proto等敏感原型的访问限制，使攻击者能自由污染宿主环境。

检查时与使用时差漏洞（CVE-2026-25641）

这是典型的"检查时与使用时差"（TOCTOU）漏洞，源于库在验证属性键与实际使用之间存在时间差。公告解释："攻击者可传入恶意对象，这些对象在使用时会强制转换为不同的字符串值"，使得安全检查时看似无害的键在实际访问时转变为恶意载荷。

**Part02**

## ****影响范围与修复方案****

所有四个漏洞均影响 SandboxJS 0.8.28 及更早版本，维护者已在 0.8.29 版本发布完整补丁。

**参考来源：**

Code Red: 4 Critical SandboxJS Flaws (CVSS 10.0) Allow Host Takeover

https://securityonline.info/code-red-4-critical-sandboxjs-flaws-cvss-10-0-allow-host-takeover/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1QWGTwJ4jnO2icEhSqbRNdWd3iaVBKjlfTsWSdDBiayVW1jWahKjlggw6mzYnEo5D6PMvFzRX6fEpVEic5NqQoVDFCWvHlh48OxrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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