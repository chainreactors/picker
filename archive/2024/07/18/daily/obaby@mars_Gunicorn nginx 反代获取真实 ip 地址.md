---
title: Gunicorn nginx 反代获取真实 ip 地址
url: https://h4ck.org.cn/2024/07/17578
source: obaby@mars
date: 2024-07-18
fetch_date: 2025-10-06T17:43:12.687859
---

# Gunicorn nginx 反代获取真实 ip 地址

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Gunicorn nginx 反代获取真实 ip 地址

2024年7月17日
[24 条评论](https://h4ck.org.cn/2024/07/17578#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG901.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG901.jpg)

闺蜜圈的后台服务使用 gunicorn 运行，对外接口通过 nginx 进行反代。但是反代有个问题，那就是 gunicorn 获取到的服务器的 ip 地址都是 127.0.0.1。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240717-150923-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240717-150923.jpg)

作为一个强迫症能忍受这个？那自然不行啊。

在 nginx 配置文件中增加 proxy\_set\_header

```
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

修改 gunicorn 启动参数，修改日志格式为：

```
--access-logformat='%({X-Real-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

重启 nginx 以及 gunicorn 服务,就可以记录真实 ip 地址了：

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240717-151856-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240717-151856.jpg)

参数说明：

```
h is the remote address
l is - (not used)
u is - (not used, reserved)
t is the time stamp
r is the status line
s is the status of the request
b is length of response
f is referrer
a is user agent
You can also customize it with the following extra variables that are not used by default:

T - request time (in seconds)
D - request time (in microseconds)
p - the process id
{Header}i - request header (custom)
{Response}o - response header (custom)
```

参考链接:https://stackoverflow.com/questions/25737589/gunicorn-doesnt-log-real-ip-from-nginx

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Gunicorn nginx 反代获取真实 ip 地址》](https://h4ck.org.cn/2024/07/17578)
\* 本文链接：<https://h4ck.org.cn/2024/07/17578>
\* 短链接：<https://oba.by/?p=17578>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[gunicorn](https://h4ck.org.cn/tags/gunicorn)[nginx](https://h4ck.org.cn/tags/nginx)[Python](https://h4ck.org.cn/tags/python)

[Previous Post](https://h4ck.org.cn/2024/07/17587)
[Next Post](https://h4ck.org.cn/2024/07/17576)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年3月12日

#### [Uni-id-co 外部系统联登](https://h4ck.org.cn/2024/03/15787)

2022年8月31日

#### [全国统计用区划代码和城乡划分代码[爬虫代码]【Json+CSV格式】](https://h4ck.org.cn/2022/08/10427)

2023年8月9日

#### [阿里云OSS直（zhí）传](https://h4ck.org.cn/2023/08/12841)

### 24 comments

1. ![](https://gg.lang.bi/avatar/9007447122714374d22b96254665d14ba508ffca15ee94c291f8531453e82e65?s=64&d=identicon&r=r) **[秋澪](https://blog.akimio.top)**说道：

   [2024年7月17日 19:10](https://h4ck.org.cn/2024/07/17578#comment-117421)

   ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

   ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我也被这个问题困扰很久了，但是一直没能解决，因为我部署的后端应用和nginx都是用docker部署的，传到后端的地址就成了docker bridge的gateway地址

   [回复](#comment-117421)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年7月17日 19:12](https://h4ck.org.cn/2024/07/17578#comment-117422)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      nginx proxy\_pass\_header 的x-real-ip 在 docker 中应该也能拿到

      [回复](#comment-117422)

      1. ![](https://gg.lang.bi/avatar/9007447122714374d22b96254665d14ba508ffca15ee94c291f8531453e82e65?s=64&d=identicon&r=r)

         [2024年7月17日 19:22](https://h4ck.org.cn/2024/07/17578#comment-117423)

         ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

         ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         好像debian是可以的，我群晖和unraid似乎不行，如果可以还请请教一下如何操作（不过通过CloudflareTunnel的流量确实是可以获取真实IP，似乎是用了其他标头）

         [回复](#comment-117423)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2024年7月17日 19:28](https://h4ck.org.cn/2024/07/17578#comment-117424)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            你 docker 里面跑的什么程序？是要通过代码获取？还是直接写到日志里？

            [回复](#comment-117424)

            1. ![](https://gg.lang.bi/avatar/9007447122714374d22b96254665d14ba508ffca15ee94c291f8531453e82e65?s=64&d=identicon&r=r)

               [2024年7月17日 19:46](https://h4ck.org.cn/2024/07/17578#comment-117425)

               ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

               ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

               jellyfin之类的，后台日志可以看到客户端的IP，还有一个就是群晖的防火墙，由于前置了nginx（为了加ssl）导致访问被归到局域网了，所以防火墙就相当于失效了

               [回复](#comment-117425)

               1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

                  [2024年7月17日 21:01](https://h4ck.org.cn/2024/07/17578#comment-117426)

                  ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

                  ![Google Chrome 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 120") Google Chrome 120 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![...