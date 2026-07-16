---
title: 网安原创文章推荐【2026/7/14】
url: https://mp.weixin.qq.com/s/HhLRg7a09K2sN3ael-Z5aA
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:56:44.256280
---

# 网安原创文章推荐【2026/7/14】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJAAocVAiay9icrcFpcQ8e6pkVIrbhRzQnhBHfMZYfd5l9gH1jtg9aBlyCKDNO2fnJwhMtt5qmKSwyw5FRRUagPleVI1O87PCZqHqw/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/14】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-14 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-14

---

### 0x1 [黑名单不是防火墙 六边形靶场 RCE 中篇：disable\_functions、分隔符、空格绕过](https://mp.weixin.qq.com/s?__biz=MzI5NDg0ODkwMQ==&mid=2247488085&idx=1&sn=7f046e28f20d750be47f2ea32a22fabe&scene=21#wechat_redirect "黑名单不是防火墙 六边形靶场 RCE 中篇：disable_functions、分隔符、空格绕过")

> 六边形攻防安全 2026-07-14 20:26:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/FaZFJ7xrqJY1IsSQr7hezibjyrasJuVLiaz4Tqr9icJEqGm1fXDjsv6S5NnF0yetFD2EPDoQoBRBUfrCS0yASNiaGuFW2bogATqnSQPOB2E0Xv8/640?wx_fmt=jpeg)

本文深入探讨了网络安全中的命令执行漏洞（RCE）的绕过技巧，特别是在六边形攻防靶场中的Web RCE系列题目。文章详细分析了如何绕过disable\_functions限制、分隔符和空格过滤等安全机制。通过具体的题目案例，如rce-bypass\_disable\_functions、rce-bypassserparator和rce-bypass\_space，作者展示了如何利用枚举目录、正则表达式和字符编码等技巧来读取文件内容，即使是在禁用了一些常见函数和参数过滤的情况下。文章强调了理解环境限制和正确利用系统API的重要性，并提供了实际的Payload示例和结果分析，为网络安全学习者提供了宝贵的实践经验和知识。

Web安全

漏洞利用

渗透测试

PHP安全

靶场练习

安全编码

---

### 0x2 [WinFsp 竞争条件漏洞允许攻击者获得 Windows 系统级访问权限](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247487744&idx=1&sn=0fd16fb15595ae4bf903defba4404939&scene=21#wechat_redirect "WinFsp 竞争条件漏洞允许攻击者获得 Windows 系统级访问权限")

> 安全圈的那点事儿 2026-07-14 19:24:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PKZRWLgHpzBTEZ2SYPaHOzZwGsP0aBjBFpCPMkTG6vLdM8xUfPgq4ibITdjG3HcYCYR1EiaHcRwHUl1yTiatBcYAglWYt75GeNicc/640?wx_fmt=jpeg)

Windows 文件系统代理（WinFsp）存在一个严重漏洞（CVE-2026-3006），可能被本地攻击者利用以获得系统级权限。该漏洞触发于内核堆溢出，属于竞态条件缺陷，影响WinFsp 2.1.25156及更早版本。新加坡网络安全局（CSA）已发布安全更新，建议管理员尽快升级。WinFsp是一个开源框架，允许开发者构建用户模式文件系统。漏洞可能导致攻击者以SYSTEM权限执行代码，威胁操作系统内核安全。此漏洞需要本地访问权限才能被利用，但成功后可绕过安全控制，访问敏感数据。CSA强调，所有使用WinFsp的应用程序和组织应更新至最新版本，并采取预防措施以降低风险。

操作系统安全

内核漏洞

本地权限提升

竞争条件漏洞

安全更新

开源软件安全

攻击链

---

### 0x3 [一个请求头引出的 API 未授权](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247490317&idx=1&sn=79ce38257f6276b72e8d67b6019f0784&scene=21#wechat_redirect "一个请求头引出的 API 未授权")

> 进击的HACK 2026-07-14 18:31:50

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlQsNGAp0iaOILkGRgiaXnjGydsot6fF3THawkvDmyXkXzV9ht7Hy9q1lea9qSEztp7od5luL52d1pPUBjO307HRz1U2aTgPjsO0/640?wx_fmt=jpeg)

