---
title: 跨租户Teams服务台钓鱼到数据外传：一次人工入侵全链路剖析
url: https://mp.weixin.qq.com/s/Q9UetMo0E-2p8G2Fv5uaag
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:41.727936
---

# 跨租户Teams服务台钓鱼到数据外传：一次人工入侵全链路剖析

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYAvD4XL7zOlTJ18bzr3CiaGQEBhLQKBzoSc1QTibrv3ypttvuv22l9sCPLA1PeuBY0GrQKmDB0HW4m9gmiawCMJtBzhoO7qzNWtib0/0?wx_fmt=jpeg)

# 跨租户Teams服务台钓鱼到数据外传：一次人工入侵全链路剖析

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

攻击者正通过跨租户 Microsoft Teams 通信冒充 IT 或服务台人员，诱骗用户授予远程桌面访问权限。获取访问权限后，攻击者利用受信任的签名应用和原生管理协议（WinRM）进行横向移动，最终使用 Rclone 将数据外传至云端存储。

本文基于微软安全团队的真实入侵案例，深度剖析这一攻击链的每个阶段，并提供完整的 KQL 检测查询和防御建议。

────────────────

攻击概览：为何这种攻击尤其危险

攻击者不再依赖传统的邮件钓鱼，而是直接通过 Microsoft Teams 跨租户通信发起攻击。由于交互发生在企业协作平台内，用户对非预期外部通信的初始戒备心理会大幅降低。虽然 Teams 内置了外部发送者标记和"接受/阻止"提示等安全功能，但这种攻击链的核心在于说服用户忽略这些警告，自愿授予远程访问权限。

**关键风险：**一旦用户批准了外部 Teams 交互，攻击者即可建立凭据支持的交互式系统访问、部署受信任应用执行攻击者控制的代码、使用 WinRM 向身份和域基础架构横向移动、部署商业远程管理工具，以及将敏感业务数据暂存至外部云基础架构。

攻击链全景

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYBu10vCJmWvZRibeOWuvA9wcUD7sLugL0BmrlkicQY7LOP9j0HHibEOTtAlQSjs9icmRW2DNrTr0a0t0EeRnb0EDH2WQxpWAibibjwtM/640?wx_fmt=png)

第一阶段：通过 Teams 建立初始联系

**MITRE ATT&CK: T1566.003 — 通过服务进行鱼叉式钓鱼**

攻击始于对 Microsoft Teams 外部协作功能的滥用。攻击者从另一个租户发起联系，冒充内部支持人员对用户进行社会工程。由于交互发生在企业协作平台而非传统邮件钓鱼渠道，用户对非预期外部通信的戒备心理会显著降低。

常见的诱饵话术包括："微软安全更新"、"垃圾邮件过滤器更新"、"账户验证"等，但目标始终一致：说服用户忽略警告和外部联系标志，启动远程管理会话并接受权限提升。有时攻击者还会叠加语音钓鱼（vishing）来增强信任感。

**时间线信号：**"ChatCreated" 事件标志着首次联系，随后会出现可疑聊天或语音钓鱼、远程管理等事件，这些事件在 Defender 检测环境中可以通过账户和聊天线程信息进行关联。

值得注意的是，攻击者通常不会通过 Teams 消息发送 URL，而是在远程管理会话期间直接在终端上导航到恶意链接。因此，最有效的防御是用户教育——让用户理解不要忽略外部标志的重要性。

第二阶段：获取远程协助访问权限

通过社会工程获取用户同意后，攻击者使用 Quick Assist 等远程支持工具获得设备的交互控制权。这通常表现为 QuickAssist.exe 启动，随后通过 Consent.exe 显示标准 Windows 权限提升提示。

从用户视角来看，攻击者说服他们打开 Quick Assist、输入短代码，然后按照所有提示和审批步骤授予访问权限。整个过程通常在不到一分钟内完成。

**检测信号：**远程协助进程树后立即在同一桌面上出现 cmd.exe 或 PowerShell——紧迫性和交互性本身就是信号。

