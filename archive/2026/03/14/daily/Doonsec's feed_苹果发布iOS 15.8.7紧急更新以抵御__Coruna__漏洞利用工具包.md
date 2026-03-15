---
title: 苹果发布iOS 15.8.7紧急更新以抵御\"Coruna\"漏洞利用工具包
url: https://mp.weixin.qq.com/s/Hk80EXyFWsd1ypA3eakxow
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:58.302935
---

# 苹果发布iOS 15.8.7紧急更新以抵御\"Coruna\"漏洞利用工具包

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJns1NBsE1GfqrDbRZtuABnAyPE4QCoiaoeWqBibT6HQric31Pg2nn4ghliawiaqstLr1nxibtQkpwsYE3gT7dE8u0hkj708MQFVAlUuQI/0?wx_fmt=jpeg)

# 苹果发布iOS 15.8.7紧急更新以抵御"Coruna"漏洞利用工具包

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvb6R05V2TJcX18dPkuXwxdXJ9REFcGfDFYKoZkRiaTIVwtb6KNqpJ8lY0Uj1p8HjnOB5okwCGJUca8amJjyaWpXSD0LvaLGw3Q/640?wx_fmt=jpeg&from=appmsg)

苹果公司已紧急发布安全更新 **iOS 15.8.7 和 iPadOS 15.8.7**，旨在保护旧款设备免受名为 **“Coruna”漏洞利用工具包** 的严重威胁。

该关键补丁于 **2026年3月11日** 发布，将新版本 iOS 的修复程序**回传至旧版系统**，确保使用老旧硬件的用户不会暴露于高级网络攻击之下。

**“Coruna”漏洞利用工具包** 通过**链式利用多个漏洞**攻击苹果设备：

* 同时针对设备**核心操作系统（内核）** 与 **WebKit 浏览器引擎**
* 攻击者仅需诱使用户访问恶意网站，即可**完全控制**受影响的 iPhone 或 iPad

### 更新背景

* 苹果此前已于 **2023年7月至2024年1月** 间在 iOS 16 和 iOS 17 中修复了这些漏洞。
* 但威胁行为者正通过 **“Coruna”工具包** 积极**将遗留漏洞武器化**。
* 本次更新是苹果为**无法升级至最新系统**的旧设备推送的必要关键补丁。

### 受影响设备

iPhone 6s、iPhone 7、iPhone SE（第一代）、iPad Air 2、iPad mini（第四代）、iPod touch（第七代）

### 修复的四大安全漏洞

| 漏洞类型 | CVE 编号 | 技术细节 |
| --- | --- | --- |
| **内核漏洞** | CVE-2023-41974 | 研究员 Félix Poulin-Bélanger 发现的**释放后重用内存问题**。恶意应用可借此以**最高系统权限执行任意代码**。修复方式：改进内存管理。 |
| **WebKit 类型混淆** | CVE-2024-23222 | WebKit 渲染引擎漏洞，用户处理恶意网页内容时**可执行任意代码**。修复方式：实施更严格的验证检查。 |
| **WebKit 内存损坏** | CVE-2023-43000 | WebKit 中的**释放后重用漏洞**，解析恶意网页时导致内存损坏。修复方式：增强内存管理技术。 |
| **WebKit 内存损坏** | CVE-2023-43010 | 恶意网页内容触发的另一严重 WebKit 问题，同样导致内存损坏。修复方式：优化内存处理协议。 |

### 风险说明

* 由于 **“Coruna”依赖网页攻击**，用户仅需**浏览网页或点击短信链接**即面临风险。
* **WebKit 漏洞（初始访问）** 与 **内核漏洞（权限提升）** 的组合构成**高度关键威胁**。

### 行动要求

**所有受影响设备的用户必须立即通过设备设置下载并安装 iOS 15.8.7 或 iPadOS 15.8.7 更新**，以防御已知漏洞利用。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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