---
title: IRGC旗下组织CyberAv3ngers：从默认密码到ICS网络武器的四年演进
url: https://mp.weixin.qq.com/s/lvVVBd6O4wSyD-_hJ2NEGg
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:05.048775
---

# IRGC旗下组织CyberAv3ngers：从默认密码到ICS网络武器的四年演进

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYARU8peMiarmrRLpleHgcnweNr9vtic6PHo5LiaIicpNrCCvZ8sJI8djnm5FwKGx4bY2pGBQ2YFZoCD4KllXuprKtoicWNVmQt4PXwc/0?wx_fmt=jpeg)

# IRGC旗下组织CyberAv3ngers：从默认密码到ICS网络武器的四年演进

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个与伊朗有关联的威胁组织，已经从篡改水务设施显示画面，进化到部署定制化 ICS 恶意软件，并利用 Rockwell Automation PLC 漏洞攻击美国多个关键基础设施领域。

────────────────

2026年4月7日，FBI、CISA、NSA、EPA、能源部和美国网络司令部六大机构联合发布警告：与伊朗相关的 APT 组织正在积极利用暴露在互联网上的可编程逻辑控制器（PLC）攻击美国关键基础设施。该公告编号为 **AA26-097A**，确认多个受害组织已遭受运营中断和财务损失。

**关键发现：**CyberAv3ngers 的 ICS 攻击技术已扩散至 60+ 个关联组织，即使核心团队被瓦解，威胁依然持续存在。受影响的 PLC 运营方应立即采取行动。

────────────────

