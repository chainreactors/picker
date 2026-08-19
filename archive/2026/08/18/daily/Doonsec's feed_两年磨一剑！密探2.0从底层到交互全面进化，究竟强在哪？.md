---
title: 两年磨一剑！密探2.0从底层到交互全面进化，究竟强在哪？
url: https://mp.weixin.qq.com/s/99gxVO-IScBI9nbQt2D6sQ
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:13.470578
---

# 两年磨一剑！密探2.0从底层到交互全面进化，究竟强在哪？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p0xRmv2LRicLwnFTuFPtnlFicxmZXasfh5KMicGT1FoKdw2mgsRMBmqRQEKb8ibmYpuicXp0ibzfLJ64bhy66SGibzW8zNd6UV8Y1Fpr70KT1DprNM/0?wx_fmt=jpeg)

# 两年磨一剑！密探2.0从底层到交互全面进化，究竟强在哪？

好靶场

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

非常好用的工具

以下文章来源于虎哥的安全圈
，作者kkbo(虎哥）

![](https://wx.qlogo.cn/mmhead/LXqicVqwJiatpVSCELa7wdySLF7sQJPfEBywkibeL7A8rDrqc4wKWlJr2UlJ1hLKDKKkiaf9hILA4d4/0)

**虎哥的安全圈**
.

分享自己和圈内朋友的在安全学习，实战及工具开发的心得。

# 密探2.0 重磅发布：Rust 全新重构，集成资产测绘、侦察、漏洞检测、云安全、MCP 工具等 50 余项能力

#

**从 2024 年 4 月密探 v1.0 发布，到今天 v2.0 正式亮相，整整两年多时间学习沉淀。**

密探v1.0 走过了 19 次版本迭代，70 余名师傅参与共建，3 个微信交流群 1300+ 人共同打磨。这段旅程里，每一次 bug 修复、每一条建议，都让密探变得更好。

但 v1.0 也有它的局限——功能覆盖少，界面UI表现不足，体验没有跟上。所以，2025 年开始，作者做了一个大胆的决定：**用 Rust 语言从零重写密探**。

今天，密探 2.0 来了。不只是换了个壳，而是从底层到交互的全面进化。

***0****1***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**工具定位**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**密探渗透测试工具 v2.0** 是一款项目级一站式网络安全检测与运维工具，集成资产测绘、情报侦察、漏洞检测、云安全、AI 自动化渗透、MCP 工具等 50 余项能力，帮助安全团队快速摸清资产、排查风险、修补短板，高效完成常态化安全运维与专项检测工作。

**技术栈：** Rust + Tauri · 支持 Windows / macOS / Linux 全平台

***0****2***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**六大核心亮点**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**0****1**

**项目级数据管理**

对信息收集及资产探测的过程数据进行项目级管理，严格区分不同项目之间的数据记录，杜绝数据混乱。便于对项目历史记录进行回溯、续用及数据整理，随时从历史记录中调取。

**0****2**

**聚合测绘 · 一键多引擎**

内置测绘语法转换算法，实现常见搜索语法自动转换适配多个测绘引擎（FOFA、Hunter、Quake、ZoomEye、DayDayMap、Censys、Shodan、零零信安等），避免不同引擎语法差异导致的人为转换错误，极大提高测绘效率。

**0****3**

**断点续扫 · 告别从头来过**

指纹识别、JSFinder、目录扫描、子域名爆破、端口扫描、弱口令、POC 扫描等耗时功能全面支持断点续扫，随时从上次结束的任务处继续完成后续扫描，彻底解决每次扫描都要从头开扫的痛点。

**04**

**Heapdump 敏感信息分析**

针对 Java 的 Heapdump 转储文件进行解析，自动分析提取数据库连接信息、SQL 语句、IP 地址、JWT Token 等敏感信息，一站直达。

**0****5**

**小程序反编译 → API 扫描一把梭**

支持多版本微信小程序解包，自动提取代码中的 API 接口、URL、AKSK 等敏感信息。尤其 API 接口可通过扫描按钮一键发起未授权检测，根据数据包状态及大小判断接口是否存在未授权风险。

**0****6**

**MCP Server · 39 个工具赋能 Agent**

密探 2.0 的 MCP Server 提供包含常规功能、项目相关、主体查询、测绘引擎、Fuzz 爆破、云安全等 39 个 MCP 工具，可为其他 Agent 智能体提供交互能力。交互结果也会保存到项目历史记录中，实现各项工作过程数据的统一管理。

***03***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**功能导航**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

|  |  |
| --- | --- |
| 模块 | 功能 |
| **主体查询** | 主体查询 · 批量主体 · ICP 查询 · IP 归属 · 搜索语法 · 敏感信息 |
| **空间测绘** | 聚合测绘 · FOFA · Hunter · Quake · ZoomEye · DayDayMap · Censys · Shodan · 零零信安 · 图标 Hash |
| **Fuzz 爆破** | 指纹识别 · JSFinder · 目录扫描 · 子域名爆破 · 端口扫描 · 弱口令 · POC 扫描 · JWT 爆破 · Swagger |
| **工具箱** | Sessionkey · Heapdump · 微信小程序 · 密码本 · 社工字典 · 杀软识别 · 编码解码 · 反弹 Shell |
| **云安全** | OSS 管理 · 云主机 · 微信利用 · 钉钉利用 · 飞书利用 · 地图密钥 · 百度人脸 |
| **AI 渗透** | MCP · 技能 · AI 助手 · 自动化渗透 · 代码审计 |
| **其他** | 武器库 · 代理池 · 网站导航 |

***0****4***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**VIP订阅**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/1bfQtE66VTmX1ibCY7eYOGXNY70ROLy2kUeLDiaquRfl5gsAae0Fz7hciaQbxovrP8EAAMfmd40RH41536tSemxEo0SKEpE1kxibjjkCWgUubAE/640?from=appmsg)

密探2.0发布订阅服务以支持密探的长期更新，订阅的费用主要用于日常开发测试AI模块TOKEN消耗，还有就是回馈提供poc，指纹的师傅等等，更加给作者继续更新提供动力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2WmKNJvMmCxyf5oV5ia6bBu28ApyiaaqXy3Pxxib0XDuSKKfibyZOibBADodl8D0LCXpIowvTJZc5New5EEgib6PGSyw6t12cwxW8uGibo8o2Hl90U/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2WmKNJvMmCxyf5oV5ia6bBu28ApyiaaqXy3Pxxib0XDuSKKfibyZOibBADodl8D0LCXpIowvTJZc5New5EEgib6PGSyw6t12cwxW8uGibo8o2Hl90U/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2WmKNJvMmCxyf5oV5ia6bBu28ApyiaaqXy3Pxxib0XDuSKKfibyZOibBADodl8D0LCXpIowvTJZc5New5EEgib6PGSyw6t12cwxW8uGibo8o2Hl90U/640?from=appmsg)

