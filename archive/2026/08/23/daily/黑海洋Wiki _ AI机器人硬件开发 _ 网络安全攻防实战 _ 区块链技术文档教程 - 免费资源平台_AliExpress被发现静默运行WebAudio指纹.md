---
title: AliExpress被发现静默运行WebAudio指纹
url: https://blog.upx8.com/AliExpress%E8%A2%AB%E5%8F%91%E7%8E%B0%E9%9D%99%E9%BB%98%E8%BF%90%E8%A1%8CWebAudio%E6%8C%87%E7%BA%B9
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-08-23
fetch_date: 2026-08-24T02:59:06.374852
---

# AliExpress被发现静默运行WebAudio指纹

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# AliExpress被发现静默运行WebAudio指纹

发布时间:
2026-08-23 New Article

分类:
[新闻简报/News](https://blog.upx8.com/news)

热度:
3545

有开发者注意到了一个奇怪的现象：蓝牙耳机支持多点蓝牙音频，能同时连接 PC 和手机，PC 通常优先播放音频，只有在 PC 没有播放内容时手机才会播放音频。这位开发者注意到，在 Firefox 或 Chrome 浏览器中打开 AliExpress 网页后，手机会停止播放音频，关闭网页则会恢复。这位开发者随后展开了调查，发现高度混淆的阿里巴巴安全脚本会创建两个 WebAudio 图形，成为浏览器指纹的一部分，该静默运行的 WebAudio 指纹会干扰多点蓝牙音频。用户可利用 uBlock Origin 扩展屏蔽阿里巴巴的脚本 collina.js 和 fireyejs.js 关闭这一指纹。

—— [奇客](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuc29saWRvdC5vcmcvc3Rvcnk_c2lkPTg1MTUw)

[取消回复](https://blog.upx8.com/AliExpress%E8%A2%AB%E5%8F%91%E7%8E%B0%E9%9D%99%E9%BB%98%E8%BF%90%E8%A1%8CWebAudio%E6%8C%87%E7%BA%B9#respond-post-10221)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")