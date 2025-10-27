---
title: UptimeRobot API 的在线状态面板（检测心跳、监控ping）
url: https://blog.upx8.com/3119
source: 黑海洋 - WIKI
date: 2022-11-30
fetch_date: 2025-10-04T00:05:26.311185
---

# UptimeRobot API 的在线状态面板（检测心跳、监控ping）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# UptimeRobot API 的在线状态面板（检测心跳、监控ping）

发布时间:
2022-11-29

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
18004

# uptime-status

一个基于 UptimeRobot API 的在线状态面板

[![image](https://user-images.githubusercontent.com/25887822/178935137-6d23521d-5894-4fb8-922d-3575be4f7abc.png)](https://user-images.githubusercontent.com/25887822/178935137-6d23521d-5894-4fb8-922d-3575be4f7abc.png)

## 事先准备

* 您需要先到 [UptimeRobot](https://blog.upx8.com/go/aHR0cHM6Ly91cHRpbWVyb2JvdC5jb20v "UptimeRobot") 添加站点监控，并在 My Settings 页面获取 API Key
* 您需要拥有一个网站空间，常见的 Nginx / PHP 等空间即可，甚至是阿里云的 OSS 等纯静态空间也行

## 如何部署：

* 下载并解压缩：[uptime-status.zip](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3liL3VwdGltZS1zdGF0dXMvcmVsZWFzZXMvbGF0ZXN0L2Rvd25sb2FkL3VwdGltZS1zdGF0dXMuemlw "uptime-status.zip")
* 修改 `config.js` 文件：
  + `SiteName`: 要显示的网站名称
  + `ApiKeys`: 从 UptimeRobot 获取的 API Key，支持 Monitor-Specific API Keys 和 Read-Only API Key
  + `CountDays`: 要显示的日志天数，建议 60 或 90，显示效果比较好
  + `ShowLink`: 是否显示站点链接
  + `Navi`: 导航栏的菜单列表

* 将所有文件上传到网站空间

⚠️ 如果没有修改代码的需求，您不需要 git clone 本项目，只需要下载 Release 的文件包即可。

⚠️ 想获得最新站点列表数据，需要删除api，重新生成

**demo：[https://status.org.cn/](https://blog.upx8.com/go/aHR0cHM6Ly9zdGF0dXMub3JnLmNuLw)**

**Githup：[https://github.com/yb/uptime-status](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3liL3VwdGltZS1zdGF0dXM)**

[取消回复](https://blog.upx8.com/3119#respond-post-3119)

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