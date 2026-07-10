---
title: 0184.并非真正的 403 错误：我如何最终访问了 10 万 Azure AD 用户：我的微软研究院故事
url: https://mp.weixin.qq.com/s/IKG0_5Vg09puHS1z1gBq1g
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:46.630535
---

# 0184.并非真正的 403 错误：我如何最终访问了 10 万 Azure AD 用户：我的微软研究院故事

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BuslAqiaiaicag0ibssehpYpBLc4j9L3L8mF8Lpn0qUBiaFy8bMdzibUOYOhzWHBIVEPbCXIlv1EEiaxfv8MJDgX9BWSiaT74xOgWN1oYpc/0?wx_fmt=jpeg)

# 0184.并非真正的 403 错误：我如何最终访问了 10 万 Azure AD 用户：我的微软研究院故事

原创

Hamzadzworm
Hamzadzworm

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：403绕过

您好，又见面了。

这是 Abdelkader Mouaz，又名 Hamzadzworm。

今天我想分享一份我提交给微软安全响应中心 (MSRC) 的最有趣的报告之一。尽管这份报告最终被归类为 **“非漏洞”，** 但我认为研究过程本身值得分享。

目标

我受邀参加了一个私人漏洞赏金计划，该公司向我提供了微软凭据，让我测试他们的环境。

像往常一样，我没有只使用一个应用程序。

我开始使用同一个账户登录不同的微软服务，看看有没有什么有趣的东西。

最终，我找到了一个。

当我进入 **“用户”** 部分时，我看到的内容完全符合我的预期：

**403 禁止访问。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButH8sx2ZibkU20mIuV43taUc8fcFu3mrrIlSeib9JOicEp5iahw8Tvb6gjLdxwLNOPD72WlV1cSQg11lSs6JA95zazrqc6368qHGIQ/640?wx_fmt=png&from=appmsg)

于是我开始逐一检查应用程序发出的每一个请求。

过了一会儿，一个请求引起了我的注意。

这是一个权限验证请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvYCXMGpe7WoKia7U1lxffnOrOP4pialOHFufNvibg1Xlqc2ALgmwialZ1roWkJjsnrRib5fHYZ7APDTwk0AJ58JnG9mo541eSiadVnw/640?wx_fmt=png&from=appmsg)

出于好奇，我直接使用 Burp Suite**发送了**请求。

结果令我意外。

应用程序没有停止，而是继续加载。

几秒钟后，我看到了一个包含超过 **64,000 个 Azure Active Directory 用户的**目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89Buvsj5x9IPVuZKUCgcOib0HYZwdoB3qjVFxC4mgEjP55CcQjqVMAHcesnq86x0U0WAtddM6V74YMdkOVQ5CJ7ribSdFh56DqJwqhg/640?wx_fmt=png&from=appmsg)

还有 4 万个已删除用户

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButicWjtTSFbdgpLAo3yGAZ7RKCicXmmyLdZj7hOAnEFcmcShwbiaEiawIKJcVibcbBicjsrnPHfGlFNCYkxZSkNvddE40bvDibTmgia6mg/640?wx_fmt=png&from=appmsg)

我不仅可以浏览用户，还可以查看与每个帐户关联的信息，并导出完整的目录数据并下载。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusmX6evjmWiagibhwpUxXvaXUibMopAK57EYlBNgk0u9Sz4b4rxrJd5EqLAaLuAAq172Le5EIqDia1M7NUJOD6tyckISID4KV1oEhw/640?wx_fmt=png&from=appmsg)

那一刻，我真的相信我发现了一个严重的授权问题。
所以我把所有事情都记录了下来，录制了概念验证视频，并将报告提交给了微软。

他们的第一反应出乎我的意料。

**这是微软的初步应对措施：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuSJ3Ojh59mvHUcFjdVz7C5SS18HDMdUMYZWkiaWUB6H7wHWnzlUGa5aNydAeb5Y3FW4nY3wRq2b7nmlvq0dRrdRVib5o6SE0Iws/640?wx_fmt=png&from=appmsg)

还有一件事，在我把这个问题提交给微软之后，他们又加了一条备注：

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuukVD3w1TNa0Z11dMJYnPcLoOnyLodPLhiaNKpDdArndibTpwoDLNdicPrUwf3ZXD8KuYKgpYQyiakXbmTmwEXRxHjHrQlb4KpzUkA/640?wx_fmt=png&from=appmsg)

##

## 你怎么认为？

##

### 如果一个受限帐户被拒绝访问某个页面，但仍然可以通过操纵自己的客户端请求来访问底层目录，您认为这是一个安全漏洞吗？

###

我也遇到过类似的 PayPal 问题，稍后我会分享相关经历。敬请期待 -.-

### 期待听到您的想法和评价。

###

预览时标签不可点

阅读原文

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