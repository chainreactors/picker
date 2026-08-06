---
title: 网络安全日报 | 2026-08-05
url: https://mp.weixin.qq.com/s/of8nhQp2iF6dZ-ZHG0jB0g
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:59:34.873518
---

# 网络安全日报 | 2026-08-05

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZEBGtsvlN1qL759yhrlqktu9SSx7ohnibUAZW4ONXvia5uw4XoxnaAesDOz14QNQm8Ek7C44ApvrSSpPbhibsPbFicUfWR8wqS0VHU/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-08-05

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年8月5日（星期三） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 1 极危事件 | 3 高危事件 | 2 中危事件 | 5 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

IBM Langflow CVE-2026-9198 入 CISA KEV（08-04）：未认证 RCE，AI agent 工具成新攻击面（新披露 / 极危）

📰 IntelFusions / IBM Security Advisory / CISA KEV · 📅 2026-08-04（披露 / 入 KEV）

IBM Langflow（14.5 万+ GitHub stars 的低代码 AI agent 编排框架）的 CVE-2026-9198（CVSS 9.8，CWE-94）于 08-04 被 CISA 列入 KEV（Due 08-07）并确认在野利用。攻击链为：任意网络可达调用方访问 /api/v1/auto\_login 即被签发 superuser token，该令牌解锁 /api/v1/validate/code 执行任意代码——默认部署无需任何凭据即完整 RCE。Langflow 此前多次被武器化（CVE-2026-33017 披露后 20 小时内即遭利用），本次 auto\_login 链在暴露实例上零凭据可达，使 AI 开发环境成为企业内网新入口。

CISA KEV 08-04 批量新增 3 项：Langflow + Tomcat CVE-2026-34486 + N-able CVE-2026-18556；3 天修复窗口成常态（新披露）

📰 CISA KEV / IntelFusions / RECATOOLS · 📅 2026-08-04（入 KEV）

CISA 于 08-04 一气将三项在野漏洞列入 KEV：IBM Langflow CVE-2026-9198（9.8）、Apache Tomcat CVE-2026-34486（7.5，EncryptInterceptor 绕过回归缺陷）、N-able N-central CVE-2026-18556（8.2，第二张 N-central KEV 条目），Due 均为 08-07（3 天窗口）。RECATOOLS 对 2026 年 176 条 KEV 新增分析显示：3 天修复窗口占比已升至 39.2%（原 21 天窗口降至 25%），短窗口从例外变为常态——「等下个维护窗口」的处置节奏已不再适配输入信号。

INC Ransomware 借 SonicWall SMA 1000 零日横行：CVE-2026-15409（SSRF 10.0）+ CVE-2026-15410（RCE 7.2）窃取 TOTP 种子绕过 MFA（持续发酵）

📰 Resecurity / Volexity / Rapid7 / The Hacker News · 📅 2026-06-22 ~ 08-05（零日利用 / 持续）

INC Ransomware 已成为利用 SonicWall SMA 1000 系列零日的主导威胁行动者：CVE-2026-15409（SSRF，10.0）与 CVE-2026-15410（RCE，7.2）链式实现未认证命令执行与设备接管。Volexity 将初始利用追溯到至少 06-22（早于 7 月补丁数周，属零日利用），归因 UTA0533；Rapid7 确认战术指纹高度一致。攻击者部署 KNUCKLEBALL→Suo5 代理隧道→ORANGETAIL（Behinder 式 webshell），核心窃取设备缓存的 TOTP MFA 种子——持有种子即可离线无限生成有效验证码使 MFA 失效。Ransomware.Live 统计 INC 已宣称 885 名受害者。关键警示：补丁仅『关门』，不撤销已窃取的凭据/会话/种子。

macOS CUPS CVE-2026-39875 root 提权 PoC 公开（08-04，7.8）：cupsd 双逻辑缺陷致本地提权，未更新 Mac 高危（新披露）

📰 dbappsecurity / 安全研究员 Dallas Dubs / Apple 安全公告 · 📅 2026-08-04（披露 / PoC 公开）

