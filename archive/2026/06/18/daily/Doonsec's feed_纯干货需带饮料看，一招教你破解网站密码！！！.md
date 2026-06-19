---
title: 纯干货需带饮料看，一招教你破解网站密码！！！
url: https://mp.weixin.qq.com/s/RhOudxmZZPsfZ5P7QP1sAg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:19.043616
---

# 纯干货需带饮料看，一招教你破解网站密码！！！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QJTLZsy5trHKqibQfKiajGic4HNuuic5Ec67pFcc3f6x3Pqp6rzCgPia94pzNWxz9udzdPq5al4uh1dnn8ia8zWUy4orWPWQh34kTG36DQYia0JVhs/0?wx_fmt=jpeg)

# 纯干货需带饮料看，一招教你破解网站密码！！！

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# **免责声明：******严格禁止**对任何未授权系统/网络进行扫描、攻击或入侵。 禁止制作/传播恶意程序，禁止参与任何网络犯罪。如擅自将本文实验技术用于非法用途，一切法律后果及责任由行为人独立承担，与作者无关。******

# **验证机制之绕过验证码前端验证**

## **实验目的**

通过本实验，掌握使用字典暴力破解绕过验证码在前端验证的逻辑，从而爆破出用户名密码登录。

## **实验环境**

·操作机：Win10
用户名：Administrator
密码：Sangfor!7890

·靶机：Apache + PHP

·实验地址：http://ip/pikachu/vul/burteforce/bf\_client.php

## **实验原理**

登录页面在设置用户名和密码的时候，没有遵循密码设置规则，但是增加了验证码，需要输入验证码，而验证码的逻辑又放在前端，通过抓包发现后台不会对输入错误的验证码进行验证，在浏览器中，输入错误的验证码是有提示的。前端设置的验证码如同虚设，后端又不会对验证码进行验证。那么可以略过验证码，直接进行暴力破解就可以了，借助字典利用穷举法将所有可能的用户名和密码一一尝试，进行蛮力攻击，最后暴力破解出用户名和密码，绕过验证机制。

## **实验步骤**

1、登录"Attack"操作机，打开浏览器，访问http://ip/pikachu/vul/burteforce/bf\_client.php

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGljEgOcZ6Nzbic6MrMkvvE1k2GibSjXVSA6Z59h0HDEXkOUDCuYP6KbsseOwZqsC244PQSgYnMLlyvYhfIjrbYsH4cIGvicqrfNQ/640?wx_fmt=png&from=appmsg)

2、随便输入用户名为：“root”，密码为“123456”以及随意验证码进行提交，弹框提示验证码输入错误

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHB9eWib6zY9j91IWiagibOlibEJdSOPkgQOCY7ocvpRYZqHufKXEghcDqdm79gv56wDXcPd0WAVX7goyHnFibj8aoD5jhRlka8ZFw4/640?wx_fmt=png&from=appmsg)

3、点击“确定”，还是随便输入用户名为：“root”，密码为“123456”以及正确验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHzgBIy3Qoxj62ydf7XHHf8dZOYG208t7CKY47MIlCibuUupkONHLlgMTlic8EOlRL1oGpicP1k2HpLtzplUTcOkiczsW9IkdW6td4/640?wx_fmt=png&from=appmsg)

4、打开桌面的的“Burp”文件夹，双击“BURP.cmd”启动Burp Suite抓包工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHESeZuTib2x1EE2MwQQCiaoy3kkP4dY8qdMyDYM5tic041zyBicBNu1NrOJHU3Btqvg5OGoH8s1sLsrp0fMu6xRBWgicH50aDXQGf8/640?wx_fmt=png&from=appmsg)

5、切换到“Proxy”代理模块的“Options”，查看Bp的代理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEaRrRdRrPbBicibOSJ9yTJiap2l6CQicUVfDy29vcqpWSgicwhGjWrQTqz1wj4HGkx3X151L5qHcWDPst93yZGaj6ymr9AvPgmLNPQ/640?wx_fmt=png&from=appmsg)

6、切换到浏览器，选择火狐插件中的代理（配置浏览器的的代理），与Bp的代理一致

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEquQ7rEbnh7ic7viav0Efjl682G9f8ktA4lFiakKMtNaicsME8KibjibicYxe0otrx3abSPwqr2ic5HgQkqRCysXh0ngbQwXGoybbiajME/640?wx_fmt=png&from=appmsg)

7、点击“Login”，提交输入的用户名、密码以及验证码，Bp成功抓取数据包（验证码输入错误时，无法抓取到数据包，只有验证码输入正确时才能抓到数据包，由此可以判断验证码的验证逻辑在前端）

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trE6ytrPicV0j7NkTWgW2THkllIic5zUV09nehiaZpnlYsiaDzbn7mibTaCFzXP9snZVMLiacKibvlqbFjxkI24A6icpujKteTqled8C10A/640?wx_fmt=png&from=appmsg)

8、右键，选择“Send to Intruder”以及“Send to Repeater”，分别将数据包发送到暴破模块和重发模块

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEjlLbtic4JpibmDfkpjLm2vGvoSgylWju7qgynQmiaqfgNqtvey6IQR4kTibT1JTCoeEHL6A6BYTmCXtZLJpQwibEPc7RSYicN2Aydg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG9JNFZD9KCNwoOjkJv98awQEbKkibFyeSIfNl6Q6EAJUVck2xCzUoH8XiaWzO2e10uxYlCMMWMIzXCKkgibQ5aIcKYqNG3Dbu8Gk/640?wx_fmt=png&from=appmsg)

