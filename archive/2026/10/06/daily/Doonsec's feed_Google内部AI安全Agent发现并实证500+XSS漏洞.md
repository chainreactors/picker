---
title: Google内部AI安全Agent发现并实证500+XSS漏洞
url: https://mp.weixin.qq.com/s/IOC2sSlS3dce3Ne-U9GAAQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:53.991476
---

# Google内部AI安全Agent发现并实证500+XSS漏洞

# Google内部AI安全Agent发现并实证500+XSS漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3icALQNczhwmdeBj8nlWJ3mOOwc7OAEfH6pO5n7CNbgDtA0GlPqseJ3cddM9ib3JmK8AicqgQVro5vedaFMVNar0m47qx6F4RFLE/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX19FanicUicQzMgc6Aia2uG2U5panmQwMibAV00VBwO8TlaCLPXYtL17V2ibp83k88RsVZvGeB2rulpCXTXfUge0HU4tXFpHBOaXObI/640?wx_fmt=webp&from=appmsg)

Google 披露了一款内部 AI 安全 Agent，目前已在其自有 Web 应用中发现 500 余个经核实的跨站脚本（XSS）漏洞。

这套名为 PageBreak 的系统专门排查可被攻击者利用、在访问者浏览器中执行恶意代码的漏洞，覆盖各类敏感服务。这一发布之所以受到关注，是因为普通 AI 扫描工具往往会产生大量可信度存疑的报告。

PageBreak 则会在真实运行环境中验证每一个疑似漏洞，确认攻击路径真实可行后，才会将问题提交给工程师。这种模式既减少了无效告警，也能挖出隐藏的 Web 漏洞。

tl;dr sec（简称 Tdr SEC）的分析师在10月1日的安全周报中重点提及了 PageBreak。本次测试属于防御性质的安全验证，不涉及恶意软件，也不代表已发生确认的入侵事件。另一项名为 The Big Sleep 的漏洞挖掘项目则主要针对数据库类漏洞。

据 Cyber Security News（CSN）查阅的公开报告显示，Google 表示 PageBreak 于2025年11月启动试点，2026年1月正式成为全职项目。该系统在“证据优先”的工作流中主要调用 Gemini 模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1O3kbPQ6lru6wwBEwtZllwzLDe0ibkkzjibo4trC1oK7Fuxa8icLETMXtKEHRPoMAzgA40DibrAg8ictMhgCD1LEQGJNHhkgfrPrhg/640?wx_fmt=png&from=appmsg)

Part01

PageBreak实证式验证流程

PageBreak 会先分析代码与流量信号，识别潜在漏洞点。它不会直接将 AI 输出作为最终安全结论，而是把疑似漏洞线索提交给专门构建的验证模块。

针对 XSS 漏洞，验证模块会先注入 JavaScript 代码，通过类浏览器测试系统打开目标页面。随后系统会检测注入的代码是否真的能够执行。

这款扫描工具不会简单标记看起来有风险的代码，而是会实证漏洞的实际影响。Google 表示，正是这套验证机制让系统的误报率接近零。同一验证方法还可用于检测 SQL 注入、路径遍历、远程代码执行、服务端请求伪造等漏洞。

此前一份关于 AI 辅助修复 Chrome 漏洞的报告显示，自动化系统可帮助团队完成浏览器漏洞的发现、复现、分级与修复工作。

PageBreak 在此基础上增加了一道关键防护环节：在上报问题前，先验证漏洞利用路径是否真实可行。

本次测试结果也验证了安全设计的效果。截至2026年9月4日，在数百个采用 Google 高保障 Web 框架构建的应用中，PageBreak 仅发现2个 XSS 漏洞，且都仅存在于加固措施不足的内部应用或调试端点，也证明了统一的框架管控可以整类杜绝相关漏洞。

Part02

构建多组有效利用链

值得注意的是，本次发现的高风险问题都不是简单的输入校验错误。其中一个案例中，PageBreak 发现了一处影响 JavaScript 文件服务器的缓存投毒漏洞。

该漏洞的成因是服务端未校验 URL 路径段，直接将其插入返回的代码中，且该路径段未被纳入缓存键计算。攻击者可以借此存储恶意响应，后续同一地理区域的其他访问者都会收到该恶意内容。

Google 目前没有发现攻击者利用该缓存漏洞的证据。但一旦被利用，就可能在 Google 敏感域名、以及加载了受影响 JavaScript 资源的外部网站上触发 XSS，这也体现了 CDN 缓存投毒攻击的典型风险：共享响应机制可将单个输入校验缺陷转化为浏览器端的代码执行风险。

第二组漏洞利用链影响管理控制台。PageBreak 发现，一处未校验的跳转值可被传入 window.location，但最初有加密签名机制阻断直接利用路径。

该 Agent 发现了一个独立的授权端点，可为恶意 JavaScript URI 生成有效签名，将原本受保护的端点转化为可利用的 XSS 路径。

第三个案例涉及 Tag Assistant Extension。该扩展对外部连接的校验较弱，加上可被获取的一次性nonce、不安全的消息转发机制，导致攻击者控制的脚本内容可传入正在调试的页面。加上扩展支持 data URL，攻击者可执行任意 JavaScript 代码，形成通用 XSS 漏洞条件。

对于未通过验证的疑似漏洞，Google 不会直接提交给产品团队，而是留存下来用于优化后续扫描规则与验证模块。Google 也承认，验证模块如果不完善，可能会漏报真实漏洞。

本次公布的结果也证明，自动化测试需要与安全框架结合使用，同时所有修复方案必须经过工程师审核，才能推送给用户。

Google 目前正在与自动补丁项目合作，处理大量已确认的漏洞报告。最终目标是让产品团队只需验证修复方案是否有效，不用反复核查 AI 生成的看似可信的报告是否对应真实安全问题。

本次公开的资料中包含受影响域名与测试样本，不涉及已确认的恶意基础设施。以下内容仅供参考，不应作为封禁名单使用。

入侵指标（IoC）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1lGUyoQsmmwOzDx7ibKO80BlicsEGiaLXgBiaXase4wufgGJgVib0XoF8Iz5tVibR5TEicb6orNS3cOZATaP10dJ7IziaOzI3f7PAibauQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2ZIdn7SxH1JxaZLFxCEuLiacXQM8oxgkC2UCa119An0NezbdKjp5uNWy6hEaI4lBibGgqkdu5KxpaUCjMTdwy4PDmCC1ORvbBkA/640?wx_fmt=png&from=appmsg)

**注：** 文中的 IP 地址与域名均已做去活化处理（例如替换为`[.]`格式），防止意外解析或跳转。仅可在 MISP、VirusTotal 或内部 SIEM 等受控威胁情报平台中恢复原始地址。

参考来源：

Google’s AI Hacker Finds 500+ XSS Flaws and Builds Working Exploit Chains

https://cybersecuritynews.com/googles-ai-hacker/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

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