---
title: CORS
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496243&idx=1&sn=7a8cff79b009cea9d2e340ba30d990e7&chksm=e8a5f850dfd27146fd92b96866b30bf9dcb1215bc5266e9e2beb068568758b10ce46f1f67b16&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-31
fetch_date: 2025-10-06T18:55:02.189388
---

# CORS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7ZFkWN2LAfSAmEClyX2m80ZREhyOAnOaK7CDn3pJEVjvCElSs2j3lTcSjee5T7U3DZXsylKbpYBg/0?wx_fmt=jpeg)

# CORS

原创

richardo1o1

迪哥讲事

## 同源策略的核心概念

同源策略要求在三个方面相同，才能允许访问彼此的资源：

1.协议相同（如 http:// 和 https://）。

2.域名相同（如 example.com 和 sub.example.com 不同）。

3.端口相同（如 http://example.com:80 和 http://example.com:8080 不同）。

如果这三者中有任何一项不同，浏览器将会阻止跨域请求，从而保护用户数据的安全。

## 具体例子：

假设我们有两个网站：

网站 A: https://www.example.com

网站 B: https://www.anotherexample.com

网站 A 中有一个网页，包含一个 JavaScript 文件，目的是从 B 网站中获取一些敏感数据，例如用户的个人信息。

```
fetch('https://www.anotherexample.com/api/userinfo')
    .then(response => response.json())
    .then(data => console.log(data));
```

当这个代码运行时，浏览器会检查：

* 网站 A 的协议是 https，网站 B 的协议也是 https，协议相同。
* 网站 A 的域名是 www.example.com，网站 B 的域名是 www.anotherexample.com，域名不同。
* 假设两个网站都在默认的 443 端口运行，端口相同。

由于域名不同，浏览器会阻止这次跨域请求，报错信息可能是“CORS 头丢失”或者“跨域请求被阻止”。

## 如何突破同源策略？

虽然同源策略严格限制跨域访问，但有时候需要允许跨域请求。浏览器中突破同源策略的一个常见方法是 跨域资源共享（CORS）。它允许服务器通过设置特定的响应头，告诉浏览器允许来自其他源的请求。

## CORS 的例子：

如果网站 B 的服务器希望允许网站 A 访问它的资源，那么它可以在响应头中添加：(其实这是后端开发所做的工作)

Access-Control-Allow-Origin: https://www.example.com

这样，浏览器会允许网站 A 访问网站 B 的资源，突破了同源策略的限制。

要使网站 B 的服务器在响应头中添加 Access-Control-Allow-Origin，通常需要在服务器端进行配置。下面举个例子来说明:

### Nginx 配置 CORS

在 Nginx 服务器中，可以通过添加以下配置来允许跨域访问。

步骤：

在 Nginx 的配置文件（通常是 /etc/nginx/nginx.conf 或者 /etc/nginx/sites-available/default）中，添加以下内容：

```
server {
    listen 80;
    server_name www.anotherexample.com;

    location /api/ {
        # 允许特定域名访问
        add_header 'Access-Control-Allow-Origin' 'https://www.example.com';

        # 允许的请求方法，比如 GET, POST
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';

        # 允许的请求头
        add_header 'Access-Control-Allow-Headers' 'Content-Type';

        # 如果需要处理复杂的跨域请求
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' 'https://www.example.com';
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
            add_header 'Access-Control-Allow-Headers' 'Content-Type';
            return 204;  # 响应空的请求体
        }
    }
}
```

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过