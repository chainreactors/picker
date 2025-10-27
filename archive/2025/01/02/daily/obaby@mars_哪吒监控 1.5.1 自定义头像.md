---
title: 哪吒监控 1.5.1 自定义头像
url: https://h4ck.org.cn/2025/01/18912
source: obaby@mars
date: 2025-01-02
fetch_date: 2025-10-06T20:06:34.433269
---

# 哪吒监控 1.5.1 自定义头像

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 哪吒监控 1.5.1 自定义头像

2025年1月1日
[31 条评论](https://h4ck.org.cn/2025/01/18912#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/2024_06_17_11_39_IMG_3994-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/01/2024_06_17_11_39_IMG_3994-tuya.jpg)

对于哪吒监控自带的授权登录，最近不知道是github问题还是什么问题，一直登录失败。醒着直接升级下监控版本，结果，效果很不错，成功升级了。

感觉是换了一个全新的版本，但是这个版本确登录不了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/image-3.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/image-3.png)

多次尝试更新之后，终于默认账号登录成功了，但是，伴随而来的是另外的一个问题。所有的监控项都没了，并且首页提示websocket建立失败。查阅文档才发现，新的版本需要将websocket一块进行代理：

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    # http2 on; # Nginx > 1.25.1，请注释上面两行，启用此行

    server_name dashboard.example.com; # 替换为你的域名
    ssl_certificate          /data/letsencrypt/fullchain.pem; # 域名证书路径
    ssl_certificate_key      /data/letsencrypt/key.pem;       # 域名私钥路径
    ssl_stapling on;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m; # 如果与其他配置冲突，请注释此项
    ssl_protocols TLSv1.2 TLSv1.3;

    underscores_in_headers on;
    set_real_ip_from 0.0.0.0/0; # 替换为你的 CDN 回源 IP 地址段
    real_ip_header CF-Connecting-IP; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
    # 如果你使用nginx作为最外层，把上面两行注释掉

    # grpc 相关
    location ^~ /proto.NezhaService/ {
        grpc_set_header Host $host;
        grpc_set_header nz-realip $http_CF_Connecting_IP; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
        # grpc_set_header nz-realip $remote_addr; # 如果你使用nginx作为最外层，就把上面一行注释掉，启用此行
        grpc_read_timeout 600s;
        grpc_send_timeout 600s;
        grpc_socket_keepalive on;
        client_max_body_size 10m;
        grpc_buffer_size 4m;
        grpc_pass grpc://dashboard;
    }
    # websocket 相关
    location ~* ^/api/v1/ws/(server|terminal|file)(.*)$ {
        proxy_set_header Host $host;
        proxy_set_header nz-realip $http_cf_connecting_ip; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
        # proxy_set_header nz-realip $remote_addr; # 如果你使用nginx作为最外层，就把上面一行注释掉，启用此行
        proxy_set_header Origin https://$host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_pass http://127.0.0.1:8008;
    }
    # web
    location / {
        proxy_set_header Host $host;
        proxy_set_header nz-realip $http_cf_connecting_ip; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
        # proxy_set_header nz-realip $remote_addr; # 如果你使用nginx作为最外层，就把上面一行注释掉，启用此行
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
        proxy_max_temp_file_size 0;
        proxy_pass http://127.0.0.1:8008;
    }
}

upstream dashboard {
    server 127.0.0.1:8008;
    keepalive 512;
}
```

而至于数据丢失，官网也写了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-193729.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-193729.png)

这就很棒。只能重新添加所有服务器，添加之后感觉一切正常了，但是后台那个头像实在是无法忍受。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/1.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/1.png)

![头像](https://api.dicebear.com/7.x/notionists/svg?seed=obaby)

尼玛，这苦大仇深的表情，作为小仙女坚决不能忍啊。在[杜老师](https://chat.dusays.com/dusays/channels/town-square)的聊天室，交流了一下，他也不知道怎么改。只能尝试js暴力修改src，代码如下：

```
var images = document.querySelectorAll('img[alt="obaby"]');
 images.forEach(function(image) {
        console.log(image);
         console.log('first inject to replace avatar!');
        image.src = "https://g.h4ck.org.cn/avatar/3a78942c4ddcda86242f20abdacee082?s=256&d=identicon&r=g";
    });
```

然而，将这段代码加入到系统设置的自定义代码内，会发现多数情况下都不能调用，只能通过差距js的方式进行调用，并且哪吒还有个问题，那就是对于其他域名下的js会加载失败，所以只能把js放到同一个服务器下。

后台添加配置：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195348.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195348.png)

此时js代码多数情况都能正常调用，为了能够加载这个js，需要修改nginx配置文件将js路径加入nginx配置文件：

```
location /inject/{
alias /home/wwwroot/s.h4ck.org.cn/inject/;
}
```

此时，顶部的头像已经修改成功了，但是下面的头像还是旧的，就很蛋疼。如果查看页面源码会发现基本都是js绘制的，本身并没有任何的内容。

遇事尝试使用nginx的替换功能进行内容替换，

```
location / {
        proxy_set_header Host $host;
        #proxy_set_header nz-realip $http_cf_connecting_ip; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
        proxy_set_header nz-realip $remote_addr; # 如果你使用nginx作为最外层，就把上面一行注释掉，启用此行
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
        proxy_max_temp_file_size 0;
        proxy_pass http://127.0.0.1:8008;
sub_filter 'https://api.dicebear.com/7.x/notionists/svg?seed=' 'https://g.h4ck.org.cn/avatar/3a78942c4ddcda86242f20abdacee082?s=256&d=identicon&r=g&name=';
sub_filter_once off;

    }
```

然而，这种替换方式竟然只有首次生效，不知道是不是nginx配置问题，最终还是回到了直接修改js文件的方法。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195537.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195537.png)

拉出app文件，这个东西是编译的的elf文件，看了下字符串长度过长，替换有些麻烦，也没趁手的elf编辑器，就很麻烦。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/3-1.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/3-1.png)

转换思路，不好改二进制，那就改对应的js文件，编辑/dashboard/assets/index-CeBwNjOv.js 替换内部的https://api.dicebear.com/7.x/notionists/svg?seed=。

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195020.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195020.png)

同时将文件头的import改为绝对路径，参考https://s.h4ck.org.cn/inject/index-obaby.js：

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195142.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195142.png)

修改之前的内容替换代码为：

```
location / {
        proxy_set_header Host $host;
        #proxy_set_header nz-realip $http_cf_connecting_ip; # 替换为你的 CDN 提供的私有 header，此处为 CloudFlare 默认
        proxy_set_header nz-realip $remote_addr; # 如果你使用nginx作为最外层，就把上面一行注释掉，启用此行
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
        proxy_max_temp_file_size 0;
        proxy_pass http://127.0.0.1:8008;
sub_filter '/dashboard/assets/index-CeBwNjOv.js' '/inject/index-obaby.js';
sub_filter_once off;

    }
```

重启nginx

通过下面的命令查看是否支持sub\_filter ，如果不支持重新编译nginx：

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195418.png)](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-195418.png)

否则会爆下面的错误：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-194012.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-194012.png)

此时头像就ok啦：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195139.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-31-195139.png)

另外一个，就是那个命令窗口，V0版本是个全屏的，这V1弄了个小窗口，看着是真tm蛋疼：

[![](https://h4ck.org.cn/wp-content/uploads/2025/01/Screenshot-2025-01-01-193325.png)](ht...