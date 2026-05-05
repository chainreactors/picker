---
title: JWT：渗透测试姿势全解析（含实战）
url: https://mp.weixin.qq.com/s/8Zf4v1IiHDNpjGIJfokDGQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:02:31.959557
---

# JWT：渗透测试姿势全解析（含实战）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFGzGYkvCwuZuwGVibP2ozRcZlnVQ1ZVfrSxyV5nen3aUOumWWgUQriaOS1eBShpbFyywGJobjicBLicL31eOQ1Z95kqDZ0DEzkd3oE/0?wx_fmt=jpeg)

# JWT：渗透测试姿势全解析（含实战）

hkl1x
hkl1x

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 导语

###### 师傅们在渗透测试做越权时，尤其是小程序的资产会经常看到cookie的字段是以eyj开头的字符串，不乏会有些头痛，没办法修改一些敏感字段从而达到越权。这就是jwt（JSON Web Token）。下面我会对jwt的渗透姿势有一个详细的讲解。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHAkloKHTP7icDncEhcq6ILWcukyeIjdGBD5gAkxF3kjGsE7RTn2ZZeRgsbYMljiaNicV5FQhHicnq5btWyvwRkbD2SFVgCIjOVib4k/640?wx_fmt=jpeg&from=appmsg)

## 原理

###### 简单来说jwt就是一个身份认证的字符串，有三部分组成：第一部分是头部（Header），第二部分是载荷（Payload），第三部分是签名（Signature）。每个部分有.分割并且通过base64编码。对于我们来说其实只需要关注前两个部分。下面我会分别解释这两个部分。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGdvdnZbicrfHXzVdiaztvn39pw8M88yrv6ibJCZWFjboVxNqrn78LxJXIo1NeGHbs8ibhJzPiap7B1x3ibeibGfYhtYBHygCWl3LJOkQ/640?wx_fmt=jpeg&from=appmsg)

### Header

###### Header部分的功能简单来说就是定义了这个jwt的加密算法和识别签名的密钥。这两个功能分别对应Header部分的alg，kid这两个参数。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHHMxWxciceSfBwfaNwX1zhiaqTdXVWEv96DB9elsIaibRTcazK9l58oxZ2gibDHiazWgScCgw3Ab7vwJHGZThPkEGx6FhSIxxNX4pE/640?wx_fmt=jpeg&from=appmsg)

### Payload

###### Payload部分其实也就是这个字符串的核心包含身份认证的字段。下图的用户字段是sub实战情况下uid、userid这些也都可能。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHlo1twH8PDChm2GkKGEpfjzaDh0x9y0rDfnefQ8HKuoD4dbAz2DyYm5HsASGZbm0M2PSPLucI2HI1YRwZwOiasRZVe0uCeKtEY/640?wx_fmt=jpeg&from=appmsg)

###### 那就想问了那我在这里直接改不就好了，这个话说的对，也不对。这个要说一下jwt的工作原理：我们上面的Header和Payload部分在进行base64编码还会通过算法密钥进行加密，如果更改这两部分的一些参数会导致整个字符串更改。从而无法进行过越权。这个也是是否产生漏洞的核心

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGISh2E2HZKAb86thWNlXODzlmdjYbiath9YDY8YjHE8fy7K9XGytdYibhDUnC3BSibD8kLFBlia4CAy2ao5nCL4oQuJpl69fnJqgM/640?wx_fmt=jpeg&from=appmsg)

## 姿势

### 有缺陷的jwt校验

###### 原理：JWT库有两个处理令牌的方法，在Node.js中，有verify()和decode()方法，分别进行验证令牌和解码令牌的操作。那么开发者在对令牌校验是使用的是decode()，说明就没有对签名进行检测。就存在安全问题。这也是上面说对也不对的原因。

> verify() 方法：用于验证令牌的签名是否有效，同时解码令牌内容。如果签名无效，该方法会抛出错误。
> decode() 方法：仅用于解码令牌内容，不解密或验证签名。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFEVQmIAdzXpOKXTRPo7LyicicGichib7ibtmOrDOE4VIblwyNdODEfuIagicq3wib7ra8MT1o1iaaZ35QoIdpPhPbIN6maNDib7mr2Iibszw/640?wx_fmt=jpeg&from=appmsg)