9、在“Repeater”中对数据包修改验证码为任意，然后点击“Send”放包，查看响应包发现后台不会对输入错误的验证码进行验证，在浏览器中，输入错误的验证码是有提示的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFo6Yu4fPSuicicY4ycSJiaShQuzibgsv0GeVcBIvq2W6EqHiaMxBEgcelTp2wic2NQs3kCA2nRoH5sGyk9tLwngkfzcEIfAktciajr1s/640?wx_fmt=png&from=appmsg)

10、切换到浏览器，右键选择“查看页面源代码”，浏览代码中发现验证码的验证逻辑是在客户端的实现规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGWyhFb02qGXFJAJOOgPbWfJNxSV8K10umObpOLwBHdbfM0Q1Ej1JZD5y0jeaNylpd4xH3dGoWqWxJiaz5SkAl46Hjuoc9dR2a0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGjFVVxOKt0YvgSQicnUfSr0wSB96CiaAbCtcGwdKbAGwibZJPZp0R3BjTxt7GZ3lcB0hBxoHAT3DicpiaJyMkBDQce5BQBCZJCBjhw/640?wx_fmt=png&from=appmsg)

11、通过前端验证码的验证逻辑的代码可以发现Javascript会从0-9和26个大写字母中随机挑选5个作为验证码，然后用 validate() 去验证，并且每点一次验证码，就会调用 createCode() 改变验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH2AKLQc2iaCiawFXX9z2YSzuLCsFNOCZlAWnMqdWZsiacbia17ibPkKCndAdmibkWcgnnqiafRbua0o8povYb9KJ9pudATxmvv1of1mE/640?wx_fmt=png&from=appmsg)

12、前端设置的验证码如同虚设，后端不会对验证码进行验证。那么不用理会验证码，直接进行暴力破解。切换到BurpSuite的的“Intruder”模块

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGDSV3IKdsZ8bCywVy2A5ich4PFpcDtjsOtibY1bx3IDjxryy8p27w4oF6fJpjkiaQlNA1DJmuysVzoudNbGDZ6jr0XukS3bISm88/640?wx_fmt=png&from=appmsg)

13、点击“Clear §”，清除所有Payload位置标志，重新选择“username”和“password”两个需要爆破的位置标志，点击“Add §”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGlmPq7YDjQwP8Bh2poGg0R8heiamCc38Om7vcAdgicr8XfeTrGkDTUcvxHchR9s9wBCq10GfsvU2A7RgVp6otgoZicCyWpF4sHyI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGx2eFF5ZsyicyAq3k7odv34TTymkpbria7DrfGdyLdPNBKSZibzypI8St4mkus225z2icteQlV6oicUtQ0s4ESOrpLxtib3rbZ0ibYLY/640?wx_fmt=png&from=appmsg)

14、将攻击模式设置为“Cluster bomb”

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFFhWxh9EzsSMiaTnwlV9riaf9hF4jpfVYOx4Ypvrvb7u5Py7gtMX7QXhSrhk6Mj5xv1gcvrL2YGLlUQqJDf7FnZQJ823ho8d9Y8/640?wx_fmt=png&from=appmsg)

15、切换到“Payloads”，设置攻击载荷。设置攻击位置1的payload类型为"Simple list"，并加载用户名字典

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG4Y3vDaLV0QkgMFmjcLRNLwicic5rHibB9IWNMZGacHmz5s3UmVjqzX02SxFvIqhB9AYxa7cGcyzlLQ68wztRQ3dI8D0anZhklO8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHO6BKE5UBuxQichvjMAdQ9mI2tD73wkB7cIGAU7RzVktMLsnAb6vXHeEUpWqQ74nicpwaTtDNicdX7GFcXJDMyJmh2HbfQBrLKOM/640?wx_fmt=png&from=appmsg)

16、设置攻击位置2的payload类型为"Simple list"，并加载密码字典

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHCwDGeuzMYjUdJS42j76mvHLHv9BfafMcZUug2dv8cau6NP8Z2HhCUPkpzaibiaP4ibicReAfIFIzJiaN21E24RApY0KhXpf8UkiaCY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHvOXwp64fdHjE6IcgsX3KyHOdW4c5Da2MfVtDvve7nLaOHKpvUXe9xQNT7hQclYbdiaWDctIu2JUrysQfPFreLNnicUuTANSbibo/640?wx_fmt=png&from=appmsg)

17、点击“Start attack”，开始暴力破解，暴破成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGI15qTp7jibfuT0IicxB5gzibtaBl163kjhyp7WibXatwER9XxhJJcM844iamvbxFI4CibHPn9AmFKwL1dlvPUoXz9ibYlJ8GjXIkE1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trETMVwePpxe3tRicwd9hFwyZjGJIvR2Q94JgibMIPzPyZiaEs7XycWFtsCwM6cN68OSUgodVibyWOaiaEK8gNf7RrTey6IMlbTAR5SE/640?wx_fmt=png&from=appmsg)

## **实验总结**

通过本实验，掌握在遇到登录页面增加有验证码验证，首先判断是前端验证还是后端验证，前端设置的验证码如同虚设，就可以略过验证码，直接使用字典暴力破解，对暴破的结果根据长度进行分析，长度值与其他不同的就是正确结果，从而绕过登录验证机制。

更多学习资料点击头像关注公众号，后台私信回复666即可领取视频学习资料。

推荐以下书籍配合实验一起理解，适用零基础想学习网安的小白，欢迎下单！！！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

建哥聊安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

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