---
title: 微软正式发布组策略，从企业设备中移除 Windows 11 Copilot
url: https://mp.weixin.qq.com/s/KeFixNsJ4DhYGgj2t92oDA
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:25:16.146046
---

# 微软正式发布组策略，从企业设备中移除 Windows 11 Copilot

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MdjeIkrWAJepaf8pq0peSSiat4szicvZKDcdnwcOb9mszMhb1ubCXtHjnrfk5e4icyUU1g7MfALvYtLXSm2ziauGYa6tQGmOsRrfE/0?wx_fmt=jpeg)

# 微软正式发布组策略，从企业设备中移除 Windows 11 Copilot

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软正式发布了一项新的组策略设置，允许 IT 管理员从受管理的 Windows 11 设备中静默卸载 Microsoft Copilot 应用。此举标志着企业正在更广泛地从捆绑式 AI 臃肿组件转向用户选择驱动的部署。

该策略名为 RemoveMicrosoftCopilotApp，于 2026 年 4 月 14 日作为2026 年 4 月星期二补丁安全更新的一部分广泛推出。

它包含在 Windows 11 版本 25H2 中，并已通过更新 KB5083769 及更高版本发布，可通过策略 CSP 和传统的组策略对象 (GPO) 管理进行访问。

## **使用组策略删除 Windows 11 Copilot**

该设置为 IT 团队提供了一种有针对性、无干扰的方法，可以从企业终端`RemoveMicrosoftCopilotApp`卸载面向消费者的Microsoft Copilot 应用。

启用后，管理员可以将策略值设置为 1 以触发删除，或设置为 0 以禁用它，这是一个与现有 Windows 策略框架一致的基于整数的简单切换。

但是，该策略经过精心限制。它只有在设备上同时满足以下三个条件时才会激活：

* 同一设备上还安装了 Microsoft 365 Copilot。
* 最终用户并未手动安装 Microsoft Copilot 应用。
* Copilot应用程序在过去28天内未启动。

这种三因素安全机制确保该策略不会干扰依赖独立 Copilot 应用的活跃用户，使其成为一种精准的工具，而不是一种粗暴的移除手段。

管理员可以通过导航至“用户配置”→“管理模板”→“Windows AI”→“删除 Microsoft Copilot 应用”在组策略编辑器中找到新策略。

它还可以通过 Policy CSP OMA-URI 路径`./User/Vendor/MSFT/Policy/Config/WindowsAI/RemoveMicrosoftCopilotApp`和设备级等效路径访问。

该设置适用于专业版、企业版、教育版和物联网企业版 SKU，有效涵盖了所有受管组织环境。

需要注意的是，此策略仅执行一次性卸载，而非永久阻止。用户可以根据需要从 Microsoft Store 重新安装 Copilot 应用。

希望永久阻止重新安装的管理员需要将此策略与 AppLocker、Windows Defender 应用程序控制 (WDAC)或 Intune 卸载配置文件等其他强制执行工具结合使用。

此次发布正值微软将人工智能功能从核心 Windows 组件中“分离”出来的大趋势之际，此前企业不断反馈未经请求的人工智能集成问题。

通过提供这种可控移除功能，微软将企业 Copilot体验定位在 Microsoft 365 Copilot 之上，将其作为托管企业环境中唯一、官方认可的 AI 助手，简化了 AI 工具集，同时赋予 IT 团队他们长期以来一直渴望的控制权。

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