---
title: Docker 管理面板：Fast Os Docker 简易安装教程
url: https://blog.upx8.com/3118
source: 黑海洋 - WIKI
date: 2022-11-29
fetch_date: 2025-10-03T23:59:31.096041
---

# Docker 管理面板：Fast Os Docker 简易安装教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Docker 应用：交叉编译 cloudreve，构建 window 二进制程序

发布时间:
2022-11-28

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18897

![](https://eller.top/storage/images/Hq4ELfR1Kg8EPs23S75EZW1ORYiwWSMXOVC9wXn2.png)

cloudreve 是一个使用 golang 语言编写的一款非常方便轻量的云盘程序，相比 nextcloud 轻便很多，只有一个主程序，你可以放在任何地方直接运行，部署起来极其容易。

最近在尝试使用 cloudreve 的过程中，遇到点小问题，想修改后重新编译。在 windows 10 上，总是无法完成编译，但在 linux 上编译 win 程序需要安装部署一些 GCC 交叉编译用到的工具链 `mingw-w64`，安装工具链在 centos 上又非常麻烦，也很容易失败。

在折腾一番后，最终借助 docker，实现一个微型的 Debian 系统，来完成编译任务，拿到最终可执行的 windows 程序。

# 安装 Docker

对于没有安装过 docker 的用户你可以参照 Docker 离线安装及基础操作使用教程 来完成 docker 的安装。

# 准备编译环境

## 获取 debian

首先我们拉取一份 debian 的 docker 镜像到本地

```
docker pull debian
```

运行 debian 容器，并通过 bash 进入容器中操作

```
docker run -it -v ~:/root debian
```

在容器中下载安装 golang：

```
apt install -y wget
wget https://golang.org/dl/go1.16.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.16.linux-amd64.tar.gz
```

配置环境变量，并使其生效：

```
cat >>~/.bashrc <<\EOF
export GOPATH=~/go
export PATH=$PATH:$GOPATH/bin:/usr/local/go/bin
EOF

source ~/.bashrc
```

此时你应该可以通过 `go version` 命令成功获取到 golang 的版本信息确认安装无误。

## 安装交叉编译工具链

接下来安装 mingw-w64 ，这在 debian 系统下非常容易：

```
apt install mingw-w64 -y
```

## Git

安装 Git

```
apt install -y git
```

获取一份最新的 cloudreve 源代码，并更新所有子模块：

```
git clone --recurse-submodules https://github.com/cloudreve/Cloudreve.git
```

## yarn

cloudreve 推荐使用 yarn 构建前端资源，先安装 yarn：

```
apt update && sudo apt install yarn
```

开始构建前端代码：

```
# 进入前端子模块
cd assets
# 安装依赖
yarn install
# 开始构建
yarn run build
```

最终，构建打包的前端静态资源文件位于 assets/build 目录下。

通过 statik工具将生成的前端资源文件，嵌入到 golang 程序中，最终发布在二进制的程序里：

```
# 回到项目主目录
cd ../

# 安装 statik, 用于嵌入静态资源
go get github.com/rakyll/statik

# 开始嵌入
statik -src=assets/build/  -include=*.html,*.js,*.json,*.css,*.png,*.svg,*.ico,*.ttf -f
```

## 编译 cloudreve

终于到最后一步可以进行编译主程序 cloudreve 了

导入交叉编译的环境变量：

```
export GOOS=windows
export GOARCH=amd64
export CC=x86_64-w64-mingw32-gcc
export CGO_ENABLED=1
```

其中 GOOS 表示目标操作系统，GOARCH 表示目标 CPU 架构。一般来说，只需要指定这两项就可以实现目标平台的交叉编译。

但 cloudreve 有用到 c 的一些类库，所以这里必须通过开启 CGO 来引用 GCC 交叉编译工具链来实现编译。

### 执行编译：

```
go build
```

如果不出问题，一两分钟你就可以在项目根目录，对应宿主机 `~/cloudreve` 目录中，看到 cloudreve.exe 这个二进制程序，将其复制到 windows 系统中运行使用。

## 再次编译：

更新源代码：

```
git pull origin master
```

更新子模块：

```
git submodule update --init --recursive
```

如果你修改了前端页面文件，你还需要重新进行打包前端资源文件，并嵌入到 golang 中。

如果只是修改了 golang 程序，那么只需要执行 `go build` 就可以实现编译。

[取消回复](https://blog.upx8.com/3118#respond-post-3118)

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