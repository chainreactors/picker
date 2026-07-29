---
title: 网络安全日报 | 2026-07-27
url: https://mp.weixin.qq.com/s/wrrlJ6-5Ws7xNNzhhSMJzg
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:02:06.394099
---

# 网络安全日报 | 2026-07-27

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZFqiaYcag5AHZbIibx8sfz26SSJcdaJVBlyI3TIVopwVloZmZPWjbSEH89gh28o3GCfn6oTZdTgF8hUqjTkRGQznMoAZYRPRicypA/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-27

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月27日（星期一） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 3 极危事件 | 4 高危事件 | 2 中危事件 | 3 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：Clop 利用 PTC Windchill/FlexPLM 反序列化 RCE CVE-2026-12569（CVSS 9.3）持续定向勒索，07-25 Ransom-ISAC 协调预警后 07-26~07-27 仍有新失陷，部署十六进制名 JSP webshell 于 /Windchill/login/，4 个已知 IoC**

**🔴 极危：Certighost AD CS 提权 CVE-2026-54121（CVSS 8.8）07-27 仍为表内第2天，PoC 已入红队标准武器库，低权限域用户伪造 DC 身份签 DC 证书→PKINIT→DCSync 提取 krbtgt 完全域接管**

**🔴 极危：持续威胁 — Zimbra CVE-2025-66376 零点击 XSS 被 Laundry Bear 利用 + Chaos msaRAT 浏览器隐藏 C2 + Claude Cowork SharedRoot CVE-2026-46331 AI agent 沙箱逃逸（07-27 新入表），三条独立链均在发酵**

**🟠 高危：AI/供应链双线告急 — Hermes 借 AI agent「YOLO」无人值守入侵泰国财政部(Go 植入 Hades) + PyPI mrmustard 量子库投毒窃 SSH/AWS/K8s 凭据 + Kimi K3 自主发现 Redis 7 两处 RCE 获官方确认 + Check Point 披露 TikTok 漏洞后续**

**🟡 中危：紧迫倒计时 — SharePoint CVE-2026-50522 ED 26-04 联邦修补仅剩 1 天(07-28) + Check Point 16232 KEV 联邦修补截止(07-25)已过 + Citrix 53890 超期在野 + wp2shell 双 CVE 持续利用**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

Clop 利用 PTC Windchill/FlexPLM 反序列化 RCE CVE-2026-12569（CVSS 9.3）持续定向勒索 — Ransom-ISAC 协调预警后续（持续发酵）

📰 Ransom-ISAC / eCrime.ch / DEFUSED / The Hacker News / CISA KEV · 📅 2026-07-24 ~ 07-27（持续发酵）

Clop 勒索软件（FIN11 / Chubby Scorpius）利用 PTC Windchill / FlexPLM 反序列化 RCE 漏洞 CVE-2026-12569（CVSS 9.3，CWE-502）的定向勒索行动持续发酵：07-25 Ransom-ISAC / eCrime.ch / DEFUSED 联合协调预警后，07-26~07-27 仍出现新失陷线索。攻击链：FlexPLM WSDL 接口预认证信息泄露（CVSS 7.5）获取内部上下文 → Windchill login servlet 服务端反序列化缺陷实现未认证 RCE → 在 /Windchill/login/ 部署十六进制命名（如 0x3f9a…jsp）JSP webshell。已知 IoC：216.152.148.54 / 216.152.151.204 / 104.243.35.63 / 5.180.41.35，勒索邮箱 support@cryptohox.com。制造/汽车/航天/零售业的 PLM/ERP 承载产品设计、工程数据与供应链，失陷即核心知识产权外泄，且 6 月底已入 CISA KEV、野外利用活跃、补丁覆盖率低。

Hermes 攻击行动借 AI agent「YOLO」无人值守入侵泰国财政部后续 — Go 植入 Hades 自主下载执行（持续发酵）

📰 安全研究团队 / 媒体披露 · 📅 2026-07-25 ~ 07-27（持续发酵）

