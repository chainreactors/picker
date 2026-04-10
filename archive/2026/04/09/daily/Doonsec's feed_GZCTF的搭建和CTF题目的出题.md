---
title: GZCTF的搭建和CTF题目的出题
url: https://mp.weixin.qq.com/s/Z9t4H39-cCGloPxaZPs-1g
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:42:16.844766
---

# GZCTF的搭建和CTF题目的出题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dribnicsKeGgfGp3bFNVpyKm47Pn5CyXicLlVQHKN8I0P3icaYEu9sKuJqUeaIlMuWUHqxebGeVHbnEJoEsWXqtaue8yiaZeianxhT9YGic0We2Gtk/0?wx_fmt=jpeg)

# GZCTF的搭建和CTF题目的出题

三社院信息Sec
三社院信息Sec

三社院信息Sec

![]()

在小说阅读器中沉浸阅读

写的如果不好见谅，作者水平有限

项目地址

https://github.com/GZTimeWalker/GZCTF

平台配置手册 地址:快速上手

https://gzctf.gzti.me/zh/guide/start/quick-start.html

GZCTF是docker搭建的

## 下载docker

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
systemctl enable docker
systemctl start docker
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGge61tAMLwgoorg23yURYTVOCeru1IdI72gW324ibtiauY4tzJMkg4d5VViaB4seQvzTEkOkEGHZmia5h4XeSIlqZQydb1eJc25DF1M/640?wx_fmt=png&from=appmsg)

## 创建 GZCTF 目录及配置文件和邮箱验证

可以不用邮箱

我用的是QQ邮箱的STMP服务 可以自己开启就行了 不建议使用SMTP，可以用腾讯云的阿里云服务器里面的邮件推送服务，反正QQ那个SMTP就前面几次可以发送成功后面直接就不行了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcgfT8arHtKG7kFTEDuoRGW0lsHRNeSu2BDCmISzFdwFs2ejf3dbQlWazzau3AsOkwm2XOdQPc9ibOEWiaUUYHXAYc1JWzaGLfxg/640?wx_fmt=png&from=appmsg)

```
mkdir -p /opt/gzctf
cd /opt/gzctf
```

创建 `appsettings.json` 文件

在终端输入 `nano appsettings.json` 我开的有邮箱验证用的QQ的

```
{
  "AllowedHosts": "*",
"ConnectionStrings": {
    "Database": "Host=db:5432;Database=gzctf;Username=postgres;Password=<你的数据库密码>"
  },
"EmailConfig": {
    "SenderAddress": "<发件人邮箱地址>",
    "SenderName": "<发件人显示名称>",
    "UserName": "<SMTP用户名>",
    "Password": "<SMTP授权码/密码>",
    "Smtp": {
      "Host": "<SMTP服务器地址>",
      "Port": 465
    }
  },
"XorKey": "<用于加密题目私钥的随机字符串>",
"ContainerProvider": {
    "Type": "Docker", // 容器后端类型：可选 Docker 或 Kubernetes
    "PortMappingType": "Default", // 端口映射模式：可选 Default 或 PlatformProxy
    "EnableTrafficCapture": false, // 是否启用流量抓取
    "PublicEntry": "<服务器公网IP或域名>", // 选手访问题目容器的入口地址
    "DockerConfig": {
      "Uri": "unix:///var/run/docker.sock" // Docker 守护进程连接路径
    }
  },
"CaptchaConfig": {
    "Provider": "None", // 验证码类型：可选 None, CloudflareTurnstile 或 HashPow
    "SiteKey": "<验证码 SiteKey>",
    "SecretKey": "<验证码 SecretKey>"
  },
"ForwardedOptions": {
    "ForwardedHeaders": 7,
    "ForwardLimit": 1,
    "KnownIPNetworks": ["192.168.12.0/8"] // 信任的反向代理内网段
  }
}
```

保存并退出：按 Ctrl+O回车保存，然后按 Ctrl+X退出

创建 `nano compose.yml`

