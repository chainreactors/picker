---
title: Microsoft Teams 漏洞可导致黑客实施欺骗攻击
url: https://mp.weixin.qq.com/s/pzRVNuZP6l7TxzPZV0Ta4g
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:44:23.231665
---

# Microsoft Teams 漏洞可导致黑客实施欺骗攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1ZVutibjR516vcjn6FyOlL3RHTHZiasw24AX56fCwUprRrJJtKxTkicvC5sR3voN2MC7dl5NDibN6uud10xsjkj9Ig9V8ypHRqFaI/0?wx_fmt=jpeg)

# Microsoft Teams 漏洞可导致黑客实施欺骗攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1UqGNkkk9bthfXa0m7oD2vLCfxsiaeNJJVebWsFg37oPghUKSI8YUQOR3SzJNlBYHp2elwOu7Pj3dFicN2HwT0WmHVVEsbpavDI/640?wx_fmt=jpeg)

##

微软 Teams 近日披露的安全漏洞可能允许攻击者伪造本地设备，这对依赖该平台进行日常通信的企业和个人用户构成安全隐患。

2026年5月12日，微软通过协调披露机制在其月度补丁日公告中公开了该漏洞（CVE-2026-32185）。该漏洞暴露了 Microsoft Teams 处理文件和目录访问时的关键缺陷，攻击者可借此操纵或伪装应用程序内的可信元素。

**Part01**

## ****漏洞技术分析****

该漏洞本质源于 Microsoft Teams 中的文件或目录可被外部访问。这种错误配置使未经授权的本地攻击者能够实施欺骗攻击，诱骗用户信任看似合法的恶意内容或通信。

虽然攻击需要用户交互且仅限于本地攻击媒介，但其对数据机密性的潜在影响被评为"高危"，这对敏感的企业环境构成严重威胁。该漏洞 CVSS 3.1 基础评分为5.5，环境调整后评分为4.8，微软将其严重性评级为"重要"。

值得注意的是，利用此漏洞无需任何特权，这降低了攻击者在共享或已遭入侵的本地环境中实施攻击的门槛。截至发布日期，该漏洞尚未被公开披露或发现在野利用。

**Part02**

## ****修复与缓解措施****

微软已通过 Google Play 商店为 Android 版 Microsoft Teams 发布安全更新（已修复版本号：1.0.0.2026092103）。微软将漏洞可利用性评估为"不太可能被利用"，且尚未确认存在 PoC 利用代码。修复级别标记为"官方补丁"，意味着相关更新已发布。

安全研究人员 Ofek Levin（来自 Enclave）通过协调披露机制向微软报告了该漏洞。建议用户和管理员立即通过 Google Play 商店更新至最新版本。在受监管或高安全性环境中部署 Microsoft Teams 的组织应优先处理此补丁，特别是将 Teams 用于业务通信的移动终端设备。

**参考来源：**

Microsoft Teams Vulnerability Allows Hackers to Perform Spoofing Attacks

https://cybersecuritynews.com/microsoft-teams-vulnerability-spoofing/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

内容含AI生成图片

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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