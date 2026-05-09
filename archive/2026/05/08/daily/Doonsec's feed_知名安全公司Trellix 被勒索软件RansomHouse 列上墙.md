---
title: 知名安全公司Trellix 被勒索软件RansomHouse 列上墙
url: https://mp.weixin.qq.com/s/MDHbOs1qDsp9fUG0gQHSnA
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:04:31.786469
---

# 知名安全公司Trellix 被勒索软件RansomHouse 列上墙

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAg4e34jmq6MWwVjTW89nlPoZyZzgPUY3qKRZWvbVjTKM6Ytp4Was4xljqvcwHa1WPUB3g17SKNmEZYsvguJSAjJE7Js9m5nfko/0?wx_fmt=jpeg)

# 知名安全公司Trellix 被勒索软件RansomHouse 列上墙

原创

独眼情报
独眼情报

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAgMmiawtoLgibPicNjNB5KLd6opGsvBbus6sGORQ4sPrWAyKD2GMvUc40OOhFtKlctria8gv0LxRv3FMZyHpL65licpWmhrL86Nc1ib8/640?wx_fmt=jpeg&from=appmsg)

## 长话短说

2026 年 5 月 7 日，勒索组织 RansomHouse 在其暗网泄漏站点将网络安全厂商 Trellix（由卖咖啡和火眼 2021 合并而成，出生自带光环） 列为受害者，并发布多张声称来自 Trellix 内部的截图，覆盖 vSphere 虚拟化集群、Rubrik 备份控制台、Dell EMC Data Domain 存储管理界面，跨域名涉及 `corp.entsec.com`、`fireeye.com`、`eng.fireeye.com` 三个集合。Trellix 官方声明承认「源代码仓库的一部分」遭未授权访问，已通知执法部门并启动外部取证调查；截至声明发布时，未发现源代码发布或分发流程受影响，也未发现源代码被利用。

**研判**：这是一次值得高度关注的事件，但**当前公开证据不支持把它定性为大规模、系统性入侵**。三点理由：

* 第一，Trellix 措辞极度克制（「源代码仓库的一部分」），与 RansomHouse 截图所示的基础设施可见性之间存在叙事落差；
* 第二，RansomHouse 是「数据窃取 + 双重勒索」型组织，发上墙意味着勒索谈判失败或从未达成，攻击者倾向把「访问截图」的视觉冲击力最大化；
* 第三，Trellix 与 RansomHouse 之间存在历史结怨——Trellix 2024 年 2 月发布 *RansomHouse am See* 揭露过该组织的 ESXi 攻击工具 MrAgent，本次攻击不能排除报复属性。

如果你是 Trellix 客户，目前**没有**证据表明需要紧急停用 Trellix 产品；但应进入供应链风险观察期，跟踪 Trellix 后续披露，重点关注是否涉及客户遥测数据、检测规则、签名或构建工具链。如果你是其他安全厂商，这是一次极好的「灯下黑」案例研究——把它作为内部红蓝演练素材，比作为外部传播谈资更有价值。

## 时间线

时间精确到日，时区为 UTC。

| 日期 | 事件 |
| --- | --- |
| 2024-02-14 | Trellix 发布 *RansomHouse am See* 研究文章，详解 RansomHouse 的 ESXi 攻击工具 MrAgent |
| 2026-04-17 | RansomHouse 在暗网帖子中声称攻陷 Trellix 的实际日期 |
| 2026-05-01 | Trellix `/statement/` 页面 meta 时间戳更新（最后修改时间） |
| 2026-05-02 前后 | Trellix 在官网首次发布事件声明；The Hacker News 同期跟进报道 |
| 2026-05-07 | RansomHouse 在其暗网 DLS 列入 Trellix，发布截图 |
| 2026-05-08 | 多家媒体报道 RansomHouse 正式认领 |

**时间线缺口**：

* 入侵实际起点不详。RansomHouse 声称的 4 月 17 日仅来自其暗网帖子。
* Trellix 何时发现入侵不详，声明只用已识别到，但未给出具体日期。
* Trellix 声明发布日与 RansomHouse 上墙日之间相隔约 5–6 天——通常意味着勒索谈判窗口已关闭。

