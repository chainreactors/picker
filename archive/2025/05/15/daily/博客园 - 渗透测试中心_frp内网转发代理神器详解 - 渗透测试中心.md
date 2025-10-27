---
title: frp内网转发代理神器详解 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18875384
source: 博客园 - 渗透测试中心
date: 2025-05-15
fetch_date: 2025-10-06T22:26:58.839550
---

# frp内网转发代理神器详解 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [frp内网转发代理神器详解](https://www.cnblogs.com/backlion/p/18875384 "发布于 2025-05-14 09:39")

### 一、frp 是什么

frp 是一个专注于内网穿透的高性能的反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。可以将内网服务以安全、便捷的方式通过具有公网 IP 节点的中转暴露到公网

### 二、VPS linux服务器端安装服务器端frps

cd  /opt

wget  wget https://github.com/fatedier/frp/releases/download/v0.48.0/frp\_0.48.0\_linux\_amd64.tar.gz

tar  -zxvf   frp\_0.48.0\_linux\_amd64.tar.gz

mv frp\_0.48.0\_linux\_amd64     frp

cd frp

### 三、服务器端frps的frps.ini进行配置

cd frp

vim  frps.ini :

[common]

# frp监听的端口，默认是7000，可以改成其他的

bind\_port = 7000

# HTTP端口

vhost\_http\_port = 54321

# HTTPS端口

vhost\_https\_port = 54322

# 用于身份验证，请自行修改，要保证服务端与客户端一致

token = 123456

# Dashboard (服务端配置)

# frp管理后台端口，请按自己需求更改

dashboard\_port = 7002

# frp管理后台用户名和密码，请改成自己的

dashboard\_user = admin

dashboard\_pwd = admin

enable\_prometheus = true

# frp日志配置

log\_file = /var/log/frps.log

log\_level = info

log\_max\_days = 3

防火墙开放端口

# 添加监听端口

sudo firewall-cmd --permanent --add-port=7000/tcp

# 添加管理后台端口

sudo firewall-cmd --permanent --add-port= 7002/tcp

sudo firewall-cmd --reload

### **四、客服端**frpc的frpc.ini进行配置

**cd frp

vim  frpc.ini :**

[common]

#公网 VPS IP

server\_addr = 106.13.218.47

#外网-服务器端监听的端口(必须与Frps.ini中的配置一致)

server\_port = 7000

# 用于身份验证，请自行修改，要保证服务端与客户端一致

token = 123456

# AdminUI (客户端配置)

# 使用内网真实地址  即可访问测试

admin\_addr = 127.0.0.1

admin\_port = 7400

admin\_user = admin

admin\_pwd = admin

[web]

type = http

local\_ip = 127.0.0.1

local\_port = 80

remote\_port = 54321

custom\_domains = 106.13.218.47       # 建议使用域名进行区分

[mysql]

type = tcp

local\_ip = 127.0.0.1

local\_port = 3306

remote\_port = 9000

[ssh]

#配置类型为tcp协议

type = tcp

#内网机器的IP

local\_ip = 127.0.0.1

#内网机器的端口

local\_port = 22

remote\_port = 9001

[rdp]

type = tcp

local\_ip = 127.0.0.1

local\_port = 3389

remote\_port = 9002

### **五、公网**服务器端frps启动

后台启动frps

nohup ./frps -c ./frps.ini

后台启动frps并输出日志到frps.log

nohup ./frps -c frps.ini 2>&1 > frps.log &

启动的监听日志：

2019/03/23 17:27:41 [I] [service.go:136] frps tcp listen on 0.0.0.0:7000

2019/03/23 17:27:41 [I] [root.go:204] Start frps success

```
则说明服务器端已经启动Frp服务，监听的端口是7000
```

### 六、内网主机启动客户端frpc

#启动linux客户端

./frpc -c ./frpc.ini

#后台启动linux客户端

```
nohup ./frpc -c frpc.ini
```

```
nohup ./frpc -c frpc.ini > frpc.log &
```

#启动windows客户端

frpc.exe    -c ./frpc.ini

### 四、Linux 系统下使用 systemd 控制 frps 及配置开机自启

