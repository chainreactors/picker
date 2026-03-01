---
title: 从0-1学习JS逆向（上篇，基础入门）
url: https://mp.weixin.qq.com/s/Vj-FKfrSazfhX8qYktEmCw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:26:39.334365
---

# 从0-1学习JS逆向（上篇，基础入门）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QLbB9SNicNBSaFzEGSDoyyIepia6myicuLVgpJNhjxYAJiaCvRPSaOibYQ4ajQFG94P5nVUricib1yR6g5icaJgrm6nkvDcTkYEicYJUicPBzicicVl0QPo/0?wx_fmt=jpeg)

# 从0-1学习JS逆向（上篇，基础入门）

原创

凌曦安全
凌曦安全

凌曦安全

![]()

在小说阅读器中沉浸阅读

本推文提供的信息、技术和方法仅用于教育目的。文中讨论的所有案例和技术均旨在帮助读者更好地理解相关安全问题，并采取适当的防护措施来保护自身系统免受攻击。

严禁将本文中的任何信息用于非法目的或对任何未经许可的系统进行测试。未经授权尝试访问计算机系统或数据是违法行为，可能会导致法律后果。

作者不对因阅读本文后采取的任何行动所造成的任何形式的损害负责，包括但不限于直接、间接、特殊、附带或后果性的损害。用户应自行承担使用这些信息的风险。我们鼓励所有读者遵守法律法规，负责任地使用技术知识，共同维护网络空间的安全与和谐。

本文首发于掌控社区：[js逆向学习保姆级教程从0-1(附详细案例，看完包学会！)](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247552680&idx=1&sn=ef42334ee4b48e2bd850753784b7c2fa&scene=21#wechat_redirect)

# 为什么要逆向js？

因为装逼是一辈子的事。随着越来越多的web网站或者小程序为了安全，都加入了加密或者防重放，可以防止百分之90的安全问题。你不会逆那就没饭吃。如下所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTjfmuibBnBR5aH3TngAjKs2R9TwIALtGQFBTlAFkDvyBqSM0sP3RkTicqeMdQnNgwEFzR3jB1Nu83apVh0ZoiagwWc84hbVHHR3Y/640?wx_fmt=png&from=appmsg)

那么，如果你会逆向js，解开密文=乱杀，因为很多开发以为做了加密，就会放松警惕，不会再对输入进行解密后的二次过滤。同时还有一个天然优势，waf无法识别密文，也就无法拦截。

如下所示：解开密文后，遍历id达到全站越权

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRM2G5fZwicXxo2axfLy6p6B8SOZCwDJhdTmIHeFwc8O70yj9NAy1uOkrvhrv14ia4Tib1lLwX9UAeRjOA7icvqdIDKUrteYqu7JRI/640?wx_fmt=png&from=appmsg)

# 常见的js加密

https://www.ssleye.com/ssltool/ 在线加解密网站

## 对称加密

比如AES、DES等，使用的加密和解密密钥都是同一个，所以叫对称加密。一般都存储在前端，或者后端动态获取，可以直接拿到。

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQeXGCjPtxXRCicKBtK8libUWgxic3JNP6sskNSRSZkeQ6iczNY71MeINYboa4sKleumibElIxo2LTib1bt5WBzt7QCkf8tibzy9iaRcWY/640?wx_fmt=png&from=appmsg)

## 非对称加密

比如RSA和ECDSA，使用非对称加密，也就是说，加密和解密使用两个密钥，公钥一般在前端，用于加密，私钥放在后端，用于解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQ8At7fvyjiaRHgva4jo7KFz5CzDA99rCS8VYdHYwYchRdGRyMDP0kEKnm4ibcItv24u4msOAttx2szcDxBeX57Q5Ktvevu2UqM8/640?wx_fmt=png&from=appmsg)

# 如何逆向？

或者说，如何找到密钥和加密方式？先来看一个靶场，真实环境下演示。靶场：https://github.com/outlaws-bai/GalaxyDemo，用Galaxy插件自带的靶场，下载后启动