## 已确认事实：Trellix 承认「部分源代码仓库」遭未授权访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgfmYaf6MKMGr1zpQx4qfLG9P6mbf3TZOjfPxgEaZrrAqia61oLE80mSkQniblOoq0g8ALSpdT8lDRg5eJueaSOCu9uVZ8cdKZics/640?wx_fmt=png&from=appmsg)

Trellix 官网声明的核心信息很短：公司最近发现攻击者未授权访问了「一部分源代码仓库」；发现后立即与外部取证专家合作处理，并通知执法部门；截至当前调查，没有发现源代码发布或分发流程受影响，也没有发现源代码被利用。Trellix 还表示，调查完成后会在适当情况下分享更多细节。

声明里的措辞值得逐字解读。它说的是源代码仓库；不是「生产环境」「客户数据平台」「更新服务器」或「签名基础设施」已经被攻陷。它还说「目前没有证据表明」——这是事件响应语境中的审慎表达：不是最终排除，而是当前调查阶段的结论。

The Hacker News 在 5 月 2 日报道了 Trellix 的源代码仓库未授权访问事件，并指出 Trellix 没有披露攻击者访问了哪些具体数据、攻击者是谁、访问持续多久；该报道随后更新称 5 月 7 日 RansomHouse 宣称对此负责。RansomHouse 已在泄露站点将 Trellix 列为受害者，并发布多张截图试图证明其访问过 Trellix 内部服务和管理仪表盘；但该组织没有说明窃取了多少数据，也没有明确说明窃取的数据类型。

最稳妥的现状描述是：**Trellix 承认源代码仓库遭未授权访问；RansomHouse 宣称负责并发布了疑似内部管理后台截图；但公开层面尚未看到完整的数据包、源代码样本、CI/CD 凭据、签名密钥或客户数据泄露证据。**

## 截图素材的技术核读

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgt9H6n1Q0fNHUbFkcUuu1kXYibO0VjUHiaDsLhBuIS6AAbYtlVxPu10HOfx0eCXOuywEcJkpgOXHtw0VOSBISRVxicWu9QRUT9fs/640?wx_fmt=png&from=appmsg)

RansomHouse 在 DLS 上发布的截图共 7 张。逐张拆解：

**Rubrik 备份管理控制台（2 张）**

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjDXmT4s0qck5ibfIxaMkiczVQKOPaVbtZnVo7iazZ9ZsEzY4YrAVmBbN6zF97iaBOhGicJqibiamPbYS2icPvBMluWUGYNDDCwQgzvNrA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAhv23myEdXo1Srb6dmPWOthnIdv27WtXZEVP82f2xcC8Q1zBL7wSAoO635OWCClyicpSwrwvf22C9ibfEoEGlvwq5NA7uhIjxKxw/640?wx_fmt=png&from=appmsg)

* `IAD1_RBK_C01` 集群：3 个 vCenter / 3737 个虚拟机，登录用户 `Krishnan.N-TA`
* `blr_rbk_c01` 集群：4 个 vCenter / 2431 个虚拟机，登录用户同上

`IAD` 通常对应 Washington Dulles（美国弗吉尼亚州 Ashburn 一带的数据中心代码），`blr` 通常对应 Bangalore（印度班加罗尔），命名习惯反映跨地域多区域部署。Rubrik 的 Inventory 页面展示 vSphere VMs、Linux & Unix Filesets、Windows Filesets、SQL Server Databases、Oracle Databases、Active Directory 等资产类别。Rubrik 这类平台对勒索攻击者具有特殊价值，因为它直接关系受害者能否恢复业务——即便截图不证明攻击者能删除备份或发起恢复破坏，能够看到备份资产清单本身就足以增强勒索叙事。

**vSphere Client 虚拟化集群（3 张）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgdv5ibY6pwwtIdTd1SwrS2kwfnM6oAKnlgdA1kFyuChd85K5cc6aXEsOH16nERU9pmoVWnqVsWoYPxFNaqibY9iaB0wOI5iczf1yE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaDr8n7ianicQGzfdkCGRGwHibpgtUW0umNyob3YibgCFpGZ4OI5iaYiaKicuj2xFyMJ4kYwibPCQSVx2WwuDG4E2Gvfyo9YVmHibicmiaznM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjnmSMuPYs63DDMUiaE4MSAFoJK296R1C1Vq2iaabibWwZ4p7GCdKSlPcWGdibd8sl8npeBMQwKOHpIN7fOZE6JnAz4DpJCR7iczOMI/640?wx_fmt=png&from=appmsg)