1.在 /etc/systemd/system 目录下创建一个 frps.service 文件(centos系统下自带systemd服务）

vim /etc/systemd/system/frps.service

frps.service：

[Unit]

# 服务名称，可自定义

Description = frp server

After = network.target syslog.target

Wants = network.target

[Service]

Type = simple

# 启动frps的命令，需修改为您的frps的安装路径

ExecStart = /opt/frp/frps  -c  /opt/frp/frps.ini

[Install]

WantedBy = multi-user.target

4.使用 systemd 命令，管理 frps

# 启动frp

systemctl start frps

# 停止frp

systemctl stop frps

# 重启frp

systemctl restart frps

# 查看frp状态

systemctl status frps

5.配置 frps 开机自启

systemctl enable frps

### 六、代理类型

frp 支持多种代理类型来适配不同的使用场景。

类型    描述

tcp    单纯的 TCP 端口映射，服务端会根据不同的端口路由到不同的内网服务。

udp    单纯的 UDP 端口映射，服务端会根据不同的端口路由到不同的内网服务。

http    针对 HTTP 应用定制了一些额外的功能，例如修改 Host Header，增加鉴权。

https    针对 HTTPS 应用定制了一些额外的功能。

stcp    安全的 TCP 内网代理，需要在被访问者和访问者的机器上都部署 frpc，不需要在服务端暴露端口。

sudp    安全的 UDP 内网代理，需要在被访问者和访问者的机器上都部署 frpc，不需要在服务端暴露端口。

xtcp    点对点内网穿透代理，功能同 stcp，但是流量不需要经过服务器中转。

tcpmux    支持服务端 TCP 端口的多路复用，通过同一个端口访问不同的内网服务

### 七、使用场景

#### 1.通过 SSH 访问内网机器

这个示例通过简单配置 TCP 类型的代理让用户访问到内网的服务器。

1. 在具有公网 IP 的机器上部署 frps，修改 frps.ini 文件，这里使用了最简化的配置，设置了 frp 服务器用户接收客户端连接的端口：

   ```
   [common]
   bind_port = 7000
   ```
2. 在需要被访问的内网机器上（SSH 服务通常监听在 22 端口）部署 frpc，修改 frpc.ini 文件，假设 frps 所在服务器的公网 IP 为 106.13.218.47

   ```
   [common]
   server_addr = 106.13.218.47
   server_port = 7000

   [ssh]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 22
   remote_port = 6000
   ```

   local\_ip 和 local\_port 配置为本地需要暴露到公网的服务地址和端口。remote\_port 表示在 frp 服务端监听的端口，访问此端口的流量将会被转发到本地服务对应的端口。
3. 分别启动 frps 和 frpc

./frps -c ./frps.ini

./frpc -c ./frpc.ini

4.通过 SSH 访问内网机器，假设用户名为 test：

   ssh -oPort=6000 test@x.x.x.x

  5.frp 会将请求 x.x.x.x:6000 的流量转发到内网机器的 22 端口。

#### 2.通过自定义域名访问内网的 Web 服务

这个示例通过简单配置 HTTP 类型的代理让用户访问到内网的 Web 服务。

HTTP 类型的代理相比于 TCP 类型，不仅在服务端只需要监听一个额外的端口 vhost\_http\_port 用于接收 HTTP 请求，还额外提供了基于 HTTP 协议的诸多功能。

1.修改 frps.ini 文件，设置监听 HTTP 请求端口为 8080：

```
[common]
bind_port = 7000
vhost_http_port = 8080
```

2.修改 frpc.ini 文件，假设 frps 所在的服务器的 IP 为106.13.218.47，local\_port 为本地机器上 Web 服务监听的端口, 绑定自定义域名为 custom\_domains。

```
[common]
server_addr = 106.13.218.47
server_port = 7000
```

```
[web]
type = http
local_port = 80
custom_domains = www.yourdomain.com

[web2]
type = http
local_port = 8080
custom_domains = www.yourdomain2.com
```

3.分别启动 frps 和 frpc。

4.将 www.yourdomain.com 和 www.yourdomain2.com 的域名 A 记录解析到 IP 106.13.218.47，如果服务器已经有对应的域名，也可以将 CNAME 记录解析到服务器原先的域名。或者可以通过修改 HTTP 请求的 Host 字段来实现同样的效果。

5.通过浏览器访问 http://www.yourdomain.com:8080 即可访问到处于内网机器上 80 端口的服务，访       问 http://www.yourdomain2.com:8080 则访问到内网机器上 8080 端口的服务。

### 3.转发 DNS 查询请求

这个示例通过简单配置 UDP 类型的代理转发 DNS 查询请求。

DNS 查询请求通常使用 UDP 协议，frp 支持对内网 UDP 服务的穿透，配置方式和 TCP 基本一致。

1. frps.ini 内容如下：

   ```
   [common]
   bind_port = 7000
   ```
2. frpc.ini 内容如下：

   ```
   [common]
   server_addr = x.x.x.x
   server_port = 7000

   [dns]
   type = udp
   local_ip = 8.8.8.8
   local_port = 53
   remote_port = 6000
   ```

   这里反代了 Google 的 DNS 查询服务器的地址，仅仅用于测试 UDP 代理，并无实际意义。
3. 分别启动 frps 和 frpc。

4.通过 dig 测试 UDP 包转发是否成功，预期会返回 www.baidu.com 域名的解析结果。

dig @x.x.x.x -p 6000 www.baidu.com

### 4.转发 Unix 域套接字

```` 这个示例通过配置 Unix域套接字客户端插件来通过 TCP 端口访问内网的 Unix域套接字服务，例如 Docker Daemon。

1. frps.ini 内容如下：

   ```
   [common]
   bind_port = 7000
   ```
2. frpc.ini 内容如下：

   ```
   [common]
   server_addr = x.x.x.x
   server_port = 7000

   [unix_domain_socket]
   type = tcp
   remote_port = 6000
   plugin = unix_domain_socket
   plugin_unix_path = /var/run/docker.sock
   ```
3. 分别启动 frps 和 frpc。 ````

`4.通过 curl 命令查看 docker 版本信息

 curl <http://x.x.x.x:6000/version>`

##### 5.对外提供简单的文件访问服务

这个示例通过配置 static\_file 客户端插件来将本地文件暴露在公网上供其他人访问。

通过 static\_file 插件可以对外提供一个简单的基于 HTTP 的文件访问服务。

1. frps.ini 内容如下...