---
title: 苹果 DarkSword 漏洞工具公开，数亿 iPhone 面临窃密风险
url: https://mp.weixin.qq.com/s/6o24iCVMgFntuACVFOLzcg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:33:53.280063
---

# 苹果 DarkSword 漏洞工具公开，数亿 iPhone 面临窃密风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDYeHmPibYoMMoeZg5icHEKOAQWMKzfCmpESu7MllZfhoAMfMgFm8cD7eYXISWNNz6zS2ghuiby4WAKIwN1ogDJI295suboMicwvsSY/0?wx_fmt=jpeg)

# 苹果 DarkSword 漏洞工具公开，数亿 iPhone 面临窃密风险

汇能云安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDb2YUmIiac2B8xVEibA5ZUZzc73xXTRjLcTmhsH0Y69bXBrAxQQ6YmrcQHx3LtHiaP5TLseoGfd33zYE32KNBInDVn80RXiaYrHvq0/640?wx_fmt=jpeg&from=appmsg)

**3****月****30****日，星期一****，您好！中科汇能与您分享信息安全快讯：**

![](https://mmbiz.qpic.cn/mmbiz_gif/AyvgaRYHWDbwshg0vOwEnQZuUtbmoYicmNI1Zust0r2WS3ZfJUuGKJm7UFXJadtOPmX7BjMElfUDyn5Qg8G4syticfphBSiaJMdg8uaV85rfRg/640?wx_fmt=gif&from=appmsg)

**01**

**Windows 远程桌面服务高危漏洞遭在野利用，政企服务器面临权限劫持风险**

工信部网络安全威胁和漏洞信息共享平台（NVDB）发布预警，Windows 远程桌面服务（RDS）存在CVE-2026-21533高危权限提升漏洞，已被黑客组织用于实际攻击。该漏洞源于服务处理内部配置与注册表项时的权限校验缺陷，**攻击者在拥有普通用户权限或建立远程桌面会话后，可构造恶意请求篡改服务启动配置，无需用户交互即可获取系统最高权限，进而植入后门、窃取数据或横向渗透。**受影响系统覆盖 Windows 10/11 全版本及 Windows Server 2012–2025 等主流服务器系统。微软已发布官方补丁，建议用户立即升级系统或安装对应安全更新，同时限制非必要远程桌面访问、启用多因素认证以降低风险。

**02**

**Claude Chrome 扩展零点击漏洞曝光，300 万用户数据遭劫持**

根据CybersecurityNews 披露，Anthropic 的 Claude Chrome 扩展存在零点击 XSS 漏洞，影响超 300 万用户。**恶意网站可在无交互情况下劫持 AI 助手，窃取 Gmail 令牌、读取 Google Drive 文件、导出聊天记录并发送邮件。**该漏洞已修复，用户需立即更新扩展至最新版。事件凸显 AI 工具安全管控缺失，企业需加强第三方扩展审计。

**03**

**苹果 DarkSword 漏洞工具公开，数亿 iPhone 面临窃密风险**

3 月 23 日，针对 iOS 的高级漏洞利用工具DarkSword完整代码在 GitHub 公开，该工具含2 组漏洞链、6 个 CVE 漏洞（含 3 个零日漏洞），可对iOS 18.4–18.7版本 iPhone 实施零点击静默入侵。**攻击者通过水坑攻击诱导用户访问恶意网页，无需交互即可获取内核权限，窃取短信、通讯录、钥匙串密码、加密货币钱包、iCloud 文件等核心数据，攻击后自动清理痕迹。**据统计，全球约2.7 亿台未升级 iPhone 受威胁，该工具此前被 APT 组织用于国家级间谍活动，代码公开后攻击门槛骤降，建议用户立即升级至iOS 18.7.3 或 iOS 26.3修复漏洞。

**04**

**Apifox 遭 CDN 投毒，数十万开发者终端被植入隐蔽后门**

三月最新报道，API 开发工具 Apifox 公网 SaaS 版桌面客户端（低于 2.8.19）遭供应链投毒。攻击者篡改官方 CDN 动态 JS 文件，利用 Electron 框架未开启沙盒的缺陷，在 Windows/macOS/Linux 平台植入高隐蔽后门。恶意代码可窃取 SSH 私钥、Git 凭证、云厂商密钥、K8s 令牌等核心凭证，实现远程命令执行与数据窃取。此次攻击持续十余天，影响数十万开发者，部分企业已出现代码仓库被劫持、生产环境入侵事件。**安全团队分析显示，攻击者精准瞄准开发工具供应链，利用 CDN 分发恶意代码，隐蔽性强、排查难度大，开发环境安全防护体系面临严峻挑战。**

**05**

**OpenClaw 满分零日漏洞曝光，13 万台 AI 智能体网关泄露风险**

360 安全云团队发现 OpenClaw Gateway WebSocket 无认证越权漏洞，获创始人 Peter 官方确认，CVSS 评分 10.0，为 AI 智能体领域首个满分零日威胁。攻击者无需认证、无需交互，即可通过 WebSocket 绕过权限校验，直接接管网关控制权，窃取核心数据、执行恶意命令或致系统崩溃。**NVDB 数据显示，公网暴露的受影响 OpenClaw 实例超 13.5 万个，其中 13 万台处于无防护状态。该框架是企业级 AI 智能体主流部署方案，境内约 2.3 万个资产暴露，85% 直接面向公网，APT 组织已批量利用其发起攻击，政企内网横向渗透风险极高。**

**06**

**思科 Catalyst SD-WAN 多高危漏洞遭在野利用，企业广域网被远程控制**

工信部网络安全威胁和漏洞信息共享平台（NVDB）发布风险提示，思科 Catalyst SD-WAN 管理软件存在多个高危漏洞，已被用于实际攻击。**该软件是企业级软件定义广域网核心方案，承担广域网部署、管理与优化职能。此次漏洞包含权限提升、任意文件覆盖、认证绕过等类型，攻击者无需复杂操作即可获取系统最高 root 权限，进而窃取企业敏感数据、远程控制系统、破坏网络架构。**受影响范围覆盖多个主流软件系列，大量政企、金融、制造业的广域网边界暴露在攻击之下。漏洞利用难度低、攻击隐蔽性强，一旦被利用将导致企业网络全面失控，业务连续性与数据安全遭受致命打击。

**07**

**APT-C-13 组织针对政企 RDP 服务器长期潜伏窃密**

国家计算机网络应急技术处理协调中心（CNCERT）发布预警，APT-C-13（Sandworm/APT44）组织正针对关键基础设施、国防与政府部门的 RDP 服务器实施隐蔽渗透。该组织一改以往破坏性攻击模式，转向长期情报窃取，通过伪装成 Office 安装镜像的恶意 ISO 文件投递初始载荷，部署 Tambur、Sumbur 等模块化工具。攻击滥用 Windows 合法组件与系统信任机制，借助计划任务、PowerShell、SSH 反向隧道、**Tor 网络及伪造根证书维持权限、隐藏来源，可在目标网络静默驻留数月。常规杀毒与安全监测难以发现，**对政企远程接入、终端防护、异常任务调度及 RDP/SSH 行为监测构成严峻挑战，大量核心业务数据面临被窃取风险。

**08**

**低价 IP-KVM 设备曝 9 个高危漏洞，BIOS 级控制权遭滥用**

奇安信威胁情报中心联合 Eclypsium 研究团队发布预警，四款主流低价 IP-KVM 设备（GL-iNet、Angeet/ Yeeso、Sipeed、JetKVM）存在9 个高危漏洞，含 CVSS 9.8 的未认证文件上传（CVE-2026-32297）与 CVSS 8.8 的命令注入漏洞（CVE-2026-32298），可链式利用实现预认证远程代码执行。此类设备价格低廉（30-100 美元），广泛部署于企业机房、IDC 机房与个人运维场景，工作于操作系统底层。**一旦被控制，攻击者可获得 BIOS 级权限，绕过磁盘加密、修改 BIOS 设置禁用安全启动，注入键盘输入、从外部介质启动，所有操作对主机安全软件完全不可见。**监测数据显示，全球超 1600 台设备直接暴露在公网，FBI 已介入调查相关威胁。该漏洞突破传统网络安全边界，成为新型攻击入口，建议企业将所有 KVM 设备隔离至专用管理 VLAN，通过 VPN 强认证限制访问，及时核查设备固件版本并安装官方补丁。

**09**

**Windows RegPwn 注册表权限提升漏洞在野利用**

英国安全团队 SDsec 披露的 Windows RegPwn 权限提升漏洞已被公开技术细节并在野利用，风险等级高。**该漏洞源于 Windows 无障碍基础架构（atbroker.exe）权限分配缺陷，低权限用户可通过注册表符号链接，将配置路径重定向至系统关键键值，在用户登录或锁屏时，从普通账户直接提升至SYSTEM 最高权限。**攻击隐蔽性极强，无需复杂交互，利用系统合法组件实现权限跨越，常规杀毒与 EDR 难以识别。政企内网中，攻击者可通过该漏洞横向渗透，控制域控制器、核心业务服务器，窃取敏感数据或植入勒索软件。CNCERT 与 NVDB 已同步预警，大量企业与政府单位的 Windows 系统正面临严峻威胁，建议立即通过官方补丁或安全工具修复，强化内网权限隔离与异常行为监测。

**10**

**恶意 VSCode 扩展伪装 AI 助手传播木马，开发者生态遭袭**

FreeBuf 3 月 29 日监测，**一款伪装成 AI 编程助手的恶意 VSCode 扩展 “ClawDBotAgent” 在应用商店传播，表面提供代码补全、调试等功能，实则植入远程控制木马。**攻击者通过伪造官方 API 文档、诱导开发者授权，获取本地项目源码、密钥与环境变量。该扩展已被微软下架，但已被下载超 1.2 万次，波及全球数千开发者。安全团队分析，其采用多层混淆与 C2 隐匿通信，可绕过主流杀毒软件。FreeBuf 提醒，开发者安装扩展前务必核对发布者身份，开启 VSCode 扩展权限审计，定期清理非官方工具。

![](https://mmbiz.qpic.cn/mmbiz_gif/AyvgaRYHWDZKQ2mv0Y97RJM9fOoOfsG3XO4VORTNHb4tg3ticJv0mSHbgyia4ic2SjVBI0ZRNH4avNBIu6Sog7Dl6ssUk1sfXyiaZAEkJKnaII4/640?wx_fmt=gif&from=appmsg)

信息来源：人民网 国家计算机网络应急技术处理协调中心 国家信息安全漏洞库 今日头条 360威胁情报中心 中科汇能GT攻防实验室 安全牛 E安全 安全客 NOSEC安全讯息平台 火绒安全 亚信安全 奇安信威胁情报中心 MACFEESy mantec白帽汇安全研究院 安全帮  卡巴斯基 安全内参 安全学习那些事 安全圈 黑客新闻 蚁景网安实验室 IT之家IT资讯 黑客新闻国外 天际友盟

![图片](https://mmbiz.qpic.cn/mmbiz_png/AyvgaRYHWDZnOnmhqdYkVQzYYCD1npL4AIDjbqtmWZxOUT04iaTXyTQyYM3H7V7JE1tUibibSibheI9gD9vklOjh2FAQw1ibSlYjImXrOibz2ttD4/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

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