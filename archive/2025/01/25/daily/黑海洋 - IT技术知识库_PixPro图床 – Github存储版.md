---
title: PixPro图床 – Github存储版
url: https://blog.upx8.com/4678
source: 黑海洋 - IT技术知识库
date: 2025-01-25
fetch_date: 2025-10-06T20:10:36.205775
---

# PixPro图床 – Github存储版

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# PixPro图床 – Github存储版

发布时间:
2025-01-24

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
81989

一款专为个人需求设计的高效图床解决方案，集成了强大的图片压缩功能与优雅的前台后台管理界面。

项目结构精简高效，提供自定义图片压缩率与尺寸设置，有效降低存储与带宽成本。

支持本地储存，阿里云OSS储存，S3存储。可通过把储存桶挂载到本地的方式解锁更多储存方式。

简洁美观的前端，支持点击、拖拽、粘贴、URL、批量上传。

瀑布流管理后台，便捷查看图片信息，支持图片灯箱、AJAX无加载刷新。

## 演示站点

前端：[https://dev.ruom.top/](https://blog.upx8.com/go/aHR0cHM6Ly9kZXYucnVvbS50b3Av)

后台：[https://dev.ruom.top/admin/](https://blog.upx8.com/go/aHR0cHM6Ly9kZXYucnVvbS50b3AvYWRtaW4v)

项目地址：[https://github.com/JLinMr/PixPro/](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0pMaW5Nci9QaXhQcm8v)

演示站点更新较快，可能跟实际效果不太一样

## 安装教程

首先下载源码ZIP，将文件上传到网站根目录，访问网址 ，填写相关信息，即可完成安装。

## 运行环境

推荐PHP 8.1 + MySQL >= 5.6

本程序依赖PHP的 Fileinfo 、 Imagick 、 exif拓展，需要自行安装。依赖 pcntl 扩展（宝塔PHP默认已安装）

要求 pcntl\_signal 和 pcntl\_alarm 函数可用（需主动解除禁用）

## 资源加速

项目已经上传到NPM，所有静态资源均可以使用

### 使用npmmirror，@version需要改为版本号

[https://cdn.npmmirror.com/packages/pixpro/@version/files/](https://blog.upx8.com/go/aHR0cHM6Ly9jZG4ubnBtbWlycm9yLmNvbS9wYWNrYWdlcy9waXhwcm8vQHZlcnNpb24vZmlsZXMv)

例如: [https://cdn.npmmirror.com/packages/pixpro/1.7.6/files/static/js/admin.js](https://blog.upx8.com/go/aHR0cHM6Ly9jZG4ubnBtbWlycm9yLmNvbS9wYWNrYWdlcy9waXhwcm8vMS43LjYvZmlsZXMvc3RhdGljL2pzL2FkbWluLmpz)

### 使用 jsdelivr

[https://cdn.jsdelivr.net/npm/pixpro@latest/](https://blog.upx8.com/go/aHR0cHM6Ly9jZG4uanNkZWxpdnIubmV0L25wbS9waXhwcm9AbGF0ZXN0Lw)

例如: [https://cdn.jsdelivr.net/npm/pixpro@1.7.6/static/js/admin.js](https://blog.upx8.com/go/aHR0cHM6Ly9jZG4uanNkZWxpdnIubmV0L25wbS9waXhwcm9AMS43LjYvc3RhdGljL2pzL2FkbWluLmpz)

## 拓展功能

本程序支持 Upgit 对接在Typora使用，对接方法如下

### 下载upgit

前往下载 [Upgit](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaWxhbnpvdS5jb20vcy9ka2MwWVhySQ)

### 如何配置

修改目录下`config.toml`文件，内容如下

```
default_uploader = "PixPro"

[uploaders.PixPro]
request_url = "https://xxx.xxx.xxx/api.php"
token = "这里内容替换为你的Token"
```

### 接入 Typora

转到 Image 选自定义命令作为图像上传器，在命令文本框中输入 Upgit 程序位置，然后就可以使用了

![](https://i1.wp.com/dev.ruom.top/i/2025/01/24/931560.webp)

1. ![COS](//q2.qlogo.cn/headimg_dl?dst_uin=777788&spec=100)

   **COS**

   2025-01-28 12:58:47

   [回复](https://blog.upx8.com/4678/comment-page-1?replyTo=30484#respond-post-4678)

   新年快乐！

[取消回复](https://blog.upx8.com/4678#respond-post-4678)

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