第三阶段：交互式侦察与访问验证

通过 Quick Assist 建立控制后，攻击者通常在最初的 30-120 秒内评估其访问级别和受陷环境。这通常表现为 cmd.exe 活动激增：验证用户上下文和权限级别、收集主机身份和操作系统等基本信息、确认域隶属关系。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYBSohgEejBwlO7k9UMddA9d1YtRDlISCv05GptRUJIFGN8e63ttAqy49Yrian9wtHFnujIdicia1237mV0icdK1VMiaDj28uPzBZMyU/640?wx_fmt=png)

在权限受限的系统上（如信息亭、VDI 或非企业域加入的设备），攻击者可能仅留下简短的侦察活动而不部署有效载荷，等到访问权限改善时再返回。

第四阶段：有效载荷投放与可信应用调用

建立远程访问后，攻击者使用归档部署或短暂脚本活动将有效载荷暂存到磁盘，并通过 DLL 侧加载在受信任签名应用下执行。已观察到的侧加载组合包括：

AcroServicesUpdater2\_x64.exe 加载 msi.dll
ADNotificationManager.exe 加载 vcruntime140\_1.dll
DlpUserAgent.exe 加载 mpclient.dll
werfault.exe 加载 Faultrep.dll

这使得攻击者提供的模块能够在来自非标准路径的受信任执行上下文中运行。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYBprsQhnNlm3p7tq3bvOQGsTMIqYfZfoUXFNbLntcN7VqDBwxR0l9MOXYPrQYQTKURibT5sfD4cGHjr6Acd8NQHvsnIywXibxqR8/640?wx_fmt=png)

第五阶段：执行上下文验证与注册表持久化

有效载荷投放后，攻击者执行运行时检查以验证主机条件。随后将大型编码值写入用户上下文注册表位置，作为加密配置数据的暂存容器。侧加载的中间加载器在内存中解密暂存的注册表数据，重建执行和 C2 配置，而无需在磁盘上写入文件。

这种行为与 Havoc 等入侵框架一致——将加密配置外部化到注册表存储，允许受信任的侧加载组件动态恢复执行上下文，即使遭遇重启或修复事件也能维持运行连续性。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYAwgyeOkkN1ow0bN1VZ78Qmhd1mcZCiauxK8CRxocibSIRLN4ZiaVBaktJaPnOn7Fe2Q7WujrKpUicTa1awk40KHCHUoKIUEPqGMd4/640?wx_fmt=png)

第六阶段：命令与控制通信

侧加载组件成功执行后，以更新器为主题的 AcroServicesUpdater2\_x64.exe 进程开始通过 TCP 443 端口发起出站 HTTPS 连接，连接至外部托管的基础架构。

与预期的应用更新工作流不同，这些连接指向动态托管的云端端点和未知外部域。这表明通信基础设施由攻击者远程控制，而非合法更新机制。使用云托管层进一步降低了基础设施可见性，使攻击者能够在不修改已部署有效载荷的情况下修改或轮换通信端点。

第七阶段：内部发现与横向移动

外部通信建立后不久，受陷进程开始通过 WinRM（TCP 5985）向企业环境中的其他域加入系统发起内部远程管理连接，最终目标包括域控制器等身份和域管理系统。

**技术细节：**攻击者使用非管理应用发起 WinRM 会话，表明这是由外部操作员指示的凭据支持的横向移动。这使得攻击者能够远程执行命令、与域基础架构交互，并将额外工具部署到目标主机上。

第八阶段：远程部署辅助访问工具

后续活动显示攻击者使用 Windows Installer（msiexec.exe）跨受陷主机远程安装了额外的管理平台。这引入了独立于原始入侵组件的替代控制通道，降低了对初始植入物的依赖，即使早期有效载荷被中断或删除，攻击者仍能通过标准管理机制维持持久远程控制。

第九阶段：数据外传

