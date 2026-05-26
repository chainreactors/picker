---
title: FreePBX 遭六层持久化攻击，电话系统被黑后可能直接产生话费损失
url: https://mp.weixin.qq.com/s/GrE2HtDnIEzeBpolw9Grpg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:08.634681
---

# FreePBX 遭六层持久化攻击，电话系统被黑后可能直接产生话费损失

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDZ9JZjricic1TkvzoszSTwuCdFqDDnEGOcEBWx6BVedW6REFgib0UJM5xc8IDg483Xia6WBVAtyz8fF94sImptrd55k8GF4bn9NxvI/0?wx_fmt=jpeg)

# FreePBX 遭六层持久化攻击，电话系统被黑后可能直接产生话费损失

汇能云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/AyvgaRYHWDYlo6gBEFpicH5GV5Dbt7ptBY4bhokLB7sL9Af6S0PqlXVFaV48bPK0dtHlDzkMPSggSN9JLtpgdvXGPWN845r0QV1OoEfL0oia0/640?wx_fmt=jpeg&from=appmsg)

**5****月****25****日，星期一****，您好！中科汇能与您分享信息安全快讯：**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AyvgaRYHWDa2qMBkubC9798swdeNEp3Ju7dG9ialk0L4GWOSLFhdXTP3ntKckRickAI0Pt4icQrVWfVv9HBIaZhibZYbIuA2EjCepYicia8pX4LFc/640?wx_fmt=gif&from=appmsg)

**01**

**TrapDoor 同时污染 npm、PyPI 和 Crates，开发者电脑正在变成供应链攻击跳板**

TrapDoor 攻击同时打进 npm、PyPI 和 Crates.io 三大开发生态。公开信息显示，该活动投放了 34 个恶意包和 384 个相关版本，伪装成安全扫描、DeFi 检测、Solidity 部署、AI 提示工程等开发工具，专门针对加密货币、Solana、DeFi 和 AI 开发者。它的危险点不只是偷一个钱包或一个 Token，而是把开发者工作站变成企业网络的长期入口。**恶意载荷会收集 SSH 私钥、浏览器数据、AWS 环境变量、Sui、Solana、Aptos 钱包，并通过 systemd、cron、Git hooks 和 shell hooks 保持持久化。**更值得警惕的是，它还会修改 `.cursorrules` 和 `CLAUDE.md`，用隐藏提示词诱导 AI 编程助手执行“看似正常”的凭据外传任务。开发团队应立即排查近期新增依赖，暂停可疑包，轮换 GitHub、AWS、SSH 和钱包密钥。

**02**

**F5 BIG-IP 被打成内网跳板，边界设备不能再当“装上就安全”的黑盒**

F5 BIG-IP 被攻击者利用作为初始入口的案例，非常值得重点关注，Microsoft 研究显示，攻击者从一台互联网暴露的 F5 BIG-IP Virtual Edition 设备进入，随后使用特权账号 SSH 登录 Linux 主机，在内网开展 Nmap 扫描、服务识别和截图探测，再发现并利用内部 Confluence 漏洞，最终向 Windows 身份环境和 Active Directory 扩展。这个链条真正危险的地方在于，攻击者并不是直接打核心业务系统，而是先拿下一个企业默认信任的边界设备**。F5、VPN、WAF、负载均衡和防火墙往往位于公网入口，同时又被内部网络高度信任，一旦版本老旧、日志不足、权限过大，就会成为低可见度跳板。**企业应把边界设备纳入 Tier-0 资产管理，定期核查版本生命周期、SSH 登录来源、设备侧凭据和异常内网扫描行为。

**03**

**Laravel-Lang 被投毒，Composer 自动加载让后门直接跑进开发环境**

Laravel-Lang 生态遭遇的供应链攻击，说明 PHP 项目的依赖风险同样不能低估。攻击者并没有直接向官方仓库提交恶意代码，而是操纵 GitHub tag，把合法版本标签指向恶意 fork，使开发者在通过 Packagist 拉取依赖时加载到被污染版本。恶意文件 `src/helpers.php` 会借助 Composer 的 `autoload.files` 机制自动执行，随后拉取二阶段脚本并窃取敏感配置。攻击目标包括 AWS、GCP、Azure、DigitalOcean 云密钥，Kubernetes 配置，Docker Token，Vault Secret，SSH 私钥，Git 凭据，浏览器密码和加密钱包。**Laravel 项目通常连接数据库、缓存、队列、支付、对象存储等大量业务系统，一旦开发环境被污染，后续就可能演变为生产凭据泄露。**建议检查 `composer.lock`，锁定可信版本，审计出站连接，并对受影响环境进行密钥轮换。

