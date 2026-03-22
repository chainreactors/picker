---
title: Chrome 安全更新修复 26 个漏洞，可导致远程代码执行
url: https://mp.weixin.qq.com/s/reRJ1ciUllW0yhtsmIM_mQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:35.984455
---

# Chrome 安全更新修复 26 个漏洞，可导致远程代码执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuWAyAWpN97GGUYgSUPaZZib2YdzaKsl8gP4uS30w4hQxg8NzfJav3z96PiaKkkMUficL5EA3lHic6WhEwNYiaGGt9uiayGZVA0uRrfc/0?wx_fmt=jpeg)

# Chrome 安全更新修复 26 个漏洞，可导致远程代码执行

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvA49gPRQ8zbZ1FpITFdicnibia8IXyMSxjXfUsUePJxU17wXqtj3pLgicu0Mk3IVViaHOzOEiay29iaMAnIOUrYq24A6ktN5CgDuEEf4/640?wx_fmt=jpeg&from=appmsg)

**谷歌已为其 Chrome 浏览器发布了一项重要的安全更新，修复了 26 个不同的漏洞，这些漏洞可能允许未经身份验证的攻击者远程执行恶意代码。**

最新稳定版更新中，Windows 和 macOS 平台升级至版本 146.0.7680.153 和 146.0.7680.154，而 Linux 用户将获得 146.0.7680.153 版本。

此次关键补丁周期旨在修复多个严重的内存损坏漏洞，这些漏洞对个人用户和企业网络都构成重大风险。

按照标准网络安全报告格式整理，以下内容重点说明了本次更新中缓解的最严重威胁。

---

## 关键漏洞与远程代码执行（RCE）风险

这些漏洞的主要攻击路径在于浏览器处理特定网页内容的方式。

攻击者可利用 WebGL、WebRTC 以及 V8 JavaScript 引擎等组件中的缺陷，绕过浏览器的安全沙箱机制。

本次更新共修复：

* 3 个“严重（Critical）”级漏洞
* 22 个“高危（High）”级漏洞
* 1 个“中危（Medium）”级漏洞

这些漏洞主要属于典型的内存管理错误，包括：

* 释放后使用（Use-after-free）
* 堆缓冲区溢出（Heap buffer overflow）
* 越界访问（Out-of-bounds access）

当攻击者成功触发这些漏洞（通常通过诱导用户访问恶意构造的网页），即可向系统内存写入恶意载荷，从而实现远程代码执行（RCE）。

---

## 高危组件影响范围

除关键漏洞外，22 个高危漏洞影响多个核心浏览器模块，包括：

* Blink
* Network
* WebAudio
* Dawn
* PDFium
* 9 个高危漏洞
* 1 个严重漏洞

---

## 漏洞明细列表

| CVE编号 | 严重性 | 浏览器组件 | 漏洞类型 |
| --- | --- | --- | --- |
| CVE-2026-4439 | Critical | WebGL | 越界内存访问 |
| CVE-2026-4440 | Critical | WebGL | 越界读写 |
| CVE-2026-4441 | Critical | Base | 释放后使用 |
| CVE-2026-4442 | High | CSS | 堆缓冲区溢出 |
| CVE-2026-4443 | High | WebAudio | 堆缓冲区溢出 |
| CVE-2026-4444 | High | WebRTC | 栈缓冲区溢出 |
| CVE-2026-4445 | High | WebRTC | 释放后使用 |
| CVE-2026-4446 | High | WebRTC | 释放后使用 |
| CVE-2026-4447 | High | V8 | 实现不当 |
| CVE-2026-4448 | High | ANGLE | 堆缓冲区溢出 |
| CVE-2026-4449 | High | Blink | 释放后使用 |
| CVE-2026-4450 | High | V8 | 越界写入 |
| CVE-2026-4451 | High | Navigation | 不可信输入验证不足 |
| CVE-2026-4452 | High | ANGLE | 整数溢出 |
| CVE-2026-4453 | High | Dawn | 整数溢出 |
| CVE-2026-4454 | High | Network | 释放后使用 |
| CVE-2026-4455 | High | PDFium | 堆缓冲区溢出 |
| CVE-2026-4456 | High | Digital Credentials API | 释放后使用 |
| CVE-2026-4457 | High | V8 | 类型混淆 |
| CVE-2026-4458 | High | Extensions | 释放后使用 |
| CVE-2026-4459 | High | WebAudio | 越界读写 |
| CVE-2026-4460 | High | Skia | 越界读取 |
| CVE-2026-4461 | High | V8 | 实现不当 |
| CVE-2026-4462 | High | Blink | 越界读取 |
| CVE-2026-4463 | High | WebRTC | 堆缓冲区溢出 |
| CVE-2026-4464 | Medium | ANGLE | 整数溢出 |

---

## 技术分析与风险说明

WebGL 漏洞尤其危险，因为其直接与 GPU（图形处理单元）交互，可能帮助攻击者突破软件层的限制。

同样，V8 JavaScript 引擎仍然是高价值攻击目标，例如类型混淆漏洞（CVE-2026-4457）可使攻击者操控对象类型处理逻辑。

谷歌表示，许多漏洞是在开发过程中通过先进的内存检测工具主动发现的，包括：

* AddressSanitizer
* MemorySanitizer
* libFuzzer

---

## 安全建议

为降低系统被入侵风险，强烈建议用户和企业管理员：

* 立即检查浏览器版本并完成更新
* 不要等待自动推送，优先手动更新
* 在企业环境中尽快完成补丁部署

尽管谷歌将在未来几天至数周内逐步推送更新，但提前更新可以有效防止被攻击者利用。

---

## 披露策略说明

按照惯例，谷歌将在绝大多数用户完成更新之前，限制漏洞细节及利用链的公开。

这种延迟披露策略可有效防止攻击者通过逆向分析补丁，开发针对未及时更新系统的 0day 利用代码。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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