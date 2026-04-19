---
title: 针对 FortiSandbox 漏洞的 PoC 攻击程序已发布，该漏洞允许攻击者执行命令
url: https://mp.weixin.qq.com/s/Ef_u1QqqbTLK4Yf6uRmhFg
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:08.024312
---

# 针对 FortiSandbox 漏洞的 PoC 攻击程序已发布，该漏洞允许攻击者执行命令

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Nh45yXEMbiaIwgN0JL6mjETWNicqDeoeY0hvMgicU84rWc5CqJggya9GzdjKGzJICMbKIANDPdPEKibCUVzoBz0DU3mGicAZmcNqI4/0?wx_fmt=jpeg)

# 针对 FortiSandbox 漏洞的 PoC 攻击程序已发布，该漏洞允许攻击者执行命令

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Fortinet 的 FortiSandbox 产品中一个严重漏洞（编号为 CVE-2026-39808）的概念验证 (PoC) 漏洞利用程序已公开发布。

该漏洞允许未经身份验证的攻击者以 root 用户（最高权限级别）身份执行任意操作系统命令，而无需任何登录凭据。

该漏洞最初于 2025 年 11 月被发现，在 Fortinet 于 2026 年 4 月发布补丁后，现已公开。

安全研究人员和防御人员被敦促立即应用此修复程序，因为目前 GitHub 上已免费提供可用的漏洞利用程序。

CVE-2026-39808 是一个 操作系统命令注入漏洞， 影响 Fortinet 的 FortiSandbox，这是一款广泛使用的沙箱解决方案，旨在检测和分析高级威胁和恶意软件。该漏洞存在于 `/fortisandbox/job-detail/tracer-behavior` 终端设备中。

## **这种攻击有多简单？**

攻击者可以通过GET 参数 注入恶意操作系统命令，这是在基于 Unix 的系统中`pipe symbol (|)`用于链接命令的常见技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Ou7WIUhJQW2wVhbR2qYn3JiaTBuFJIIgAXdGiaS8A8biaYvrVMApF1UPQgDo1DwfuFV0Np130JHW2zwVGonkrpDwI2PnRhrkxe9I/640?wx_fmt=png&from=appmsg)

由于存在漏洞的端点未能正确清理用户输入，注入的命令由底层操作系统以 root 权限直接执行。

经确认，FortiSandbox 版本 4.4.0 至 4.4.8 受此漏洞影响。

CVE-2026-39808 最令人担忧的地方在于它很容易被利用。

据在 GitHub 上发布 PoC 的研究员 samu-delucas 称，只需一条 curl 命令即可实现未经身份验证的远程代码执行 (RCE)，且权限为 root 用户：

`curl -s -k --get "http://$HOST/fortisandbox/job-detail/tracer-behavior" --data-urlencode "jid=|(id > /web/ng/out.txt)|"`

在这个例子中，攻击者将命令输出重定向到存储在网站根目录中的文件，然后可以通过浏览器检索该文件。

这意味着攻击者无需登录即可读取敏感文件、植入恶意软件或完全控制主机系统。

## **Fortinet的回应**

Fortinet 已修复该漏洞，并通过其 FortiGuard PSIRT 门户网站发布了 FG-IR-26-100 号官方公告。

该安全公告确认了漏洞的严重性，并列出了受影响的版本。运行 FortiSandbox 4.4.0 至 4.4.8 版本的组织应立即升级到已修复的版本。

* **立即修复：** 按照 Fortinet 官方公告中的说明，将 FortiSandbox 升级到 4.4.8 以上的版本。
* **审核暴露实例：**检查 FortiSandbox 管理接口是否暴露于不受信任的网络或公共互联网。
* **查看日志：**  查找对 `/fortisandbox/job-detail/tracer-behavior` 端点的异常 GET 请求，以此作为攻击尝试的指标。
* **应用网络分段：**将对 FortiSandbox 管理接口的访问限制为仅允许受信任的 IP 范围。

由于可用的概念验证版本已公开发布，漏洞利用窗口已经打开。安全团队应将此视为重中之重的补丁，并立即采取行动保护受影响的系统。

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