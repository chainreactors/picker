---
title: 7月15日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/Glwk6X_Akq3BtXaUeSslkQ
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:55:53.535802
---

# 7月15日高危CVE漏洞速报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nZrMrH4FF0JPA3uf0FSpJGQ52g3w5rovhzhfTiaXkbD7kB4CBEYxSxb7t8wiaCmMshC9iaatPxKMkngqmbxO8OFAxlroicUR2FzZicOI6r4aTO94/0?wx_fmt=jpeg)

# 7月15日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危预警

# 【安全速报】07月15日高危漏洞紧急预警

2026年07月15日  |  探知安全

微软7月补丁星期二修复570+漏洞创纪录，SharePoint双满分RCE+2个在野零日正被勒索软件积极利用；SonicWall SMA1000 VPN双漏洞CISA KEV紧急新增，未认证SSRF直通内网；Edge V8类型混淆CVSS 9.0亟待更新；Windows Print Spooler严重RCE再次成为攻击入口；Linux KVM Januscape潜伏16年虚拟机逃逸漏洞完整利用链已证实，请立即排查修复。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58644 / 56164 | CVSS 9.8 |

### 微软7月补丁星期二：570+漏洞修复创纪录，SharePoint满分RCE双漏洞+2个在野零日（CISA KEV紧急新增·勒索软件积极利用）

微软2026年7月补丁星期二（7月14日发布）一口气修复约570个安全漏洞，是上月206个漏洞的近三倍，打破单月补丁记录。其中两个零日漏洞已确认在野利用：CVE-2026-56164针对SharePoint Server实现未认证权限提升（CISA KEV 7/14新增），攻击者无需任何凭据即可通过网络提升至系统最高权限；CVE-2026-56155针对ADFS活动目录联合身份验证服务，允许本地攻击者提升权限至域管理员级别，可横向移动至整个企业身份信赖链（CISA KEV 7/14新增）。两个严重级RCE漏洞均为CVSS 9.8满分：CVE-2026-58644是SharePoint Server远程代码执行，CVE-2026-50522同样是SharePoint Server RCE，两者均可被未认证攻击者通过网络低复杂度利用，微软评估「利用可能性高」。第三个公开零日CVE-2026-50661为BitLocker安全功能绕过（公开PoC）。值得注意的是，攻击者正在将SharePoint EoP与RCE漏洞链式利用——先用RCE获取初始权限，再用EoP飙升至SYSTEM最高权限，整套自动化攻击脚本网络上数百美元即可买到。

影响范围

Microsoft SharePoint Server所有本地部署版本、ADFS活动目录联合身份验证服务、Windows BitLocker全盘加密；覆盖Windows操作系统、Office、远程桌面服务、Windows Admin Center等核心组件

修复建议：立即部署微软2026年7月安全更新；SharePoint本地部署农场优先安装CVE-2026-58644/50522/56164补丁；ADFS服务器立即安装CVE-2026-56155补丁；BitLocker用户安装CVE-2026-50661；备份数据后再应用补丁以防兼容性问题

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-15409 / 15410 | CVSS 9.8 |

### SonicWall SMA1000 VPN双漏洞集群：未认证SSRF直通内网+代码注入完全接管（CISA KEV 7/14紧急新增·在野利用确认）

CISA于7月14日将SonicWall SMA1000（Secure Mobile Access）安全远程访问设备中的两个漏洞紧急纳入已知利用漏洞（KEV）目录，确认正被活跃攻击利用，要求联邦机构3天内（7月17日前）完成修复。CVE-2026-15409是未认证服务器端请求伪造（SSRF）漏洞——攻击者无需任何凭据，即可诱骗SMA1000设备代表自己向内部系统发起请求，直接绕过网络边界访问内网资源。CVE-2026-15410是Appliance Management Console（AMC）中的代码注入漏洞（CVSS 7.2），允许已认证管理员执行任意操作系统命令。两个漏洞可串联使用：远程攻击者先利用未认证SSRF打通内网通道，再联合代码注入实现设备完全接管。SMA1000是企业对外暴露的VPN安全网关，部署在公网边界，一旦沦陷攻击者即直接进入内网。今年SonicWall VPN设备已多次成为勒索软件攻击的首选入口，本次在野利用确认后修补窗口极短。