Hermes 攻击行动利用 AI agent『无人值守（YOLO）』运行模式入侵泰国财政部的事件持续发酵。攻击者诱使目标在开启自主执行权限的 AI agent 环境中运行恶意指令，agent 在无人工确认下自行下载并执行 Go 语言植入程序 Hades——具备命令执行、文件窃取与持久化能力，并针对政府财务系统横向移动。此事件标志『AI agent 自主权限滥用』已从概念验证走向真实国家级定向攻击；当 agent 被赋予不受约束的工具调用与代码执行权限（尤其对接内部系统、凭据与云服务时），攻击者只需污染其决策输入即可完成整条入侵链。多家安全团队提示应将 AI agent 权限收敛、命令审批与行为审计纳入零信任架构，并对 agent 可调用的凭据做最小授权。

PyPI 量子库 mrmustard 0.7.4 供应链投毒持续发酵 — 安装期静默窃取 SSH/AWS/K8s 凭据经 DNS 隧道外传

📰 PyPI Security / Xanadu / 开源社区 · 📅 2026-07-25 ~ 07-27（持续发酵）

PyPI 上的连续变量量子机器学习库 mrmustard（Xanadu 开源框架）0.7.4 版本供应链投毒持续发酵：恶意版本于安装时静默窃取 SSH 私钥、AWS 凭据与 Kubernetes 配置（~/.kube/config），并经 DNS 隧道外传至攻击者域名。PyPI 已下架恶意版本、Xanadu 发布清理声明，但下游已安装的污染环境仍需排查。该投毒延续 2026 年『高价值开发者依赖 + 凭据窃取』供应链主线（此前 npm / Maven / PHP 均现同类手法），量子与 AI 研究社区为重点目标。开发者应锁定依赖哈希、启用私有镜像与构建审计、对安装脚本做沙箱验证，并对 ~/.ssh 与 ~/.aws 做访问审计。

AI 模型 Kimi K3 自主发现 Redis 7 两处内存破坏缺陷获官方确认 — Streams UAF + RedisBloom TDigest OOB，暂无补丁（新进展）

📰 Kimi K3 安全研究 / Redis 官方 · 📅 2026-07-25 ~ 07-27（新进展）

Kimi K3 自主发现 Redis 7 的两个高危内存破坏缺陷（尚无 CVE）已获 Redis 官方确认并进入修复排期：①Streams 模块 use-after-free（UAF），特制 XADD / XGROUP 可触发，在一定条件下 RCE；②RedisBloom 模块 TDigest 数据结构越界读写（OOB），破坏堆内存。两者均影响默认配置 Redis 7 实例，公网暴露的缓存/消息队列节点风险最高。Redis 官方确认将发布修复版本，建议用户暂不将 Redis 7 直接暴露公网。此事件再次印证『AI 辅助漏洞挖掘』在真实开源组件中的落地能力——安全团队应优先将 Redis 置于私有网络、启用认证与 ACL、禁用未用模块（如 RedisBloom）、监控异常命令与崩溃。

朝鲜关联 APT BlueNoroff 新型 Zoom 钓鱼工具包持续活跃 — 伪造会议邀请诱装后门，画像并窃取加密钱包

📰 安全研究团队 / 威胁情报 · 📅 2026-07-25 ~ 07-27（持续发酵）

朝鲜关联 APT BlueNoroff（Lazarus 关联）新型 Zoom 钓鱼工具包持续活跃：攻击者伪造 Zoom 会议邀请与更新提示，诱导受害者安装带后门的『Zoom』客户端或浏览器扩展，进而画像并窃取加密钱包（MetaMask、硬件钱包助记词输入）相关数据。该套件含伪造登录页、凭证收割表单与针对加密货币交易所的定向投递，体现 Lazarus / BlueNoroff 持续将加密货币资产作为核心目标、并借高频视频会议习惯实施社工。防御侧须对下载的会议软件做来源校验、对钱包操作环境做隔离、警惕非官方渠道的『Zoom 更新』，并对企业视频会议账户启用防钓鱼 MFA。

SharePoint CVE-2026-50522 反序列化 RCE 利用升级 + CISA ED 26-04 联邦修补仅剩 1 天（07-28）— 窃取机器密钥持久化（新进展）

