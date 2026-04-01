---
title: CertiK发布OpenClaw安全报告：复盘AI智能体快速增长下的安全逻辑缺陷（附安全指南）
url: https://mp.weixin.qq.com/s/s7lhfSG0eDW5YsGLbI2gvQ
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:34.670571
---

# CertiK发布OpenClaw安全报告：复盘AI智能体快速增长下的安全逻辑缺陷（附安全指南）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yYpNAymx6u0LunXc6GticFHTUMLTP4MPlc0xeH7QsjXtjMHuy74AiaOia0jIwAaG94vpfmqV6m3z5yLvyiaBVHHGhAQIQwtCicTOnpDUMzNpibeeE/0?wx_fmt=jpeg)

# CertiK发布OpenClaw安全报告：复盘AI智能体快速增长下的安全逻辑缺陷（附安全指南）

原创

CertiK
CertiK

CertiK

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/mmbiz_png/yYpNAymx6u0wwW1QNmTOyDn53B9lOLQUBgr9qD61btfOZfkhQlWV41OLZygS4od3cK0HNW9TImedWVAJEIemxcgZxCMxv6GuGibmbZOJAibuQ/640?wx_fmt=png&from=appmsg)**

CertiK《OpenClaw安全报告》现已发布。报告聚焦OpenClaw这一现象级AI智能体框架，基于已公开并修复的安全事件，系统回顾了其发展过程中的安全边界，剖析了潜在的风险模式，并提出针对开发者与使用者的防护建议。

报告指出，随着OpenClaw的GitHub星标突破30万，AI驱动助手正加速走向实际应用。但其从边缘项目到大规模部署的快速演进，也使早期基于“本地可信环境”的安全模型难以适应复杂场景。数据显示，在2025年11月至2026年3月期间，OpenClaw累计产生280条安全公告及100个以上CVE漏洞，反映出AI智能体在真实环境中的安全挑战。

# **架构性缺陷：从“本地可信”到权限失控**

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yYpNAymx6u0z1U9icLibZlOaYiaQqqiaKbxG39jVKA1HkolIt8WcQbuYHY4zGmk7sxuD6BRuzFQfYYNsdGFphnf1Vq4Y5ia3L6xFret0dziaqH4XY/640?wx_fmt=jpeg)**

OpenClaw演化与爆发式增长情况

报告指出，部分历史漏洞集中反映出OpenClaw在控制平面存在的底层设计缺陷。其核心网关（Gateway）长期以“访问来源接近性”替代身份验证机制，导致攻击者能利用本地来源或URL参数等轻易获取Shell执行、文件访问及多设备控制等完整编排权限。

此外，在20余个消息平台的身份绑定机制中，由于使用可变属性及缺失Webhook验证等授权机制设计问题，导致允许列表（Allowlist）被频繁绕过，相关问题已形成约60条安全公告。

# **执行链漏洞：校验偏差与本地资产泄露风险**

在执行层面，策略校验与实际执行之间存在偏离。由于强制执行机制未对指令解析后的最终形态进行校验，攻击者通过参数缩写即可绕过基于精确匹配的拒绝列表，导致预设的安全边界在实际运行中失效。

同时，本地工作空间集中承载高价值资产，但文件系统边界控制不一致。由于各模块各自实现校验逻辑而非共享统一机制，路径遍历漏洞与沙箱缺口在多个模块中独立出现。相关问题在历史漏洞中多次出现，进一步扩大了潜在攻击面。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/yYpNAymx6u21VJSDgtxonOCt6mmchuplQLYhRVdcJBr0bAaGHnAwcXEtOibeLrxvvHBZe4gd5HwSvL4Kz6y2ZXqxxW4VYiarV9ic98wPHJDzzA/640?wx_fmt=png&from=appmsg)**

OpenClaw系统高层架构图

# **供应链与部署风险：攻击面持续扩大**

扩展生态已成为大规模供应链攻击的主要载体。报告指出，在ClawHub插件市场中已发现数百个恶意技能（Skill），同时还存在仿冒安装程序及npm软件包等问题。不同于传统供应链攻击，AI智能体技能可通过自然语言影响系统行为，使其更难被传统检测机制识别。

此外，部署配置风险同样不容忽视。数据显示，在82个国家发现超过13.5万个暴露在网络中的实例。关闭沙箱、权限策略过宽或跨信任边界部署等情况，即使在无代码漏洞的前提下，也可能带来严重安全隐患。

此外，提示词注入（Prompt Injection）依然是尚未解决的基础性挑战，涉及间接注入、标记伪造等攻击方式。报告强调，这一问题无法仅靠模型层解决，必须通过多层系统级防护、严格的能力控制，并将持久性存储作为关键攻击面加以保护。

# **多维防御建议：从开发到部署的安全治理**

针对上述风险，CertiK在报告中针对开发者、部署方和非技术用户提出了多维度防御建议：

* 开发者：在构建类似OpenClaw的智能体系统时，安全必须从设计之初就作为核心要素，而非在系统规模扩大后再进行补救，包括加固控制平面管理接口，对派生进程强制执行不可变的权限继承，并引入语义防火墙等系统级防护。
* 部署方：管理AI智能体应类比管理“特权员工”，持续监控、定期审计以及严格的访问权限管理。运营方应将服务绑定至本地回环地址运行，建议在隔离环境中使用非Root账户运行，强制执行身份验证与允许列表机制，并对第三方扩展按不可信代码标准进行严审。
* 普通用户：现阶段应保持谨慎，在安全性更成熟的版本发布前，避免赋予自治智能体对个人或企业核心账户的广泛访问权限。

更详细的安全建议与实践指南，请点击文末的“阅读原文”，查阅完整的《OpenClaw安全报告》。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mHUbQLu9aKkzUzMI4TIaLqGmFv3Tb6l6n5icsH0UYmUo71WUibpicfic3YsT1xvfrkLyoCKKBWTA7pNia5d2V1TwjhA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/yYpNAymx6u3JrNwdeY9Kh6KkyzVEiczFF3BnDOu3UDlS7VTweswicto8IiciadTmx5hu7MibgNibZniboNhibK2HeehXmgj5Pzph4ibq0bEv6gJcWicz0/0?wx_fmt=png)

CertiK

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/yYpNAymx6u3JrNwdeY9Kh6KkyzVEiczFF3BnDOu3UDlS7VTweswicto8IiciadTmx5hu7MibgNibZniboNhibK2HeehXmgj5Pzph4ibq0bEv6gJcWicz0/0?wx_fmt=png)

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