---
title: 【漏洞预警】Fortinet多个产品身份验证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzAxNDM3NTM0NQ==&mid=2657044860&idx=1&sn=2ff650583175cf79e13410fbea2b633f&chksm=803fa9a2b74820b48f19d2b405d13ad5b5d149bf325eb88067a05be827a036e6211105d866c2&scene=58&subscene=0#rd
source: SecPulse安全脉搏
date: 2022-10-13
fetch_date: 2025-10-03T19:47:11.955285
---

# 【漏洞预警】Fortinet多个产品身份验证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5u08OUQmyqc5dEEiaNJf0XdeSpicAzyNcNy0ja9HnLluQoLXBricjfiaXhCKSztcNuxx8DKor4koueN1VYW6Awe23A/0?wx_fmt=jpeg)

# 【漏洞预警】Fortinet多个产品身份验证绕过漏洞

安识科技

SecPulse安全脉搏

##

1. **通告信息**

近日，安识科技A-Team团队监测到Fortinet官方发布安全公告，修复了其多个产品中的一个身份验证绕过漏洞（CVE-2022-40684），其CVSSv3评分为9.6，目前已发现被利用。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

##

2. **漏洞概述**

漏洞名称：Fortinet多个产品身份验证绕过漏洞

CVE编号：CVE-2022-40684

简述：Fortinet（飞塔）是一家全球知名的网络安全产品和安全解决方案提供商，其产品包括防火墙、防病毒软件、入侵防御系统和终端安全组件等。

在受影响的FortiOS、FortiProxy 和 FortiSwitchManager产品的管理界面中，可以通过使用备用路径或通道绕过身份验证，并在未经认证的情况下通过特制的HTTP或HTTPS请求对管理界面进行操作。

##

3. **漏洞危害**

在受影响的FortiOS、FortiProxy 和 FortiSwitchManager产品的管理界面中，可以通过使用备用路径或通道绕过身份验证，并在未经认证的情况下通过特制的HTTP或HTTPS请求对管理界面进行操作。

##

4. **影响版本**

目前受影响的 Fortinet版本：

FortiOS 版本 7.2.0 - 7.2.1

FortiOS 版本 7.0.0 - 7.0.6

FortiProxy 版本 7.2.0

FortiProxy 版本 7.0.0 - 7.0.6

FortiSwitchManager 版本 7.2.0

FortiSwitchManager 版本 7.0.0

##

5. **解决方案**

目前该漏洞已经修复。据调查，Internet 上可能存在超过 140,000 台可远程访问的 FortiGate防火墙（使用FortiOS系统），如果这些产品的管理界面也暴露于Internet，则很容易受到攻击。建议受影响用户尽快升级到以下版本：

FortiOS 版本 >= 7.2.2

FortiOS 版本 >= 7.0.7

FortiProxy 版本 >= 7.2.1

FortiProxy 版本 >= 7.0.7

FortiSwitchManager 版本 >= 7.2.1

下载链接：

https://fortiguard.fortinet.com/

缓解措施：

无法立即升级的用户可以通过禁用HTTP/HTTPS管理界面，或使用本地策略限制可以访问管理界面的IP地址来缓解此漏洞，详见参考链接中的Fortinet安全公告。

##

6. **时间轴**

【-】2022年10月10日 安识科技A-Team团队监测到漏洞公布信息

【-】2022年10月11日 安识科技A-Team团队根据漏洞信息分析

【-】2022年10月12日 安识科技A-Team团队发布安全通告

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5u08OUQmyqeMDQk5XTcSCesCTFM98kRm3Z5lyfPDmgLQDdSE5lV5t70yVhqZIXj4nCjyT8MV6pSzHmSIPZIg5A/0?wx_fmt=png)

SecPulse安全脉搏

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5u08OUQmyqeMDQk5XTcSCesCTFM98kRm3Z5lyfPDmgLQDdSE5lV5t70yVhqZIXj4nCjyT8MV6pSzHmSIPZIg5A/0?wx_fmt=png)

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