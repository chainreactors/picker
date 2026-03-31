---
title: OpenClaw（龙虾）安全风险浅析与排查指南
url: https://mp.weixin.qq.com/s/vZZmZZBQQ-ZVeKBuHScMqw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:31:50.557994
---

# OpenClaw（龙虾）安全风险浅析与排查指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IOnTlXyEl263roganrWBmYXCv5Uj79iatuejXgoDK3wLIqEH1FTbxmrZ6RTMbT61jo7j87uXVyZtYZfnGptMqEFZvRcymNuQ7IjK84WeO6hQ/0?wx_fmt=jpeg)

# OpenClaw（龙虾）安全风险浅析与排查指南

中成信息
中成信息

中成信息

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/IOnTlXyEl26lD37bniaB9K4f3CjcPk2wjqN5V9wAUMSe5Ihc1MTib9LFjX51MGUov2DAMQTWlnC7aDdcBxrlZaL3bPtT9f8bBmBtESmiclyIAA/640?wx_fmt=png&from=appmsg)

一、概述

开源 AI 智能体 OpenClaw（代号“小龙虾”）凭借强大的自动化能力快速普及，但其默认高权限、弱安全配置、漏洞频发以及恶意插件风险，也使其逐渐成为内网安全中的高危变量。近期，央视、工信部、行业协会相继发出预警：大量 OpenClaw 实例存在公网暴露现象，漏洞与恶意插件问题突出，一旦在内网中部署不当，极易引发数据泄露、系统失控、横向渗透等严重安全事件。

与普通办公软件不同，OpenClaw不是一个被动执行点击指令的工具，而是具备任务编排和自主执行能力的智能体。为了完成自动化操作，它通常需要访问本地文件、调用命令终端、读取缓存数据，甚至接触 API Key、访问令牌、浏览器会话等敏感信息。也正因为如此，一旦权限失控、配置不当或遭到恶意利用，OpenClaw就可能从效率工具迅速转变为攻击者进入内网的重要跳板。

# 二、风险根源：从架构到配置的 “先天隐患”

默认配置极度脆弱：管理端口默认绑定0.0.0.0，无有效认证或弱口令保护；API密钥、凭证明文存储，易被窃取。

漏洞数量居高不下：累计披露 258 个漏洞，含多个超危、高危漏洞，以远程代码执行、命令注入为主，利用难度极低。

插件生态暗藏风险：插件市场中近一成插件含恶意代码，部分插件加载不可信内容，成为攻击跳板。

智能体行为难管控：易发生提示词注入、权限失控、误操作等问题，且缺乏有效管控手段。

```
"channels": {},"gateway": {  "port": 18789,  "mode": "local",  "bind": "lan",  "controlUi": {    "allowedOrigins": [      "http://localhost:18789",      "http://127.0.0.1:18789"    ]  }}
```

安全配置加固

```
# 关键文件权限设置chmod 600 config.yaml  # 仅所有者可读写chmod 750 plugins/     # 仅所有者可执行，组可读# 禁用危险功能sed -i 's/enable_file_access: true/enable_file_access: false/' config.yaml
```

三、内网暴露的致命危害

## 数据泄露：窃取内网核心数据、代码仓库、账号密码，泄露商业机密与用户隐私。

## 系统被控：攻击者通过漏洞 / 恶意插件获取系统控制权，植入木马、勒索病毒，破坏业务。

## 横向渗透：以 OpenClaw 为跳板，入侵内网核心服务器、数据库，导致全网沦陷。

## 合规与业务风险：违反数据安全法、等保要求，同时因智能体误操作引发业务中断。

# 四、高危场景与多维排查指南

## （一）四大高危场景

终端部署场景：员工私自部署，端口暴露、无认证，沦为内网攻击入口。

开发运维场景：高权限运行 + 端口暴露，漏洞利用后直接接管核心服务器。

办公自动化场景：权限过大，易导致办公数据、客户资料等核心信息泄露。

云服务器场景：默认公网端口开放，公网与内网双向暴露，攻击快速传导。

## （二）排查步骤与要点

1. 资产测绘（摸清底数）

   终端核查：检查配置目录~/.openclaw/、进程openclaw/clawdbot、端口18789。

   网络扫描：Nmap 扫描端口 + HTTP 特征验证，降低误报。

   流量审计：识别 UA、专属 Header、异常外联、反向隧道。
2. 风险判定（快速筛出高风险）

   端口非127.0.0.1监听、无认证 / 弱口令、凭证明文存储、第三方未审核插件、版本存在高危漏洞、高权限运行（root/admin）、配置异常导致invalid link。
3. 深度排查（全面体检）

   配置审计：重点检查端口绑定、认证开启状态、权限配置（需为最小权限）。

   插件排查：仅保留官方签名插件，卸载未知 / 高风险权限插件。

   权限审计：禁用 root / 管理员权限运行，开启操作日志，核查异常指令。

   漏洞修复：升级至最新安全版，安装所有安全补丁。

# 五、闭环加固方案（从边界到终端）

## （一）网络隔离（斩断攻击链路）

## 管理端口默认绑定本地回环地址(127.0.0.1/localhost)，严禁绑定0.0.0.0对公网暴露。

