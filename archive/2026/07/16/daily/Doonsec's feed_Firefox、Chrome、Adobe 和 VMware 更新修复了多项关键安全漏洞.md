---
title: Firefox、Chrome、Adobe 和 VMware 更新修复了多项关键安全漏洞
url: https://mp.weixin.qq.com/s/Kndq5ayLaknllpu48PedcA
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:39.065053
---

# Firefox、Chrome、Adobe 和 VMware 更新修复了多项关键安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsibEmDdwwHUxnNFiafmfySicprdf1icUATWibeicNIDpeSygkO9ZlWK2an6tW6tiaticuxf61rhVF7FntAkia7uDzodklOuFMCnmfOHuibFY/0?wx_fmt=jpeg)

# Firefox、Chrome、Adobe 和 VMware 更新修复了多项关键安全漏洞

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADsicbib0zjPJfic5INHibtFDJYDprfnSGLYA2LjxBzPmjd7lcTnV3zvyc1aYXRBwqGUfjiaPu07XbFIAvbiaTicStoEFTibNPNbos31aI8E/640?wx_fmt=jpeg&from=appmsg)

Mozilla发布了更新，修复Firefox中的两个关键缺陷，之前警告说漏洞利用代码已被公开。

漏洞列表如下——

* **CVE-2026-15718，JavaScript**

  ： WebAssembly 组件中的一个无效指针
* **CVE-2026-15719，DOM**

  中的站点隔离：导航组件

Mozilla在一份公告中表示：“我们知道针对此的漏洞利用代码是公开的，但我们并未发现任何在野外利用这一漏洞的攻击。”这两个漏洞均已在 Firefox 152.0.6 版本中得到修复。

此次发布之际，谷歌修复了15个安全漏洞，其中包括Ozone中存在的两个关键漏洞（CVE-2026-15764和CVE-2026-15765），该跨平台抽象层允许浏览器原生与各种显示服务器和窗口系统交互。它支持 Linux、ChromeOS 和 Fuchsia。

根据NIST国家漏洞数据库（NVD）中CVE-2026-15764的描述，Linux版150.0.7871.125之前，在Ozone中使用After Free功能，使远程攻击者能够说服用户通过特定的UI手势，可能通过精心设计的HTML页面利用堆损坏。”

这些缺陷已在 Windows 和 Mac 的 Chrome 版本 150.0.7871.124/.125 以及 Linux 版本 150.0.7871.124 中得到修补。

在相关进展中，Adobe 发布了针对 88 个漏洞的安全更新，其中包括 ColdFusion、Commerce、Experience Manager 和 Illustrator 中的多个严重严重性漏洞。其中八台是Adobe冷融合 -

* **CVE-2026-48318**

  （CVSS 评分：9.9）——一个可能导致任意代码执行的路径穿越漏洞
* **CVE-2026-48322**

  （CVSS 评分：9.6）——一个可能导致任意代码执行的代码注入漏洞
* **CVE-2026-48284**

  （CVSS 评分：9.6）——一个不当输入验证漏洞，可能导致任意代码执行
* **CVE-2026-48321**

  （CVSS 评分：9.3）——一个错误的授权漏洞，可能导致权限升级
* **CVE-2026-48325**

  （CVSS 评分：9.3）——一个关键功能漏洞的缺失认证，可能导致任意代码执行
* **CVE-2026-48319**

  （CVSS 评分：9.1）——一种可能导致任意代码执行的路径穿越漏洞
* **CVE-2026-48324**

  （CVSS 评分：9.1）——一个可能导致任意代码执行的SQL注入漏洞
* **CVE-2026-48327**

  （CVSS 评分：9.0）——一个错误授权漏洞，可能导致任意代码执行

CodeFusion 的缺陷已在 ColdFusion 2025 更新 11 和 ColdFusion 2023 更新 22 中得到修复。Adobe 还修复了 Adobe Commerce 和 Magento 开源以及 Adobe Experience Manager 中的两个关键缺陷 -

* **CVE-2026-48356**

  （CVSS 评分：9.6）——Adobe Commerce 和 Magento 开源中的一个文件上传漏洞，可能导致权限升级
* **CVE-2026-48358**

  （CVSS 评分：9.1）——Adobe Commerce 和 Magento 开源中输出漏洞的不当编码或逃逸，可能导致任意代码执行
* **CVE-2026-48259**

  （CVSS 评分：9.6）——Adobe Experience Manager 中的一个服务器端请求伪造漏洞，可能导致任意代码执行
* **CVE-2026-48359**

  （CVSS 评分：9.6）——Adobe Experience Manager 中对 XML 外部实体引用的不当限制，可能导致任意代码执行

此外，博通发布了针对VMware Avi负载均衡器（**CVE-2026-47865，CVSS**评分：9.8）中一个关键认证绕过漏洞的修复，该漏洞可被拥有网络访问权限的恶意用户利用以访问Avi控制平面。北约网络安全中心（NCSC）的菲利普·韦滕斯被认为发现并报告了这一漏洞。

虽然这些漏洞尚未被标记为被主动利用，但鉴于威胁行为者常利用这些产品中的缺陷进行攻击，组织安装最新更新至关重要。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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