---
title: JWT：渗透测试姿势全解析（含实战）
url: https://mp.weixin.qq.com/s/el__Ih_587ALW3xDQaf_jQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:07.936315
---

# JWT：渗透测试姿势全解析（含实战）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZljYTjOjh4td5HzvjkI5QETWnVgynMvNA4TZZK9jY33XQzkNeSLnMBPg/0?wx_fmt=jpeg)

# JWT：渗透测试姿势全解析（含实战）

赤弋安全团队

![]()

在小说阅读器中沉浸阅读

## 导语

###### 师傅们在渗透测试做越权时，尤其是小程序的资产会经常看到cookie的字段是以eyj开头的字符串，不乏会有些头痛，没办法修改一些敏感字段从而达到越权。这就是jwt（JSON Web Token）。下面我会对jwt的渗透姿势有一个详细的讲解。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlESfmfkO1epcz7w58qgM3MRialWJbWpxz5dPjuFwX15rOXGTwKibiadYRg/640?wx_fmt=jpeg&from=appmsg)

## 原理

###### 简单来说jwt就是一个身份认证的字符串，有三部分组成：第一部分是头部（Header），第二部分是载荷（Payload），第三部分是签名（Signature）。每个部分有.分割并且通过base64编码。对于我们来说其实只需要关注前两个部分。下面我会分别解释这两个部分。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlybjHpGvkiaKs062lTrWMvKm1cZ4FbLurkNGB8eloibeCnw34xwkbed5w/640?wx_fmt=jpeg&from=appmsg)

### Header

###### Header部分的功能简单来说就是定义了这个jwt的加密算法和识别签名的密钥。这两个功能分别对应Header部分的alg，kid这两个参数。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZl3Gd7UIN7juvUabrlnlxVib2KkEZ3wTI6IqnGrbS66Cia2vDySkHyrIOw/640?wx_fmt=jpeg&from=appmsg)

### Payload

###### Payload部分其实也就是这个字符串的核心包含身份认证的字段。下图的用户字段是sub实战情况下uid、userid这些也都可能。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZl9QF95Dzibfr8tiaBQib9cwf8x7w2d583I3trrSq8icdxAfulqTwkTXvQWg/640?wx_fmt=jpeg&from=appmsg)

###### 那就想问了那我在这里直接改不就好了，这个话说的对，也不对。这个要说一下jwt的工作原理：我们上面的Header和Payload部分在进行base64编码还会通过算法密钥进行加密，如果更改这两部分的一些参数会导致整个字符串更改。从而无法进行过越权。这个也是是否产生漏洞的核心

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlrI8dTG7n05pyhAH3HeN3V6vSNMI06DIMUk5j2MaEENBPdicU0aYYIlQ/640?wx_fmt=jpeg&from=appmsg)

## 姿势

### 有缺陷的jwt校验

###### 原理：JWT库有两个处理令牌的方法，在Node.js中，有verify()和decode()方法，分别进行验证令牌和解码令牌的操作。那么开发者在对令牌校验是使用的是decode()，说明就没有对签名进行检测。就存在安全问题。这也是上面说对也不对的原因。

> verify() 方法：用于验证令牌的签名是否有效，同时解码令牌内容。如果签名无效，该方法会抛出错误。
> decode() 方法：仅用于解码令牌内容，不解密或验证签名。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZl3BmHzwnn3YLy2X0MV0aVRN7x5KlibspNtN8XIdDYxMmEmV6v74qhNMQ/640?wx_fmt=jpeg&from=appmsg)

###### 案例主要来自bp靶场还有一个实际案例。下面可是我们第一个实验。登录后生成jwt。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlO8wFIUzDfSadCeATgXSiaJGB46MmPxkQhQA2uarLibDUYpkz5Jq5icQgw/640?wx_fmt=jpeg&from=appmsg)

###### 放到jwt解析网站，更改其sub字段为administrator。（网站：https://www.jsongj.com/ede/jwt）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlkcA7og7RlzCu3MmKWVDV7gko7051NIatD9f41738CKsL0yciaoxvk3g/640?wx_fmt=jpeg&from=appmsg)

###### 我们可以看到这里的签名是随机的，按照jwt的工作原理这个是不行的。但是这个是存在漏洞的。然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlmU3Bljz6YeOIDSHEFHpGSicuXuSJr9daPa84IGFY7wvhibkT2MjlrWDw/640?wx_fmt=jpeg&from=appmsg)

### 空密码算法

###### 原理：开发者没有对jwt的算法类型严格校验，就存在安全问题。我们上面说过alg参数是决定jwt算法的类型，那么是空算法会导致密钥也不会生效。从而达到越权。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlbuvEkfUGD8FvYq0DwKHzflkV264Qftsiacc8VKHqaRyXkrSZjacLtkg/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，放到jwt解析网站，更改其sub字段为administrator，并且把alg字段设置为none。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlNxW5kHMicq353Q58famsACs50SFT6eHSR3mYMthp1wnK1QVbZWYxYSQ/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlmU3Bljz6YeOIDSHEFHpGSicuXuSJr9daPa84IGFY7wvhibkT2MjlrWDw/640?wx_fmt=jpeg&from=appmsg)

### 密钥可爆破

###### 原理：常见的jwt加密算法有两种HS256（对称加密），RS256（非对称加密）。那么对称加密也就是只存在一个密钥对字符串加解密。如果开发者使用了存在弱口令的密钥，就存在安全问题了。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlZvVic2k5k0WuHsKYM9oK76ic0Kp5n0GBAJhn8fP4e91icuCakAlfiafFgA/640?wx_fmt=jpeg&from=appmsg)

