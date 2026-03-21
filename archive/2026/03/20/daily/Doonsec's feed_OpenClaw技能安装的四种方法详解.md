---
title: OpenClaw技能安装的四种方法详解
url: https://mp.weixin.qq.com/s/zKmWj0LhQFv_-wzgOh7muw
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:00:17.984313
---

# OpenClaw技能安装的四种方法详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I4ibOKsL0MdDdqx9gSh7IC0APC17d4LiaSBRicUfnH08tADcqPyNGdr9LqWHtUicdex4nIzMibWLWiaZ1NKhzq0E0gFIJoB0bo8rMoroboZcxbAuQ/0?wx_fmt=jpeg)

# OpenClaw技能安装的四种方法详解

原创

SOC安全分析之旅

![]()

在小说阅读器中沉浸阅读

01

ClawHub仓库安装法

操作流程：打开ClawHub仓库并搜索目标技能（如"word-docx"）复制技能名称后执行npm install -g clawhub运行clawhub install [技能名]完成安装

示例演示：npm install -g clawhubclawhub install word-docx

02

Skills.sh命令行安装

实施步骤：访问skills.sh网站搜索技能复制提供的安装命令（如npx skills add vercel-labs/skills）选择全局安装模式（Global）并确认

安装选项：

| 安装类型 | 安装路径 | 适用场景 |
| --- | --- | --- |
| Project | 当前项目目录 | 局部使用 |
| Global | ~/.agents/skills/ | 全系统可用 |

03

Find-Skills自动安装

智能检索：

* ✓ 通过语义搜索匹配技能需求

* ✓ 自动推荐高评分技能（按下载量排序）

安装验证：ls ~/.agents/skills/

04

离线包手动安装

适用场景：无网络环境或定制化需求

核心优势：避免依赖在线仓库

注意事项：需自行处理版本兼容性

05

技术细节

所有方法最终安装路径统一为~/.agents/skills/

推荐使用Symlink方式保持技能更新同步

典型安装耗时：30秒-3分钟（视网络状况）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

SOC安全分析之旅

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

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