---
title: 网安原创文章推荐【2026/1/17】
url: https://mp.weixin.qq.com/s/7MwojwqqmxgZmh1C52L6SA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:39:17.358249
---

# 网安原创文章推荐【2026/1/17】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vML07fExwAdic7EnrrQjaUrnibw10qNCquZ9WPV7FKRicGgPkYs8YbQNUDU8ibOOBpYsZpYk8Dqm7ibq1YQQzLJs71A/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/1/17】

AJay13
AJay13

洞见网安

![]()

在小说阅读器中沉浸阅读

# 2026-01-17 微信公众号精选安全技术文章总览

> 洞见网安 2026-01-17

---

### 0x1 [AI免杀工具 对抗Google平台62款杀软](https://mp.weixin.qq.com/s?__biz=Mzk5MDIyNTQzMA==&mid=2247484029&idx=1&sn=22c357c25a474bb6572f94a6a4861270&scene=21#wechat_redirect "AI免杀工具 对抗Google平台62款杀软")

> 金刚狼不懂安全 2026-01-17 23:16:34

![](https://mmbiz.qpic.cn/mmbiz_jpg/Bua8mEDRSfdOy1eSIwWWBZMtfYqJyRFmD58KvLFeVE9gh7fPswMVdXDbazUGWoAuC6Zdiaxe2xU6wZahHHye9kg/640?wx_fmt=jpeg)

CodeBypass 是一款基于 AI 的免杀工具，专注于通过智能变异与语义重构提升后门脚本在静态与行为检测中的通过率。它支持 PHP、JSP、ASP、ASPX 等常见 webshell 格式的快速免杀，并具备多语言支持、智能变异、语义保持、多样化策略、快速迭代、适应性学习等能力。CodeBypass 通过自动化免杀流程，减少人工成本，并适合在本地测试与自动化场景中对接模型推理能力。文章还介绍了 CodeBypass 的使用方法，包括调用本地 webshell 和接入 AI 大模型的配置。此外，文章展示了 CodeBypass 在杀软检测平台上的效果，以及生成的 WebShell 代码样例，说明了其隐蔽性高和功能正常的特点。最后，文章提到了 AI 一键免杀工具 1.0 已发布，提供了大量 wolfshell 变种成果，包括哥斯拉 JSP 和 PHP 的一句话免杀变种。

人工智能免杀

Webshell免杀

代码变异

语义保持

多语言支持

AI模型集成

自动化安全工具

恶意软件检测

---

### 0x2 [做个\"脚本小子\"--fscan.exe的免杀篇](https://mp.weixin.qq.com/s?__biz=Mzk0NDYyNzAyMw==&mid=2247483921&idx=1&sn=b5960d3a65de444becc7791cf17ea50a&scene=21#wechat_redirect "做个\")

> kingman安全 2026-01-17 22:34:58

![](https://mmbiz.qpic.cn/mmbiz_jpg/XxjRljYHYk0SaTgP2s3YtHwwdatfIlDrweGOezXyJoF0gjibwbhvw79TxME1xYCngEANa0PQKcic9aTAeyBGLFfw/640?wx_fmt=jpeg)

本文主要介绍了如何通过一系列步骤来制作一个免杀的fscan工具。首先，文章指导读者在Windows和Linux环境下进行环境配置，包括安装Go语言环境、设置环境变量等。接着，文章详细介绍了如何下载并配置fscan工具，包括修改go.mod文件、替换代码中的特定字符串等。为了实现免杀，文章建议使用garble工具对Go代码进行混淆，以避免被杀软识别。具体操作包括删除不必要的代码、使用garble混淆代码、生成可执行的exe文件等。最后，文章还提供了一些额外的建议，如使用VMP加壳或upx加壳来进一步加强免杀效果。整个过程详细且实用，对于想要制作免杀工具的网络安全学习者来说是一个很好的参考。

网络安全

恶意软件开发

代码混淆

免杀

渗透测试

反分析

---

### 0x3 [Stowaway多级代理工具](https://mp.weixin.qq.com/s?__biz=MzkwMTcwNzEwOA==&mid=2247483846&idx=1&sn=6d9c85da2184b338c72650bc4f934433&scene=21#wechat_redirect "Stowaway多级代理工具")

> 白小客 2026-01-17 21:27:51

![](https://mmbiz.qpic.cn/mmbiz_jpg/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6409yq12RKF0mTYVx3EoXTr1jc3p2SibAxHHzdpBMCicw88UsvwbMOudg/640?wx_fmt=jpeg)

本文介绍了一款名为Stowaway的多级代理工具，该工具使用Go语言编写，旨在帮助渗透测试人员突破内网访问限制。Stowaway支持Windows、Linux和mac操作系统，并能适配不同架构。工具操作简单，无需修改配置文件，命令直观。文章详细介绍了Stowaway的基本功能、部分命令解释以及如何使用该工具建立多级代理。具体包括如何设置被动监听地址、通信加密密钥、主动模式下的目标节点地址等。文章通过三个Windows主机的拓扑图演示了Stowaway的搭建过程，包括服务端、一层代理和三层代理的设置，并指出在实际使用中需要注意端口放行和防火墙规则。此外，还提到了如何设置socks5代理以及如何解决乱码问题。

渗透测试工具

代理服务器

内网穿透

网络安全

命令行工具

跨平台

加密通信

---

### 0x4 [漏洞科普——React Server Components 拒绝服务漏洞（CVE-2025-67779）](https://mp.weixin.qq.com/s?__biz=Mzk0MzczMDE2Ng==&mid=2247484143&idx=1&sn=ff78dd606c0f1e36dbee2ac69527efb0&scene=21#wechat_redirect "漏洞科普——React Server Components 拒绝服务漏洞（CVE-2025-67779）")

> w小小杂谈w 2026-01-17 20:49:53

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/H4a8P08TZsiatFjnQibsYG5Rla2Wsrcic4IiczdMwlEiaiav6VwFgVM79o8c1nty6JPMNujHXkeYLkTK4tzOJtcj6FYg/640?wx_fmt=jpeg)

CVE-2025-67779 是一个影响 React Server Components（RSC）服务端包的高严重性拒绝服务（DoS）漏洞。该漏洞由不安全的反序列化逻辑引起，攻击者通过发送特制的 HTTP 请求可导致服务器进入无限循环状态，从而挂起服务器进程并消耗大量 CPU 资源，使得服务不可用。这一漏洞是由于对 CVE-2025-55184 补丁修复不完整导致的，即使用户已经应用了之前的修复补丁，仍可能存在风险。漏洞的利用原理在于服务端在处理客户端发送的序列化 HTTP 请求负载时，由于未对外部输入进行安全约束，在特定条件下会进入无限循环或逻辑挂起路径。防御措施包括升级到官方修复版本，受影响的包有 react-server-dom-webpack、react-server-dom-turbopack 和 react-server-dom-parcel，安全版本应至少为 19.0.3 或更高版本。

漏洞分析

拒绝服务攻击

React安全

反序列化漏洞

软件补丁

安全漏洞分类

---

### 0x5 [【钓鱼攻防】手把手带你学会GoPhish钓鱼框架](https://mp.weixin.qq.com/s?__biz=Mzg5NTU2NjA1Mw==&mid=2247505192&idx=1&sn=ed157569dcb35fdbabbf8b2a1b29f3b2&scene=21#wechat_redirect "【钓鱼攻防】手把手带你学会GoPhish钓鱼框架")

> 平凡安全 2026-01-17 20:01:54

![](https://mmbiz.qpic.cn/mmbiz_jpg/v94hWOZcBpxf5ujLrIwurOt7k2PHrAOyJRyhBDFQeYrKic1DL3rEpMA4MVpqqVzP47D8x11X9kOUicOre8VIwgXQ/640?wx_fmt=jpeg)

本文详细介绍了网络安全领域的钓鱼攻防技术，以Gophish开源项目为例，手把手教学如何搭建钓鱼测试平台。文章首先强调了网络安全学习中承认自身弱点的重要性，并指出知识面和知识链对于攻击面的宽度和杀伤链的深度至关重要。接着，文章详细指导了如何搭建Gophish平台，包括下载安装、配置文件、远程访问设置等。随后，文章深入讲解了如何设置发件人邮箱、创建钓鱼页面、编辑内容、捕获提交数据以及配置邮件模板等操作。此外，文章还介绍了如何导入用户邮箱、创建钓鱼事件、配置发送策略等。最后，文章提醒了钓鱼邮件发送时的注意事项，并强调了使用钓鱼技术时应遵循的道德和法律规范。

网络安全钓鱼

网络安全测试

GoPhish框架

网络安全工具

密码捕获

邮件安全

渗透测试

---

### 0x6 [【接口漏洞第六章第四节】绕过前端限制：浅析REST路径中的服务器端参数污染漏洞](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797748&idx=1&sn=1ceb82965d28b1ffc969c7ff4cbf8d3e&scene=21#wechat_redirect "【接口漏洞第六章第四节】绕过前端限制：浅析REST路径中的服务器端参数污染漏洞")

> 升斗安全 2026-01-17 19:21:09

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0qQibWnvfBicRDkLqdwzee0YTTxWkYfkoIwEcVTEfbjPdvriatoQSLLyQ8VpJPyZQniaVMXQM7TXLNKw/640?wx_fmt=jpeg)

本文旨在探讨RESTful风格系统中的一种接口漏洞——服务器端参数污染。文章首先介绍了RESTful API的特点，指出其参数通常置于URL路径中而非查询字符串。通过具体示例，阐述了攻击者如何通过操纵URL路径参数来利用该API进行越权访问。文章详细解释了路径遍历攻击的原理，并举例说明了如何通过URL编码来修改参数值，导致服务器端请求路径的改变。最后，文章强调了对API接口漏洞的研究将持续进行，并鼓励读者关注相关内容。

接口安全

RESTful API

路径遍历

服务器端漏洞

安全漏洞

---

### 0x7 [【杀软对抗】HeavenlyBypassAV免杀工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247484880&idx=1&sn=334f084dfed22f942c17921b4f583d33&scene=21#wechat_redirect "【杀软对抗】HeavenlyBypassAV免杀工具")

> 安全天书 2026-01-17 19:00:57

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvSCMR82FwEgBnBedBm3XI4RibLKGSiatPticIZ0cMhoOWMoVFZBw6pMUsB6NLOtRkkicnlmTeDxgLBSr2hfyQbArA/640?wx_fmt=jpeg)

本文介绍了一种名为HeavenlyBypassAV的自动化免杀生成工具，该工具支持绕过360核晶、火绒、Windows Defender、微步沙箱等安全软件的检测。文章强调，这些技术和工具仅用于安全测试和防御研究，禁止用于非法入侵或攻击他人系统。文章详细描述了工具的免杀效果，包括对360静态扫描和火绒动态上线的绕过效果。此外，文章还提到了一个名为“红蓝偶像练习生”的小圈子，该圈子专注于渗透测试、红蓝对抗、钓鱼手法研究等技术领域，并分享了一系列相关技术文章和工具。

网络安全工具

免杀技术

安全测试

杀软对抗

渗透测试

红蓝对抗

钓鱼攻击

恶意软件分析

安全研究

---

### 0x8 [记几个edusrc简单挖掘案例](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247486575&idx=1&sn=d5990540619f781dd43e35684a4d9451&scene=21#wechat_redirect "记几个edusrc简单挖掘案例")

> 陌笙不太懂安全 2026-01-17 18:16:22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC0cuY8KB87c6bM7icib81gYmJN4FzHRLPC8MgEcmleW5JxDrtjwTlQJpg/640?wx_fmt=jpeg)

