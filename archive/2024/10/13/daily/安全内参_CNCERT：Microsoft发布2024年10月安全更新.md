---
title: CNCERT：Microsoft发布2024年10月安全更新
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512787&idx=2&sn=94828a20e72077d6efa04ed68019ad56&chksm=ebfaf5f3dc8d7ce5689d1aa690a28ce53e736974c2990bc70a3a0f42a8dec3f48218dc1ce448&scene=58&subscene=0#rd
source: 安全内参
date: 2024-10-13
fetch_date: 2025-10-06T18:50:49.589187
---

# CNCERT：Microsoft发布2024年10月安全更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vRMdIERZB6PcdsF2ekKda83DgGhXoFzZNnfNUcR5w8NkpskcUyjVFP3gbYW1YIMwe1ksOLa0IIAw/0?wx_fmt=jpeg)

# CNCERT：Microsoft发布2024年10月安全更新

安全内参

编者荐语：

利用上述漏洞，攻击者可以绕过安全功能限制，获取敏感信息，提升权限，执行远程代码，或发起拒绝服务攻击等。

以下文章来源于CNVD漏洞平台
，作者CNVD

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Feicia15peMqhiakNKwwYia1jf7VRCsgbvzMKK6yMty7jEg/0)

**CNVD漏洞平台**
.

国家信息安全漏洞共享平台（China National Vulnerability Database）是由国家计算机网络应急技术处理协调中心联合重要信息系统单位、基础电信运营商、网络安全厂商、软件厂商和互联网企业建立的国家网络安全漏洞库。

安全公告编号:CNTA-2024-0016

10月9日，微软发布了2024年10月份的月度例行安全公告，修复了多款产品存在的117个安全漏洞，产品包括Windows 11、Windows 10、Windows Server 2022、Windows Server 2019、Windows Server 2008和Visual Studio Code等。

利用上述漏洞，攻击者可以绕过安全功能限制，获取敏感信息，提升权限，执行远程代码，或发起拒绝服务攻击等。CNVD提醒广大Microsoft用户尽快下载补丁更新，避免引发漏洞相关的网络安全事件。

|  |  |  |  |
| --- | --- | --- | --- |
| **CVE编号** | **公告标题** | **最高严重等级和漏洞影响** | **受影响的软件** |
| CVE-2024-43572 | Microsoft Management Console远程代码执行漏洞 | 重要  远程代码执行 | Server 2012  R2  Server 2012  Server 2008  R2  Server 2008  Server 2016  Windows 10  Server 2022  Windows 11  Server 2019 |
| CVE-2024-43488 | Visual Studio Code extension for Arduino远程代码执行漏洞 | 严重  远程代码执行 | Visual Studio  Code |
| CVE-2024-43573 | Windows MSHTML Platform欺骗漏洞 | 一般  欺骗 | Windows 11  Windows 10  Server 2022  Server 2016  Server 2012  Server 2019 |
| CVE-2024-43468 | Microsoft Configuration Manager远程代码执行漏洞 | 严重  远程代码执行 | Microsoft  Configuration Manager 2403  Microsoft  Configuration Manager 2309  Microsoft  Configuration Manager 2303 |
| CVE-2024-43582 | Remote Desktop Protocol Server远程代码执行漏洞 | 严重  远程代码执行 | Windows 11  Windows 10  Server 2022  Server 2019 |
| CVE-2024-43560 | Microsoft Windows Storage Port  Driver权限提升漏洞 | 重要  权限提升 | Server 2012 R2  Server 2012  Server 2016  Windows 10  Server 2022  Windows 11  Server 2019 |
| CVE-2024-43556 | Windows Graphics Component权限提升漏洞 | 重要  权限提升 | Server 2012 R2  Server 2012  Server 2008 R2  Server 2008  Server 2016  Windows 10  Server 2022  Windows 11  Server 2019 |
| CVE-2024-43583 | Winlogon权限提升漏洞 | 重要  权限提升 | Microsoft Copilot Studio |
| CVE-2024-43615 | Microsoft OpenSSH for Windows远程代码执行漏洞 | 重要  远程代码执行 | Windows 10  Server 2022  Windows 11  Server 2019 |
| CVE-2024-43509 | Windows Graphics Component权限提升漏洞 | 重要  权限提升 | Server 2012 R2  Server 2012  Server 2008 R2  Server 2008  Server 2016  Windows 10  Server 2022  Windows 11  Server 2019 |
| CVE-2024-43609 | Microsoft Office欺骗漏洞 | 重要  欺骗 | Office 2016  Office LTSC 2021  365 Apps for Enterprise  Office 2019  Office LTSC 2024 |
| CVE-2024-43502 | Windows Kernel权限提升漏洞 | 重要  权限提升 | Server 2019  Windows 10 |
| CVE-2024-43581 | Microsoft OpenSSH for Windows远程代码执行漏洞 | 重要  远程代码执行 | Windows 10  Server 2022  Windows 11  Server 2019 |

参考信息：

https://msrc.microsoft.com/update-guide/releaseNote/2024-Oct

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：CNVD漏洞平台

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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