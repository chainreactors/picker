---
title: 从 IAM 松散管理到零信任架构：Sendbird AWS 安全实战演进实录
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484070&idx=1&sn=183c6569561febbd5b919e8496dc65f3&chksm=c006ca56f7714340d02c223a0b9e81cb9306f6fad5f7b304ce4295583d75777110b0f346b19c&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-12
fetch_date: 2025-10-06T20:37:45.346559
---

# 从 IAM 松散管理到零信任架构：Sendbird AWS 安全实战演进实录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk7DOFdlEX96TCNRxjRw7AVXibwdyv7wicuMF2xddE1K4NX2j0VOBVwkbjMVglbibibqbs8djjY9pCFS3g/0?wx_fmt=jpeg)

# 从 IAM 松散管理到零信任架构：Sendbird AWS 安全实战演进实录

原创

tonghuaroot

RedTeam

### Sendbird 简介

Sendbird 是领先的实时通信云服务提供商，为全球企业客户提供可嵌入的聊天、语音、视频 API 及 SDK，服务覆盖社交平台、金融科技、医疗健康等高合规性行业。其基础设施构建于 AWS 全球架构。

本文系统披露 Sendbird 从初创期到成熟阶段的 AWS 安全实践：早期采用 IAM 用户、MFA 基础防护，逐步演进为联邦身份认证、零信任访问控制、策略即代码等深度防御体系。通过 Okta SSO 全量迁移、Teleport 精准权限审批、Orca 安全平台三位一体改造，实现从 "应急响应" 到 "安全左移" 的体系升级，为海量消息交互提供企业级安全保障。

本文主要包含初创阶段的安全基线（安全团队成立前）、安全体系升级（安全团队主导）、可验证的技术演进 3 个部分。

### 初始阶段：创业成长期的基础安全配置

在安全团队未完全建制前，Sendbird的AWS环境以满足快速工程迭代为主，仅维持基础安全水位。随着专职安全团队的组建，开始系统性重构云安全体系。

本部分剖析早期架构的安全瓶颈，后续章节将详解成熟期安全增强方案。

### 1. IAM基础账号体系的脆弱性

* **MFA基础防护**：工程师通过IAM用户密码登录，强制启用多因素认证（MFA）
* **权限管理痛点**：采用Inline Policy导致权限可视化缺失，审计困难
* **Root账户滥用**：存在使用Root账户执行运维操作的违规行为

### 2. 初级云安全态势管理（CSPM）

* 依赖单一CSPM工具进行CloudTrail日志分析及配置错误告警

### 3. 服务间通信安全风险

* IAM Bot账号密钥在多服务间共享，异常行为检测失效
* 凭据泄露将导致横向攻击面扩大

### 4. 主机层访问控制

* 工程师通过SSH直连EC2实例及数据库
* 自制审批系统实现数据库访问管理

### 5. 基础设施即代码（IaC）管理缺口

* 使用Terraform+Atlantis实现GitOps，但部分账户仍存在本地IAM用户直接修改

### 6. 应急响应机制缺陷

* 各账户预设Breakglass管理员角色
* 缺乏使用审批流程与时效控制

### 7. GovCloud合规挑战

* 政府云区域存在相同架构缺陷

## 云安全架构11项关键强化措施

### 1. 全景式云安全平台选型

* 替换单一CSPM工具，采用Orca Security实现：

+ **无代理快照扫描**：分钟级资产可见性
+ **容器安全**：镜像漏洞管控
+ **K8S 运行时防护**：异常行为检测

### 2. 身份联邦升级

* **Okta 联邦身份集成**：

+ 通过AWS IAM Identity Center建立SSO体系
+ Okta组动态映射权限集（Permission Sets）
+ HR系统联动实现自动化用户生命周期管理

* **策略即代码**：

+ Terraform统一管理Customer Managed Policies
+ 清除冗余的 Inline Policies

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7DOFdlEX96TCNRxjRw7AVXuWhSvrpAWWbHc6Vq7tzDbn87h1UFGSiabXukN6kibxicluGA9uXy1HWUA/640?wx_fmt=png&from=appmsg)

image

### 3. IAM用户清除计划

* 采用双轨验证机制：

1. 公告IAM用户淘汰时间表
2. 并行测试SSO角色权限覆盖度
3. 漏洞修复后执行全局IAM用户清理

### 4. 零信任主机访问体系

* 引入Teleport实现：

+ **SSH代理网关**：集中式访问控制
+ **数据库动态授权**：基于工单的审批流
+ 会话录像审计：满足合规取证需求

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7DOFdlEX96TCNRxjRw7AVXHhq6lCOjLtQyia0topK5SFNSHhLAjrAFL9NCiaEiaibYaqibsPCZ6rD4Vww/640?wx_fmt=png&from=appmsg)

image

### 5. Kubernetes安全增强

* **集群访问治理**：

+ Teleport集成K8s RBAC
+ 命名空间级临时权限申请
+ 审批链与时间窗控制

### 6. IaC全流水线管控

* 强制所有AWS账户接入Atlantis：

+ PR审核机制保障变更合规性
+ 消除本地执行漏洞

### 7. 应急响应流程再造

* **Breakglass角色治理**：

+ 集成Okta Identity Governance（OIG）
+ 管理员多级审批工作流
+ 自动时效回收策略

### 8. 云威胁检测体系

* 构建检测架构：

1. CloudTrail全量日志接入SIEM
2. Orca安全事件关联分析

### 9. 终端安全准入控制

* **设备可信链构建**：

+ Okta设备信任策略
+ 仅允许企业托管设备访问AWS控制台
+ 终端健康状态动态验证

### 10. 服务控制策略（SCP）加固

* 账户级防护层设计：

+ 关键API操作全局封禁
+ 即使Breakglass角色也无法越权

### 11. GovCloud合规对齐

* 全量安全控制措施同步部署至政府云区域

## 架构演进启示录

通过这11项措施，Sendbird实现了：

* **最小特权原则落地**：权限动态化管理
* **攻击面收敛**：SSH/K8S 访问代理化
* **审计能力增强**：全链路行为日志
* **合规基线提升**：满足合规要求

以上内容来源于 Sendbird

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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