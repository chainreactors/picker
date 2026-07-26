---
title: 【热点安全风险】7月25日 | Clop 勒索团伙正针对互联网暴露的 PTC Windchill 和 FlexPLM 实例开展数据窃取勒索活动
url: https://mp.weixin.qq.com/s/QfMB0oA8mvJga20skcbLUA
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:23:29.036108
---

# 【热点安全风险】7月25日 | Clop 勒索团伙正针对互联网暴露的 PTC Windchill 和 FlexPLM 实例开展数据窃取勒索活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaPgUxMqaSAiaTRGt3BqaictgobcEa8kkbbcA6BvO95M0CMyEEjfEtLM5fnKjia4Y25f4cgXsXY9CnG0Q5VohaAEUFtOu80f8UcTwn44aPIVhFo/0?wx_fmt=jpeg)

# 【热点安全风险】7月25日 | Clop 勒索团伙正针对互联网暴露的 PTC Windchill 和 FlexPLM 实例开展数据窃取勒索活动

华顺信安威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**PART.****0****1**

风险汇总‍‍‍

## 风险一：Clop 针对 PTC Windchill / FlexPLM 发起数据窃取勒索，PLM系统需优先排查

公开报道显示，Clop 勒索团伙正针对互联网暴露的 PTC Windchill 和 FlexPLM 实例开展数据窃取勒索活动，相关攻击利用 CVE-2026-12569。PLM 系统常承载产品设计、制造、供应链与客户资料，一旦被入侵，可能同时造成核心数据外泄、业务勒索和供应链协作中断。

### 建议排查

1. 盘点所有 PTC Windchill、FlexPLM 实例及其公网暴露情况。
2. 核查是否已安装 PTC 6月、7月发布的安全补丁。
3. 检查 Web 目录、访问日志、异常 JSP 文件和大体量数据下载行为。
4. 排查是否收到 Clop 相关勒索邮件或异常数据外传告警。

### 加固建议

1. 立即按 PTC 官方公告安装修复补丁。
2. 将 Windchill、FlexPLM 置于 VPN、零信任网关或可信访问入口之后。
3. 对疑似被入侵系统执行隔离、取证、WebShell 清理和凭据轮换。
4. 将 PLM 系统纳入核心业务数据保护和勒索攻击演练范围。

参考来源：

https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/

## 风险二：Zimbra 邮件系统漏洞被用于窃取邮件、凭据与2FA恢复码

NSA、CISA 及多国伙伴披露，Laundry Bear / Void Blizzard 等攻击者利用 Zimbra Collaboration Suite 漏洞 CVE-2025-66376 发起邮件窃密活动。相关攻击在用户打开或预览恶意邮件时即可触发，可能窃取近期开启会话中的邮件、联系人、浏览器保存凭据、2FA 恢复码和应用专用密码。

### 建议排查

1. 盘点 Zimbra Collaboration Suite 版本，确认是否低于官方修复版本。
2. 检查近 90 天异常邮件导出、异常 IMAP/POP3/SMTP 登录和应用专用密码创建记录。
3. 排查 Webmail 异常脚本执行、DNS 外传、可疑邮件预览事件。
4. 对政府、科研、能源、教育、制造和高管邮箱执行专项复核。

### 加固建议

1. 升级至 Zimbra 官方修复版本。
2. 禁用或清理未知应用专用密码，强制重置高敏账号凭据。
3. 对 Webmail 入口启用严格访问控制、MFA 和异常登录告警。
4. 加强邮件网关对 HTML 邮件、脚本片段和异常 CSS 结构的检测。

参考来源：

https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-zimbra-zero-click-flaw-for-email-theft/

## 风险三：Fake Claude 广告投毒传播 SectopRAT，AI工具下载入口成为高热钓鱼场景

Huntress 披露的 FakeAgent 活动显示，攻击者通过 Bing 搜索广告引导用户访问托管在真实 claude.ai 域名下的恶意 Artifact，再跳转至伪造 Claude Desktop 安装包并投递 SectopRAT。该活动在 7月21日至22日影响至少 29 个组织，相关页面在移除前已有约 7,100 次访问，说明 AI 工具下载入口正在成为企业初始访问热点。

