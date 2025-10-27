---
title: Linux使用docker安装wireguard带UI面板
url: https://blog.upx8.com/3147
source: 黑海洋 - WIKI
date: 2022-12-12
fetch_date: 2025-10-04T01:15:07.597819
---

# Linux使用docker安装wireguard带UI面板

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux使用docker安装wireguard带UI面板

发布时间:
2022-12-11

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
45001

# 前言

之前发过一个[Linux使用K3S安装wireguard带UI面板](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudHJ1ZW5hc3NjYWxlLmNvbS8yMDIxLzEyLzI1LzQwMy5odG1s)，今天来发一个简单的docker安装wg

# 安装docker

网上其实有挺多的安装docker的教程，不过我将会使用官方的方法，授人以渔，教大家如何使用官方的文档。

首先打开[dockerhub](https://blog.upx8.com/go/aHR0cHM6Ly9odWIuZG9ja2VyLmNvbS8)

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/2696758026.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/2696758026.png)

往下滑，滑到最下面，点击Docs

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/2127618477.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/2127618477.png)

点击download and install

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/1173527544.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/1173527544.png)

选择你的系统

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/3945671880.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/3945671880.png)

选择你的发行版，我这里是Debian

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/2864228339.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/2864228339.png)

卸载现有的版本，如果没有就不用执行了

然后按照文档安装即可

安装依赖

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

添加docker官方的GPG key

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

设置稳定版仓库

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

安装docker

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

检查版本

```
docker version
```

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/2642518088.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/2642518088.png)

有显示就是安装好了

# 安装wireguard

这期的wireguard使用[这个项目](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1BsYWNlMS93Zy1hY2Nlc3Mtc2VydmVy)

```
docker run \
  -it \
  -d \
  --cap-add NET_ADMIN \
  --device /dev/net/tun:/dev/net/tun \
  -v wg-access-server-data:/data \
  -e "WG_ADMIN_PASSWORD=admin的密码" \
  -e "WG_WIREGUARD_PRIVATE_KEY=私钥" \
  -p 8000:8000/tcp \
  -p 51820:51820/udp \
  place1/wg-access-server
```

私钥可以在电脑上下一个wireguard软件，新建手动隧道，会生成私钥

安装好浏览器访问IP:8080就可以访问了，账号是admin

[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/3090225611.png)image.png](https://www.truenasscale.com/usr/uploads/2022/01/3090225611.png)

添加设备就可以获得节点信息了
[![image.png](https://www.truenasscale.com/usr/uploads/2022/01/2917026283.png)](https://www.truenasscale.com/usr/uploads/2022/01/2917026283.png)

1. ![jabeta](https://gravatar.loli.net/avatar/avatar/bc5de58a5180cc47de0678ed6a725689?s=32&r=&d=)

   **jabeta**

   2022-12-20 19:46:39

   [回复](https://blog.upx8.com/3147/comment-page-1?replyTo=26800#respond-post-3147)

   大哥图没了，麻烦方便时候更新一下呗

[取消回复](https://blog.upx8.com/3147#respond-post-3147)

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