---
title: MCSManager 游戏服务端web面板
url: https://blog.upx8.com/3150
source: 黑海洋 - WIKI
date: 2022-12-15
fetch_date: 2025-10-04T01:32:48.922252
---

# MCSManager 游戏服务端web面板

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# MCSManager 游戏服务端web面板

发布时间:
2022-12-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
16837

## 这是什么？

MCSManager 面板（简称：MCSM 面板）是一款开源，分布式，轻量级，快速部署，支持大部分游戏服务端和控制台程序的管理面板

官方：[https://mcsmanager.com/](https://blog.upx8.com/go/aHR0cHM6Ly9tY3NtYW5hZ2VyLmNvbS8)

## 软件特性

软件在 Minecraft 和其他游戏社区内中已有一定的流行程度，它可以帮助你集中管理多个物理服务器，动态在任何主机上创建游戏服务端，并且提供安全可靠的多用户权限系统，可以很轻松的帮助你管理多个服务器，一直在为 Minecraft，Terraria，Steam 游戏服务器管理员，运维人员和个人开发者提供健康的软件支持。

[![截图.png](https://camo.githubusercontent.com/7d2741c08bbda304ba727add920a1b362f2c5a7c7356dedb6452a2c71efcfac3/68747470733a2f2f7075626c69632d6c696e6b2e6f73732d636e2d7368656e7a68656e2e616c6979756e63732e636f6d2f6d63736d5f706963747572652f4d43534d392e706e67)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS83ZDI3NDFjMDhiYmRhMzA0YmE3MjdhZGQ5MjBhMWIzNjJmMmM1YTdjNzM1NmRlZGI2NDUyYTJjNzFlZmNmYWMzLzY4NzQ3NDcwNzMzYTJmMmY3MDc1NjI2YzY5NjMyZDZjNjk2ZTZiMmU2ZjczNzMyZDYzNmUyZDczNjg2NTZlN2E2ODY1NmUyZTYxNmM2OTc5NzU2ZTYzNzMyZTYzNmY2ZDJmNmQ2MzczNmQ1ZjcwNjk2Mzc0NzU3MjY1MmY0ZDQzNTM0ZDM5MmU3MDZlNjc)

[![Screenshot.png](https://camo.githubusercontent.com/2294089f8139f99b180d843f6548f208adb5c9fcf7e5206e6aaff73ba52b1039/68747470733a2f2f6d63736d616e616765722e636f6d2f6d61696e322e706e67)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS8yMjk0MDg5ZjgxMzlmOTliMTgwZDg0M2Y2NTQ4ZjIwOGFkYjVjOWZjZjdlNTIwNmU2YWFmZjczYmE1MmIxMDM5LzY4NzQ3NDcwNzMzYTJmMmY2ZDYzNzM2ZDYxNmU2MTY3NjU3MjJlNjM2ZjZkMmY2ZDYxNjk2ZTMyMmU3MDZlNjc)

[![QQ20221207-174328@2x](https://user-images.githubusercontent.com/18360009/206144481-7f57b40d-f71b-4d7e-a617-846da69ca1a3.png)](https://user-images.githubusercontent.com/18360009/206144481-7f57b40d-f71b-4d7e-a617-846da69ca1a3.png)

## 运行环境

控制面板可运行在 Windows 与 Linux 平台，无需数据库与任何系统配置，只需安装 node 环境即可快速运行，属于轻量级的 Minecraft 服务端控制面板。

必须 `Node 14.17.0` 以上，无需数据库和更改任何系统配置，开箱即可运行。

## 配置/数据文件

配置文件： `data/SystemConfig/config.json`

用户数据文件：`data/User/*.json`

远程守护进程配置：`data/RemoteServiceConfig/*.json`

## 软件文档

地址：[https://docs.mcsmanager.com/](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLm1jc21hbmFnZXIuY29tLw)

## 安装

### Windows

对于 Windows 系统，**已整合成直接运行版本，下载即可运行**（使用管理员权限运行）:

前往：[https://mcsmanager.com/](https://blog.upx8.com/go/aHR0cHM6Ly9tY3NtYW5hZ2VyLmNvbS8)

### Linux

**一行命令快速安装**

```
// 国内用户专用 gitee 加速源
wget -qO- https://gitee.com/mcsmanager/script/raw/master/setup.sh | bash

// 或原始源（科学上网）
wget -qO- https://raw.githubusercontent.com/mcsmanager/Script/master/setup.sh | bash
```

* 脚本仅适用于 AMD64 架构 Ubuntu/Centos/Debian/Archlinux。
* 执行完成后，使用 `systemctl start mcsm-{web,daemon}` 即可启动面板服务。
* 面板代码与运行环境自动安装在 `/opt/mcsmanager/` 目录下。

**Linux 手动安装**

* 若一键安装不起作用，则可以尝试此步骤手动安装。

```
# 切换到安装目录，没有此目录请执行 mkdir /opt/
cd /opt/
# 下载运行环境（已有 Node 14+ 可忽略）
wget https://npmmirror.com/mirrors/node/v14.17.6/node-v14.17.6-linux-x64.tar.gz
# 解压文件
tar -zxvf node-v14.17.6-linux-x64.tar.gz
# 链接程序到环境变量中
ln -s /opt/node-v14.17.6-linux-x64/bin/node /usr/bin/node
ln -s /opt/node-v14.17.6-linux-x64/bin/npm /usr/bin/npm

# 准备安装目录
mkdir /opt/mcsmanager/
cd /opt/mcsmanager/

# 下载面板端（Web）程序
git clone https://github.com/MCSManager/MCSManager-Web-Production.git
# 重命名文件夹并进入
mv MCSManager-Web-Production web
cd web
# 安装依赖库
npm install --production --registry=https://registry.npmmirror.com/
cd /opt/mcsmanager/

# 下载守护进程（Daemon）程序
git clone https://github.com/MCSManager/MCSManager-Daemon-Production.git
# 重命名文件夹并进入
mv MCSManager-Daemon-Production daemon
cd daemon
# 安装依赖库
npm install --production --registry=https://registry.npmmirror.com/

# 打开两个终端或两个 Screen 软件的终端窗口
# 先启动守护进程
cd /opt/mcsmanager/daemon
# 启动
node app.js

# 然后启动面板端进程
cd /opt/mcsmanager/web
# 启动
node app.js

# 访问 http://localhost:23333/ 即可进入面板。
# 默认情况下，面板端会自动扫描 daemon 文件夹并且自动连接到守护进程。
```

* 注意，这种安装方式不会自动注册面板到系统服务（Service），所以必须使用 `screen` 软件来管理。

## 更新版本

如果您是 `9.X` 升级到更高版本，在 `Linux` 系统下，请分别前往 `/opt/mcsmanager/web`，`/opt/mcsmanager/daemon` 目录中执行 `git pull` 进行更新。

在 `Windows` 系统下更新请前往官方下载最新安装包，覆盖所有文件即可生效。

> 注意，建议更新前备份一次 `data` 目录。

## 项目体系

整个软件运行需要三个项目的互相配合才可运行，您普通安装的代码是编译再整合后的产物。

[**控制面板端**](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01DU01hbmFnZXIvTUNTTWFuYWdlcg)

* 角色：控制中心
* 责任：负责提供网页前端的后端接口，提供 API 接口，用户数据管理和对守护进程进行通信和授权。

[**网页前端**](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01DU01hbmFnZXIvVUk)

* 角色：控制中心的用户交互界面
* 责任：以网页形式展示数据，发送请求，并且拥有与守护进程通信的能力，此项目最终产物是纯静态文件。

[**守护进程**](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01DU01hbmFnZXIvRGFlbW9u)

* 角色：被控端
* 责任：控制本地主机的所有实例，真实进程的实际管理者，拥有与任何对象的通信能力。

## 搭建开发环境

此段落面向开发人员，普通用户无需关注也无需执行。

所有项目全部以开发环境运行后，便可以进行开发与预览，请务必遵循开源协议。

**控制面板端（MCSManager）**

```
git clone https://github.com/MCSManager/MCSManager.git
cd MCSManager
npm install
npm run start
# 默认将采用 ts-node 直接执行 Typescript 代码
# 默认运行在 23333 端口
```

**网页前端（UI）**

```
git clone https://github.com/MCSManager/UI.git
cd UI
npm install
npm run serve
# 访问 http://localhost:8080/ 即可预览界面
# 所有 API 请求将自动转发到 23333 端口
```

**守护进程（Daemon）**

```
git clone https://github.com/MCSManager/Daemon.git
cd Daemon
npm install
npm run start
# 运行后请在控制面板端连接本守护进程
# 默认运行在 24444 端口
```

[取消回复](https://blog.upx8.com/3150#respond-post-3150)

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