```
python3 manager.py
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTbkjOL6WqTYSCYoibibtjtgvPyKwNPLX4YzUlNH8MO9JV7eX1M9SSKCI0trdec2pVs8kQzSj5ib4bfahRQTt0Z2RScFwW8O4M2oE/640?wx_fmt=png&from=appmsg)

访问点击查询功能点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQAecsDutb6CS639pEKnod04HHRU4uIGfNg0MjsGENFZdtq0g6QZmPRt7jpvjnLGxS7buEPoowo8mNbFo4z4QU3ZkUyy1dnrO4/640?wx_fmt=png&from=appmsg)

抓包，发现是密文

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQgcy2LKnVW4llicCAw6NsgWJhG9dib5MH9pfbgQiaObqxdq0RgIpWZE1DFbkp0oibvYcCickd8uqPRSLYOtq5Xicp4s6WNc5w1iaZRyE/640?wx_fmt=png&from=appmsg)

发送的是密文，那么肯定是前端加密，要找到加密方法和密钥。

## 如何快速定位加密处代码

在实战中，肯定会有很多前端文件，所以不太可能一眼发现加密的地方

### 1. 通过字段关键字

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTocfD6m9QnibbqpLbPvCicsbFNqxY2N6KNrYGic7jXVibNyAiaEicMmRDlnibWztvGOoj403GnaLoicsRTvhwnXrX4Wk3Krtb7ibnd6gqk/640?wx_fmt=png&from=appmsg)

搜索data关键字

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTFkbNOUQjU6EnhJY8rDqH2kwh1iaOEZ9EDD1CibqNLQ49T18Nh5MW1SNME6wHWkZj3aa3CuaKdf1X2VfgeY31t6yGvFJibosribEA/640?wx_fmt=png&from=appmsg)

一个小技巧，只搜索data会出现多个，如果搜索data:就很快定位了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBRpIn0zO2HFn045pQYB8IgfsNTx1qKBXPjDCGwoFVRUwnWULwkA2gI1k0wTuTcyfIFy9DV6MicgVQTjlM62f6qKKVopY3RQT0QY/640?wx_fmt=png&from=appmsg)

然后就找到了加密方法encrypted

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBRsyaGdXTXXwYaBY1SnhG5C3E8cskfAP3OMmB1E9569krgzk1PAMpDwSiaVPuQCBicJhvibSWWw0WxoTUfJR3yFMvuHhDfFKYAyZ0/640?wx_fmt=png&from=appmsg)

在此代码全局搜索，就找到了加密的方式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBRFfPAj5EQ4c8lpBoKVKkGX46Gjw47dmia37QYscQEByZHcxfIOHRlEvLquiak5iciaJxjA6k1w31yibBJJbyYaU8rrVVr8U31diarlU/640?wx_fmt=png&from=appmsg)

### 2. 通过js关键字

通过直接搜索，加密方法调用的关键字 CryptoJS.mode

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTjoZgl8cO7cng00sNg0gTckpPjcn6XXDtia5GKI2VA5OIVhicDnDatZ5AAQp3AdiakoIBj3wJ8qw4A9iaNtfhq7TH1R6W0yib6ib4Lo/640?wx_fmt=png&from=appmsg)

或者，iv、key等等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSog72IhQVahwMicePFcAicOEVWuTkuv270ic3iaC6C6icsXp1leDrPsgNnZXSvnQLJzcUOdiagNyjF4dibSdk64tJTm5ge9XGpxaOkGw/640?wx_fmt=png&from=appmsg)

### 3. 通过路由

直接搜索请求的路由，也可以在上下文中找到加密方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQ81SO2PC5ytF3ySOzIribIBu7rSu9QFncY7E2PuWNOibvErGCtVAGvfLmzxB5JDh26Ly1aXD3DStOQqmn80liaU0xwlTo4fxwKng/640?wx_fmt=png&from=appmsg)

### 4. 通过断点

如果以上都找不到呢？没有找到已知的加密方法，或者没有找到关键字呢？自写加密，那该怎么找到关键的加密代码？这就需要使用断点，先通过发送请求的js，找到功能所对应的代码，根据断点去判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQwCAJBwIOc44bms90F4QYYVUOWEaz7cr1IAoGyjXicaJ0ZnELbj68M3vkFqN5iaCbzsvAu2OVicGzGJke2zO40GgMTOaQZEm3CD8/640?wx_fmt=png&from=appmsg)

例如此处，在功能点处打上断点，然后点击查询，跳到断点处，且功能还没触发，那么就可以慢慢看上下文，找到具体的实现方法

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBR9T2jzZHzAUSrWh4nlM8y6ksFZV74ysAibX5kEIShDXQzR51O0cJzQ9xia0ySWeTNHDSwdh9ge9zFibHyhXa18xuyIWFfUhlTdSA/640?wx_fmt=png&from=appmsg)

案例：北大某站从js逆向到账户接管

此处重置密码

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBSdIcDjLNveKoWJoibBlvpHymz9qiaCPCyhOxNzZ6ldWXqPKBBoOQpnfYsMibKBk03wJ8Ag9jazGXicpWnbMMRIf5hgFiaNYvsgf3ZQ/640?wx_fmt=png&from=appmsg)

抓包重放发现是有签名校验,且用时间戳防止重返

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSk3KQcZ4UZfZK34eGJ7f9sJia5z1ibcE1Hx8JIvPc0j59q829zBsrC9tO0ABTep3RLb3B8pXUwfaN0npS0fLvgTEcKictUGAibpsY/640?wx_fmt=png&from=appmsg)

逆向签名发现加密方式

sign的值来自函数G()

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTxRXjic00icx5HX7uNdVcKnR7clrmDDwhnTwOFUQiaR5MuUxV2mZpxmpunuBLiaYB2gc47mMRumvLK5YdYD38S2U7j6bPrfXicR1NA/640?wx_fmt=png&from=appmsg)

跟进函数G()

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQ99f8jfRsXrmlPKDweSZNO9XiaKJeEoAhAkYOQejA7gAjeOmlvgpXQ6cS6vUzsqic35bdk3DbJ0QP6dEIW3dv0p9KslbjBzZLYE/640?wx_fmt=png&from=appmsg)

发现所有的加密参数，然后编写py代码开始爆破4位短信验证码，审核的时候可以根据真实接受到的短信验证码，调整下爆破区间，密码为test321

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBRYGPcpqE762cJ16HbovPEZV7sQTGGEHy07VWqYTwL1dmP3HVOxyFALHInT7dDLMTD0NH1vS8xfVg6LjOHszTjYllGyiaauFCicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBSkvYY4iaibbVtttQqsnPpkKOYlv731sws24gziakQYKl8W7v1fLBfnaic2P6pCfn5kDZAbTKqSkY7KgibT6iceZmmD3ysaJuhCCmco0/640?wx_fmt=png&from=appmsg)

爆破完成后成功登陆

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQpQ2zNs4FaLo15AMhpWuyZicYyyQy56u0x4ia4iaiata4736gQ2Q0VxKQKRUucAvPKgA26kFSez3hqTnocvFXxUPs8UYH9uufWCNs/640?wx_fmt=png&from=appmsg)

同理，修改绑定手机号处，方法也一致

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTFPBGMN7Z7I9jTQOJeMxWXs2olgMQiaTvFPQiaoptr8sCibKLpBwveLIyURDGxNPZQOaAkKvZrNCeWSFLqaMonymOrvuw58icRXaU/640?wx_fmt=png&from=appmsg)

请求包参数一致

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTia9A15JjKRoRVTdGcGNjeH1GZT7Yk1Viao5mRwcEy9zR3lsYLrQTicZKUhKtACpI583Tiaf44znk1UdCvicJicyeh202pRib6xTHSpc/640?wx_fmt=png&from=appmsg)

# 获取手机号

测此处，需要先提交一条。此处可以看到我只有一条，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSb5NMp6dHgcibat34qE56Xz4OoGhlXJyfrCO5ZLNs5icboUHXj6xqsYtuvTNPZhRK5nxtKDHe6PIgBAHm0B26jVBeOPTd16CUpY/640?wx_fmt=png&from=appmsg)

通过替换这些参数，遍历

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQps5lgr2C5wicrBRiaQibdm4OuCSC7gpD7C4cdPx3bpkGULUwx2hzMPLbO4d3oOtcZdwS6JhpibgTARnSlaPRlgvU62I7z3G3ck4k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQOjEccj31j0NxhXNp0LvpELOOFok3K5Ih5MvyZw5YUN3rTt43Kgdq0vicRD8TDic5KK3PibEHhwJLguzGnfCPcJbsTJCkSNAemOk/640?wx_fmt=png&from=appmsg)

用脚本加密，可以看到是一样的，只需要修改一下数字遍历即可

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRmddF8PyxOqwL2jyZsqWuibR4lLt2ByuE3ibXlS63KuNN3S65RjkcuawDiaxArB6SXg6g0Tj3eYGbVzMUUpCAuTgXG43rs149SeA/640?wx_fmt=png&from=appmsg)

查看其他人的评论

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTDrm3TpCdFjrOib8wpp5Sq71l4OzL5LHibg5YpvPn0XqhuvmVQ1jTcp0RqhksMWwNXKLsPdHJbU0E6Y53FMAcQmlzECYE0WnXGU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRWgUwP0efXsSibnX1dVHLYVNDKUsicib3ltvWD6pSWI5z3iaXf2NM1EtyLEwCXRRqTZknXmKr9GjLby9z2sgz7hR14hzIjGZp5gDQ/640?wx_fmt=png&from=appmsg)

拿到手机号可以实现部分账号接管

# 解密

可以通过在线网站直接解开，但是每次都需要反复加解密，很麻烦，而且也不好配合sqlmap等工具

![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRgX0vEFBb6LnrcibibSda9bePx2HuVC8MVkiajwmaWFzeVOXOU91sEpEJ1wSFVbic6dKRxicOGGRicp9jv2KgmUL3aRgIiayaZ1aCK7I/640?wx_fmt=png&from=appmsg)

但是像验证码爆破这种，可以通过自写脚本，来的更快...