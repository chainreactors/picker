---
title: RSSHub 公共实例整理与自建教程
url: https://blog.upx8.com/RSSHub
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-31
fetch_date: 2026-11-01T08:21:03.686248
---

# RSSHub 公共实例整理与自建教程

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
RSSHub 公共实例整理与自建教程

# RSSHub 公共实例整理与自建教程

[资源](https://blog.upx8.com/Free)
10-31
·
约 8 分钟
·
黑海洋
·

3,561

## 简介

RSSHub 是一个开源的 RSS 生成器,能给本身没有 RSS 的网站(B 站、微博、GitHub Trending、Telegram 频道等)生成订阅源。不想自己搭服务时,可以直接用别人公开的实例;但公共实例共享资源、随时可能失效,长期使用最好自建。

本文记录 4 个实测可用的公共实例,以及一份从零开始的自建教程,方便日后查阅。

## 可用的公共实例

以下 4 个实例在 2026-10-31 实测可以使用,均来自 [RSSHub 官方公共实例列表](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvemgvZ3VpZGUvaW5zdGFuY2Vz)。

| 实例地址 | 服务器位置 | 维护者 |
| --- | --- | --- |
| https://rsshub.rssforever.com | 阿联酋 | Stille |
| https://hub.slarker.me | 美国 | Slarker |
| https://rsshub.ktachibana.party | 美国 | KTachibanaM |
| https://rsshub.isrss.com | 美国 | isRSS |

位置与维护者信息取自官方列表,该列表本身更新不频繁,仅供参考。

### 怎么用

把官方文档里的 `https://rsshub.app` 换成上表任意一个地址即可,路由部分不变。例如订阅 GitHub 每日 Trending:

```
https://rsshub.rssforever.com/github/trending/daily
```

路由大全见 [RSSHub 路由文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvcm91dGVzLw)。

## 使用技巧与注意事项

公共实例是志愿者提供的,稳定性没有保证,订阅前先做好这几件事:

* **先测再订**:打开实例首页,再请求一条简单路由(如 `/github/trending/daily`),确认能返回内容。
* **别只靠一个**:多个实例轮换使用,某个挂了就换。社区反馈公共实例经常出问题,域名过期后还可能被他人接管,地址要定期复查。
* **反爬严格的站点基本不行**:微博、Twitter/X、知乎等通常需要自己的 cookie,只能自建后配置。
* **隐私**:公共实例的运营者能看到你的请求,不要往 URL 里放私人 token。
* **自动容错**:可以部署 [rsshub-never-die](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0Nhb01laVlvdVJlbi9yc3NodWItbmV2ZXItZGll),它在多个实例之间做负载均衡和故障切换,订阅里只写一个地址。

`rsshub-never-die` 的实例配置示例(权重越大,被选中概率越高):

```
RSSHUB_NODE_URLS='https://rsshub.rssforever.com|weight=2, https://hub.slarker.me|weight=3, https://rsshub.ktachibana.party, https://rsshub.isrss.com'
```

## 自建 RSSHub 教程

推荐用 Docker 自建,最快 1 分钟跑起来。下面三步从简到全,配置细节以[官方部署文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvZGVwbG95Lw)为准。

### 前提

* 一台能跑 Docker 的机器(VPS、NAS、家里的小主机均可;放在家宽网络对反爬更友好)
* 已安装 Docker 与 Docker Compose
* 想对外访问时,准备一个域名

### 方式一:一行命令

```
docker run -d --name rsshub -p 1200:1200 diygod/rsshub
```

浏览器打开 `http://服务器IP:1200`,看到 RSSHub 首页即成功。再访问 `http://服务器IP:1200/github/trending/daily` 验证路由。

需要用到 Puppeteer 的路由(要无头浏览器渲染的站点),换成内置 Chromium 的镜像:

```
docker run -d --name rsshub -p 1200:1200 diygod/rsshub:chromium-bundled
```

### 方式二:Docker Compose(推荐)

加上 Redis 缓存,重复请求更快,也更不容易被目标网站限流。新建 `docker-compose.yml`:

```
services:
  rsshub:
    image: diygod/rsshub
    container_name: rsshub
    restart: always
    ports:
      - "1200:1200"
    environment:
      NODE_ENV: production
      CACHE_TYPE: redis
      REDIS_URL: "redis://redis:6379/"
      CACHE_EXPIRE: 600
    depends_on:
      - redis

  redis:
    image: redis:alpine
    container_name: rsshub-redis
    restart: always
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

启动与日常维护:

```
docker compose up -d          # 启动
docker compose logs -f rsshub # 看日志
docker compose pull && docker compose up -d   # 更新到最新版
```

要支持 Puppeteer 路由,可以改用 `diygod/rsshub:chromium-bundled` 镜像,或另加一个浏览器服务并设置 `PUPPETEER_WS_ENDPOINT`,具体写法参考官方 Compose 示例。

### 常用环境变量

在 `environment` 下添加。完整列表见[官方配置文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvZGVwbG95L2NvbmZpZw)。

| 变量 | 作用 |
| --- | --- |
| `PORT` | 监听端口,默认 1200 |
| `CACHE_TYPE` / `REDIS_URL` | 缓存类型与 Redis 地址 |
| `CACHE_EXPIRE` | 缓存时间(秒),调大可减少对目标站的请求 |
| `ACCESS_KEY` | 访问密钥,设置后请求需带 `?key=密钥` |
| `GITHUB_ACCESS_TOKEN` | 提高 GitHub 相关路由的 API 额度 |
| `PROXY_URI` | 给被墙或限制地区的站点配置代理 |

微博、知乎、B 站等站点需要登录态的路由,还要按各路由文档配置对应的 cookie 变量,这是自建最大的好处。

### 对外访问:域名与反向代理

不建议直接暴露 1200 端口。用 Caddy 可以自动签发 HTTPS 证书,配置只要两行:

```
rss.example.com {
    reverse_proxy 127.0.0.1:1200
}
```

用 Nginx 的话:

```
server {
    listen 80;
    server_name rss.example.com;

    location / {
        proxy_pass http://127.0.0.1:1200;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Nginx 方案再用 certbot 申请证书即可。

### 其他部署方式

没有服务器时,也可以部署到 Vercel、Railway、Zeabur 等平台,步骤见官方部署文档。免费额度和稳定性各有限制,Puppeteer 路由通常不支持。

### 公开前的安全检查

* 设置 `ACCESS_KEY`,避免实例被陌生人当免费代理刷
* 只用 HTTPS 对外提供服务
* cookie、token 只放环境变量,别写进公开仓库
* 定期 `docker compose pull` 更新,路由经常随目标网站变化而修复

## 备忘清单与参考

### 常见问题

| 现象 | 可能原因与处理 |
| --- | --- |
| 订阅突然没更新 | 公共实例挂了或限流,换一个实例地址再试 |
| 返回 403 / 反爬提示 | 目标站拦截了机房 IP,需自建并配置 cookie 或代理 |
| 路由 404 | 路由已变更或下线,查最新[路由文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvcm91dGVzLw) |
| 自建后页面打不开 | 检查防火墙是否放行端口,`docker compose logs rsshub` 看报错 |

### 备忘

* 订阅前用浏览器测试路由能否返回内容
* 每个订阅至少备一个备用实例
* 有条件就自建,并设置 `ACCESS_KEY`
* 定期复查实例是否仍可用

### 参考链接

* [RSSHub 公共实例列表](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvemgvZ3VpZGUvaW5zdGFuY2Vz)
* [RSSHub 部署文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvZGVwbG95Lw)
* [RSSHub 路由文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnJzc2h1Yi5hcHAvcm91dGVzLw)
* [rsshub-never-die(多实例容错代理)一键部署到 Cloudflare Workers](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0Nhb01laVlvdVJlbi9yc3NodWItbmV2ZXItZGll)
* [RSSHub 源码仓库](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0RJWWdvZC9SU1NIdWI)

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[上一篇
workbuddy一键完成所有任务（多账户）](https://blog.upx8.com/workbuddy)
[下一篇
LocModel：越狱大模型、AI 绘图、视频生成和 Agent 都装进本地电脑](https://blog.upx8.com/LocModel-AI-Agent)

## 相关文档

* [免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案
  11-01](https://blog.upx8.com/WAF-Worker-IP)
* [Clearcam：不换摄像头，给现有 RTSP 监控加上本地 AI
  11-01](https://blog.upx8.com/Clearcam-RTSP-AI)
* [LocModel：越狱大模型、AI 绘图、视频生成和 Agent 都装进本地电脑
  10-31](https://blog.upx8.com/LocModel-AI-Agent)
* [workbuddy一键完成所有任务（多账户）
  10-31](https://blog.upx8.com/workbuddy)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [简介](#简介)
* [可用的公共实例](#可用的公共实例)
  + [怎么用](#怎么用)
* [使用技巧与注意事项](#使用技巧与注意事项)
* [自建 RSSHub 教程](#自建-rsshub-教程)
  + [前提](#前提)
  + [方式一:一行命令](#方式一一行命令)
  + [方式二:Docker Compose(推荐)](#方式二docker-compose推荐)
  + [常用环境变量](#常用环境变量)
  + [对外访问:域名与反向代理](#对外访问域名与反向代理)
  + [其他部署方式](#其他部署方式)
  + [公开前的安全检查](#公开前的安全检查)
* [备忘清单与参考](#备忘清单与参考)
  + [常见问题](#常见问题)
  + [备忘](#备忘)
  + [参考链接](#参考链接)

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
2008](https://blog.upx8.com/Free)
[安全
375](https://blog.upx8.com/os_security)
[开发
536](https://blog.upx8.com/code)
[资讯
2124](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)