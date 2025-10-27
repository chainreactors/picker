---
title: 搭建web网页版ssh（tabby-web）
url: https://blog.upx8.com/4208
source: 黑海洋 - WIKI
date: 2024-07-06
fetch_date: 2025-10-06T17:43:33.000556
---

# 搭建web网页版ssh（tabby-web）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 搭建web网页版ssh（tabby-web）

发布时间:
2024-07-05

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
25940

## ![](https://img.imgdd.com/f210f3.7d54132c-513e-4683-b216-47fc6131323c.png)

## 前言

因为每次连接服务器都要下载ssh终端软件，如果是临时使用，不是很方便。所以有个网页版的ssh会更方便使用。

## 项目地址：https://github.com/Eugeny/tabby-web

## 第一步：安装docker和docker-compose

```
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```

## 第二步：新建目录及配置文件

1.在终端运行下面的命令新建目录和配置文件

```
mkdir tabby && cd tabby
nano docker-compose.yml
```

2.把下面的配置文件内容粘贴到docker-compose.yml

**配置文件内容**

```
version: "3.8"

x-app: &common
  restart: on-failure:3
  logging:
    driver: "json-file"
    options:
      max-size: "200k"
      max-file: "10"
  network_mode: bridge

services:
  tabby-web:
    <<: *common
    image: ghcr.io/eugeny/tabby-web:latest
    container_name: tabby-web
    restart: always
    environment:
      - PORT=8006
      - DEBUG=False
      - APP_DIST_STORAGE=file:///app-dist
      - DATABASE_URL=mysql://user:pass@ip:3306/webssh # 设置数据库信息
      - NPM_REGISTRY=https://registry.npmjs.com
      - SOCIAL_AUTH_GITHUB_KEY=1234567890 # 设置GITHUB信息
      - SOCIAL_AUTH_GITHUB_SECRET=1234567890 # 设置GITHUB信息
    volumes:
      - /opt/docker-data/tabby-web:/app-dist
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - 8006:8006
    deploy:
      resources:
        limits:
          memory: 4G  # 设置内存限制为4GB

  tabby-connection-gateway:
    <<: *common
    image: ghcr.io/eugeny/tabby-connection-gateway:master
    container_name: tabby-connection-gateway
    restart: always
    environment:
      - TABBY_AUTH_TOKEN=1234567890 # 设置验证Token，随便填
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - 9000:9000
    command: --token-auth --host 0.0.0.0
```

## 第三步：拉取启动和设置版本信息。

1.启动拉取Tabby项目

```
docker-compose up -d
```

2.设置nightly版本

设置版本的命令

```
docker exec -it tabby-web /manage.sh add_version 1.0.189-nightly.2

docker exec -it tabby-web sh -c "cd /app-dist/1.0.189-nightly.2 && mv tmp*/* . && rm -rf tmp*"
```

可以在**[这里查询](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubnBtanMuY29tL3BhY2thZ2UvdGFiYnktd2ViLWNvbnRhaW5lcj9hY3RpdmVUYWI9dmVyc2lvbnM)**最新的版本号。

第四步：访问SSH网页

```
127.0.0.1:8006
```

把127.0.0.1改为你自己服务器的IP。想要用域名访问的话，就自己反代一下。

[取消回复](https://blog.upx8.com/4208#respond-post-4208)

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