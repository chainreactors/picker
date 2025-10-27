---
title: Nginx和Apache下https配置
url: https://blog.upx8.com/3107
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:14.163229
---

# Nginx和Apache下https配置

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Nginx和Apache下https配置

发布时间:
2022-11-21

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
10288

### 准备工作：

```
www.aaa.com.crt     //证书文件
www.aaa.com.key     //私钥文件
ca.crt              //证书链文件
```

### Nginx虚拟主机配置文件：

> server {
>  listen 80; //监听80端口
>  listen 443 ssl http2; //监听443端口
>  server\_name www.aaa.com; //服务域名
>  root /www/aaa; //站点根目录
>  index index.html index.htm; //默认首页文档
>  #ssl on; //注意，开启此项将只能只用https访问
>  ssl\_certificate /alidata/ssl/bingyang.crt; //证书文件
>  ssl\_certificate\_key/alidata/ssl/bingyang.key; //证书私钥文件
>  ssl\_protocols TLSv1 TLSv1.1 TLSv1.2;
>  ssl\_session\_cache shared:SSL:60m;
>  ssl\_session\_timeout 10m;
>  ssl\_ciphers HIGH:!aNULL:!MD5;
>  ssl\_prefer\_server\_ciphers on;
>
> location / {
>  }
>
> #开启列出目录(可选)
>  autoindex on; //开启显示文件目录
>  autoindex\_exact\_size off; //显示文件大小（off为自动单位）
>  autoindex\_localtime on; //显示修改时间
>
> #错误页配置
>  error\_page 404 /404.html;
>  location = /40x.html {
>  }
>  error\_page 500 502 503 504 /50x.html;
>  location = /50x.html {
>  root /50x/ //50x错误页文件目录
>  }
> }

### Apache虚拟主机配置文件：

> <VirtualHost \*:80> //http访问端口
> ServerName www.aaa.com //绑定域名
> DocumentRoot "/www/aaa/" //站点根目录
> DirectoryIndex index.html index.htm //首页默认文档
> <Directory "/www/aaa/"> //站点目录
>  Options FollowSymLinks //不允许列出目录
>  #Options Indexes FollowSymLinks //允许列出目录
>  AllowOverride All
>  Require all granted
> </Directory>
> </VirtualHost>
>
> <VirtualHost \*:443> //https访问端口
> ServerName www.aaa.com //绑定域名
> DocumentRoot "/www/aaa/" //站点根目录
> DirectoryIndex index.html //首页文档
>
> SSLEngine on //开启SSL
> SSLCertificateFile "/root/www.aaa.com.crt" //证书文件
> SSLCertificateKeyFile "/root/www.aaa.com.key" //证书私钥
> SSLCertificateChainFile "/root/ca.crt" //证书链文件
>
> <Directory "/www/aaa/">
>  Options FollowSymLinks //不允许列出目录
>  #Options Indexes FollowSymLinks //允许列出目录
>  AllowOverride All
>  Require all granted
> </Directory>
> </VirtualHost>

[取消回复](https://blog.upx8.com/3107#respond-post-3107)

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