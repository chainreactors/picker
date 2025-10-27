---
title: Ente全家桶部署：Ente Photos、Ente Auth
url: https://blog.upx8.com/4758
source: 黑海洋 - Wiki
date: 2025-04-20
fetch_date: 2025-10-06T22:03:27.844289
---

# Ente全家桶部署：Ente Photos、Ente Auth

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ente全家桶部署：Ente Photos、Ente Auth

发布时间:
2025-04-19

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
62560

[Ente](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2VudGUtaW8vZW50ZQ)是印度人开源的一套端到端加密平台服务，他们打算在这个平台内开发众多产品，目前平台内已经开发出了2个产品分别是：

Ente Photos（Apple和Google Photos的替代品）、Ente Auth（2FA应用程序）

这篇文章详细记录下部署过程，喜欢折腾的可以逝试。。。

由于他们的文档写的太拉稀了（估计是故意的，想让别人买他们的托管服务）导致整个部署过程中坑太多了，而且他们的这些个程序涉及到很多不同的组件又相互依赖，导致配置起来非常复杂，硬生生让我体验到了小时候拼积木的那种感觉。。。

说实话咖喱味有点重，到处糊，连文档都是这里糊一点那里糊一点。。。

其实当我部署完了后我压根就没有心情去用了，这么复杂的东西要我自托管，没出问题还好，要出了点问题修都不知道从哪里开始。。而且最重要的是Ente Photos这个程序，就我个人体验了一番后，真的觉得不如immich一根，我直接去用immich多好，省时又省力。。。

至于Ente Auth（2FA应用程序），这玩意谁去用自托管的啊，是Google身份验证器不香了嘛？你的小鸡再稳能有Google的稳？不怕哪天机子炸了把你全关门外了？我最多自托管个Bitwarden密码管理器，要我自托管2FA程序我觉得完全没必要，我又不是FBI，又不是国家机密人员。。。

不过有一说一，人家好歹开源了就是。。是真开源，非常完整的开源。。服务端、Web端、各种客户端（Android、iOS、Windows等）都开源了。。

纯当闲着没事瞎坤8折腾了。。

准备工作：

1、一个SMTP服务器，用于注册账号发验证码。

2、域名做好如下解析：

ente-museum.example.com （后端服务）
ente-web.example.com （Ente Photos的Web客户端）
ente-cast.example.com （为Ente Photos提供投屏幻灯片的功能）
ente-albums.example.com （为Ente Photos提供分享相册的功能）
ente-accounts.example.com （Passkey通行密钥，这也是一种2FA服务，这个和Ente Auth是分开的）
ente-auth.example.com （Ente Auth 2FA应用程序的Web客户端）
minio.example.com （minio对象存储API）
console.minio.example.com （minio对象存储控制台）

安装好Docker和需要用到的包：

```
apt -y update
apt -y install curl wget nginx python3-certbot-nginx
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

创建目录和compose文件：

```
mkdir -p /opt/ente.io && cd /opt/ente.io && nano docker-compose.yml
```

写入如下内容，需要修改的地方都写了注释：

```
name: ente.io
services:
  museum:
    image: ghcr.io/ente-io/server:latest
    container_name: ente-museum
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - ./museum.yaml:/museum.yaml:ro
      - ./ente-data:/data:ro

  web:
    image: ghcr.io/ente-io/web:latest
    container_name: ente-web
    restart: unless-stopped
    environment:
      ENTE_API_ORIGIN: https://ente-museum.example.com # 后端服务museum的域名
      ENTE_ALBUMS_ORIGIN: https://ente-albums.example.com # 分享相册的域名
    ports:
      - "127.0.0.1:3000:3000" # Photos web app
      - "127.0.0.1:3001:3001" # Accounts
      - "127.0.0.1:3003:3003" # Auth
      - "127.0.0.1:3004:3004" # Cast

  albums:
    image: ghcr.io/ente-io/web:latest
    container_name: ente-albums
    restart: unless-stopped
    environment:
      ENTE_API_ORIGIN: https://ente-museum.example.com # 后端服务museum的域名
      ENTE_ALBUMS_ORIGIN: https://ente-albums.example.com # 分享相册的域名
    ports:
      - "127.0.0.1:3002:3002" # Public albums

  socat:
    image: alpine/socat
    container_name: ente-socat
    restart: unless-stopped
    network_mode: service:museum
    depends_on:
      - museum
    command: "TCP-LISTEN:3200,fork,reuseaddr TCP:minio:3200"

  postgres:
    image: postgres:16
    container_name: ente-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: imlala # 数据库用户名
      POSTGRES_PASSWORD: pgpassword # 数据库用户的密码
      POSTGRES_DB: ente_db # 数据库名
    volumes:
      - ./db-data:/var/lib/postgresql/data
    healthcheck:
      test:
        [
          "CMD",
          "pg_isready",
          "-q",
          "-d",
          "ente_db",
          "-U",
          "pguser"
        ]
      start_period: 40s
      start_interval: 1s

  minio:
    image: minio/minio
    container_name: ente-minio
    restart: unless-stopped
    environment:
      MINIO_SERVER_URL: "https://minio.example.com" # MinIO对象存储API的域名
      MINIO_BROWSER_REDIRECT_URL: "https://console.minio.example.com" # MinIO对象存储控制台的域名
      MINIO_ROOT_USER: admin # MinIO对象存储用户名
      MINIO_ROOT_PASSWORD: miniopassword # MinIO对象存储用户的密码
    ports:
      - "127.0.0.1:3200:3200"
      - "127.0.0.1:3201:3201"
    volumes:
      - ./minio-data:/data
    command: server /data --address ":3200" --console-address ":3201"

  minio-provision:
    image: minio/mc
    container_name: ente-provision
    depends_on:
      - minio
    volumes:
      - ./minio-provision.sh:/provision.sh:ro
      - ./minio-data:/data
    entrypoint: sh /provision.sh
