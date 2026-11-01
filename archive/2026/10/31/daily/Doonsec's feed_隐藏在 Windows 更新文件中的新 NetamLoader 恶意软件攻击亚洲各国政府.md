---
title: 隐藏在 Windows 更新文件中的新 NetamLoader 恶意软件攻击亚洲各国政府
url: https://mp.weixin.qq.com/s/gTIU4mhI2_HHNLptdphyZQ
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:20:10.448562
---

# 隐藏在 Windows 更新文件中的新 NetamLoader 恶意软件攻击亚洲各国政府

# 隐藏在 Windows 更新文件中的新 NetamLoader 恶意软件攻击亚洲各国政府

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

卡巴斯基研究人员发现NetamLoader，这是一种基于XAML标记语言构建的.NET加载框架。这似乎是一起针对亚洲政府机构专用的定制版Windows系统的供应链攻击。目前尚无已知的高级持续性威胁（APT）组织与此事件相关联。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyJ06udmfbL5e0vPgb6ga1XAJ2wTH0ibAfe6RXicW0lVrFB4cgcM7MzImeR55iab7EXvsrfVMx9utndXphY0gTIjggkqgeib6TQibjUk/640?wx_fmt=jpeg)

NetamLoader 恶意软件

卡巴斯基安全网络标记了一个使用 AppDomainManager 注入加载任意 .NET 程序集的 .config 文件。该文件位于 C:\Windows\SoftwareDistribution\Download 路径下的一个 CAB 压缩包中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyITBUfNAgH6qLh05ectTJ45Hyegf6hiabw6kRvGYcjqyfTNCr5QkM4cAwJcMGzQXkGIugn2TxnFjIUuicHqMQZfQabFkZ63o2wiaU/640?wx_fmt=png&from=appmsg)

CAB 文件中的大部分内容都是合法的 Patch My PC 组件，且注入的程序集均由微软签名。只有 Resources.resx 文件存在恶意代码。

根据卡巴斯基发布的报告，PatchMyPC-ScriptRunner.exe 会加载一个特制的配置文件，该文件指向 Microsoft.HostIntegration.Connectors。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyLy4tJ7VBDJGSjsCIU1qiasF36u9J2PAkPXKUrXbBChofMT6P9K3M3NmiaLYibJbrpv6zfts7iaUcbcDOnxK0sPBy8icA76Ptyv9TDI/640?wx_fmt=png&from=appmsg)

随后，DataCacheFactoryConfiguration 类读取 fabric.config，该文件会解析 Resources.resx。此文件包含一个 Base64 格式的 BinaryFormatter 对象，它会触发 TypeConfuseDelegate 反序列化攻击，并调用 XamlReader.Parse() 方法执行第一个 XAML 有效载荷。

XAML-1 从主机命令行的 SHA-256 哈希值中提取 AES 密钥并解密 XAML-2。若解密失败，该进程会静默退出。XAML-2 会解包另外两个组件：XAML-2-1 通过将 CAmsiAntimalware::Scan 指针重定向到经过补丁处理的 Console.Clear() 来劫持反恶意软件扫描接口（AMSI），使所有扫描结果均显示为安全；XAML-2-2 则用于部署 .NET 1 加载器及其 JSON 命令与控制（C2）配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyIzwrkts2N6W5BnIt6zRb1T4jjP7nJVSF6P0rIy47Uyz7gtF3kN0P2Vo9icyZy2zZaEZn2AfKYicIibQnA6hvKDquhByO6COs5SN4/640?wx_fmt=png&from=appmsg)

该加载器会清除更新记录、CLR 使用日志以及预取文件。它还会从 CmitUpdateAgent 日志中移除 GetExtendedUpdateInfoHandler 条目，这些条目可能指向政府定制版的 Windows 系统。

随后它利用通过 RPC 创建的 COM 对象在 dllhost.exe 中启动 XAML-3，将有效负载与原始进程树分离以逃避终端检测与响应（EDR）。这与今年出现的其他规避反恶意软件扫描接口（AMSI）的加载程序类似。

最后一个插件在首次联系前会等待20至40分钟，这能绕过沙箱。随后，它会每5至6分钟轮询一次命令与控制服务器（C2），若轮询失败则每22至28小时尝试一次。

流量采用 AES-128-CBC 算法并搭配 HMAC-SHA256 验证，插件接受任意证书。下载的 XAML 在独立的应用程序域中运行。看门狗计时器会在约 28 小时后终止该进程。

C2 是 openaigpt4v[.]com，位于 Cloudflare 背后，IP 地址为 104.18.14[.]219。卡巴斯基在亚洲发现了一名受害者，并推断其关注范围涉及更广泛的政府机构。

防御人员应留意.NET 可执行文件旁出现的意外.config 文件，尤其是在 SoftwareDistribution\Download\Install 目录中。他们还应针对 AMSI 篡改以及通过 COM 启动的 dllhost.exe 发出警报。

又一起更新渠道滥用案例表明，受信任的更新工作流正成为越来越有吸引力的攻击目标。

技术报告：

https://securelist.com/netamloader/121676/

新闻链接：

https://gbhackers.com/netamloader-malware/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. Volt Typhoon 在四次零日漏洞利用活动中使用了隐蔽静默列车网络

被称为“Volt Typhoon”的网络间谍组织，其活动被追溯至一个现已被捣毁的、代号为“Silent Train ”的秘密接入网络，该网络曾被用于零日漏洞利用和获取接入权限。

🔗https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html

2. 被指源自北朝鲜的攻击导致币安63亿美元被盗

币安将一起价值63亿美元的加密货币盗窃案与一台被入侵的DevOps笔记本电脑关联，区块链分析师将此事归咎于朝鲜黑客。

