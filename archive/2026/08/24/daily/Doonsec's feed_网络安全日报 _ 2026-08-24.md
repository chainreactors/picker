---
title: 网络安全日报 | 2026-08-24
url: https://mp.weixin.qq.com/s/eKZiTzBeUC2ulIoK9yotyA
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:57:45.184495
---

# 网络安全日报 | 2026-08-24

# 网络安全日报 | 2026-08-24

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔒 网络安全日报

2026年8月24日（星期一） | 数据来源：NVD / CISA KEV / CISA / CVE Brief / Enigma Global / IONIX / Rapid7 / VulDB / ENISA / Google Cloud / BleepingComputer / Kaspersky / The Hacker News / ajking.io / mySites.guru

|  |  |  |  |
| --- | --- | --- | --- |
| 1 极危事件 | 3 高危事件 | 2 中危事件 | 5 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 5 条 |

Joomla Fabrik 扩展未认证 RCE 集群曝光：CVE-2026-76604/76605/76606/76607 均 CVSS 10.0

📰 Enigma Global / mySites.guru / IONIX · 📅 2026-08-23

Fabrik 是 Joomla 上广泛使用的表单/数据构建扩展，08-23 披露一批 critical 漏洞：CVE-2026-76604（PHP 表单元素未认证 RCE，影响 < 4.7.3）、CVE-2026-76605（图像元素 CWE-94 代码注入 RCE，1.0.0–4.7.3）、CVE-2026-76606（图像元素 CWE-22 路径遍历）、CVE-2026-76607（下载插件缺失访问检查），CVE-2026-77992（calc 元素 heredoc 逃逸 9.5）及两枚 SQLi（CVE-2026-76571/76602，9.3）全部未认证。官方已重发 4.7.2 构建（部分公告以 4.7.3 为修复分界），但 4.7.2 曾被多次重发导致版本识别混乱，且尚无确认在野利用——未认证+满分 CVSS 使其成为自动化扫描的优先目标，互联网暴露的 Joomla+Fabrik 站点面临整服沦陷。

SOHO/边界网络设备 RCE 连发：TRENDnet TEW-821DAP（CVE-2026-77946）+ Comfast CF-N1-S（CVE-2026-78050）

📰 IONIX / Rapid7 / VulDB · 📅 2026-08-22~08-23

CVE Brief 将网络边缘硬件列为 08-23 critical 榜首：TRENDnet TEW-821DAP 2.2.01b05 的 NTP 时区配置处理器（/cgi-bin/apply\_time.cgi，uci\_safe\_get 函数）存在未认证栈溢出 CVE-2026-77946，CVSS 10.0（v3.1）/ 9.3（v4），公开 PoC 可用，设备已 EOL、暂无官方补丁；Comfast CF-N1-S 2.6.0.1 的 Web 管理 NTP 时区接口（/cgi-bin/mbox-config，sub\_41AD7C）栈溢出 CVE-2026-78050，CVSS 9.9，漏洞利用已公开。两者均无补丁可用，攻击者可借畸形 HTTP POST 直接以 root 接管设备并作为内网跳板，建议立即收敛管理面、禁用 WAN 远程管理、将设备置于防火墙后。

Google Cloud Application Integration 缺失授权漏洞 CVE-2026-12710（CVSS 9.3）公开

📰 ENISA EUVD / Google Cloud / CIRCL · 📅 2026-08-22

CVE-2026-12710 是 Google Cloud Application Integration 的 QueryEngineTask 组件缺失授权漏洞（CWE-862），影响 2025-04-28 至 2026-04-04 的版本，外部攻击者无需认证即可访问敏感内部数据（CVSS v4 9.3，AV:N/AC:L/PR:N/UI:N/VC:H/VI:H）。Google 表示该问题已于 2026-04-04 在服务端修复、客户无需任何操作，但作为云集成平台，其查询引擎暴露内部数据面的风险值得集成方复核自身数据流与最小权限配置，避免类似「云侧漏洞+客户不可控」的信任盲区。

车载 Android 头单元遭 MoYu/BadBox 供应链投毒：DoFun TWCore→JarService→zhima 反向代理僵尸网络

📰 BleepingComputer / Kaspersky · 📅 2026-08-23

