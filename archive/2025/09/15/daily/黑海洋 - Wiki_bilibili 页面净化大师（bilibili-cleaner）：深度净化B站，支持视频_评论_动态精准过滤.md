---
title: bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤
url: https://blog.upx8.com/4851
source: 黑海洋 - Wiki
date: 2025-09-15
fetch_date: 2025-10-02T20:10:00.198080
---

# bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤

发布时间:
2025-09-14

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
24424

## 工具简介

**bilibili 页面净化大师（bilibili-cleaner）是一款针对B站网页端的净化与过滤脚本。它可以清理顶栏、视频列表、播放器与评论区的冗余元素，并基于时长、UP主、标题关键词、BV号**等维度筛选视频；同时支持对**评论与动态**按**用户名、关键词、评论类型、用户等级**进行过滤。

* GitHub：`https://github.com/festoney8/bilibili-cleaner`
* GreasyFork：`https://greasyfork.org/zh-CN/scripts/479861`

## 核心功能

### 页面净化优化

* 适配新版B站网页，默认用户已登录，**大会员体验更佳**。
* 可与多项功能混搭，配合浏览器缩放获得更清爽的版面。
* 不适配老版本与未登录状态页面。

### 视频过滤（黑白名单共用，全站有效）

* **白名单优先级高于黑名单**，命中白名单的视频不会隐藏。
* 开启UP主过滤后，可**右键单击UP主**直接屏蔽。
* 开启BV号过滤后，可**右键单击视频标题**直接屏蔽。
* 标题关键词与白名单对大小写不敏感，支持正则：使用`/ ... /`包裹，例如`/abc|\d+/`，默认**ius模式**（不区分大小写，支持跨行）。
* **注意**：带 `index.html` 的首页不生效，请使用无后缀首页 `https://www.bilibili.com/`。

### 评论过滤

* 开启用户名过滤后，在评论区**右键单击用户名**即可屏蔽。
* 关键词黑名单大小写不敏感，正则语法与视频过滤一致（示例：`/abc|\d+/`，默认ius模式）。
* **白名单高优先级**，命中白名单的评论不隐藏。

### 动态过滤

* 支持按**用户名、视频标题**等条件筛选动态内容，减少无关信息干扰。

## bilibili 页面净化大师（bilibili-cleaner）效果

![preview | bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤](https://p.sda1.dev/15/4cc506128a02e83928321c2b37059117/preview.webp "bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤 2")

![preview homepage | bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤](https://p.sda1.dev/15/c1ae913086d223efaa13e86fdd61558d/preview-homepage.webp "bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤 3")

![preview dynamic | bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤](https://p.sda1.dev/15/88296c268f2599fbe15d84143c30caf9/preview-dynamic.webp "bilibili 页面净化大师（bilibili-cleaner）：深度净化B站，支持视频/评论/动态精准过滤 4")

## 使用建议（避免误伤与性能问题）

* **时长过滤**不宜过长，建议 **60–90 秒**，避免错过优质内容。
* **关键词**尽量具体，避免过度屏蔽导致推荐区“空洞”。
* **正则**需谨慎书写，过宽可能引发大量内容被屏蔽与频繁加载。
* **白名单**影响范围大，确认后再添加；若屏蔽后内容仍存在，可能因命中白名单。
* 热门区块如「热门视频」「每周必看」「排行榜」常见低质量内容，可前往对应页**统一屏蔽**；遇到高质量UP主可**加入白名单**保存。

## 已知问题与处理

* 给UP主充电若出现**载入失败（NaN）**，关闭通用项\*\*「URL参数净化」\*\*并刷新后再尝试。
* **特殊活动直播**修改脚本设置后需**刷新**才生效；此场景下**弹幕净化不生效**。

## bilibili 页面净化大师（bilibili-cleaner）安装与获取

开源仓库（说明与源码）：[https://github.com/festoney8/bilibili-cleaner](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2Zlc3RvbmV5OC9iaWxpYmlsaS1jbGVhbmVy "bilibili 页面净化大师GitHub地址")

安装页面（GreasyFork）：[bilibili 页面净化大师](https://blog.upx8.com/go/aHR0cHM6Ly9ncmVhc3lmb3JrLm9yZy96aC1DTi9zY3JpcHRzLzQ3OTg2MS1iaWxpYmlsaS0lRTklQTElQjUlRTklOUQlQTIlRTUlODclODAlRTUlOEMlOTYlRTUlQTQlQTclRTUlQjglODg "bilibili 页面净化大师安装地址")

[取消回复](https://blog.upx8.com/4851#respond-post-4851)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")