```

新建后端服务museum需要用到的配置文件：

```
nano museum.yaml
```

写入如下配置：

```
key:
    encryption: hidden
    hash: hidden

jwt:
    secret: hidden

apps:
    public-albums: https://ente-albums.example.com
    cast: https://ente-cast.example.com
    accounts: https://ente-accounts.example.com

webauthn:
    rpid: ente-accounts.example.com
    rporigins:
        - "https://ente-accounts.example.com"

#internal:
#    admins:
#        - hidden
#    disable-registration: true

smtp:
    host: mail.example.com
    port: 587
    username: smtp
    password: smtppassword
    email: smtp@example.com

db:
    host: postgres
    port: 5432
    name: ente_db
    user: imlala
    password: pgpassword

s3:
    are_local_buckets: true
    b2-eu-cen:
        key: admin
        secret: miniopassword
        endpoint: https://minio.example.com
        region: eu-central-2
        bucket: b2-eu-cen
    wasabi-eu-central-2-v3:
        key: admin
        secret: miniopassword
        endpoint: https://minio.example.com
        region: eu-central-2
        bucket: wasabi-eu-central-2-v3
        compliance: false
    scw-eu-fr-v3:
        key: admin
        secret: miniopassword
        endpoint: https://minio.example.com
        region: eu-central-2
        bucket: scw-eu-fr-v3
```

注意事项：

1.配置文件内各种加密密钥的生成：

key生成：

```
head -c 32 /dev/urandom | base64 | tr -d '\n';
```

hash生成：

```
head -c 64 /dev/urandom | base64 | tr -d '\n';
```

jwt生成：

```
head -c 32 /dev/urandom | base64 | tr -d '\n' | tr '+/' '-_';
```

用生成好的内容替换掉上述配置文件内的hidden字符串。

2.s3存储的名字目前在配置文件内是硬编码的，不能修改，比如b2-eu-cen。但是实际的bucket的名字是可以改的。

3.如果不启用复制功能（默认情况下未启用），实际上只需要b2-eu-cen这一个bucket就够了，剩下的wasabi-eu-central-2-v3和scw-eu-fr-v3没有用到，数据是不会存储在里面的。

接下来还需要新建一个脚本文件：

```
nano minio-provision.sh
```

写入如下内容，用于初始化minio对象存储，创建需要用到的bucket等，注意修改脚本内的miniopassword密码为你自己的：

```
#!/bin/sh

# Script used to prepare the minio instance that runs as part of the development
# Docker compose cluster.

while ! mc config host add h0 http://minio:3200 admin miniopassword
do
   echo "waiting for minio..."
   sleep 0.5
done

cd /data

mc mb -p b2-eu-cen
mc mb -p wasabi-eu-central-2-v3
mc mb -p scw-eu-fr-v3
```

给执行权限：

```
chmod +x minio-provision.sh
```

启动：

```
docker compose up -d
```

现在来配置NGINX反向代理。新建反向代理museum后端的配置文件：

```
nano /etc/nginx/sites-available/ente-museum
```

写入如下配置：

```
server {
    listen 80;
    server_name ente-museum.example.com;
    client_max_body_size 0;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

新建反向代理Ente Photos Web客户端的配置文件：

```
nano /etc/nginx/sites-available/ente-web
```

写入如下配置：

```
server {
    listen 80;
    server_name ente-web.example.com;
    client_max_body_size 0;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

新建反向代理Ente Photos投屏幻灯片的配置文件：

```
nano /etc/nginx/sites-available/ente-cast
```

写入如下配置：

```
server {
    listen 80;
    server_name ente-cast.example.com;
    client_max_body_size 0;

    location / {
        proxy_pass http://127.0.0.1:3004;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X...