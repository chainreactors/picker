---
title: Postman 汉化教程，手把手教你如何设置中文
url: https://blog.upx8.com/3170
source: 黑海洋 - WIKI
date: 2023-01-11
fetch_date: 2025-10-04T03:32:24.053101
---

# Postman 汉化教程，手把手教你如何设置中文

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Postman 汉化教程，手把手教你如何设置中文

发布时间:
2023-01-10

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
26223

前天有个小伙伴问我 Postman 如何进行中文汉化，说英文看着着实不习惯。其实，Postman 本身并不支持中文，那要怎么汉化呢？

这里分享一个 GitHub 上大佬分享的 Postman 汉化补丁包，亲测还是挺好用的，只需要复制到指定目录下进行解压，即可将 Postman 设置成中文，下面是我汉化成功的截图：

## Postman 简介

Postman 是一款非常流行的 API 调试工具，可以说是测试工程师、后端开发人员，基本上是人手必备。

## 下载&安装 Postman

> 注意：想要汉化 Postman， 就**必须导入汉化补丁包，且补丁包的版本号需与 Postman 版本号一致才行**，否则大概率无法汉化。所以，**需先确认汉化补丁包的版本号，再下载对应版本的 Postman 使用**。

小哈写这篇文章的时候，补丁包的最新版本号为 `9.12.2`：下载 Postman 汉化补丁包

**汉化补丁下载链接：[https://github.com/hlmd/Postman-cn/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hsbWQvUG9zdG1hbi1jbi9yZWxlYXNlcw)**

确认了补丁包版本号后，再下载对应版本的 Postman :

| Postman 历史版本下载 | 请把下面链接的"版本号"替换为指定的版本号, 然后浏览器中访问即可直接下载 |
| --- | --- |
| Windows64位 | https://dl.pstmn.io/download/version/版本号/win64 |
| Windows32位 | https://dl.pstmn.io/download/version/版本号/win32 |
| Mac Intel Chip | https://dl.pstmn.io/download/version/版本号/osx\_64 |
| Mac Apple Chip | https://dl.pstmn.io/download/version/版本号/osx\_arm64 |
| Linux | https://dl.pstmn.io/download/version/版本号/linux |

比如补丁版本号为 `9.12.2`, 如果想要下载 Windows 64 位的 Postman，则下载链接为 **[https://dl.pstmn.io/download/version/9.12.2/win64](https://blog.upx8.com/go/aHR0cHM6Ly9kbC5wc3Rtbi5pby9kb3dubG9hZC92ZXJzaW9uLzkuMTIuMi93aW42NA "https://dl.pstmn.io/download/version/9.12.2/win64")**，浏览器访问该地址，则可直接下载：

![](https://img.quanxiaoha.com/quanxiaoha/166910692124840)

下载成功后，双击安装即可。

## 开始汉化 Postman

安装成功后，我们开始汉化 Postman:

### Windows 系统

1、下载好对应版本的汉化补丁包 `app.zip`;

2、进入到 Postman 安装目录下的 `/resources` 文件夹中：

> 桌面找到 Postman 应用程序右键 -> 打开文件所在位置，再进入 `app-*.*.*/resources` 目录下， 默认安装地址：`C:/Users/用户名/AppData/Local/Postman`， 示例：`C:/Users/用户名/AppData/Local/Postman/app-8.8.0/resources`

3、**复制 `app.zip` 到 `resources` 目录**，将`app.zip`**解压到当前文件夹**会生成一个`app`目录，如上图所示；

4、**重启 Postman** 即可看到已经汉化成功~

### Mac 系统

1、下载对应版本的 `app.zip`;

2、**解压** `app.zip`；

3、进入 `访达/应用程序/Postman.app/Contents/Resources/`:

> 进入`访达/应用程序`找到`Postman.app`右键查看包内容，再进入`Contents/Resources`

4、替换 `app` 文件夹

> 如果目录下没有 `app` 文件夹，那么直接解压 `app.zip` 得到 `app` 文件夹即可 将`app.zip`解压出来的`app`文件夹复制到`Resources`目录，替换原本的`app`文件夹 可以先删除或重命名原本的`app`文件夹

5、重启 Postman 就可以了~

### Linux 系统

1、下载对应版本的 `app.zip`:

```
# 下方为Github地址 将版本号替换为对应版本号，例如：8.8.0
wget https://github.com/hlmd/Postman-cn/releases/download/版本号/app.zip
```

2、**解压&&替换`app`文件夹**：

```
# Postman安装地址 自行替换
unzip -o -d Postman安装地址/app/resources app.zip
```

## 禁掉 Postman 自动更新

由于汉化补丁包版本号需要与 Postman 版本号对应的关系，如果更新了 Postman 会导致汉化失效，那么，如何禁掉 Postman 自动更新呢？

### Windows

Windows 删除安装目录的 update.exe 即可。

### Mac / Linux

将此解析加入你电脑的主机文件 hosts ：

```
0.0.0.0         dl.pstmn.io
```

> 注意：这是一项危险操作，将会使你的电脑无法与 Postman 下载服务器连接，当然这就可以使你的 Postman 应用程序不再更新, 如果想更新请将此解析注释或移除。

### hosts 文件在哪里？

Windows：`C:/Windows/System32/drivers/etc/hosts`

Linux & Mac：`/etc/hosts`

[取消回复](https://blog.upx8.com/3170#respond-post-3170)

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