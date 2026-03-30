---
title: Ansible 库存管理
url: https://mp.weixin.qq.com/s/ah5K1OgdXcwO1pVKz8vrRA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:42:24.576836
---

# Ansible 库存管理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dibzmm9niba06fYqeaibjvqg2QdMCVEZVpKk4SlpvPmuaIaQflCKcJe7BV6yLQZA0rK9qIMibYwQic3PIc2gNaR9AN2ibSICjyshBYTMmYknUibfEE/0?wx_fmt=jpeg)

# Ansible 库存管理

原创

Lino
Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

本节我们来学习 Ansible 库存管理。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07uIsvwz5CXxcrlc02Wyo6GKHLPL6SZXcU4NGKzVe2jQQbeVyJ7xIxD65PMGU6ibyyn5MDEsFBj8Qz1bg9iafZ3EXG2mzibwg6uQ8/640?wx_fmt=png&from=appmsg)

在小型实验室，手动维护一个 `hosts` 文件很简单。但在企业级网络中，设备数量可能是成百上千，且频繁变动（如云端的虚拟防火墙、SD-WAN 节点）。

手动更新静态文件不仅低效，更是运维事故的温床。

## 静态与动态

### 静态库存 (Static Inventory)

静态库存是最基础的形式，通常是 `.ini` 或 `.yaml` 文件。它适用于设备变动频率极低的实验室环境或小型办公网。

* 优点：直观，支持 [group:vars] 层级嵌套。
* 缺点：无法自动同步 CMDB 或云平台的状态，扩展性差。

## 动态库存 (Dynamic Inventory)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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