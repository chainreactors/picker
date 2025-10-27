---
title: Picsur：简单易用的图床程序
url: https://buaq.net/go-161867.html
source: unSafe.sh - 不安全
date: 2023-05-06
fetch_date: 2025-10-04T11:38:37.036359
---

# Picsur：简单易用的图床程序

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/64fccc4a0e71e391f693af7f27fdc799.jpg)

Picsur：简单易用的图床程序

Picsur是一个类似Imgur的图床程序，主打的就是一个简单易用。我搭建试了一下，目前还只能上传单张图片，不能从浏览器批量上传。。如果介意这个的话可以
*2023-5-5 20:7:6
Author: [blog.upx8.com(查看原文)](/jump-161867.htm)
阅读量:30
收藏*

---

Picsur是一个类似Imgur的图床程序，主打的就是一个简单易用。

我搭建试了一下，目前还只能上传单张图片，不能从浏览器批量上传。。如果介意这个的话可以直接pass掉了。

还有就是图片是直接存储在postgresql数据库里面的。

项目地址：https://github.com/CaramelFur/Picsur

安装需要用到的软件：

```
apt -y update
apt -y install curl nginx python3-certbot-nginx
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

新建compose：

```
mkdir -p /opt/picsur && cd /opt/picsur && nano docker-compose.yml
```

写入如下配置：

```
version: '3.9'

services:
  picsur:
    image: ghcr.io/caramelfur/picsur:latest
    container_name: picsur
    restart: unless-stopped
    environment:
      PICSUR_DB_HOST: picsur_postgres
      PICSUR_DB_PORT: 5432
      PICSUR_DB_USERNAME: picsur
      PICSUR_DB_PASSWORD: dbpassword
      PICSUR_DB_DATABASE: picsur
      PICSUR_ADMIN_PASSWORD: adminpassword
      PICSUR_MAX_FILE_SIZE: 128000000
    ports:
      - '65535:8080'

  picsur_postgres:
    image: postgres:14-alpine
    container_name: picsur_postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: picsur
      POSTGRES_PASSWORD: dbpassword
      POSTGRES_USER: picsur
    volumes:
      - ./db:/var/lib/postgresql/data
```

启动：

```
docker compose up -d
```

配置nginx反代：

```
nano /etc/nginx/sites-available/picsur
```

写入如下配置：

```
server {
    listen 80;
    server_name picsur.example.com;
    client_max_body_size 0;

    location / {
        proxy_pass http://127.0.0.1:65535;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```

启用新的nginx配置：

```
ln -s /etc/nginx/sites-available/picsur /etc/nginx/sites-enabled/picsur
```

签发ssl证书：

```
certbot --nginx
```

默认的管理员账号是admin，密码是compose内的PICSUR\_ADMIN\_PASSWORD变量设置的值。

建议登录进去之后在系统设置里面把反代的域名配置一下：

[![](https://lala.im/wp-content/uploads/2023/05/lala.im_2023-05-04_14-39-40.png)](https://lala.im/wp-content/uploads/2023/05/lala.im_2023-05-04_14-39-40.png)

文章来源: https://blog.upx8.com/3507
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)