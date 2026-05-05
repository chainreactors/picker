---
title: Docker入门之最轻量的编排神器docker compose
url: https://mp.weixin.qq.com/s/-a5iLiCGgc0W3uH53kcaPA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:00:27.253941
---

# Docker入门之最轻量的编排神器docker compose

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvczvbZRXYGrv64aw2UGCibMBIb8Xo41ah8QIy5ibPBAWdBj7yXN3dkHDCibFcbyZFps3IGZEHe108UPKhMb2qEB8uDjibiaQxzPqf6k/0?wx_fmt=jpeg)

# Docker入门之最轻量的编排神器docker compose

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

缘起

可能会有人以为，docker编排，适用于复杂应用架构和集群环境，单机应用并不需要，其实说起个人对docker编排的需求，来源于逐渐复杂的docker运行命令：

1. 启动一个简单的docker

```
docker run -it alpine sh
```

2. 一个应用端口，一个管理端口

```
docker run -it -p 80:80 -p 8080:8080 alpine sh
```

3. 持久化应用数据，日志

```
docker run -it -p 80:80 -p 8080:8080 -v ./data:/data -v ./log:/var/log/nginx  alpine sh
```

4. 指定自定义的网络、传递环境变量给应用程序

```
docker run -it -p 80:80 -p 8080:8080 -v ./data:/data -v ./log:/var/log/nginx -e --network=bridge NGINX_PORT=80 --name alpine alpine sh
```

此处省略N个需求，然后，你可能会遇到下面这个启动命令：

```
docker run -d \  --name my_nginx_demo \  --restart unless-stopped \  -p 8080:80 \  -p 8443:443 \  -v /host/nginx/html:/usr/share/nginx/html:ro \  -v /host/nginx/conf/nginx.conf:/etc/nginx/nginx.conf:ro \  -v my_volume:/app/data \  --mount type=bind,source=/host/logs,target=/var/log/nginx \  -e NGINX_HOST=example.com \  -e NGINX_PORT=80 \  --env-file=./env.list \  --network=bridge \  --dns 8.8.8.8 \  --dns-search example.com \  --hostname webserver \  --add-host extrahost:192.168.1.100 \  --link db_container:db \  -m 512m \  --memory-reservation 256m \  --memory-swap 1g \  --cpus 1.5 \  --cpu-shares 512 \  --ulimit nofile=65536:65536 \  --shm-size 256m \  --security-opt seccomp=unconfined \  --cap-add NET_ADMIN \  --cap-drop ALL \  --user 1000:1000 \  --read-only \  --tmpfs /tmp:rw,noexec,nosuid,size=64m \  --health-cmd="curl -f http://localhost/ || exit 1" \  --health-interval=30s \  --health-retries=3 \  --label env=production \  --label project=mywebapp \  --log-driver json-file \  --log-opt max-size=10m \  --log-opt max-file=3 \  --rm=false \  nginx:latest
```

会有人想在命令行输入这个命令么？

如果有了编排，就可以将这些需求全部写在编排文件中，然后简单：

```
docker compose up -d
```

所以，还有人以为，单个镜像的启动，并不需要编排？

## docker compose 简单介绍

docker compose 起源于一个叫 Fig 的开源项目，最初，他只是一个python脚本，用来读取配置文件（现今的编排文件），将其转换成docker run命令去执行，以实现将复杂的docker命令简单化。所以最初他是一个可执行的python脚本，后来docker收购了他，改名docker-compose，安装方式就是下载并放在/usr/bin/目录下。

docker-compose确实太好用了，说他是单机docker必备的工具也不为过，所以后来docker官方将docker-compose功能直接集成到了docker cli中，命令变成了docker compose，让其变成了docker的一个子命令。

## docker compose 命令的简单适用

最简单的就是启动和关闭了：

```
docker compose up docker compose down
```

***注意：*** 这里有一个默认参数，就是编排文件：当前目录下的compose.yml文件（兼容v1版本的docker-compose.yml）,也可以手工指定非当前目录或者非标准文件名的编排文件：-f 文件名

其他常用命令：

简单的记忆方法就是，他可以用docker其他关于容器的命令，只是默认使用编排文件限制范围：

```
docker compose ps   # 类似与docker ps查看运行的容器，不过只现实当前默认配置文件里面的容器...
```

## docker compose 编排文件解释

docker run命令有九个核心功能维度：运行控制、网络配置、存储管理、环境变量、资源限制、安全权限、健康检查、日志管理、元数据标记。

来使用一个简单的例子，来简单说明使用docker compose 编排的时候，如何实现：