![](https://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYCxr8SicaUF6DqPL7Rib5uib5ibXk6eMMpFoWibhXqlTOTKy3PvaRWBmb6jGsXswEQEvpmovvzZTyUicZnaYInuEicQesdfm6zsVMZ91A/640?wx_fmt=jpeg)

▲ CyberAv3ngers 组织攻击关键基础设施概念图（来源：Tenable）

谁是 CyberAv3ngers？

CyberAv3ngers 是一个受伊朗政府指示的网络威胁组织，作为伊朗伊斯兰革命卫队网络电子司令部（**IRGC-CEC**）的行动代号活跃。该组织至少自2020年起活跃，安全社区使用多个名称追踪：**Storm-0784**（微软）、**Bauxite**（Dragos）、**Hydro Kitten**、**UNC5691**（Mandiant）以及 MITRE ATT&CK ID **G1027**。

尽管最初以反以色列意识形态的黑客行动主义者形象示人，但 CISA、美国财政部及多家网络安全研究机构的调查证实，该组织的资金、工具和运营复杂度远超普通黑客行动主义者。

2024年2月，美国财政部外国资产控制办公室（OFAC）**制裁了六名 IRGC-CEC 官员**：Hamid Reza Lashgarian（IRGC-CEC 负责人）、Hamid Homayunfal、Mahdi Lashgarian、Milad Mansuri、Mohammad Amin Saberian 和 Mohammad Bagher Shirinkar。国务院"正义奖励"计划悬赏高达 **1000万美元** 征集"Mr. Soul"身份信息。

2025年12月泄露的内部运营记录证实，该组织与 **Moses Staff** 行动存在直接基础设施和管理层面的重叠，将此前被视作独立的多个伊朗网络角色统一为国家主导的协调行动。

四阶段能力演进

该组织的运营历史展示了一条清晰的能力升级轨迹：

**第一阶段：宣传期（2020–2022）**
"Cyber Avengers"角色首次出现，声称对以色列电力中断和铁路破坏负责。后被 DomainTools 证实其图片素材来自2022年 Moses Staff 泄露数据的裁剪和换标。

**第二阶段：默认凭据利用（2023年10月–2024年1月）**
通过利用互联网暴露设备的默认密码，攻陷至少 **75台 Unitronics Vision Series PLC**，涉及美国、以色列、英国和爱尔兰。宾夕法尼亚州 Aliquippa 市水务局是最知名受害者。CISA 联合公告 AA23-335A 记录了该攻击活动。

**第三阶段：定制 ICS 恶意软件（2024年中）**
Claroty Team82 发现并分析了 **IOCONTROL**——一个为 IoT/OT 环境定制构建的 Linux 恶意软件平台。OpenAI 披露 CyberAv3ngers 曾使用 ChatGPT 进行目标侦察和代码调试。

**第四阶段：认证绕过利用（2026年3月至今）**
转向利用 **CVE-2021-22681**（CVSS 9.8），一个 Rockwell Automation Logix 控制器的关键认证绕过漏洞，使用租赁的海外基础设施配合 Studio 5000 Logix Designer 软件连接暴露在互联网上的 PLC。

IOCONTROL：国家级 ICS 网络武器

IOCONTROL 由 Claroty Team82 归因于 CyberAv3ngers，是一个模块化架构的恶意软件平台，可运行于多种基于 Linux 的 IoT/OT 设备。受影响设备类型包括 IP 摄像头、路由器、PLC、HMI、防火墙和燃料管理系统，涉及 D-Link、Hikvision、Baicells、Red Lion、Orpak、Phoenix Contact、Teltonika 和 Unitronics 等厂商。

核心技术特征：

• **C2 通信：**使用 MQTT over TLS（端口8883），可与合法 IoT 流量混为一体

• **DNS 隐蔽：**使用 DNS-over-HTTPS 解析 C2 域名，绕过网络监控

• **配置加密：**AES-256-CBC 加密配置数据

• **持久化：**通过 systemd 启动脚本实现

• **能力：**OS 命令执行、端口扫描、自删除

CVE-2021-22681：无补丁的关键漏洞

CVE-2021-22681 是 Rockwell Automation Logix 控制器生态系统中的一个**关键认证绕过漏洞**（CVSS 9.8）。该漏洞源于 Studio 5000 Logix Designer 工程软件与 Logix PLC 之间通信验证所使用的加密密钥保护不足。远程未认证攻击者获取或截获该密钥后，可冒充合法工程软件绕过认证，直接连接受影响控制器。

**⚠ 关键警告：**Rockwell Automation 已声明该漏洞无法通过补丁完全修复。没有可部署的软件更新。唯一的缓解方案是纵深防御策略，包括网络分段、工程工作站隔离、CIP Security 启用和物理模式开关加固。这意味着依赖补丁管理流程的组织将无法通过标准流程解决此漏洞。

受影响产品包括 RSLogix 5000（版本16–20）、Studio 5000 Logix Designer（版本21及更高）以及多个 Logix 控制器系列：**CompactLogix、ControlLogix、GuardLogix、DriveLogix 和 SoftLogix**。该漏洞于2021年2月首次披露，2026年3月因伊朗关联攻击者的积极利用被添加至 CISA 已知被利用漏洞目录（KEV）。

为什么小型公用事业和市政运营商屡遭攻击？

这不是巧合，而是结构性问题：

• 许多组织使用 **TeamViewer 或 AnyDesk** 等消费级远程工具管理 OT 环境

• PLC 管理界面直接暴露在公网上，默认凭据无安全网关保护

• IT 与 OT 环境之间网络分段不足

• 2024年 CISA 评估发现美国水务公用事业合规不达标率超过 **70%**

• 这些组织通常缺乏专职 OT 安全人员，预算有限

"蜂群效应"：威胁扩散

当前威胁等级为**严重**。三大因素汇聚：

1. 一个有国家支持、已展现破坏民用基础设施意愿的行为者

2. 定制 ICS 恶意软件能力 + 无补丁的关键认证绕过漏洞

3. 美伊之间"Operation Epic Fury"后的积极动能对抗态势

CyberAv3ngers 的 ICS 攻击技术已扩散至约 **60+ 个亲伊朗黑客行动主义组织**。这种"蜂群效应"创造了无单一破坏点的分布式威胁面，降低了攻击门槛，并增加了缺乏操作纪律的攻击者造成意外物理后果的风险。

立即行动清单

• **断开 PLC 的互联网连接**——任何暴露在互联网上的 Rockwell Logix 控制器都可被无认证利用

• **将物理模式开关设为"Run"**——阻止远程修改 PLC 逻辑和配置

• **离线备份所有 PLC 逻辑和配置**

• **导入 CISA AA26-097A 的 IOC**——部署至 SIEM、IDS 和防火墙，监控来自海外主机商的端口44818、2222、102、22、502流量

• **实施 IT/OT 网络分段**——隔离运行 Studio 5000 的工程工作站

• **审计 OT 远程访问**——将消费级工具替换为带 MFA 的企业 VPN

• **部署 IOCONTROL 行为检测**——对 OT 网段的 MQTT over TLS（端口8883）和 DNS-over-HTTPS 流量告警

────────────────

**IoC 与检测资源**

|  |  |
| --- | --- |
| 类型 | 详情 |
| 漏洞 | CVE-2021-22681 (CVSS 9.8) |
| 恶意软件 | IOCONTROL (aka OrpraCab/QueueCat) |
| C2 协议 | MQTT over TLS (port 8883) |
| 加密 | AES-256-CBC |
| 监控端口 | 44818, 2222, 102, 22, 502, 8883 |
| CISA 公告 | AA26-097A (2026-04-07) |
| 关联追踪 | Storm-0784, Bauxite, Hydro Kitten, UNC5691, G1027 |

────────────────

**参考资源**

• CISA AA26-097A: cisa.gov/news-events/cybersecurity-advisories/aa26-097a

• Claroty Team82 IOCONTROL 分析: claroty.com/team82/research

• Tenable CVE-2021-22681: tenable.com/cve/CVE-2021-22681

**来源：**Tenable Blog | **原文：**tenable.com/blog/what-to-know-about-cyberav3ngers

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