影响范围

SonicWall SMA1000系列所有固件版本（修补前版本）；企业VPN远程访问网关，公网暴露设备达数万台级别

修复建议：立即升级SMA1000至最新修补固件版本；审计所有管理账户是否存在异常登录和配置变更；排查AMC日志是否存在可疑命令执行记录；轮换管理员凭据；如无法立即可限制管理接口仅内网白名单访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58289 | CVSS 9.0 |

### Microsoft Edge V8引擎类型混淆远程代码执行（CVSS 9.0·微软二次评分无用户交互·浏览即沦陷）

微软于7月3日披露了Edge浏览器（Chromium内核）中V8 JavaScript引擎的类型混淆RCE漏洞，CVSS评分9.0。该漏洞存在于V8引擎的JavaScript对象类型标记检查逻辑中：引擎在处理对象类型转换时错误地将一种类型的对象当作另一种类型访问，导致攻击者可实现任意内存读写原语——先泄露内存布局绕过ASLR，再覆写函数指针劫持执行流。微软内部二次评分为CVSS 9.0（AV:N/AC:H/PR:N/UI:N/S:C），评估为无需用户交互即可远程触发；NVD评分略微保守为8.3（需用户交互）。攻击者仅需诱导受害者访问特制恶意网页即可完全控制Edge渲染进程，若结合沙箱逃逸可进一步渗透至操作系统层。Edge 150.0.4078.48已于7月2日修复。此漏洞影响所有安装Edge的Windows/macOS/Linux平台，包括企业大量管理终端。补丁发布后24小时内极有可能被逆向工程并开发自动化利用工具。

影响范围

Microsoft Edge (Chromium) < 150.0.4078.48，覆盖Windows 10/11、Windows Server、macOS、Linux全平台（企业桌面环境广泛使用）

修复建议：立即更新Microsoft Edge至150.0.4078.48或更高版本（edge://settings/help强制检查更新）；企业管理员通过Microsoft Update Catalog或Edge for Business MSI批量部署；启用浏览器自动更新策略确保后续安全补丁及时生效

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58608 | CVSS 9.8 |

### Windows Print Spooler打印后台处理程序严重远程代码执行（Critical·微软7月补丁·勒索软件经典攻击入口）

微软7月补丁星期二中两个标记为「严重」等级的漏洞之一：CVE-2026-58608影响Windows Print Spooler打印后台处理程序服务，可实现远程代码执行。Print Spooler是Windows系统中处理打印作业的核心服务，默认在所有Windows版本中运行且经常暴露于企业网络环境中。该品类漏洞一直是勒索软件团伙和国家黑客的心头好——从2010年Stuxnet利用打印服务传播，到2021年PrintNightmare（CVE-2021-34527）全球蠕虫级攻击，再到2024年PrintJack（CVE-2024-21433），Windows打印服务已成为最危险的横向移动入口之一。攻击者成功利用后可获取SYSTEM级权限，在域环境中横向跳转至域控制器，最终部署勒索软件载荷。该漏洞与CVE-2026-58644（SharePoint RCE）并列为本月最优先修补的两个严重漏洞。

影响范围

Windows 10/11所有版本、Windows Server 2019/2022/2025（Print Spooler服务默认启用，企业域环境中广泛运行）

修复建议：立即安装微软2026年7月安全更新；在不需要打印服务的服务器上通过组策略禁用Print Spooler服务（Stop-Service Spooler -Force; Set-Service Spooler -StartupType Disabled）；域控制器必须优先修补；部署PowerShell脚本批量检测和修复域内所有Windows主机

|  |  |  |
| --- | --- | --- |
| 高危 | CVE-2026-53359 / 46113 | CVSS 8.8 |

