---
title: Docker授权绕过漏洞使主机暴露于潜在攻击者之下
url: https://mp.weixin.qq.com/s/eQqEBMIGW3MNcoGWiuVKEw
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:31.220086
---

# Docker授权绕过漏洞使主机暴露于潜在攻击者之下

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MXBXic5iaAMicDSmPtKQjKNNqbj81HneI8hfrWXfrbptaNoVQwLNS5BvZm7Ld1ZzRpMwBzMIVibP4EjPg5Rbj2akWUaXNARCwJCsA/0?wx_fmt=jpeg)

# Docker授权绕过漏洞使主机暴露于潜在攻击者之下

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Docker Engine 中发现了一个高危安全漏洞，该漏洞可能使主机面临授权绕过攻击的风险。

该漏洞编号为 CVE-2026-34040，攻击者可以通过操纵 API 请求正文来绕过授权插件 (AuthZ)。

虽然该漏洞被利用的可能性仍然很低，但其严重性评级为“高”。

它尤其会影响依赖 AuthZ 插件根据传入请求正文的内容做出访问控制决策的环境。

## **Docker 授权绕过漏洞**

问题的核心在于Docker 守护进程如何处理过大的请求体。拥有底层访问权限的攻击者可以向系统发送精心构造的 API 请求。

这会触发一个缺陷，即 Docker 守护进程会将请求转发给活动的授权插件，但会剥离请求正文。

由于 AuthZ 插件缺少正确评估请求所需的数据，因此它可能会允许通常会阻止的操作。

从本质上讲，安全守门人被迫做出盲目决定，导致恶意指令在不被察觉的情况下溜走。

安全研究人员指出，此漏洞源于对先前 Docker 授权缺陷（编号为 CVE-2024-41110）的不完整修复。

此漏洞仅影响主动使用 AuthZ 插件的用户。如果您的 Docker 环境不依赖这些插件进行安全检查，则您的系统不会受到此特定攻击的影响。

该漏洞影响 29.3.1 之前的所有 Docker Engine 版本。由于该攻击需要本地访问和低权限，因此被入侵的容器或受限用户帐户可能会利用此漏洞提升权限、更改主机配置或访问敏感数据。

为确保受影响系统的安全，管理员应立即升级到 Docker Engine 版本 29.3.1，该版本包含官方补丁。

如果无法立即更新，安全团队可以实施以下变通方案：

* 停止使用依赖请求体检查进行安全决策的授权插件。
* 严格限制对 Docker API 的访问，只允许受信任的各方访问，并强制执行最小权限原则。

该漏洞由安全研究人员团队负责任地披露，修复工作由 Docker 开发社区牵头。

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