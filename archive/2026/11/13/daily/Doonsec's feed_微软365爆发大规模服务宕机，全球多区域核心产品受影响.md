---
title: 微软365爆发大规模服务宕机，全球多区域核心产品受影响
url: https://mp.weixin.qq.com/s/Urylmz-wj4tHrxSqxCYhvw
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:21.744789
---

# 微软365爆发大规模服务宕机，全球多区域核心产品受影响

# 微软365爆发大规模服务宕机，全球多区域核心产品受影响

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3pU0BJr7FzChwAN9ia8DBJ7rRic8kVLgMQrCn2bkVdaWhV9iaxlGyW4ib0ctbjQ6LCMibLfhroxutXVuEAKnYRVQibBSibFK8nAlnibC0/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1q9ictnnWneuDyUEoUDujjVx6B036Mic3n9eeFBwJp7OXJFZ7OL8ZyES8UX2q7S8sbdOrbGIcIDfKOHoldhd1K5jonum3LQqfQA/640?wx_fmt=png&from=appmsg)

2026年11月12日，微软365爆发大规模服务宕机，用户云服务访问受阻。故障持续至11月13日，微软正全力修复故障基础设施。

微软最初仅排查美洲地区Exchange Online邮箱访问异常问题，随后确认连接故障可能波及全球所有区域用户。目前已知受影响的服务包括Outlook、Teams、SharePoint、Copilot以及微软Defender XDR，具体服务和功能受限范围以微软最新公告为准。管理员可通过事件编号MO1550821查看详细故障明细；针对Exchange Online邮箱连接问题，微软单独设立事件编号EX1550543跟踪更新进展。微软目前尚未确认所有客户均受到影响。

微软365状态官方账号（@MSFT365Status）2026年11月12日发文称："我们正在排查美洲地区用户通过多种方式访问Exchange Online邮箱时遇到的问题，更多信息可在微软365管理中心查看EX1550543事件详情。"

初步排查显示，多个区域的服务负载过高。微软后续澄清，负载压力并非来自流量增长。故障根源是部分服务器意外不可用，剩余基础设施不得不承接所有连接请求。工程师已开始在微软全球系统中调度流量，降低受影响环境的运行压力。

此次宕机并非微软365近期首次出现服务故障。今年7月，微软365就曾发生宕机，影响Teams、SharePoint与Copilot服务，故障根源是一次网络配置变更。目前微软尚未确认本次故障与此前事件原因相同，因此不能直接套用过往事件的结论判断当前调查方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3MaV0u4LLdS81aYcchqvm8Dj345uqCuafHbEClImhBB0R5vPicGWib5vom0IrLVZKAy1uB7UnRCVJQ6USZg5Wv1ib9l4dG2n300w/640?wx_fmt=png&from=appmsg)

Part01

自动健康检查失效

拖慢故障恢复进度

微软排查发现，自动健康检查失效是本次故障的关键诱因。这类检查的作用是判断服务器是否可正常处理用户请求。调查人员目前重点排查负责处理服务器健康状态的组件，同时测试配置变更方案、重启受影响服务器，逐步恢复服务容量。

根据微软官方事件更新，采用替代健康检查方案后，部分服务器已恢复服务。工程师开始大范围推广这一方案，同时调试自动恢复系统，用于检测并重启无响应的服务器。不过这些措施并未立刻达到预期的恢复效果。

微软后续发现，受影响服务器上的某个核心进程出现资源过载问题，进一步导致服务容量下降。部分已恢复的服务器初期运行稳定，但流量接入后会再次进入无响应状态。这种情况大幅提升了恢复难度——服务器重新上线并不代表其可以稳定支撑正常使用。

工程师已暂停所有新部署操作，将流量切换至备用链路。团队同时评估回滚近期几项配置更新的可行性，判断这一操作是否能加快恢复速度。微软最初表示，未发现故障发生时间点附近存在匹配的配置变更，因此回滚操作目前只是可选恢复手段，不能证明配置问题就是本次故障的根本原因。

Part02

Defender XDR服务受阻

对安全团队而言，微软Defender XDR服务受阻引发了普遍担忧：团队是否还能正常访问告警、开展调查工作。此前微软Defender门户曾出现过访问故障，当时仪表盘无法访问直接打断了整套安全运营流程。不过需要明确的是，仅门户访问异常并不代表端点防护功能或后台检测机制已经停止运行。

管理员可在微软365管理中心跟踪EX1550543与MO1550821事件进展，若管理中心无法访问，可通过微软公共服务状态页面获取更新。目前微软公开的更新内容仅涉及基础设施故障与恢复工作，没有证据表明本次宕机由网络攻击导致。

微软365状态官方账号（@MSFT365Status）2026年11月13日发文称："我们已梳理所有已知影响场景，更新了受影响服务与功能清单，相关内容可在微软365管理中心MO1550821公告的'更多信息'板块查看。"

截至最新公告发布，微软尚未确认服务完全恢复，也未给出明确的修复完成时间。企业需要注意区分部分恢复与稳定服务的差异，尤其是已恢复的服务器在流量接入后可能再次无响应。微软目前仍在调查这一异常现象，同时对部分流量采取限流措施，稳妥推进剩余服务容量的恢复工作。

本次事件仍在发展中，待微软公布更多宕机与服务恢复相关信息后，我们将持续跟进更新。

参考来源：

Massive Microsoft 365 Outage Impacts Exchange Online, Teams, SharePoint, Copilot, and Defender XDR Users

https://cybersecuritynews.com/massive-microsoft-365-outage/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

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