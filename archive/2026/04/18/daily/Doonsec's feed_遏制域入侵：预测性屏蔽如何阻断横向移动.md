---
title: 遏制域入侵：预测性屏蔽如何阻断横向移动
url: https://mp.weixin.qq.com/s/qdvt3VufhfRpoHj2vS9eIQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:50:40.061840
---

# 遏制域入侵：预测性屏蔽如何阻断横向移动

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYAGlianicFhnwND4t1pq5GQ1wTvKDiapK8IXJJgaQx55jo8pIurE7oC4afxm8ldiaKtDK9t6wAXNBibmSxBkSGo0kHgPtDk316zcm0k/0?wx_fmt=jpeg)

# 遏制域入侵：预测性屏蔽如何阻断横向移动

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软安全博客 · 2026年4月17日

遏制域入侵：预测性屏蔽如何阻断横向移动

在基于身份的攻击活动中，一旦威胁行为者获得域管理权限，任何初始入侵都可能从严重升级为危急。攻击者此时实质上掌控了 Active Directory 域——可以修改组成员关系和 ACL、签发 Kerberos 票据、复制目录机密，以及通过 GPO 推送策略。

域入侵的棘手之处在于其极快的演进速度：在许多真实案例中，首次获取访问权限后域级凭据几乎立即被攻破，而一旦暴露，攻击者会立即利用，防御者根本来不及完整评估事态。

────────────────

什么是预测性屏蔽？

微软 Defender 的**预测性屏蔽（Predictive Shielding）**是自动攻击中断功能中的一项能力，旨在阻止基于身份的攻击扩散。与传统方式等待账户被观察到恶意行为不同，预测性屏蔽聚焦于凭据可能暴露的时刻——当 Defender 在设备上检测到高置信度的凭据窃取活动信号时，它可以主动限制可能已暴露的账户。

其工作流程如下：

► Defender 检测到设备上与凭据暴露高度相关的入侵后活动

► 评估哪些高权限身份可能已在该上下文中暴露

► 对这些身份施加**遏制措施**，限制攻击者枢轴能力，阻断横向移动路径

核心理念：关闭攻击者"利用新暴露凭据的速度"快于"响应者评估范围、重置和清理速度"之间的差距。

────────────────

真实入侵案例深度剖析

2025年6月，某公共部门组织遭到威胁行为者攻击。该攻击者手法老练，依次完成了初始利用、本地提权、目录侦察、凭据访问，并向 Microsoft Exchange 和身份基础设施扩展。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYDaHH9g72cBaOKflQJ44W2Pck7Yz0pziaHv4qdP9RnTMPEJfdkKiaeYynLQpdlsUSTKcpT14n7QHKNO8nZuVaDIhDgr4oU0SQPdg/640?wx_fmt=png)

图1：域入侵攻击链全景图

阶段一：初始入口

攻击从边界开始：攻击者利用面向互联网的 IIS 服务器上的文件上传漏洞植入并启动 Web Shell。随后，通过 Web Shell 同时执行多项侦察活动，并利用 BadPotato 等 Potato 类令牌模拟原语将权限提升至 **NT AUTHORITY\SYSTEM**。

图2：攻击中的发现命令示例

攻击者使用被入侵的 IIS 服务账户尝试重置高影响账户的密码（无需执行凭据转储），同时部署 **Mimikatz** 转储登录凭据（MSV、LSASS、SAM），收割设备上暴露的凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYBxiaocA0CibhQEabGdvqqicp0UtyyhgZW3D3icib5BJWOfQ3WUmNbWS2E0zZN3fCj5wNqbsSofkbfTyCLT5343dMoQZfG0ugX1ia8bA/640?wx_fmt=png)

图3：Mimikatz 凭据转储活动

关键要点：此阶段的遏制应限于主机级别，优先阻止凭据窃取和权限提升，防止其触及身份基础设施。

阶段二：首次枢轴——目录凭据实体化与 Exchange 委派

24小时内，攻击者利用被入侵的特权账户在域控制器上远程创建计划任务，触发 NTDS 快照活动并使用 **makecab.exe** 打包输出，实现对目录凭据材料的离线访问——足以大规模滥用凭据。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYAibbEwubLyakqIib4RicKAwl77kVcCHYCK52vEu0LBJR2hj6XvSA6icDicrFiaqYxMricNTCYtxicmlyZ0kMGHNRGpydcOb8TNcKdfRAQ/640?wx_fmt=png)

图4：NTDS 凭据提取活动

攻击者随后在 Exchange Server 上植入 **Godzilla Web Shell**，枚举具有 *ApplicationImpersonation* 角色分配的账户，并通过 *Add-MailboxPermission* 授予委派主体对所有邮箱的完全访问权限。

攻击者还使用 Impacket 的 **atexec.py** 远程枚举角色分配。该行为触发了 Defender 的自动攻击中断功能，撤销了管理员账户的会话并阻止其进一步使用。

