---
title: 网安原创文章推荐【2026/3/13】
url: https://mp.weixin.qq.com/s/R688kQWJ0kS9ALA_oT0PsA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:33:41.563092
---

# 网安原创文章推荐【2026/3/13】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CZMNsicRfJAC5npZnMfL27W94zXAJMl3bVMfKBSr2icWMBkjSWTYHO72LFUJnhXONdP3picvug3sWicCtYr4tJhYxQqNrYcC4dBQeCzlwa9oG7Q/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/3/13】

AJay13
AJay13

洞见网安

![]()

在小说阅读器中沉浸阅读

# 2026-03-13 微信公众号精选安全技术文章总览

> 洞见网安 2026-03-13

---

### 0x1 [JoySafeter的加固版OpenClaw来了！](https://mp.weixin.qq.com/s?__biz=MjM5OTk2MTMxOQ==&mid=2727850653&idx=1&sn=bc8d609d7dbc9c50455a0188b8c3126f&scene=21#wechat_redirect "JoySafeter的加固版OpenClaw来了！")

> 京东安全应急响应中心 2026-03-13 22:38:32

![](https://mmbiz.qpic.cn/mmbiz_jpg/waPVkHfLDdgXRPsJnDRKcNodPRNewhDMFK1y0r1iboaurYGzn04v4DTgaHtEztlYmcjVIFlNhfRdaYc0t11rX6FgCovBY2g9cPzyVqkTxxia4/640?wx_fmt=jpeg)

OpenClaw作为一款热门的AI Agent框架，因其强大的自主执行能力受到关注，但也存在高权限和弱默认安全的问题，导致个人或企业在使用时面临安全风险。京东开源的JoySafeter通过加固版OpenClaw和构建安全检测、skills安全审计等能力，为AI Agent的安全使用提供了解决方案。OpenClaw的主要风险包括威胁类型如提示词注入、供应链投毒、上下文溢出、劫持、数据外传和权限持久化等，这些风险可能导致数据泄露、系统损毁和业务中断。传统安全工具难以应对这些内部欺骗和外部逃逸的攻击。OpenClaw的安全模型基于操作者信任自己，虽然内置了全面的安全机制，但默认未开启，需要主动加固。JoySafeter通过将安全策略写成Markdown，为OpenClaw植入安全基因，并构建了配置硬管控、认知层防护和运行时审计的纵深防御体系。JoySafeter还提供了安全检测报告和Skill安全审计报告，以及定期任务进行安全审计检查，帮助用户重塑OpenClaw的安全，实现安心使用。

---

### 0x2 [Chrome 零日漏洞已被恶意攻击者积极利用，用于执行恶意代码](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247485476&idx=1&sn=2822e2a80db224cc60ce0d1bedd73f01&scene=21#wechat_redirect "Chrome 零日漏洞已被恶意攻击者积极利用，用于执行恶意代码")

> 安全圈的那点事儿 2026-03-13 19:01:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PhMCkN6DyTaJ8SEzotKiaZUcCibMt7ibmNdOqxmicN2xoDVLnljajIZuHdn6Gxr8NZdU7edibUzJQ49QWhwhk5Anee2ZKvCeZCMpbA/640?wx_fmt=jpeg)

谷歌发布紧急安全更新，修复Chrome浏览器的两个严重零日漏洞CVE-2026-3909和CVE-2026-3910。这两个漏洞均被归类为高危，攻击者已证实正在利用它们执行恶意代码。CVE-2026-3909是Skia库中的越界写入漏洞，可能导致浏览器崩溃或执行恶意代码。CVE-2026-3910是V8引擎中的不恰当实现，可能允许攻击者绕过安全沙箱。谷歌警告称，攻击者通过恶意网站即可触发这些漏洞，无需用户交互。建议用户立即更新浏览器以保护系统安全。

浏览器安全

零日漏洞

恶意代码执行

安全更新

内存安全

JavaScript引擎安全

漏洞利用

网络安全威胁

---

### 0x3 [【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797965&idx=1&sn=7f50945921f1eaa1d50f3f659d81e0ff&scene=21#wechat_redirect "【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战")

