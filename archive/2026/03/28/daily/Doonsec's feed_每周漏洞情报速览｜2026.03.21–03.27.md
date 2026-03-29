---
title: 每周漏洞情报速览｜2026.03.21–03.27
url: https://mp.weixin.qq.com/s/jT0f-oyFlRjHBTXHBEeuZA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:38:06.117875
---

# 每周漏洞情报速览｜2026.03.21–03.27

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzz97CZwkyiaiaSK925fDJXot4hwkOjT3l0ZfSoAwOMBrdHFGCYs2ZGPLsbyia7FiaBkbbpjquKf0mpMft52hic57IFpZl614I8IoNLQQ/0?wx_fmt=jpeg)

# 每周漏洞情报速览｜2026.03.21–03.27

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器中沉浸阅读

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

* **Microsoft Authenticator 未认领深度链接账户接管漏洞（CVE-2026-26123）**

Microsoft Authenticator 的 ms-msa:// 深度链接未被应用自身注册，恶意应用可拦截该链接窃取身份令牌，无需任何权限即可完全接管微软账户并绕过 2FA。

https://khaledsec.medium.com/microsoft-authenticators-unclaimed-deep-link-a-full-account-takeover-story-cve-2026-26123-e0409a920a02

* **思科 FMC 认证绕过远程代码执行漏洞（CVE-2026-20079）**

思科 Firepower Management Center 存在认证绕过漏洞，攻击者无需凭据即可绕过身份验证并实现远程代码执行。

https://www.vulncheck.com/blog/cisco-fmc-auth-bypass-cve-2026-20079

* **Rails Active Storage DiskService 路径遍历漏洞（CVE-2026-33195）**

Rails Active Storage 的 DiskService 未验证文件路径是否限定在存储根目录内，攻击者可通过构造恶意 blob key 读取、写入或删除服务器上的任意文件。

https://github.com/advisories/GHSA-9xrj-h377-fr87

* **DigitalOcean Droplet Agent 命令注入预授权 RCE 漏洞（CVE-2026-24516）**

DigitalOcean Droplet Agent 存在命令注入漏洞，攻击者无需认证，通过向端口 22 发送特定 TCP 数据包并注入恶意命令，可以 root 权限执行任意代码。

https://github.com/poxsky/CVE-2026-24516-DigitalOcean-RCE

* **OpenHands Git Diff 处理程序命令注入漏洞（CVE-2026-33718）**

OpenHands 的 get\_git\_diff() 方法将 API 接口的 path 参数未经过滤直接拼接到 shell 命令中，已认证攻击者可在运行时容器内执行任意命令。

https://github.com/OpenHands/OpenHands/security/advisories/GHSA-7h8w-hj9j-8rjw

* **Llama.Cpp 整数溢出堆缓冲区溢出 RCE 漏洞（CVE-2026-27940）**

llama.cpp 在解析 GGUF 文件时 mem\_size 计算存在整数溢出，攻击者通过构造恶意模型文件可触发堆缓冲区溢出，利用 glibc tcache 绕过进一步实现任意代码执行，已有公开 PoC 成功获取 root shell。

https://github.com/ngtuonghung/CVE-2026-27940

* **llama.cpp CVE-2025-53630 修复绕过堆缓冲区溢出漏洞**

针对 CVE-2025-53630 的修复仅对单次累加做溢出检查，未保护最终 mem\_size 计算，攻击者仍可通过构造两个超大张量绕过修复触发整数溢出，最终实现远程代码执行。

https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-3p4r-fq3f-q74v

* **Langflow Agentic 助手认证代码执行漏洞（CVE-2026-33873）**

Langflow 的 Agentic 助手在验证 LLM 生成代码时调用了带有 exec() 的动态执行路径，攻击者可通过影响模型输出实现服务端任意 Python 代码执行，默认开启的 AUTO\_LOGIN 配置可进一步降低利用门槛。

https://github.com/langflow-ai/langflow/security/advisories/GHSA-v8hw-mh8c-jxfc

* **Apple SEPKeyStore 驱动 UAF 条件竞争漏洞（CVE-2026-20687）**

Apple iOS/macOS 的 AppleSEPKeyStore 组件存在条件竞争 UAF 漏洞，攻击者通过多线程高频操作制造竞争窗口，可导致内核内存损坏或系统崩溃。

https://github.com/zeroxjf/CVE-2026-20687-AppleSEPKeyStore-UAF

* **Apple MacOS dyld 缓冲区溢出漏洞（CVE-2026-20700）**

Apple macOS 的 dyld 组件存在缓冲区溢出漏洞，拥有内存写入权限的攻击者可利用该漏洞执行任意代码。

https://github.com/vschko/CaseStudies/tree/main/dyld-bug-jan2026

