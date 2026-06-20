---
title: 【工具】查询邮箱注册信息的开源工具：MailAccess
url: https://mp.weixin.qq.com/s/NDzoo6ADXEgzVh3IDDQYkg
source: Doonsec's feed
date: 2026-06-19
fetch_date: 2026-06-20T06:12:27.330520
---

# 【工具】查询邮箱注册信息的开源工具：MailAccess

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/no8YFGgia2NH1JMQFj2OSn7Ns7kExejxzPeBorPWIIDwQH5oeaUkQvw39xHPYpaDjvLiblTNfw1VgWCXayBvkusKFXlRicZyx33ALRD7MOJJ0Y/0?wx_fmt=jpeg)

# 【工具】查询邮箱注册信息的开源工具：MailAccess

原创

丁爸
丁爸

丁爸 情报分析师的工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天给大家推送一个专门用于调查电子邮箱在各种平台注册信息的自托管开源情报平台MailAccess。它能够覆盖泄露数据库、社交网络、DNS 记录和开放网络，并返回统一的风险评分和结构化调查结果，用户可以将这些结果导出或导入 Maltego。MailAccess专为获得授权的安全研究人员、开源情报分析师和渗透测试人员而设计。

工具GitHub地址：

https://github.com/KatrielMoses/MailAccess

## 它的功能

* **身份图谱**——跨平台关联来自每次调查的账户、用户名和信号
* **名称共识引擎**——通过置信度评分，从多个独立的名称信号中确认真实身份。
* **防御者简报**——面向安全经理的风险概要，包含可操作的发现和后续步骤
* **电话号码恢复**——用于查找和验证与目标关联的号码的流程
* **Telegram/WhatsApp提示**——轻量级即时通讯应用占用空间检查以及其他模块
* **基于YAML 的平台系统**——社交风格的检查已定义`backend/platforms/`；无需为每个站点编写新的 Python 代码，即可实现社区扩展
* **原生 Maigret 引擎**——无需 Maigret 运行时依赖即可覆盖 2500 多个平台，包括 WMN 未涵盖的区域性、小众和国际平台。
* **全面检测**——在扫描开始前，排除那些对任意用户名返回误报的平台。
* **平台去重**——按个人资料 URL 域名合并 WMN 和 Maigret 的结果，以避免重复计算已确认的平台。
* **深度入侵模式**——检查前 100 个最严重的入侵网站是否存在账户
* **历史情报**——互联网档案馆存档搜索 + GitHub 提交作者搜索
* **递归邮件发现**——通过名称关联恢复同一人拥有的其他电子邮件
* **资质风险评分**——采用 0-100 分的独立资质风险信号，分为低/中/高/危四个等级，并提供主要驱动因素和建议的后续步骤。
* 并发模块执行——所有模块并行运行，结果按到达顺序流式传输。
* WebSocket 流式传输——无需轮询即可实时获取部分结果。
* REST API + Web UI + CLI — 选择最适合您工作流程的界面。
* 插件模块系统——只需放入`.py`文件`backend/modules/`即可自动注册；无需接线
* 6 种导出格式：JSON、CSV、PDF、Markdown、STIX 2.1、Maltego XML
* Maltego 本地转换服务器 — 直接从 Maltego 桌面应用程序运行调查
* Webhook 通知 — Slack、Discord 或任何 HTTP 端点
* 暴露评分（0-100）及风险等级：低/中/高/危
* 默认使用 SQLite；PostgreSQL 可通过 Docker Compose 配置选项启用。

以下是安装该工具后测试一个邮箱注册情况：

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NGtiahlZjhMZt0qRVXQgZPxkfmHO2ibbSnzn4GL0H89IarzPp5zx6ib9qz8OgDM16DVexGUwN48w1FzdMJ0iaMureiak7WDiaXXv9ITc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NHGl6LnP8BqiaZJNZpGMHyQgpTJx933TicN1CwxK6H2bjsJ7hViaUyXkLzEFTeMInUsrTNdibgrXucbAJefOibIL0DCribB4s3bB8dk4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NEeMjWsrgCpp9RCW5fx9qERicyeOpAibpS3FZZcu0OhJaWRqPlaTuu3XxmWeMEhWFe1o4FheQTKsHajSEibYs34yT4XQNCBsLibIx4/640?wx_fmt=png&from=appmsg)

长按识别下面的二维码可加入星球

里面已有万余篇资料可供下载

续费五折优惠

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5zKJ6IvDm7zH8uGKMLmpkqKYLbkAVHcDIy1pTdjbsOlqh0GOYj7RhhMsfCLtUtWfwEicsFibUicCMwnw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFlImicSViahE1DvyBficCzEKUPcROfEyKNC2MALtdp5kGAzo8FicsrkvM3ohjzple9FNv0NrW68dZUc66pIQEh98nkwviaSExiaoGgk/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFESZibsC7Dx12Z6vvEDg99uEsCAvGHwbf50FqMe83gZyVraKI9lPm2jOBuchjNKJPS16RBW7WeTJq8TrOaMe82iaScO3GaaKKaY/0?wx_fmt=png)

丁爸 情报分析师的工具箱

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFESZibsC7Dx12Z6vvEDg99uEsCAvGHwbf50FqMe83gZyVraKI9lPm2jOBuchjNKJPS16RBW7WeTJq8TrOaMe82iaScO3GaaKKaY/0?wx_fmt=png)

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