本文讲述了在网络安全测试中，通过一个请求头的差异导致API未授权的漏洞发现过程。作者在测试过程中发现，尽管目标网站的Actuator路径均返回404，但通过在H5页面请求中添加特定的请求头，如`x-id-finger: mobile`，路由被重定向到另一个暴露了Actuator接口的后端服务。文章详细分析了这一漏洞的发现过程，包括不同业务入口（PC/H5）导致的路由隔离失效，以及如何通过枚举请求头和子路径来发现未授权接口。此外，文章还提供了针对此类问题的防御建议，包括网关层和应用层的修复措施，强调了在进行安全测试时关注不同业务入口差异的重要性。

Web安全

API安全

微服务安全

请求头安全

漏洞挖掘

安全测试

安全配置

---

### 0x4 [手把手教你IDA自动逆向分析样本](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485782&idx=1&sn=70c3dd6f85dcd5ea3b9148f7658ba4fe&scene=21#wechat_redirect "手把手教你IDA自动逆向分析样本")

> 安全天书 2026-07-14 17:14:53

![](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQXt9BgULeIeuPAMtwmOLTDB52TIVWIJvBSRC2ribEibeSpjb8jTPNZZatwSmSIwV4ia9bd4icyMon8FYBNWff7S6CZ5BChDBEFGhMQ/640?wx_fmt=jpeg)

本文详细介绍了如何使用IDA进行自动逆向分析样本的步骤。首先，介绍了所需的软件安装过程，包括Node.js、Git for Windows、Claude Code和CC switch。接着，指导读者如何安装和配置IDA 9.3版本以及ida-pro-mcp插件。文章还提供了配置.mcp.json文件的示例，以便启动逆向分析。最后，文章强调了使用IDA分析DLL文件、检测执行shellcode操作以及解密shellcode的重要性。此外，文章还提到了加入一个专注于渗透测试、红蓝对抗、钓鱼手法思路和武器化的圈子，以及分享的相关技术文章和工具。

逆向工程

安全工具

安全开发

代码审计

恶意代码分析

安全研究

操作系统安全

编程语言

---

### 0x5 [美海军最新研究：将二进制文件变成AI逆向的提示注入武器](https://mp.weixin.qq.com/s?__biz=MzYzNjEwMTkyMA==&mid=2247485442&idx=1&sn=de633dc0c7842358f781117b44a5c97e&scene=21#wechat_redirect "美海军最新研究：将二进制文件变成AI逆向的提示注入武器")

> 猫头鹰OSINT 2026-07-14 17:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/SmpxklM1IWxbBMvohjwfoq2O5CxSY0ZoeQEibibKO6aTC9pRGuER6fhTGazFAs2RX9p6SB0D3rYGicK8sC952EXicrdx5rU9jssib86s3t0E8aTU/640?wx_fmt=jpeg)

美国海军研究生院的研究揭示了网络安全领域的新风险，即攻击者可以通过在二进制文件中隐藏特殊字符串来诱导AI逆向分析工具产生错误判断。这种攻击方式被称为二进制级提示注入攻击，它将提示注入技术从网页、文档和聊天内容扩展到软件二进制文件领域。研究团队发现，攻击者可以在不改变程序运行结果的情况下，通过在程序中加入字符串变量来影响AI分析系统的判断。这种攻击利用了Ghidra等逆向工程平台与AI模型的结合，通过AI模型对代码的理解来生成分析报告。研究还表明，攻击者可以通过设计短小、高效的攻击载荷来绕过Ghidra对字符串长度的限制。此外，研究团队还探讨了基于规则和机器学习的检测方法，并提出了建立多层防御体系来应对这种新型攻击。

AI攻击

逆向工程

二进制分析

恶意软件分析

人工智能安全

软件供应链攻击

机器学习安全

防御策略

---

### 0x6 [仅核查网址远远不够：利用微软官网实施的设备代码钓鱼攻击](https://mp.weixin.qq.com/s?__biz=MzAxNjg3MjczOA==&mid=2247487837&idx=1&sn=2a9dacf754eb96f4ea5cc858990c6120&scene=21#wechat_redirect "仅核查网址远远不够：利用微软官网实施的设备代码钓鱼攻击")

