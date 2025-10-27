---
title: 震惊！YAK-JWT靶场的通关方式竟然是...
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527683&idx=1&sn=f2bcbe8c29a127a08a073efae31342ce&chksm=c2d111a7f5a698b136b4c4f6ccc2774a7fd9cacfb63433e04b1d3aaaabc9bd8dd78d060acfa2&scene=58&subscene=0#rd
source: Yak Project
date: 2025-02-15
fetch_date: 2025-10-06T20:37:49.429819
---

# 震惊！YAK-JWT靶场的通关方式竟然是...

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUBblZ0xWuqoJa8icQGCvcbPCcDhmTdfyicRXC9ydnDEXWksDGicF6dXKKg/0?wx_fmt=jpeg)

# 震惊！YAK-JWT靶场的通关方式竟然是...

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

先祝大家情人节快乐

然而作为一头单身奋斗牛，超级牛表示：

心中无爱人，工作自然神

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZdbUQQ4XHENEjzic4cMLR2oXfg0ShSMGjwwEDx4bxgyV8WyFK2qicCw8EWWxpmjyOwaAVt6ypzFLLjg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUexITo4H4zK76YASJx2GibdZaOvZic9diaqUlcBRkwHNxjxrpwRTPnuQ9Q/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUZnYaHYl3h0sKdVTiacBNpqMXnBJOgRq2pvlvuKiaakok2mFbiawDwGS2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDU3icLGBWeetibGhCFZLEUJUtCLde0lQcuicEWiabjyBPNl46Oic5Kzs5ZbPg/640?wx_fmt=png&from=appmsg)

打开jwt靶场是一个登录页面

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUfTLKMicZybKjCXdwXJSMd4hrFOJfmcHUUkWDhAwoUGvONmtYPCxSlyQ/640?wx_fmt=png&from=appmsg)

尝试弱口令admin/admin成功登录。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUbc6EvIugxBdVHC3dibQpYfYzNF4sppPv8Wmed6MBSVdaas2Sxrm61hw/640?wx_fmt=png&from=appmsg)

通过抓包可以看到，整个登录过程主要是3个请求：

第一个页面：**https://127.0.0.1:8080/jwt/unsafe-login1** （GET请求）

这个页面是登录首页，通过localStorage从会话中读取VULINBOX\_JWT变量，如果存在则通过这个jwt请求/jwt/unsafe-login1/profile，获取用户信息并展示。否则显示登录页面。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUO5ZwlDUVd4mekhUGLO7kialibWzLY6BFOZn5SFMPTHUjjOj1KktuPYmw/640?wx_fmt=png&from=appmsg)

第二个页面：**https://127.0.0.1:8080/jwt/unsafe-login1** （POST请求）

同在/jwt/unsafe-login1页面，通过POST请求发送认证信息，如果成功则返回jwt，否则返回认证失败的错误

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUsJS2FGGuxlMNFrV5nB9tv4sLeQ5Tib4iasuqdThphLxF9xLH3hEdZVfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUEQM8ib0G6vYZrCiaZWJHnARJelKJGPESRicayzjIe1qicgYUibdpKiac3sew/640?wx_fmt=png&from=appmsg)

第三个页面：**https://127.0.0.1:8080/jwt/unsafe-login1/profile**

通过Authorization将jwt传递给后端，如果验证成功则返回用户信息，否则返回认证失败的提示

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUtZ8knicOOOXbNWib5jQOTSUBel0uvfuIibWW3SO4QH1BmCDtRHlBbCx4A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUe8T4P1J5QibpnPlroAvzF3pEdcDlNk584k3Q6xCI8ficjZS6Vhm2j5cQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUsLdetPmpoopyV0yBtLomrj5nXhzF3lxHIpQG2uNt8rZMltPM0R7ibCA/640?wx_fmt=png&from=appmsg)

用户首先通过用户名密码向后端请求得到jwt，再通过jwt向后端请求得到完整用户信息，并将信息展示在前端。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUX9uoZn4y9kH9ic7A9lhYoCZgBTFHVXRicQibR9m0BZLsicicOqeJdF7AwQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUqJVtWT654egmjTszWuWEzwz1uG5K86tticRMs7uRWTkwwQcXtL5e1cg/640?wx_fmt=png&from=appmsg)

首先打开JWT的登录(未验证算法)案例，在这个案例中，后端未校验加密算法，将根据用户传递的加密算法解密验证jwt。

如图是正常的jwt结构。可以看到在header中存储了用户名，根据页面提示，游戏目标是**为用户信息添加flag字段**。所以我们的目标就是修改jwt内的header，并绕过后端的校验。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUgYNOBCXiaGB6fWFoX0PwYibjxU4zu210SoxLvY92ukzEX249AJC6PibJw/640?wx_fmt=png&from=appmsg)

首先了解一下jwt结构：jwt由3部分组成，使用.连接，第一部分是header信息，第二部分是Claims信息，第三部分是签名。

如果使用node方式生成jwt那header部分和Claims部分都是直接通过base64编码，签名为空，那可以编写脚本：

```
```
header = codec.EncodeBase64(json.dumps({        "age": 25,        "alg": "none",        "kid": 1,        "typ": "JWT",        "username": "admin",        "flag":1,    }))claims = codec.EncodeBase64(json.dumps({
    }))
println("%s.%s."%[header,claims])
```
```

通过webfuzzer将刚生成的jwt发送到/jwt/unsafe-login1/profile接口，发现这次返回值只有一个flag

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUa5LCAjhPcAm6NpGuXYCib2jkGH1eZKqdomrfmNreN6ZXCfo6ial7lFdQ/640?wx_fmt=png&from=appmsg)

通过mitm抓包改包修改jwt可以看到通关页面

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUViaa7KVKiaGhkQMRZVuOibYMF1d3aIWEMjZ9zmmicQtkCFRMLEg5iaBrPFw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUNsq6Cuxk9voiagvJvd3LqG90evXEmIEVC75XLnnL8aOj7bOKMAwqZhA/640?wx_fmt=png&from=appmsg)

打开案例：登录(错误中泄漏key)

和案例1相同的页面，发现获取用户信息的接口改为了**/jwt/unsafe-login2/profile**。尝试使用案例1的手段发现报错：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUDVLU2wnZomXHhTtfD1lSxTkibibColMWvT37Fa6xd5p9XR0QJ7lCibeXQ/640?wx_fmt=png&from=appmsg)

可以看到原因是禁用了none的认证方式：'none' signature type is not allowed，但从错误中可以看到泄漏的key。

key是一个byte数组，所以可以编写yak代码，通过泄漏的key生成修改后的jwt：

```
key = []byte{100,89,84,117,75,83,66,116,72,120,88,98,73,109,110,70,99,74,97,75}jwtStr = jwt.JWTGenerateEx("HS256", {        "flag":1,    },{}, key)~println(jwtStr)
```

将生成的jwt应用到/jwt/unsafe-login2/profile接口，得到返回数据

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDU4VIMjjb0XLfIzV6YJaqtiaMafv1FOibAVE65KPHnSU8mj5ZD6Rvq2cGw/640?wx_fmt=png&from=appmsg)

从前端页面可以看到修改成功

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUViaa7KVKiaGhkQMRZVuOibYMF1d3aIWEMjZ9zmmicQtkCFRMLEg5iaBrPFw/640?wx_fmt=png&from=appmsg)

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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