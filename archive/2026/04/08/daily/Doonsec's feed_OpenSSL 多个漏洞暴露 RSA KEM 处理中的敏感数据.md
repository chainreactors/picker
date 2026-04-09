---
title: OpenSSL 多个漏洞暴露 RSA KEM 处理中的敏感数据
url: https://mp.weixin.qq.com/s/V_g-AuLrA_ouHPjFIFhm5w
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:36.529327
---

# OpenSSL 多个漏洞暴露 RSA KEM 处理中的敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MYzicfoQBiaCNeWHj3JRsKVr3swr0oj8hic8O0XLTHoiaS3zPw8MXKOibqvgPMicvCmN4CR3Kt2qtice2EXibsZfibJAESXXsLLQSkriaOY/0?wx_fmt=jpeg)

# OpenSSL 多个漏洞暴露 RSA KEM 处理中的敏感数据

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

OpenSSL中新披露的一个漏洞可能允许攻击者访问存储在应用程序内存中的敏感数据。

该漏洞编号为 CVE-2026-31790，属于中等严重性漏洞，会影响 RSA 密钥封装机制 (KEM) RSASVE 封装的处理。

OpenSSL于2026年4月7日发布安全公告，敦促用户立即应用补丁。核心问题在于加密过程中故障处理不当。

当应用程序使用 RSASVE 密钥封装来建立秘密加密密钥时，它们依赖特定的函数来验证密钥是否成功。然而，由于编码疏忽，系统无法正确验证返回值。

## **漏洞利用原理**

该缺陷存在于 RSA\_public\_encrypt() 函数中，该函数本应返回成功时写入的字节数，或者在出错时返回 -1 。

然而，受影响的代码仅检查返回值是否不为零。如果 RSA 加密失败并返回 -1，系统就会错误地将其登记为成功（尽管实际上并非如此）。

这种误报促使封装过程继续进行。应用程序设置输出长度，并将密文缓冲区视为已生成有效密钥。

如果攻击者提供无效的 RSA 公钥，并且应用程序未能首先验证它，则系统将处理该错误并将缓冲区中未初始化的内容泄露回攻击者。

这种过时的内存可能包含来自先前应用程序进程的高度敏感数据。

红帽公司的 Simo Sorce于 2026 年 2 月报告了该漏洞，Nikola Pajkovsky 开发了修复程序。旧版本的 OpenSSL，特别是 1.0.2 和 1.1.1 版本，完全不受此漏洞的影响。

如果您正在运行受影响的版本（包括相应的 FIPS 模块），则必须升级到最新的已修补版本。

可用的安全更新包括：

* OpenSSL 3.0 用户应升级到 3.0.20 版本。
* OpenSSL 3.3 用户应升级到 3.3.7 版本。
* OpenSSL 3.4 用户应升级到 3.4.5 版本。
* OpenSSL 3.5 用户应升级到 3.5.6 版本。
* OpenSSL 3.6 用户应升级到 3.6.2 版本。

无法立即修复系统的管理员可以实施代码层面的变通方案。开发人员必须确保其应用程序在处理公钥之前对其进行验证。

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