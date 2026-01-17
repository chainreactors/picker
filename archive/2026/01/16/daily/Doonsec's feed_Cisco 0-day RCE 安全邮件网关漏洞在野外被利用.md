---
title: Cisco 0-day RCE 安全邮件网关漏洞在野外被利用
url: https://mp.weixin.qq.com/s/wUIhnvYbUIO9B2lT0En5OQ
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:26.006270
---

# Cisco 0-day RCE 安全邮件网关漏洞在野外被利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qw6g97TWG2CyicdwgRkc6ApWcrasaTlt1y5hxv6icTRO16DG1T6RgwzribcT02A9UXw4txuPoDoxBTug/0?wx_fmt=jpeg)

# Cisco 0-day RCE 安全邮件网关漏洞在野外被利用

原创

O安全研究员
O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qw6g97TWG2CyicdwgRkc6ApWibuW8cVzypnIsf1Iw8kHngdX5hyKUibRRvklTVXTMDwViaO0bINBtOSVA/640?wx_fmt=png&from=appmsg)

思科已确认其安全邮件网关和安全邮件及网页管理设备中，正在积极利用一个关键的零日远程代码执行漏洞。

该漏洞被追踪为CVE-2025-20393，允许未经认证的攻击者通过精心设计的HTTP请求执行任意根级命令，指向垃圾邮件隔离功能。

该漏洞源于Cisco AsyncOS软件的垃圾邮件隔离功能中HTTP请求的验证不足，导致受影响设备能够以根权限远程执行命令。

该系统被归类为CWE-20（不当输入验证），最高 CVSSv3.1 基础得分为10.0，突出其网络可访问性、低复杂性以及对机密性、完整性和可用性的重大影响。

利用目标是启用垃圾邮件隔离并暴露于互联网的设备，通常在6025端口上，该配置默认未启用，部署指南中也不鼓励。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qw6g97TWG2CyicdwgRkc6ApWDjCIMYCn8GdsBScMstAV34lITwibm4futFPmg8kbjKnqYtb4lVgdvnw/640?wx_fmt=png&from=appmsg)

思科于2025年12月10日得知这些攻击，证据显示利用行为可追溯到2025年11月。

## **利用活动与威胁行为者**

Cisco Talos将此次行动归功于UAT-9686（也称UNC-9686），这是一个与中国有关联的高级持续威胁行为者，基于与APT41和UNC5174等组织工具重叠的中等信心。

攻击者部署基于Python的AquaShell后门用于持久远程访问，同时使用反向SSH隧道工具如AquaTunnel和Chisel进行内部枢轴处理，以及AquaPurge用于日志清除以规避检测。目标包括电信和关键基础设施行业，后期利用重点是间谍活动而非勒索软件。

美国网络安全和基础设施安全局（CISA）于2025年12月17日将CVE-2025-20393列入其已知被利用漏洞目录，并要求联邦机构于2025年12月24日前进行缓解。截至2026年1月，尚无公开的概念验证漏洞，但自动扫描技术有所增加。

入侵迹象包括植入的持久化机制，即远程访问的隐蔽通道;思科建议通过技术支持中心（TAC）验证，并启用远程访问。

## **缓解与固定释放**

思科发布了修复漏洞并移除已知持久化机制的补丁;没有任何变通方法。管理员应立即升级，并通过网络>IP接口下的网页界面确认垃圾邮件隔离状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qw6g97TWG2CyicdwgRkc6ApW9bmQaBl8aiapL9nuKCk5OyaJebNcoU90hkMyc5Yq6TDsghGqzjBnaYA/640?wx_fmt=png&from=appmsg)

额外的加固措施包括防火墙、隔离邮件/管理接口、禁用不必要的服务如HTTP/FTP，以及使用强认证协议如SAML或LDAP。

思科安全邮件云服务保持不变。组织应外部监控日志，并联系TAC进行攻破评估。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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