### 建议排查

1. 检查终端是否下载或运行过异常的 Claude Desktop 安装包。
2. 排查 SectopRAT、ArechClient2、DLL 侧载、计划任务持久化和异常远控行为。
3. 检查员工近期通过搜索广告下载 AI 工具、开发工具、远程协作工具的记录。
4. 排查浏览器密码、Cookie、VPN 凭据、IM 工具凭据是否存在异常使用。

### 加固建议

1. 通过企业软件分发平台统一提供 AI 工具安装包。
2. 对搜索广告软件下载、仿冒安装包和新注册相似域名访问建立告警。
3. 对浏览器凭据、Cookie、远程控制和 HVNC 行为加强终端检测。
4. 建立 AI 工具白名单，避免员工直接从广告结果下载安装。

参考来源：

https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat

## 风险四：Chaos 勒索关联 msaRAT 借浏览器隐藏C2，终端行为检测需补强

Cisco Talos 披露，Chaos 勒索相关攻击中出现新的 Rust 后门 msaRAT。该恶意软件利用 Chrome 或 Edge 的调试能力和 WebRTC 通信，让外联流量看起来更像正常浏览器行为。对依赖域名信誉、端口放行和普通 C2 阻断的企业而言，此类“借浏览器通信”的后门会显著增加检测难度。

### 建议排查

1. 检查终端是否存在异常无头 Chrome、Edge 进程和远程调试参数。
2. 排查近期邮件钓鱼、语音钓鱼、远程管理软件安装和伪装更新包执行记录。
3. 检查 Cloudflare Workers、Twilio TURN、WebRTC 相关异常外联。
4. 关联 EDR、代理日志和身份日志，确认是否存在勒索前置活动。

### 加固建议

1. 对浏览器远程调试参数、无头运行和异常父子进程建立告警。
2. 将合法云服务访问纳入行为基线，不做简单全量放行。
3. 对远程管理软件安装、MSI 执行和内存加载 DLL 进行重点监控。
4. 在勒索攻击预案中增加“浏览器代理 C2”检测规则。

参考来源：

https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/

## 风险五：Dolphin X 窃密木马引入AI画像，开发者与云凭据成为高价值目标

Varonis 披露 Dolphin X 窃密木马与远控工具正在地下论坛销售，其面板声称可窃取 300 多类应用数据，并通过 AI Profiler 对感染主机进行价值评分。对企业而言，风险重点在于开发者终端和云运维终端：本地 `.env` 文件、SSH 密钥、云 Token、密码管理器和浏览器凭据都可能被用于后续入侵。

### 建议排查

1. 检查开发者终端、本地项目目录和云运维主机上的长期凭据存储情况。
2. 排查异常的 HVNC、远程桌面、浏览器凭据读取和批量文件打包行为。
3. 检查云访问 Token、Git Token、SSH Key 和密码管理器访问日志。
4. 关注地下木马投递、钓鱼附件、假工具安装包和压缩包执行链路。

### 加固建议

1. 减少长期凭据落盘，优先使用短期 Token、Vault 和按需授权。
2. 对开发者终端启用敏感文件访问监控和出站数据检测。
3. 对云管理权限实施最小权限、JIT 授权和异常地理位置告警。
4. 将“终端被窃密后凭据轮换”纳入标准应急流程。

参考来源：

https://hackernoon.com/dolphin-x-stealer-targets-300-apps-and-profiles-users-with-ai

## 风险六：RefluXFS Linux 本地提权影响企业发行版，服务器与多租户环境需优先更新

Qualys 披露 Linux Kernel XFS 文件系统漏洞 CVE-2026-64600。该问题影响启用 XFS reflink 的系统，攻击者在本地低权限条件下可能覆盖受保护文件并获取 root 权限。由于 XFS 在企业 Linux 发行版、容器宿主机和虚拟化节点中较常见，存在本地执行入口的服务器应尽快纳入补丁计划。

### 建议排查

