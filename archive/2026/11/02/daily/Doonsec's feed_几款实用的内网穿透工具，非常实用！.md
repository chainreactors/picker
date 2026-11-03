---
title: 几款实用的内网穿透工具，非常实用！
url: https://mp.weixin.qq.com/s/sxuZPTg1BblY6UAlDEAR2w
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:49:07.725346
---

# 几款实用的内网穿透工具，非常实用！

# 几款实用的内网穿透工具，非常实用！

点击关注 👉
点击关注 👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击“马哥网络安全”，关注，置顶公众号

每日技术干货，第一时间送达！

本文以渗透的视角，总结几种个人常用的内网穿透，内网代理工具，介绍其简单原理和使用方法。

![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=0)

01

nps

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=1)

简介

nps是一款轻量级、高性能、功能强大的内网穿透代理服务器。目前支持tcp、udp流量转发，可支持任何tcp、udp上层协议（访问内网网站、本地支付接口调试、ssh访问、远程桌面，内网dns解析等等……），此外还支持内网http代理、内网socks5代理、p2p等，并带有功能强大的web管理端。

* 一台有公网IP的服务器（VPS）运行服务端（NPS）
* 一个或多个运行在内网的服务器或者PC运行客户端（NPC）

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8Ll2t83r3ichhTqjhCI5cDLGqEVibs4mqJyic5fKy7sLI1tByHiarMnlVy6g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=0)

特点

* Go语言编写
* 支持跨平台
* 支持多种协议的代理
* web管理端

使用方法

https://github.com/ehang-io/nps/releases

NPS安装配置

找到自己服务器相应版本的server：

```
cd ~wget https://github.com/cnlh/nps/releases/download/v0.23.2/linux_amd64_server.tar.gztar xzvf linux_amd64_server.tar.gzcd ~/nps
```

在nps目录下面会有一个nps可执行文件、conf配置目录和web网页目录，我们只需要修改conf/nps.conf即可：

```
vim conf/nps.conf
```

需要改一下#web下面的几个参数，

```
web_host= 服务器IP或者域名web_username= admin（登录用户名）web_password= 你的密码web_port=8080（web管理端口）
```

修改#bridge 可以更改 NPC的连接端口。比如我们拿到一台权限受限的服务器，有防火墙，可能只有部分端口（80，443）可以出网，就需要修改成出网端口。

```
##bridgebridge_type=tcpbridge_port=443  # 修改连接端口bridge_ip=0.0.0.0
```

##### 启动

```
#Mac/Linux./nps test|start|stop|restart|status 测试配置文件|启动|停止|重启|状态
```

```
#Windowsnps.exe test|start|stop|restart|status 测试配置文件|启动|停止|重启|状态
```

##### NPC

