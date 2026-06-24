---
title: 俄罗斯FortiBleed行动窃取1.1亿凭证，43万台设备沦陷
url: https://mp.weixin.qq.com/s/yRJKgwm_I7OKBW0FwGXm7A
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:44.715230
---

# 俄罗斯FortiBleed行动窃取1.1亿凭证，43万台设备沦陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3Ushcj4ciaGVIJlbVOsNOHSkt6pwbWXqIWibQaA1oXtM9SW1sShpe2Qe11RCHSDDZ5gpX3YfdCiaUT3EsGmUqlQRSg6Ymb8YPMFk/0?wx_fmt=jpeg)

# 俄罗斯FortiBleed行动窃取1.1亿凭证，43万台设备沦陷

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0BtS1jhL6YPGy6O77dDUBtTQ9lWs6lVyeMLHPqghY2ARyBjbEaxJCLO7LbeOvKXW1c3jNOM8q6wKZ28eH3BceWYE1mrCYBlrI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3z9y1GXTIIHlTiaf3eLhAEaxeBz7RVyZWy35ZaJKVJtUx2sBebwn6mvSXQpdhjow6y36ZohaQIquSlN4tJPBInCwJNHiaOWU5Z8/640?wx_fmt=jpeg&from=appmsg)

Part01

攻击概况

FortiBleed行动已针对43万台以上FortiGate设备发起攻击，窃取1.1亿组凭证，通过大规模凭证窃取实施入侵。SOCRadar威胁研究团队（STRU）发布的最新威胁情报报告首次完整揭露了这场可能成为2026年最具破坏性的凭证窃取行动。该团队是最早发现并命名FortiBleed行动的研究组织。

![FortiBleed攻击](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2ckqnBH0aZ4at1rVLfe0pVOyLdAuaMImUDuDOY552h7yicCoZ4oyD6ic1SLicCsGnmO8KCqUEa1emPlLsz9cKJklaNWE9goIn2iak/640?wx_fmt=jpeg)

Part02

行动技术剖析

攻击链五阶段全还原

报告技术细节完整呈现了攻击全流程：

1. 侦察阶段：攻击者使用Masscan进行端口扫描，配合定制化Shodan\_Recon工具进行被动信息收集，并通过专用FortiProbe-fast二进制程序从上百万扫描结果中筛选确认的FortiGate设备。

2. 目标筛选：根据企业营收对目标分级，体现精确运营规划而非随机攻击。

3. 初始入侵：通过16个针对FortiGate管理员账户命名规范定制的字典进行SSH暴力破解，同时针对SSL-VPN门户实施凭证填充攻击。

4. 核心窃密：使用基于Golang的FortigateSniffer工具，滥用合法FortiOS诊断命令diagnose sniffer packet被动捕获24种协议认证流量（包括Kerberos、RADIUS、NTLM等），全程无需部署恶意软件。

5. 横向移动：在至少一起已确认案例中，攻击者在离线破解Kerberos哈希数分钟后，即从北约盟国防务承包商处定向窃取DFS备份数据。

基础设施架构

攻击者使用东欧松散监管的微型主机服务商网络，核心基础设施划分为四个功能子网：C2聚合、凭证验证、嗅探器部署和代理轮换。测试环境运行7台QEMU/KVM架构的Kali Linux虚拟机，配置严格IPTables规则，支持多操作员通过共享tmux会话远程访问。

Part03

攻击特征与归因

* 工具特征：西里尔字母注释指向俄罗斯背景
* 攻击模式：符合向勒索软件团伙出售初始访问权限的中间商特征，但针对北约盟国防务承包商的行为暗示可能存在国家背景行为体的机会性合作
* 受害者分布：66%为员工不足200人的中小企业，90%年营收低于1亿美元。印度、美国和台湾地区受影响域名占比近1/3，IT服务行业为主要目标

Part04

防护建议

STRU建议相关组织立即：

* 轮换所有Fortinet VPN及管理接口凭证
* 强制启用多因素认证
* 将FortiGate管理接口与互联网隔离
* 审查认证日志异常活动

SOCRadar已发布免费检测工具：socradar.io/free-tools/fortibleed。完整技术报告（含MITRE ATT&CK映射、IoC列表）详见socradar.io。该攻击活动仍在持续进行。

参考来源：

FortiBleed: The Most Detailed Breakdown Yet of an Active Russian Credential-Harvesting Operation

https://securityaffairs.com/194004/hacking/fortibleed-the-most-detailed-breakdown-yet-of-an-active-russian-credential-harvesting-operation.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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