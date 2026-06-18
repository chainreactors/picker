---
title: 攻击者正利用FortiSandbox三大漏洞发起攻击，未认证即可获取root权限
url: https://mp.weixin.qq.com/s/Y7x2um1kBIPiLAPD75Y_Cw
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:57.963116
---

# 攻击者正利用FortiSandbox三大漏洞发起攻击，未认证即可获取root权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3YXOzicFV8UPmiaOVYsPkmiauF7e8gjNBQut3m8ZyEoxI2XefstkuD2smIvhKMISzUbsAwBDfwFOG3ic2ibyf6W9ypibOjCaUdrDzIo/0?wx_fmt=jpeg)

# 攻击者正利用FortiSandbox三大漏洞发起攻击，未认证即可获取root权限

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1oyHhasIuv5UVva0W30MI5y3oeiaEV27XeWXp1dGabgqhO0YniaNBjLCYanGKce2peRicKxHyw97R5TJ5KA2h32TlfRfIKTCVGrU/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2Y2MBSsnfRDB4beAEjia2o0ZAUmQNibXAteSlLnlhTQ8VeKibzkVvWN5nvjPLw0NJC4XYP0ryiahsuFW6iboC9bU7Sk6hyHeicttCII/640?wx_fmt=jpeg&from=appmsg)

威胁攻击者正在积极利用Fortinet FortiSandbox平台的多个关键漏洞，过去24小时的实时攻击遥测数据已确认存在利用尝试。Defused安全团队标记了三个正被活跃利用的CVE漏洞，其中包括此前无公开利用记录的CVE-2026-39813。

伪装成Fortinet FortiSandbox实例的蜜罐传感器和欺骗基础设施已捕获针对三个漏洞的利用尝试，攻击者均通过向/jsonrpc/ API端点发送精心构造的POST请求触发，攻击流量均通过443端口传输。

Part01

漏洞技术细节

CVE-2026-39813：FortiSandbox JRPC API中的路径遍历漏洞(CWE-24)，允许未经身份验证的远程攻击者通过特制HTTP请求绕过认证。攻击者通过向API注入类似session: "../../tmp/"的遍历序列，可在无需凭证的情况下访问敏感系统数据(包括配置备份、序列号和版本详情)。该漏洞此前无野外利用记录，本次观测到的攻击集群属首次公开案例。

CVE-2026-39808：FortiSandbox API端点中的操作系统命令注入缺陷(CWE-78)，允许未经认证的攻击者以root权限执行任意命令。自2026年4月起已有公开PoC利用代码，攻击者通过管道串联Unix命令利用jid GET参数实施攻击，当前已观测到与该PoC一致的攻击载荷。

CVE-2026-25089：第二个操作系统命令注入漏洞(CWE-78)，影响FortiSandbox Web UI 5.0.0–5.0.5、4.4.0–4.4.8、全版本4.2以及FortiSandbox Cloud/PaaS部署。值得注意的是，该漏洞目前尚无有效的公开利用代码。观测到的利用尝试呈现"振动编码"特征(即可能由AI辅助或启发式生成的逻辑缺陷利用代码)，表明攻击者正在试探性探测而非使用已验证的有效载荷。

Part02

受影响版本

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3FusyaFLhcAGCMc6YibWdQvu90nQoOuMawQcHjicCoOIGMcSviaiaVBUG8pmoHxgaVtvDpSdsbs9INaAU8qIBmGuyrfGh88Oxlh8o/640?wx_fmt=jpeg)

这三个漏洞均可通过单次HTTP请求在未认证状态下触发，这意味着暴露在外的FortiSandbox管理接口无需任何前置访问权限即可被利用。

![Fortinet FortiSandbox 漏洞（来源: X）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3VRKxUZxSZCVOXibiayZglxS3oqIVGfxgMyYibmgXJ6ph4JoodrEFVL5dA7astibMslRjXKlr9PkaVqOV54yick9e9jT7kseCZGQbs/640?wx_fmt=jpeg&from=appmsg)

遭入侵的FortiSandbox可能被武器化，将恶意文件标记为安全文件传递给依赖的Fortinet产品，或作为企业网络内部的横向移动跳板。观测到的攻击者IP 141.11.43[.]175归属于AS136510 Streamline Servers Pty Ltd(新加坡)，具有高威胁评分。

Part02

入侵指标(IOC)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1LkFWWS4sQJTgNzajDI6xPyj3FTNpAEGMkugseiaAiaY1FVvv7qfzxXwcNXONzrSp67f0d0tzhOQ4PEqwOHmLsHhianIpRFT2uOM/640?wx_fmt=png&from=appmsg)

参考来源：

Critical Fortinet FortiSandbox Vulnerabilities Actively Exploited in Attacks

https://cybersecuritynews.com/fortinet-fortisandbox-vulnerabilities-exploit/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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