macOS 打印特权守护进程 cupsd 被披露存在两个逻辑缺陷串联的本地提权漏洞 CVE-2026-39875（CVSS 7.8）：无特权用户注册指向受控监听器的打印机→cupsd 错误泄露受信任认证令牌→重放令牌定位任意路径→打印任务以 root 写入攻击者内容，全程无需交互即提权至 root。研究员 Dallas Dubs 于 08-04 公开完整细节与 PoC，利用门槛骤降。影响 7 月底安全更新前所有 macOS 版本；苹果已在 Sequoia 15.7.8 / Sonoma 14.8.8 / Tahoe 26.6 修复。与上周 Screen Sharing 预认证 root RCE 共同构成 Mac 平台短期密集漏洞窗口。

NVIDIA Dynamo CVE-2026-24254 OOB write 9.8（08-04 NVD）：AI 推理服务拓扑远程代码执行暴露面扩大（新披露）

📰 NVD / GitHub Advisory / NVIDIA PSIRT · 📅 2026-08-04（NVD 发布）

NVIDIA Dynamo for Linux（开源 LLM/多模态推理服务与分发框架）被披露多模态 serving 拓扑存在越界写（OOB write）漏洞 CVE-2026-24254（CVSS 9.8，AV:N/AC:L/PR:N/UI:N），网络可达且无需认证。成功利用可触发代码执行、特权提升、数据篡改与信息泄露，攻击链为『暴露的推理服务→拓扑越界写→内存破坏→代码执行→宿主推理节点沦陷→借模型权重与云凭据横向』。NVD 于 08-04 发布，受影响/修复版本待 NVIDIA 公告 2026/5842 核实。AI 推理基础设施核心组件暴露在公网的风险随之上升。

勒索与数据窃取浪潮：Baicizhan(dragonforce 08-03) / ProHealth(Krybit 08-02) / Nidec(08-04) / Encore(CRPxO 08-02) 接连被列（持续发酵）

📰 recentbreaches / dexpose / businesswire / cyber.netsecops · 📅 2026-08-02 ~ 08-05（持续）

多起勒索与数据窃取事件在 08-02~08-05 集中曝光：在线教育平台 Baicizhan 于 08-03 被 dragonforce 列名（内部文件外泄，真实性待核实）；新加坡 ProHealth Medical Group 于 08-02 遭 Krybit 勒索并威胁泄露医疗数据；日本电产 Nidec 台湾子公司于 08-04 发布二次调查更新，确认 6 月勒索后文件夹/文件名列表已公开；美国房地产服务商 Encore Enterprises 于 08-02 被 CRPxO 声称窃取 700GB。事件横跨教育、医疗、制造、房地产，双重勒索与泄露站点施压成常态。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 5 条 |

CVE-2026-9198CVSS 9.8

**受影响产品：**IBM Langflow（低代码 AI agent/LLM 工作流编排框架，版本 1.0.0–1.10.0；GitHub 14.5 万+ stars，被数据科学/企业 AI/独立开发者广泛用于构建多智能体与 RAG 管线，常集成 LLM Provider API、内部数据库与云账户；按 IBM 安全公告升级至修复版本）

**漏洞描述：**CWE-94 代码注入——Langflow OSS 1.0.0 至 1.10.0 存在未认证 RCE 链：任意可达网络的调用方访问 /api/v1/auto\_login 端点即可被签发超级用户令牌，该令牌进而解锁 /api/v1/validate/code 端点执行攻击者提交的任意代码。在默认部署下，这意味着无需任何凭据即可获得宿主完整远程代码执行。攻击链为『网络可达 Langflow 实例 → auto\_login 签发 superuser token → 令牌解锁 validate/code → 执行任意代码 → 宿主/AI 开发环境完全接管 → 借存储的 LLM/云凭据横向至企业内网』。