```
services:  my_nginx_demo:    image: nginx:latest    container_name: my_nginx_demo  # 1    restart: unless-stopped    # 1    ports:   # 2      - "8080:80"      - "8443:443"    volumes:  # 3      - /host/nginx/html:/usr/share/nginx/html:ro      - /host/nginx/conf/nginx.conf:/etc/nginx/nginx.conf:ro      - my_volume:/app/data      - /host/logs:/var/log/nginx    environment:   #  4      NGINX_HOST: example.com      NGINX_PORT: 80    env_file:      - ./env.list    networks:          - default_network   # 2    dns:   #2      - 8.8.8.8    dns_search:  #2      - example.com    hostname: webserver  # 2    extra_hosts:      - "extrahost:192.168.1.100"    deploy:      resources:        limits:    # 4          cpus: "1.5"          memory: 512m        reservations:          cpus: "0.5"          memory: 256m    mem_swappiness: 0    shm_size: 256m   # 4    ulimits:      nofile:        soft: 65536        hard: 65536    security_opt:  # 5      - seccomp=unconfined    cap_add:  # 5      - NET_ADMIN    cap_drop:  # 5      - ALL    user: "1000:1000"   # 5    read_only: true  # 5    tmpfs:      - /tmp:rw,noexec,nosuid,size=64m    healthcheck:   # 6      test: ["CMD", "curl", "-f", "http://localhost/"]      interval: 30s      retries: 3      start_period: 10s      timeout: 10s    labels:   # 4      env: production      project: mywebapp    logging:   # 7      driver: json-file      options:        max-size: "10m"        max-file: "3"
networks:       # 2  default_network:    driver: bridge
volumes:    # 3  my_volume:    driver: local
```

简单的解释（下列序号对应编排文件中注释的序号）：

1. 运行控制：容器名称、重启策略

   container\_name： my\_nginx\_demo：为容器指定一个名称，便于后续管理。

   restart： 设置容器的重启策略。unless-stopped表示容器退出时自动重启，除非手动停止。
   其他可选值包括no（不重启）、on-failure（仅在异常退出时重启）、always（总是重启）
2. 网络配置

   networks： 指定自定义docker网络，以及其他网络配置
3. 存储与数据持久化参数

   volumes： 数据存储和持久化，这里也分三种：命名卷、临时卷、绑定挂载，这些基础知识见前文：

   [Docker 入门之基本概念](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651207&idx=1&sn=a2f78e7c80d0a950cd43df8efb4b2d0a&scene=21#wechat_redirect)
4. 环境变量与元数据参数

   environment: 直接配置的环境变量

   env\_file: 将文件的内容直接导入成环境变量

   labels： 为容器添加标签，用于元数据标记和分类管理，方便后续通过标签过滤和搜索容器
5. 安全与权限参数

   security\_opt: 配置安全选项，例如seccomp、AppArmor等安全配置

   cap\_add: 添加Linux能力，例如NET\_ADMIN，允许容器执行特定的网络管理操作

   cap\_drop: 删除默认的Linux能力，例如ALL，移除容器的所有默认权限，增强安全性

   user: 指定容器内运行的用户和用户组，例如"1000:1000"，避免以root用户运行容器，提高安全性

   read\_only: 将容器文件系统设置为只读，防止容器内的应用程序修改文件系统，增强安全性

   tmpfs: 将指定目录挂载为临时文件系统（tmpfs），可以设置为只读、不可执行等选项，增强安全性和性能

   ***PS:*** 关于权限的需求，来源于安全，来源于no-root 容器的需求，使用root运行的镜像，大部分是不需要配置相关安全权限的。
6. 健康检查参数

   定义健康检查命令，定期检查Nginx是否正常响应，每30秒执行一次，连续失败3次后标记容器为不健康
7. 日志管理参数

   指定日志驱动为json-file（默认值），将日志以JSON格式写入文件限制单个日志文件大小为10MB，最多保留3个历史日志文件，防止日志无限增长

***注意：*** 这是一个为了解释编排功能的意象编排文件，实际使用中并不需要显示指定这些参数，大部分使用默认参数即可运行，只有在你需要的时候，才配置这些参数。

## 小结

这里只简单的说明了编排对单个运行容器的作用，下次再写关于多容器的编排，那才是编排的更高级的用途。

## 推荐本系列其他

[Docker 入门之基本概念](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651207&idx=1&sn=a2f78e7c80d0a950cd43df8efb4b2d0a&scene=21#wechat_redirect)

[Docker 入门之网络基础](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651229&idx=1&sn=5a2f71c14af29d9f4b426045fdb3274b&scene=21#wechat_redirect)

[Dockerfile语法全解析：从构建原理到分层构建的实战指南](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651314&idx=1&sn=763e8906a602d17e55fd0b89918f0960&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过