### Linux KVM Januscape：潜伏16年释放后使用虚拟机逃逸漏洞（双CVE补丁·云主机宿主机崩溃+根级逃逸验证）

2026年7月6日公开披露的Linux内核KVM虚拟化层Use-After-Free漏洞，编号CVE-2026-53359，潜伏代码库长达16年之久。该漏洞位于KVM内存管理子系统的阴影页表处理代码中，恶意客户机虚拟机（VM）可触发竞态条件破坏宿主机内核内存状态，实现两种攻击路径：一是导致宿主机内核恐慌崩溃（DoS），PoC可在数秒内从客户机内部可靠触发，使同一物理主机上所有其他客户机瞬间宕机；二是完整的虚拟机逃逸——研究员Hyunwoo Kim已在受控环境中证实可利用该漏洞从客户机获取宿主机root权限，虽然完整利用代码未公开但技术可行性已确认。更危险的是在RHEL/CentOS/AlmaLinux等发行版中，KVM设备节点/dev/kvm默认以0666（世界可读写）模式分发，任何非特权本地用户均可访问触发该漏洞。完全修复需同时应用CVE-2026-53359和配套CVE-2026-46113两个补丁，仅应用其中一个补丁将使系统仍处于部分暴露状态——这一细节常被企业运维忽视。所有基于KVM的x86云基础设施管理员均应将其视为紧急修补窗口。

影响范围

Linux内核KVM虚拟化子系统（受影响版本广泛，RHEL/CentOS/AlmaLinux/Ubuntu/Debian等主流发行版；所有基于KVM的公有云、私有云和虚拟化平台）

修复建议：立即应用CVE-2026-53359和CVE-2026-46113两个补丁（7月4日已合并至主线内核，缺一不可）；检查内核版本确认两个补丁均已生效；在未修补前限制非受信用户对/dev/kvm的访问权限（chmod 660 /dev/kvm）；云服务商应优先修补宿主机内核

紧急提醒

本期是微软7月补丁星期二特刊，570+漏洞修复破历史纪录，57个严重级别漏洞、3个零日漏洞正在被勒索软件和国家级攻击者积极利用。SharePoint满分RCE（CVE-2026-58644/50522 CVSS 9.8）+在野EoP（CVE-2026-56164）链式攻击已成套自动化武器，非认证攻击者可直接接管企业SharePoint服务器并飙升至SYSTEM权限。SonicWall SMA1000 VPN网关双漏洞（CVE-2026-15409/15410）CISA KEV紧急新增，3天修复窗口。Edge V8类型混淆CVSS 9.0浏览即沦陷、Print Spooler严重RCE再次成为经典攻击入口、Linux KVM潜伏16年虚拟机逃逸漏洞云基础设施全面告急——请安全团队将SharePoint和Print Spooler补丁排在最优先级，本周内完成全量修复。

处置建议

① 所有Microsoft SharePoint本地部署农场立即安装7月安全更新，CVE-2026-58644/50522/56164三级补丁一并应用

② ADFS身份验证服务器立即安装CVE-2026-56155补丁，审计域内身份认证日志排查异常Token签发行为

③ SonicWall SMA1000用户立即升级到最新固件，审计管理账户和配置变更，轮换所有管理员凭据

④ 所有Microsoft Edge浏览器立即更新至150.0.4078.48+，企业管理员通过WSUS/SCCM批量推送

⑤ Windows域环境立即安装7月安全更新，域控制器和不需打印的服务器禁用Print Spooler服务

⑥ Linux KVM虚拟化宿主机必须同时应用CVE-2026-53359和CVE-2026-46113双补丁，云服务商优先修补

觉得有用？点击右下角**在看**，让更多人看到

探知安全 · 每日推送最新漏洞资讯

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ayPnpNqYCJKbeG52l1HMrttVrHhaGYKtDOWalO9FcwwVTzzCKhpg0BEKR4eZdo8JXdrv6n8RZAOgtnmcEPgvHg/0?wx_fmt=png)

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