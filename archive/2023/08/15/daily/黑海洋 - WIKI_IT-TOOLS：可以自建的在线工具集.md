---
title: IT-TOOLS：可以自建的在线工具集
url: https://blog.upx8.com/3778
source: 黑海洋 - WIKI
date: 2023-08-15
fetch_date: 2025-10-04T12:02:40.490287
---

# IT-TOOLS：可以自建的在线工具集

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# IT-TOOLS：可以自建的在线工具集

发布时间:
2023-08-14

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
22602

IT-TOOLS有点类似于国内的站长工具，里面有各种各样的小工具可供使用，比如：uuid生成器、ipv4子网计算器、base64加密、dockerrun转dockercompose等等。

项目地址：https://github.com/CorentinTh/it-tools

安装需要用到的软件：

```
apt -y update
apt -y install curl nginx python3-certbot-nginx
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

新建compose：

```
mkdir -p /opt/ittools && cd /opt/ittools && nano docker-compose.yml
```

写入如下配置：

```
version: '3.9'

services:
  ittools:
    image: 'ghcr.io/corentinth/it-tools:latest'
    container_name: it-tools
    restart: unless-stopped
    ports:
      - '65534:80'
```

启动：

```
docker compose up -d
```

配置nginx反代：

```
nano /etc/nginx/sites-available/ittools
```

写入如下配置：

```
server {
    listen 80;
    server_name it-tools.example.com;
    client_max_body_size 0;

    location / {
        proxy_pass http://127.0.0.1:65534;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```

启用新的nginx配置：

```
ln -s /etc/nginx/sites-available/ittools /etc/nginx/sites-enabled/ittools
```

签发ssl证书：

```
certbot --nginx
```

预览：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/05/lala.im_2023-05-04_14-59-55.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/05/lala.im_2023-05-04_14-59-55.png)

[取消回复](https://blog.upx8.com/3778#respond-post-3778)

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