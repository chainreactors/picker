---
title: Strata：用显存+内存+硬盘协同调度，让普通电脑跑 1250 亿参数模型
url: https://blog.upx8.com/Strata-1250
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-26
fetch_date: 2026-10-27T07:04:42.540249
---

# Strata：用显存+内存+硬盘协同调度，让普通电脑跑 1250 亿参数模型

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
Strata：用显存+内存+硬盘协同调度，让普通电脑跑 1250 亿…

# Strata：用显存+内存+硬盘协同调度，让普通电脑跑 1250 亿参数模型

[资源](https://blog.upx8.com/Free)
10-27
·
约 1 分钟
·
黑海洋
·

3,565

## ![907c0db9c8b8c55f.jpg](https://img.776161.xyz/blogupx8/2026/10/907c0db9c8b8c55f.jpg)

## 一、Strata 是什么

* GitHub 上的开源模型部署工具，目标是让硬件配置有限的普通电脑也能运行超大参数语言模型，最高支持 **1250 亿参数（125B）**。
* 即使显卡只有 **8GB 显存**，也不一定只能跑小模型，本地运行大模型的硬件门槛有望降低。

## 二、工作原理

* 核心思路是**模型权重分层存放和加载**：

  + 部分数据放入**显存**；
  + 其余数据利用**系统内存**；
  + 必要时借助**硬盘空间**；
  + 通过显存、内存、硬盘协同调度，突破显存容量的部分限制。
  + 官方/文章称：相同模型、相同提示词下，Strata 速度比 **llama.cpp 快近 4 倍**。

  ## 三、部署方法

  1. **下载开源 Strata 项目**

     + 下载地址：[https://github.com/Niko1221/Strata/releases/tag/v0.2.6](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL05pa28xMjIxL1N0cmF0YS9yZWxlYXNlcy90YWcvdjAuMi42)
     + 下载后直接打开安装，会根据电脑硬件推荐最适合的模型和部署环境。
     + 支持 **N卡、A卡、Mac、Linux** 等系统。
  2. **加载本地模型**

     + 如果之前下载过开源模型，可直接载入：
     + 点击左侧 **模型 → 管理模型 → 使用本地 GGUF 格式的模型**，加载即可。
     + 自带**监控面板**。

  ## 四、一句话总结

  Strata 通过显存、内存、硬盘协同调度来分层加载模型权重，试图让 8GB 显存级别的普通电脑也能运行 125B 超大模型，并支持本地 GGUF 模型加载和多平台部署。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[上一篇
一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构](https://blog.upx8.com/Agent-Skills-Skill)
[下一篇
Work破甲包使用教程：用四个md文件改掉 AI 的人格](https://blog.upx8.com/Work-md-AI)

## 相关文档

* [美初创公司将270亿参数模型压进iPhone
  07-10](https://blog.upx8.com/%E7%BE%8E%E5%88%9D%E5%88%9B%E5%85%AC%E5%8F%B8%E5%B0%86270%E4%BA%BF%E5%8F%82%E6%95%B0%E6%A8%A1%E5%9E%8B%E5%8E%8B%E8%BF%9BiPhone)
* [Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新
  10-24](https://blog.upx8.com/Hoistbay-S3-CloudFront)
* [技能制造技能的skill
  10-23](https://blog.upx8.com/skill)
* [C盘清理神器 (Skills)
  10-23](https://blog.upx8.com/C-Skills)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [一、Strata 是什么](#sec-1)
* [二、工作原理](#sec-2)
* [三、部署方法](#sec-3)
* [四、一句话总结](#sec-4)

[![黑海洋](https://blog.upx8.com/logo.webp)
**黑海洋**
WIKI](https://blog.upx8.com/)

黑海洋专注 AI 智能体、程序开发、开源工具与免费资源分享，提供保姆级部署教程、源码下载、云服务器运维与安全资讯。

分类

[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)

常用

[全部文档](https://blog.upx8.com/all.html)
[RSS 订阅](https://blog.upx8.com/feed/)
[RSS 评论](https://blog.upx8.com/feed/comments/)
[Sitemap](/sitemap.xml)

关于

[关于本站](/about.html)
[友情链接](https://blog.upx8.com/links.html)
[我的收藏](https://blog.upx8.com/library.html)

Copyright © 2026 黑海洋

[浙ICP备2021040518号-1](https://beian.miit.gov.cn)

站点正常

[首页](https://blog.upx8.com/)

分类

搜索
[收藏](https://blog.upx8.com/library.html)

**全部分类**

[资源
2096](https://blog.upx8.com/Free)
[安全
374](https://blog.upx8.com/os_security)
[开发
533](https://blog.upx8.com/code)
[资讯
2114](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)