**利用状态：**CISA 于 08-04 将 CVE-2026-9198 列入 KEV（Date Added 2026-08-04，Due 2026-08-07），确认在野利用；NVD/IBM 给出 CVSS 9.8 Critical（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）。Langflow 此前多次成为武器化目标：CVE-2026-33017 自披露后 20 小时内即遭利用（Sysdig 观测），CVE-2026-55255 于 07-07 入 KEV。本次 auto\_login→validate/code 链在默认部署下零凭据可达，互联网暴露实例无论配置何种凭据均暴露，主动利用高度可能。  ·  **补丁状态：**按 IBM 安全公告（node/7278927）升级 Langflow 至修复版本；临时：将实例从公网移除/反向代理鉴权、审计暴露面；将 flow 中存储的 LLM Provider Key、云凭据、源码库令牌、数据库凭据视为已泄露并立即轮换；监控 Langflow 进程派生的异常 shell 与 auto\_login/validate/code 异常请求。

CVE-2026-34486CVSS 7.5

**受影响产品：**Apache Tomcat（版本 11.0.20 / 10.1.53 / 9.0.116；最广泛使用的 Java Servlet/HTTP 应用服务器之一，承载大量企业内部与互联网应用；修复版本 11.0.21 / 10.1.54 / 9.0.117）

**漏洞描述：**CWE-311 敏感数据缺失加密——CVE-2026-34486 是 CVE-2026-29146 修复所引入的回归缺陷，导致 Apache Tomcat 的 EncryptInterceptor 可被绕过，集群节点间本应加密传输的敏感数据以明文形式暴露。攻击链为『利用修复引入的回归 → 绕过 EncryptInterceptor → 集群内节点通信敏感数据明文泄露 → 凭据/会话等机密被截获』。该漏洞影响配置了集群 EncryptInterceptor 的 Tomcat 实例。

**利用状态：**CISA 于 08-04 将 CVE-2026-34486 列入 KEV（Date Added 2026-08-04，Due 2026-08-07），确认在野利用；CVSS 7.5（CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N）。Apache 列出受影响版本 11.0.20/10.1.53/9.0.116，建议升级至 11.0.21/10.1.54/9.0.117。因属 KEV 在野项，暴露的 Tomcat 集群须优先修复。  ·  **补丁状态：**升级 Apache Tomcat 至 11.0.21 / 10.1.54 / 9.0.117；临时：对集群间通信启用独立传输层加密（TLS）、网络层隔离集群节点、审计 EncryptInterceptor 配置；对面向互联网实例优先修复并核查是否已被入侵。

CVE-2026-18556CVSS 8.2

**受影响产品：**N-able N-central（远程监控与管理 RMM 平台；CVE-2026-18577 所溯源的『原始』认证绕过漏洞，此前已于 2026.2 修复；CISA 因其被在野利用于 08-04 列入 KEV，Due 08-07；升级至 2026.3.1.7 Hotfix 并核查历史失陷）

**漏洞描述：**CWE-288 备用路径/通道认证绕过——CVE-2026-18556 是 N-able N-central 的原始认证绕过漏洞，即 CVE-2026-18577（不完整补丁遗留的替代利用向量）所溯源的根因漏洞。攻击者可在未认证状态下绕过认证获取远程管理访问并接管管理员账户，进而借 Take Control 横向至托管客户设备、注册 Cloudflare 隧道持久化。攻击链与 18577 同源：『网络可达 N-central 实例 → 备用认证路径绕过 → 远程管理员接管 → Take Control 连接托管设备 → Cloudflare 隧道持久化』。

**利用状态：**CISA 于 08-04 将 CVE-2026-18556 列入 KEV（Date Added 2026-08-04，Due 2026-08-07），确认在野利用——这是 N-central 一周内第二张、12 个月内第四张 KEV 条目。尽管该原始漏洞已于 2026.2 修复，但 KE V 列入表明其仍被现实攻击者利用（可能针对未升级或已失陷实例）。N-able 于 08-02 通报针对原漏洞另一利用方法未被前次修复覆盖（即 18577）。  ·  **补丁状态：**确保 N-central 已升级至 2026.3.1.7 Hotfix（含 18556/18577 修复）并审计实例是否已在补丁前被入侵；将管理接口限制于带外/可信网络、审计管理员账户异常变更；排查已知攻击 IP 入站、用 N-able 检测模板核查 svchost.exe / Cloudflared 服务；轮换 Take Control 与相关凭证。

