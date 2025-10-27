---
title: Pwn2Own Austin 2021 Cisco RV34x RCE 漏洞链复现
url: https://www.secpulse.com/archives/197154.html
source: 安全脉搏
date: 2023-03-08
fetch_date: 2025-10-04T08:52:33.049676
---

# Pwn2Own Austin 2021 Cisco RV34x RCE 漏洞链复现

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Pwn2Own Austin 2021 Cisco RV34x RCE 漏洞链复现

[漏洞复现](https://www.secpulse.com/archives/category/articles/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-07

11,363

* 前言
* 固件解压
* 漏洞分析

+ CVE-2022-20705 Improper Session Management Vulnerability
+ CVE-2022-20707 Command Injection

* 参考链接

## 前言

这个**RCE漏洞利用链**的实现是由几个逻辑洞的结合而导致的，这几天我花了一些时间复现了一遍，在此记录一下。

## 固件解压

我下载的是 **RV345 v1.0.03.24**，从官网下载到压缩包解压之后可以看到它的 **rootfs** 是 **ubi** 格式的 **img**。之前我都是使用 **kali**里的 binwalk 对其进行解压可以直接得到解压之后的文件系统。但是由于前几天我的虚拟机坏了，不得不进行重装，但是我还没有装 kali。故找了一下提取 **ubi** 格式的方式。在 **github** 上有一个项目：https://github.com/nlitsme/ubidump，通过里面的 **ubidump.py** 可以很轻松地提取出 **ubi** 格式的文件。命令如下：

```
python3 ubidump.py -s . 0.ubi
```

## 漏洞分析

### CVE-2022-20705 Improper Session Management Vulnerability

**CVE-2022-20705 Improper Session Management Vulnerability**，是由于 **nginx** 的配置不当导致的。**nginx** 的配置文件是 **/etc/nginx/nginx.conf**，如下

```
user www-data;
worker_processes  4;

error_log /dev/null;

events {
    worker_connections  1024;
}

http {
	access_log off;
	#error_log /var/log/nginx/error.log  error;

	upstream jsonrpc {
		server 127.0.0.1:9000;
	}

	upstream rest {
		server 127.0.0.1:8008;
	}

	# For websocket proxy server
	include /var/nginx/conf.d/proxy.websocket.conf;
	include /var/nginx/sites-enabled/*;
}
```

可以发现它又加载了: **/var/nginx/conf.d/proxy.websocket.conf 和 /var/nginx/sites-enabled/** ，但是固件解压出来的 rootfs 里的 var 目录有些问题，所以笔者只能根据别人的文章找一下漏洞发生的配置文件。结合 **rest.url.conf** 和 **proxy.conf** 来看。

```
location /api/ {
        proxy_pass http://rest;
        include /var/nginx/conf.d/proxy.conf;
}

location /api/operations/ciscosb-file:file-copy {
	proxy_pass http://rest;
	include /var/nginx/conf.d/proxy.conf;
	proxy_read_timeout 3600;
	proxy_send_timeout 3600;
}

location /api/operations/ciscosb-file:form-file-upload {
	set $deny 1;

	if ($http_authorization != "") {
		set $deny "0";
	}

	if ($deny = "1") {
		return 403;
	}

	upload_pass /form-file-upload;
	upload_store /tmp/upload;
	upload_store_access user:rw group:rw all:rw;
	upload_set_form_field $upload_field_name.name "$upload_file_name";
	upload_set_form_field $upload_field_name.content_type "$upload_content_type";
	upload_set_form_field $upload_field_name.path "$upload_tmp_path";
	upload_aggregate_form_field "$upload_field_name.md5" "$upload_file_md5";
	upload_aggregate_form_field "$upload_field_name.size" "$upload_file_size";
	upload_pass_form_field "^.*$";
	upload_cleanup 400 404 499 500-505;
	upload_resumable on;
}

location /restconf/ {
        proxy_pass http://rest;
        include /var/nginx/conf.d/proxy.conf;
}

location /restconf/operations/ciscosb-file:file-copy {
        proxy_pass http://rest;
        include /var/nginx/conf.d/proxy.conf;
        proxy_read_timeout 3600;
        proxy_send_timeout 3600;
}
```

```
proxy_http_version 1.1;
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header Authorization $http_authorization;
proxy_set_header Accept-Encoding "";
proxy_set_header Connection "";
proxy_ssl_session_reuse off;
server_name_in_redirect off;
```

如果我们请求中 **Authorization** 不为空，此时 set $deny "0"，就可以向下调用 **upload** 模块。它会在调用 **/form-file-upload**前，把文件上传到 **/tmp/upload** 下。并且由于没有设置 **level**，它的存储格式类似 **/tmp/upload/0000000001**。至此我们可以实现任意文件上传至 **/tmp/upload**。

我们接着向下分析，可以在 **rootfs/etc/nginx/conf.d** 下找到 **web.upload.conf** 如下：

```
location /form-file-upload {
	include uwsgi_params;
	proxy_buffering off;
	uwsgi_modifier1 9;
	uwsgi_pass 127.0.0.1:9003;
	uwsgi_read_timeout 3600;
	uwsgi_send_timeout 3600;
}

location /upload {
	set $deny 1;

        if (-f /tmp/websession/token/$cookie_sessionid) {
                set $deny "0";
        }

        if ($deny = "1") {
                return 403;
        }

	upload_pass /form-file-upload;
	upload_store /tmp/upload;
	upload_store_access user:rw group:rw all:rw;
	upload_set_form_field $upload_field_name.name "$upload_file_name";
	upload_set_form_field $upload_field_name.content_type "$upload_content_type";
	upload_set_form_field $upload_field_name.path "$upload_tmp_path";
	upload_aggregate_form_field "$upload_field_name.md5" "$upload_file_md5";
	upload_aggregate_form_field "$upload_field_name.size" "$upload_file_size";
	upload_pass_form_field "^.*$";
	upload_cleanup 400 404 499 500-505;
	upload_resumable on;
}
```

我们可以发现其对 **/upload** 进行了 **$cookie\_sessionid** 的检验，但是并没有对 **/form-file-upload** 进行检验。我们看一下 **/form-file-upload** 的后端处理程序。启动脚本 (uwsgi-launcher) 如下：

```
#!/bin/sh /etc/rc.common

export UWSGI_PLUGIN_DIR=/usr/lib/uwsgi/plugins

start() {
        uwsgi -m --ini /etc/uwsgi/jsonrpc.ini &
        uwsgi -m --ini /etc/uwsgi/blockpage.ini &
        uwsgi -m --ini /etc/uwsgi/upload.ini &
}

stop() {
        killall -9 uwsgi
}
```

我们再去找一下 **/etc/uwsgi/upload.ini**

```
[uwsgi]
plugins = cgi
workers = 1
master = 1
uid = www-data
gid = www-data
socket=127.0.0.1:9003
buffer-size=4096
cgi = /www/cgi-bin/upload.cgi
cgi-allowed-ext = .cgi
cgi-allowed-ext = .pl
cgi-timeout = 300
ignore-sigpipe = true
```

从上述文件中我们可以知道 **/form-file-upload** 它对应的后端处理程序是 **/www/cgi-bin/upload.cgi**。因此我们可以无条件访问 **upload.cgi**。

同时上述配置文件中我们可以看到检查了 `/tmp/websession/token/$cookie_sessionid` 文件是否存在。但是存在缺陷，就是这里的 **$cookie\_sessionid** 是用户在 **http** 请求中传进去的一个值，它并没有检查是否存在 **../../** ，也就是说我们可以通过跨目录来导致授权绕过。如：我们可以传递 **../../../etc/firmware\_version**。![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197154-1678175397.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197154-1678175398.png)

同时也可以看到在 *...