攻击者使用文件同步工具 Rclone 将数据从内部网络位置传输到外部云存储服务。传输参数中的文件类型排除设置表明，攻击者有针对性地外传业务相关文档，同时最小化传输大小和检测风险。

────────────────

防御与缓解建议

**1. Microsoft Teams 安全策略**
审查外部协作策略，确保用户在与跨租户联系人交互时收到清晰的外部发送者通知。考虑在授予远程支持会话前要求基于设备或身份的访问条件。

**2. Microsoft Defender for Office 365**
为 Teams 对话启用 Safe Links（带点击时验证），并确保零小时自动清除（ZAP）处于活动状态，以追溯隔离被武器化的消息。

**3. Microsoft Defender for Endpoint**
禁用或将远程管理工具限制为授权角色，以阻止模式启用标准 ASR 规则，应用 WDAC 防止从 ProgramData 和 AppData 路径进行 DLL 侧加载。

**4. Microsoft Entra ID**
强制实施条件访问策略，要求管理角色使用 MFA 和合规设备，将 WinRM 限制为授权管理工作站，并监控 Rclone 或类似同步工具的数据外传行为。

**5. 用户教育**
建立内部服务台认证口令，让员工了解 IT 服务台的正常联系方式（通信媒介、域名、别名、电话号码等），展示如何区分外部和内部 Teams 通信，以及如何识别显示名称与真实来电者信息的差异。将任何未经请求的外部 IT 服务台联系视为固有可疑行为。

────────────────

KQL 威胁狩猎查询

微软安全团队提供了多条 KQL 查询，帮助安全团队主动发现此类攻击的指标。以下为核心查询：

**A. Teams → RMM 工具关联查询**
关联 MessageEvents 和 DeviceProcessEvents 表，查找 Teams 消息后 30 分钟内 Quick Assist/AnyDesk/TeamViewer 启动事件，通过 VictimAccountObjectId 进行内连接。

**B. 执行检测**
DeviceProcessEvents | where FileName =~ "cmd.exe" | where ProcessCommandLine has\_all ("/S /D /c", "\" set /p=\"PK\"\"", "1>")

**C. ZIP → ProgramData → 签名宿主侧加载关联**
关联 DeviceFileEvents（ProgramData 下 ZIP 创建）和 DeviceProcessEvents（AcroServicesUpdater2\_x64.exe/DlpUserAgent.exe/ADNotificationManager.exe 启动），时间窗口 10 分钟。

**D. PowerShell → 高风险 TLD → AppData EXE 写入**
检测 PowerShell 访问 .top/.xyz/.zip/.click 域后 5 分钟内向 AppData\Roaming 写入 .exe 文件的行为。

**E. 注册表 ASEP 异常检测**
监控 SOFTWARE\Classes\Local Settings\Software\Microsoft 下 UCID/UFID/XJ01/XJ02/UXMP 等注册表值名的变化。

**F. 非浏览器进程 → API Gateway → 内部 AD 协议**
检测非浏览器进程先连接 .execute-api. 域名，10 分钟内再发起端口 135/389/445/636 连接的行为。

**I. 数据外传检测**
DeviceProcessEvents | where FileName =~ "rclone.exe" | where ProcessCommandLine has\_all("copy ", "--config rclone\_uploader.conf", "--transfers 16", "--max-age=3y", "--exclude \*.mdf")

────────────────

MITRE ATT&CK 技术映射

|  |  |  |
| --- | --- | --- |
| 战术 | 技术 ID | 技术名称 |
| 初始访问 | T1566.003 | 通过服务进行鱼叉式钓鱼 |
| 执行 | T1059.001 | PowerShell |
| 防御规避 | T1574.002 | DLL 侧加载 |
| 横向移动 | T1021.006 | Windows Remote Management |
| 命令与控制 | T1071.001 | Web 协议 |
| 数据外传 | T1567.002 | 通过云存储外传 |

────────────────

**来源：**Microsoft Security Blog
**发布日期：**2026年4月18日
**作者：**Microsoft Defender Security Research

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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