---
title: Linux下安装Go环境
url: https://blog.upx8.com/3178
source: 黑海洋 - WIKI
date: 2023-01-15
fetch_date: 2025-10-04T03:56:52.132904
---

# Linux下安装Go环境

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux下安装Go环境

发布时间:
2023-01-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
13038

# 安装Go环境

> Golang官网下载地址：[https://go.dev/doc/install](https://blog.upx8.com/go/aHR0cHM6Ly9nby5kZXYvZG9jL2luc3RhbGw)

1. 打开官网下载地址选择对应的系统版本, 复制下载链接
   这里我选择的是
   go1.19.5.linux-amd64：[https://dl.google.com/go/go1.19.5.linux-amd64.tar.gz](https://blog.upx8.com/go/aHR0cHM6Ly9kbC5nb29nbGUuY29tL2dvL2dvMS4xOS41LmxpbnV4LWFtZDY0LnRhci5neg)

2. `cd`进入你用来存放安装包的目录。嫌麻烦就直接输入`cd ~`。
   然后执行

```
wget https://dl.google.com/go/go1.19.5.linux-amd64
```

3. 下载完成

4. 执行`tar`解压到`/usr/loacl`目录下，得到`go`文件夹

```
tar -C /usr/local -zxvf  go1.19.5.linux-amd64
```

5. 添加`/usr/loacl/go/bin`目录到PATH变量中。添加到`/etc/profile` 或`$HOME/.profile`都可以

```
// 习惯用vim，没有的话可以用命令`sudo apt-get install vim`安装一个
vim /etc/profile
// 在最后一行添加
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
// wq保存退出后source一下
source /etc/profile
```

6. 执行`go version`，如果现实版本号，则Go环境安装成功。

[取消回复](https://blog.upx8.com/3178#respond-post-3178)

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