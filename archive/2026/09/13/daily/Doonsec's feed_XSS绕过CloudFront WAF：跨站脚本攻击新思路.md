---
title: XSS绕过CloudFront WAF：跨站脚本攻击新思路
url: https://mp.weixin.qq.com/s/hITPQvHUXrqFs3sJZxZMzg
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:59.003331
---

# XSS绕过CloudFront WAF：跨站脚本攻击新思路

# XSS绕过CloudFront WAF：跨站脚本攻击新思路

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PysTbCytibLpYYqs8aRpejq9iaFuHjiaqVOc0mcxPCJPqu0jG2xcHfz79fSdKOMBrxbB7zml66J57akIJAlQyHOqpxicHdmoiaE8xg/640?from=appmsg)
> **导语**：安全研究人员近日公开了一种针对CloudFront WAF的XSS攻击绕过技术。该技术利用HTML标签与JavaScript URI方案的特殊组合，成功绕过WAF的基本过滤规则，在目标站点注入恶意JavaScript代码。

---

## 一、攻击背景

CloudFront是亚马逊云服务（AWS）提供的CDN与Web应用防火墙解决方案，被广泛应用于各类网站的安全防护。由于其部署规模大、覆盖面广，针对CloudFront WAF的攻防对抗一直是安全研究的热点领域。

本次公开的绕过技术聚焦于如何构造一个能让WAF"视而不见"的XSS有效载荷，使得恶意JavaScript代码在被注入目标页面后仍能正常执行。

---

## 二、有效载荷构造

以下是该研究团队使用的核心攻击载荷：

```
<目的/数据="javascript:alert/**/(document.domain)">//</object>
```

该载荷的绕过逻辑主要依赖以下两个关键技巧。

### 2.1 JavaScript URI方案与HTML标签结合

攻击者选用了`<object>`标签，并将其`data`属性值设置为JavaScript URI方案。当浏览器解析该标签时，会尝试以JavaScript方式执行`data`属性中的内容，从而触发XSS。

这里的核心技巧在于`javascript:`协议头的处理方式。

![WAF绕过原理图](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6O6FKwRHDl6GSn4HmOSQUibyxTnGD57RXgDCDGAXS8Hm3KnyFAfGN0Yz5I0jP5rpVmcKqLEEWzlwHtWrzxtC6hvBcfPiaUlsaLp8/640?from=appmsg "WAF绕过原理图")

### 2.2 冒号编码绕过检测

在标准的HTML解析中，`:`（冒号）字符可以被编码为`&colon;`实体。当WAF基于字符串匹配进行恶意代码检测时，`javascript&colon;`与原始的`javascript:`并不完全一致，因此可能被判定为"安全"而放行。

但浏览器在渲染阶段会正确解析`&colon;`为冒号，最终还原为可执行的`javascript:`协议头。

### 2.3 注释符混淆Payload特征

载荷中插入的`/**/`是CSS/JavaScript注释语法的组合。它在WAF的规则匹配层面可能打断连续字符串的识别，使得攻击特征更难被规则命中。

在代码执行层面，`/**/`作为空注释对最终行为没有影响，浏览器仍会完整执行`alert(document.domain)`调用。

---

## 三、风险评估

该绕过技术的风险等级为**中**。

其影响主要体现在以下方面：部署了CloudFront WAF且未开启AWS Managed Rules高级模式的站点，若后端应用存在XSS注入点，则可能被此类载荷突破；传统的正则匹配型WAF规则对此类编码变形攻击的防御能力有限。

---

## 四、防御建议

针对上述绕过技术，建议采取以下防御措施：

启用AWS WAF的Cross-site scripting规则时，优先选择"High"敏感度等级，并开启"Inspect HTML escaping"选项；严格限制用户输入，不依赖WAF作为唯一的XSS防护层，在服务端对所有输出进行上下文感知转义；定期审查WAF日志，对异常编码请求（如`&colon;`等HTML实体）进行标记和分析。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PJGuRM99MEBLctOeEglfZUSoIKohw8wbOibNKb7Pu9ngiaekF0GEEpS6W9phTOh34HRFg6RakLXPRRzzjK69CiaMsT9UCkiaGHwqM/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NsibTy7EPpryvDsJRdcbNNeeNicjLu48ze4kFrXJQ5t7Ph6gs30Gka9cTqZoOc0ZFh1NAak0xmqJYK9DsvLZicibibMJQ6H1OH1iaYQ/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MlbmXBPELlg46vJ2hVziaXaHic1lPLq6xcsriarxAPdJEguew8IJbS7ickX43whNLj0msBlg60ffMgcbQkZibW3QdMr2ibRa7MNj6S0/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MuFTTwcUUXbFTmf5pfg1CG8dvOJ9p2M1Quibozv7yezBTJicv6q2UZQdV0LtUn4LzbmcoZiaNjY1hQgTv4ZoiaPs1aUnd4UrFI0vU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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