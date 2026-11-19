---
title: 米饭云盘（mifun-storage）：把 Telegram 频道当硬盘，零成本自建个人图床
url: https://blog.upx8.com/mifun-storage-Telegram
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-18
fetch_date: 2026-11-19T09:46:04.517641
---

# 米饭云盘（mifun-storage）：把 Telegram 频道当硬盘，零成本自建个人图床

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
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
米饭云盘（mifun-storage）：把 Telegram 频道当硬盘，零成…

# 米饭云盘（mifun-storage）：把 Telegram 频道当硬盘，零成本自建个人图床

[资源](https://blog.upx8.com/Free)
11-18
·
约 20 分钟
·
黑海洋
·

5,050
·
[1 条评论](#comments)

> 摘要：米饭云盘是一个把文件二进制存在 Telegram Channel、本地只存元数据的轻量存储系统，主打个人图床 / Markdown 图床。上传下载全程走 Node.js Stream，不落临时文件，官方宣称"无限容量、不占本机与服务器空间"。本文梳理它的真实能力边界、50 MiB / 20 MiB 硬限制、Docker 部署、图床外链、缓存与鉴权配置，以及上手前必须知道的几个坑。
>
> 标签：`自建图床` `Telegram` `对象存储` `Docker` `Markdown图床` `开源`
>
> 建议 slug：`mifun-storage-telegram-picture-bed`

![米饭云盘 Web 文件管理器界面：macOS 风格浅色窗口，左侧为存储位置与八色快捷标签，顶部有网格/列表切换、名称排序、管理员登录、暗色模式和搜索框，主区域以网格展示文件夹与文件，底部显示"已加载 13/13 个项目，共 18 MB"](https://i0.wp.com/cdn.skyimg.net/up/2026/11/18/fa4b835f310ad34009c894e38bb59030.webp)

## 先看数据

| 项目 | 值 |
| --- | --- |
| 仓库 | [AndySkaura/mifun-storage](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0FuZHlTa2F1cmEvbWlmdW4tc3RvcmFnZQ.cd4b2f7e20) |
| Star / Fork | **287 / 30** |
| 许可 | **MIT** |
| 主语言 | TypeScript（后端 Fastify 5 + Prisma 6；GitHub 页面显示 HTML 是因 `web/` 下含前端页面） |
| 建库 / 最后推送 | 2026-07-27 / 2026-11-16 |
| Node 要求 | **Node.js 20+** |
| 核心依赖 | Fastify 5 · Prisma 6 · grammY 1.45（Telegram Bot）· SQLite / MySQL 8.x · Tailwind CSS · ECharts · sharp |
| 在线 Demo | [p.kuraa.cc](https://blog.upx8.com/go/aHR0cHM6Ly9wLmt1cmFhLmNj.b0fb4ac76d)（作者标注为备用服务器，不为联通质量负责） |
| Docker 镜像 | `andyskaura/mifun-storage` |

项目 2026 年 7 月才建库，不到四个月攒到近 300 星，迭代活跃。**这是新项目**，生产环境用之前先把数据备份方案想清楚。

## 它到底解决了什么

自建图床的老问题：图存自己服务器，要买硬盘、要防丢、要扛流量。米饭云盘的思路是把这个负担整体外包给 Telegram：

* **文件二进制只存 Telegram Channel**，你的服务器不存一个字节的图片本体；
* **SQLite / MySQL 只存目录结构、文件元数据和 Telegram 映射**（哪个文件对应哪条频道消息）；
* 上传下载用 Node.js Stream **边收边转**，不写本地临时文件；
* 对外暴露一个 Finder 风格的 Web 文件管理器，用起来像网盘。

结果就是：**机器只要跑得住一个 Node 进程，容量随 Telegram 频道走**。对个人博客、Markdown 笔记、论坛配图这类"文件多、单个小、访问量不高"的场景，这套模型很省事。

先泼一盆冷水：它**不是完整网盘**。没有多用户、没有分享系统、没有去重、没有细粒度权限体系。定位就是单人 / 小团队自用的低并发图床与小文件归档工具。

## 能力边界：这几条限制绕不过去

**单文件大小是 Telegram Bot API 定的，不是本项目定的：**

| 方向 | 上限 | 说明 |
| --- | --- | --- |
| 上传 | **50 MiB** | 对应 `MAX_UPLOAD_SIZE=52428800` |
| 下载 | **20 MiB** | 对应 `MAX_DOWNLOAD_SIZE=20971520`，超限返回 `DOWNLOAD_FILE_TOO_LARGE` |

把环境变量调大**没用**，官方 Bot API 就是这条线。真要突破，得自己再部署一套 [Telegram Bot API Server](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3RkbGliL3RlbGVncmFtLWJvdC1hcGk.ce2ee3b736) 并改造项目的 Telegram 接入层——成本和复杂度都上一个量级，作者明确说这不是项目初衷。环境变量只建议按实际需求**调小**。

另外几条要记牢：

* "无限上传"指的是频道可持续存，**不是**承诺无限容量、无限可用性或服务等级；
* 元数据（目录 / 标签 / 映射）依赖本地 SQLite 或 MySQL，**这部分丢了文件就找不回来了**，数据库必须备份；
* 不适合高并发网盘、多人协作、频繁随机读写的对象存储场景。
* 不提供 CDN、图片压缩裁剪、格式转换、防盗链、高可用——这些得自己在外面加。

## 安装部署

### 环境准备

1. Node.js 20+；
2. 一个 Telegram Bot（找 @BotFather 拿 Token）；
3. 一个专门存文件的 Telegram Channel，把 Bot 拉进去并给**发布消息**权限；
4. Channel ID，形如 `-1001234567890`。

默认内置 SQLite，`data/mifun-storage.db` 自动建表，**不用装数据库**。要接已有 MySQL 8.x 时再配置 `DATABASE_URL`。

### 方式一：Docker Compose（推荐）

```
mkdir mifun-storage && cd mifun-storage
curl -O https://raw.githubusercontent.com/AndySkaura/mifun-storage/main/docker-compose.yml
curl -o .env https://raw.githubusercontent.com/AndySkaura/mifun-storage/main/.env.example
```

编辑 `.env`，至少填这两项：

```
TELEGRAM_BOT_TOKEN=1234567890:你的真实token
TELEGRAM_STORAGE_CHAT_ID=-1001234567890
```

不用外部 MySQL 就保持 `DATABASE_URL` 留空。然后启动：

```
docker compose up -d
docker compose ps
docker compose logs -f tgfs
```

访问 `http://localhost:3000`。

日常运维命令：

```
# 重启 / 停止 / 启动
docker compose restart
docker compose stop
docker compose start

# 手动更新到最新版本
docker compose pull && docker compose up -d
docker image prune -f

# 删除容器和网络，但保留 SQLite 数据
docker compose down
```

> **`docker compose down -v` 千万别跑**——`-v` 会连 SQLite 数据卷一起删掉。

Compose 里还带了一个可选的 Watchtower 自动更新配置，默认不启动。它要挂载 Docker Socket，等于把宿主机 Docker 管理权限交给容器，**只适合可信镜像**，不需要就别开：

```
docker compose --profile auto-update up -d
```

### 方式二：直接用 Docker 镜像

```
curl -o .env https://raw.githubusercontent.com/AndySkaura/mifun-storage/main/.env.example
# 填好 Telegram 配置后
docker run -d \
  --name mifun-storage \
  --restart unless-stopped \
  --env-file .env \
  -e HOST=0.0.0.0 \
  -v mifun_storage_data:/app/data \
  -p 3000:3000 \
  andyskaura/mifun-storage:latest
```

注意更新方式：`docker restart` 不会更新镜像，光 `docker pull` 也不会替换正在跑的容器。得停掉、删掉、再用新镜像重建。重建不会删 `mifun_storage_data` 卷。

### 方式三：源码本地运行

```
cp .env.example .env
# 编辑 .env，填 Telegram 配置
npm install
npm run dev          # 开发模式，默认 http://localhost:3000
```

生产模式：

```
npm run build
npm start
```

如果配了 MySQL，首次部署和每次 Schema 变更后都要跑一次迁移：

```
npm run prisma:deploy
```

### 关键环境变量

| 变量 | 默认值 | 作用 |
| --- | --- | --- |
| `PORT` / `HOST` | `3000` / `0.0.0.0` | 监听地址 |
| `SITE_URL` | 空 | 生成 `/about` 页的 Canonical、OG、`robots.txt`、`sitemap.xml` 绝对地址 |
| `ABOUT_ENABLED` | `true` | 设 `false` 关闭统计页与统计 API，并隐藏首页统计入口 |
| `DATABASE_URL` | 空 | 留空用 SQLite；MySQL 8.x 连接串 |
| `TELEGRAM_BOT_TOKEN` | 必填 | Bot Token |
| `TELEGRAM_STORAGE_CHAT_ID` | 必填 | 存储频道 ID |
| `ADMIN_TOKEN` | 空 | 管理员凭证，留空 = 关闭鉴权（见下文安全提醒） |
| `MAX_UPLOAD_SIZE` | `52428800` | 上传上限，只建议调小 |
| `MAX_DOWNLOAD_SIZE` | `20971520` | 下载上限，只建议调小 |

## 当作图床用：拿到长期稳定的外链

图片上传成功后，响应里有个 `contentToken`——这是该文件长期稳定的随机访问凭证。拼出图片地址：

```
https://你的域名/api/files/content/<contentToken>/preview
```

原图、缩略图、下载各有入口：

```
# 内联预览（图片可直接 <img> 引用）
curl http://localhost:3000/api/files/content/<contentToken>/preview

# JPEG 缩略图
curl -o thumbnail.jpg http://localhost:3000/api/files/content/<contentToken>/thumbnail

# 下载原图
curl -OJ http://localhost:3000/api/files/content/<contentToken>/download
```

`contentToken` 是 128 bit 随机生成的 22 位 Base64URL 字符串，**不暴露递增文件 ID**，方便配长期 CDN 缓存。Web 管理器里对图片双击可全屏预览、右键复制的就是这个公共链接。

上传本身也支持 API：

```
curl -X POST http://localhost:3000/api/files/upload \
  -F 'parentId=1' \
  -F 'file=@./example.png'
```

想保持真正的流式上传，multipart 字段按 `parentId` → 可选 `thumbnail` → `file` 顺序发。缩略图必须是 < 200 KiB、最大边 ≤ 320px 的 JPEG。网页端上传图片时浏览器会自动生成缩略图一起存进 Telegram。

## 缓存与 CDN：一条配错就出安全事故

这是整套系统里最需要认真对待的部分。公共内容和私有内容必须走两套规则：

| 内容类型 | 路径前缀 | 缓存策略 |
| --- | --- | --- |
| 公共内容 | `/api/files/content/...` | 可长期缓存；撤销链接时要主动 purge |
| 私有内容 | `/api/files/private-content/...` | **禁止共享缓存**，且必须转发 `Authorization` 头 |

Nginx 参考配置：

```
# 私有内容：保留鉴权头，禁用共享缓存
location ^~ /api/files/private-content/ {
    proxy_pass http://127.0.0.1:3000;
    proxy_set_header Host $host;
    proxy_set_header Authorization $http_authorization;
    proxy_cache off;
}

# 公共内容：由应用返回长期缓存响应头
location ~ ^/api/files/content/[A-Za-z0-9_-]+/(download|preview|thumbnail)$ {
    proxy_pass http://127.0.0.1:3000;
    proxy_set_header Host $host;
}
```

用 CDN 时按三条来：

1. `/api/files/private-content/` 前缀 → 绕过缓存（Cloudflare 配 `Bypass cache`）；
2. `/api/files/content/<token>/(download|preview|thumbnail)` → 允许长期缓存（Cloudflare 配 `Eligible for cache`，Edge TTL 可设一年）；
3. 别覆盖应用返回的 `private`、`no-store`、`Vary: Authorization` 响应头。

私有内容响应带 `Cache-Control: private, max-age=31536000, immutable`（允许浏览器本地长期保存）和 `Cloudflare-CDN-Cache-Control: no-store`（禁止 CDN 缓存）。**私有链接一旦被共享缓存记住，等于鉴权形同虚设**。

## 管理员鉴权与存储位置

### 管理员 Token

`ADMIN_TOKEN` 留空 = **关闭鉴权，所有人匿名可写**。生产环境务必设置：

```
openssl rand -hex 32
```

配置后，删除项目、管理存储位置属于管理员操作，请求头带：

```
Authorization: Bearer <ADMIN_TOKEN>
```

上传、建文件夹、复制粘贴允许匿名。Web 管理器右上角"管理员登录"验证成功后，Token 只存在当前标签页的 `sessionStorage`，关标签页即失效。别把 Token 塞进 URL 或下载链接。

### 存储位置

存储位置是相互独立的一级空间，类似多个磁盘分区，迁移时会建默认的 `mifun-storage` 并把已有文件归入其中。管理员可为每个位置设置匿名权限：

* `hidden`：无密码时匿名用户不可见；设密码后显示锁定状态，解锁可读；
* `read`：匿名可浏览、搜索、预览、下载、按标签筛选，不能写入；
* `write`：匿名还能上传、建文件夹、粘贴、改标签。

几点细节：
...