```
services:
  gzctf:
    image: registry.cn-shanghai.aliyuncs.com/gztime/gzctf:develop
    restart: always
    environment:
      - "GZCTF_ADMIN_PASSWORD=<你的初始管理员密码>"# 数据库未初始化时的首个管理员密码
      - "LC_ALL=zh_CN.UTF-8"# 平台语言设置，默认为中文
    ports:
      - "80:8080"# 将容器 8080 端口映射到宿主机 80 端口
    volumes:
      - "./data/files:/app/files"# 题目附件及静态文件存储目录
      - "./appsettings.json:/app/appsettings.json:ro"# 挂载配置文件（只读）
      - "/var/run/docker.sock:/var/run/docker.sock"# 允许平台控制宿主机 Docker 环境
    depends_on:
      - db # 确保数据库服务优先启动

  db:
    image: postgres:alpine
    restart: always
    environment:
      - "POSTGRES_PASSWORD=<你的数据库密码>"# 须与 appsettings.json 中的密码保持一致
    volumes:
      - "./data/db:/var/lib/postgresql"# 数据库数据持久化目录
```

配置好了启动就行

```
docker compose up -d
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcT1htJEZkwv0eJw04NjfRzlqnmHa9lcqvFqTCJRq6l3ReA2lFNxiamDYtLFnftWCia9podkRZiaRLMBkvBc7HV5ytMzkiaM8r785U/640?wx_fmt=png&from=appmsg)

有问题阿里云镜像加速

```
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker.m.daocloud.io",
    "https://dockerhub.icu",
    "https://registry.cn-hangzhou.aliyuncs.com"
  ]
}
EOF
systemctl daemon-reload
systemctl restart docker
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcFegEwFXw4xzknzkVVfEeZQzZCE1XJ74kojUXX5zJvpvL2QErM4V0U02tlckZxOMPVudm0k5XVJjETc8qnYmgC98KbQRSJ3p0/640?wx_fmt=png&from=appmsg)

需要开启系统的网络转发功能

```
sudo sysctl -w net.ipv4.ip_forward=1
```

强制防火墙放行 Docker 的流量

```
sudo iptables -P FORWARD ACCEPT
```

成功 访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgeO3IYU11F16ag7FpLLFFAniaHzmbSFHhRaj5ygHKxNWcNFpOFNmG2iaabu9WGYaTVKiaz4gRRqPbablPK1wibLrZ2tqicMmtTuryiaE/640?wx_fmt=png&from=appmsg)

然后用设置的管理员登录就行

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgc9ibiaJsQ8ibf6dcbwGT4H7WERIdeB4PEeloM2rqfwM9A4PZuISzQk9AlFfXvAwB22ibtI2hO2PXzhX5enp13ynRrFZu5VscmKibzg/640?wx_fmt=png&from=appmsg)

开启邮箱验证  就可以发邮箱验证了

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgcx62MYWpvbCjqUmac55H8R3Y7RTAGfjYKf3s7JkkgA2jvAozRmyCqeFHJPgpofDMgdMZjoLFciaHJibLvPRBou2tqKRQziaAVkHI/640?wx_fmt=png&from=appmsg)

不建议用STMP 不知道什么情况一直出现问题 后面我就禁用邮件验证了

## 验证码

个人用不到

可以用cloudflare 官网Cloudflare Dashboard | Manage Your Account

修改appsettings

```
"CaptchaConfig": {
    "Provider": "CloudflareTurnstile",
    "SiteKey": "key",
    "SecretKey": "key",
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfmWA9U0yf3VqBFG0iaPibh79R2ljvO5EGZLOun8N09OXkP71zd1rcJsLasyUj40nlicO5WIQzuUBc7qCmhhiaiayGvHJUa4BfLQuIc/640?wx_fmt=png&from=appmsg)

## Web出题和动态 flag

GZCTF动态flag 变量是GZCTF\_FLAG

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgd5wLdtuZJV1HhKJ0zAd8kf0E3sGG0WicBxG0BUs9SibW250gBof38DDRTY5le5r1EuWkUrSyvIeFsnSs9pVybGhrcChLJ1lhNMY/640?wx_fmt=png&from=appmsg)

动态 flag 的核心逻辑是：**平台在启动题目容器时，会将 flag 注入到环境变量 `GZCTF_FLAG` 中。** 写一个启动脚本（`flag.sh`），在容器启动的一瞬间，把这个环境变量里的值写到文件里或者数据库里就行

随便写一下题目

目录结构

```
/opt/ctf/
├── Dockerfile
├── flag.sh
└── src/
    └── index.php