本文记录了几个edusrc平台上的简单挖掘案例，涉及弱口令资产收集、若依相关漏洞挖掘、以及存储XSS/SSRF漏洞挖掘。作者通过案例详细介绍了如何发现和利用这些漏洞。在第一个案例中，作者通过发现Drupal系统的弱口令尝试获取敏感信息。在第二个案例中，作者利用若依系统的常见漏洞进行登录，并通过尝试druid和swagger系统路径拼接找到了后台登录页面，进一步获取管理员账户信息。在第三个案例中，作者通过上传存储XSS和SSRF漏洞，展示了如何利用这些漏洞进行攻击。文章中还提到了一些常见的XSS攻击payload和绕过防火墙的方法。

漏洞挖掘

网络安全实践

渗透测试

XSS攻击

SSRF攻击

弱口令攻击

安全工具

安全意识

---

### 0x9 [【APP测试】frida的python库使用](https://mp.weixin.qq.com/s?__biz=Mzk0NzQ0MjMxOA==&mid=2247484477&idx=1&sn=3acba50ebd1b734d6144419b753f4811&scene=21#wechat_redirect "【APP测试】frida的python库使用")

> 蝉SEC 2026-01-17 17:33:17

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyVCFs3agXpeWH8kPqCQK5DRaNssmcqoYCpzIuroiankVmrgwYFzPpSXA/640?wx_fmt=jpeg)

