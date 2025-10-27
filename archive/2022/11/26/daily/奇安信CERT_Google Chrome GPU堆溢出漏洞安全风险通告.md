---
title: Google Chrome GPU堆溢出漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497113&idx=1&sn=76113d2d01432b6eb1b383fd9123b857&chksm=fe79d101c90e5817e6503ca34cff483174d26805c184492edf297d314c1c91f2316edbe96f4c&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2022-11-26
fetch_date: 2025-10-03T23:50:01.383348
---

# Google Chrome GPU堆溢出漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icVIdJHZMBTBAEzzlMb4wdT0gLRSZzgbsCUciadicwPdLKmIVfZrA1iafTB6Uib08XQjdIuMdTGFvCVWA/0?wx_fmt=jpeg)

# Google Chrome GPU堆溢出漏洞安全风险通告

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

近日，奇安信CERT监测到Google官方发布**Google Chrome GPU堆溢出漏洞(CVE-2022-4135)**通告，Google Chrome GPU进程存在堆溢出漏洞，成功利用此漏洞可导致在应用程序上下文中执行任意代码。目前，**Google已发现此漏洞被用于在野攻击**。**鉴于此漏洞影响较大，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Google Chrome GPU****堆溢出漏洞** | | |
| **公开时间** | 2022-11-24 | **更新时间** | 2022-11-25 |
| **CVE****编号** | CVE-2022-4135 | **其他编号** | QVD-2022-45069 |
| **威胁类型** | 代码执行 | **技术类型** | 堆缓冲区溢出 |
| **厂商** | Google | **产品** | Chrome |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | **已发现** | 未公开 |
| **漏洞描述** | Google Chrome GPU 进程存在堆溢出漏洞，利用此漏洞需要用户交互，成功利用此漏洞可导致在应用程序上下文中执行任意代码。 | | |
| **影响版本** | Google Chrome < 107.0.5304.121 | | |
| **不受影响版本** | Google Chrome >= 107.0.5304.121 | | |
| **其他受影响组件** | 基于Chromium的浏览器 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Google Chrome GPU堆溢出漏洞 | | | |
| **CVE****编号** | CVE-2022-4135 | **其他编号** | | QVD-2022-45069 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 8.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 无 | | 需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | Google Chrome GPU存在堆溢出漏洞，利用此漏洞需要用户交互，成功利用此漏洞可导致在应用程序上下文中执行任意代码。**目前，谷歌已发现此漏洞被用于在野攻击。** | | | |

处置建议

目前，Google Chrome已发布新版本（Google Chrome for Mac /Linux 107.0.5304.121、Google Chrome for Windows 107.0.5304.121/.122），建议用户尽快升级至最新版本。

**版本检测及升级步骤：**

1． 查看右上角的“更多”图标，选择帮助 -> 关于Google Chrome

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icVIdJHZMBTBAEzzlMb4wdT3RbJtlgZJvhibr3yLRPbIdtrM9PyYy2ucuiahLh2zZc1HzUgspz0OuFQ/640?wx_fmt=png)

2． 等待下载完成后，选择重新启动

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icVIdJHZMBTBAEzzlMb4wdTJRXjmJJKzVsEuiaiap9soick8KCY5wazpBuWs87ic5lFKGbLOy7sib7PuOA/640?wx_fmt=png)

3． 查看当前版本

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icVIdJHZMBTBAEzzlMb4wdT6AlcBXORNvbzCmd4icXtHAg7MhyIyDzzicZ8icRsR9MeJg7C31bXp9H9g/640?wx_fmt=png)

参考资料

[1]https://chromereleases.googleblog.com/2022/11/stable-channel-update-for-desktop\_24.html

时间线

2022年11月25日，奇安信 CERT发布安全风险通告。

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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