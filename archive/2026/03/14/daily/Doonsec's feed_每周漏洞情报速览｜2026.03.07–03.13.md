---
title: 每周漏洞情报速览｜2026.03.07–03.13
url: https://mp.weixin.qq.com/s/jBLcHxq4BnzNUUXnMydYBg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:29.448140
---

# 每周漏洞情报速览｜2026.03.07–03.13

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzzicdMqUOfBdfNEB0QjekwHrfiay17WEiad7aLde3qJ1wBiaIPqvGaRpZY8BiaRRSBhLxSdicoMfZcQEm53T4EshjEacrR6hZMLJVUp9o/0?wx_fmt=jpeg)

# 每周漏洞情报速览｜2026.03.07–03.13

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器中沉浸阅读

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

* **Firefox WebAssembly JIT 误编译导致类型混淆漏洞（CVE-2026-2796）**

Firefox 浏览器的 Wasm 模块在处理 call.bind 包装函数时存在优化缺陷，可导致跨语言边界的类型混淆，进而实现完整的浏览器沙箱内代码执行。

https://red.anthropic.com/2026/exploit/

* **TP-Link Tapo C260 摄像头多个高危漏洞（CVE-2026-0651、CVE-2026-0652、CVE-2026-0653）**

该型号摄像头存在本地文件读取、远程代码执行及权限提升漏洞，攻击者可利用未加密的本地网络协议绕过身份验证并接管设备。

https://spaceraccoon.dev/getting-shell-tapo-c260-webcam/

* **思源笔记 /export 接口路径穿越漏洞（CVE-2026-30869）**

思源笔记的导出接口在处理解密路径时信任用户输入，攻击者可通过双重 URL 编码绕过安全过滤，读取服务器上的任意敏感文件。

https://github.com/siyuan-note/siyuan/security/advisories/GHSA-2h2p-mvfx-868w

* **Tencent WeKnora SQL 注入验证绕过漏洞（GHSA-8w32-6mrw-q5wv）**

WeKnora 数据库查询工具的 SQL 校验框架未能递归处理 PostgreSQL 的数组和行表达式，导致攻击者可走特殊节点绕过防注入检测实现 RCE。

https://github.com/Tencent/WeKnora/security/advisories/GHSA-8w32-6mrw-q5wv

* **Eclipse Jetty Web 服务器 Inflater 内存泄漏漏洞（CVE-2026-1605）**

Jetty 的 GzipHandler 在处理解析失败的 gzip 请求时未能正确清理 Inflater 对象，攻击者可通过持续构造异常请求耗尽服务器内存。

https://hcs-team.com/blog/cve-2026-1605/

* **OneUpTime 探针组件 Node.js 沙箱逃逸 RCE 漏洞（GHSA-h343-gg57-2q67）**

OneUpTime 允许用户运行 Playwright 代码，但由于使用不安全的 vm 模块且未进行 AST 过滤，攻击者可通过原型链逃逸实现容器内的命令执行。

https://github.com/advisories/GHSA-h343-gg57-2q67

* **Qwik 框架服务器端函数反序列化 RCE 漏洞（CVE-2026-27971）**

QwikCity 中间件在处理 server$ 函数时未对反序列化过程进行严格校验，在 Bun 等环境中可被利用来执行任意系统级代码。

https://www.sebsrt.xyz/blog/a-qwik-rce/

* **Cloudflare Pingora OSS 请求走私漏洞**

Pingora 的 HTTP/1 协议栈在解析非 RFC 合规的请求体时存在歧义，当作为 ingress 代理保护多个后端时，可能由于解析差异导致请求走私。

https://blog.cloudflare.com/pingora-oss-smuggling-vulnerabilities/

* **Azure Arc Windows 代理本地权限提升漏洞（CVE-2026-26117）**

Windows Azure Arc 代理栈中存在一系列逻辑漏洞，低权限用户可利用中间人攻击干扰服务通信，从而获取 SYSTEM 权限或接管云端身份。

https://cymulate.com/blog/cve-2026-26117-azure-arc-windows-lpe-cloud-identity-takeover/

* **simple-git 忽略大小写导致远程代码执行漏洞（CVE-2026-28292）**

simple-git 在处理 ext:: 协议时缺少 /i 标志，导致攻击者可通过改变字符大小写绕过之前的安全补丁，在宿主机上执行任意系统命令。

