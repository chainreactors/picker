---
title: Apache Tomcat 漏洞使加密拦截器绕过成为可能
url: https://mp.weixin.qq.com/s/id7KduNRt00R00JnKT2eFg
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:41:22.628881
---

# Apache Tomcat 漏洞使加密拦截器绕过成为可能

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Mib1f40hIXMTLJQUmhMU1ZTjvBxV06lOYsf8ZLhtVlpthNbABsIGaRu3nx3qJDr2VLLpBeILymZE5wS6zl4gtC8mlsOEKsXicrc/0?wx_fmt=jpeg)

# Apache Tomcat 漏洞使加密拦截器绕过成为可能

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

阿帕奇软件基金会已为阿帕奇汤姆猫发布了关键的安全更新，以解决三个新披露的漏洞。

由于 Apache Tomcat 是一款广泛部署的开源网络服务器，这些漏洞给许多企业环境带来了重大风险。

新发现的漏洞可能会让攻击者破坏加密通信、利用有缺陷的补丁以及绕过客户端证书认证。

强烈建议系统管理员查看官方通告，并应用必要的补丁以保障其网络基础设施的安全。

## **CVE-2026-29146 加密拦截填充甲骨文攻击**

安全研究人员乌里·卡茨（Uri Katz）和阿维·卢梅尔斯基（Avi Lumelsky）来自 Oligo Security，他们在 Apache Tomcat 的 EncryptInterceptor 中发现了一个重要的严重漏洞。

默认情况下，此组件使用了密码块链接（CBC）模式，这无意中使服务器暴露于填充预言攻击之下。

简单来说，填充块攻击让恶意行为者能够通过分析服务器对错误填充数据请求的响应，逐步解密被拦截的流量。
这种加密缺陷最终使攻击者能够篡改加密的会话数据。此漏洞影响以下 Apache Tomcat 版本：

Apache Tomcat 11.0.0-M1 至 11.0.18
Apache Tomcat 10.1.0-M1 至 10.1.52
Apache Tomcat 9.0.13 至 9.0.115

## **CVE-2026-34486 加密拦截器绕过漏洞**

尽管开发人员试图修补填充预言漏洞，但他们代码中的一个错误却引入了一个新的、严重的重大问题。

由 striga.ai 的巴特洛梅伊·德米特鲁克（Bartlomiej Dmitruk）发现的这一后续漏洞，使攻击者能够完全绕过 EncryptInterceptor。

由于针对 CVE-2026-29146 的初始安全修复存在缺陷，运行特定补丁版本的系统仍面临流量拦截和篡改的风险。

这凸显了在发现不完整的修复措施时迅速部署二次补丁的重要性。以下版本存在此绕过漏洞：

Apache Tomcat 11.0.20
Apache Tomcat 10.1.53
Apache Tomcat 9.0.116

CVE-2026-34486  “加密拦截器”绕过漏洞

第三个漏洞由早稻田大学的尾山春树发现，其严重程度为中等，涉及数字证书验证。

在线证书状态协议（OCSP）检查旨在验证客户端证书是否已被吊销。
然而，当使用了外部函数与内存 API（FFM）并且明确禁用了软失败功能时，这些检查仍会偶尔出现软失败。

因此，客户端证书身份验证错误地信任了可能无效的证书，未能如预期般阻止未经授权的访问。此身份验证绕过影响以下版本：

Apache Tomcat 11.0.0-M14 至 11.0.20
Apache Tomcat 10.1.22 至 10.1.53
Apache Tomcat 9.0.92 至 9.0.116

为解决这三项漏洞，Apache 软件基金会强烈建议用户立即升级其服务器环境。

系统管理员必须根据其当前的发布分支，升级到 Apache Tomcat 11.0.21 版、10.1.54 版或 9.0.117 版。

实施这些最新的软件版本将确保 EncryptInterceptor 安全运行，并且客户端证书认证能严格按照配置执行。

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