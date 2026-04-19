---
title: 一文读懂JWT常见安全问题
url: https://mp.weixin.qq.com/s/ZrELunMetRsgGPY8wZWCtw
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:48:16.754401
---

# 一文读懂JWT常见安全问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m43aPn9XEfN0ibAa18QFL3j4FrWQpzr9A2ejXkgNJZzg6LTcQBR5wmmwAOKNjZWdVx57EoklUO6xwXqk89dXYsHCc79iaNYCfibbtG8wEC3quo/0?wx_fmt=jpeg)

# 一文读懂JWT常见安全问题

原创

deepsec
deepsec

深安安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在现代Web应用中，JWT（JSON Web Token）已经成为非常主流的身份认证方式。无论是微服务架构、前后端分离，还是移动端API认证，都经常能看到JWT的身影。

但在实际安全测试中，JWT相关漏洞却屡见不鲜。很多问题并不是JWT本身设计缺陷，而是**开发实现不当或安全意识不足**导致的。

**JWT基本结构**

![](https://mmbiz.qpic.cn/mmbiz_png/m43aPn9XEfNEkGbOnibIOb7JhasrTxxaPoPzlo7TGuiadJGPmGricJt0l7qfuia6CL8luFcdBibBYhWMbYkkYL7d9M7azEib6qiaztaadicIa0bKSyo/640?wx_fmt=png&from=appmsg)

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

.

eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ

.

blW\_oiHH0uX4NBhC8K83a1EHWKhNJCxTyGyDMwK6dPU

JWT本质上由三部分组成：

Header.Payload.Signature。

Header：用于说明签名算法。

Payload：存储用户信息和声明。

Signature：用于验证Token是否被篡改。

需要注意：JWT只是Base64编码，不是加密。

**Header：**

{

"alg":"HS256",

"typ": "JWT"

}

**Payload：**

{

"user":"admin", "role": "admin"

}

**Signature：**

HMACSHA256(base64UrlEncode(header)+"."+base64UrlEncode(payload), secret)

**JWT存在的常见安全问题**

**01**

**alg=none漏洞**

早期JWT规范支持一种算法：alg=none，表示**不进行签名验证**。

如果服务端没有强制指定算法，攻击者就可以构造一个**没有签名的JWT**。

攻击流程：

1️⃣获取一个正常Token

2️⃣修改Header

{

 "alg": "none",

  "typ": "JWT"

}

3️⃣删除Signature

如果服务器仍然接受Token，就可以**伪造任意身份**。

攻击者可以直接篡改Payload部分形成越权，例如构造管理员凭证，从而获得管理员权限。

{

 "user": "admin"

}

**02**

**HS256/RS256算法混淆攻击**

JWT常见两种算法：

* 对称加密：HS256
* 非对称加密（公钥+私钥）：RS256

在验证JWT的过程中，如果代码逻辑是为非对称加密算法（如RS256）设计的，它会直接使用公钥进行验签。但当开发者没有对传入的alg参数做严格限制时，攻击者可以传入一个使用对称加密算法（如HS256）签名的JWT。

如果此时服务器的验证逻辑不变，它可能会错误地将本应用于**验证**的**公钥**，当作了对称加密算法的**签名密钥**来使用。在公钥容易被泄露（例如通过/.well-known/jwks.json等接口）的情况下，攻击者便可伪造通过校验的JWT。

攻击者可以：

1. 将Header改为alg: HS256
2. 使用泄露的服务器公钥作为HMAC密钥重新签名

服务器验证时会认为签名合法。

示例

首先，通过公开接口收集到服务器的公钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m43aPn9XEfOI9QBt8Iy7MmicXufxRowIXIFLsvoNJrtx1QCPpEMaibuhuibPvnAM8q6D707fEdOHibamsKWh5BLGAUh5ibDhtLhwvZ3TbXHibucxI/640?wx_fmt=png&from=appmsg)

使用工具将其转换为PEM格式，并保存到本地文件public.pem。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m43aPn9XEfP98cdic6SXnKfWlOWKaic3mjYIEicnRKYBBToQVqAs3PXlR1L6vsZXBJ0ypicxSCLGBsW0uEgMKkjliaajPJysCLc2LxF74giaG16gw/640?wx_fmt=png&from=appmsg)

使用jwt\_tool执行攻击，将alg修改为HS256并用获取到的公钥作为密钥来签名，构造一个新的JWT，成功将权限提升到administrator。

python .\jwt\_tool.py -t https://example.com/admin -rc 'session=eyJraWQiOiI5ODY4YTliOC0zYzM3LTRiZDctOTI0YS0xMzUwNWRmODc3YmYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc1MzAwMDg1Nywic3ViIjoid2llbmVyIn0.Wjv2YdNi1l\_XgUUqHISF9OGbiWUtGbqaRMjVqRgSV\_2Pq3J8omvvmC-qrdMm1s\_76pryxd6TZyLsMQETbtOayD5SR4Hym-U9v6XmfEYVmEQAvrLhvUJYni7oMnq9RHLNUiSvBTZXjCrkcLk2GKs-pp9C3vLGInjGhhYBQGX-YlWF9I-S5-lc\_GiW5lCWlVbqS8BopQG0QaSBZcPS4zcBxxlzj5CCGdIlP38VajiLY5q0I-3SfBlnyOtVpIhHQrFMONlqESYH6gyKOj1uuRaNR3UWk6dasGBHnCRKpwwskXm8gHzMZDjGFbkwRi7pfQ1bwWud9mko1q8leO6A-gcN3g' -np -I -pc "sub" -pv "administrator" -X k -pk public.pem

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m43aPn9XEfOBeHOmlzGYOHTnWxia7TEvHpAuNwLmoZug3eicN7Z2J7jribzwRJTe7EXxF7DbE1w8rsvxica0CYftsqQrlICg6wYkWMlp4cRGqYU/640?wx_fmt=png&from=appmsg)