1. 识别使用 XFS 文件系统且启用 reflink 的 Linux 服务器。
2. 检查内核版本是否处于受影响范围。
3. 排查多用户主机、容器宿主机、共享计算节点和托管平台节点。
4. 检查近期本地提权、SUID 文件异常、配置文件被覆盖等迹象。

### 加固建议

1. 按发行版公告更新 Linux Kernel，并完成重启验证。
2. 对多用户主机、容器宿主机和共享计算节点优先修复。
3. 收紧本地低权限账号、临时目录和可写目录权限。
4. 对关键系统启用文件完整性监控和异常提权告警。

参考来源：

https://www.bleepingcomputer.com/news/linux/new-refluxfs-linux-flaw-lets-attackers-gain-root-privileges/

## 风险七：Origin Energy 数据泄露确认，能源客户数据或被用于定向诈骗

Origin Energy 7月23日确认客户数据遭未授权访问和披露，7月24日澳大利亚媒体继续关注其后续诈骗风险。可能受影响数据包括姓名、地址、出生日期、电话、账户信息以及部分银行卡或信用卡尾号。公用事业企业拥有大量实名客户资料，泄露后容易被用于冒充客服、账单诈骗、身份冒用和二次钓鱼。

### 建议排查

1. 排查客户数据平台、CRM、客服系统和第三方数据处理接口访问记录。
2. 检查批量导出、异常查询、非工作时间访问和异常管理员操作。
3. 核查是否存在未授权数据同步、影子数据库或外包账号滥用。
4. 关注客户投诉、钓鱼短信、冒充客服和账户接管迹象。

### 加固建议

1. 对客户数据访问实施分级授权和最小权限。
2. 对批量导出、敏感字段查询和异常下载建立实时告警。
3. 对客服、营销、外包和数据分析账号强化 MFA 与行为审计。
4. 制定数据泄露后的客户通知、诈骗预警和监管沟通流程。

参考来源：

https://www.originenergy.com.au/about/investors-media/update-on-data-security-incident/

**PART.****02**

总体处置建议‍‍‍

## 总结

今天的热点风险主要集中在三类企业痛点：高价值业务系统被勒索团伙盯上，邮件与终端凭据被隐蔽窃取，以及 AI 工具、浏览器和开发者环境成为新的攻击跳板。安全运营团队应优先处理公网暴露、已被利用、可导致数据外泄或凭据泄露的系统，并在补丁之外同步完成日志排查和凭据轮换。

## 整体风险处置建议

1. 优先排查公网暴露的 PLM、邮件、远程管理和开发支撑系统。
2. 对已确认被利用或被勒索团伙关注的漏洞执行补丁、隔离和取证闭环。
3. 对云密钥、Git Token、数据库凭据、浏览器凭据和应用专用密码集中轮换。
4. 对 AI 工具下载、浏览器调试能力、CI/CD 工作流和开发终端建立允许清单。
5. 强化异常 WebShell、无头浏览器、DNS 外传和批量数据导出的检测。
6. 将客户数据系统和供应链系统纳入勒索攻击与数据泄露演练。

## 合规说明

以上内容基于公开信息整理，仅用于网络安全防护与管理决策参考，具体影响范围与修复方式请以厂商官方公告为准。

![](https://mmbiz.qpic.cn/mmbiz_png/iaPgUxMqaSAhoh0qmQmVFSZR5CZH6zqTtXJAnxcsIYOGT6gdZxjJicvloaqjr7XhADDbc0IfHy7SYHoDKfQR3bwwRZoz58vxD8YkL4E1S6uKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaPgUxMqaSAjLgib6qPpqOw0kZlYBRwrY4qLM4trxNBkSLlZECbuuGKGnia3DwZZQC5lGe1z03Dqc22xCwc0UrhAHkJiaLQdKpCz24b18P4B6Ow/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaPgUxMqaSAgSZ8kG6XSXjCxBibx0ptvia0wlqy8WngVzGH1dngS2WeUwXXde2k5X4U8pE4HfcFkb3GphRPNJhI4dbhibYASkakicMqPKw4jvgz4/0?wx_fmt=png)

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