🔗https://securityaffairs.com/202119/cyber-crime/6-3-billion-stolen-from-binance-in-attack-attributed-to-north-korea.html

3. 隐藏在Windows 更新文件中的新 NetamLoader 恶意软件攻击亚洲各国政府

卡巴斯基研究人员发现NetamLoader，这是一种基于XAML标记语言构建的.NET加载框架。这似乎是一起针对亚洲政府机构专用的定制版Windows系统的供应链攻击。目前尚无已知的高级持续性威胁（APT）组织与此事件相关联。

🔗https://gbhackers.com/netamloader-malware/

4. 苹果通知99个国家的受害者其遭遇雇佣军间谍软件感染

苹果已向近100个国家发送了关于雇佣间谍软件感染的新通知，收件人包括记者和纪录片制片人。

🔗https://cyberscoop.com/apple-spyware-notifications-pall-mall-process/

5. 黑客利用Cisco SD-WAN漏洞部署定制版KeyDrift恶意软件

一个新识别的高级持续性威胁（APT）组织，其追踪编号为 UAT-11473，被发现利用思科 Catalyst SD-WAN 控制器中的身份验证绕过漏洞 CVE-2026-20127，部署了一款名为 KeyDrift 的自定义恶意软件框架。

🔗https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/

**一般威胁事件**

General Threat Incidents

1. Cursor上的恶意Claude Code扩展植入了SSH后门

10月29日，Anthropic公司Claude Code的VS Code恶意扩展程序通过Cursor扩展市场分发了约11小时，导致多达5000名开发者暴露在旨在安装持久SSH后门的恶意软件威胁之下。

🔗https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/

2. Yoba恶意软件在合法的OpenAI和Anthropic二进制文件背后隐藏了加密货币挖矿程序

Yoba恶意软件利用伪造的ChatGPT和Claude应用程序，通过已签名的安装程序侧载恶意软件，并部署加密货币挖矿程序。

🔗https://securityaffairs.com/202149/malware/yoba-malware-hides-a-crypto-miner-behind-legitimate-openai-and-anthropic-binaries.html

3. 时尚零售商 Resolve 称黑客窃取了支付卡信息

时尚零售商 Revolve 向投资者警告称，在近期一起网络事件中，网络犯罪分子获取了支付卡号和有效期信息。

🔗https://therecord.media/resolve-fashion-retailer-data-breach-payment-cards

4. PHP2Shell 攻击攻陷25台服务器，渗透美国政府关联网络

网络安全研究人员披露了一起威胁组织策划的人工智能（AI）辅助攻击的细节，该组织利用PHP2Shell漏洞入侵了暴露在外的系统。

🔗https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html

5. 攻击者冒充 AI 机器人持续扫描凭证

一名威胁攻击者潜伏在30多个不同的AI机器人背后，专门查找并窃取泄露的凭证，持续扫描敏感数据却一无所获。

🔗https://www.darkreading.com/cyber-risk/attacker-impersonates-ai-bots-scans-credentials

6. 佛罗里达州警告称，在助学金网站泄露事件中，有 490 万人的社会安全号码遭泄露

佛罗里达州警告称，在助学金网站数据泄露事件中，有 490 万人的社会保障号码遭泄露。

🔗https://therecord.media/florida-warns-5-million-affected-financial-aid-site-breach

7.Polymarket 因加密货币窃取脚本漏洞暂停交易，250 万美元资金已被追踪

预测市场平台 Polymarket 于周四暂停交易，此前黑客入侵第三方服务并分发导致加密货币被盗的 JavaScript 代码，约 250 万美元的资产已追踪至疑似攻击者的钱包。

🔗https://www.bleepingcomputer.com/news/security/polymarket-halts-trading-after-crypto-draining-script-breach-25m-traced/

**漏洞事件**

Vulnerability Incidents

1. Linux内核严重漏洞可使MPTCP服务器遭远程root攻击

Anthropic 的安全研究人员针对一个严重的 Linux 内核漏洞开发了一种利用方法，该漏洞可让未认证的攻击者在运行多路径 TCP（MPTCP）监听器的服务器上以 root 权限远程执行命令。

🔗https://www.bleepingcomputer.com/news/security/critical-linux-kernel-flaw-allows-remote-root-attacks-on-mptcp-servers/

2. TeamViewer 漏洞让攻击者可在 IT 支持人员电脑上执行代码

TeamViewer 存在一个漏洞，当 IT 支持技术人员连接到攻击者控制的设备时，攻击者可在其电脑上执行代码。远程会话建立后，攻击者无需再进行任何点击操作，也无需窃取技术人员的密码。

🔗https://hackread.com/teamviewer-vulnerability-code-it-support-staff-pcs/

3. CVE-2026-111497：Node2Shell/HTTP2Shell 漏洞可能允许远程代码执行

2026年10月21日，Node.js项目披露了CVE-2026-111497漏洞，这是Node.js及其他软件所使用的谷歌Brotli解码器中的一个越界写入漏洞。该漏洞也被称为Node2Shell，近期又被称作HTTP2Shell。CVSS 4.0标准下为9.2分（严重）。

🔗https://www.zscaler.com/blogs/security-research/cve-2026-111497-node2shell-http2shell-vulnerability-may-allow-rce

4. WordPress 7.1.4 修复未认证升级窗口 RCE；发布后检测到利用尝试

该版本修复了22个安全漏洞。最严重的是核心更新流程中存在一个未授权的竞争条件漏洞，该漏洞可能导致远程代码执行。威胁行为者已在积极尝试利用该漏洞。

🔗https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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