```
./npc -server=你的IP:8024 -vkey=唯一验证密码 -type=tcp
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8Lk1hia7lksdb4ibtp550JgYibtPvpjLs4X6tfBYCNmS9iaRcrQE5iajPn5icQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=1)

新建好客户端后，也可以在+中看到，详细的客户端连接命令：

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8LH6AL4N8KRfQwicxichNib4JjxNljN7LCTyxt0rQib0j28KkO1Mfm18iazng/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=2)

web管理端

在客户端界面可以通过新增的方式添加客户端连接，每一个连接的vkey都是唯一区分的。

每一个客户端，在建立连接后，都可以建立多个不同协议的隧道，这一个个隧道就是不同的代理了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8LTBlGydq1eaU5dlw8iaP0XXQPt97Gsqa2fuXuEH6zK8KqTSWuWyUBtEQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=3)

通过不同的协议和端口就可以连接代理的内网机器。

![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=6)

02

frp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=7)

简介

frp 是一个专注于内网穿透的高性能的反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。可以将内网服务以安全、便捷的方式通过具有公网 IP 节点的中转暴露到公网。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8L6hVfFSHbfmn9FkPiagLG5aibOXxNHfZfLfU6LkEUzW3qwYGmic5L7vPng/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=4)

特点

* 客户端服务端通信支持 TCP、KCP 以及 Websocket 等多种协议。
* 端口复用，多个服务通过同一个服务端端口暴露。
* 跨平台，但是支持的比nps少一点
* 多种插件，提供很多功能

使用方法

下载：https://github.com/fatedier/frp/releases

以下内容摘自：https://segmentfault.com/a/1190000021876836

* 通过 rdp 访问家里的机器

1、修改 frps.ini 文件，为了安全起见，这里最好配置一下身份验证，服务端和客户端的 common 配置中的 token 参数一致则身份验证通过：

```
# frps.ini[common]bind_port = 7000# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh
```

2、启动 frps：

```
./frps -c ./frps.ini
```

3、修改 frpc.ini 文件，假设 frps 所在服务器的公网 IP 为 x.x.x.x：

```
# frpc.ini[common]server_addr = x.x.x.xserver_port = 7000# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh[rdp]type = tcplocal_ip = 127.0.0.1local_port = 3389remote_port = 6000
```

4、启动 frpc：

```
./frpc -c ./frpc.ini
```

5、通过 rdp 访问远程的机器，地址为：

```
x.x.x.x:6000
```

* 开机自启

针对 Windows 系统，为了便于使用，可以配置一下开机的时候静默启动。

1、在 frpc.exe 的同级目录创建一个 start\_frpc.vbs：

```
start_frpc.vbs'请根据实际情况修改路径'CreateObject("WScript.Shell").Run """D:\Program Files\frp_windows_amd64\frpc.exe""" & "-c" & """D:\Program Files\frp_windows_amd64\frpc.ini""",0
```

2、复制 start\_frpc.vbs 文件，打开以下目录，注意将

```
<USER_NAME>
```

改为你的用户名：

```
C:\Users\<USER_NAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

3、鼠标右击，粘贴为快捷方式即可。

* 通过 SSH 访问公司内网机器

frps 的部署步骤同上。

4、启动 frpc，配置如下：

```
# frpc.ini[common]server_addr = x.x.x.xserver_port = 7000# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh[ssh]type = tcplocal_ip = 127.0.0.1local_port = 22remote_port = 6000
```

5、通过 SSH 访问内网机器，假设用户名为 test：

```
ssh -oPort=6000 test@x.x.x.x
```

6、通过自定义域名访问部署于内网的 Web 服务

有时想要让其他人通过域名访问或者测试我们在本地搭建的 Web 服务，但是由于本地机器没有公网 IP，无法将域名解析到本地的机器，通过 frp 就可以实现这一功能，以下示例为 http 服务，https 服务配置方法相同， vhost*http*port 替换为 vhost*https*port， type 设置为 https 即可。

1.修改 frps.ini 文件，设置 http 访问端口为 8080：

```
# frps.ini[common]bind_port = 7000vhost_http_port = 8080# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh
```

2.启动 frps：

```
./frps -c ./frps.ini
```

3.修改 frpc.ini 文件

假设 frps 所在的服务器的 IP 为 x.x.x.x，local\_port 为本地机器上 Web 服务对应的端口， 绑定自定义域名 www.yourdomain.com:

```
# frpc.ini[common]server_addr = x.x.x.xserver_port = 7000# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh[web]type = httplocal_port = 80custom_domains = www.yourdomain.com
```

4.启动 frpc：

```
./frpc -c ./frpc.ini
```

5.将 www.yourdomain.com 的域名 A 记录解析到 IP x.x.x.x，如果服务器已经有对应的域名，也可以将 CNAME 记录解析到服务器原先的域名。

6.通过浏览器访问 http://www.yourdomain.com:8080 即可访问到处于内网机器上的 Web 服务。

对外提供简单的文件访问服务

通过 static\_file 插件可以对外提供一个简单的基于 HTTP 的文件访问服务。

frps 的部署步骤同上。

1.启动 frpc，启用 static\_file 插件，配置如下：

