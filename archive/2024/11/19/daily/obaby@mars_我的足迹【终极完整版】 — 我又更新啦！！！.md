---
title: 我的足迹【终极完整版】 — 我又更新啦！！！
url: https://h4ck.org.cn/2024/11/18564
source: obaby@mars
date: 2024-11-19
fetch_date: 2025-10-06T19:14:31.958827
---

# 我的足迹【终极完整版】 — 我又更新啦！！！

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F)

# 我的足迹【终极完整版】 — 我又更新啦！！！

2024年11月18日
[85 条评论](https://h4ck.org.cn/2024/11/18564#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/A2I2296_e-tuya-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/A2I2296_e-tuya.jpg)

我的足迹这个东西，周末实现的方法，终究感觉不高级的样子。就是看起来平平无奇，除了那几个点点，剩下的貌似也没什么意思。

[**扶苏**](https://pwsz.com/hobby/4108.html)给留言写到他也做了一个足迹页面，说可以作为参考。去参观膜拜了一番，感觉 js 实现的就是要高级一些。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241118-132714.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241118-132714.jpg)

为什么？因为 js 实现的 tm 能动啊。

原本不想写 js 的，主要是懒，实在是不想写代码。但是，但是看到这个东西，难免心动，然后就食言了。我又做了一个。

然后，还是先来看效果吧：
 ﻿

这个是不是看起来就高级了一些？主要是支持点击事件。

代码中定义了三组内容：

```
locations 点亮城市
passed_locations 途径城市
out_China_locations 国外城市 这一部分加入了经纬度信息，百度地图的反向查询，查出来的坐标是错误的，所以就独立处理了。
    var out_China_locations = [{
        city: "清迈",
        text: "泰国清迈",
        mark: "已经游玩",
        longtitude: 98.96095,
        latitude: 18.79325
    },
    {
        city: "清莱",
        text: "泰国清莱",
        mark: "已经游玩",
        longtitude: 99.72588,
        latitude: 19.903138
    }];
```

另外，在使用改代码的时候，还需要找两个头像文件，分别用来进行地图打点：

```
// 创建小车图标
                    var myIcon = new BMapGL.Icon("https://h4ck.org.cn/avatar/avatar_circle-256.png", new BMapGL.Size(26, 26));
                    // 创建Marker标注，使用小车图标
                    // var pt = new BMapGL.Point(116.417, 39.909);
                    var marker = new BMapGL.Marker(point, {
                        icon: myIcon
                    });
```

点击时间代码，需要修改域名：

```
var city = locations[i].city;
            var text = "\r\n <a target='_blank' href='" + "https://h4ck.org.cn/?s=" + locations[i].text + "'>  https://h4ck.org.cn/?s=" + locations[i].text + "</a>";
```

原来的效果：

![](https://api.map.baidu.com/staticimage/v2?ak=CA9cuqs5s2OY72PAcwG3kx470A9v3yuX&width=900&height=800&zoom=5&center=103.8319522831,36.0615585627&markerStyles=0xFF0000|0x808000&markers=&markerStyles=m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|m,V,0xFF69B4|s,P,0xFFFF00|s,P,0xFFFF00|s,P,0xFFFF00|s,P,0xFFFF00|s,P,0xFFFF00|s,P,0xFFFF00&markers=117.120128,36.652069|118.088910,24.479627|118.054994,36.813787|120.210792,30.246026|116.407387,39.904179|121.473667,31.230525|114.057939,22.543527|118.674633,37.433992|119.221487,34.596639|116.047387,43.933212|118.887613,42.256876|117.962749,40.952942|117.086963,36.201784|117.323759,34.810858|102.833669,24.881490|112.938882,28.228304|112.945439,27.831360|113.132783,27.828862|119.526850,35.416912|122.120519,37.513315|121.447755,37.464551|114.057939,22.543527|113.264499,23.130061|108.939645,34.343207|118.356464,35.103771|119.161721,36.707668|120.382665,36.066938|100.301614,25.678466|110.198418,20.045805|109.511709,18.252865|109.769146,18.313334|107.582096,23.316753|117.201509,39.085318|116.359244,37.436492|117.184892,29.274400|118.859307,28.970229|113.121586,23.021351|120.311889,31.491064)

修改之后，高级感是不是瞬间就有了呢，嘻嘻。

开源代码地址：

<https://github.com/obaby/BabyFootprint>

参考文档：

<https://lbsyun.baidu.com/jsdemo.htm#cLocation>

最终效果预览：

<https://h4ck.org.cn/footprint/>

## 更新：

上面的内容虽然够用了，但是每次还要更新代码，这多蛋疼啊。所以，我又更新了，这次我直接加了一个后台，哈哈哈

# Baby 足迹地图

## 简介：

基于百度地图的足迹地图。

## 功能

* 支持后台添加位置信息
* 支持添加带gps坐标的位置信息
* 支持自定义marker图标

## 安装运行：

docker运行：

```
docker run -d -p 10086:10086 obaby/baby-footprint:1.0
```

python 3.8 – 3.10

```
pip install -r requitements.pip
```

## 启动服务 建议使用nginx反代：

```
python manage runserver 0.0.0.0:10086
```

### 后台登录地址：

[http://127.0.0.1:10086/admin/](http://127.0.0.1:10086/)

登录账号：obaby
默认密码：123456

## 修改：

前端页面修改js，static/js/footprint.js 编辑以下代码替换默认图标：

```
var location = locations[i];
var city = locations[i].name;
var text = "\r\n <a target='_blank' href='" + "https://h4ck.org.cn/?s=" + locations[i].text + "'>  https://h4ck.org.cn/?s=" + locations[i].text + "</a>";
var mark = locations[i].mark;
var marker_image = "https://h4ck.org.cn/avatar/avatar_circle-256.png";
if (location.is_passed ){
    marker_image = "https://h4ck.org.cn/avatar/avatar-2.png";
}
```

* marker\_image 默认图标
* <https://h4ck.org.cn/avatar/avatar-2.png> 经停点图标
* <https://h4ck.org.cn/?s=> 弹出卡片搜索地址以及链接地址

## 截图：

### 后台首页：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/admin.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/admin.png)

### 添加地点：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/add.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/add.png)

**（如果不带gps坐标或者坐标无效，将会通过百度地图api解析gps坐标）**

### 列表：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/list.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/list.png)

### 首页：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/home.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/home.png)

## 扩展内容 nginx反代：

```
server
    {
        listen 443 ssl http2;
        #listen [::]:443 ssl http2;
        server_name footprint.h4ck.org.cn ;
        index index.html index.htm index.php default.html default.htm default.php;
        root  /home/wwwroot/footprint.h4ck.org.cn;

        ssl_certificate /home/lighthouse/footprint.h4ck.org.cn_nginx/footprint.h4ck.org.cn_bundle.pem;
        ssl_certificate_key /home/lighthouse/footprint.h4ck.org.cn_nginx/footprint.h4ck.org.cn.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        ssl_ciphers "TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5";
        ssl_session_cache builtin:1000 shared:SSL:10m;
        # openssl dhparam -out /usr/local/nginx/conf/ssl/dhparam.pem 2048
        ssl_dhparam /usr/local/nginx/conf/ssl/dhparam.pem;

        include rewrite/none.conf;
        #error_page   404   /404.html;

        # Deny access to PHP files in specific directory
        #location ~ /(wp-content|uploads|wp-includes|images)/.*\.php$ { deny all; }
location /static/ {
       alias    /home/wwwroot/babyfootprint/static/;
}

location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;

        proxy_pass http://127.0.0.1:10099;
        proxy_http_version 1.1;
proxy_set_header Accept-Encoding "";
}
        access_log  /home/wwwlogs/footprint.h4ck.org.cn.log;
    }
```

## 11.19 更新内容：

增加文章链接，打卡图片链接：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-092853-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-092853.jpg)

新效果图：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-092748-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-092748.jpg)

预览地址：

[https://footprint.h4ck.org.cn](https://footprint.h4ck.org.cn/)...