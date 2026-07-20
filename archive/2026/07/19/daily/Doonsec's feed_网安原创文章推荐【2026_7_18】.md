---
title: 网安原创文章推荐【2026/7/18】
url: https://mp.weixin.qq.com/s/PVhx6WPxGLr7pHRKm6UiZQ
source: Doonsec's feed
date: 2026-07-19
fetch_date: 2026-07-20T05:31:20.474739
---

# 网安原创文章推荐【2026/7/18】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CZMNsicRfJACOpoDm6tC8ACZpjbJ1K2uuibiclpE5EMePF16PJA5kLlySNTnibUB3F5yRNqibEwbRWwEz8LB9mBxzQrjHhhPnxCTAPbjuiawkYM9w/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/18】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-18 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-18

---

### 0x1 [免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485805&idx=1&sn=ffc7f09f5fa8e56f9e86efeb4ef66c00&scene=21#wechat_redirect "免杀更新--Heavenly自动化生成白加黑3.0")

> 安全天书 2026-07-18 19:31:48

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVbOuTjTPd9VJSaklib29IqyPhyaRFPsRno4AtDy5ibtEaIiaJ75jp9TK6LMBCgbZMazaFRYcY1sBkLJQDX2dQ9FYj7EJzwNIFtOM/640?wx_fmt=jpeg)

本文介绍了一种名为Heavenly的自动化生成白加黑免杀工具，该工具旨在简化白加黑免杀流程，支持生成黑DLL以实现免杀。文章强调了工具的使用仅限于安全测试和防御研究，禁止用于非法入侵或攻击他人系统。工具更新内容包括修复BUG和新增反沙箱功能。文章还提到了一个名为“纷传”的圈子，该圈子专注于渗透测试、红蓝对抗、钓鱼手法等研究方向，并分享了多个相关工具和文章。文章列举了多个免杀工具和技巧，如HeavenlyBypassAV、HeavenlyProtectionCS等，以及对抗各种杀软和EDR的技术。最后，文章推荐了往期相关免杀和渗透测试的文章，并邀请读者加入圈子交流学习。

网络安全工具

免杀技术

渗透测试

红蓝对抗

AV绕过

CS插件

Webshell

钓鱼攻击

安全研究

---

### 0x2 [在看 | 周报：上海警方破获非法爬取企业数据案；网警破获侵犯公民个人信息案，13人被采取刑事强制措施](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247656239&idx=1&sn=b62cc264cb6e3bb9e4c59728f7f9a328&scene=21#wechat_redirect "在看 | 周报：上海警方破获非法爬取企业数据案；网警破获侵犯公民个人信息案，13人被采取刑事强制措施")

> 安在 2026-07-18 16:03:39

![](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38nTRvKLpoqoXqeVic62ibaIJvtgiankmicl8nIYognnwqRFj8RPC3e7XouV01BHHd2k9ppdWcbEqlrUw/640?wx_fmt=jpeg)

2026.7.11-2026.7.17

---

### 0x3 [GateIn-基于内核级联的正向C2](https://mp.weixin.qq.com/s?__biz=MzYyMzcxNjMxNA==&mid=2247483780&idx=1&sn=d7f8b88259ddba4dde9164f47f41c406&scene=21#wechat_redirect "GateIn-基于内核级联的正向C2")

> 巡音安全 2026-07-18 15:42:38