作者工具更新不易，各位师傅有钱捧个钱场，不愿出钱捧个人场，GITHUB点星，自媒体宣传都可以，有你的支持才能让“密探持续更新”。 工具会以更新日志，感谢名单，VIP激活码等方式回馈为工具更新提供POC、指纹、API KEY等帮助的师傅。
   由于作者平时工作也比较忙，可能会漏看微信消息，如果师傅需要升级VIP，可以直接扫工具里面“咸鱼”二维码或咸鱼上搜索“密探的咸鱼店”下单，售后会及时发货。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/tn9sjR9XQYDIB1TBnQRXSx8mrfJOnzwIhPD71av02DPmDCXFSqfooU4ia8SQLdNvVRDAIeU8fHNJ96J4dAYO1Z1RfdxcubgPKPkWia3asuHFI/640?from=appmsg)

**免费获得VIP的方式**

**0****1**

**提交有效 BUG**

通过密探使用提交有效 Bug 帮助升级，经确认后免费赠送 VIP 一年激活码 1 个。

**0****2**

**资源贡献（指纹库 / POC / 各种 KEY）**

为密探升级作出实质贡献，包括但不限于：提交高质量指纹、POC、为功能开发提供各种 KEY 账号，一次免费赠送 VIP 一年激活码 3 个

**0****3**

**推广赠送**

从密探 2.0 发布之日起，在公众号 / 抖音号 / 博客发布密探的介绍和使用相关内容。

阅读（播放）> 1000：免费赠送 VIP 一年激活码 20 个