> 升斗安全 2026-03-13 17:55:24

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGHDqGsiaz6DtUOueGhN0VCL2UH2wSnLqIa5ia42SopCn89wHVo6UmCVx9Fm5V360rkBFs05QOfqcDThibBHtwSoicqcMhF7ibgwicxvI/640?wx_fmt=jpeg)

本文旨在探讨网络安全领域中的文件上传漏洞，这是一种常见的服务器端漏洞。文章首先强调了安全研究的合法性和用户责任，并简要回顾了前文关于SSRF漏洞的内容。接着，详细解释了文件上传漏洞的定义、产生原因以及潜在的危害。文章指出，由于文件上传功能中可能存在的验证措施缺陷或绕过，攻击者可能上传具有危险性的文件，包括能执行远程代码的服务器端脚本文件。此外，文章讨论了文件上传漏洞可能导致的安全风险，如远程代码执行和Web Shell的部署，后者允许攻击者远程执行系统命令，从而获得对服务器的完全控制。文章最后预告了后续将结合理论分享一个实战案例，并鼓励读者关注和支持。

网络安全漏洞

Web应用安全

文件上传漏洞

攻击与防御

代码执行

渗透测试

安全开发

---

### 0x4 [MCPHub 高危漏洞实录：零凭证访问与授权后命令执行](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247557923&idx=1&sn=79f8d411159ec91e1ad6852f27db3f7b&scene=21#wechat_redirect "MCPHub 高危漏洞实录：零凭证访问与授权后命令执行")

> 蚁景网络安全 2026-03-13 17:35:51

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkiaupiaWQPuM1OKJTYTrlD3orlVcc4KJXT5UzCWvkGYAAJ2DAr8UgekjvnvAwzgITXrYkgHbDMwAfXsrsgzUSzrNiczo21tMv6FyM/640?wx_fmt=jpeg)

本文详细分析了 MCPHub（一个 MCP 服务器的统一管理中间层）中存在的两个主要漏洞，并说明了它们之间没有依赖关系，仅因出自同一项目而被放在同一篇文章中讨论。第一个漏洞是身份认证绕过漏洞，攻击者无需任何凭证，通过修改 URL 中的用户名即可冒充该用户，获取其完整权限，包括调用其配置的所有 MCP 工具。此漏洞源于系统直接信任 URL 参数中的用户名，缺乏身份验证和权限验证。第二个漏洞是授权命令执行漏洞，攻击者需先登录获取合法的 admin token，然后通过添加配置了恶意命令的服务器，执行任意命令。此漏洞源于对命令和参数字段缺乏验证，直接将用户输入传递给子进程执行。文章还描述了攻击步骤和漏洞危害，并指出两个漏洞的修复情况，强调仅供安全研究与学习参考。

身份认证绕过

SSE 安全漏洞

逻辑错误

命令执行

输入验证不足

不安全配置管理

会话管理缺陷

---

### 0x5 [Windows内核攻防—利用RTCore64驱动绕过Windows签名校验](https://mp.weixin.qq.com/s?__biz=Mzk2NDUzMjgxOA==&mid=2247484846&idx=1&sn=0797059ee994580391d776f242e0ee07&scene=21#wechat_redirect "Windows内核攻防—利用RTCore64驱动绕过Windows签名校验")

> Heri76安全 2026-03-13 16:59:28