本文详细介绍了使用 Frida 的 Python 库进行动态分析和逆向工程的优势与局限性。首先，文章阐述了使用 Python 库自动化处理和扩展 Frida 调试能力的必要性，以及如何通过 Python 的丰富库支持实现算法转发和 RPC 功能。其次，文章指出了使用 Python 库时缺乏即时修改功能的局限性，并提供了通过文件监听实现动态加载 Frida 脚本的解决方案。接着，文章详细介绍了使用 Frida 的 Python 库附加到目标进程的多种方法，包括通过包名附加、PID 附加、spawn 方式启动进程以及连接非标准端口和多个设备。最后，文章深入探讨了 Frida 与 Python 之间的实时交互机制，包括使用 send 和 console.log 进行消息传递的区别，以及 script.post 和 recv 函数在双向交互中的应用。这些内容为读者提供了使用 Frida 的 Python 库进行高效逆向工程和动态分析的全面指导。

Frida

动态分析

逆向工程

自动化

脚本交互

Python

Android安全

RPC

---

### 0xa [文件上传](https://mp.weixin.qq.com/s?__biz=MzkzODYzNzQ5MQ==&mid=2247486668&idx=1&sn=862ec5b33082de9397e3bd04ba7ee275&scene=21#wechat_redirect "文件上传")

