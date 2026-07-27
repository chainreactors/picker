---
title: 网络安全日报 | 2026-07-26
url: https://mp.weixin.qq.com/s/v34_drwyOrhlEAmaThsb4g
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:40:40.424543
---

# 网络安全日报 | 2026-07-26

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWuEZyvfHZHyc0c4OV4ia8AWIPAEd0sPnZOleBmSx8YfmTAmdOkV0iaLkDaG8JfrYIMjGF5WIZuNLjoDj3JAng41CFTfejAApMRUg90r1Zpg4/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-26

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月26日（星期日） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 3 极危事件 | 4 高危事件 | 2 中危事件 | 2 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：Clop 利用 PTC Windchill/FlexPLM 反序列化 RCE CVE-2026-12569（CVSS 9.3）发动定向勒索，Ransom-ISAC 07-25 协调预警，部署十六进制名 JSP webshell 于 /Windchill/login/，4 个已知 IoC**

**🔴 极危：Certighost AD CS 提权 CVE-2026-54121（CVSS 8.8）PoC 07-24 公开，低权限域用户伪造 DC 身份签 DC 证书→PKINIT→DCSync 提取 krbtgt 完全域接管（H0j3n & Aniq Fakhrul）**

**🔴 极危：持续威胁 — Zimbra CVE-2025-66376 零点击 XSS 被 Laundry Bear 利用 + Chaos msaRAT 浏览器隐藏 C2 + Claude Cowork SharedRoot 沙箱逃逸，三条独立链均在发酵**

**🟠 高危：AI/供应链双线告急 — Hermes 借 AI agent「YOLO」无人值守入侵泰国财政部(Go 植入 Hades) + PyPI mrmustard 量子库投毒窃 SSH/AWS/K8s 凭据 + Kimi K3 自主发现 Redis 7 两处 RCE + Check Point 披露 TikTok 漏洞**

**🟡 中危：持续风险 — Check Point 16232 KEV 联邦修补截止(07-25)已过 + Citrix 53890 超期在野 + SharePoint 50522 ED 26-04 仅剩 2 天(07-28) + wp2shell 双 CVE 持续利用**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

Clop 利用 PTC Windchill/FlexPLM 反序列化 RCE CVE-2026-12569（CVSS 9.3）发动定向勒索 — Ransom-ISAC 07-25 协调预警

📰 Ransom-ISAC / eCrime.ch / DEFUSED / The Hacker News / CISA KEV · 📅 2026-07-24 ~ 07-26（持续）

Clop 勒索软件（FIN11 / Chubby Scorpius）正利用 PTC Windchill / FlexPLM 反序列化 RCE 漏洞 CVE-2026-12569（CVSS 9.3，CWE-502）发动定向勒索行动——Ransom-ISAC、eCrime.ch 与 DEFUSED 于 07-25 发布联合协调预警（The Hacker News 同日报道）。攻击链：先借 FlexPLM WSDL 接口预认证信息泄露（CVSS 7.5）获取内部上下文，再触发 Windchill login servlet 服务端反序列化缺陷实现未认证 RCE，在 /Windchill/login/ 路径下部署十六进制命名（如 0x3f9a…jsp）的 JSP webshell。已知 IoC：216.152.148.54 / 216.152.151.204 / 104.243.35.63 / 5.180.41.35，勒索联系邮箱 support@cryptohox.com。受影响的制造/汽车/航天/零售业 PLM/ERP 系统承载产品设计、工程数据与供应链，一旦失陷可直接外泄核心知识产权。该漏洞 6 月底入 CISA KEV、PTC 6-17 发布补丁，但补丁覆盖率低、野外利用活跃。

Hermes 攻击行动利用 AI agent「无人值守（YOLO）」模式入侵泰国财政部 — Go 植入 Hades 自主下载执行

📰 安全研究团队 / 媒体披露 · 📅 2026-07-25 ~ 07-26（新披露）

