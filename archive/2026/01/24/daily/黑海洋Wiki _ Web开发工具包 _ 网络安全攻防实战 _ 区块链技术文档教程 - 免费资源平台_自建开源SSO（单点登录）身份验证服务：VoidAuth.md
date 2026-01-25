---
title: 自建开源SSO（单点登录）身份验证服务：VoidAuth
url: https://blog.upx8.com/1346
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-01-24
fetch_date: 2026-01-25T03:56:13.865796
---

# 自建开源SSO（单点登录）身份验证服务：VoidAuth

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 自建开源SSO（单点登录）身份验证服务：VoidAuth

发布时间:
2026-01-24 New Article

分类:
[程序开发/Code](https://blog.upx8.com/code)

热度:
5098

VoidAuth是一款开源的SSO身份验证和用户管理软件，可为您的自托管应用程序保驾护航，并支持诸多实用功能，例如Passkey登录、邀请注册、自助注册、电子邮件支持等等。

VoidAuth特点（摘自项目文档）：

> 🌐 OpenID Connect (OIDC) Provider
> 🔄 Proxy ForwardAuth
> 👤 User and Groups Management
> 📨 User Self-Registration and Invitations
> 🎨 Customizable (Logo, Title, Theme Color, Email Templates)
> 🔑 Multi-factor Authentication, Passkeys, and Passkey-Only Accounts
> 📧 Secure Password Reset with Email Verification
> 🔒 Encryption-At-Rest with Postgres or SQLite Database

其实类似VoidAuth这样开源并且支持自建的SSO程序有很多，在接触VoidAuth之前，我部署过很多个，这里就不详细说了。我只想简单谈一下个人体验，我用过的这些软件里面或多或少都有这样的问题：安装和配置非常复杂、程序本身设计的过于臃肿，对于个人自托管爱好者而言（个人用户），甚至有很多用不到的功能，而VoidAuth完美的解决了上述问题，它非常轻量且易于使用。

VoidAuth最让我觉得好用的一个功能是ProxyAuth（转发认证），我自建的这些服务里面并不是所有都原生支持OIDC的，对于那些不支持OIDC的应用程序，我现在可以通过ProxyAuth来实现SSO，真正做到了一个账号登录所有服务。

这篇文章记录下VoidAuth安装以及OIDC、ProxyAuth的配置。

安装Docker：

```
apt -y update
apt -y install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

创建目录新建compose文件：

```
mkdir /opt/voidauth && cd /opt/voidauth && nano docker-compose.yml
```

写入如下内容：

```
services:
  voidauth:
    image: voidauth/voidauth:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:3001:3001"
    volumes:
      - ./voidauth/config:/app/config
    environment:
      APP_URL: https://voidauth.example.com # 设置你的域名
      APP_PORT: 3001
      STORAGE_KEY: JW8G+gr2sa8vuStV2F/6rR7VeqvarijvogwvE8jIDD0= # 使用openssl rand -base64 32命令生成
      DB_PASSWORD: yourdbpassword # 设置数据库密码
      DB_HOST: voidauth-db
      SIGNUP: false
      SIGNUP_REQUIRES_APPROVAL: true
      ENABLE_DEBUG: false
    depends_on:
      voidauth-db:
        condition: service_healthy

  voidauth-db:
    image: postgres:18
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: yourdbpassword # 设置数据库密码
    volumes:
      - db:/var/lib/postgresql/18/docker
    healthcheck:
      test: "pg_isready -U postgres -h localhost"

volumes:
  db:
```

启动：

```
docker compose up -d
```

默认的管理员账号与密码可通过查看容器日志获取：

```
docker compose logs -f
```

注：仅容器第一次启动会输出管理员账号与密码，后续不再显示，务必保存好。

配置Ferron反向代理：

```
nano /etc/ferron.kdl
```

写入如下内容：

```
voidauth.example.com {
   header "Access-Control-Allow-Origin" "*"
   proxy "http://127.0.0.1:3001/"
}
```

重载Ferron：

```
systemctl reload ferron
```

现在来配置ProxyAuth，让不支持OIDC的服务接入VoidAuth，实现单点登录。开始前先简单介绍一下这个功能是怎么实现的。

我现在的自托管环境，基本都是用Docker启动的服务，直接暴露服务的地址和端口，例如：127.0.0.1:5030，然后通过主机的Web Server反向代理127.0.0.1:5030，实现域名绑定、SSL证书申请、服务对外的发布（公网访问）。

VoidAuth的ProxyAuth其实就是ForwardAuth（转发认证），这个功能是需要与反向代理配合使用的，也就是说需要Web Server软件支持才行。我们配置Web Server，让服务在公网访问的时候先跳转到VoidAuth进行身份认证，认证完成后再跳转回源服务，这就是大致的流程。

现在主流的NGINX、Caddy、Traefik Web Server都是支持ForwardAuth的，如果您使用的是这类软件，可以参考[VoidAuth官方的文档](https://blog.upx8.com/go/aHR0cHM6Ly92b2lkYXV0aC5hcHAvIy9Qcm94eUF1dGgtYW5kLVRydXN0ZWQtSGVhZGVyLVNTTy1TZXR1cA)来配置。我目前使用的是Ferron Web Server，官方没有相应的文档，所以这里我只记录与Ferron相关的内容。

编辑Ferron配置文件：

```
nano /etc/ferron.kdl
```

加入如下配置，建议直接配置在全局（\*）：

```
* {
    trust_x_forwarded_for #true
}
```

根据[Ferron 2.2.1版本的发布记录](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZlcnJvbndlYi9mZXJyb24vcmVsZWFzZXMvdGFnLzIuMi4x)可以得知，这将让Ferron在默认情况下信任“X-Forwarded-For”标头，且不再覆盖X-Forwarded-Host、X-Forwarded-Proto标头，这个配置非常关键，没有这个配置Ferron将无法与VoidAuth配合使用。

假设我要保护的服务域名是：slskd.example.com，写入如下配置：

```
slskd.example.com {
   auth_to "https://voidauth.example.com/api/authz/forward-auth"
   auth_to_no_verification #false
   auth_to_copy "Remote-User" "Remote-Email" "Remote-Name" "Remote-Groups"
   proxy "http://127.0.0.1:5030/"
}
```

重载Ferron使新配置生效：

```
systemctl reload ferron
```

在VoidAuth添加需要保护的服务域名：slskd.example.com：

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_15-06-35.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_15-06-35.png)

这样就配置好了，是不是特别简单，当用户访问slskd.example.com时，会先跳转到VoidAuth进行身份认证。

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-16-55.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-16-55.png)

现在简单介绍一下OIDC的配置，您在VoidAuth的管理员后台点击OIDC Apps，可以查看对接服务需要用到的各种OIDC Endpoints：

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-19-57.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-19-57.png)

然后您可以在VoidAuth的管理员后台创建一个OIDC App，这里我以[Arcane Docker容器管理平台](https://blog.upx8.com/go/aHR0cHM6Ly9sYWxhLmltLzk5MzguaHRtbA)为例：

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-21-44.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-21-44.png)

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-22-55.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-22-55.png)

Arcane配置：

[![自建开源SSO（单点登录）身份验证服务：VoidAuth](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-28-59.png)](https://i0.wp.com/lala.im/wp-content/uploads/2026/01/2026-01-12_16-28-59.png)

这里需要注意的是适用范围需要加上：groups，管理员声明需要配置为：groups，值配置为：auth\_admins。因为我没有在VoidAuth创建新的管理员账号，默认的管理员账号（auth\_admin）所属的组就是auth\_admins，这样配置就可以让您以管理员的身份通过OIDC登录到Arcane。

最后，也许您可以看看[VoidAuth官方的文档](https://blog.upx8.com/go/aHR0cHM6Ly92b2lkYXV0aC5hcHAvIy9PSURDLUd1aWRlcw)，他们提供了众多服务的OIDC接入指南可供参考。

[取消回复](https://blog.upx8.com/1346#respond-post-5403)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")