---
title: Bark 推送服务的部署和使用小技巧
url: https://blog.upx8.com/3194
source: 黑海洋 - WIKI
date: 2023-01-22
fetch_date: 2025-10-04T04:33:38.052650
---

# Bark 推送服务的部署和使用小技巧

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Bark 推送服务的部署和使用小技巧

发布时间:
2023-01-21

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
35080

## 前言

Bark 是一款 iOS 端的推送服务，通过部署一个 Server 服务端，可以通过浏览器，脚本，以及各种程序里来给 iOS 设备发送推送通知。

这个项目其实已经出来有好几年了，只是最近在优化一些运维管理项目时才接触和使用，在使用了几个月后还是打算分享下部分小技巧。

Finb/bark-server

中文文档

---

## 推送流程简单说明

首先需要一个服务端，本文会介绍如何部署。然后 iOS 设备在 App Store 安装`Bark`，获取到该设备的唯一`key`，通过浏览器、curl 命令或者在各种 shell python 脚本里来配置推送内容。触发后，服务端接受到推送，会请求苹果的`APNs`向你的 iOS 设备发送推送通知。

### 免费的推送服务器

### [https://bark.ioiox.com](https://blog.upx8.com/go/aHR0cHM6Ly9iYXJrLmlvaW94LmNvbS8)

需要注意的是：所有`key`和`内容`都会记录到服务器日志中，**请不要**使用免费服务器来推送`机密或私有信息`，**也请不要滥用**。你可以继续参照下文部署自己的服务端。

## Bark Server

使用 docker 来部署非常简单，官方镜像支持 X86 和 ARM 架构。

### docker

```
docker run -dt --name bark -p 8080:8080 -v `pwd`/bark-data:/data finab/bark-server
```

根据情况自行修改端口映射和数据目录的挂载。

### docker compose

```
version: '3.8'
services:
  bark-server:
    image: finab/bark-server
    container_name: bark-server
    restart: always
    volumes:
      - ./data:/data
    ports:
      - "8080:8080"
```

### 配置域名 （可选）

部署完毕后`http://IP:8080`就是 bark 的后端服务地址，可以直接使用，也可以参考以下 nginx conf 来配置域名和 HTTPS。

注意修改域名，证书路径和端口。

**展开查看 nginx conf 配置**

## 常规使用

### 客户端

iOS 设备直接在 App Store 下载`bark`，打开后添加 bark 后端服务器地址。`（实际上不添加也不影响使用，只是添加服务器端可以方便的在 app 里查看到各种推送地址方便复制使用。）`同时也会看到本设备的一串`key`，请不要随意泄露此`key`，以免被别人滥用推送垃圾通知，如果泄露也可以通过删除 app 重新安装来更新。

### bark 的常规命令

其实 app 内和官方文档已经很好的介绍了如何使用，最简单的例子如下：
**浏览器中打开**

```
https://bark.ioiox.com/your_key/标题/内容
```

**curl命令（可以用于 shell python 脚本中）**

```
curl https://bark.ioiox.com/your_key/标题/内容
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/3541866296.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/3541866296.jpg)
还可以配置分组，分组的意思是在 iOS 端里的历史记录中可以根据分组来查看各种通知。

```
https://bark.ioiox.com/your_key/标题/内容?group=IOIOX
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/4181517948.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/4181517948.jpg)
[![](https://static.ioiox.cn/usr/uploads/2022/01/2912878674.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/2912878674.jpg)

更多关于自定义 icon、铃声、自动复制、自动保存、时效性、角标等等功能可以直接查看 iOS 端说明。

## 高级用法

常规在浏览器或者命令行推送对文字的空格，换行都是需要进行 url-encoder 才能识别，以下是一些我在使用中用到过的示例，大家可以直接拿去使用。

### 换行

换行符为`%0a`，**注意标题是不支持换行的**。

```
https://bark.ioiox.com/your_key/标题/内容%0a换行
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/3291541008.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/3291541008.jpg)

```
https://bark.ioiox.com/your_key/网站服务通知/网站：www.ioiox.com%0a状态：运行正常
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/2465375414.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/2465375414.jpg)

### 空格

空格符为`%20`,**标题也是可以使用空格符**。
如果是在浏览器里发送推送，可以直接在内容里使用空格，浏览器会自动转换。

```
https://bark.ioiox.com/your_key/标题/内容 空格
```

如果在命令行里则需要使用空格符

```
https://bark.ioiox.com/your_key/标题/内容%20空格
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/860638737.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/860638737.jpg)

### 其他需要转译的字符

例如`/`符号也是需要进行 url-encoder 获得`%2F`。

```
https://bark.ioiox.com/your_key/GitHub/stilleshan%2Fdockerfiles
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/3973868738.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/3973868738.jpg)
配合换行和空格

```
https://bark.ioiox.com/your_key/GitHub%20Action/仓库:%20stilleshan%2Fdockerfiles%0a状态:%20Workflow%20工作流成功
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/1189412269.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/1189412269.jpg)

### icon 和 group 等多个叠加

正常情况下 icon 配置，icon 图标会缓存到 iOS 设备中。

```
https://bark.ioiox.com/your_key/标题/内容?icon=https://www.ioiox.com/avatar.jpg
```

如果同时还需要配置 group 等，则需要使用`&`来拼接。

```
https://bark.ioiox.com/your_key/标题/内容?icon=https://www.ioiox.com/avatar.jpg&group=IOIOX
```

[![](https://static.ioiox.cn/usr/uploads/2022/01/3284575737.jpg)](https://static.ioiox.cn/usr/uploads/2022/01/3284575737.jpg)

**基本上以上一些小技巧应该能完全满足大部分的需求了。当然 bark 还支持 Jason 格式的请求，相信会 Jason 的程序员们应该不需要我来教了，直接查看文档即可。**

[取消回复](https://blog.upx8.com/3194#respond-post-3194)

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