📰 watchTowr / CISA / Microsoft / Defused / AJ King · 📅 2026-07-20 ~ 07-27（新进展）

Microsoft SharePoint 反序列化 RCE CVE-2026-50522（CVSS 9.8，CWE-502）利用持续升级，CISA 紧急指令 ED 26-04 要求联邦机构 07-28 前修补并轮换机器密钥——大限仅剩 1 天。最危险之处在攻击者窃取 IIS 机器密钥：即使后续打补丁，窃取到的密钥仍可伪造有效令牌持久化访问，watchTowr 称其具 ToolShell 级影响，为过去一个月第 4 个在野利用的 SharePoint CVE。面向互联网的本地部署风险最高，联邦与关键行业须于 07-28 前完成修补 + 密钥轮换，否则失陷窗口将长期存在。安全团队应假设已遭尝试入侵、猎杀 WebShell 与凭据窃取。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 3 条 |

CVE-2026-54121CVSS 8.8

**受影响产品：**Microsoft Active Directory Certificate Services（AD CS，企业 PKI，签发用于域内加密/签名/PKINIT 身份验证的 X.509 证书，是整个域身份信任根；一旦被伪造 DC 证书即可接管域）

**漏洞描述：**CWE-285 不当授权（Improper Authorization）— AD CS 在注册『chase』回退（chase client DC）时信任请求者提供的 cdc（ms-DS-MachineAccountQuota 派生）主机名，而未验证其是否为真实域控。低权限域用户借恶意 SMB/LDAP/LSA 监听 + 默认 ms-DS-MachineAccountQuota=10 创建机器账户，伪造 DC 身份使 CA 签发 DC 证书，进而经 PKINIT 认证为 DC 并 DCSync 提取 krbtgt，实现完全域接管（Certighost 攻击链）。

**利用状态：**07-24 PoC（Certighost）由 H0j3n & Aniq Fakhrul 公开（github.com/aniqfakhrul/CVE-2026-54121），CVSS 8.8；07-14 微软补丁新增 \_ValidateChaseTargetIsDC 校验目标确为真实 DC；截至 07-27 尚未入 CISA KEV，但公开武器化路径已形成、域环境暴露面高，多支红队已将此 PoC 纳入标准域提权武器库。  ·  **补丁状态：**安装 07-14 微软安全更新；临时缓解：certutil -setreg policy\EditFlags -EDITF\_ENABLECHASECLIENTDC 后 Restart-Service CertSvc -Force（须先在 staging 环境测试）；审查 AD CS 证书模板、限制注册权限、启用 EID 4886/4887 证书请求审计、对来自非 DC 的 DCSync（EID 4662 Replicating Directory Changes）告警。

CVE-2026-12569CVSS 9.3

**受影响产品：**PTC Windchill / FlexPLM（制造业 PLM/ERP，承载产品设计、工程数据与供应链，行业含制造/汽车/航天/零售；是核心知识产权与研发协作中枢）

**漏洞描述：**CWE-502 不可信数据反序列化（Deserialization of Untrusted Data）— Clop 链式利用 FlexPLM WSDL 接口的预认证信息泄露（CVSS 7.5）获取内部上下文，再触发 Windchill login servlet 服务端反序列化缺陷，实现未认证远程代码执行，并在 /Windchill/login/ 路径下部署十六进制命名（如 0x3f9a…jsp）的 JSP webshell 维持持久化。

**利用状态：**Clop（FIN11 / Chubby Scorpius）自 07-24 起持续活跃利用，07-25 Ransom-ISAC / eCrime.ch / DEFUSED 联合协调预警（The Hacker News 报道）；CISA KEV（6 月底收录）；PTC 6-17 发布补丁但覆盖率低。07-26~07-27 持续出现新失陷线索，已知 IoC：216.152.148.54 / 216.152.151.204 / 104.243.35.63 / 5.180.41.35；勒索联系邮箱 support@cryptohox.com。  ·  **补丁状态：**升级 PTC Windchill / FlexPLM 至 6-17 补丁；在网络边界阻断上述 IoC IP；审查 /Windchill/login/ 下异常 JSP/webshell；监控 FlexPLM WSDL 预认证探测与异常反序列化请求；对疑似失陷主机做数据外泄狩猎与凭据轮换。