阅读（播放）> 2000：免费赠送 VIP 一年激活码 30 个

**0****4**

**邀请赠送**

产凡邀请好友付费可以获得相应的赠送。

邀请 1 位好友付费购买 VIP，赠送邀请者 VIP 一年激活码（6 个月）1 个，以此类推。

邀请 1 位好友付费购买 VIP 团队版，赠送 VIP 一年激活码 8 个。

邀请 1 位好友付费加入「密探」知识星球，赠送 VIP 一年激活码 3 个。

**0****5**

**活动赞助**

公众号或网络安全论坛开展的各种宣传活动，可根据活动的性质、受众的情况与作者联系，可免费赠送一定数量的 VIP 一年激活码

***05***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**下载与关注**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

基于 Rust + Tauri 全新开发，跨平台支持 Windows、macOS、Linux 三大系统，选择对应架构下载安装即可使用，后续支持「关于密探」界面提示自动升级。

GitHub 下载：
  https://github.com/kkbo8005/mitan/releases

密探 B 站视频：
  https://space.bilibili.com/552795114

虎哥抖音号：
  6509 2382 655（欢迎关注）

![](https://mmbiz.qpic.cn/mmbiz_gif/uRexc1g7MQvlHnje9oKpGq6ZrYrAWCnT3Ndh7zemcXMDuNVPjFMxug1HfSSicHicJfj3icKjbUp7815kQBHnxXyfoMSCJibe4HTeYHLCfzsEOhc/640?from=appmsg)

***0****6***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_gif/aqt1FFJ3QtgET3d3UaC9wZ5EQavqNuOuXTuLFAhb8lOOkcrU54ibHLTBSrDdZP5wBR5ZqBEcKQuticJNe10Njgv9EOEaFf74GwGg7Rv4eiaywo/640?from=appmsg)

**请在得到充分授权的情况下使用“密探”**

本工具仅供授权渗透测试和安全研究使用，用户须确保已获得目标系统的合法授权。任何未经授权的扫描和测试行为均违反相关法律法规，由用户自行承担全部法律责任。用户在使用过程中获取的数据应妥善保管并在使用完成后及时销毁。未经授权，严禁对本工具进行反编译、逆向工程或二次分发。

***0****7***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**致       谢**

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4LQV7puFz9gb4u5OZftA890ZTyb8JFJKQQRV0RmdIcicI4Za0/640?from=appmsg)

**0****1**

**2.0版本（截至2026年8月16日）**

@Sik @湘南第一深情 @曾哥 @温酒看日出 @🌲 @99977 @至明善渊 @ZoomEye 官方 @过去式 @梧祁 @小浪 @REMADOME.md @Forget me @Sukalis @重剑无锋 @无先森@大白哥 @湫东坡\_up @小机智 @重阳 @醉殷 @TyC2l& @陈明 @奔奔 @破阈侦攻小队—郭兵 @雪山乘客 @狮恩

**0****2**

**1.0版本**

@Sik @湘南第一深情 @无先森 @重剑无锋 @小肖ovo @404xyunxi @soufaker @瑾夏年华 @xiaokp7  @LiPaCai @归城 @Confy @DXError\_xiaoyu @C @听雨 @HOPE @NuyoaH\_T @3had0w @罗纯 @lovjl @小船儿 @指尖的风@hellong\_ @XW @个性男孩 @Godyu @季风吹向大海 @天明 @曾哥 @上心 @杨CC @狐狸 @弱鸡 @橘橘 @何处 @柯林斯 @小机智 @FF0C @正在输入锺 @ANy @油猫饼的猫 @marino-admin @coolcat @Mine @大白哥 @BIU @哎呦喂 @一方 @伯徽 @rissssk @冰淇霖 @奇点 @清醒的沉沦 @姜姜 @浅笑⁹⁹⁶ @MKID @凌晨四点半 @梧祁 @土豆(potato) @k11p1 @奋斗的小浪 @Forget me @pop人 @各有命 @十一@laobai @轻风亦清风 @地图大师 @雪山乘客

***0****8***

![](https://mmbiz.qpic.cn/mmbiz_png/vZ0RJppk7JyMfCTvdqSvd9AdpaRqYorwEWddTiauhibRicYLWvqn3dlQX518Qh4L...