###### 案例主要来自bp靶场还有一个实际案例。下面可是我们第一个实验。登录后生成jwt。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFH9VSU2qywZicSxXjyjuf8abNxicWTYRicCC6KpjraicoHGnibbC9ex2tq0SvycEib3H0mLkylFExDU8dX8VRNqCPryqes2uAcTjUOcs/640?wx_fmt=jpeg&from=appmsg)

###### 放到jwt解析网站，更改其sub字段为administrator。（网站：https://www.jsongj.com/ede/jwt）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHQEAgEyjsYAiasWicyfUd8Sg7mejPz3Jf8MlibkUyhezlUibKnalveX3ibrnibr7uoCiajj1A4PHLHle6NsMXlPwoosD58DzFoWTINCc/640?wx_fmt=jpeg&from=appmsg)

###### 我们可以看到这里的签名是随机的，按照jwt的工作原理这个是不行的。但是这个是存在漏洞的。然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHFWT0X2xrsG6IhVgbjPibWN0tNM7euciayIdSBAzTszkjsqDpsNY5vkbvpiafXibmDn7ibtibpjVRXzX62XujbrUoOD5Z7prrbFZD5U/640?wx_fmt=jpeg&from=appmsg)

### 空密码算法

###### 原理：开发者没有对jwt的算法类型严格校验，就存在安全问题。我们上面说过alg参数是决定jwt算法的类型，那么是空算法会导致密钥也不会生效。从而达到越权。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFH7Zjb0FqMs2QqAVOx0kglScZDVNl9qKxJKJ1LW5GibqOBLbNicSznM1GyfJbyib2RmY2D4KEmHcReyefrcg8ysicExibuQ5GtBoKBg/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，放到jwt解析网站，更改其sub字段为administrator，并且把alg字段设置为none。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFGVIaun0niaMeBt9XI7Z3zU8r9hHdib3GcGBMD4zkZDHzeed6EozN1NDSrZ4pBUgl9WlSqiboNYrhMpVYRP9ezuC9aCAkj2oXOTQc/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGkuH4M0BnIFf5ia8ex9gaLAo5jV9oYhmbs9ak5VB5DlL5ibAdswgK2POC8v2tlZJKC64Kz1XyaDnIgGStmtVLuvNsdJJQUGJOpo/640?wx_fmt=jpeg&from=appmsg)

### 密钥可爆破

###### 原理：常见的jwt加密算法有两种HS256（对称加密），RS256（非对称加密）。那么对称加密也就是只存在一个密钥对字符串加解密。如果开发者使用了存在弱口令的密钥，就存在安全问题了。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFHPVDM8Zcribicr1J4ngJ9Vr1nZ5Kj7ONshovKKa63Iy9oySibAVTqI1cNRp3JQzFnUMUia0uSiakAz1aMC2BDQyUEUyoibcGu5nElqM/640?wx_fmt=jpeg&from=appmsg)

###### 这里使用实际案例分享，找到一处登录框注册登录。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFENm89sibRs56j0icTRAyVjsj4iauykBy7QhhbwRib6Iia0acrvp1RibzsBHCyKS7goiag0tD8twWQmglvG0hYxyEsDvOcfkqBAqapa9U/640?wx_fmt=jpeg&from=appmsg)
![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFFAh5zgaI0yR2jXMYk142jkE9LIyhy5cicRUnjXoAQAR70R9pd5bfibEUV7AEgZTMCCXDRAFELyibjibvvmVd5FI63yI8H9dnmIlJY/640?wx_fmt=jpeg&from=appmsg)

###### 查看cookie为jwt并且加密算法为hs256，尝试使用hashcat爆破密钥

> 命令：hashcat -m 16500 -a 0 jwt.txt jwt.secrets.list --force
> 字典：https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGl2bPFicibmicJDfg1BY7ZBAibic2mt3NwL6vqmBbIHhu05E780S9CocpaqP6ibAxlw0BAfkRM1RibN6ziaG3aaE4zjibhZYdSKW0nQJyI/640?wx_fmt=jpeg&from=appmsg)

###### 修改参数为admin，成功登录后台

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFEXNVyM3E8uQKZ38AKK47suGTJBd4hUT03tbia8PxXmMuSJ144iaey9w2HbxBaVeMv6GMft3L32YTN57kUfkmvg7cyDB7vSH5Rmg/640?wx_fmt=jpeg&from=appmsg)

### jwk注入