> 卡巴斯基威胁情报 2026-07-14 13:54:25

![](https://mmbiz.qpic.cn/mmbiz_jpg/5DBHibIELyXB7E9tSI1EQFIwpH8m9lo7fgDn1c9HscDGDD7gUnsmHgJFhtVyibwxJ4ltrr09ZBer5Xs2bx5Ukoyib3BClhK0q8InHzjalYONPM/640?wx_fmt=jpeg)

本文揭示了利用微软官方身份平台进行的设备代码钓鱼攻击的新型攻击方式。这种攻击利用了设备授权许可的 OAuth 2.0 规范，让攻击者在受害者不知情的情况下获取登录凭证。文章详细描述了设备授权码流程的各个步骤，包括请求授权码、向用户展示验证码、输入验证码并授权访问、轮询查询服务端授权状态、下发各类访问令牌以及自动续期访问权限。文章还分析了攻击者如何通过伪装成正规邮件和PDF文件诱导用户点击恶意链接，最终跳转至仿冒企业法务门户进行钓鱼攻击。此外，文章提出了抵御设备码钓鱼攻击的防护方案，包括用户提高警惕、企业评估和关闭不必要的设备码授权流程，以及部署邮件安全防护工具等。

钓鱼攻击

网络安全意识

OAuth 2.0

多因素认证

企业安全防护

恶意软件

域名安全

---

### 0x7 [聊一聊CORS跨域漏洞的危害](https://mp.weixin.qq.com/s?__biz=MzIxOTQ1OTY4OQ==&mid=2247487970&idx=1&sn=15c34126a68c266d52e663f1a937062b&scene=21#wechat_redirect "聊一聊CORS跨域漏洞的危害")

> 重生之成为赛博女保安 2026-07-14 13:50:23

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bcFEmmDxVAjo6RicJM4j9JgQY12FUlnrLZt0icaXia1jysWLEP0ZJmhEj4snh9ZD4jM4LAymtMAcacy0Hndzib2N1ps1CJ04mibb3sIJEkQJxS0w/640?wx_fmt=jpeg)

本文详细探讨了CORS跨域漏洞的危害、利用方式和防护措施。首先介绍了CORS的概念和浏览器的同源策略，解释了当端口、协议或域名不同时，两个网站被视为跨域。接着，文章阐述了CORS失效可能导致的危害，如数据窃取和钓鱼攻击。在利用方面，文章分析了CORS失效的常见场景，包括通过构造特定域名绕过后端校验逻辑、利用iframe反射漏洞等。最后，文章提出了防护措施，包括严格校验ACAO、设置SameSite属性以及控制凭证的存储和使用，以降低CORS漏洞的风险。

跨域资源共享（CORS）

网络安全漏洞

浏览器安全策略

Web安全

数据窃取

XSS攻击

CSRF攻击

防护措施

---

### 0x8 [自写c2单文件对抗EDR](https://mp.weixin.qq.com/s?__biz=MzkyMTcwNTQyMQ==&mid=2247484064&idx=1&sn=bbc6c5dfa03531dbb7d21542a9b4c168&scene=21#wechat_redirect "自写c2单文件对抗EDR")

> freedom安全 2026-07-14 11:47:28

