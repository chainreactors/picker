---
title: 05_等保系列之安全工作规划
url: https://mp.weixin.qq.com/s/3iquAQIm-BYsP4dXUpU6ug
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:35:44.172503
---

# 05_等保系列之安全工作规划

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AXRefkPRWsEA4crQxmWRA0uDyxuibHqxTrv6F2X0BfbFTrC3s6HiaV91IWVZmjDakJpN5ibPsdsbiboLnHTZStTVzA/0?wx_fmt=jpeg)

# 05\_等保系列之安全工作规划

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

# 05\_等保系列之安全工作规划

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。

    一个中心，三重防护。即安全管理中心、安全通信网络、安全区域边、安全计算环境，此外网安法中要求系统建设必须做到三同步，即同步规划、同步建设、同步使用。

## 践行三同步原则

    《网安法》第三十三条规定:“建设关键信息基础设施应当确保其具有支持业务稳定、持续运行的性能，并保证安全技术措施同步规划、同步建设、同步使用”。

### 同步规划:

    在业务规划的阶段，应当同步纳入安全要求，引入安全措施。如同步建立信息资产管理情况检查机制，指定专人负责信息资产管理，对信息资产进行统一编号、统一标识、统一发放，并及时记录信息资产状态和使用情况等安全保障措施。

### 同步建设:

    在项目建设阶段，通过合同条款落实设备供应商、厂商和其他合作方的责任保证相关安全技术措施的顺利准时建设。保证项目上线时，安全措施的验收和工程验收同步，外包开发的系统需要进行上线前安全检测，确保只有符合安全要求的系统才能上线。

### 同步使用:

    安全验收后的日常运营维护中，应当保持系统处于持续安全防护水平，且运营者每年对关键信息基础设施需要进行一次安全检测评估。

## 安全管理中心

    本控制项为等级保护标准技术部分核心，名称虽然看着像管理，但实际归为技术部分。本项主要包括系统管理、审计管理、安全管理和集中管控四个控制点，其中的集中管控可以说是重中之重，主要都是围绕它来展开的。

### 系统管理

#### 定义:

    系统管理涉及对组织内信息技术系统的规划、安装、维护和更新。

#### 主要职责:

* 确保系统的可用性、可靠性和性能。
* 管理硬件、软件和网络的配置。
* 监控系统的运行状态，及时响应系统故障。
* 管理用户账户和访问权限。
* 维护系统文档和配置记录。

#### 权限控制要求:

    只允许特定的命令或操作界面来管理，并对操作进行审计。只要有后台登录界面供管理员登录，而且管理员所有操作都要记录并且可以查询。

### 审计管理

#### 定义:

审计管理是指对组织的内部控制、操作流程和信息系统的安全性进行独立、客观的评估和验证。

#### 主要职责:

* 评估信息系统的合规性、完整性和有效性。
* 检查内部控制的有效性，确保操作符合既定政策和程序。
* 识别系统中的潜在风险和漏洞。
* 提供改进建议，促进风险管理。
* 审计分析，记录的存储、管理和查询完整性，，避免被修改。

### 安全管理

#### 定义:

    安全管理涉及制定和实施安全策略、程序和措施，以保护信息资产免受威胁和攻击。

#### 主要职责:

* 制定安全政策和标准。
* 实施访问控制和安全认证机制。
* 监测和响应安全事件。
* 管理安全漏洞和风险管理。
* 提供安全培训和意识提升。
* 安全策略的配置，参数设置，安全标记，授权以及安全配置检查和保存。

### 集中管控

#### 定义:

    集中管控是指通过集中的监控和管理工具，对组织的信息系统进行全面的管理和控制。

#### 主要职责:

* 集中监控系统的运行状态和性能。
* 集中管理日志和事件信息，以便进行审计和分析。
* 实施集中式的配置管理和变更管理。
* 提供统一的操作界面和报告工具。

#### 应用案例: 带外管理

##### 定义:

    通过专门的网管通道实现对网络的管理，将网管数据与业务数据分开，为网管数据建立独立通道。

##### 作用:

    只传输管理数据、统计信息、计费信息等，网管数据与业务数据分离，可以提高网管的效率与可靠性，也有利于提高网管数据的安全性。可以把通过网络访问设备(Telnet等方式)方式进行严格限制，比如限定特定的IP地址才可以通过Telnet访问设备。大部分的访问均通过带外网管系统进行，可以把整个IT环境设备的访问统一到带外网管系统。

## 控制建议

由于黑客利用漏洞入侵系统或者平台，搞事情之前首先要提权，拿到管理员权限后才可以为所欲为，因此要对这些账户进行必要的保护。

1. 对特权账号的访问控制功能，包括共享账号和应急账号。
2. 监控、记录和审计特权访问操作、命令和动作。
3. 自动地对各种管理类、服务类和应用类账户的密码及其它凭据进行随机化、管理和保管。
4. 为特权指令的执行提供一种安全的单点登录(SSO)机制。
5. 委派、控制和过滤管理员所能执行的特权操作。
6. 隐藏应用和服务的账户，让使用者不用掌握这些账户实际的密码。
7. 具备或者能够集成高可信认证方式，譬如集成MFA。

## 总结

√三同步原则

√ 安全管理中心

√ 控制建议

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

![图片](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFtSkiayt0qhnGMdQLOiaibqxvgibgaWjhuM9B25NW9yrlU1ga4MrHFSor63U27nUWveeCDvpRvT0TXdg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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