https://www.codeant.ai/security-research/security-research-simple-git-remote-code-execution-cve-2026-28292

* **OneUpTime 身份验证绕过导致跨租户数据暴露漏洞（GHSA-r5v6-2599-9g3m）**

由于系统信任客户端控制的 is-multi-tenant-query 头部，攻击者可绕过授权检查访问其他租户的项目数据并获取重置密码的令牌。

https://github.com/advisories/GHSA-r5v6-2599-9g3m

* **Hitachi Vantara Pentaho 报表设计器远程代码执行漏洞（CVE-2025-11158）**

Pentaho 平台允许业务用户在报表文件中嵌入恶意的 Groovy 脚本，服务器在解析上传的报表时将以系统权限执行这些脚本。

https://www.ox.security/blog/cve-2025-11158

* **"Zombie Zip" 压缩包检测绕过漏洞（CVE-2026-0866）**

通过构造存储方法与实际压缩方法不一致的 ZIP 文件，攻击者可以使大多数安全扫描引擎因无法正确解压而漏掉其中的恶意负载。

https://isc.sans.edu/diary/32786

* **Cisco Catalyst SD-WAN 预身份验证绕过漏洞（CVE-2026-20127）**

Cisco SD-WAN 控制器和管理器中存在身份验证绕过缺陷，攻击者可利用已在野利用的漏洞获得管理权限并执行后续攻击链。

https://attackerkb.com/topics/bP3FMvHe7z/cve-2026-20127/rapid7-analysis

* **FortiClient EMS 预身份验证 SQL 注入漏洞（CVE-2026-21643）**

FortiClient EMS 7.4.4 版本在处理多租户 Site HTTP 头部时存在输入过滤不当，未登录攻击者可通过构造恶意的 Site 头部执行任意 SQL 命令。

https://bishopfox.com/blog/cve-2026-21643-pre-authentication-sql-injection-in-forticlient-ems-7-4-4

* **Apache Airflow HTTP Provider 远程代码执行漏洞（CVE-2025-69219）**

具有数据库访问权限的用户可以通过构造恶意的数据库条目，触发 Triggerer 组件上的代码执行，实现与 DAG 作者相同的权限。

https://github.com/sak110/CVE-2025-69219/blob/main/poc.py

* **Argo Workflows 敏感信息泄露漏洞（CVE-2026-28229）**

Argo Workflows 在处理工作流模板时未能正确验证 Authorization 令牌，任何客户端通过发送特定伪造令牌即可获取包含保密信息的内容。

https://github.com/advisories/GHSA-56px-hm34-xqj5

* **HuggingFace smolagents SSRF 漏洞（CVE-2026-2654）**

当 smolagents 的本地执行器配置了 network-capable 模块时，缺少对 URL 的有效过滤和出口限制，可被利用来探测内网或窃取云凭据。

https://www.raxe.ai/labs/advisories/RAXE-2026-031

* **Windows 快捷方式（.lnk）文件处理逻辑漏洞（CVE-2026-25185）**

Windows 在处理特定结构的快捷方式文件时存在解析缺陷，通过精心构造的 .lnk 文件可能导致凭证泄露或拒绝服务。

https://trustedsec.com/blog/lnkmemaybe-a-review-of-cve-2026-25185

* **Chrome 紧急安全更新修复两处在野利用高危漏洞（CVE-2026-3909、CVE-2026-3910）**

Google 修复了两个已在野利用的 Chrome 漏洞，分别涉及 Skia 2D 图形库和 V8 引擎逻辑。

https://chromereleases.googleblog.com/

* **Google Gemini 平台交互逻辑代码执行漏洞**

安全研究员发现 Google Gemini 存在一处潜在的代码执行路径，可能允许攻击者利用特定的交互逻辑在受限环境内执行代码。

https://medium.com/@dhiraj\_mishra/code-execution-in-google-gemini-4e5909ec167d

更多漏洞情报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9ib2OpcMWwnlYboiasGBg5zicmic03pX3WPCaHmrl0lMt4RXHm8wEgZCg8W5ug8Ria9NO6btdejeTbAUic8xicREK0WVicPcFWSwFkOm4/640?wx_fmt=png&from=appmsg)

建议您订阅360数字安全-漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。

邮箱：360VRI@360.cn

网址：https://vi.loudongyun.360.net

**“洞”悉网络威胁，守护数字安全**

**关于我们**

360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

360漏洞研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

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