* `DNVAPPVC5.corp.entsec.com`：26 个集群 / 99 台 ESXi 主机 / 1531 个虚拟机；CPU 容量 5.86 THz，存储容量 1267.95 TB
* `v-iad03-svcs01.fireeye.com`：3204 个虚拟机 / 30 台主机；活跃告警 3162 条
* `srv-eng-vcs02.eng.FireEye.com`：1001 个虚拟机 / 25 台主机；包含 `601-HIGH SECURITY CAGE` 文件夹（命名暗示高安全隔离区），并出现工程、实验室、模板、工具、恶意软件研究等文件夹结构

`fireeye.com` 是 Trellix 合并前 FireEye 时代的遗留域名。`entsec.com` 命名习惯类似「enterprise security」。**研判**：跨这三个域名集合的截图同时呈现，加上 Trellix 官方已经承认入侵，**倾向认为**这些资产确实归属 Trellix 当前或历史控制范围。vSphere 截图的威胁含义在于：攻击者想证明自己接触到虚拟化控制平面，而 vSphere 对企业内部横向移动、批量关停/加密虚拟机、导出 OVF 模板、定位高价值系统都非常关键。

**Dell EMC DD System Manager（2 张）**

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjHSibYkkibIzjaGNdib17YX7H4ia4GwzYeWJjUYMpVTf01KFY1G6KmhAcK8KdACSS66iabiclPzbvJ306tQicBC3ZJMRRBq5a4NLt00g/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAhy6SDR0ogKbroauIAsAqqUT0rMfwmiaib5Pzup6OeTtGg6ibvcvE6whfQE710iaEKLX20g5yRZ1ZfHsicHAD13fPEetCeETTYHu5ib4/640?wx_fmt=png&from=appmsg)

* `10.44.38.80`：File System 总容量 493.74 TiB / 已用 307.55 TiB
* `10.44.38.51`：File System 总容量 884.56 TiB / 已用 244.20 TiB

两台都登录用户 `CORP\kn1`，使用 AD 域账号。RFC1918 私网 IP（10.0.0.0/8）说明**这是从内部网络视角的截图，不是外部暴露资产**。Data Domain 是企业级去重备份存储设备，与上面 Rubrik 一起构成完整的「备份基础设施」。对勒索团伙而言，备份存储后台的截图往往比普通文件服务器截图更具心理压迫感，因为它暗示攻击者可能了解恢复链路。

**研判**：如果上述全部截图属实，攻击者展示的访问广度跨越**虚拟化、备份、备份存储**三个层面——这正是勒索组织摧毁恢复能力的「黄金三件套」。**但**仅有可见性截图不等于具备破坏性控制。截图中的登录用户 `Krishnan.N-TA`（Rubrik）和 `CORP\kn1`（Data Domain）都是普通运维账号，没有展示 root / domain admin 等更高权限的证据。Trellix 声明也没有提到任何 VM 加密、备份删除或业务中断——**这是支持「攻击未升级到破坏阶段」假设的关键证据**。

## 关键反差与截图的证明力

截图所呈现的是**基础设施可见性**（vSphere、Rubrik、Data Domain），但 Trellix 官方声明只提到**源代码仓库**被部分访问。两者不在同一系统层面。这是本次事件最值得关注的叙事落差。

两种解读：

1. 攻击者从某条入口横向移动到了基础设施层，但 Trellix 在声明中只承认其中影响最小、最可控的一段（源代码仓库）——**研判**：这是受害方淡化策略的常见模式，但目前没有独立证据证伪 Trellix 的说法。
2. 截图与源代码仓库分别属于两个不同的入侵阶段或访问路径，攻击者展示的截图未必反映其实际窃取数据的范围。

两种假设目前都不能排除，**待证实**。

截图本身的证明力既不能简单打成「真」也不能打成「假」。增强可信度的因素包括：多个不同后台类型且界面细节较丰富；出现 FireEye 遗留域名，与 Trellix 历史资产关系相符；部分页面带有具体资源数量、版本、构建号、近期任务、告警和时间戳；截图内容也与 SecurityWeek 报道的「内部服务和管理仪表盘」一致。

