---
title: Trivy 漏洞利用中的恶意脚本注入可导致凭证窃取
url: https://mp.weixin.qq.com/s/JxyglSZxEBwxEJIfP9yDbQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:14:34.964356
---

# Trivy 漏洞利用中的恶意脚本注入可导致凭证窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NPyaq4sLAL2n7FuD0hwYfyia2bqSRMibyKLodHZROaNC1jIqt36X1Jlw4dBsAIrMTNHVxtDcob7bdeQvpyFfXiag3cQ4ULmcQxcc/0?wx_fmt=jpeg)

# Trivy 漏洞利用中的恶意脚本注入可导致凭证窃取

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

针对官方 Trivy GitHub Action ( ) 的复杂供应链攻击`aquasecurity/trivy-action`已导致全球持续集成和持续部署 (CI/CD) 管道遭到破坏。

该事件于 2026 年 3 月下旬披露，标志着 Trivy 生态系统在一个月内遭受的第二次重大安全漏洞。

攻击者成功强制推送了 76 个现有版本标签中的 75 个，以传播恶意信息窃取程序。由于超过 10,000 个 GitHub 工作流文件依赖于此操作，潜在的凭证窃取影响范围极其广泛。

## **标签中毒攻击的机制**

攻击者没有将代码推送到分支或创建新版本，而是利用之前凭证泄露事件中残留的写入权限，悄无声息地更改了现有的版本标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PhLibMphcYO8TyxRicqQxI7DCeoq9TwlqtAr8LncAoicYDPu5ggJ3DNaFicIzpAPJicdicSmdBKic4ibERibaby54zAQrSJIOWyRL7j5ko/640?wx_fmt=png&from=appmsg)

威胁行为者强制推送了 75 个标签，包括广泛使用的版本，如 `@0.33.0` 和 `@0.18.0`，指向新伪造的提交。

这实际上将受信任且本应不可更改的版本引用变成了他们定制的信息窃取恶意软件的直接分发机制。

通过完全绕过创建新版本的需要，攻击者最大限度地降低了触发自动安全警报或通知项目维护人员未经授权的分支更新的可能性。

为了逃避检测，攻击者伪造了 Git 提交元数据。他们克隆了原始作者姓名、日期和提交消息，使恶意提交在代码库日志中看起来合法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PXickEC6H317fIUHOzL2j1XxnnkspLKnKuRXOpkDlanPXW3W1ozXk1nKOk8mHZgNmQI75PERtviaGWmEfjjxyicS7Ydiaco5rMBF0/640?wx_fmt=png&from=appmsg)

修改后的代码使用了当前的主文件树，但将合法 `entrypoint.sh` 文件替换成了受感染的版本。

由于恶意提交的日期与 2026 年 3 月的父提交冲突，且这些提交缺少 GitHub 的 Web 流 GPG 签名，仔细检查后即可发现伪造行为。值得注意的是，版本号 `@0.35.0` 保持不变，是唯一安全的标签。

注入的 204 行 `entrypoint.sh` 脚本会在运行合法的 Trivy 扫描之前执行其恶意操作，从而使其能够隐藏在众目睽睽之下。

根据 Socket 的说法，信息窃取程序分三个不同的阶段运行：有针对性的收集、强大的加密和隐蔽的窃取。

在收集阶段，该恶意软件会同时攻击托管在 GitHub 和自托管服务器上的运行器。在托管于 GitHub 的 Linux 环境中，它利用无需密码的 `sudo` 权限转储 `Runner.Worker` 进程内存，并直接从堆内存中提取密钥。

在自托管的运行器上，一个全面的 Python 脚本会抓取文件系统，查找多个目录中的敏感数据。

该脚本会系统地搜索 SSH 密钥、数据库凭证、CI/CD 配置文件，甚至加密货币钱包数据，从而确保获得大量有价值的信息。

在第二阶段，被盗数据使用 AES-256-CBC 进行压缩和加密，加密密钥用 RSA-4096 公钥封装。

最后，该恶意软件尝试通过向域名抢注的域名发送 HTTPS POST 请求来泄露加密的数据包 `scan[.]aquasecurtiy[.]org`。

如果此主要通道失败，脚本将使用受害者自己的GitHub 个人访问令牌创建一个名为 的公共存储库 `tpcp-docs` ，并将窃取的数据作为发布资产上传。

该恶意软件自称为“TeamPCP Cloud stealer”。安全研究人员将TeamPCP视为一个云原生威胁行为体，该行为体以利用配置错误的云基础设施进行勒索软件和加密货币挖矿活动而闻名。

组织必须立即停止 `trivy-action` 使用版本标签进行引用，但以下情况除外 `@0.35.0`。为确保完全安全，管道应将操作固定到特定的安全提交 SHA（`57a97c7e7821a5776cebc9bb87c984fa69cba8f1`）。

任何执行过恶意标签的环境都应被视为已完全入侵。安全团队应立即轮换所有暴露的密钥，包括云凭证和 API 令牌。

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