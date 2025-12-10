---
title: QM-Music：构建的轻量级私有云音乐服务器
url: https://blog.upx8.com/4919
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-09
fetch_date: 2025-12-10T03:21:30.298899
---

# QM-Music：构建的轻量级私有云音乐服务器

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# QM-Music：构建的轻量级私有云音乐服务器

发布时间:
2025-12-09

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
2589

## QM-Music：专为音乐爱好者打造的轻量级私有云音乐服务器

**QM-Music** 是一款基于 Subsonic 协议开发的开源音乐服务器，专注于为用户提供低资源占用、高性能、全平台兼容的私有化音乐解决方案。通过 Docker 快速部署，你可以轻松在任意设备上搭建属于自己的云端音乐库，随时随地访问与播放，数据完全掌控在你手中。

---

### 💡截图界面

![QM-Music：构建的轻量级私有云音乐服务器](https://img.7761.cf/img/20251209/3380324596.png)![QM-Music：构建的轻量级私有云音乐服务器](https://img.7761.cf/img/20251209/2254490121.png)

### 🚀 核心亮点

#### 🐳 容器化部署，极速上手

支持 Docker 和 docker-compose 一键部署，无需繁琐环境配置，几分钟即可运行。

#### 🌱 超轻资源占用

运行内存仅约 150MB，适合各类轻量服务器与本地设备。

#### 🎧 完全兼容 Subsonic 协议

支持音流、feishin、Amperfy、substreamer、music-assistant 等客户端无缝接入。

#### 🔄 智能音频转码

可按需启用 libmp3lame/acc 动态转码，节省移动网络流量。

#### 📁 支持主流音频格式

全面兼容 MP3、FLAC、AAC、WAV 等格式，无需手动转换。

#### 🔒 私有化部署，数据可控

本地存储与自建服务器实现完全的数据隐私保障。

---

### 🎧 多端用户体验优化

* 多用户权限管理
* 自定义播放列表与收藏夹
* 本地/在线歌词智能同步
* 结构化音乐展示（按专辑、歌手、流派分类）
* 播放历史追踪与个性化偏好记录

---

### 🔍 高效的音乐管理与探索功能

* 定时扫描目录，自动刷新曲库
* ID3 标签与专辑元数据智能识别
* 全局搜索功能，快速定位歌曲/专辑/歌手
* 推荐相似歌曲与歌手，助力音乐发现
* 支持流派筛选，探索多样化风格

---

### ⚙️ 配置灵活，支持拓展生态

QM-Music 支持丰富的环境变量设置，配合 Spotify、Last.fm 等 API 可拓展更多元数据体验。使用者可根据实际需求进行深度定制。

---

### 🖥️ 快速部署指令

**Docker 一键启动：**

```
docker run -d \
  --name qm-music \
  -p 6688:6688 \
  -v /your/music:/data/qm-music/music_dir \
  -v /your/db:/data/qm-music/db \
  -v /your/cache:/data/qm-music/cache \
  -e QM_FFMPEG_ENABLE=true \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  qmmusic/qm-music:latest
```

**Docker Compose 示例：**

```
services:
  qm-music:
    image: qmmusic/qm-music:latest
    ports:
      - "6688:6688"
    volumes:
      - /your/music:/data/qm-music/music_dir
      - /your/db:/data/qm-music/db
      - /your/cache:/data/qm-music/cache
    environment:
      - QM_FFMPEG_ENABLE=true
      - TZ=Asia/Shanghai
    restart: unless-stopped
```

部署完成后，通过浏览器访问 `http://[服务器IP]:6688`，使用默认账号 `admin/admin` 登录并立即修改密码。

---

### 📜 开源与免责声明

本项目遵循 Apache 2.0 协议开源，支持自由修改与二次开发。仅限学习与研究用途，使用者须自行承担相关法律与风险责任。

项目地址：🔗 [https://github.com/chenqimiao/qm-music](https://github.com/chenqimiao/qm-music "QM-Music 开源地址")

[取消回复](https://blog.upx8.com/4919#respond-post-4919)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")