```

index.php (题目源码)

这是题目页面。出题逻辑是：在页面源码中预留一个占位符，启动容器时由脚本动态替换

```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Web 签到</title>
</head>
<body>
    <h1>Welcome to GZCTF</h1>
    <p>这是一道签到题，你的 flag 是：</p>
    <code>{{FLAG}}</code>
</body>
</html>
```

flag.sh (启动脚本)

这个脚本负责“动态注入”。GZCTF 分配 flag 时会写入 `$GZCTF_FLAG` 环境变量。

```
#!/bin/sh

# 1. 接收动态变量，若平台未下发则使用默认值 flag{sanjiu}
export FLAG=${GZCTF_FLAG:-flag{sanjiu}}

# 2. 将源码中的占位符替换为真实 Flag
sed -i "s/{{FLAG}}/$FLAG/g" /var/www/html/index.php

# 3. 彻底销毁环境变量，防止选手通过 /proc/1/environ 或 phpinfo() 提权/非预期读取
unset GZCTF_FLAG
unset FLAG

# 4. 启动 Apache 服务并接管主进程
exec apache2-foreground
```

Dockerfile

这里使用了阿里云镜像源。

```
# 基础镜像使用官方 PHP-Apache
FROM php:7.4-apache

# 替换 Debian 软件源为阿里云源，加速后续可能需要的扩展安装
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# 拷贝 Web 源码到 Apache 默认目录
COPY src/ /var/www/html/

# 拷贝并配置启动脚本
COPY flag.sh /flag.sh
RUN chmod +x /flag.sh

# 暴露 80 端口供平台映射
EXPOSE 80

# 指定容器启动命令
CMD ["/flag.sh"]
```

**构建镜像**：

```
docker build -t web .
```

有问题改一下全局配置

配置多个国内目前还存活的加速源

```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker.m.daocloud.io",
    "https://docker.nyist.machengqiang.com"
  ]
}
EOF
```

重启 Docker 服务让配置生效

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdGKriccv2FzmBumKHYo7b0QSyaGvQVuuokmdN7XxocMFAaGKd6ib3TLshD3XXLP9a5NxMaQlpdrQQpCE6ZicNGH3xBRCZhrtwqnI/640?wx_fmt=png&from=appmsg)

创建题目动态flag

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeNmuPhzyNFeDXZhMWNTK7bicGKId6AjoExjHibBBnCe7Vmj2nfRI9TbquxpS5UupAf4aqoXibUImXQMoPhTAXuEFSPibO93SlSicVU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgckbRR1QRWmtIh4ECxLqh7JyCDPggJghdIYEFzA00ZoaGpEylYohp8qmouFMVd52Dv6RssO0tZMRWm5q0xMKTnSU3C9pDjmWyU/640?wx_fmt=png&from=appmsg)

我暴露的是80端口直接用80端口就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgd4Nr6tqhqJrnNRJcldZuI0dmDFfsbmlrTQia1Uic7ScRwKicCaz6KiaUEoyvibk1saibialK6oEF631Ur1ib5LfZHTBrU4Rf5SUfDxc8c/640?wx_fmt=png&from=appmsg)

设置

```
flag{[GUID]} #不一定是flag 也可以是 CTF{[GUID]}
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGge6zW43PIC23H7SuPXr2IjzVfEaNKosoMVncHYZx1yE79f99EURo2yLLPF9oQBzmKibzAhx7WA0fckgvnvWtLLO6mgTic3Sq7jGw/640?wx_fmt=png&from=appmsg)

你就会发现是动态flag了

## Pwn的出题和动态flag

简单编写一个简单的 C 程序（执行 `/bin/sh`），并使用 `socat` 将其绑定到 80 端口上来实现。

目录结构

```
pwn/
├── Dockerfile
├── flag.sh
└── src/
    └── pwn.c
```

pwn.c

简单的 pwn 签到源码，作用是直接弹出一个 shell。注意：pwn 题必须关闭 I/O 缓冲，否则通过网络连接时会无法正常输入输出。

```
#include <stdio.h>
#include <stdlib.h>

int main() {
    // 关闭 I/O 缓冲（防止网络截断）
    se...