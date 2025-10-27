---
title: Docker安装新版MinIO（含反代、DNS Bucket、权限设置）
url: https://blog.upx8.com/3274
source: 黑海洋 - WIKI
date: 2023-03-14
fetch_date: 2025-10-04T09:30:37.206447
---

# Docker安装新版MinIO（含反代、DNS Bucket、权限设置）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Docker安装新版MinIO（含反代、DNS Bucket、权限设置）

发布时间:
2023-03-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
45331

最近需要给一台机器配个单机版的minio，遂记录下配置过程。

以前我写过一篇不是用docker安装的文章，但是那篇文章里面其实有些问题我没解决，这篇文章一并解决了。

在开始前，需要准备两个子域名并做好解析，一个用于api，一个用于console。

例如：minio.example.com（用于api）console.minio.example.com（用于console）

安装需要用到的软件：

```
apt -y update
apt -y install curl nginx python3-certbot-nginx
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

创建目录，新建docker-compose文件：

```
mkdir -p /opt/minio && cd /opt/minio && nano docker-compose.yml
```

写入如下配置：

```
version: '3.7'

services:
  minio:
    image: quay.io/minio/minio
    container_name: minio
    restart: unless-stopped
    environment:
      - MINIO_DOMAIN=minio.example.com
      - MINIO_SERVER_URL=https://minio.example.com
      - MINIO_BROWSER_REDIRECT_URL=https://console.minio.example.com
      - MINIO_ROOT_USER=imlala
      - MINIO_ROOT_PASSWORD=yourpasswd
    ports:
      - "127.0.0.1:9000:9000"
      - "127.0.0.1:9090:9090"
    volumes:
      - ./data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3
    command: server /data --console-address ":9090"
```

这里有几个非常容易混淆的环境变量，下面一个个详细解释下。

MINIO\_DOMAIN，是用来启用dns style bucket功能的，也就是virtual hosted-style，注意这个变量后面填写的域名不要加https://。

MINIO\_SERVER\_URL其实就是指的api服务域名，在配置反向代理的情况下，务必要正确填写为反代服务器所用的域名。

MINIO\_BROWSER\_REDIRECT\_URL指的是console的域名，在配置反向代理的情况下，也要填写为反代服务器所用的域名，同时不能与api服务用同相同的域名，用相同的域名会出各种各样的问题。

另外9000端口为api服务端口，9090为console端口。在配置反代的时候注意区分。

配置好了后启动即可：

```
docker compose up -d
```

下面来配置nginx反向代理。

反代api，新建nginx配置：

```
nano /etc/nginx/sites-available/minio
```

写入如下配置：

```
server {
   listen 80;
   server_name minio.example.com;
   ignore_invalid_headers off;
   client_max_body_size 0;
   proxy_buffering off;

   location / {
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header Host $http_host;

       proxy_connect_timeout 300;
       proxy_http_version 1.1;
       proxy_set_header Connection "";
       chunked_transfer_encoding off;
       proxy_pass http://localhost:9000;
   }
}
```

反代console，新建nginx配置：

```
nano /etc/nginx/sites-available/console-minio
```

写入如下配置：

```
server {
   listen 80;
   server_name console.minio.example.com;
   ignore_invalid_headers off;
   client_max_body_size 0;
   proxy_buffering off;

   location / {
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header Host $http_host;

       proxy_connect_timeout 300;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
       chunked_transfer_encoding off;
       proxy_pass http://localhost:9090;
   }
}
```

启用新的配置：

```
ln -s /etc/nginx/sites-available/minio /etc/nginx/sites-enabled/minio
ln -s /etc/nginx/sites-available/console-minio /etc/nginx/sites-enabled/console-minio
```

签发ssl证书：

```
certbot --nginx
```

现在可以打开控制台（console.minio.example.com）使用MINIO\_ROOT\_USER、MINIO\_ROOT\_PASSWORD来登录你的账号。

创建一个桶，假设这里我把桶名设置为imlala：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-07-44.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-07-44.png)

此时如果你需要用到dns bucket（virtual hosted-style）就再添加一个子域名解析到minio服务器。

例如：imlala.minio.example.com，解析名必须和桶名一致。

然后配置一个新的nginx反代：

```
nano /etc/nginx/sites-available/imlala-bucket
```

写入如下配置：

```
server {
   listen 80;
   server_name imlala.minio.example.com;
   ignore_invalid_headers off;
   client_max_body_size 0;
   proxy_buffering off;

   location / {
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header Host $http_host;

       proxy_connect_timeout 300;
       proxy_http_version 1.1;
       proxy_set_header Connection "";
       chunked_transfer_encoding off;
       proxy_pass http://localhost:9000;
   }
}
```

启用新的配置：

```
ln -s /etc/nginx/sites-available/imlala-bucket /etc/nginx/sites-enabled/imlala-bucket
```

签发ssl证书：

```
certbot --nginx
```

测试你的dns bucket，访问域名imlala.minio.example.com，如果正常的话应该能够看到类似下面的内容：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-21-19.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-21-19.png)

下面说一下最基本的权限设置，因为minio的权限配置很复杂，这里只说一下我个人日常使用的一些权限设置，如果你是自己一个人用，按照我这样配置就足够了。

还是用刚才创建的桶（imlala）来演示，如果你希望这个桶可以对外提供服务，首先需要把这个桶的匿名访问权限改为只读：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-29-20.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-29-20.png)

在perfix这里输入一个/则表示该桶下面的所有路径都是只读的：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-31-10.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-31-10.png)

注意这里一定不能给写权限，给写权限就意味着任何人都可以往这个桶上传文件。

然后现在还有一个问题是，虽然现在是只读的了，但是当用户直接访问你的桶域名（imlala.minio.example.com）会直接暴露出你桶下面的所有目录和文件名，等于是直接给你列目录了，这样也是不太好的。

我们可以通过配置具体的策略来关闭列目录，在你设置好匿名访问权限为只读后，刷新一下页面看到这个地方就会显示为custom：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_11-05-58.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_11-05-58.png)

编辑这个策略，看到里面默认的配置是：

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "*"
                ]
            },
            "Action": [
                "s3:GetBucketLocation",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::imlala"
            ]
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "*"
                ]
            },
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::imlala/*"
            ]
        }
    ]
}
```

只需删除”s3:ListBucket”即可关闭列目录，注意语法，删除”s3:ListBucket”也需要同时去掉上面”s3:GetBucketLocation”的逗号。

同时为安全起见，你应该在console创建一个新的普通用户，这个用户给一个读写权限即可：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-27-17.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_10-27-17.png)

然后用普通用户登录console，在这个普通用户下面创建Access Keys、Secret Key：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_11-16-04.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/01/lala.im_2023-01-18_11-16-04.png)

在配置其他程序使用桶的时候始终用普通用户下面的Access Keys、Secret Key即可。

1. **[2023-07-04 R11; 荒原往事](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9ncy5xdWRhbmdlLnRvcC81OTg)**

   2023-07-05 23:19:49

   [回复](https://blog.upx8.com/3274/comment-page-1?replyTo=27322#respond-post-3274)

   [...]参考这篇文章Docker安装新版MinIO（含反代、DNS Bucket、权限设置） (upx8.com)[...]

[取消回复](https://blog.upx8.com/3274#respond-post-3274)

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