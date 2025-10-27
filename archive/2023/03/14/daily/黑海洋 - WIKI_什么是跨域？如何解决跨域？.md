---
title: 什么是跨域？如何解决跨域？
url: https://blog.upx8.com/3261
source: 黑海洋 - WIKI
date: 2023-03-14
fetch_date: 2025-10-04T09:30:39.558188
---

# 什么是跨域？如何解决跨域？

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 什么是跨域？如何解决跨域？

发布时间:
2023-03-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14471

**✨ 什么是跨域**

* **域：** 是指浏览器不能执行其他网站的脚本
* **跨域：** 它是由浏览器的 **同源策略** 造成的,是浏览器对 `JavaScript` 实施的安全限制，所谓同源（即指在同一个域）就是两个页面具有相同的协议 `protocol`，主机 `host` 和端口号 `port` 则就会造成 **跨域，域名组成**
* **![](https://pic.imgdb.cn/item/640f2f97f144a010070294e5.png)**

## ✨ 跨域场景

* 场景的跨域场景有哪些，请参考下表

| 当前url | 请求url | 是否跨域 | 原因 |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| `http://www.autofelix.cn` | `http://www.autofelix.cn/api.php` | **否** | 协议/域名/端口都相同 |
| `http://www.autofelix.cn` | `https://www.autofelix.cn/api.php` | **是** | 协议不同 |
| `http://www.autofelix.cn` | `http://www.rabbit.cn` | **是** | 主域名不同 |
| `http://www.autofelix.cn` | `http://api.autofelix.cn` | **是** | 子域名不同 |
| `http://www.autofelix.cn:80` | `http://www.autofelix.cn:8080` | **是** | 端口不同 |

## ✨ 解决跨域的四种方式

* **nginx的反向代理**
* 使用 `nginx` 反向代理实现跨域，是最简单的跨域方式
* 只需要修改 `nginx` 的配置即可解决跨域问题，支持所有浏览器，支持`session`，不需要修改任何代码，并且不会影响服务器性能

```
// nginx配置
server {
    listen       81;
    server_name  www.domain1.com;
    location / {
        proxy_pass   http://www.domain2.com:8080;  #反向代理
        proxy_cookie_domain www.domain2.com www.domain1.com; #修改cookie里域名
        index  index.html index.htm;

        # 当用webpack-dev-server等中间件代理接口访问nignx时，此时无浏览器参与，故没有同源限制，下面的跨域配置可不启用
        add_header Access-Control-Allow-Origin http://www.domain1.com;  #当前端只跨域不带cookie时，可为*
        add_header Access-Control-Allow-Credentials true;
    }
}
```

* **jsonp请求**
* `jsonp` 是服务器与客户端跨源通信的常用方法。最大特点就是简单适用，兼容性好 `兼容低版本IE`，缺点是只支持 `get` 请求，不支持 `post` 请求
* 原理时网页通过添加一个 `<script>` 元素，向服务器请求 `json` 数据，服务器收到请求后，将数据放在一个指定名字的回调函数的参数位置传回来

```
//jquery实现
<script>
$.getJSON('http://autofelix.com/api.php&callback=?', function(res) {
     // 处理获得的数据
     console.log(res)
});
</script>
```

* **后端语言代理**
* 可以通过一种没有跨域限制的语言中转一下，通过后端语言去请求资源，然后再返回数据
* 比如 `http://www.autofelix.cn` 需要调用 `http://api.autofelix.cn/userinfo` 去获取用户数据，因为子域名不同，会有跨域限制
* 可以先请求 `http://www.autofelix.cn` 下的 `php` 文件，比如 `http://www.autofelix.cn/api.php`，然后再通过该 `php` 文件返回数据

```
<?php
// api.php 文件中的代码
public function getCurl($url, $timeout = 5)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
    $result = curl_exec($ch);
    curl_close($ch);

    return $result;
}

$result = getCurl('http://api.autofelix.cn/userinfo');

return $result;
```

* **后端语言的设置**
* 主要通过后端语言主动设置跨域请求，这里以 `php` 作为案例

```
<?php
// 允许所有域名访问
header('Access-Control-Allow-Origin: *');
// 允许单个域名访问
header('Access-Control-Allow-Origin: https://autofelix.com');
// 允许多个自定义域名访问
static public $originarr = [
   'https://autofelix.com',
   'https://baidu.com',
   'https://csdn.net',
];

// 获取当前跨域域名
$origin = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : '';
if (in_array($origin, self::$originarr)) {
    // 允许 $originarr 数组内的 域名跨域访问
    header('Access-Control-Allow-Origin:' . $origin);
    // 响应类型
    header('Access-Control-Allow-Methods:POST,GET');
    // 带 cookie 的跨域访问
    header('Access-Control-Allow-Credentials: true');
    // 响应头设置
    header('Access-Control-Allow-Headers:x-requested-with,Content-Type,X-CSRF-Token');
}
```

相关文献：[https://blog.csdn.net/fujian9544/article/details/106597778](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1amlhbjk1NDQvYXJ0aWNsZS9kZXRhaWxzLzEwNjU5Nzc3OA)

相关文献：[https://www.docsget.com/#/Cross-domain/](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZG9jc2dldC5jb20vIy9Dcm9zcy1kb21haW4v)

[取消回复](https://blog.upx8.com/3261#respond-post-3261)

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