一支被称为 Hermes 的攻击行动利用 AI agent 的『无人值守（YOLO）』运行模式，对泰国财政部（Ministry of Finance）发动定向入侵。攻击者诱使目标在开启自主执行权限的 AI agent 环境中运行恶意指令，agent 在无人工确认下自行下载并执行 Go 语言编写的植入程序 Hades——该植入具备命令执行、文件窃取与持久化能力，并针对政府财务系统做横向移动。此事件标志『AI agent 自主权限滥用』已从概念验证走向真实国家级定向攻击：当 agent 被赋予不受约束的工具调用与代码执行权限（尤其对接内部系统、凭据与云服务时），攻击者只需污染其决策输入即可完成整条入侵链。安全团队应将 AI agent 的权限收敛、命令审批与行为审计纳入零信任架构。

PyPI 量子库 mrmustard 0.7.4 遭供应链投毒 — 安装时静默窃取 SSH / AWS / K8s 凭据并经 DNS 隧道外传

📰 PyPI Security / Xanadu / 开源社区 · 📅 2026-07-25（新披露）

PyPI 上的连续变量量子机器学习库 mrmustard（Xanadu 公司开源框架）0.7.4 版本遭供应链投毒：攻击者在恶意版本植入代码，于安装时静默窃取 SSH 私钥、AWS 凭据与 Kubernetes 配置（~/.kube/config），并经 DNS 隧道外传至攻击者控制的域名。PyPI 安全团队已下架恶意版本、Xanadu 发布清理声明。该投毒延续 2026 年『高价值开发者依赖 + 凭据窃取』的供应链攻击主线（此前 npm / Maven / PHP 均出现同类手法），量子与 AI 研究社区因频繁拉取可信学术库而成为重点目标。开发者应锁定依赖哈希、启用私有镜像与构建审计，并对安装脚本做沙箱验证。

Check Point Research 披露 TikTok 平台漏洞（07-26）— 伪造消息控账户 + ads.tiktok.com 存储型 XSS，平台已修复

📰 Check Point Research / TikTok · 📅 2026-07-26（新披露）

Check Point Research 于 07-26 披露 TikTok 平台多个漏洞：攻击者可在受害者不知情下伪造消息内容、操控其账户展示，并通过 ads.tiktok.com 子域的存储型 XSS（CWE-79）注入恶意脚本，实现账户接管内控或传播钓鱼内容。Check Point 已通过负责任披露流程上报，TikTok 方面确认并已修复相关问题。尽管平台侧已修复，该案例凸显巨型社交平台『消息真实性』与『广告子域输入净化』的攻击面：伪造消息可助长诈骗与舆情操纵，而 ads 子域 XSS 一旦结合高权限会话即可跨账户影响。用户应警惕异常消息与登录跳转，平台方须持续强化 CSP 与输入净化。

AI 模型 Kimi K3 自主发现 Redis 7 两处内存破坏缺陷（尚无 CVE）— Streams UAF + RedisBloom TDigest OOB 可 RCE

📰 Kimi K3 安全研究 / Redis 官方 · 📅 2026-07-25（新披露）

AI 模型 Kimi K3 在其安全研究中自主发现 Redis 7 的两个高危内存破坏缺陷（尚无 CVE 编号）：①Streams 模块的 use-after-free（UAF），可由特制 XADD / XGROUP 命令触发，在一定条件下实现远程代码执行；②RedisBloom 模块 TDigest 数据结构的越界读写（OOB），可破坏堆内存。两者均影响默认配置的 Redis 7 实例，暴露公网的缓存 / 消息队列节点风险最高。Kimi K3 团队已向 Redis 官方提交报告，等待修复版本。此事件再次印证『AI 辅助漏洞挖掘』在真实开源组件中落地的能力——安全团队应优先将 Redis 实例置于私有网络、启用认证与 ACL、禁用不必要的模块（如未使用的 RedisBloom），并监控异常命令与崩溃。

朝鲜关联 APT BlueNoroff 新型 Zoom 钓鱼工具包 — 伪造会议邀请与更新诱装后门，画像并窃取加密钱包

📰 安全研究团队 / 威胁情报 · 📅 2026-07-25（新披露）