CVE-2026-24254CVSS 9.8

**受影响产品：**NVIDIA Dynamo for Linux（NVIDIA 的开源 LLM/多模态推理服务与分发框架，用于在多 GPU/节点间编排生成式 AI 推理；被 AI 平台用于大规模部署大模型推理服务；NVIDIA 安全公告 2026/5842，受影响/修复版本待定，建议按公告核验）

**漏洞描述：**NVIDIA Dynamo for Linux 的多模态服务（serving）拓扑存在越界写（out-of-bounds write）漏洞：攻击者可触发越界写，成功利用可能导致代码执行、特权提升、数据篡改、拒绝服务与信息泄露。攻击链为『网络可达的 Dynamo 推理服务 → 多模态 serving 拓扑越界写 → 内存破坏 → 代码执行/特权提升 → 宿主推理节点沦陷 → 借托管的模型权重与云凭据横向』。CVSS v3.1 向量 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H，网络可达、无需认证、复杂度低。

**利用状态：**NVD 于 08-04 发布（CVSS 9.8 Critical，Unreviewed）；CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H。受影响与修复版本在 GitHub Advisory 中标记为 Unknown（NVIDIA 公告 2026/5842 待核实具体版本）。作为 AI 推理基础设施的核心组件，暴露在公网的 Dynamo 节点一旦被利用，影响范围涵盖模型服务与下游云资源，须按厂商公告优先处置。  ·  **补丁状态：**按 NVIDIA 安全公告 2026/5842 升级至修复版本（版本待定，建议核验）；临时：将 Dynamo 推理服务置于内网/零信任网关之后、限制网络可达性、启用最小权限与隔离；监控推理节点异常进程与出站连接；对托管的模型权重与云凭据做访问收敛。

CVE-2026-39875CVSS 7.8

**受影响产品：**Apple macOS CUPS 打印系统（cupsd 特权守护进程；影响 2026 年 7 月底安全更新之前的所有 macOS 版本；修复于 macOS Sequoia 15.7.8 / Sonoma 14.8.8 / Tahoe 26.6）

**漏洞描述：**macOS 打印系统特权守护进程 cupsd 存在两个逻辑缺陷串联的本地权限提升漏洞：无特权用户注册一个指向其受控监听器的打印机，cupsd 错误将一个本不应泄露的受信任认证令牌传递给该监听器；攻击者重放此令牌定位任意文件路径，随后提交打印任务以 root 权限将攻击者控制的内容写入该路径。整个过程无需用户进行任何交互，即可将权限提升至 root 完全控制设备。

**利用状态：**安全研究员 Dallas Dubs 于 08-04 公开完整技术细节与可用 PoC 代码，利用门槛大幅降低；CVSS 7.8（CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H）。影响 2026 年 7 月底安全更新前的所有 macOS 版本；苹果已在 macOS Sequoia 15.7.8 / Sonoma 14.8.8 / Tahoe 26.6 修复。虽尚无在野利用证据，但 PoC 公开使任何未打补丁设备面临极高本地提权风险。  ·  **补丁状态：**立即更新至 macOS Sequoia 15.7.8 / Sonoma 14.8.8 / Tahoe 26.6；对无法即时更新的设备，限制本地低特权账户、收紧文件权限与 cupsd 暴露面；在 EDR 中监控 cupsd 异常令牌传递、异常打印机注册与 root 写入行为；对高价值 Mac 启用文件完整性监控。

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

IBM Langflow CVE-2026-9198 auto\_login→validate/code 未认证 RCE 链拆解：superuser token 伪造如何绕过默认部署认证（Inte...