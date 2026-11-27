---
title: 绿联 NAS Docker 部署 Remotion
url: https://www.uedbox.com/post/120209/
source: 体验盒子
date: 2026-11-26
fetch_date: 2026-11-27T10:16:35.870011
---

# 绿联 NAS Docker 部署 Remotion

[跳到正文](#content)

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2026/assets/images/logo-ub2026.svg)](https://www.uedbox.com/)

[ ]

* [项目](https://www.uedbox.com/work/)
* [服务](https://www.uedbox.com/services/)
* [文章](https://www.uedbox.com/blog/)
* [开始合作](https://www.uedbox.com/start/)
* [关于](https://www.uedbox.com/about/)
* [更多](###)
  + [分享](https://www.uedbox.com/share/)
  + [AI导航](https://www.uedbox.com/aihub/)
  + [老电影](https://www.uedbox.com/movie/)
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/)
  + [Exploits](https://www.uedbox.com/exploits/)
  + [SecTools](https://www.uedbox.com/tools/)
  + [UserAgent解析](https://www.uedbox.com/useragentparser/)
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/)
  + [存档](https://www.uedbox.com/archives/)

搜索  搜索

[首页](https://www.uedbox.com/)/[产品](https://www.uedbox.com/ai/product/)/绿联 NAS Docker 部署 Remotion

发布 2026-11-26 文章 [产品](https://www.uedbox.com/ai/product/)

# 绿联 NAS Docker 部署 Remotion

 推荐

[人手必备的 AI 编辑器，Cursor 专属半价注册入口[点击领取 5折 专属优惠注册]](https://cursor.com/referral?code=YRIIY4MGHGOP)

Remotion 是一个用 React 写代码生成视频的框架。把它丢进 NAS 的 Docker 里跑，既能实现网页端随时预览、渲染导出视频不占主力电脑性能，也方便后续接定时任务做自动化视频生成。

这里以 **绿联（x86 架构）** 为例，分享一套零交互、一步到位的 Docker Compose 部署方案，顺便把实操中容易踩的几个深坑一次性填平。

目录表

Toggle

* [一、 硬件与环境准备](#%E4%B8%80%E3%80%81_%E7%A1%AC%E4%BB%B6%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87)
* [二、 Docker Compose 一键部署](#%E4%BA%8C%E3%80%81_Docker_Compose_%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2)
* [三、 必看避坑：局域网访问报 crypto.randomUUID 错误](#%E4%B8%89%E3%80%81_%E5%BF%85%E7%9C%8B%E9%81%BF%E5%9D%91%EF%BC%9A%E5%B1%80%E5%9F%9F%E7%BD%91%E8%AE%BF%E9%97%AE%E6%8A%A5_cryptorandomUUID_%E9%94%99%E8%AF%AF)
* [四、 日常使用与性能调优](#%E5%9B%9B%E3%80%81_%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E4%B8%8E%E6%80%A7%E8%83%BD%E8%B0%83%E4%BC%98)

## 一、 硬件与环境准备

* **架构要求**：建议 Intel/AMD 处理器的 x86\_64 机型（如 DXP4800 Plus）。ARM 架构入门机型的无头浏览器依赖兼容性较差，不建议折腾。
* **内存建议**：至少 4GB 可用内存，推荐 8GB 及以上。底层需要跑无头 Chrome 逐帧渲染，内存太小容易触发 OOM 崩溃。
* **建好目录**：打开绿联云「文件管理」，在
  `/docker`
  共享文件夹下新建
  `remotion`
  目录，里面再建一个空的
  `app`
  文件夹（最终路径：
  `/docker/remotion/app`
  ）。

## 二、 Docker Compose 一键部署

Remotion 官方脚手架是交互式的，直接塞进 Docker 后台会卡死退出；精简版 Node 镜像又缺少 Chrome 运行所需的图形与音频系统库。

下面这份
`compose.yaml`
已经把 **Linux 浏览器依赖安装、标准 TypeScript 工程初始化（
`index.ts`
+
`Root.tsx`
+
`remotion.config.ts`
）以及标记文件判断**全写进去了。首次启动会自动安装环境，后续重启容器直接秒开。

1. 打开绿联 Docker 应用 -> **项目** -> **创建**。
2. 项目名称填
   `remotion`
   ，路径选
   `/docker/remotion`
   。
3. 粘贴以下配置并点击 **立即部署**：

yaml

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 | services:  remotion:  image: node:20-bookworm  container\_name: remotion-studio  working\_dir: /app  # 必须分配至少 1GB-2GB 共享内存，否则内部 Chrome 渲染必崩  shm\_size: '2gb'  restart: unless-stopped  ports:  - "3000:3000"  volumes:  - ./app:/app  environment:  - NODE\_ENV=development  command:  - bash  - -c  - |  if [ ! -f /var/tmp/.chrome-deps-installed ]; then  apt-get update && apt-get install -y --no-install-recommends libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2 libpango-1.0-0 libcairo2 && touch /var/tmp/.chrome-deps-installed  fi  if [ ! -f /app/src/Root.tsx ]; then  mkdir -p /app/src  echo "eyJuYW1lIjoicmVtb3Rpb24tbmFzIiwidmVyc2lvbiI6IjEuMC4wIiwic2NyaXB0cyI6eyJkZXYiOiJyZW1vdGlvbiBzdHVkaW8iLCJidWlsZCI6InJlbW90aW9uIGJ1bmRsZSJ9LCJkZXBlbmRlbmNpZXMiOnsiQHJlbW90aW9uL2NsaSI6ImxhdGVzdCIsInJlYWN0IjoiXjE4LjMuMSIsInJlYWN0LWRvbSI6Il4xOC4zLjEiLCJyZW1vdGlvbiI6ImxhdGVzdCJ9LCJkZXZEZXBlbmRlbmNpZXMiOnsiQHR5cGVzL3JlYWN0IjoiXjE4LjMuMTIiLCJ0eXBlc2NyaXB0IjoiXjUuNi4zIn19" | base64 -d > /app/package.json  echo "eyJjb21waWxlck9wdGlvbnMiOnsidGFyZ2V0IjoiRVMyMDE4IiwibW9kdWxlIjoiY29tbW9uanMiLCJqc3giOiJyZWFjdC1qc3giLCJzdHJpY3QiOnRydWUsImVzTW9kdWxlSW50ZXJvcCI6dHJ1ZSwic2tpcExpYkNoZWNrIjp0cnVlLCJmb3JjZUNvbnNpc3RlbnRDYXNpbmdJbklmaWxlTmFtZXMiOnRydWUsIm5vRW1pdCI6dHJ1ZSwibW9kdWxlUmVzb2x1dGlvbiI6Im5vZGUifSwiaW5jbHVkZSI6WyJzcmMiXX0=" | base64 -d > /app/tsconfig.json  echo "aW1wb3J0IHsgQ29uZmlnIH0gZnJvbSAnQHJlbW90aW9uL2NsaS9jb25maWcnOwoKQ29uZmlnLnNldEVudHJ5UG9pbnQoJy4vc3JjL2luZGV4LnRzJyk7CkNvbmZpZy5zZXRWaWRlb0ltYWdlRm9ybWF0KCdqcGVnJyk7CkNvbmZpZy5zZXRPdmVyd3JpdGVPdXRwdXQodHJ1ZSk7Cg==" | base64 -d > /app/remotion.config.ts  echo "aW1wb3J0IHsgcmVnaXN0ZXJSb290IH0gZnJvbSAncmVtb3Rpb24nOwppbXBvcnQgeyBSZW1vdGlvblJvb3QgfSBmcm9tICcuL1Jvb3QnOwoKcmVnaXN0ZXJSb290KFJlbW90aW9uUm9vdCk7Cg==" | base64 -d > /app/src/index.ts  echo "aW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JzsKaW1wb3J0IHsgQ29tcG9zaXRpb24gfSBmcm9tICdyZW1vdGlvbic7CgpleHBvcnQgY29uc3QgSGVsbG9Xb3JsZDogUmVhY3QuRkMgPSAoKSA9PiB7CiAgcmV0dXJuICgKICAgIDxkaXYgc3R5bGU9e3sgZmxleDogMSwgYmFja2dyb3VuZENvbG9yOiAnIzExMScsIGNvbG9yOiAnd2hpdGUnLCBkaXNwbGF5OiAnZmxleCcsIGp1c3RpZnlDb250ZW50OiAnY2VudGVyJywgYWxpZ25JdGVtczogJ2NlbnRlcicsIGZvbnRTaXplOiA2MCB9fT4KICAgICAgSGVsbG8gVUdSRUVOIE5BUyEKICAgIDwvZGl2PgogICk7Cn07CgpleHBvcnQgY29uc3QgUmVtb3Rpb25Sb290OiBSZWFjdC5GQyA9ICgpID0+IHsKICByZXR1cm4gKAogICAgPD4KICAgICAgPENvbXBvc2l0aW9uCiAgICAgICAgaWQ9IkhlbGxvV29ybGQiCiAgICAgICAgY29tcG9uZW50PXtIZWxsb1dvcmxkfQogICAgICAgIGR1cmF0aW9uSW5GcmFtZXM9ezE1MH0KICAgICAgICBmcHM9ezMwfQogICAgICAgIHdpZHRoPXsxOTIwfQogICAgICAgIGhlaWdodD17MTA4MH0KICAgICAgLz4KICAgIDwvPgogICk7Cn07Cg==" | base64 -d > /app/src/Root.tsx  npm install  fi  npx remotion studio --host 0.0.0.0 |

请谨慎使用此类代码。

> **提示**：首次部署会下载依赖并安装
> `npm`
> 包，打开容器日志耐心等 1~2 分钟，看到
> `Server ready - Local: http://localhost:3000`
> 即表示就绪。完整环境大约占用 800MB~1.2GB 硬盘空间；不渲染时待机内存仅占 150MB 左右，CPU 占用基本为 0。

## 三、 必看避坑：局域网访问报 `crypto.randomUUID` 错误

直接用电脑浏览器访问
`http://NAS_IP:3000`
时，点击界面上的添加组件库或部分操作会弹窗报错：
`TypeError: crypto.randomUUID is not a function`
。

* **原因**：现代浏览器出于安全策略，在非 HTTPS 的局域网 HTTP 环境下禁用了原生的
  `crypto.randomUUID`
  接口。
* **解决办法（二选一）**：

## 四、 日常使用与性能调优

* **代码编辑与导出**：通过电脑 SMB 挂载绿联的
  `/docker/remotion/app`
  目录，直接用本地 VS Code 修改
  `src/`
  里的代码，网页端会实时热更新。点击网页右下角 **Render** 导出的 MP4 文件，会自动存放在
  `/docker/remotion/app/out`
  目录下。
* **防止内存爆满**：如果是原厂 8GB 内存的机型，在网页端点击渲染导出时，建议把高级设置里的 **Concurrency（并发数）** 手动调低为
  `2`
  或
  `3`
  。默认全核并发拉满会导致无头浏览器多开，容易吃光内存。
* **彻底清理**：以后如果不想用了，在 Docker 里删掉项目和镜像，再把硬盘上的
  `/docker/remotion`
  文件夹删掉即可，不会在系统里留垃圾。

如果需要补充**中文字体安装参数**（防止渲染中文标题变成方块）或**定时自动渲染脚本**，随时告诉我。

[Remotion](https://www.uedbox.com/post/tag/remotion/)

原文链接：[绿联 NAS Docker 部署 Remotion](https://www.uedbox.com/post/120209/)

转载需保留署名与原文链接，未授权不得使用。

点赞0分享本文打赏支持

×

### 分享本文

扫码或复制链接，快速分享当前页面。

![扫码分享]()二维码按当前页面实时生成，弹窗打开时应可直接扫码。

复制链接系统分享

更多渠道见[分享页](https://www.uedbox.com/share/)。

×

### 打赏支持

可通过支付宝或微信打赏，支持内容持续维护。

#### 支付宝打赏

![支付宝打赏二维码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/alipay.png)

#### 微信打赏

![微信打赏二维码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/wx_pay.png)

[联系服务](https://www.uedbox.com/start/)邮件联系

合作沟通请附目标、周期与预算范围。

[上一篇**Capso：我重新审视了一遍 macOS 截图工具**](https://www.uedbox.com/post/120099/)

## 精选置顶

[![2026 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/wp-content/uploads/2024/01/Torrent-Search-Engine.jpg)](https://www.uedbox.com/post/54994/)

2019-05-12 更新 2026-05-28

### [2026 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/post/54994/)

bt磁力搜索引擎，最新更新，安全优质 BT 种子和磁力链接下载是现在下载资源的主要方式，由于版权等各种原因，磁力搜索引擎时常被和谐掉...

[周边](https://www.uedbox.com/web-security/safety/) [BT磁力搜索引擎](https://www.uedbox.com/post/tag/bt%E7%A3%81%E5%8A%9B%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E/) [BT种子](https://www.uedbox.com/post/tag/bt%E7%A7%8D%E5%AD%90/)

[![用uBlock Origin过滤广告，享受最好的广告拦截体验](https://www.uedbox.com/wp-content/uploads/2019/05/uBlock_Origin-250x250.png)](https://www.uedbox.com/post/55544/)

2019-05-24 更新 2025-11-20

### [用uBlock Origin过滤广告，享受最好的广告拦截体验](https://www.uedbox.com/post/55544/)

疯了！我要过滤广告 这是一篇自黑文。现在几乎95%以上的网站都放有广告，更甚的是那些大网站大平台，一个页面有本事放几十个广告脚本，...

[周边](https://www.uedbox.com/web-security/safety/) [uBlock Origin](https://www.uedbox.com/post/tag/ublock-origin/) [广告拦截](https://www.uedbox.com/post/tag/%E5%B9%BF%E5%91%8A%E6%8B%A6%E6%88%AA/)

[![手机BT/种子下载，手机磁力链下载软件整理](https://www.uedbox.com/wp-content/uploads/2019/06/gopeed-250x250....