---
title: 如何利用 Codex 与 GPT Image-2 重构扫描器字典管理 UI
url: https://mp.weixin.qq.com/s/3WlmwpXU0cAjPVBFZvdQmA
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:51:31.067060
---

# 如何利用 Codex 与 GPT Image-2 重构扫描器字典管理 UI

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xZjx15SZGqJibr7zHrB0uHTKFG2TkIr1F7aEeuV0I2lDqBISwOtZt6ZGnMOuoElUezicfW5KjFhyh7Z2icCTaEiaJbF076ZStWm63icyiaP1Y8zes/0?wx_fmt=jpeg)

# 如何利用 Codex 与 GPT Image-2 重构扫描器字典管理 UI

原创

洋洋
洋洋

塔罗安全学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在 GPT Image-2 模型之前，设计一套合理的 UI 就像抽奖——随机生成多个 HTML 原型，挑一个相对顺眼的，再反复修改。这个模型的出现，把整个工作流简化了许多。以下是我如何结合两个模型来重构扫描器字典管理 UI 的过程。

## 原本的 UI

![image-20260507163206961](https://mmbiz.qpic.cn/sz_mmbiz_png/xZjx15SZGqKjj4Gp9ibicjWPmXK26MpSkvicwS06dMHGiafVQM9iaKGJibx7ZFYVvCglZYic7htc5CcIFibb68qUOWu0y3Ya3WvyGw3vTvNiavVV8UbY/640?wx_fmt=png)这个页面来自之前的星环项目。在我看来，它明显更适合"字典很少"的场景，差不多是一个轻量 MVP。

它的主要问题在于：左侧只是文件列表，信息维度很少；没有排序、筛选、分类、标签、分页、批量操作；右侧大面积空白，依赖用户先点选。几个字典还能应付，一旦变成几十个上百个，用户会很难找、很难比较、也很难维护。

## 第一步：用 Codex 分析现状

重构之前，先用 Codex 读取页面截图和对应的源码，让它了解当前页面的情况——有多少按钮、显示了什么字段。之后再让它给出重构提示词：

> 比如我给这张截图给 AI，再给个提示词让它设计新的设计图，你给我提示词。

以下是它给出的提示词：

```
基于我提供的截图，重新设计「月狐 LunaFox」后台中的「字典管理」页面，输出一张高保真的产品 UI 设计图。  设计目标： 把当前"左侧小列表 + 右侧详情空白很多"的布局，改成更适合字典数量变多时使用的 MVP 管理界面。不要做复杂大版本，只做一个轻量、真实可落地的管理页。  必须保留： - 左侧导航栏整体结构、品牌、当前选中的「工具 / 字典管理」 - 顶部应用栏和右上角图标区域 - 页面标题「字典管理」 - 搜索字典输入框 - 「上传字典」主按钮 - 现有字段：字典名称、描述、行数、文件大小、ID、更新时间、Hash - 操作：编辑内容、删除  推荐新布局： - 主内容区改为表格优先，而不是左侧列表优先 - 表格列包括：名称、描述、行数、大小、更新时间、操作 - 名称列作为主列，文件名加粗，描述作为次级文本 - 行数和大小要便于快速扫描 - 操作列使用图标按钮或轻量文字按钮：编辑、删除 - 点击某一行后，可以在右侧轻量详情面板或表格下方详情区展示 ID、Hash、更新时间等信息 - 页面整体适合 20 到 100 个字典的管理场景  视觉风格： - 保持当前产品的黑白灰、极简、工具型后台风格 - 信息密度比现在更高，但不要拥挤 - 使用清晰边框、浅灰分隔线、紧凑表格行 - 不要大面积空白 - 不要卡片堆叠，不要营销风，不要渐变背景，不要玻璃拟态 - 整体像成熟的安全工具 / 运维后台 / 资源管理控制台  画面要求： - 桌面端 16:9 宽屏截图 - 中文界面 - 高保真 UI mockup - 看起来像真实产品截图，而不是概念海报 - 不要新增后端暂时没有的字段，比如分类、标签、状态、使用次数、来源
```

```

```

## 第二步：用 GPT Image-2 生成设计稿

把提示词和原始截图扔给 GPT 的图片模型，让它出设计稿：

![image-20260507163615011](https://mmbiz.qpic.cn/mmbiz_png/xZjx15SZGqJxaLYmqnXibzrWtYZbPqT4ZcushKvHeWLhnYd4wQmvicDLjkwQkcBNfgPCibyKCJOgEVmtfWcptr9ibteiaTV7PRIdlC596NPQtaEw/640?wx_fmt=png)可以看到，页面层级比原版强了不少。这就是 GPT 图片模型当下的优势——它投喂了大量优秀 SaaS 系统的设计。如果绕过图片模型，直接让 GPT 5.4 或 5.5 设计，效果会差很多。

## 第三步：根据实际需求迭代

设计中我发现，很多字典并不只属于一个类型。比如某个字典既可以用于 API 路径，也可以用于子域名 fuzz；某个敏感路径字典，可能同时服务目录扫描和指纹识别。不容易归类为单一类型。

于是我让 AI 重组了提示词，重新喂给 GPT 图片模型：

![image-20260507164039680](https://mmbiz.qpic.cn/mmbiz_png/xZjx15SZGqJ9ib71ol6qQ1eH19K1M8oQbtNBMW17logeA5ln21v6ZvntLYDmQZUtJ1D78F8TP5tjJC0XMHhEVtwKicCYOTQEYZ5JWEkoib2hnI/640?wx_fmt=png)这个版本明显好很多，但细节处理仍有不少问题——这也是当前 AI 的局限。需要根据这张图片让 AI 做整体设计对齐，再通过 Codex 桌面端的能力进行调整。

## 第四步：让 GPT 5.4 对齐实现

以下是让 GPT 5.4 根据图片进行对齐的提示词：

```
根据我提供的截图，对字典管理页面进行重构对齐，直到 UI 设计完全一样，一次性完成。
```

```

```

发送过去后，半小时再回来看，页面已经完成了 UI 重构：

![image-20260507164337587](https://mmbiz.qpic.cn/mmbiz_png/xZjx15SZGqL5TxgAmw5lcL2M5R9d9APtspKoSEL5wBEmDCEZubdjfyCmh5Tg7fSibgib6pJFRUhc1FGFE7qvNJScA4icWtPzpMS2nnwzgv9yrY/640?wx_fmt=png)可以看到重构后的页面与设计图差别仍然很大，问题不少。这时候就需要利用 Codex 桌面版进行手动调整：

![image-20260507165346118](https://mmbiz.qpic.cn/sz_mmbiz_png/xZjx15SZGqIeHnvEEWrIlMXrLJPaHsf2GGakhMPrlZe2X9nAYaOnguUycNHVicv2kWpnXOdWu6m4qWsgA1mgDAMXfMMGLsb8Le3DDd83JqVc/640?wx_fmt=png)经过几个小时的反复微调，最终完成重构：

![image-20260507202944133](https://mmbiz.qpic.cn/mmbiz_png/xZjx15SZGqIaBNrbbJl7lESdWPnUibORw7RiaNowSyxp3micwYXKicuekDFvFXjh07icnPqkzS9MsrswnKYgfoYQrc84hIXlJQcELRy4Ft6FJzqQ/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHJLT0krIpLicq1SDppPicWtD9WT2vqMxfSPoDTel0zk7r49TmrRBTiaBickOiaUTrjNdD4YoIzFibCLVu1g/0?wx_fmt=png)

塔罗安全学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHJLT0krIpLicq1SDppPicWtD9WT2vqMxfSPoDTel0zk7r49TmrRBTiaBickOiaUTrjNdD4YoIzFibCLVu1g/0?wx_fmt=png)

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