* **Fortinet FortiClientLinux 符号链接本地权限提升漏洞（CVE-2026-24018）**

Fortinet FortiClientLinux 存在 UNIX 符号链接跟随漏洞，本地非特权用户可利用该漏洞将权限提升至 root。

https://github.com/febin0x10/Fortinet\_FortiClient\_Exploit\_CVE-2026-24018

* **Espintcp ULP 条件竞争 UAF 漏洞（CVE-2026-23239）**

Linux 内核 espintcp ULP 模块在 espintcp\_close() 中使用 cancel\_work\_sync() 而非 disable\_work\_sync()，导致 Worker 在 cancel 后仍可通过 Delayed ACK 路径被重新调度，访问已释放对象形成 UAF，该研究同时提出了"Out-of-Cancel"新漏洞类型。

https://core-jmp.org/2026/03/out-of-cancel-a-new-linux-kernel-race-condition-bug-class/

* **Linux Kernel io\_uring resize 条件竞争空指针解引用漏洞（CVE-2026-23275）**

Linux Kernel io\_uring 执行 resize 操作时会短暂将 ctx->rings 置为 NULL，timerfd hrtimer 回调在此窗口期内仍可访问该空指针，引发内核崩溃（DoS）。

https://naup.mygo.tw/2026/03/23/My-First-CVE-CVE-2026-23275/

* **MantisBT SOAP API MySQL 类型转换身份验证绕过漏洞（CVE-2026-30849）**

MantisBT 在 MySQL 部署下的 SOAP API 存在身份验证绕过漏洞，攻击者将密码参数设置为整数 0，利用 MySQL 类型转换特性即可以 administrator 身份完全控制 SOAP API。

https://hubs.li/Q04846TZ0

* **SiYuan 发布服务目录遍历漏洞（CVE-2026-33670）**

SiYuan 发布服务的 /api/file/readDir 接口未作身份鉴权，攻击者可遍历笔记本下所有文档的目录结构，结合文件读取漏洞可进一步实现任意文档读取。

https://github.com/siyuan-note/siyuan/security/advisories/GHSA-xmw9-6r43-x9ww

* **SiYuan 发布服务任意文档读取漏洞（CVE-2026-33669）**

SiYuan 发布服务的 /api/block/getChildBlocks 接口存在未授权访问缺陷，攻击者可通过文档 ID 读取发布服务下所有被加密或受限文档的完整内容。

https://github.com/siyuan-note/siyuan/security/advisories/GHSA-34xj-66v3-6j83

* **Zephyr RTOS DNS 解析器越界写入漏洞（CVE-2026-1678）**

Zephyr RTOS 的 dns\_unpack\_name() 函数存在越界写入漏洞，攻击者通过发送含多个超长标签的畸形 DNS 数据包可触发堆缓冲区溢出，无需认证即可利用。

https://www.0xkato.xyz/CVE-2026-1678-DNS-Parser-Overflow-in-Zephyr/

* **LangChain load\_prompt 路径遍历云凭证泄露漏洞（CVE-2026-34070）**

langchain-core 中遗留的 load\_prompt 函数存在路径遍历漏洞，攻击者可利用该漏洞读取云服务器上的敏感凭证文件（如 AWS 密钥等）。

https://github.com/Rickidevs/CVE-2026-34070

* **Stackfield 桌面应用路径遍历任意文件写入 RCE 漏洞（CVE-2026-28373）**

Stackfield 桌面应用在处理加密备份时存在路径遍历与任意文件写入漏洞，攻击者通过构造恶意备份文件可将内容写入敏感路径，最终实现远程代码执行。

https://www.rcesecurity.com/2026/03/stackfield-desktop-app-rce-via-path-traversal-and-arbitrary-file-write-cve-2026-28373/

* **雄迈 DVR/NVR Sofia 主机名配置命令注入漏洞（CVE-2026-34005）**

雄迈 DVR/NVR 设备的 Sofia 固件在处理主机名配置时未过滤用户输入，攻击者可通过构造恶意主机名在设备上执行任意系统命令。

https://github.com/uky007/CVE-2026-34005/blob/main/index.md

* **PTC Windchill PDMLink 未授权代码注入漏洞**

PTC Windchill PDMLink 等工业 PLM 产品存在未授权代码注入漏洞，攻击者无需认证即可注入并执行恶意代码，威胁工业制造企业核心系统。

https://www.karma-x.io/blog/post/47/

更多漏洞情报

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz8Eib90Qgicpc9315mVtJaQxDnHL4opIl9x0sVo4LkWXX1ib1APzaXGLyR8Zbo052MvZvbjrwfeEqjfJMMr0PuszV5K6uDBoibr2T0/640?wx_fmt=png&from=appmsg)

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