Kaspersky 分析确认，MoYu 组织（曾关联 BadBox 僵尸网络）针对中国车机厂商 DoFun（深圳驾控）的 Android 头单元发起供应链攻击：6 月发现合法系统应用 TWCore 从 cardoor[.]cn 的 MQTT 服务器下载无界面恶意 APK「JarService」，解密执行二级加载器连接 C2 并周期上报设备信息；最终载荷加载名为「zhima」的反向代理模块，将车机变为住宅代理节点并从事点击欺诈。这是首例专门针对车载头单元的恶意感染链，Kaspersky 已通知 DoFun，后者称已修复；提醒汽车 IoT 固件供应链与默认 MQTT 通道成为新型变现/僵尸网络入口。

Incus 容器管理器七连发严重漏洞（含 CVE-2026-48755，CVSS 9.9，公开 PoC）

📰 Enigma Global / GitHub lxc/incus · 📅 2026-08-22

Incus（开源容器/VM 管理器，github.com/lxc/incus）同期披露七枚严重漏洞，其中 CVE-2026-48755 为备份压缩参数注入（CWE-88），可链式 CVE-2026-48769/62867/62940/62941 提权，公开 PoC 已可用；另有 CVE-2026-63125（镜像 backup.yaml 符号链接攻击，项目级权限即可 root 执行）等。攻击仅需项目级 can\_create\_images/can\_create\_instances 权限，多租户环境下容器逃逸即宿主机完全沦陷——系统性安全审查暴露的集群缺陷使容器隔离模型在被修复前视为已被击穿，使用 Incus 做多租户隔离的团队应视其为紧急补丁事件。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 5 条 |

CVE-2026-76604CVSS 10.0

**受影响产品：**Fabrik 扩展 for Joomla（fabrikar.com），所有 < 4.7.3 版本（含 1.0.0 起全部历史版本）；Joomla 4.2+/5.1+ 站点广泛安装，常暴露于公网的表单/数据构建组件

**漏洞描述：**未认证远程代码执行（CWE-94 代码注入）：Fabrik 的 PHP 表单元素（form element）在解析模型生成的工具调用/表单参数时，将攻击者可控输出直接传入 PHP 代码执行路径，攻击链为「暴露的 com\_fabrik 前端端点 → 构造恶意表单/工具调用参数 → 未认证 RCE → 服务器任意 PHP 代码执行 → 整服沦陷」。同集群 CVE-2026-76605（图像元素 CWE-94 RCE）、CVE-2026-76606（图像元素 CWE-22 路径遍历）、CVE-2026-76607（下载插件缺失访问检查）、CVE-2026-77992（calc 元素 heredoc 逃逸 9.5）均无需认证

**利用状态：**CVSS v4 10.0（AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H）；尚无确认在野利用，但未认证+满分 CVSS 使其成为自动化扫描优先目标，攻击复杂度极低、网络可达、无需用户交互；互联网暴露的 Joomla+Fabrik 实例即时面临风险  ·  **补丁状态：**升级至官方最新 4.7.2 重发构建（部分第三方公告以 4.7.3 为修复分界，建议直接安装 fabrikar.com 最新构建并重新下载校验）；临时缓解：① 收敛 com\_fabrik 前端端点公网暴露 ② WAF 拦截异常表单/工具调用参数 ③ 监测 web 日志中针对 com\_fabrik 的异常请求 ④ 对受影响站点假设已暴露并审计

CVE-2026-77946CVSS 10.0

**受影响产品：**TRENDnet TEW-821DAP 无线接入点，固件 2.2.01b05（组件：NTP 时区配置处理器 /cgi-bin/apply\_time.cgi）；大量 SOHO/分支网络边缘设备，常因远程管理暴露于公网

**漏洞描述：**栈溢出远程代码执行（CWE-121/119）：uci\_safe\_get 函数读取用户可控 UCI 配置参数后，以无边界拷贝写入固定大小栈缓冲区，攻击链为「构造超长 HTTP POST 至 /cgi-bin/apply\_time.cgi（参数 system.ntp.server / enable\_server / cameo.time.time\_zone / cameo.cameo.syslog\_server）→ 溢出覆盖返回地址 → 以 root/服务权限任意代码执行 → 设备完全接管」

