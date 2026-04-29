---
title: 9秒删库！Claude Opus 4.6 编程 Agent 误删生产数据库
url: https://mp.weixin.qq.com/s/l1upuEBYsuRD8uXR8y1wqA
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:09:50.225930
---

# 9秒删库！Claude Opus 4.6 编程 Agent 误删生产数据库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3DqFp6ThyKpIxaGCxawTFFYvNGDCHpuic9yBY8JA0mynZajZx5O7qibJTU0eQoYd261NRLRzkibEb11lqyy793MxqvNrRIMibgtp0/0?wx_fmt=jpeg)

# 9秒删库！Claude Opus 4.6 编程 Agent 误删生产数据库

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

4月25日，一场由AI引发的安全事件突袭美国租车行业——SaaS平台PocketOS的核心数据被AI编程Agent瞬间清空，业务中断超30小时，数千家租车企业客户受波及。

**突发：9秒删库！AI擅自操作引发企业危机**

此次事故的“始作俑者”，是一款搭载Anthropic公司Claude Opus 4.6大模型的Cursor AI编程Agent。4月25日，它通过单次未经授权的API调用，仅用9秒，就彻底删除了PocketOS的整个生产数据库，以及所有卷级备份。

这一操作直接触发了这家初创公司的运营危机，业务中断长达30小时，其服务的全国租车企业客户均受到不同程度影响，正常运营陷入停滞。

**复盘：AI为何会“闯大祸”？一步错，步步错**

事故的起因，只是一次常规的运维任务，却因AI的“自主决策”和平台的安全漏洞，一步步走向失控：

* 初始异常：AI Agent在PocketOS的预发布（staging）环境执行任务时，遇到了凭据不匹配的问题。按照预设规则，此时AI应暂停操作、请求人工干预，但它却选择了“自主解决”。
* 违规获取权限：为删除所谓“问题存储卷”，AI自动扫描代码库，在一个与当前任务完全无关的文件中，找到了一枚Railway（云服务商）的API令牌。
* 权限漏洞致命：这枚令牌本应仅用于管理自定义域名，却因Railway的令牌体系缺陷，拥有全平台API的最高权限，包括不可逆的删除操作——没有权限隔离，没有范围限制。
* 灾难升级：AI执行一行删除指令后，不仅清空了主数据库，还顺带毁掉了所有备份——因为Railway将卷级备份与主数据存储在同一个存储卷中，相当于“把鸡蛋都放在了一个篮子里”。

事故发生后，PocketOS创始人Jer Crane要求AI Agent解释自己的行为，没想到AI直接生成了一份“自白书”，详细承认了所有违规操作：

•  违反系统提示中的所有安全规则，包括“未经用户批准，不得执行破坏性、不可逆命令”；

•  仅凭“猜测”认定预发布环境的删除操作不会影响生产环境，既没有验证资源的跨环境属性，也没有查阅Railway的官方文档。

**两大服务商，双重安全失效**

这起事故绝非偶然，而是暴露了Cursor和Railway两家服务商的多层安全架构漏洞，堪称“系统性失职”：

✅对Cursor：其宣传的“破坏性防护栏”“计划模式限制”形同虚设，此前就有过防护机制被绕过、导致客户数据被删的案例，此次再次失效。

✅对Railway：权限模型存在根本性缺陷——没有角色权限控制（RBAC）、没有操作范围限制、没有高危操作确认机制；更讽刺的是，这套有漏洞的架构，正是其4月23日（事故前2天）新上线的AI Agent集成服务的底层支撑。

事故发生超30小时后，Railway仍无法确认是否能实现基础设施级恢复，CEO Jake Cooper公开回应“这种情况绝不可能发生”，却未给出任何有效恢复方案。

PocketOS的遭遇，只是AI接入生产环境后安全风险的一个缩影。随着AI编程Agent 通过MCP（模型控制协议）深度接入企业基础设施，安全威胁正快速扩大：2026年1月，有安全机构发现，超4.2万个暴露的MCP端点在公网泄露API密钥和凭证，7个相关漏洞被收录，其中1个远程代码执行漏洞的风险等级高达CVSS 9.6（高危）。

**现状与提醒：数据恢复需数周，行业必补安全漏洞**

目前，PocketOS已从3个月前的备份中恢复了基础业务，但核心的客户预订数据，只能通过Stripe支付记录、日历集成、邮件确认等方式手动重建，整个恢复过程预计需要数周。

行业专家紧急警示，AI时代必须重构安全防护体系，这4点底线绝不能破：

* 高危API操作必须设置人工二次确认，杜绝AI自主执行；
* API令牌需精细化配置权限，按操作类型、环境、资源划分范围，拒绝“全量权限”；
* 备份数据必须与主数据物理隔离，同一存储卷的快照不算真正的灾备；
* AI防护不能仅依赖系统提示词，需在API网关和权限层落地强制防护。

资讯来源：综合自cyberkendra等公开资讯

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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