替换JWT并重放数据包，则攻击成功。

**03**

**弱密钥导致Token爆破**

如果系统使用：HS256，并且密钥过于简单，例如：secret、123456、password、jwtsecret，攻击者可以离线暴力破解密钥。

常见工具有hashcat、John the Ripper、jwt\_tool。

示例

hashcat -m 16500 jwt.txt wordlist.txt

一旦密钥被破解：攻击者就可以随意生成Token。

**04**

**未验证签名**

有些开发者为了调试方便，会关闭签名验证：

jwt.decode(token,options={"verify\_signature":False})

或者

verify=False

此时服务器只解析Payload，而不验证Signature。

攻击者只需要：1️⃣Base64解码Payload 2️⃣修改权限 3️⃣再编码回去

例如：

role=user → role=admin

服务器仍然会信任Token。

**05**

**JWT信息泄露**

很多开发者误认为JWT是加密的，因此把敏感信息放入Payload。

例如：

{"username":"admin", "password":"123456"}

但JWT只是Base64编码：任何人都可以轻松解码。

echo payload | base64 -d

常见泄露信息：用户密码、手机号、邮箱、内部 ID、权限信息。

**06**

**Token没有过期时间**

JWT应该包含时间字段：

* exp过期时间
* nbf生效时间
* iat签发时间

如果没有设置过期时间，Token可能永久有效。

一旦Token被窃取，攻击者可以长期使用该Token登录系统。

**07**

**多实例固定密钥导致的重放攻击**

JWT是**无状态认证**，服务器通常不会保存Token状态。

因此如果供应链厂商运维人员在部署时没有根据不同的安装单位生成新的密钥，而是使用了开发环境源码中的固定密钥，则攻击者可以在存在弱口令的系统A获取到管理员权限token并在本单位的相同系统中进行重放，从而获取到管理员权限。

**08**

**通过kid参数注入自签名JWT**

JWT Header中有一个字段kid用于指定密钥ID。

{"alg": "RS256", "kid": "key1"}

如果服务器把kid参数的值当作一个文件名（或文件路径的一部分），然后从硬盘上读取这个文件的内容来作为验证用的密钥，而没有对kid进行过滤，则存在安全风险。

攻击者可能构造：

kid = ../../../../../../../dev/null

并将密钥指定为空字节将用户提权到 管理员权限，例如使用jwt\_tool进行攻击：

python .\jwt\_tool.py -t https://example.com/admin -rc 'session=eyJraWQiOiJhNjIyM2FhZS0zNGVhLTQ3ZGYtOGI1OC1kZWE3MzNlZjQwZDIiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc1Mjk5NjcyMiwic3ViIjoid2llbmVyIn0.dtLkZnYfOd5Ls6yWGZ98w5ONT5kVwHgbHpJ5LeO5ubE' -np -I -pc "sub" -pv "administrator" -hc "kid" -hv "../../../../../../../dev/null" -X b

![](https://mmbiz.qpic.cn/mmbiz_png/m43aPn9XEfPicHGyjS47ZaN2Q3KBVfX6VNQoPW0RicXXqGicNaHqPWnwE7EL0M7gL0l1I95zxcksa5Qw4MPJRotLoicG6CEgC9ibL0fQknqn4qr8/640?wx_fmt=png&from=appmsg)

使用新的JWT重放数据包，则可以攻击成功。

**JWT安全最佳实践**

为了避免上述问题，建议遵循以下安全策略：

强制指定算法为非对称算法

例如

jwt.decode(token,key,algorithms=["RS256"])

避免服务器接受来自用户的公钥签名token。

使用强密钥

密钥长度建议≥256 bit避免弱密钥爆破。

设置过期时间

Token必须包含：exp过期时间；nbf生效时间；iat签发时间，并设置合理的有效期。

不在Payload中存储敏感信息

JWT不是加密存储，不要放密码、手机、身份证号。

部署时强制生成新密钥

建议部署时强制生成新的密钥以防止来自供应链的JWT重放攻击。

必要时实现Token黑名单

当用户：

* 退出登录
* 修改密码
* 权限变更

可以将旧Token加入黑名单。

**总结**

JWT在现代Web架构中非常重要，但安全问题往往来自实现细节。总结一下JWT的常见风险：

* 算法漏洞（none/algorithm confusion）
* 密钥问题（弱密钥/泄露）
* 实现问题（不验证签名）
* 设计问题（无过期/重放攻击）
* 使用问题（信息泄露/存储不安全）

只有在设计、实现、部署各个阶段都考虑安全，JWT才能真正发挥它的优势。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Qsk04gN6ImpTtW2B4fKZubqr4ujoXBwAHLjQV5e60UPB5ZFHjE3bGtibTibBaVGZgJT2iaro7rZ3LrM2iaewXbLhBQ/0?wx_fmt=png)

深安安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Qsk04gN6ImpTtW2B4fKZubqr4ujoXBwAHLjQV5e60UPB5ZFHjE3bGtibTibBaVGZgJT2iaro7rZ3LrM2iaewXbLhBQ/0?wx_fmt=png)

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