**04**

**art-template 被植入 iOS 水坑攻击，前端依赖也能让网站访客中招**

art-template 这个 npm 包被后门化的事件，和普通开发者想象中的“依赖投毒”不太一样。攻击者不是单纯窃取开发机凭据，而是把恶意脚本注入前端浏览器 bundle，让使用受影响版本的网站变成水坑攻击入口。公开分析显示，受影响版本包括 4.13.3、4.13.5 和 4.13.6，恶意代码会在访客浏览器中执行，并专门识别 Safari on iOS 11.0 到 17.2 的设备；一旦命中，会回传 IP、iOS 版本等信息，再通过多层反机器人检测后拉取最终利用模块。也就是说，**开发者只是不小心升级了一个模板库，最终受害者可能是访问网站的 iPhone 用户。建议前端团队立即审计依赖树，排查 art-template 相关版本，检查打包产物中是否存在异常外部脚本加载。**

**05**

**FreePBX 遭六层持久化攻击，电话系统被黑后可能直接产生话费损失**

FreePBX 被 INJ3CTOR3 攻击的事件很有现实意义，因为它不是为了“炫技”，而是直接用于电信欺诈。攻击者针对暴露在公网的 FreePBX VoIP 系统部署 JOMANGY PHP WebShell，并通过六层持久化机制保持访问。它会设置定时任务、修改 shell profile、复制多个隐藏 crontab、部署进程守护、在 Web 目录多路径放置 WebShell，并在高可用模块里植入 PHP 执行器。更麻烦的是，部分感染系统即使漏洞已打补丁，也会因为持久化残留而反复自我恢复。**FreePBX 连接真实 SIP 中继和运营商线路，一旦被攻击者控制，就可能被用来拨打高费率号码，损失直接体现在电话账单上。确认感染后，不建议只删文件，应从干净基线重建，并更换所有 SIP、Web、数据库和系统账号密码。**

**06**

**cPanel&WHM 任意文件读取漏洞公开，主机面板可能泄露数据库和 SSL 私钥**

奇安信 CERT 通告的 cPanel&WHM CVE-2026-29205 值得主机商和站长重点处理。该漏洞源于 cpdavd 服务附件下载端点存在权限管理错误和路径过滤不足，攻击者可在无需认证的情况下，通过构造特定文件路径参数，以 root 权限读取服务器任意文件。被读取的内容可能包括系统配置文件、数据库凭据、SSL 私钥等高价值数据。**cPanel&WHM 广泛用于虚拟主机、IDC 机房、云服务商和企业自建托管环境，一台主机面板失守，可能影响多个站点、邮箱、数据库和域名配置。**该漏洞 PoC、EXP 和技术细节均已公开，全球关联风险资产规模较大。建议立即升级到官方修复版本，并限制 2079/2080 等 cpdavd 端口暴露。

**07**

**Megalodon 六小时污染 5500 多个 GitHub 仓库，CI/CD 变成凭据收割机**

Megalodon 攻击展示了自动化供应链投毒的速度。**攻击者在不到 6 小时内向 5561 个 GitHub 仓库推送 5718 个恶意提交，伪装成“ci: add build optimization step”“chore: optimize pipeline runtime”等正常 CI 优化。**恶意 GitHub Actions 工作流会请求 `id-token: write` 等高权限，并在运行后收集环境变量、AWS/GCP/Azure 元数据、SSH 私钥、Docker 配置、`.npmrc`、Kubernetes 配置、Vault Token、Terraform 凭据和源码中的 API Key。更麻烦的是，部分受影响项目随后发布了带后门的 npm 版本，把风险从 GitHub 仓库继续带到软件包生态。企业应检查是否出现异常 GitHub Actions 文件、陌生自动化提交和可疑 OIDC 权限，并尽快轮换 CI/CD 密钥。

**08**

**Lenovo 签名驱动可被武器化终止 EDR，BYOVD 攻击仍是终端防护硬伤**