![](https://mmbiz.qpic.cn/mmbiz_jpg/kEiaw3nqIkVb5LDdu9q3othibZUIE0lRMDU6GX6dfWz0uPaGNsfCzLBsvAkBNrOThdzSrJcfJstztlpPfEjzsaVGRxuY2cvWV26d12lkow4OU/640?wx_fmt=jpeg)

GateIn是一种基于内核级联的正向C2（Command and Control）模型，旨在提高网络攻击的隐蔽性和稳定性。与传统的反向连接模型不同，GateIn采用正向连接，由操作台按需连接目标，而非Agent主动回连。这种设计使得攻击流量可以挂载在已有的入站端口上，如53/UDP等，从而降低被检测的风险。GateIn支持Windows和Linux平台，通过WinDivert和NFQUEUE等技术实现内核级的流量捕获和命令执行。在Linux平台上，GateIn的Agent主要使用Go语言编写，支持多种正向接入方式，包括UDP、NFQUEUE和QUIC协议。在Windows平台上，GateIn通过Windivert技术实现内核级的UDP和RUDP通信。此外，GateIn还支持级联功能，允许攻击者通过已打通的节点将控制扩展到内网中的其他主机。文章还介绍了GateIn的文件管理功能、rootkit能力、进程隐藏、权限提升以及隐匿文件和目录等高级功能。

网络入侵检测

C2通信

隐蔽通信

内核级联

代理服务

操作系统安全

Rootkit技术

自动化部署

多协议支持

---

### 0x4 [Cloudflare攻击掩护：ClickFix新型攻击链曝光，PowerShell隐藏执行并窃取Windows主机指纹](https://mp.weixin.qq.com/s?__biz=MzYzOTMyNTUzNw==&mid=2247485458&idx=1&sn=f1a7aa4a3e675b526c3009a690838140&scene=21#wechat_redirect "Cloudflare攻击掩护：ClickFix新型攻击链曝光，PowerShell隐藏执行并窃取Windows主机指纹")

> 威胁情报Z分析 2026-07-18 13:23:58

![](https://mmbiz.qpic.cn/mmbiz_jpg/0LGiaGIrzXunIOoobhm8kmiaetARHE9Kk3PssMM2JibAVFy8uP9thbU8hVNyyztk2tFVUl3ia8NKSxD7rVEm6Q9fxmYmLp2403jTCqMvb3RIRCQ/640?wx_fmt=jpeg)

本文揭示了名为ClickFix的新型攻击链，该攻击链利用Cloudflare的托管服务作为掩护。攻击者通过PowerShell脚本隐藏执行，绕过执行策略，收集受害者的计算机名称、用户名、域、Windows操作系统版本、PowerShell版本和管理员权限等信息。这些信息随后被提交到远程的PHP端点，并可能用于后续的攻击阶段。攻击的初始和后续阶段的目标网站地址被标记为IOC，分别是https://d01a43-tuttoprofess[.]sphostserver[.]com和https://d01a43-tuttoprofess[.]sphostserver[.]com/index.php。该攻击手段的发现对网络安全领域具有重要意义，提醒了安全研究者对云服务的利用方式和攻击者可能采取的新策略。

恶意软件攻击

隐蔽攻击

持久化攻击

信息窃取

PowerShell滥用

远程访问木马（RAT）

漏洞利用

云安全威胁

---

### 0x5 [紧急安全预警｜WordPress Bricksforge 爆出未授权提权漏洞(CVE-2026-14956)，攻击者可直接创建管理员账户](https://mp.weixin.qq.com/s?__biz=Mzk2OTAzNjI0OQ==&mid=2247486403&idx=1&sn=6cd848e914b78a789f03a2b3b143501b&scene=21#wechat_redirect "紧急安全预警｜WordPress Bricksforge 爆出未授权提权漏洞(CVE-2026-14956)，攻击者可直接创建管理员账户")

> 杂杂咱谈 2026-07-18 13:02:06

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRHt8VSSTAu2e2v6VTicur291cJibPTPQ0gJdlJy6VD37S6MAVzoibibEjmkWic0JqiaribERLmDNZBgZyD2jh5AtXdf0MVf1hkDiceEvs0/640?wx_fmt=jpeg)

安全研究人员近日披露了WordPress Bricksforge 插件存在一个严重的未授权权限提升漏洞（CVE-2026-14956），CVSS评分高达9.8（Critical）。该漏洞存在于Bricksforge Pro Forms的专业表单用户注册功能中，由于fieldIds参数校验不严，攻击者可以在无需登录的情况下直接创建管理员账户，从而完全控制网站。官方已发布修复版本3.1.8.6，但建议所有使用Bricksforge ≤ 3.1.8.5的站点立即升级至最新版本，以防止漏洞被利用。目前尚未发现大规模在野利用，但由于漏洞利用门槛低，风险不容忽视。受影响的产品包括Bricksforge（WordPress插件），受影响版本为Bricksforge ≤ 3.1.8.5。

WordPress安全漏洞

未授权访问

权限提升

远程攻击

安全更新

漏洞利用

网站安全

插件安全

---

### 0x6 [一个客户端重定向，绕过了SameSite=Strict：我的CSRF赏金之旅](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798840&idx=1&sn=dcd9b92e5b219735e53e060ed1f10d29&scene=21#wechat_redirect "一个客户端重定向，绕过了SameSite=Strict：我的CSRF赏金之旅")

> 升斗安全 2026-07-18 09:43:49

![](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGHBNP81MwIKU2VJtlD3ic6ZmALR1eqtfj4OQ6KdRJ7oPt2X5fFLcFfvTGW1sPl1pL1uVgNW58BHmcdKDdxIg8YEk4DxD0RrI9Ig/640?wx_fmt=jpeg)

【文章说明】目的：本文内容仅为网络安全技术研究与教育目的而创作。红线：严禁将本文知识用于任何未授权的非法活动。

---

### 0x7 [CVE复现 | CVE-2026-9256漏洞复现](https://mp.weixin.qq.com/s?__biz=MzkxNjcyMTc0NQ==&mid=2247485436&idx=1&sn=4d7ac59b874a1a9721eefd524809c581&scene=21#wechat_redirect "CVE复现 | CVE-2026-9256漏洞复现")

> 凌日网络与信息安全团队LapR1skT 2026-07-18 08:00:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oltLnnib9JXQk5DR1MFAiaWKyAbO0QDLT7nJZHqhibLRkqVjTQXYyvEsMLFBI5vab1rhUcEbF7iasdPKTt5LaA75DicvnWpe1j9tt2McK0fBs3zE/640?wx_fmt=jpeg)