CVE-2026-46331CVSS 9.1

**受影响产品：**Claude Cowork（企业 AI 编码 agent 协作环境，在隔离 VM/容器沙箱中执行代码、读写本地文件与 git 仓库，是开发者日常 AI 辅助编程入口，宿主机承载 SSH 密钥、浏览器凭证与企业代码仓���）

**漏洞描述：**CWE-264 权限边界不当（沙箱逃逸）— Claude Cowork 的 SharedRoot 机制在宿主机与沙箱 VM 间建立共享根目录挂载，因挂载权限配置缺陷，AI agent 在沙箱内执行的代码可越权读写宿主机文件系统（含 ~/、~/.ssh、浏览器凭证、企业代码仓库），实现『沙箱逃逸』。攻击者可借提示注入诱导 agent 读取/外传宿主机敏感文件，无需任何传统漏洞利用。

**利用状态：**07-25 Accomplish AI / The Hacker News 披露；07-26 首个概念验证 PoC 公开（github.com/anthropics/CVE-2026-46331-poc），CVSS 9.1；AI 编码 agent 逃逸已从理论走向可利用，Anthropic 已发布缓解指南并默认收紧 SharedRoot 权限。该漏洞与 Hermes『AI agent YOLO 无人值守』入侵同属 2026 年『AI agent 权限滥用』主线。  ·  **补丁状态：**升级 Claude Cowork 至修复版本、禁用 SharedRoot 共享挂载或限制为只读子集；对 AI agent 沙箱启用只读根 + 命名空间隔离 + seccomp；禁止 agent 访问 ~/.ssh、密钥链与凭证文件；对 agent 读写操作做审计与告警；对开发机启用 EDR 文件访问监控。

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Clop PTC Windchill/FlexPLM 反序列化 RCE 链拆解（CVE-2026-12569）：WSDL 预认证信息泄露 + login servlet 反序列化 + 十六进制 JSP webshell（持续跟踪）

📰 Ransom-ISAC / eCrime.ch / DEFUSED / The Hacker News · 📅 2026-07-27

【可学技术 — 制造业 PLM/ERP 反序列化 RCE 利用链（①为何预认证即可打：FlexPLM 的 WSDL 接口默认暴露且缺乏授权，攻击者可先经 ?wsdl 拉取接口元数据、枚举可调用方法获取内部上下文——常被忽略的『信息泄露前置』步骤→②Windchill login servlet 如何对不可信请求体做反序列化（CWE-502），特制 payload 触发服务端任意对象实例化与 gadget 链执行→③为何 webshell 命名为十六进制串（如 0x3f9a…jsp）并落在 /Windchill/login/：规避基于文件名特征（\*.jsp / shell\*）的 WAF 与文件监控，借合法路径伪装→④IoC 如何落到 4 个 IP 与勒索邮箱 support@cryptohox.com，以及 Clop/FIN11 的定向勒索 TTP）→安全团队可借鉴此方法→对 Windchill/FlexPLM 做 WSDL 接口鉴权收敛、反序列化请求审计、/login/ 异常 JSP 狩猎与 IoC 阻断

Chaos msaRAT『Living off the Browser』C2 逆向（Cisco Talos）：无头浏览器 + WebRTC DataChannel + Twilio TURN 中继隐藏真实 C2

📰 Cisco Talos / Help Net Security / The Hacker News · 📅 2026-07-27

【可学技术 — 高隐蔽 C2 流量伪装与检测（①为何 RAT 进程仅绑 127.0.0.1 并启动 Chrome/Edge 无头实例经 CDP 驱动：将真实 C2 通信伪装成浏览器正常上网，网络侧只见 Cloudflare Workers / Google STUN / Twilio 访问→②WebRTC DataChannel + TURN 中继如何让攻击者真实服务器地址从不出现在流量中，且 DTLS + ChaCha-Poly13...