![](https://mmbiz.qpic.cn/mmbiz_jpg/Lem2Faf53JDBv71rl03rPTd7MwaGkeZibsCndtqsXhEsa9azibrjNZe9beibH9rTMArd5lf0XtFFrGPuCmg4BnlicF1qeSbdOSuQ14vR1YmUPoI/640?wx_fmt=jpeg)

本文主要探讨了自写C2（Command and Control）在对抗企业内部安全防御系统EDR（Endpoint Detection and Response）时的实际作用。作者指出，尽管有师傅提出自写的C2在断网和杀毒能力上较弱，但实际上在许多企业内网中，安全代理（agent）并未完全联网，因此自写的C2在这些环境中仍具有一定的实战价值。本期文章将重点分析在实战出网环境下，面对近期更新的病毒库，自写的C2在以下安全防御系统中的表现：天擎、某山终端、某步、某融信天擎、某盟。文章强调了在联网且信任区无文件的情况下，这些安全防御系统的应对能力。

C2通信

EDR对抗

病毒库更新

实战研究

企业内网安全

终端安全

---

### 0x9 [t.me突然全球失联：不是服务器宕机，钓鱼围猎已经开始](https://mp.weixin.qq.com/s?__biz=MzI1MDkwNzQ4NA==&mid=2247484056&idx=1&sn=0532ddfb8f8e64f6eb7280c8da467a72&scene=21#wechat_redirect "t.me突然全球失联：不是服务器宕机，钓鱼围猎已经开始")

> MessFreeSecurity 2026-07-14 11:26:13

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMBHZjccYnZIj54v3WuteAdOqe4WYnzcH1MSlJl6em06JfYoSA3rko90fRwDqk2kJ3EBZ5Kh24Wqn1WP9ex1viaX3L5Z5DMP5UZ0/640?wx_fmt=jpeg)

2026年7月14日，Telegram短链接域名t.me出现全球失联现象，经调查发现并非服务器宕机，而是域名被注册局设置为serverHold状态，导致公共DNS无法返回其A记录。同时，安全监测发现新注册的域名正在仿冒Telegram登录页，试图收集用户信息。尽管存在解析故障和钓鱼基础设施的证据，但无法证明钓鱼团伙制造了故障或接管了t.me域名。t.me的到期时间正常，且故障仅限于短链接域名，不影响Telegram消息服务。安全团队发现仿冒登录页面和数据接收API，以及一个高度可疑的二维码仿冒页。事件发生后的几小时内，钓鱼域名被注册，表明攻击者迅速行动。文章强调了事件中时间上的巧合不能证明攻击者事先知情或制造了故障。

DNS劫持

钓鱼攻击

域名注册

安全监测

用户教育

威胁情报

应急响应

安全事件分析

---

### 0xa [开源一个 OTP 管理工具-口令盒子](https://mp.weixin.qq.com/s?__biz=Mzg5NzY5NjM5Mg==&mid=2247486103&idx=1&sn=00f45a59e4015bfae774c4499b74bfbc&scene=21#wechat_redirect "开源一个 OTP 管理工具-口令盒子")

> YY的黑板报 2026-07-14 10:31:04

![](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tLgpccicrGZzlbOkGPuHwL2zFIe2Uyk8S5yAvD0ECeWj93xN3vZZDoibM0rsUW2zv3nmoKSZ2s5icRnYWcwQ37D6gusHbdzxpZwLs/640?wx_fmt=jpeg)

本文介绍了一款名为OTP盒子的开源OTP管理工具的开发背景和功能。作者指出，虽然市面上有许多OTP管理工具，但许多不开源的OTP工具存在广告或同步费用问题，而开源工具如Aegis则缺乏同步功能。因此，作者决定自己开发一款OTP管理工具。OTP盒子是一款Android应用，它强调隐私和安全，支持本地加密存储密钥，并提供指纹或PIN应用锁。该工具支持通过GitHub Gist进行端到端加密同步。功能包括扫码添加、导入图片、手动录入密钥、支持口令盒子备份格式、编辑服务名和账号等。为了确保安全，OTP盒子使用了SQLCipher加密数据库和EncryptedSharedPreferences，并提供了指纹、面容和设备凭证解锁以及PIN码备用解锁。此外，应用还支持自动锁定和备份同步加密导出。

开源软件

移动应用安全

两步验证

数据同步

加密技术

备份与恢复

用户认证

---

### 0xb [好文 | 藏在 Windows 里的永久指纹 GDID —— FBI 靠它锁定了 Scattered Spider](https://mp.weixin.qq.com/s?__biz=MzI2Mjk4NjgxMg==&mid=2247484682&idx=1&sn=2cc583b001c28e144deaec70d5d102aa&scene=21#wechat_redirect "好文 | 藏在 Windows 里的永久指纹 GDID —— FBI 靠它锁定了 Scattered Spider")

> 赛博生...