朝鲜关联 APT BlueNoroff（Lazarus 关联）被披露新型 Zoom 钓鱼工具包：攻击者伪造 Zoom 会议邀请与更新提示，诱导受害者安装带后门的『Zoom』客户端或浏览器扩展，进而画像并窃取加密钱包（如 MetaMask、硬件钱包助记词输入）相关数据。该套件包含伪造登录页、凭证收割表单与针对加密货币交易所的定向投递，体现 Lazarus / BlueNoroff 持续将加密货币资产作为核心目标、并借高频视频会议习惯实施社工。防御侧须对下载的会议软件做来源校验、对钱包操作环境做隔离、警惕非官方渠道的『Zoom 更新』。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 2 条 |

CVE-2026-54121CVSS 8.8

**受影响产品：**Microsoft Active Directory Certificate Services（AD CS，企业 PKI，签发用于域内加密/签名/PKINIT 身份验证的 X.509 证书，是整个域身份信任根；一旦被伪造 DC 证书即可接管域）

**漏洞描述：**CWE-285 不当授权（Improper Authorization）— AD CS 在注册『chase』回退（chase client DC）时信任请求者提供的 cdc（ms-DS-MachineAccountQuota 派生）主机名，而未验证其是否为真实域控。低权限域用户借恶意 SMB/LDAP/LSA 监听 + 默认 ms-DS-MachineAccountQuota=10 创建机器账户，伪造 DC 身份使 CA 签发 DC 证书，进而经 PKINIT 认证为 DC 并 DCSync 提取 krbtgt，实现完全域接管（Certighost 攻击链）。

**利用状态：**07-24 PoC（Certighost）由 H0j3n & Aniq Fakhrul 公开（github.com/aniqfakhrul/CVE-2026-54121），CVSS 8.8；07-14 微软补丁新增 \_ValidateChaseTargetIsDC 校验目标确为真实 DC；尚未入 CISA KEV，但公开武器化路径已形成，域环境暴露面高。  ·  **补丁状态：**安装 07-14 微软安全更新；临时缓解：certutil -setreg policy\EditFlags -EDITF\_ENABLECHASECLIENTDC 后 Restart-Service CertSvc -Force（须先在 staging 环境测试）；审查 AD CS 证书模板、限制注册权限、启用 EID 4886/4887 证书请求审计、对来自非 DC 的 DCSync（EID 4662 Replicating Directory Changes）告警。

CVE-2026-12569CVSS 9.3

**受影响产品：**PTC Windchill / FlexPLM（制造业 PLM/ERP，承载产品设计、工程数据与供应链，行业含制造/汽车/航天/零售；是核心知识产权与研发协作中枢）

**漏洞描述：**CWE-502 不可信数据反序列化（Deserialization of Untrusted Data）— Clop 链式利用 FlexPLM WSDL 接口的预认证信息泄露（CVSS 7.5）获取内部上下文，再触发 Windchill login servlet 服务端反序列化缺陷，实现未认证远程代码执行，并在 /Windchill/login/ 路径下部署十六进制命名（如 0x3f9a…jsp）的 JSP webshell 维持持久化。

**利用状态：**Clop（FIN11 / Chubby Scorpius）自 07-24/25 活跃利用；Ransom-ISAC / eCrime.ch / DEFUSED 于 07-25 发布联合协调预警（The Hacker News 同日报道）；CISA KEV（6 月底收录）；PTC 6-17 发布补丁；已知 IoC：216.152.148.54 / 216.152.151.204 / 104.243.35.63 / 5.180.41.35；勒索联系邮箱 support@cryptohox.com。  ·  **补丁状态：**升级 PTC Windchill / FlexPLM 至 6-17 补丁；在网络边界阻断上述 IoC IP；审查 /Windchill/login/ 下异常 JSP/webshell；监控 FlexPLM WSDL 预认证探测与异常反序列化请求；对疑似失陷主机做数据外泄狩猎与凭据轮换。

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Clop PTC Windchill/FlexPLM 反序列化 RCE 链拆解（CVE-2026-12569）：WSDL 预认证信息泄露 + login servlet 反序列化 + 十六进制 JSP webshell