但截图仍不是完整证据：它无法证明攻击者当前仍有访问权限，无法证明其权限级别，无法证明数据已被成功外传，也无法证明其访问源代码仓库与访问这些管理后台属于同一条入侵链路。它也无法排除其他可能性，例如员工终端被信息窃取木马感染后泄露会话、第三方运维账号被盗、历史截图被复用、内部文档截图被窃取，或者攻击者只获得了只读视图。

合理结论是：**RansomHouse 展示的材料足以支持「至少存在内部可见性或内部材料获取」的判断，但不足以支持「Trellix 构建链已被控制」或「客户环境已被波及」的结论。**

## 为什么这件事敏感：安全厂商的源代码泄露不是普通代码泄露

安全厂商的源代码对攻击者的价值并不只在于「能不能直接编译产品」。更重要的是，源代码可能暴露检测逻辑、绕过点、内部 API、默认配置、测试样例、硬编码密钥、开发注释、历史漏洞修复方式，以及产品与云端服务之间的信任边界。Dark Reading 的分析也强调，源代码泄露可能让攻击者理解安全产品的控制点和检测机制，从而为规避检测提供优势；真正的关键风险还取决于攻击者是否触达 CI/CD、签名密钥、发布凭据、包发布令牌等构建与分发环节。

这正是 Trellix 声明特别强调「没有发现源代码发布或分发流程受影响」的原因。这句话在回应最严重的供应链问题：攻击者是否能够把恶意代码放进 Trellix 的正式产品更新链。如果只是只读访问部分仓库，风险主要是情报暴露和潜在漏洞挖掘；如果攻击者能写入仓库、控制构建流水线、窃取签名密钥或发布令牌，风险就会升级为供应链投毒。

## RansomHouse 是谁，会怎么打

RansomHouse 自 2021 年底活跃，被 Palo Alto Unit 42 追踪为 `Jolly Scorpius`。该组织的关键特征如下：

**商业模式**：勒索即服务（RaaS），双重勒索为主——窃取数据 + 加密文件 + 公开威胁。早期阶段曾以「纯数据窃取」（exfiltration only）模式运行，2024 年后回归加密 + 数据外泄并行。Unit 42 在 2025 年 12 月披露 RansomHouse 已经把加密升级为「双密钥分层架构」。

**典型 TTP**：

* 初始访问：钓鱼邮件、利用 Citrix 远程访问软件和 VMware ESXi 漏洞（这部分细节正是 Trellix 2024 年 *RansomHouse am See* 文章中通过赎金谈判记录还原出来的）
* 横向移动：RDP、合法管理工具、Cobalt Strike、Vatet Loader、Metasploit
* 备份摧毁与 ESXi 加密：自研工具 **MrAgent**（自动化 ESXi 部署）+ **Mario** 加密器（基于 Babuk 源码二改）；MrAgent 的用途之一就是在大量 hypervisor 上自动化部署勒索软件并收集虚拟机环境信息
* 数据外泄：CDN 服务器（regular CDN，非 anonymizing 网络）

**与本次 Trellix 事件的相关性**：RansomHouse 历来重点针对 ESXi 虚拟化基础设施。本次截图正好覆盖 vSphere 多个 vCenter，与该组织典型 TTP 高度吻合。**研判**：**倾向认为**入侵路径与该组织过往模式一致，可能从某个面向互联网的服务（VPN、Citrix、未打补丁的边界设备）开始，横向移动到 vSphere 管理面。但**缺乏 Trellix 官方提供的 IOC 或攻击链细节**，这一研判依据是模式匹配而非证据链——属于中等置信度。

**反向假设**：本次入侵也可能是某个 RansomHouse 的关联机构（affiliate）操作，TTP 不必完全套用「典型 RansomHouse 模式」。RansomHouse 是 RaaS 性质，关联机构使用的工具集差异较大。把模式匹配作为强归因依据需要谨慎。

## 历史结怨：Trellix 自己曾经点名 RansomHouse

这一点非常值得关注：**2024 年 2 月 14 日**，Trell...