---
title: 信息安全漏洞预警（2026年2月23日-2月28日）
url: https://mp.weixin.qq.com/s/EUtsKUtoEuBs3TbIdgTumA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:18:39.592756
---

# 信息安全漏洞预警（2026年2月23日-2月28日）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2xCpgJcagfibozwXdWBCRq284eggrBEriam8l798RWJHOrhTYvojicLdgEFvbHNzs1pl9kbKlK3gg6w4dJjeaTetebjlLtkCWCqVmumOsjq0S4/0?wx_fmt=jpeg)

# 信息安全漏洞预警（2026年2月23日-2月28日）

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

我司致力于持续观察与收集国内外最新的漏洞情报，重点关注CNVD、CNNVD等权威安全平台发布的漏洞公告，及时整理和收录相关漏洞信息，助力提升信息安全防护能力，保障客户系统的安全稳定运行。经过我们团队的分析和筛查，我们收录了以下安全漏洞信息。目前，相关官方机构已经发布了针对这些安全漏洞的补丁和修复方案。我们建议相关用户和组织及时关注并采取相应的安全措施，以确保信息系统的安全和稳定。收录的漏洞详细信息如下：

涉及漏洞数量：CVE漏洞： 456个；CNVD漏洞：6个 ；其它漏洞：1个；

重点关注漏洞：

### 1.ComfyUI-Manager CRLF注入漏洞

| 漏洞名称 | ComfyUI-Manager CRLF注入漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-02809 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-23 |
| 影响版本 | ComfyUI ComfyUI-Manager <3.39.2 |
| 漏洞说明 | ComfyUI是一款流行的基于节点的Stable Diffusion图形用户界面，广泛应用于AI图像生成工作流的构建和执行。ComfyUI-Manager是ComfyUI的扩展管理器插件，用于简化自定义节点、模型和依赖项的安装管理。ComfyUI-Manager存在CRLF注入漏洞，攻击者可利用该漏洞注入不安全的配置项，配合Git URL安装功能实现远程代码执行。 |
| 修复方式 | 建议升级ComfyUI-Manager至3.39.2或更高版本：https://github.com/Comfy-Org/ComfyUI-Manager/commit/f4fa394e0f03b013f1068c96cff168ad10bd0410 |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-02809 |

### 2.用友网络科技股份有限公司U8+渠道管理(高级版)存在SQL注入漏洞（CNVD-C-2025-1245200）

| 漏洞名称 | 用友网络科技股份有限公司U8+渠道管理(高级版)存在SQL注入漏洞（CNVD-C-2025-1245200） |
| --- | --- |
| 漏洞编号 | CNVD-2026-06351 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-14 |
| 影响版本 | 用友网络科技股份有限公司 U8+渠道管理(高级版) |
| 漏洞说明 | U8+渠道管理（高级版）是一套渠道管理软件，与U8+供应链系统、财务系统一道，将企业管理半径由企业内部延伸到分销渠道和销售终端。用友网络科技股份有限公司U8+渠道管理(高级版)存在SQL注入漏洞，攻击者可利用漏洞获取数据库敏感信息。 |
| 修复方式 | 厂商已发布补丁修复漏洞，请广大用户及时下载更新：https://security.yonyou.com/#/noticeInfo?id=761 |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-06351 |

### 3.Google Chrome代码执行漏洞（CNVD-2026-11751）

| 漏洞名称 | Google Chrome代码执行漏洞（CNVD-2026-11751） |
| --- | --- |
| 漏洞编号 | CNVD-2026-11751 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-25 |
| 影响版本 | Google Chrome(Linux) <144.0.7559.59；Google Chrome(Mac) <144.0.7559.60；Google Chrome(Windows) <144.0.7559.59 |
| 漏洞说明 | Google Chrome是美国谷歌（Google）公司的一款Web浏览器。Google Chrome存在代码执行漏洞，该漏洞是由ANGLE中的免费使用引起的。攻击者可利用该漏洞在系统上执行任意代码。 |
| 修复方式 | 厂商已发布了漏洞修复程序，请及时关注更新：https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop\_13.html |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-11751 |

### 4.hexchat crate has a Use After Free vulnerability

| 漏洞名称 | hexchat crate has a Use After Free vulnerability |
| --- | --- |
| 漏洞编号 | N/A |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-26 |
| 影响版本 |  |
| 漏洞说明 | All versions of this crate have function deregister\_command which can result in use after free. This is unsound. |
| 修复方式 | 建议您更新当前系统或软件至最新版，完成漏洞的修复。 |
| 相关链接 | https://github.com/advisories/GHSA-x43w-ph7m-pfjx |

### 5.Apache Kyuubi目录遍历漏洞

| 漏洞名称 | Apache Kyuubi目录遍历漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-11808 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-28 |
| 影响版本 | Apache Kyuubi >=1.6.0，<=1.10.2 |
| 漏洞说明 | Apache Kyuubi是Apache基金会的一个分布式SQL网关。Apache Kyuubi存在目录遍历漏洞，该漏洞源于客户端可绕过服务器端配置，攻击者可利用该漏洞导致访问未授权的本地文件。 |
| 修复方式 | 厂商已发布了漏洞修复程序，请及时关注更新：https://kyuubi.apache.org/releases.html |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-11808 |

### 6.Microsoft Windows Routing and Remote Access Service远程代码执行漏洞

| 漏洞名称 | Microsoft Windows Routing and Remote Access Service远程代码执行漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-11809 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-02-28 |
| 影响版本 | Microsoft Windows Server 2008；Microsoft Windows Server 2012 R2；Microsoft Windows Server 2016；Microsoft Windows Server 2019；Microsoft Windows Server 2008 R2；Microsoft Windows Server 2012；Microsoft Windows Server 2022；Microsoft Window 10 22H2；Microsoft Window 10 21H2；Microsoft Window 10 1809；Microsoft Window 10 1607；Microsoft Window 11 23H2；Microsoft Window 11 24H2；Microsoft Windows Server 2025；Microsoft Window 11 25H2 |
| 漏洞说明 | Microsoft Windows Routing and Remote Access Service是美国微软（Microsoft）公司的一种网络服务，用于实现网络路由、虚拟专用网络（VPN）和拨号连接等功能。Microsoft Windows Routing and Remote Access Service存在远程代码执行漏，攻击者可利用该漏洞在系统上执行任意代码。 |
| 修复方式 | 厂商已发布了漏洞修复程序，请及时关注更新：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62549 |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-11809 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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