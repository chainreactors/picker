---
title: Windows 11和Server 2025更新默认阻止不可信的交叉签名内核驱动程序
url: https://mp.weixin.qq.com/s/cMajwJ74cgRm4SzdCJXufw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:50.259152
---

# Windows 11和Server 2025更新默认阻止不可信的交叉签名内核驱动程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7P0fG3PLibah83bS2Q8GsMWtm0HFKXuebV0yvkPK7lYyO6cYGUxuaNgmQqc9e6yIIuicx9J63UJQHdATSOM09QddkBkbLF396daA/0?wx_fmt=jpeg)

# Windows 11和Server 2025更新默认阻止不可信的交叉签名内核驱动程序

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

微软正在采取重大步骤，通过消除对弃用的交叉签名根程序签署的驱动程序的信任，来加强Windows操作系统的抵御内核级威胁。

从2026年4月更新开始，Windows 11和Windows Server 2025将默认阻止这些不受信任的驱动程序。

此策略确保只有通过Windows硬件兼容性程序认证的驱动程序才能自动加载，大大减少了恶意行为者的攻击面。

交叉签名根程序于21世纪初推出，允许第三方证书颁发机构受Windows信任的代码签名证书。

然而，该系统没有提供内核代码的安全性或兼容性的保证。由于开发人员管理自己的私钥，该程序成为凭证盗窃的频繁目标，允许威胁行为者部署rootkit。

微软于2021年正式弃用了该签名程序，此后所有相关证书都已过期。尽管如此，Windows继续信任这些遗留证书，以保持与遗留硬件的兼容性。

这项新的更新终于结束了挥之不去的信任。展望未来，认证管道要求供应商在收到受保护的微软拥有的证书之前，通过严格的身份审查，提交严格的测试结果，并进行恶意软件扫描。

为了防止系统崩溃，微软正在为信誉好、广泛使用的交叉签名驱动程序引入一个明确的允许列表。

内核更新也将在仔细的评估模式下部署。Windows内核将审核驱动程序加载信号，以确保新策略不会中断关键功能。

系统只有在满足特定的运行时间和重新启动阈值后才会强制执行阻止。如果在此审核阶段检测到不受支持的欠佳表现，系统会重置评估计时器并保留强制执行。

依赖内部开发的自定义内核驱动程序的企业环境有替代选项。组织可以使用应用程序控制业务策略安全地绕过默认块。

通过使用根植于设备的UEFI安全启动变量的权限签署此策略，管理员可以明确信任私人签名人。

这确保了威胁行为者无法任意加载恶意驱动程序，而合法的内部操作继续不间断。

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