本文详细介绍了Nginx中一个名为CVE-2026-9256的高危漏洞。该漏洞存在于ngx\_http\_rewrite\_module模块中，攻击者可以利用特定的rewrite指令配置触发堆缓冲区溢出，从而获取服务器堆地址和libc基址，为实现远程代码执行（RCE）创造条件。该漏洞影响NGINX开源版和商业版的部分版本。文章中提供了漏洞复现的步骤，包括编写Nginx配置文件和docker-compose配置文件，以及如何启动容器和验证漏洞。同时，文章也引用了多个安全博客和阿里云AVD的资料，对漏洞进行了详细的解析。最后，文章强调了使用漏洞复现信息时的免责声明，提醒使用者自行承担可能产生的后果。

漏洞复现

网络安全

Nginx漏洞

缓冲区溢出

远程代码执行

代码审计

Docker

---

### 0x8 [Windows零日漏洞LegacyHive：非管理员如何劫持管理员账户](https://mp.weixin.qq.com/s?__biz=MzkyMjQ5ODk5OA==&mid=2247524130&idx=1&sn=67ae41540f446af72ecbf4d35d494216&scene=21#wechat_redirect "Windows零日漏洞LegacyHive：非管理员如何劫持管理员账户")

> 网空闲话plus 2026-07-18 07:14:24

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d15AmiaRsccTcCYEa9udRUatEGWU8K9w88WERwBc5DkJGq0I1oBFeOqt0aQVAib4jQ2phvLACp5arTbPta1xQ6smcNS8LDuLfs0k/640?wx_fmt=jpeg)

2026年7月，安全研究员NightmareEclipse公开了一个名为LegacyHive的Windows零日漏洞，该漏洞允许攻击者在获得低权限立足点后，通过Windows用户配置文件服务（ProfSvc）挂载并篡改管理员用户的注册表配置单元，从而在管理员登录时实现权限提升和代码执行。由于微软的补丁并未修复此漏洞，所有受支持的Windows版本都面临风险。公开的PoC代码能力受限，但原始漏洞利用无需额外用户凭据，可直接强制加载任意配置单元。LegacyHive利用了Windows对象管理器和注册表配置单元加载流程中的身份模拟和竞态条件缺陷。攻击者可以通过修改注册表项，使恶意代码在管理员登录时执行。微软尚未给出修复时间表，但网络安全专家已发布检测规则，企业可部署实时告警和加固措施。

Windows 漏洞

零日漏洞

权限提升

注册表攻击

本地安全

安全漏洞披露

内核级攻击

应急响应

漏洞利用技术

---

> 本站文章为人工采集，目的是为了方便更好的提供免费聚合服务，如有侵权请告知。具体请在留言告知，我们将清除对此公众号的监控，并清空相关文章。所有内容，均摘自于互联网，不得以任何方式将其用于商业目的。由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，本站以及文章作者不承担任何责任。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

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