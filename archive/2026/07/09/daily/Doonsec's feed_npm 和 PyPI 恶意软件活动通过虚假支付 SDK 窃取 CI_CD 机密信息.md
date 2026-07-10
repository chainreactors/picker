---
title: npm 和 PyPI 恶意软件活动通过虚假支付 SDK 窃取 CI/CD 机密信息
url: https://mp.weixin.qq.com/s/Vf6wY5_kmdPXWUZVptUASg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:55:49.135595
---

# npm 和 PyPI 恶意软件活动通过虚假支付 SDK 窃取 CI/CD 机密信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7N70KyP4DkWQ2Tp9cxQgRaYCX8DNJsGceFhEAWF3nW0KvNAX7pLxPf1vHDmS5NtankzwfazAc7LkWxwjW9ibcUbmQa4zDdvvlTA/0?wx_fmt=jpeg)

# npm 和 PyPI 恶意软件活动通过虚假支付 SDK 窃取 CI/CD 机密信息

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这是一场有组织的供应链攻击活动，通过 npm 和 PyPI 推送了 17 个恶意软件包，伪装成 PaySafe、Skrill 和 Neteller 等知名支付服务的 SDK。

该活动打包了 17 个 npm 模块，每个模块有四个快速版本，以及 4 个PyPI 包，这些包通过单个恶意版本进行访问，伪装成便捷的支付 SDK 外观，但其中包含旨在收集环境中存储的凭据并将其泄露到攻击者控制的通过 ngrok 托管的基础设施的逻辑。

该 npm 集群包含 paysafe-checkout、paysafe-node、paysafe-js、neteller 和几个 Skrill 品牌名称的软件包；每个 npm 软件包都发布了 1.0.0 到 1.0.3 版本，并在发布后大约六分钟内被检测为恶意软件包。

PyPI 上的 paysafe-sdk、paysafe-payments、paysafe-api 和 paysafe-kyc 软件包分别发布了 1.0.0 版本，其行为与对应的 JavaScript 版本完全相同。Socket 的博客记录了受影响的软件包以及两个生态系统的示例代码。

攻击者构建了一个逼真的 SDK 外观，对常见的 SDK 调用立即返回成功响应，同时在后台执行隐蔽的遥测和数据窃取。

例如，paysafe-node 模块导出 PaysafeClient，该客户端从环境中读取 PAYSAFE\_API\_KEY 和 PAYSAFE\_ENV，并实现 payments.create/get 和 customers.create/get。

客户端不会联系真正的 Paysafe 端点，而是立即返回 { success: true, method, path }，同时安排延迟调用内部数据泄露例程，该例程会将指纹以及包含 KEY、SECRET、TOKEN、PASS、AUTH 或 API 的任何环境变量发送到 C2 主机。

Socket 的人工智能在一份与 GBhackers 分享的报告中称，扫描器检测到了一批于 2026 年 7 月 7 日发布的 npm 和 PyPI 恶意软件。该恶意软件包含故意规避沙箱和反分析检查，以降低在自动化环境中被检测到的可能性。

当主机暴露出常见的沙箱指标（主机名或用户名包含 sandbox、analyzer、cuckoo、vmware、vbox、malware 或类似字符串）或系统 CPU 核心数少于两个时，它会提前返回。

JavaScript 和 Python 构建都实现了类似的检查，表明参与者在不同生态系统中的行为是经过校准的。

## **npm 和 PyPI 恶意软件**

C2 基础设施被故意混淆：最终回调主机是通过多个解码阶段 XOR、字符移位和反转来恢复的，从而在 ngrok 风格的基础设施下产生跟踪域。

泄露的有效载荷包括主机名、用户名、当前工作目录、时间戳、硬编码的软件包名称、可选的上下文额外数据（API 方法/路径和截断的 API 密钥）以及所有与密钥模式匹配的环境变量（截断为 100 个字符）。

实际上，CI/CD 和开发人员工作站中常见的密钥，如 PAYSAFE\_API\_KEY、AWS\_SECRET\_ACCESS\_KEY、GITHUB\_TOKEN、NPM\_TOKEN 等，都是过滤逻辑的明确目标。

该攻击活动表现出专业化、以经济利益为驱动的特征：针对支付 SDK、环境感知沙箱规避、使用每个软件包的混淆密钥来阻碍基于签名的检测，以及使用 ngrok 或类似隧道服务（这些服务曾被滥用）。

该行为者决定在 npm和 PyPI 之间快速切换，扩大了其运营范围，并使只监控一个生态系统的防御者面临更大的挑战。

团队的补救措施包括立即删除和替换与套接字列表匹配的任何依赖项、撤销和轮换暴露的凭据，以及全面审查 CI 运行器环境变量和密钥管理。

组织还应加强供应链卫生：锁定软件包版本、强制执行 SBOM 和依赖项允许列表、启用软件包安装异常检测以及在构建期间运行环境感知密钥扫描。

这一事件再次表明，现代供应链威胁跨越多种语言生态系统，并且越来越多地针对 CI/CD 机密信息，而不仅仅是可执行有效载荷。

对于面向开发者的域名抢注 SDK 尝试静默收集令牌的情况，快速检测和凭证轮换仍然是最有效的缓解措施。

预览时标签不可点

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