###### 原理：当jwt使用非对称算法时公钥会可能写在jwt内部，如果开发者没有严格遵守公钥白名单，可能导致任意密钥进行验证，就存在安全问题了。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFHM31Ljm7ico5nFDy2xvjgicaTwDbh2RvwLlywmc0DRoqEkS9aReRHFWJENUklDJKBOud8Zvy4qfJBODrcib6mPhgFIC6QN6g4v8Q/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，复制jwt使用jwt\_tools实现jwk注入攻击。(具体一下参数请看工具使用)

> 命令：python jwt\_tool.py jwt -I -pc sub -pv administrator -hc kid -hv jwt\_tool -X i
> 下载地址：https://github.com/ticarpi/jwt\_tool

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFEJgDSHTGqN3Q8VXWcM0CGH6PnQrBo5pd5O9KdaNA2aRnfElaNaeGD7HTD11tiaJUVgaGuk5PZoEgJCwCDkV9UESJxG7QVa6Ptc/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFFPbK6KRricKoAyALibkmcel52yjMYeqoUxjwBeKHaBkqkdj79icIb9LYoGusRVJB03kcTrWlTj97ImrzBnH727znjk1TXV2z3Pho/640?wx_fmt=jpeg&from=appmsg)

### jku注入

###### 原理：上面说过如果使用非对称加密算法公钥可能写在jwt里，同时也可能写在一个web路径。还是如果开发者没有严格遵守公钥白名单，可能导致任意密钥进行验证。相对与jwk注入是本地加载，而jku是远程加载。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFEhdDWQAgZMiawHNfsAma3pudQWibBBB86rQfuNghG9Kb43ic7xUia3Ef9Hl5hnjntfvwYlTWbjnk2c5bu2HmMFw0hCCUk6abb4uWs/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，复制jwt使用jwt\_tools实现jku注入攻击。靶场为我们提供了公钥的加载路径url。

> 命令：python jwt\_tool.py jwt -I -pc sub -pv administrator -hc kid -hv jwt\_tool -X s -ju url

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHKPZVq0jpB9kBvYLnUWUvA37bSFkBkET9kzTqh7F4Bnue7bBPwCGgC7jolln1pqibiabqX4xY2Y4odibXibuojTZvxEGI1vJWryo0/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们把生成的公钥写到公钥加载的url中

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGyT6I2ALc546iaBsMCLEofX6QmWa6695LC9SWp0ZaxVeWl3m8aXrvSdPnCx3j9roaaCaGJdItyItTrgqibteibMibA3J7uTtpHKaI/640?wx_fmt=jpeg&from=appmsg)
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGGrPUMOQzXiaAPLYSPgcCor886ecYnnboflxJ4rJlXao9KzzyhdGHjvNjW5PzNIIOBdiaIAXTOVyPQibdupDMZ3KlRSB9jPk4Www/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFFTy0YCoPXWqWl7svotMoHQ4SLXXk62P1eGxtTpYog5zbXAg4tYB6amd6j4oKEO1lDAcNzSC08HKR0duNP7XECsibD25ndv1Cb0/640?wx_fmt=jpeg&from=appmsg)

### 算法混淆

###### 原理：服务器预期用 RS256（非对称）验证，但攻击者将 alg 改为 HS256（对称），并利用服务器公开的 RSA 公钥作为 HS256 的 “共享密钥” 生成签名。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFGogsiarKKgRiactcRFLSOzW5zCLj68Wmk8KgtobdDicqvlOMKzticpB7DkmqUlEYzicAd20Mz2ciadWbxDF1pxJRKVASUlyNrjOavL4/640?wx_fmt=jpeg&from=appmsg)

###### bp靶场指明了公钥的路径。把公钥转换成pem格式。保存到电脑命名为key.pem（网站：https://www.authgear.com/tools/jwk-generator）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHfibSrLictCkLG56VicymlSiaicKoTcRnPVFDOgSjXhktR4FPyAQ3IczBIdQfjgZmNXTg6j1qLK6pzPAtiaHLM4crWEdKmmHWQvBObM/640?wx_fmt=jpeg&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFF7sp3trb67icFrH86X02lJkRpyHO2DOKOX3tb4hQQL9HEkxfFUic5PYdB544Kiakkh2XXpZEAvXamZoEMDDVHsBqCngxOve7CpY8/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成j...