###### 这里使用实际案例分享，找到一处登录框注册登录。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlTwvKe0dSic3CBlgfQdwGic65enONodu8syVQs21s74IpR0htwEnJo07w/640?wx_fmt=jpeg&from=appmsg)
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlTj7uDXdRxAfU0fnVX41UXdyn7vl7T5uqd6KPu7iaL12TOnd7vk0YiaUA/640?wx_fmt=jpeg&from=appmsg)

###### 查看cookie为jwt并且加密算法为hs256，尝试使用hashcat爆破密钥

> 命令：hashcat -m 16500 -a 0 jwt.txt jwt.secrets.list --force
> 字典：https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlv3a43jesYAEzYTtDDahOvbcYyZab7xylKibNibWiamNGvKeHeuQM42kzQ/640?wx_fmt=jpeg&from=appmsg)

###### 修改参数为admin，成功登录后台

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlXYCZc8WJficzIN7x5IXxlQBuemfZI5lRm2UnibMVreK8F2K5l5UEuRmA/640?wx_fmt=jpeg&from=appmsg)

### jwk注入

###### 原理：当jwt使用非对称算法时公钥会可能写在jwt内部，如果开发者没有严格遵守公钥白名单，可能导致任意密钥进行验证，就存在安全问题了。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlGa2XgIrlhWXl3Zy4BYz3ADeL03GMwrgrIurjPKicwyftwngs0nHPTYA/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，复制jwt使用jwt\_tools实现jwk注入攻击。(具体一下参数请看工具使用)

> 命令：python jwt\_tool.py jwt -I -pc sub -pv administrator -hc kid -hv jwt\_tool -X i
> 下载地址：https://github.com/ticarpi/jwt\_tool

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlUlEXianmXD74hFF9tBSlzqsVppuWywybEL0r48DiadXNzWeuyrByD00w/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlmU3Bljz6YeOIDSHEFHpGSicuXuSJr9daPa84IGFY7wvhibkT2MjlrWDw/640?wx_fmt=jpeg&from=appmsg)

### jku注入

###### 原理：上面说过如果使用非对称加密算法公钥可能写在jwt里，同时也可能写在一个web路径。还是如果开发者没有严格遵守公钥白名单，可能导致任意密钥进行验证。相对与jwk注入是本地加载，而jku是远程加载。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlqWr7VGkicWsmEiaS9GJE7kIN2JuQngSWsYZNtKnOQicmoEJibeJ2gKhMoQ/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，复制jwt使用jwt\_tools实现jku注入攻击。靶场为我们提供了公钥的加载路径url。

> 命令：python jwt\_tool.py jwt -I -pc sub -pv administrator -hc kid -hv jwt\_tool -X s -ju url

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlpvib19jWZia1nmbtnibcEWHiaNGRyOR3VK5mmpeYmM8Czz8Z88sEbHT51w/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们把生成的公钥写到公钥加载的url中

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZloO6v6icf84Il626XmqJrvnRuibufVCAZ72s8rIY0TbdEDz9icSyJzwcHQ/640?wx_fmt=jpeg&from=appmsg)
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlpJ2nZEpZogfBOwdE6h99micaQThA7nYtP4TiaehkWcztdVXQVF45KcEQ/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlmU3Bljz6YeOIDSHEFHpGSicuXuSJr9daPa84IGFY7wvhibkT2MjlrWDw/640?wx_fmt=jpeg&from=appmsg)

### 算法混淆

###### 原理：服务器预期用 RS256（非对称）验证，但攻击者将 alg 改为 HS256（对称），并利用服务器公开的 RSA 公钥作为 HS256 的 “共享密钥” 生成签名。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlG6tnpnBolJiadUSQuBWnKNUlc7JRYGqxAB4Uvia3XGxgjkNkV5JHyg3A/640?wx_fmt=jpeg&from=appmsg)

###### bp靶场指明了公钥的路径。把公钥转换成pem格式。保存到电脑命名为key.pem（网站：https://www.authgear.com/tools/jwk-generator）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlnd8VWmkvcWFucKptpvLwWKMSGwIgScz9NUJxRuQXA37aH8RkYzSicRQ/640?wx_fmt=jpeg&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlDbzssJ2ib42rua1HribWYRMeOkdiapEicKficicPqic3nibtXdElOAEO6k2qMw/640?wx_fmt=jpeg&from=appmsg)

###### 依旧是bp靶场登录生成jwt，复制jwt使用jwt\_tools实现算法混淆攻击。

> 命令：python jwt\_tool.py jwt -X k -pk key.pem -I -pc sub -pv administrator
> ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZl8Uyh4Ir45pAicKeKMd3fX2CyonzAB9BBq5bons9pKDQs0jwl4XOkPTA/640?wx_fmt=jpeg&from=appmsg)

###### 然后我们拿着这个jwt访问管理员路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tb6OwBlojEibuvOha6RYbm44DpucdNoZlmU3Bljz6YeOIDSHEFHpGSicuXuSJr9daPa84IGFY7wvhibkT2MjlrWDw/640?wx_fmt=jpeg&from=appmsg)

###### 针对jwt以上的姿势应该适用于大部分场景，还有一些kid参数sql注入，目录遍历漏洞。因为没有实际案例，就没有说。等实战测试记得测一下就好了

## 结语

###### 总结一下吧，先看加密算法，如果是对称加密，就尝试爆破密钥，或设置none算法，非对称算法尝试是否存在jkw，jku。或sql注入或目录遍历。

> git...