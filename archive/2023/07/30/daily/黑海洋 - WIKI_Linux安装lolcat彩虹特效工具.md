---
title: Linux安装lolcat彩虹特效工具
url: https://blog.upx8.com/3724
source: 黑海洋 - WIKI
date: 2023-07-30
fetch_date: 2025-10-04T11:53:20.735970
---

# Linux安装lolcat彩虹特效工具

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux安装lolcat彩虹特效工具

发布时间:
2023-07-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
12285

#### 什么是lolcat？

Lolcat是用于Linux，BSD和OSX的实用程序，其连接方式类似于cat命令，并为其添加了彩虹颜色。Lolcat主要为Linux终端中的文本添加彩虹般的颜色。

#### 在Linux中安装Lolcat

由于 Lolcat 是一个 ruby gem 程序，所以在你的系统中必须安装有最新版本的 ruby。

`apt-get install ruby`    [在基于 APT 的系统中]
`yum install ruby`          [在基于 Yum 的系统中]
`dnf install ruby`          [在基于 DNF 的系统中]

接下来，使用以下命令从git存储库下载并安装最新版本的lolcat。

`wget https://github.com/busyloop/lolcat/archive/master.zip`

`unzip master.zip`

`cd lolcat-master/bin`

`gem install lolcat`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-49-50.png)

安装lolcat后，使用以下命令检查lolcat版本。

`lolcat -v`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-48-07.png)

#### Lolcat帮助文档

`lolcat -h`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-51-36.png)

**给文本赋予彩虹颜色的动画:**

`echo Hello World 2022 | lolcat -a -d 200`

![](https://loukas.cn/wp-content/uploads/2022/02/dklw6-qlulc.gif)

这里选项 -a 指的是 Animation(动画)， -d 指的是 duration(持续时间)。在上面的例子中，持续 200 次动画。

**配合neofetch使用:**

`apt-get install neofetch`

`neofetch | lolcat`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_21-09-46.png)

[取消回复](https://blog.upx8.com/3724#respond-post-3724)

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