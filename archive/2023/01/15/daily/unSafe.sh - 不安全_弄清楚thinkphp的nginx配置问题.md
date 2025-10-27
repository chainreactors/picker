---
title: 弄清楚thinkphp的nginx配置问题
url: https://buaq.net/go-145556.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:55:47.884158
---

# 弄清楚thinkphp的nginx配置问题

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

弄清楚thinkphp的nginx配置问题

一个比较完整的配置如下，我会标出需要注意的地方server { listen 80; listen [::]:80; li
*2023-1-14 22:52:50
Author: [www.yanglong.pro(查看原文)](/jump-145556.htm)
阅读量:35
收藏*

---

一个比较完整的配置如下，我会标出需要注意的地方

```
server {
    listen       80;
    listen  [::]:80;
    listen       443 ssl;
    server_name  localhost;

    root   /var/www/php/public;

    ssl_certificate     /var/www/php/docker/nginx/test/https.pem;
    ssl_certificate_key /var/www/php/docker/nginx/test/https.key;
    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers         HIGH:!aNULL:!MD5;

    index index.php;

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        try_files $uri $uri/ /index.php$uri$is_args$query_string;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    location ~.*.php($|/) {
        fastcgi_split_path_info ^(.+\.php)(.*)$;
        # fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        # fastcgi_pass   php-fpm:9000;
        # fastcgi_index  index.php;
        fastcgi_pass   unix:/var/tmp/php-fpm/php-fpm.sock;
        fastcgi_param  SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param  PATH_INFO $fastcgi_path_info; # TP要这玩意

        include        fastcgi_params;
    }

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```

文章来源: https://www.yanglong.pro/%e5%bc%84%e6%b8%85%e6%a5%9athinkphp%e7%9a%84nginx%e9%85%8d%e7%bd%ae%e9%97%ae%e9%a2%98/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)