> 哦0吼 2026-01-17 16:05:31

![](https://mmbiz.qpic.cn/mmbiz_jpg/zDpX4yCYbJaOVMicf7XE1jIRpYQkt0jR3jqibGB5WNWdJT1aeDDOwlZibC6QRuI9tPNczBlxy3iam7UZXlTafnsA5g/640?wx_fmt=jpeg)

本文详细分析了文件上传过程中可能存在的安全风险。首先介绍了常见的文件头类型和中间件配置，如Apache的解析规则和.htaccess文件的配置。接着，阐述了文件上传的定义和核心危害，包括上传WebShell、窃取服务器数据等。文章重点分析了绕过前端和后端检测的常见方法，如JavaScript检测绕过、MIME类型检测绕过、文件内容检测绕过等。此外，还介绍了后端文件后缀检测绕过的方法，包括黑名单检测、双写绕过、大小写绕过等。最后，文章讨论了二次渲染检测和条件竞争检测绕过的方法，并提供了Python脚本辅助批量上传和访问文件。

网络安全

文件上传漏洞

Web应用安全

PHP安全

漏洞利用

配置安全

代码审计

---

### 0xb [【CobaltStrike】NeoCS 4.9 终极版（自破解+二开+BUG修复）](https://mp.weixin.qq.com/s?__biz=MzkzNTgzOTg4Mg==&mid=2247487471&idx=2&sn=2e250bcd93f52857ea272384d7babc62&scene=21#wechat_redirect "【CobaltStrike】NeoCS 4.9 终极版（自破解+二开+BUG修复）")

> 星夜AI安全 2026-01-17 15:15:48

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2mH717LQaBIZwWOwcJgqkJC3Xu6aZDMRZiaAOZibBQLjrrfxfhic5OMkKkBI9miabGhWglcVu4rCuEwkg/640?wx_f...