关键要点：一旦目录凭据和特权委派被利用，事件范围和影响会急速扩大。防御者应优先保护域控制器、特权身份和认证路径。

阶段三：规模与速度——工具回归、密码喷洒与横向移动

数周后，攻击者携 Impacket 工具（secretsdump、PsExec）卷土重来，Defender 对被滥用账户进行了反复中断。这迫使攻击者转向其他被入侵账户。

被 Defender 中断后，攻击者从初始入侵的 IIS 服务器发起**大规模密码喷洒攻击**，通过密码重用解锁了至少 **14 台服务器**的访问权限，并使用多个域和服务主体对数台域控制器和 IIS 服务器发起远程凭据转储。

即使自动攻击中断立即响应，攻击者因先前的大规模凭据转储已拥有多个凭据。这正是引入预测性屏蔽来先发制人地中断面临风险的暴露账户的原因。

阶段四：预测性屏蔽打破攻击链

在攻击的第二阶段，团队激活了预测性屏蔽。当暴露信号出现时（例如凭据转储尝试和来自被入侵主机的重放），自动遏制不仅阻止了被滥用账户的新登录尝试和交互式枢轴操作，还对同一受损表面上活动的**上下文关联身份**实施了限制。

至关重要的是：当高权限的 Enterprise Admin 或 Schema Admin 凭据暴露时，预测性屏蔽在**被利用之前**就将其遏制，阻止了通常会演变为灾难性的权限升级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYC4GBiawp4j5Yg8UHpeF5Tib3siauAyfxh7OHOI36HPQ8xLYMwoYMJibG4R1fPfgYiaNSFiaBmHL1ByQbJgiceNM0Ib4yUz3mibo4eZYfw/640?wx_fmt=png)

图5：攻击者在 Schema Admin 权限下的操作

阶段五：最后的挣扎与终止

在攻击的最后阶段，高价值身份被预先遏制后，攻击者转向利用 Apache Tomcat 服务器。他们入侵了三台 Tomcat 服务器，植入 Godzilla Web Shell，并通过 PowerShell 执行 **Invoke-Mimikatz** 收割额外凭据。攻击者还使用 Impacket **WmiExec** 访问 Microsoft Entra Connect 服务器，尝试提取 Entra Connect 同步凭据。

在最终阶段，攻击者使用 **comsvcs.dll MiniDump** 在文件共享服务器上对 LSASS 进行完整转储：

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYDCuanicpvw7NN7EAI6QjEH8WFib7JBfnAGT1PenvkEiad6vEMqBCn4rIwJZJWYxoNpiaia9FV7TF86W2Ic2mlPwhicQdQLibEp7KsaKY/640?wx_fmt=png)

图6：LSASS 转储命令

Defender 的攻击中断功能反复切断攻击者的会话并阻止新的登录尝试。**2025年7月28日，该攻击活动失去动力并终止。**

────────────────

预测性屏蔽如何改变了结果

在入侵域之前，攻击者主要受限于他们控制的主机。然而，即使少量暴露的凭据也可能解除这些约束，通过特权认证和委派路径给予攻击者广泛访问权限。爆炸半径快速扩散，时间压力急剧上升，遏制决策变得更加棘手——因为身份基础设施和高权限账户是生产依赖项。

在此案例中，预测性屏蔽激活后，攻击态势发生了转变——Defender 不再被动响应每个新被滥用的账户，而是**先发制人地行动**，将凭据窃取尝试转变为被阻止的枢轴操作。高价值身份被预先遏制后，攻击者转向其他凭据来源，但每次后续尝试都触发了针对性遏制，直到他们失去动力。

遏制有效的"信号"：一旦特权枢轴被阻止，威胁行为者通常会猎取替代凭据来源，防御必须持续跟踪不断移动的爆炸半径。

────────────────

MITRE ATT&CK 技术映射

|  |  |  |
| --- | --- | --- |
| 战术 | 技术ID | 技术名称 |
| 初始访问 | T1190 | 利用面向公众的应用程序 |
| 持久化 | T1505.003 | 服务器软件组件：Web Shell |
| 执行 | T1059.001 | 命令和脚本解释器：PowerShell |
| 权限提升 | T1068 | 利用漏洞提升权限 |
| 凭据访问 | T1003.001 | OS 凭据转储：LSASS 内存 |
| 凭据访问 | T1003.003 | OS 凭据转储：NTDS |
| 横向移动 | T1021.002 | 远程服务：SMB/Windows 管理共享 |
| 凭据访问 | T1110.003 | 暴力破解：密码喷洒 |
| 防御规避 | T1070.004 | 主机指标移除：文件删除 |
| 持久化/权限提升 | T1098 | 账户操作 |
| 凭据访问 | T1078 | 有效账户 |

────────────────

来源：Microsoft Security Blog ｜ 翻译：AI 自动翻译

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