Lenovo BootRepair.sys 驱动被研究人员证明可被滥用来终止安全进程。这类攻击属于典型 BYOVD，也就是“自带有漏洞驱动”攻击。**因为驱动由合法厂商签名，传统安全产品容易默认信任它；但该驱动在设备对象访问控制和 IOCTL 权限检查上存在缺陷，低权限用户可打开驱动句柄，并向指定控制码传入进程 PID，最终让内核调用 `ZwTerminateProcess` 终止任意进程。**研究演示中，甚至可以终止 CrowdStrike Falcon 这类受保护的 EDR 进程。对攻击者来说，这是一种先关防护、再跑 Mimikatz 或横向工具的实用路径。企业应建立易被滥用驱动阻断清单，启用 Microsoft vulnerable driver blocklist，并监控异常驱动加载和安全进程被终止事件。

**09**

**中东电信网络被大量滥用做 C2，可信运营商基础设施也可能藏着攻击流量**

研究人员发现，中东地区多个电信网络和托管服务商正在被攻击者大规模滥用为 C2 基础设施。报告在三个月内识别出超过 1350 个活跃 C2 服务器，分布在 98 家区域基础设施提供商之上，覆盖沙特、阿联酋、土耳其、以色列、伊拉克、伊朗、埃及、叙利亚等 14 个国家。最突出的是，沙特 STC 网络中发现 981 个 C2 服务器，占区域 C2 总量的 72.4%。这些基础设施承载的威胁包括 IoT 僵尸网络、钓鱼工具、勒索软件投递、远控木马和间谍活动。对防守方来说，只盯单个恶意 IP 已经不够，还要从 ASN、托管商、网络段和重复出现的基础设施模式来做威胁监测。

**10**

**WantToCry 通过 SMB 远程加密文件，不落地木马也能完成勒索**

WantToCry 勒索软件的攻击方式很值得企业关注，因为它不一定需要在受害主机上运行恶意程序。攻击者先扫描互联网上暴露的 SMB 服务，通过弱口令或泄露凭据登录后，把文件通过 SMB 会话拉到攻击者基础设施上远程加密，再写回原位置。由于本地没有典型勒索进程，没有明显的恶意可执行文件落地，传统依赖进程和签名检测的安全工具更难发现，受害文件会被改成 `.want\_to\_cry` 扩展名，并留下勒索说明。这个事件再次提醒企业**，SMB 端口绝不能直接暴露公网。建议关闭 139/445 公网访问，强制复杂口令和 MFA，监控异常 SMB 大量读写、外联数据传输和文件扩展名批量变化。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AyvgaRYHWDYQpmVibQHCWYpqQ7H4OgichXXJCkvUQoFAy0Dy4OLmbibB4jZMicGicoLu8dvibxhiag1ibTfnalskcibYVDibxRWHeBora7eowgKDRAMgQ/640?wx_fmt=gif&from=appmsg)

信息来源：人民网 国家计算机网络应急技术处理协调中心 国家信息安全漏洞库 今日头条 360威胁情报中心 中科汇能GT攻防实验室 安全牛 E安全 安全客 NOSEC安全讯息平台 火绒安全 亚信安全 奇安信威胁情报中心 MACFEESy mantec白帽汇安全研究院 安全帮  卡巴斯基 安全内参 安全学习那些事 安全圈 黑客新闻 蚁景网安实验室 IT之家IT资讯 黑客新闻国外 天际友盟

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AyvgaRYHWDa69Bt4VMPDarKv7eerDvWCdbSfXkuPicraN4ZqqnjNp3AwmGa1iapfsoGJictEkIjzRk6grINbT5dn7rH1OH4wrDaljl0a76qFIk/640?wx_fmt=png&from=appmsg)

本文版权归原作者所有，如有侵权请联系我们及时删除

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NSXvotEG4JxfVX9phMzJeKxa6TJkRkiad551HzMtpQVE1WJGiaB2n35mb3ponQiblLvDVPs7yb9iaq1ulcBl8ibpveg/0?wx_fmt=png)

汇能云安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NSXvotEG4JxfVX9phMzJeKxa6TJkRkiad551HzMtpQVE1WJGiaB2n35mb3ponQiblLvDVPs7yb9iaq1ulcBl8ibpveg/0?wx_fmt=png)

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