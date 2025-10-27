---
title: Nginx常用经典配置|反向代理、HTTPS重定向、端口转发
url: https://buaq.net/go-162586.html
source: unSafe.sh - 不安全
date: 2023-05-10
fetch_date: 2025-10-04T11:37:20.061605
---

# Nginx常用经典配置|反向代理、HTTPS重定向、端口转发

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

![]()

Nginx常用经典配置|反向代理、HTTPS重定向、端口转发

目前前后端项目分离场景多了以后，一般是前端一个端口，后端一个端口。如前端是https://example.com/index.html，调用的接口是ht
*2023-5-9 23:53:59
Author: [blog.upx8.com(查看原文)](/jump-162586.htm)
阅读量:43
收藏*

---

目前前后端项目分离场景多了以后，一般是前端一个端口，后端一个端口。

如前端是https://example.com/index.html，调用的接口是https://example.com:4433

如此部署对于一些小项目未免有些麻烦，当然你在公网环境下也可以选择使用子域名、其他域名进行跨域访问。

这里说的是同一个域名，同一个端口，让前后端同时进行访问服务。

前端地址：https://example.com/index.html

接口地址：https://example.com/api/

这里先记录我已经测试通过的反向代理的方式，即不改变原本的server配置。直接通过反向代理将example.com/api 重定向到 example.com:4443/

```
location ^~ /api/ {
    proxy_pass  https://example.com:4433/;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

值得一提的是，location段的^~是代表某个字符作为开头匹配，这里就是以/api/作为开头进行匹配URL规则。

这里不能写作~，因为~是正则匹配的意思，用了正则就不能再proxy\_pass段配置URI了，所谓URI就是4433端口后面的/。

如果不写/，当访问example.com/api/index.php时，会代理到example.com:4433/api/index.php。并不能定位到后端的根路径，所以这里以/结束。

如果想让你的非标准https端口，如2083支持HTTP跳转HTTPS访问，请参照如下配置。

```
error_page 497 https://$host:2083$request_uri;
```

如果不这么配置，默认当用户不确定网站协议时，采用了HTTP协议访问你的HTTPS网站就会出现无法访问。

错误如：The plain HTTP request was sent to HTTPS port

日常为了保证访客安全性，我们常常需要让全站保持HTTPS访问，那么你可以通过以下配置。

```
server {
        listen 80 default_server;
        server_name example.com;
        rewrite ^(.*) https://$server_name$1 permanent;
        #上面的rewrite也可以写作
        return 301 https://$host$request_uri;
}
server {
        listen 443 ssl;
        server_name example.com;
}
```

做法是，让80监听到的HTTP链接全部重定向到HTTPS端口中。

## HSTS策略保持HTTPS连接

与此同时，你也可以通过开启HSTS策略强制让访客浏览器保持使用HTTPS链接，添加如下代码：

```
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains;preload" always;
```

* max-age：设置单位时间（秒）内強制使用 HTTPS 连接，这里为1年
* includeSubDomains：可选，站点所有子域同时生效
* preload：可选，非规范值，用于定义使用『HSTS 预加载列表』
* always：可选，保证所有响应都发送此响应头，包括各种內置错误响应

反向代理的场景很多，例如前面的前后端统一域名端口，例如负载均衡等。

```
location / {
    proxy_pass  http://example.com;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

完整参数配置

```
location / {
    proxy_pass  http://example.com;
    proxy_redirect     off;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_max_temp_file_size 0;
    proxy_connect_timeout      90;
    proxy_send_timeout         90;
    proxy_read_timeout         90;
    proxy_buffer_size          4k;
    proxy_buffers              4 32k;
    proxy_busy_buffers_size    64k;
    proxy_temp_file_write_size 64k;
}
```

Nginx端口转发性能也非常强大，可以用于内网数据库、其他服务端口外露的场景。

如将内网的192.168.1.2MySQL数据库端口通过Nginx所在服务器的33062端口进行外露。

```
upstream TCP3306 {
    hash $remote_addr consistent;
    server 192.168.1.2:3306;
}

server {
    listen 33062;
    proxy_connect_timeout 5s;
    proxy_timeout 300s;
    proxy_pass TCP3306;
}
```

可以通过 ngx\_http\_access\_module 允许限制某些IP地址的访问。

比如仅允许内网 IP 访问管理后台页面。

```
location /admin {
    allow 192.168.1.0/24;
    allow 10.0.0.0/24;
    deny all;
}
```

其中的 192.168.1.0/24 和 10.0.0.0/24 皆为允许访问的 IP。默认从上而下依次匹配规则，如果匹配不中前面的内网IP，则默认命中最后的拒绝访问。

如果你已经明确知道你的网站只有 GET、POST、HEAD 这三种请求，其他请求完全用不到，则可以通过如下方式直接屏蔽掉。

```
if($request_method !~ ^(GET|HEAD|POST)$) {
    return404;
}
```

有时候，为了优化一些网站性能，可以将超时时间设置低一些，来降低死链接。

```
http {

    client_body_timeout 10;
    client_header_timeout 30;
    keepalive_timeout 30 30;
    send_timeout 10;

}
```

当用户请求返回数据中不包含具体的nginx版本号，避免一些版本漏洞被猜解。

```
server_tokens off;
```

文章来源: https://blog.upx8.com/3536
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)