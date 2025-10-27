---
title: Immich – 开源自托管的手机照片备份工具[iPhone/Android]
url: https://buaq.net/go-150962.html
source: unSafe.sh - 不安全
date: 2023-02-26
fetch_date: 2025-10-04T08:08:16.911347
---

# Immich – 开源自托管的手机照片备份工具[iPhone/Android]

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/13f6e0875fd2ead974aa0d6ce5ea7b4b.jpg)

Immich – 开源自托管的手机照片备份工具[iPhone/Android]

Immich 是一个直接从 iPhone、Android 手机上备
*2023-2-25 15:2:0
Author: [www.appinn.com(查看原文)](/jump-150962.htm)
阅读量:80
收藏*

---

**Immich** 是一个直接从 iPhone、Android 手机上备份照片与视频的开源解决方案，通过部署在自己的电脑、NAS、服务器中，使用 App 进行备份。界面酷似 Google Photos，支持多用户、照片和相册分享、好友上传、地理位置、机器学习识别事件等功能。是居家备份照片的好帮手。[@Appinn](https://www.appinn.com/immich/)

![Immich - 开源自托管的手机照片备份工具[iPhone/Android]](https://static1.appinn.com/images/202302/immich.jpg!o "Immich - 开源自托管的手机照片备份工具[iPhone/Android] 1")

前不久，推荐了一款适合普通电脑使用的照片备份工具 **PhotoSync**：

> **PhotoSync** 是一款通过 Wi-Fi 快速、安全地移动、备份、共享照片与视频的工具，支持 iPhone、Android，可以将照片备份至 NAS、电脑、FTP、网盘等处。
>
> [https://www.appinnn.com/photosync/](https://www.appinn.com/photosync/)

而 Immich，则适合拥有自己服务器的同学，首选 Ubuntu、Debian、MacOS 系统，也可以在 Windows 的 Docker Desktop 下工作。

## Immich 手机照片/视频备份

Immich 的服务器端基于 Web，拥有自己的 iPhone、Android 应用，只需要在移动应用中填入服务器段的 API 地址，即可使用，两者功能有少许不同：

| 特征 | 移动应用 | 网页 |
| --- | --- | --- |
| 上传和查看视频和照片 | ✅ | ✅ |
| 打开应用程序时自动备份 | ✅ | ❌ |
| 用于备份的选择性相册 | ✅ | ❌ |
| 将照片和视频下载到本地设备 | ✅ | ✅ |
| 多用户支持 | ✅ | ✅ |
| 相册和共享相簿 | ✅ | ✅ |
| 可擦洗/可拖动的滚动条 | ✅ | ✅ |
| 支持RAW（HEIC，HEIF，DNG，APPLE ProRaw） | ✅ | ✅ |
| 元数据视图（EXIF、地图） | ✅ | ✅ |
| 按元数据、对象和图像标签搜索 | ✅ | ❌ |
| 管理功能（用户管理） | ❌ | ✅ |
| 后台备份 | ✅ | ❌ |
| 虚拟滚动 | ✅ | ✅ |
| OAuth 支持 | ✅ | ✅ |
| 实时照片备份和播放 | iOS | ✅ |
| 用户自定义存储结构 | ✅ | ✅ |
| 公开分享 | ❌ | ✅ |

## 备份功能

配置好服务器端，登录移动应用之后，给于相册权限，就可以备份了，支持前台备份与后台备份，使用起来非常简单，有中文界面

![Immich - 开源自托管的手机照片备份工具[iPhone/Android] 1](https://static1.appinn.com/images/202302/img_29a927d93d25-1.jpg!o "Immich - 开源自托管的手机照片备份工具[iPhone/Android] 2")

## 分享与上传

分享与上传就很赞了，你可以通过 Immich 将某个相册分享给好友，可以设置很多权限，包括：

* 设置描述文字
* 显示元数据（EXIF）
* 允许下载
* 允许上传
* 过期时间

![Immich - 开源自托管的手机照片备份工具[iPhone/Android] 2](https://static1.appinn.com/images/202302/screen-appinn2023-02-25-14-49-30.jpg!o "Immich - 开源自托管的手机照片备份工具[iPhone/Android] 3")

其中允许上传功能，可以让好友直接通过浏览器上传手机里的照片，在与好友一起出门游玩回来之后，共享照片真是太方便了。

## 安装 Immich

基于 Docker，安装 Immich 也很容易，先修改配置文件 .env：

```
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```

实际上，只需要修改里面的 *UPLOAD\_LOCATION* 部分，使用绝对路径，这是保存照片的路径。

其它设置保持默认，然后就可以安装了：

```
wget https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
docker-compose up -d
```

最后，在浏览器打开：`IP:2283` 就可以创建用户进入 Immich 了。

## 手机 App

Immich 可以通过命令行进行[批量上传](https://immich.app/docs/features/bulk-upload)，也有官方 App：

* [Google Play Store](https://play.google.com/store/apps/details?id=app.alextran.immich)
* [Apple App Store](https://apps.apple.com/us/app/immich/id1613945652)
* [F-Droid](https://f-droid.org/packages/app.alextran.immich)
* [GitHub Releases (apk)](https://github.com/immich-app/immich/releases)

在登录的时候，服务器地址填入：`IP:2283/api` 即可。

## DEMO / 示例

有一个官方 DEMO 可以测试：

* <https://demo.immich.app/auth/login>

公共场合，请谨慎上传图片啊，昨天的 [memos](https://www.appinn.com/memos/) DEMO 中，已经有同学干坏事了 😂

最后，[官网](https://immich.app/) / [GitHub](https://github.com/immich-app/immich)。

---

文章来源: https://www.appinn.com/immich/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)