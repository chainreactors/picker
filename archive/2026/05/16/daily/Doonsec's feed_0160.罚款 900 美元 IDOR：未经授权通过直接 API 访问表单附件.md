---
title: 0160.罚款 900 美元 IDOR：未经授权通过直接 API 访问表单附件
url: https://mp.weixin.qq.com/s/AtqGYtDbbb4K0R-KpMuBuA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:46:18.121808
---

# 0160.罚款 900 美元 IDOR：未经授权通过直接 API 访问表单附件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MW9pCm89BuvDLiaAZOOkkl2U8LTtssm2eeIfjiclVUl0tYqJccZP1j5rJFTWUqreUib4zlH6Q5jpgib1T3swD1rTNc4HA7hCseA4Cc9WKq5Dicgo/0?wx_fmt=jpeg)

# 0160.罚款 900 美元 IDOR：未经授权通过直接 API 访问表单附件

原创

Abhi Sharma
Abhi Sharma

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：IDOR

大家好！在测试一个 SaaS 平台（ **ExampleCenter** ）时，我发现了一个**授权绕过漏洞**，该漏洞允许低权限用户从他们无权访问的表单中下载文件附件。

我因此获得了 **800 美元的赏金和 100 美元的复测奖金**。起初，这看起来像是一个简单的端点问题，但深入研究后，我发现它实际上是一个典型的 **IDOR 漏洞，具有枚举潜力**。让我们来详细分析一下。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuupXmsMicicptCwDZiaMozGOj91vUajljmFpdUPc7k2dUjrG1fzaH6y1aiaicPFUDNdCWbafaE2NMYfzP6t0MS4XNOLicicvc1n2V0QAc/640?wx_fmt=png&from=appmsg)

## 了解目标

ExampleCenter 提供了一个**人员/表单系统**，组织可以通过表单收集数据。

这些表格通常包含：

* 个人文件
* ID
* 同意书
* 敏感用户信息

访问控制旨在确保：

* 只有授权用户才能查看表单提交内容。
* 只有拥有相应权限的用户才能访问附件。

我使用**查看者级别的帐户**进行了测试，结果如下：

* ❌ 无法访问目标表单
* ❌ 无法查看提交内容
* ❌ 无法通过用户界面下载附件。

所以从用户界面角度来看——一切看起来都很安全。

## 引发漏洞的想法

在检查网络流量时，我注意到文件下载是通过直接端点进行的。

这让我想到：

> *“如果后端只检查附件 ID，而不检查实际权限呢？”*

所以我决定手动测试。

## 缺陷：直接访问附件

我使用 **Viewer 用户**的有效会话构造了一个请求：

```
GET /form_submission_value/{attachment_id}/attachments?attachment_name={attachment_name} HTTP/2Host: api.examplecenter.comCookie: session=<viewer_session>
```

## 我的预期与实际发生的情况

我原本以为会收到 403 Forbidden 或 Access denied 错误，但实际上我收到了 **200 OK — 文件下载成功。**

虽然：

* 我无法访问该表格。
* 我在用户界面中看不到提交的内容。

👉 我仍然可以下载附件

## 缺失的一环：枚举

分析师提出了一个重要的问题：

> *如何获取附件名称？*

而这正是这个漏洞变得更有趣的地方👇

##

## 枚举可能性

* attachment\_id → 顺序
* Attachment\_name → 可猜测/可枚举
* 端点无速率限制

👉 这会导致暴力破解/枚举攻击

攻击者可以：

* 迭代 ID
* 尝试使用常见的文件名
* 提取有效附件

## 为什么这很重要

即使统计工作需要付出努力，但其影响却十分重大，因为：

👉 一旦找到有效参数 →**即可完全访问文件**

##

## 根本原因

这是一场经典的 IDOR：

> *后端授权仅依赖于对象引用（attachment\_id 和 attachment\_name）。*

缺少支票；

* 用户是否有权访问该表单？
* 用户是否有权提交内容？
* 该用户是否允许上传此附件？

👉 无需授权验证

##

## 影响

此漏洞会导致：

### 保密性影响

* 访问敏感文件和图像
* 个人用户数据的泄露

### 数据泄露

* ID
* 医疗表格
* 私人投稿

### 隐私风险

* 违反用户信任
* 未经授权的数据披露

##

## 赏金与计划响应

* 报告日期：2026 年 1 月 6 日
* 说明：枚举解释
* 分诊日期：2026 年 1 月 13 日
* 严重程度：中等（基于 CVSS 评分）
* 赏金：800 美元 + 100 美元奖金
* 重新测试：修复已确认

**![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusPeQGwShu4fAwQ3Fdd8nicJKBJ0s4dxxonyXaNXicfjsDofT1OEcvl4XNl8UjibKfGExnic5mXHGVicc5Rte1dZBjib3Eh73jn20WCw/640?wx_fmt=png&from=appmsg)**

## 要点总结

* 务必测试**直接下载端点。**
* IDOR 通常隐藏在以下功能背后：文件下载、媒体访问和附件
* 不要止步于“需要一个参数”——测试枚举
* 缺乏速率限制可能会将低级漏洞转化为真正的攻击。
* 即使对参数进行部分控制，也可能导致数据泄露。

##

## 个人见解

这个漏洞源于一种非常简单的思维方式：

> *“如果我无法在用户界面中访问它……我还能直接获取它吗？”*

单单这个问题就会导致很多现实世界中的漏洞。

##

## 结论

该漏洞凸显了仅依赖**对象标识符而没有进行适当授权检查**是多么危险。

尽管用户界面正确地限制了访问权限，但后端允许直接检索敏感文件，完全绕过了访问控制。

这类错误非常常见，尤其是在处理上传和文档的系统中。

请始终记住：

> *如果一个端点返回一个文件……它必须验证是谁在请求该文件，否则你就可以获得赏金。*

下次再见——祝你编程愉快！🚀

##

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

Rsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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