---
title: php2shell连锁反应：Okta企业网关同发七连公告
url: https://mp.weixin.qq.com/s/QbtISusBt8E2Zkxf1BEOKw
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:57.265824
---

# php2shell连锁反应：Okta企业网关同发七连公告

# php2shell连锁反应：Okta企业网关同发七连公告

原创

赤霄攻防实验室
赤霄攻防实验室

赤霄攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![封面｜漏洞情报（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8aeDZEr2WJN14tPCKCVTo73OB8lSchOroak580BBGibFSr5icpJYI0oXkU5G2t8JwMMG5JrDKHUM8I784aQ2iaOZIRgcSaAvZj1Gr4/640?wx_fmt=png)

▲ 封面｜漏洞情报（制图：赤霄攻防实验室）

TL;DR

**下文来了**：昨晚写的 PHP 双 RCE 烧到了企业身份基础设施。Okta Access Gateway 同日发布七连公告，连「php2shell」这个社区命名都被官方公告直接采用了

**最重的**：管理台命令执行（CVE-2026-115547，9.1），管理员上下文配置值注入，S:C 作用域变更

**怎么办**：OAG 升 2026.44.0（PHP 8.3.36）+ 2026.10.2（命令执行修复）。用 Okta 的企业今晚核对版本

![漏洞档案卡（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8aficDyTW1oM79GjbUoEIA1YKTWiasnz361mlSIf8hd7pw5CG9PAuHJ70EeH6Q5mIuClwn5m3B2tOaY3gwDfiboibsTZf9KcRGbWvtY/640?wx_fmt=png)

▲ 漏洞档案卡（制图：赤霄攻防实验室）

## 连锁反应比预想的快

昨天写完 PHP 的两个 9.8，我留了句话：跑着 PHP 的企业产品都会陆续中招。没想到这句话二十四小时就应验了，而且中的不是无名之辈。10 月 22 号，Okta 给自家的 Access Gateway（OAG，企业级访问网关）一口气发了七个安全公告，其中一条的标题直接写着：PHP Runtime Vulnerabilities Affecting Okta Access Gateway。

更有意思的细节是，Okta 的公告里正式使用了「PHP2Shell」这个社区命名。一个漏洞有了官方背书的名字，基本就等于进入了主流威胁词典。OAG 内置的 PHP 运行时是 8.3.x，8.3.36 之前的版本全部受影响。Okta 说默认配置能缓解已知利用，但还是把修复版 2026.44.0（捆绑 PHP 8.3.36）推给了所有客户。

![Okta 官方公告：PHP 运行时波及 OAG（来源：trust.okta.com）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8afU2WmKicU9RAvcezw4g5oBEuwLqzxGRLCAHbpC16ypD5jMLkyIt9cBPm6REEm8yriaajWEiaKXphcVXO00AMldnFxiaU8ffEy0tOo/640?wx_fmt=png)

▲ Okta 官方公告：PHP 运行时波及 OAG（来源：trust.okta.com）

## 七个公告里最重的那个

php2shell 只是七连公告之一。同批最重的是 CVE-2026-115547，9.1 分：OAG 管理控制台的输入校验问题， specially formatted 的配置值会被处理，管理员上下文直接执行系统命令。注意评分向量里的 S:C——作用域变更，打穿管理台之后影响的不只是管理台。

前提条件得说清楚：需要管理员权限（PR:H）。所以这不是「任何人都能打」的洞，而是「管理员账号一旦泄露就能把网关变成跳板」的洞。在企业环境里，管理员凭据钓鱼、会话劫持都不是小概率事件，这个前提并不算苛刻。加上另外五个：LDAP 数据源过滤器注入、Kerberos 配置路径问题、SNMP 配置、应用标签、认证源验证——OAG 的输入卫生这一周全线告急。

![连锁反应时间线（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8aduPLwEzNS6fmwWpLvmW9zfTVHwtut2HicKCVJOQZdTwXNmDsJCsPB9b3I2Plc4og5hUeEyoHDTBpm063tyU726X1ALdz4MnmXI/640?wx_fmt=png)

▲ 连锁反应时间线（制图：赤霄攻防实验室）

## 身份基础设施是根，根的补丁最优先

Okta 这类身份提供商的产品出了洞，补丁优先级要提到最高，原因很朴素：它是所有其他系统信任的起点。网关失守，后面接的 SSO、MFA 策略、应用信任关系全部变成攻击者的工具箱。

给企业采购的另一个提醒：把「上游运行时漏洞的响应速度」写进供应商评估。OAG 这次从 PHP 官方公告到自家修复版发布不到 48 小时，这个速度值得肯定，但它是 Okta。你用的那些小厂网关和面板呢？他们的 PHP 版本多少年没动过了？挑供应商的时候问一句「上次上游运行时出 9.8 你们多久发的修复版」，答案能筛掉一大半不合格的。

还有个细节值得玩味：Okta 特意在公告里写了「默认配置可缓解已知利用」。这句话是在告诉客户风险可控，但反过来说明非默认配置（比如自定义过 PHP 设置的部署）可能不在保护范围内。改过默认值的企业，升级前先把自己的配置跟官方基线对一遍。

![命令执行公告（来源：trust.okta.com）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8adp48IqNbSljrwoVfu9jxroRxAoAJZsqB5bZrG9yaoJtHBEl7wlCDvqSN0OhZfOTFjEoH1VH9wib18FhsnyCmdjq1Dm2v3icsGGI/640?wx_fmt=png)

▲ 命令执行公告（来源：trust.okta.com）

![七连公告清单（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8aegOmaccNvicHkM31aIZSN9YEdA9QJfK0d4Sdd3vs8fKtuuI4a9p29ccxXRL9LuDP08hdp7rN2jAHLb8CibZIicOA4xczF6Ric6Xew/640?wx_fmt=png)

▲ 七连公告清单（制图：赤霄攻防实验室）

## 参考

1. Okta 官方公告 ×7（trust.okta.com/security-advisories/）
2. CVE-2026-115547（9.1，CWE-94/20）
3. CVE-2026-109618 / 109619（php2shell，见本号昨日文章）

免责声明：本文仅用于安全研究与防御交流。

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8acyYZfmKJeSLQ7Quiag7TKhsm6Z5yHicU9D1f8on7dzPIKTE1LJpnoT3TmcTlngd8BRNH8cf30FeI94XtDOrUOJibW2Jh16nvMQ6g/0?wx_fmt=png)

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