![](https://mmbiz.qpic.cn/mmbiz_jpg/pgh9MpJCA6iaFbbVbHibZhIwgMxPibX0Z3WRL8VPpQQicF4yxIs0b8M2eicBqibPyBibwLI68Co27ib5BiakFzYgqd4vJ9yh0fCVibc3QlKkBic3IxdQok/640?wx_fmt=jpeg)

本文详细介绍了如何通过修改 Windows 内核中的 g\_CiOptions 变量来绕过驱动签名验证机制（DSE）。文章首先解释了 DSE 机制及其在 Windows 加载驱动时的作用，指出 g\_CiOptions 是控制 DSE 功能的关键变量。由于 g\_CiOptions 未导出，文章提出通过特征码扫描 CI.dll 来定位其位置。作者使用 IDA Pro 分析 CI.dll，确定了 g\_CiOptions 的特征码，并给出了适用于 Windows 10 和 Windows 11 的特征码。接着，文章介绍了利用 NtQuerySystemInformation 函数枚举内核模块，结合特征码扫描用户态内存来定位 g\_CiOptions 内核地址的方法。为修改 g\_CiOptions，文章建议使用 RTCore64.sys 驱动，该驱动存在可读可写的漏洞且未被微软拉黑，可通过它进入内核修改 g\_CiOptions 的值为 0，从而允许加载无签名驱动。最后，作者通过实际测试验证了该方法的有效性，并展示了加载无签名驱动并执行内核操作（如结束进程）的过程，同时指出天擎 EDR 在未配置相关策略时未产生告警。

---

### 0x6 [常见网络安全事件通报类型与应急处置](https://mp.weixin.qq.com/s?__biz=MzkwNjI1MTkyMQ==&mid=2247484510&idx=1&sn=aa15a00ed1641c081c273a8531ee0da9&scene=21#wechat_redirect "常见网络安全事件通报类型与应急处置")

> 墨守安全 2026-03-13 16:55:41

![](https://mmbiz.qpic.cn/mmbiz_jpg/F9ccIXSyq6SQfg9lial7rjVOniaO9icsZw6LDPsQeP73Gu5mrviaO98MKfGUVgIdIV3BNGheYg7f1hj3FXkjfZFAmgrr5Gy4H9U73wCzVdQHGeA/640?wx_fmt=jpeg)

文章详细分析了常见的网络安全事件通报类型及其应急处置方法。文章首先介绍了勒索病毒、挖矿病毒、银狐木马和网页内嵌恶意代码等常见网络安全事件的类型和特征。对于勒索病毒，文章强调了备份和前期巡检的重要性，并提供了详细的处置方法，包括断网、结束恶意进程、检查系统漏洞和弱口令等。挖矿病毒的处置方法与勒索病毒类似，重点在于暂停危害、找出并结束高资源占用进程，并检查异常网络连接。银狐木马的处置与前述方法基本一致，重点在于断网、结束恶意进程，并加强人员网络安全意识。网页内嵌恶意代码的处置则包括深度检测、清除恶意代码和修补漏洞等步骤。文章还介绍了“两高一弱”问题，即高危漏洞、高危端口和弱口令，并提供了相应的处理方法，包括漏洞扫描、端口管理和强密码策略等。最后，文章强调了网络安全事件应急响应的重要性，并提出了构建“技术+管理+运营”三位一体的网络安全防护体系的建议。

---

### 0x7 [下一代凭证窃取与“无文件”横向移动技术研究](https://mp.weixin.qq.com/s?__biz=MzkzNDQ0MDcxMw==&mid=2247488549&idx=1&sn=c490bfd5827a2922447fdda726cf50d0&scene=21#wechat_redirect "下一代凭证窃取与“无文件”横向移动技术研究")

> 白帽子社区团队 2026-03-13 16:44:59

![](https://mmbiz.qpic.cn/mmbiz_jpg/DupJg3UCeKKDX6E54G7sKKTaBQCYG5hQcibOIbrdHS2QP3DZqY0A00tuYapKFg8icdZDrL6hbibHTmETwYrCIguCqxn6sAHoxKZOOBFEsn5LQ8/640?wx_fmt=jpeg)

本文深入探讨了多种突破 LSASS 保护、实现凭证窃取和横向移动的技术路径。首先分析了利用内核驱动漏洞（如 CVE-2023-21716 和 CVE-2023-21551）绕过 PPL 保护读取 LSASS 内存的方法，通过构造畸形数据触发堆溢出或类型混淆漏洞，在内核态直接读取敏感数据结构。其次，介绍了合法系统工具（如 PowerShell、WMI、certutil、regsvr32）的非常规组合攻击链，利用这些工具的合法性和协议特性，实现无文件、无写盘的横向移动和凭证提取。此外，还详细阐述了通过内核调试接口（Debug Port）间接读取 LSASS 内存的技术实现，包括环境配置、内存读取和凭证分析。文章进一步探讨了 SMB 协议中的无文件代码执行技术，利用 CreateContexts 和 Named Pipes 注入恶意逻辑，以及 WinRM 协议的反向隧道和远程命令注入机制。最后，分析了 Kerberos 票据传递与伪造的高级变种，包括影子票据和分布式黄金票据技术，以及 DPAPI 与证书存储的离线破解方法，揭示了未来凭证窃取与横向移动技术的发展趋势，强调防御者需从静态规则转向行为建模和异常模式识别，并建立跨协议联动的威胁情报体系。

内核漏洞利用
无文件攻击
凭证窃取
红队渗透
SMB利用
WinRM利用
DCOM利用
WMI利用
Kerberos攻击
DPAPI破解
证书破解
EFS破解
BitLocker破解
隐蔽信道
横向移动
高级持续性威胁

---

### 0x8 [John the Ripper（开膛手约翰） 哈希破解工具的实操应用](https://mp.weixin.qq.com/s?__biz=MzkzMjcxOTk4Mg==&mid=2247486892&idx=1&sn=2781f6cd274109e728ae4a302564b90f&scene=21#wechat_redirect "John the Ripper（开膛手约翰） 哈希破解工具的实操应用")

> 网络安全直通车 2026-03-13 15:57:31

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiase17hRoCyTTcNQ7MYe6kS6nUBFxpMib5X9UdvDICoYNI6lQP7jl67nib4Jhia9DMVlaicmibe1kOqcY19VDndlW61jxKuRjOxcn9l8/640?wx_fmt=jpeg)

本文详细介绍了John the Ripper（开膛手约翰）哈希破解工具的实操应用。文章首先介绍了John the Ripper的核心功能和辅助工具，如hash-id.py和unshadow，以及核心字典rockyou.txt的使用。接着，文章详细讲解了John the Ripper的三种核心破解模式：自动模式、指定格式模式和Single Crack Mode，并分别介绍了它们的应用场景和操作命令。此外，文章还涵盖了不同场景下的破解流程，包括基础哈希破解、Linux /etc/shadow文件破解、压缩文件和SSH文件破解等。最后，文章介绍了如何在John the Ripper中编写自定义破解规则，并提供了具体的规则语法和示例。

哈希破解

网络安全工具

密码学

Linux安全

字典攻击

系统安全

实战指南

---

### 0x9 [【漏洞复现】Weblogic 反序列化漏洞(CVE-2020-2555)](https://mp.weixin.qq.com/s?__biz=Mzg4ODYyMDMzOA==&mid=2247488812&idx=1&sn=bc8171f784bc7857beba50605da151bb&scene=21#wechat_redirect "【漏洞复现】Weblogic 反序列化漏洞(CVE-2020-2555)")

> NS Demon团队 2026-03-13 15:46:45

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JlWRciccfVpyE8FAXt0pDQYwk8m6JhTekUlWXG6Xd1mpZU5mKB7LPNibSibic2044jMondaXakgT6Nw1GprI8sNia4w/640?wx_fmt=jpeg)

该文章详细描述了Oracle Coherence的CVE-2020-2555漏洞，该漏洞允许未经身份验证的攻击者通过构造T3网络协议请求进行攻击，成功利用该漏洞可实现在目标主机上执行任意代码。文章首先介绍了受影响的产品版本，包括Oracle Coherence 3.7.1.17、Oracle Coherence 12.1.3.0.0、Oracle Coherence 12.2.1.3.0和Oracle Coherence 12.2.1.4.0。接着，文章提供了漏洞搭建的步骤，使用vulfocus进行复现，并指导读者如何使用网上的exp进行漏洞验证。文章还包含了详细的漏洞复现代码，包括T3握手过程、构建T3请求对象、发送恶意对象数据等功能。最后，文章通过实际案例展示了如何利用该漏洞在dnslog网站发现记录，并成功反弹shell，寻找flag。整个文章对于理解和使用该漏洞提供了详细的指导。

漏洞利用

漏洞分析

Coherence

未授权访问

代码执行

命令执行

网络协议

---

### 0xa [新型免杀加载器来了！过火绒、360核晶、Defender一键搞定](https://mp.weixin.qq.com/s?__biz=MzkzNTgzOTg4Mg==&mid=2247487930&idx=1&sn=c5421dc982232024ea9fc90ea868f0dd&scene=21#wechat_redirect "新型免杀加载器来了！过火绒、3...