```
# frpc.ini[common]server_addr = x.x.x.xserver_port = 7000# 用于身份验证，请自行修改，要保证服务端与客户端一致token = abcdefgh[test_static_file]type = tcpremote_port = 6000plugin = static_file# 要对外暴露的文件目录plugin_local_path = /tmp/file# 访问 url 中会被去除的前缀，保留的内容即为要访问的文件路径plugin_strip_prefix = staticplugin_http_user = abcplugin_http_passwd = abc
```

2.通过浏览器访问 http://x.x.x.x:6000/static/ 来查看位于 /tmp/file 目录下的文件，会要求输入已设置好的用户名和密码。

常用功能

##### 统计面板（Dashboard）

通过浏览器查看 frp 的状态以及代理统计信息展示。

注：Dashboard 尚未针对大量的 proxy 数据展示做优化，如果出现 Dashboard 访问较慢的情况，请不要启用此功能。

需要在 frps.ini 中指定 dashboard 服务使用的端口，即可开启此功能：

```
[common]dashboard_port = 7500# dashboard 用户名密码，默认都为 admindashboard_user = admindashboard_pwd = admin
```

打开浏览器通过 http://[server\_addr]:7500 访问 dashboard 界面，用户名密码默认为 admin。

##### 加密与压缩

这两个功能默认是不开启的，需要在 frpc.ini 中通过配置来为指定的代理启用加密与压缩的功能，压缩算法使用 snappy：

```
# frpc.ini[ssh]type = tcplocal_port = 22remote_port = 6000use_encryption = trueuse_compression = true
```

如果公司内网防火墙对外网访问进行了流量识别与屏蔽，例如禁止了 SSH 协议等，通过设置 use\_encryption = true，将 frpc 与 frps 之间的通信内容加密传输，将会有效防止流量被拦截。

如果传输的报文长度较长，通过设置 use\_compression = true 对传输内容进行压缩，可以有效减小 frpc 与 frps 之间的网络流量，加快流量转发速度，但是会额外消耗一些 CPU 资源。

##### TLS

从 v0.25.0 版本开始 frpc 和 frps 之间支持通过 TLS 协议加密传输。通过在 frpc.ini 的 common 中配置 tls\_enable = true 来启用此功能，安全性更高。

为了端口复用，frp 建立 TLS 连接的第一个字节为 0x17。

注意：启用此功能后除 xtcp 外，不需要再设置 use\_encryption。

##### 代理限速

目前支持在客户端的代理配置中设置代理级别的限速，限制单个 proxy 可以占用的带宽。

```
# frpc.ini[ssh]type = tcplocal_port = 22remote_port = 6000bandwidth_limit = 1MB
```

在代理配置中增加 bandwidth\_limit 字段启用此功能，目前仅支持 MB 和 KB 单位。

##### 范围端口映射

在 frpc 的配置文件中可以指定映射多个端口，目前只支持 tcp 和 udp 的类型。

这一功能通过 range: 段落标记来实现，客户端会解析这个标记中的配置，将其拆分成多个 proxy，每一个 proxy 以数字为后缀命名。

例如要映射本地 6000-6005, 6007 这 6 个端口，主要配置如下：

```
# frpc.ini[range:test_tcp]type = tcplocal_ip = 127.0.0.1local_port = 6000-6006,6007remote_port = 6000-6006,6007
```

实际连接成功后会创建 8 个 proxy，命名为 test*tcp*0, test*tcp*1 ... test*tcp*7。

![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=9)

03

ew

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=10)

简介

EW 是一套便携式的网络穿透工具，具有 SOCKS v5服务架设和端口转发两大核心功能，可在复杂网络环境下完成网络穿透。但是，现在工具已经不更新了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YscRq4LT5WvP12Ams5drTS6DqKzJHR8LictYyw6ZXuWs5cMXuoKhIqHfxy8WzbvlTCF5ze4yTkacYggC0ICxSBQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=5...