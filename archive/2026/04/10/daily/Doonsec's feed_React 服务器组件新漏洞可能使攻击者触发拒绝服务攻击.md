---
title: React 服务器组件新漏洞可能使攻击者触发拒绝服务攻击
url: https://mp.weixin.qq.com/s/aZCyNZxktA4BAeNSDvfezg
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:16:39.316208
---

# React 服务器组件新漏洞可能使攻击者触发拒绝服务攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NwgTYbK2ns9icgttyEicxm7XqvIWFG3sod82UWfgST8icFmicoAUtFaAvpWcURofVBMkibazHTZLK8eonC718DDC2WTZxSnUPnic3icI/0?wx_fmt=jpeg)

# React 服务器组件新漏洞可能使攻击者触发拒绝服务攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

React 服务器组件中新披露的一个高危漏洞可能允许未经身份验证的攻击者触发拒绝服务 (DoS)攻击。

该漏洞编号为 CVE-2026-23869，对使用特定服务器端渲染包的 Web 应用程序构成重大风险。

由于该漏洞利用不需要任何特权，且攻击复杂度较低，因此威胁行为者可以很容易地通过网络攻击易受攻击的服务器，从而扰乱业务运营。

## **了解漏洞利用**

该漏洞被归类为不受控制的资源消耗问题（CWE-400），并且还与不安全的反序列化实践（CWE-502）有关。

威胁行为者可以通过向 React 服务器函数端点发送特制的 HTTP 请求来触发此漏洞。

当易受攻击的服务器收到此恶意载荷时，它会尝试处理请求，从而导致 CPU 使用率大幅飙升。

单个请求就可能导致 CPU 使用率过高，持续长达一分钟，最终才会抛出可捕获的错误。如果攻击者持续发送这类精心构造的请求，服务器的处理能力将迅速耗尽。

资源耗尽导致应用程序无法处理合法用户流量，从而造成应用程序停机和用户体验完全中断。

该漏洞专门针对流行的 Web 打包工具使用的服务器端文档对象模型 (DOM) 包。

如果您的应用程序依赖于 React 服务器组件，则必须检查项目依赖项中是否包含以下 npm 包：

* `react-server-dom-parcel`
* `react-server-dom-turbopack`
* `react-server-dom-webpack`

这三个软件包的三个活跃版本中都存在此漏洞：

* 版本 19.0.0 至 19.0.4
* 版本 19.1.0 至 19.1.5
* 版本 19.2.0 至 19.2.4

React 开发团队已成功将安全修复程序移植到旧版本，以解决不受控制的资源消耗漏洞。

为保护您的基础架构免受潜在的拒绝服务攻击，管理员必须立即将受影响的 npm 包升级到以下已修补的版本：

* 更新至版本 19.0.5
* 更新至版本 19.1.6
* 更新至版本 19.2.5

需要注意的是，并非所有 React 应用都存在风险。该漏洞仅限于运行 React 服务器组件的环境。

如果您的 React 应用完全在客户端运行，没有服务器端，则不会受到影响。同样，如果您的应用未使用任何支持 React 服务器组件的框架、打包工具或打包插件，则可以忽略此警告。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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