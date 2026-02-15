---
title: 漏洞挖掘之利用js挖掘漏洞
url: https://mp.weixin.qq.com/s/Tqc7yQno7_CDD8pIwLwDGw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:17:27.640955
---

# 漏洞挖掘之利用js挖掘漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRlvib2CeJEhWAe2JHv8D52WggkNgdU7UfoELukK8l5eTicXBvngJt5CAFzicYUicmTn0ZKbVr1mOibf79PxBrkVXW2l8l4oZz7yxib4/0?wx_fmt=jpeg)

# 漏洞挖掘之利用js挖掘漏洞

中铁13层打工人
中铁13层打工人

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:中铁13层打工人原文连接:https://forum.butian.net/index.php/share/3915
```

# 前言：

在漏洞挖掘中，通过对js的挖掘可发现诸多安全问题，此文章主要记录学习如何利用JS测试以及加密参数逆向相关的漏洞挖掘。

# 漏洞挖掘

## 一、js中的敏感信息泄露

1、默认用户名密码

2、硬编码密码、其他秘钥泄露

## 二、js中的指纹信息

框架信息、开发商信息、版本信息等

## 三、js中的接口泄露

js中内含大量接口，可通过敏感字匹配爬取接口的方式来集中测试；也可结合目标测试功能点，通过截取父目录后到源码中搜索从而找到隐藏的接口，进而得到前端未显示的业务模块代码。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCoC4MpaTHKtVFTPSZGtl2A8GNN98d80enxcCJHU50BpdIuNic79NA0OksFTI5Kq3yL4mHmngJhbetgK6iaFdgGz2wR860hWDMU/640?wx_fmt=png&from=appmsg)

## 四、js异步加载

当访问某系统发现有多个功能模块，短时间内无法快速加载各类功能或者有不显示的业务，此时可借助异步加载执行JS文件，从而更快看到页面内容和源码且利于实现代码分割。

1、什么是异步加载js

同步加载方法通常使用 `<script>` 标签直接在 HTML 文档中嵌入或链接外部 JavaScript 文件，这种方式下，浏览器会等待 JavaScript 文件加载并执行完成后，才会继续解析 HTML 文档的其余部分。

异步加载 JavaScript 可使用 `async` 或 `defer` 属性在 `<script>` 标签中实现。异步加载允许浏览器继续解析 HTML，不必等待 JavaScript 文件的加载和执行。

2、实战案例

访问目标系统，发现其主页的登录页面没有注册点且测试过其他的方法发现无法绕过登录。这种情况下考虑从前端源码入手看能否找到其他功能点。开发者模式下利用network工具，可查看相关请求接口引入了哪些js文件，着重关注类型为“XHR”或“Script”的请求，这些中通常包含异步加载的js文件，为了更直观看到完整的解析源码下一步可将当前网站下的JS全部异步加载到首页。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSHoZbsicxcbegViaiabhSWhwZHeRFxmVykz7TTaSu2TgDibmrB7u0b3DSUW5hP8zQ4tYzVGl64yueCpC2MW4xuTpPOQ76EJbgoSUM/640?wx_fmt=png&from=appmsg)

异步调试js代码如下：

```
var arr=["https://xxx.xxx.com/xxxxxxx/xxxx/0.1.0/js/xxxxxxx.js",  //这里引入的是完整的js所在路径"https://xxx.xxx.com/xxxxxxx/xxxx/0.1.0/js/xxxxxxx.js"]for(var i=0;i<arr.length;i++){var script = document.createElement('script');script.src = arr[i];document.getElementsByTagName('head')[0].appendChild(script);}
```

在控制台中调试代码，运行后结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQibWP1Yc8n2coPulicNZ7YkAaktYtBgTvEuWmUh59tZOvsplDcUiazvQekWjw2HpZfNfKeo335PiaewMk7k7ccOjJkvwAaHg9bfRY/640?wx_fmt=png&from=appmsg)

运行后可看到完整的js代码，后对代码进行查看发现了一个包含file接口，猜测应为文件相关的接口。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRCA9bHMajm8Mve3hLz2Cwjd2w8hOlPiamYM7oxbqYzSr8SKMkZX0BWKnkvK4RnTXptK0jIiaibS9qOcquD5mP2AwLBTFhgk0ibaibI/640?wx_fmt=png&from=appmsg)

跟进源码查看哪里调用了这个接口方法进而构造发包需要的参数。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT2Qde0gsaVyhcgQQnqmuyO2n2Iqh5Dj1j56OJhO9eswyNlo3fh0WZTIpMySJfrsBicp7iaBnyUxLnM0pAav3B8dTNgG5nl2gmIQ/640?wx_fmt=png&from=appmsg)

测试发包的返回中包含云服务资源链接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTR1w4TA6no7ickMc2JShUjOkGVUW0sTm5hicqGzg8TbYBqC2qy7ic8bQOgrvovTfcImyflgV2PRlAbc8XDLnjSE99A80o4qAHtlI/640?wx_fmt=png&from=appmsg)

访问返回的链接发现其为存储桶资源信息，至此测试完毕。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSGGds041FC1ticjqWz0pRXWSao2wicu6U8XG28xZF9v7Hh4yuXnxCT9UfibUASFAvic8Yz9KPolXM2rhuuIayLYAWjWJP8ZxZgPX4/640?wx_fmt=png&from=appmsg)

## 五、js逆向破解加密

思路：

定位漏洞源码所在js--大致浏览代码逻辑--下断点调试或者根据关键字搜索--找到加密算法--将加密算法py脚本化--破解解密--测试漏洞

案例分析：某网站越权查看信息逆向分析

1、抓包分析

测试某系统，访问该系统某功能点查看信息根据抓包情况进行分析，发现传参部分都做了加密操作，同时得到查询接口为/rxxx/xxxxxte，其中nonce 是一个随机字符串，用于防止重放攻击；skey用于加密或身份验证的密钥；sign 是请求的签名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSQ825tCzVq5cOJ30cGAibPTocsuvrRsGGfF6s4ticzLPncSB7wnunSg7SBWe1nBibWVYfxfuYdzwXf6zibnZU5Nw3eOibyA8AJUPuI/640?wx_fmt=png&from=appmsg)

2、逆向分析

对抓到的数据接口/rxxxx/xxxxxxte进行分析，一般都是先进行一波搜索，看能否定位到加密位置，如果定位不到就在接口调用位置下断点再访问接口进行调试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTHnbMYMVBhHeYL5f2GVppGFpiblqMicY35Vc8tUDsn3p0LlEZpRvoXbVmVWOCuwEuqfhFgN5l4YR8HQOhYwu6q5oFGYgAW1Ao4Q/640?wx_fmt=png&from=appmsg)

经过搜索找到其中一个JS中有很多条记录，进入JS中进行整体分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRXHEcwEIdpM9yrGdDSBicD1NBWQwEDiaGbH3zNzCRbttueRM2icoddL4jMc9n8KD5ypibkywY0Uia9w4YGj4bEmbCeBNFjsnH1oubQ/640?wx_fmt=png&from=appmsg)

对该JS进行整体检索时，发现该代码块存在请求体内所有的加密参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSl3Cj8dXzk3eSkuKr3cPudAZXRzNM07W4MV4ib9uAALW0lBbo4ycicZ91LW5mXdaMgl7vRRticzP03DeCffXdl02VkGBbrvU7lGQ/640?wx_fmt=png&from=appmsg)

即对该部分进行断点分析，发现该请求在此处断掉，且传入的e参数是rsa公钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ3UQpTg5fmiaPR60jic4fXYP3uQPA4iaiarzluy7tWth3WdWwbbEUiat0cGzQmZwXpfYdwEqYpjVXggLNQoicNia9gucEZaXvXc1TNFc/640?wx_fmt=png&from=appmsg)

因此该部分即为加密请求体中的所有加密代码部分。

对该部分代码进行代码分析，这段代码即为加密代码块，继续跟进分析其主要原理：

主要加密代码块getKeyParams 方法：

该方法生成一个包含加密参数的对象，主要用于构造请求数据。

```
getKeyParams: function(t, e) {    var n = {        timestamp: "",        nonce: "",        skey: "",        body: "",        sign: "",        aesSecretKey: ""    };    ut = e;    n.timestamp = (new Date).getTime();    n.nonce = this.getNonce(32);    n.skey = this.getAesSecretKey();    n.aesSecretKey = rt;    n.body = this.encryptByAES(r()(t), rt, "12xxxxxxxxxxxef").encryptContent;    var i = this.encryptByMD5(n.timestamp + n.nonce + n.skey + n.body);    return n.sign = this.encryptByRSA(i, ut), n;}
```

该函数用于生成时间戳、随机数（nonce）、AES 密钥、加密内容（body）和签名（sign）先初始化一个对象 n，包含 timestamp、nonce、skey、body、sign 和 aesSecretKey，然后获取当前时间戳和nonce，随后生成 AES 密钥并加密输入的数据 ，使用固定的初始化向量（IV）"1xxxxxxxxxxf"，然后计算签名，使用 MD5 哈希连接 timestamp、nonce、skey 和 body 的值，最后用 RSA 加密生成签名。

1、getNonce方法：生成随机字符串nonce（根据主函数来看是nonce长度是32）

函数通过循环从指定字符集（默认为字母和数字）中随机选择字符，构建最终字符串。

```
getNonce: function(t, e, n) {    var i, a = "";    void 0 === t && (t = 10), "string" == typeof e && (n = e), i = e && "number" == typeof e ? Math.round(Math.random() * (e - t)) + t : t, n = n || "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";    for (var o = 0; o < i; o++) {    var l = Math.round(Math.random() * (n.length - 1));    a += n.substring(l, l + 1)    }    return a}
```

2、encryptByMD5方法：对输入的字符串进行MD5加密

该函数通过 MD5 算法对输入字符串进行MD5加密，并输出大写的哈希值，用于生成唯一标识符。

```
encryptByMD5: function(t) {                    return console.log("md5", t), ot.a.MD5(t)                        .toString()                        .toUpperCase()                }
```

3、encryptFunction 方法：方法用于封装 RSA 加密

函数使用 RSA 对 ct 进行加密，其中ut 是用于加密的公钥。

```
encryptFunction: function() {  return this.encryptByRSA(ct, ut);}
```

4、getAesSecretKey 方法：该方法生成一个 AES 密钥并加密

函数生成一个 16 位的随机 AES 密钥，并使用 RSA 对该密钥进行加密。

```
getAesSecretKey: function() {  var t = ut;  return rt = this.getNonce(16), console.log("16", rt), ct = this.encryptByRSA(rt, t);}
```

5.encryptByAES 方法：该方法用于 AES 加密

函数使用 AES 加密输入的内容，密钥为 e，初始化向量（IV）为 n，返回加密后的内容和加密密钥。

```
encryptByAES: function(t, e, n) {    var i = ot.a.enc.Utf8.parse(e),        a = ot.a.enc.Utf8.parse(n);    return {        encryptContent: ot.a.AES.encrypt(t, i, {            iv: a,            mode: ot.a.mode.CBC,            padding: ot.a.pad.Pkcs7        }).toString(),        encryptSecretKey: e    };}
```

至此分析完加密算法，下来使用python将其还原：

```
import base64import hashlibimport randomimport timefrom Crypto.Cipher import AES, PKCS1_v1_5from Crypto.PublicKey import RSAfrom Crypto.Util.Padding import pad, unpadrsa_public_key = '''-----BEGIN PUBLIC KEY-----MxxxxxxxxxMBUD-----END PUBLIC KEY-----'''.strip()class EncryptHandler:    def __init__(self, rsa_public_key):        self.aes_key = self.get_nonce(16)  # 生成 AES 密钥        self.iv = '12xxxxxxxxxef'.encode('utf-8')  # 固定的 IV，实际中可根据需求随机化        self.rsa_public_key = rsa_public_key    @staticmethod    def get_nonce(length):        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"        return ''.join(random.choice(characters) for _ in range(length))    def aes_encrypt(self, data):        cipher = AES.new(self.aes_key.encode('utf-8'), AES.MODE_CBC, self.iv)        encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))        return base64.b64encode(encrypted).decode('utf-8')    def md5_sign(self, data):        return hashlib.md5(data.encode('utf-8')).hexdigest().upper()    def rsa_encrypt(self, data):        key = RSA.import_key(self.rsa_public_key)        cipher = PKCS1_v1_5.new(key)        encrypted_data = cipher.encrypt(data.encode('utf-8'))        return base64.b64encode(encrypted_data).decode('utf-8')    def prepare_request(self, body):        ti...