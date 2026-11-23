---
title: 【网络安全】SCA Audit：ARTEX 二开静态代码审计平台
url: https://mp.weixin.qq.com/s/8w0OnBgZF_-v3EJMDOUceA
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:24.325921
---

# 【网络安全】SCA Audit：ARTEX 二开静态代码审计平台

# 【网络安全】SCA Audit：ARTEX 二开静态代码审计平台

原创

效能跃迁实验室
效能跃迁实验室

效能跃迁实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# SCA Audit（CodeScan-Artex）基于 ARTEX 二次开发，复用多 Agent 编排内核，面向静态代码审计场景； **输出的审计结果支持绑定源码行号、接口权限信息。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpwibPm45IVDL22qMRuzFw5gxmvzfb0jYibelNybt5wZo2Kmmsa4jicYStzv4qanYcia348N736bia3VZZ2iah4JGtz3u4yqicLOmy4kicQ/640?wx_fmt=webp&from=appmsg)

---

## 开源地址

* **仓库**：https://github.com/Ernket/CodeScan-Artex
* **技术栈**：Go（内嵌 Next.js）+ PostgreSQL · AGPL-3.0
* **控制台**：`http://localhost:7878`

---

## 与 ARTEX 的异同

### 相同：资产图、探索图

沿用双图架构：

* 资产图：记录对外暴露面；
* 探索图：记录推理过程。

调度模型不变：
planner 下发审计意图，worker 执行任务并回写结果，形成完整事件闭环。

![](https://mmbiz.qpic.cn/mmbiz_jpg/w4WPiaObtlpxgYvfnJF1aoY48gNhNCvrLgckxos7LicMVjnhzWbKdlibLUXCp0E4UnmsibuQ7rChSicgBeVZ5ZGDnZTeSC3f7tExewmwib389bFkM/640?wx_fmt=webp&from=appmsg)

### 不同：静态只读审计面

* Agent 无执行权限：不跑系统命令、不向外发包探测。
* 审计对象：本地源码 + Maven 本地仓库第三方依赖（依赖按需反编译读取）。
* 整体为只读静态审计，无动态攻击 / 探测行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpzGld4y9thg86AA1syiaL7xsxnvwgDVPoaljg2HyMkialAbJFaEmSeq5qwAsawwLkm5wicmnswaVsq5wLgyPk4GzLybXDTCUGsoVQ/640?wx_fmt=webp&from=appmsg)

---

## 界面摘录

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpzgTrQicfDZtf2Cmj5XvBrROFsxBmyg110sJYH9VFJiaLdAdzTBvlpNcibWWYtlbYQRc1aJCdkwg99uMM2Hj9ILoLXuypeOgMxLx0/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/w4WPiaObtlpwDnY1cMHriciawVv4nGvHVSRTYEvjmclx2mrG3Zwicg3aqDwIbZU0w1cib0w837MY5TeGgKaJBxDsdXOuicS3LmtGKiaFLj63rrqJCA/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w4WPiaObtlpyoEt6qnia1he55SPqSicHFy8cco8FUshmRpQVrU2hJWO6BVScFR7eUvLLbt3B9XlC0h93z1umlfljFEPjvG1iaKHtBtKJOUxgdIU/640?wx_fmt=webp&from=appmsg)

---

## 延伸阅读

* SCA Audit：https://github.com/Ernket/CodeScan-Artex
* 破军 Pojun：https://github.com/chu0119/Pojun

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7OncKt4Qr9zqhxVYGj9l6Y3F1k75h3f7IBYroJUJnfhfxJGCYnYkkOEXsicDG171scGlicL58pmwTsFyR7pOCb0Q/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过