**利用状态：**CVSS v3.1 10.0（AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H）/ v4 9.3；公开 PoC 已可用，网络可达、未认证、无需用户交互、复杂度低；设备已 EOL，暂无官方补丁，预计将出现扫描利用  ·  **补丁状态：**暂无官方补丁；临时缓解：① 管理/配置接口（/cgi-bin/apply\_time.cgi 及相关 CGI）仅限可信内网 ② 禁用 WAN 远程管理、设备置于防火墙/VPN 后 ③ 监测针对时间/NTP 配置端点的异常 POST ④ 评估更换为受支持型号（相关硬件修订已 EOL）

CVE-2026-78050CVSS 9.9

**受影响产品：**Comfast CF-N1-S 无线接入点/路由器，固件 2.6.0.1（组件：Web 管理 NTP 时区接口 /cgi-bin/mbox-config?method=SET§ion=ntp\_timezone，函数 sub\_41AD7C）；SOHO/分支网络边缘设备

**漏洞描述：**栈溢出（CWE-121）：Web 管理 NTP 时区配置处理中，对参数 timestr/ntp\_client\_enabled 的操纵触发栈缓冲区溢出，攻击链为「构造畸形 HTTP 请求至 /cgi-bin/mbox-config NTP 时区接口 → 溢出栈缓冲区 → 远程代码执行或设备崩溃（DoS）」

**利用状态：**CVSS 9.9（Max，VulDB）；漏洞利用已公开，可远程发起、复杂度低；未认证、网络可达；与同厂商 CF-N1-S 其他栈溢出（CVE-2026-77148/77022）共同构成 SOHO 设备高危暴露面  ·  **补丁状态：**核查 Comfast 官方是否有 2.6.0.1 之后修复固件并尽快升级；临时缓解：① 收敛 Web 管理接口至可信网络 ② 禁用不必要的 NTP 时区 Web 配置 ③ 监测异常管理请求与设备异常重启 ④ 设备置于防火墙后、禁止公网 WAN 管理

CVE-2026-12710CVSS 9.3

**受影响产品：**Google Cloud Application Integration（托管云服务，承载企业系统集成与数据编排，客户无法直接打补丁）

**漏洞描述：**缺失授权（CWE-862 Missing Authorization）：QueryEngineTask 组件未正确校验调用者权限，外部攻击者无需认证即可访问敏感内部数据，攻击链为「外部请求 → QueryEngineTask 未授权访问 → 读取集成平台内部敏感数据」

**利用状态：**CVSS v4 9.3（AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:N）；网络可达、未认证、无需用户交互；Google 表示该问题已于 2026-04-04 服务端修复、客户无需任何操作，无公开 PoC  ·  **补丁状态：**作为托管服务由 Google 控制修复，客户侧无补丁版本；临时缓解：① 复核 Application Integration 数据流与最小权限配置 ② 审查集成连接器的数据访问范围 ③ 对跨系统集成启用异常访问告警与审计 ④ 规避「云侧漏洞+客户不可控」信任盲区，重要数据面做额外访问控制

CVE-2026-48755CVSS 9.9

**受影响产品：**Incus（github.com/lxc/incus）7.1.0 之前版本，用于容器与 VM 管理的多租户基础设施，容器逃逸即宿主机沦陷

**漏洞描述：**备份压缩中用户提供的压缩算法验证不当导致命令行参数注入（CWE-88 Argument Injection）：可任意写文件并升级为命令执行；关联漏洞 CVE-2026-48769/62867/62940/62941 可被链式利用，暴露面涉及备份导入流程

**利用状态：**CVSS 9.9；公开 PoC 可用，显著增加被利用可能性；多租户环境下容器逃逸直接导致宿主机完全沦陷；远程可达  ·  **补丁状态：**升级至 7.1.0 或更高（建议 7.3.0+ 修复同集群符号链接等缺陷）；临时缓解：① 审计备份导入流程对压缩算法的校验 ② 以非 root 用户运行 incus ③ 隔离多租户工作负载 ④ 监控宿主机异常文件写入与异常进程

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

mySites.guru — Fabrik 4.7.2 安全发布解析：Joomla 扩展未认证 RCE/路径遍历/SQLi 集群根因与补丁核验

📰 mySites.guru · 📅 2026-08-23

