---
title: Docker 常用操作命令
url: https://blog.upx8.com/3145
source: 黑海洋 - WIKI
date: 2022-12-11
fetch_date: 2025-10-04T01:12:32.645799
---

# Docker 常用操作命令

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Docker 应用：部署 LAMP 应用程序环境

发布时间:
2022-12-10

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
15131

![](https://eller.top/storage/images/Hq4ELfR1Kg8EPs23S75EZW1ORYiwWSMXOVC9wXn2.png)

本文来简单通过 Docker 部署一套可用的 LAMP 环境，在这个过程中你不再需要考虑依赖缺失的问题，不再考虑调整编译参数的问题，这一切都交给 Docker 和成熟可用的 Docker  镜像。

我们需要做的就是将项目路径、文件配置规划好，方便 后期移植、升级、更替容器镜像。

如果你还没安装 Docker 可以参照这篇文章 Docker 离线安装及基础操作使用教程 快速安装好 Docker。

# 规划配置

当前系统采用 debian10 记录，其他系统类似，可以参考。

为移植方便，我们将所有数据存储在一个路径下：/mnt/veracrypt

```
# Docker 数据存储路径：
mkdir /mnt/veracrypt/docker -p

#MySQL 数据存储路径：
mkdir /mnt/veracrypt/mysql/data -p

#Nginx 配置路径：
mkdir /mnt/veracrypt/nginx -p

#PHP 配置路径：
mkdir /mnt/veracrypt/phpconf -p

#Redis 数据路径：
mkdir /mnt/veracrypt/redis -p

#站点数据路径：
mkdir /mnt/veracrypt/web -p
```

为后面网络访问通畅，我们为后续要装的这些软件所在容器创建一个公用的 bridge 网络

```
docker network create b1
```

查看网络

```
root@debian:~# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
7c1c2ced15f0        b1                  bridge              local
10fe945000c1        bridge              bridge              local
efb07245d56e        host                host                local
7b1c4ff2d09e        none                null                local
```

# 安装 PHP-FPM

和常规 nginx + php-fpm 部署逻辑一样，先创建一个 php-fpm 容器，稍后再去部署 nginx。

选用镜像，你可以在 https://hub.docker.com/search?q=php&type=image 这里找到你想要的镜像，一般第一条搜索结果是官方的。

我们采用一款第三方镜像，稍微的轻量一点：https://github.com/bitnami/bitnami-docker-php-fpm

下载 git 项目

```
cd ~ && git clone https://github.com/bitnami/bitnami-docker-php-fpm.git --depth=1
```

构建 PHP7.4

```
cd ~/bitnami-docker-php-fpm/7.4-prod/debian-10/ && docker build  -t phpfpm:7.4 .
```

自定义 php 配置

```
cat >/mnt/veracrypt/phpconf/custom.ini <<\EOF
expose_php = Off
date.timezone = PRC
EOF
```

创建 php-fpm 容器

```
docker run -d --name phpfpm-74 -v /mnt/veracrypt/web:/app -v /mnt/veracrypt/phpconf/custom.ini:/opt/bitnami/php/etc/conf.d/custom.ini --network=b1 phpfpm:7.4
```

解释命令：

* -d 后台守护运行
* --name 将容器命名为 phpfpm-74
* -v 映射绑定外部目录和容器内部目录，其中 /app 为容器内默认的站点根目录。
* --network 将其网络绑定到 b1 中。

composer 使用

这个镜像已经内置了 composer2，你可以直接连入容器使用 bash 操作来更新你的项目依赖；

```
docker exec -it phpfpm-74 bash
```

或者直接使用：

```
docker exec -it -v $PWD:/app phpfpm-74 composer install --ignore-platform-reqs
```

设置权限：

之所以将用户改为 daemon 是因为这个 phpfpm 的镜像中，php-fpm.ini 中默认用户是 daemon 。

```
# 容器外
cd /mnt/veracrypt/web && chown -R daemon:daemon . && chmod -R 775 .
# 容器内
cd /app && chown -R daemon:daemon . && chmod -R 775 .
```

# 安装 MySQL

MySQL 采用官方的镜像，参照这里：https://hub.docker.com/\_/mysql

拉取镜像

```
docker pull mysql:5.7
```

创建 MySQL 容器

```
docker run --name mysql --network=b1 -v /mnt/veracrypt/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=your_password -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

解释：

* -e ROOT\_PASSWORD=  将你的密码设置为 your\_password
* -v /mnt/veracrypt/mysql/data:/var/lib/mysql 将你的数据存储在指定位置
* -character-set-server= 及 --collation-server= 指定默认数据库编码
* --network 将其网络绑定到 b1 中。

使用 mysql 命令连接到 mysql 数据库：

```
docker exec -it mysql mysql -uroot -p
# 之后输入你的 mysql 密码就可以了
```

# 安装 Redis

镜像地址：https://hub.docker.com/\_/redis

之前我们创建了 Redis 存放数据的目录，在这里还需要给他创建一个存放配置文件的目录。

```
mkdir /mnt/veracrypt/redis/conf
```

 你可以将你自定义的配置信息写入这个配置文件中，需要什么加什么就行了，配置来源可以参考官网或者稍后进入容器后，将配置复制一份出来用作参考。

比如，我给配置文件增加一项登录密码设定：

```
cat >/mnt/veracrypt/redis/conf/redis.conf <<\EOF
requirepass "redis_password"
EOF
```

这个 Redis 为了在容器之间通信方便，已经关闭网络安全保护，即相当于加上了 protected-mode no 这一项，不限制任何网络的链接，所以当你打算开放 Redis 链接到公网时，更需要设置密码。

创建 Redis 容器

```
docker run --name redis -v /mnt/veracrypt/redis:/data -v /mnt/veracrypt/redis/conf:/usr/local/etc/redis --network=b1 -d redis redis-server  /usr/local/etc/redis/redis.conf --appendonly yes
```

解释：

* -v 绑定数据目录和配置目录。
* --network=b1 将网络连接配置到 b1 网络中
* --appendonly yes 持久化存储，会将你的所有写操作记录到文件，有利于恢复数据，却占文件系统体积。
* /usr/local/etc/redis/redis.conf 启动时指定加载配置文件
* --network 将其网络绑定到 b1 中。

# 安装 Nginx

拉取 nginx 最新镜像：

```
docker pull nginx
```

创建一份临时 nginx 容器获取其 nginx.conf

```
docker run --name tmp-nginx-container -d nginx
docker cp tmp-nginx-container:/etc/nginx/nginx.conf $(pwd)/nginx.conf
docker rm -f tmp-nginx-container
```

查看 nginx.conf ，可以看出他会默认加载 /etc/nginx/conf.d/\*.conf 下的配置文件。

![](https://eller.top/storage/images/YBTtrV14hNyElyaTCw41o1u7lw8PydujNVvunaqj.png)

这样我们待会儿就只需要绑定这个目录到容器中就能自动加载了，为方便修改 nginx.conf，也将其绑定上。

创建站点目录、配置目录：

```
mkdir /mnt/veracrypt/web/default/wwwroot  -p
mkdir /mnt/veracrypt/web/default/log -p
mkdir /mnt/veracrypt/nginx/conf.d -p
mkdir /mnt/veracrypt/nginx/cache -p
```

Nginx 配置文件示例，你可以将其存放到 /mnt/veracrypt/nginx/conf.d/default.conf 中：

```
log_format default.log.format '$remote_addr - $remote_user [$time_local] $request'
        '$status $body_bytes_sent $http_referer '
        '$http_user_agent $http_x_forwarded_for';
server {
        listen       80;
        listen       443 ssl http2;
        server_name default.com;
        index index.html index.htm index.php;
        root  /app/default/wwwroot;

        #/root/.acme.sh/default.com/fullchain.cer
        ssl_certificate      /app/default/fullchain.cer;
        #/root/.acme.sh/default.com/default.com.key
        ssl_certificate_key  /app/default/default.com.key;
        ssl_session_timeout  5m;
        ssl_protocols  TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_protocols TLSv1.1 TLSv1.2;
        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers   on;

        if ($scheme != 'https') {
          rewrite ^ https://$http_host$request_uri? permanent;
        }

        location / {
            try_files $uri $uri/ /index.php?$query_string;
        }

        location ~ .*\.(php|php5)?$ {
            fastcgi_pass    phpfpm-74:9000;
            fastcgi_index index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            fastcgi_param  SCRIPT_NAME $fastcgi_script_name;
            fastcgi_param PHP_ADMIN_VALUE "open_basedir=/tmp/:/proc/:/app/default/wwwroot:$document_root";
            include fastcgi_params;
        }
        access_log  /app/default/log/access.log default.log.format;
        error_log  /app/default/log/error.log;
}
```

重点说明：

phpfpm-74:9000 这里原本是 127.0.0.1:9000 的常规配置，在这里使用之前创建的 php-fpm 时指定的名字就可以在 b1 网络中访问到对应的容器了。

同样，在 b1 网络下任意容器中，都可以通过容器名代替 IP 地址使用。

创建 nginx 容器

```
docker run --name nginx \
-v /mnt/veracrypt/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
-v /mnt/veracrypt/nginx/cache:/var/cache/nginx \
-v /mnt/veracrypt/nginx/conf.d:/etc/nginx/conf.d:ro \
-v /mnt/veracrypt/web:/app \
-p 80:80 -p 443:443 --network=b1 -d nginx
```

如果你在宿主机安装了 acme.sh 可以使用下面的命令：

```
docker run --name nginx \
-v /mnt/veracrypt/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
-v /mnt/veracrypt/nginx/cache:/var/cache/nginx \
-v /mnt/veracrypt/nginx/conf.d:/etc/nginx/conf.d:ro \
-v /mnt/veracrypt/web:/app \
-v ~/.acme.sh:/root/.acme.sh \
-p 80:80 -p 443:443 --network=b1 -d nginx
```

解释：

* --network 将其网络绑定到 b1 中。
* -v 分别绑定了主要 nginx.conf 配置，虚拟主机配置文件目录 conf.d/\*.conf，nginx 的 cache 目录，网站的起始根目录，acme.sh 的脚本目录。
* -p 绑定 80 和 443 端口

# 容器网络

在上面 nginx 的配置过程中，也介绍了可以通过容器名代替 IP 使用，比如 phpfpm-74:9000 替代 127.0.0.1:9000。

同样，在 php 项目的配置文件中填写关于 redis、mysql 的 host 地址信息时，可以用容器名代替，如：

```
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
...
REDIS_HOST=redis
REDIS_PORT=6379
```

测试可以通过 curl

```
curl nginx:80
curl mysql:3306
curl redis:6379
```

# 开机自启

将以上创建的容器更新为开机自启：

```
docker update --restart=always mysql
docker update --restart=always nginx
docker update --restart=always phpfpm-74
docker update --restart=always redis
```

# 计划任务

如果你想执行计划任务，这比以往复杂一点。

建议还是在宿主机调度计划任务，前提也需要将容器运行起来，如果容器挂了那么就会失败。

这里以 laravel 项目的计划任务调度写法举例：

```
* * * * * docker exec -it phpfpm-74 bash -c "cd /app/default/wwwroot && php artisan schedule:run"
```

[取消回复](https://blog.upx8.com/3145#respond-post-3145)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/u...