## 确需远程访问仅通过SSH隧道、VPN或反向代理接入，禁止直接开放18789管理端口。

## 配置防火墙与安全组，仅放行可信IP访问必要端口，关闭所有非业务端口； 启用HTTPS加密通信，使用TLS1.2及以上版本证书，杜绝HTTP明文传输。

## 部署至独立VLAN/访客网络，禁止访问内网核心系统，阻断横向渗透路径。

## 禁用自动发现协议，定期核查端口监听状态，配置会话自动超时，防止未授权访问。

### （二）配置加固（从根源消隐患）

敏感凭证绝不明文写入配置文件，统一通过环境变量注入，配置文件权限设为仅属主可读写。

定期轮换 API 密钥与访问令牌，不同平台使用独立密钥，避免单点泄露波及全局。

关闭调试模式与详细日志回显，防止敏感信息在日志中泄露，定期校验配置文件完整性。

加密存储敏感配置，严禁在代码仓库、聊天记录中泄露密钥信息，开启密钥操作审计。

```
#使用环境变量存储export OPENCLAW_API_KEY="your-api-key"
#添加到.gitignoreecho ".env" >> .gitignoreecho "*.key" >> .gitignore
#定期轮换密钥
```

### （三）插件与供应链防护

仅从官方技能市场ClawHub安装插件，拒绝第三方不明插件，禁用自动安装功能。

安装前审查插件权限与代码，规避挖矿、高危命令执行类恶意插件。

定期清理闲置插件，对文件操作、系统命令类高风险插件启用沙箱限制。

订阅官方安全公告，定期深度扫描插件，自定义插件禁止硬编码密钥与高危指令。

### （四）管理与应急（筑牢长效防线）

定期执行轻量与深度安全审计，自动修复隐患，及时更新版本并安装安全补丁。

启用加密操作日志并保留足够周期，记录指令执行、插件安装、配置修改等行为。

制定应急响应预案，发现异常立即断网、保存现场、重置密钥、排查恶意插件。

企业场景需建立部署审批机制，禁止私自部署，定期开展资产排查与渗透测试。

## 六、结语

## OpenClaw的安全核心，在于主动防御、最小权限、持续管控。从部署隔离到网络收敛，从密钥保护到插件审计，每一项措施都能有效降低被攻击风险。无论是个人用户还是企业场景，只有养成定期审计、及时更新、谨慎授权的安全习惯，才能让 “小龙虾” 充分发挥效率价值，同时守护好数字资产与内网安全。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SUlNQ5ia1qWP6CdmAnkTDWcgGM21xo6kqGqMicl0NPpncTGJZWwzicoO5A/640?wx_fmt=png&from=appmsg)

关于我们

漳州中成信息科技有限公司是一家专注于网络安全实战防护的创新型服务提供商。我们深刻理解网络安全的核心在于攻防对抗的持续较量，并以此独特视角为基石，致力于为客户构建动态、主动、智能化的纵深防御体系。区别于传统的被动防御，我们坚信“未知攻，焉知防”。公司汇聚了顶尖的渗透测试专家（红队）、应急处置精英（蓝队）及经验丰富的安全服务工程师，形成了一支具备完整攻防对抗能力的专业团队。我们的渗透测试团队模拟真实攻击者的思维与手段，深入挖掘系统、应用及网络中的深层次漏洞与风险点；应急处置团队则能在安全事件发生时快速响应、精准定位、有效遏制损失并溯源根因；安服工程师团队则致力于将攻防对抗中获得的宝贵经验转化为常态化的安全策略、加固措施与运营流程。

---

**点击名片**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4Siau2HicdH2XxjSEtMnzvqz4cTYibemFyA3TvGH4ZLYABel0MzmHoL8wJQ/640?wx_fmt=png&from=appmsg)

**关注我们**

**扫描官网二维码**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4Siau2HicdH2XxjSEtMnzvqz4cTYibemFyA3TvGH4ZLYABel0MzmHoL8wJQ/640?wx_fmt=png&from=appmsg)

**了解更多**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IOnTlXyEl26GI78T6YncCwKHUKyaGaPfNrv9UJ9HO2UzCY5bafOpicHYkAQ0GM2nN2ib7D75utBpNud4pfcYSb2zojicstr6bVn2jOrIw6ick5s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SXmokj8yGgrQAoBPcFlOgWdWUcj8e5rUKUQVVTQ0ibsppahzAstALX6w/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4ShmKJlD9Q30YqOaiamGgmfOA3libRTCd5cNA1qM7z8RUsAr56ibrAocibiag/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SsibXafic39wibiaEqD6KgYYCSR6Fn5PgAclH1kkky6SglBKoSOTDo4A8wA/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SQoSNk9tODofTCnyfyYcxxotNAKCWTxN1PYUvaZ1cFx99I4iayaiaNzGUl1KmibAgvvVWnCkvAF1w5Q/0?wx_fmt=png)

中成信息

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SQoSNk9tODofTCnyfyYcxxotNAKCWTxN1PYUvaZ1cFx99I4iayaiaNzGUl1KmibAgvvVWnCkvAF1w5Q/0?wx_fmt=png)

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