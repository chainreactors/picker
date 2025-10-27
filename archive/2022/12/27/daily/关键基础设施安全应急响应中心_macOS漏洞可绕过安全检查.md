---
title: macOS漏洞可绕过安全检查
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533487&idx=3&sn=dd3652a2a41151e1db7b674816c777e5&chksm=c1e9cffef69e46e8369bb03f84136131d0798dbf7b66a069c560b29b21073927545a96dcd6f2&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-27
fetch_date: 2025-10-04T02:33:25.349261
---

# macOS漏洞可绕过安全检查

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvwTfibP77FicVLmeHHogWVx9iciaYMtKwIGvWYYDC9U80qVVhKodPjibVicXVDf22b1jJfzQ4ujKVqXnsA/0?wx_fmt=jpeg)

# macOS漏洞可绕过安全检查

关键基础设施安全应急响应中心

微软研究人员在macOS中发现一个安全漏洞，攻击者利用该漏洞可以实现安全检查绕过。

Gatekeeper是macOS中的一个安全特征，可以自动检查从互联网下载的Mac APP是经过公证的还是开发者自签名的，并要求用户在启动前进行确认或发布关于APP不可信的预警消息。

微软首席安全研究员Jonathan Bar Or在macOS Gatekeeper中发现一个安全漏洞——Achilles，漏洞CVE编号为CVE-2022-42821。攻击者利用该漏洞可以在有漏洞的macOS设备上绕过Gatekeeper的应用执行限制来部署恶意软件。

# **Gatekeeper绕过**

Gatekeeper的安全检查是通过com.apple.quarantine这个扩展属性实现的，web浏览器会对所有下载的文件分配com.apple.quarantine属性，与Windows系统的mark-of-the-web类似。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28284O2odEtDZLc00B8u2y5nBy2qYBZBqXjtf0odGFoqZTaX5h8xDI5ojygoxTwXvoVWESuOib6hmw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

攻击者可以通过精心伪造的payload来滥用其中的逻辑问题来设置ACL（访问控制列表）权限，用于拦截web浏览器和互联网下载器为下载为ZIP文件的payload设置com.apple.quarantine 属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28284O2odEtDZLc00B8u2y5UHGY4REdO4pZITQh9ia3r2dVQnG35tP7d0q90mbgxUeOAvBKMDLJudQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 设置任意访问控制列表的代码

因此，压缩文件中的恶意payload中的恶意APP可以在受害者系统上启动而不会被Gatekeeper 拦截，攻击者即可以下载和部署恶意软件。

使用ACL绕过Gatekeeper的PoC视频参见：https://www.microsoft.com/en-us/videoplayer/embed/RE5dQo5

12月13日，苹果已在macOS 13 (Ventura)、macOS 12.6.2 (Monterey)、macOS 1.7.2 (Big Sur)系统中修复了该漏洞。微软称，苹果在macOS Ventura系统中引入的Lockdown Mode对定向复杂网络攻击的高风险用户是一个可选的保护特征，该特征旨在组织零点击的远程代码执行漏洞利用，因此无法应对Achilles漏洞。无论Lockdown Mode的状态如何，终端用户都应当尽快安装补丁。

完整技术细节参见：

https://www.microsoft.com/en-us/security/blog/2022/12/19/gatekeepers-achilles-heel-unearthing-a-macos-vulnerability

**参考及来源：**

https://www.bleepingcomputer.com/news/security/microsoft-finds-macos-bug-that-lets-malware-bypass-security-checks/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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