【可学技术 — 流行 CMS 扩展漏洞集群的修复核验与资产清点】mySites.guru 拆解 Fabrik 4.7.2 重发安全更新：四枚 CVSS 4.0 10.0（CVE-2026-76604/76605 未认证 RCE、CVE-2026-76606 图像元素路径遍历、CVE-2026-76607 下载插件缺失访问检查）、CVE-2026-77992（calc 元素 heredoc 逃逸 9.5）及两枚 SQLi（9.3）全部未认证。可学要点：① 为何 4.7.2 被多次「同版本号重发」导致版本识别混乱、须重新下载校验而非依赖已报版本号 ② 用扩展 inventory 工具对全量 Joomla 站点批量标记受影响 Fabrik 版本（替代逐站人工核查）③ Joomla 3 站点无法安装 Fabrik 4 且无补丁、须手动源码补丁或迁移的处置路径 ④ 对 CMS 扩展建立「版本重发追踪 + 受影响面清单」的常态补丁核验 SOP。

ajking.io — AI 生成漏洞利用脚本 targeting Siemens S7 PLC（AA26-231A）+ BTR 驱动武器化内核级 EDR 删除

📰 ajking.io · 📅 2026-08-23

【可学技术 — OT/ICS 攻击检测映射与合法驱动滥用取证】ajking.io 威胁简报给出两条可学技术链：① NSA/CISA/FBI/DOE/EPA 五部门联合公告 AA26-231A——伊朗背景行动者用 AI 生成的 Python 利用脚本（snap7.dll/python-snap7 库，经 S7comm TCP 102）对 S7-200/300/400/1200/1500（含 F 系列安全控制器）做读/写访问，附完整 ATT&CK(ICS) 映射（T0834/T0893 横向、T0821/T0893 数据操纵、T1596.005 侦察）与检测规则缺口（Splunk/Elastic/Sigma 均无 S7comm snap7 伪装规则）→ 安全团队可据此补齐 OT 协议异常检测；② Check Point Black Hat 2026 演示 Microsoft Defender 合法签名驱动 BTR.sys 被武器化（注册含 :changelist 的 rogue 服务键，启动期 Ring 0 删安全软件，无 CVE、无补丁）→ 可学 Sysmon Event ID 6/13 检测 BTR.sys 异常加载与 :changelist 注册表写入。

BleepingComputer — MoYu/BadBox 车载 Android 头单元供应链投毒：JarService 无界面负载 + MQTT C2 + zhima 反向代理取证

📰 BleepingComputer / Kaspersky · 📅 2026-08-23

【可学技术 — IoT/车机供应链感染链的恶意负载与 C2 取证】Kaspersky（经 BleepingComputer 报道）逆向 MoYu 组织针对 DoFun 车机 Android 头单元的供应链攻击：合法系统应用 TWCore 从 cardoor[.]cn 的 MQTT 服务器下载无界面 APK「JarService」，解密执行二级加载器连接 C2 并周期上报 model/分辨率/SSID/MAC，最终加载「zhima」反向代理模块将车机变为住宅代理节点并从事点击欺诈。可学要点：① MQTT 物联网通道作为 C2 的识别与流量基线 ② 无界面 APK + 二级加载器 + 周期性设备信息上报的 IOC 结构 ③ zhima 反向代理模块将 IoT 设备武器化为代理节点的变现模式与检测（异常出网/代理流量）④ 对车机/ IoT 固件供应链建立「合法系统应用→可疑下载域名→无界面负载」的溯源与信任校验。

|  |  |  |
| --- | --- | --- |
| 🛠️ | 安全工具动态 | 3 条 |

projectdiscovery/nuclei — 高速模板化漏洞扫描器（含 CVE 模板，用于核验 Fabrik/TRENDnet/Comfast/Zimbra 暴露面）

📰 GitHub（ProjectDiscovery） · 📅 持续维护

开源、基于 YAML 模板的漏洞/暴露面扫描器（Go），通过 nuclei-templates 社区库覆盖大量 CVE 检测模板，支持对资产清单批量探测今日重点漏洞（Fabrik com\_fabrik 端点、TRENDnet/Comfast NTP/Web 管理 CGI、Zimbra 邮件端口、Incus 等）并输出...