📰 Ransom-ISAC / eCrime.ch / DEFUSED / The Hacker News · 📅 2026-07-25

【可学技术 — 制造业 PLM/ERP 反序列化 RCE 利用链（①为何预认证即可打：FlexPLM 的 WSDL 接口默认暴露且缺乏授权，攻击者可先经 ?wsdl 拉取接口元数据、枚举可调用方法获取内部上下文——这是常被忽略的『信息泄露前置』步骤→②Windchill login servlet 如何对不可信请求体做反序列化（CWE-502），特制 payload 触发服务端任意对象实例化与 gadget 链执行→③为何 webshell 命名为十六进制串（如 0x3f9a…jsp）并落在 /Windchill/login/：规避基于文件名特征（\*.jsp / shell\*）的 WAF 与文件监控，借合法路径伪装→④IoC 如何落到 4 个 IP 与勒索邮箱 support@cryptohox.com，以及 Clop/FIN11 的定向勒索 TTP）→安全团队可借鉴此方法→对 Windchill/FlexPLM 做 WSDL 接口鉴权收敛、反序列化请求审计、/login/ 异常 JSP 狩猎与 IoC 阻断

PyPI mrmustard 供应链投毒逆向（Xanadu 量子库）：安装时凭据窃取（SSH / AWS / K8s）与 DNS 隧道外传手法

📰 PyPI Security / Xanadu / 开源社区 · 📅 2026-07-25

【可学技术 — Python 包安装期恶意代码执行与凭据外传（①恶意代码如何嵌入 setup.py / 安装钩子（setup.cfg 的 [options.extras\_require] 或 import 时触发），使 pip install 即执行而非运行期→②窃取目标为何是 SSH 私钥（~/.ssh/id\_rsa）、AWS 凭据（~/.aws/credentials）与 Kubeconfig（~/.kube/config）：覆盖代码仓库、云与集群三类最高价值凭据→③为何用 DNS 隧道外传：将凭据编码进子域名查询，规避基于 HTTP/TLS 明文流量的 DLP 与出口防火墙检测，且 DNS 通常默认放行→④与 2026 年 npm/Maven/PHP 同源手法的共性）→安全团队可借鉴此方法→在 CI 中对依赖做哈希锁定与沙箱安装验证、监控异常 DNS 子域查询、对 ~/.ssh 与 ~/.aws 做访问审计

Redis 7 内存破坏（Kimi K3 AI 发现）原理与缓解：Streams UAF（特制 XADD/XGROUP）+ RedisBloom TDigest OOB 越界读写

📰 Kimi K3 安全研究 / Redis 官方 · 📅 2026-07-25

【可学技术 — 内存安全类 RCE 的 root cause 与防御（①Streams 模块的 UAF：某命令路径在释放底层 radix/rax 节点后仍保留悬空引用，特制 XADD/XGROUP 触发重放使控制流落入已释放内存→②RedisBloom TDigest 的 OOB：压缩结构在合并/更新分位数时未校验偏移边界，越界读写破坏相邻堆块元数据→③两者在默认配置下可达、公网暴露实例最危险，且 Redis 通常以高权限运行使 RCE 影响放大→④『AI 辅助漏洞挖掘』如何对大型 C 项目做缺陷定位，提示未来补丁评审与模糊测试应前置）→安全团队可借鉴此方法→将 Redis 置于私有网络、启用 requirepass + ACL、以 rename-command 禁用危险命令、卸载未用模块、监控异常崩溃与命令模式

|  |  |  |
| --- | --- | --- |
| 🛠 | 安全工具动态 | 3 条 |

projectdiscovery/nuclei-templates — 7月第12周（持续更新至 2026-07-26）：新增 CVE-2026-54121（Certighost AD CS）/ CVE-2026-12569（PTC Windchill）+ Clop IoC 检测

📰 GitHub / projectdiscovery · 📅 持续更新至 2026-07-26

ProjectDiscovery 漏洞检测模板库针对本期高危项快速更新。本期重点：①CVE-2026-54121 ...