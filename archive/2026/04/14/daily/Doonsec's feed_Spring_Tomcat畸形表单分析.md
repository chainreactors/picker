---
title: Spring/Tomcat畸形表单分析
url: https://mp.weixin.qq.com/s/omlK0ugRLk6tHJEPWHxXGA
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:39.194829
---

# Spring/Tomcat畸形表单分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N8PSUCGBuBP0NfG7hO5NShbcDY5K6PlcIXjnB2NegpLbBj5yAsCJgKLjpaasylvA2rIU9wwibQMD0W64WLSjgXNxlvLMAtxj4aWs5OTXnmhY/0?wx_fmt=jpeg)

# Spring/Tomcat畸形表单分析

原创

小白安全
小白安全

小白安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、前言

好久没写文章了，在AI时代下，安全已经有比较大的变化了，感觉输出远不如AI，只能向AI大人学习了。

在很久之前一次项目中，本来分析了一个 fastjson 反序列化漏洞，能成功 RCE，当时是周末，就没继续看了，等周一想再看看的时候，发现被 waf 拦截了，于是想分析分析Spring/Tomcat畸形表单

# 二、测试环境

```
spring-boot 2.6.13内置tomcat 9.0.68
```

# 三、分析过程

在org.springframework.web.servlet.DispatcherServlet#doDispatch处下断点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBPyuSmQibVYKwY2siaIEqtQuZVXNnWGEXPKKyA9onl5Gv1l1aDj8BddSktGQLExvNuzoyQZDf9OibcwOt4Fcwk9gVRhpu5F50bglY/640?wx_fmt=png&from=appmsg)

看代码，应该会进入checkMultipart

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBNdnRianhXZmjXbnT1sBPlv9gPqEekwwY9EZfoC9t1UiaGFmvHe38vNTgUe9eMgTUw2fmiaCFt9X3dicxXS2k8aDnGqmA8G947nnqY/640?wx_fmt=png&from=appmsg)

这里会进入org.springframework.web.multipart.support.StandardServletMultipartResolver#isMultipart，默认情况下this.strictServletCompliance 是 false，这里会判断请求头的Content-Type 是否multipart/开始，忽略大小写

中间省略一部分

继续往下，会走到FileItemIteratorImpl#init，会初始化相关的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBOotNsiao0wNo5ZhGDuia61MCSc9dsv5zp0dylibskFM06qzMSm5ovYxrjVFd88rQYXpkRKftnL39LXWudibRibicOkoibC0dlTjKxribc/640?wx_fmt=png&from=appmsg)

# 1、Content-Type

## 1.1 FileUpladBase#getBoundary

org.apache.tomcat.util.http.fileupload.FileUploadBase#getFieldName(java.lang.String)

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBNOaSftIfW5vYmSLtqWTibIlAiamyagNy4tD965XvoLNAUncKy0Tvsqt7TkuXAQndWK4X0ZvKVMJ4SUpDa9ib9TJ2biaBgkEx9E6PM/640?wx_fmt=png&from=appmsg)

继续跟进，会走到FileUploadBase#getBoundary

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBMSpAZIoubYa9SsuRLRegm46YqW8jTnuNkm1mbkxtZBUia4ER4zPdJTXKicBgIc0uF11NhKcPb668ibciaMBf8uhx9fMPfwoUFohGo/640?wx_fmt=png&from=appmsg)

然后使用ParameterParser#parse(java.lang.String, char[])来处理 contentType，使用;或,做为分隔符

构造 Content-Type

```
Content-Type:multipart/form-data,boundary=----WebKitFormBoundaryD9Okowji7fMSUFeT
```

还可以这样

```
Content-Type:multipart/form-data,,,,,,,,,,,,,boundary=----WebKitFormBoundaryD9Okowji7fMSUFeT
```

这样（中间部分被当成 paramName，不影响）

```
Content-Type:multipart/form-data,;,boundary=----WebKitFormBoundaryD9Okowji7fMSUFeTContent-Type:multipart/form-data;,;boundary=----WebKitFormBoundaryD9Okowji7fMSUFeT
```

继续往下分析

1.2 ParameterParser#parse

对Content-Type 以及Content-Disposition 进行解析

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBMclPDqic73sjFJ18ak9G6jC0HVU1zicCHSjzABW8AeGjPeKFFjBbhxuqeqs1LtibWshXTbTepCUOmxgJ0iacibXPSqwpnxTadp62wc/640?wx_fmt=png&from=appmsg)

首先会使用 parseToken 使用=、;来获取 paramValue

使用；或，进行分割

如果以;进行分割，会走到 329 行的判断，如果 paramName 不为 null 或空，则会使用RFC2231Utility.stripDelimiter处理参数名称

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBP8vhaT7bwyzpJPqQX4yV2BLibEw7uhl5DnagZ45ag8c9uynlqTqz97ZX85tvzYhmbEQYd0QxOMyqRj6H0bRCZhHeTuSyaoaGMc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBMiaZJhZBO2qOdkyqUubVib5ucesHb0icPicYicoUam7LLlZD8VQHIaoHAJ7nWcicST78f2HNJk57Y0uaWutmmXNIG5eyfZvj6Lqzdg8/640?wx_fmt=png&from=appmsg)

如果paramName 以\*为结尾，会删除，并返回删除\*后的paramName；最后将paramName 转换为小写，put 到 params 中

构造 Content-Type

1、 给参数名称加\*

```
Content-Type:multipart/form-data*;boundary="----WebKitFormBoundaryD9Okowji7fMSUFeT"
```

2、大小写转换

```
Content-Type:MultIpart/Form-Data*;boundary="----WebKitFormBoundaryD9Okowji7fMSUFeT"
```

使用=进行分割

如果以=进行分割，那么会先获取=左边的为 paramName,然后再继续以;进行分割，获取到的内容就是 paramValue,如果不为 null，会进行处理paramValue = RFC2231Utility.hasEncodedValue(paramName) ? RFC2231Utility.decodeText(paramValue) : MimeUtility.decodeText(paramValue);

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBOiaj19jd75sGHpk3nUBzrxru6aIibBm4DTOdtGUXcCJ1u2KuIt8PWQ6ZoXjjFOOhg1ssS32GcfIlOV2z5UXfU6kXqKvic6EaIU0E/640?wx_fmt=png&from=appmsg)

RFC2231Utility#decodeText

如果 paramName 带\*，进入

org.apache.tomcat.util.http.fileupload.util.mime.RFC2231Utility#decodeText

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBO1te3UElp1w5D1DeUBjGkH2CHibxhjZ1hnLavrdypyUNy7wVib8xoEpcVlVcaDHRhbhahwPyRvpZiaSODYSZkHa9AXEnFAmVGDicM/640?wx_fmt=png&from=appmsg)

这里就很有意思了，使用'对 paramValue 进行分割，将前面一部分，获取为字符集编码，然后匹配'后面是不是',如果是会将后面所有的内容使用 fromHex 进行处理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBPLptclUMYiagdREexLU4vuohF7pCApKmrNpmr0qeu1zDB93Xxx3SZHvTfzogllEjQia6eXso1IHMDiaCnZDWd1peEVLM5KuxoRng/640?wx_fmt=png&from=appmsg)

这里可操作性空间就很大了，如果匹配到%，会将后面的字节，进行 hex 解码处理，如果没有匹配到，则原样写入

基础版

```
Content-Type:multipart/form-data*;;;;;;;;;;;;;;;;;;;;;;boundary*="UTF-8''%2d%2d%2d%2d%57%65%62%4b%69%74%46%6f%72%6d%42%6f%75%6e%64%61%72%79%44%39%4f%6b%6f%77%6a%69%37%66%4d%53%55%46%65%54"
Content-Type:multipart/form-data*,,,,,,,,,,,,,,,,,,,,,,boundary*="UTF-8''%2d%2d%2d%2d%57%65%62%4b%69%74%46%6f%72%6d%42%6f%75%6e%64%61%72%79%44%39%4f%6b%6f%77%6a%69%37%66%4d%53%55%46%65%54"
```

进阶版（原样字符+hex 混淆）

```
Content-Type:multipart/form-data*;;;;;;;;;;;;;;;;;;;;;;boundary*="UTF-8''-%2d-%2d%57%65%62%4b%69%74%46%6f%72%6d%42%6f%75%6e%64%61%72%79%44%39%4f%6b%6f%77%6a%69%37%66%4d%53%55%46%65%54"
Content-Type:multipart/form-data*,,,,,,,,,,,,,,,,,,,,,,boundary*="UTF-8''-%2d-%2d%57%65%62%4b%69%74%46%6f%72%6d%42%6f%75%6e%64%61%72%79%44%39%4f%6b%6f%77%6a%69%37%66%4d%53%55%46%65%54"
```

还可以使用其它字符集

MimeUtility#decodeText

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBOPBPn1aqhlKicJY3T8FXNPUxUlCb5PSoVeibQ2hINYicObEkCCx5sWVYaOXk2YwRvnKPBK10BHuib07vgweXNoHNHJC8SjzYjIx4E/640?wx_fmt=png&from=appmsg)

首先判断 paramValues 是否包含`=?`,包含则进入后续流程

进入MimeUtility#decodeWord

看注释，使用Parse a string using the RFC 2047 rules for an "encoded-word" type. This encoding has the syntax: encoded-word = "=?" charset "?" encoding "?" encoded-text "?="

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBNmsGqWzqN4eYrrncwISmXbGqmhTSwxfF8Adt2UMNOIpXSfIssicP2icREe4OLzPk8NNmkbD8ccfqIKkl3Pgc9z5Nyp1DwXEd2j8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBNfcqicoH54ia2ss0kKhpib3k3f0yNGprj2DQKW3tA8EAPNhCWhicdDomdpXZibdKBTVNLaIIia6sDqeAY1Y4iaRr0QQH72EOJwRT7LAw/640?wx_fmt=png&from=appmsg)

基础版

```
Content-Type:multipart/form-data*;;;;;;;;;;;;boundary="=?UTF-8?B?LS0tLVdlYktpdEZvcm1Cb3VuZGFyeUQ5T2tvd2ppN2ZNU1VGZVQ=?=";;;;;
Content-Type:multipart/form-data*,,,,,,,,,,,,boundary="=?UTF-8?B?LS0tLVdlYktpdEZvcm1Cb3VuZGFyeUQ5T2tvd2ppN2ZNU1VGZVQ=?=";;;;;;
```

进阶版

这里使用`?=`来判断 paramValue 的结尾，那么就可以在`?=`后面加数据,比如

```
Content-Type:multipart/form-data*;;;;;;;;;;;;boundary="=?UTF-8?B?LS0tLVdlYktpdEZvcm1Cb3VuZGFyeUQ5T2tvd2ppN2ZNU1VGZVQ=?=123132123;a="
Content-Type:multipart/form-data*,,,,,,,,,,,,boundary="=?UTF-8?B?LS0tLVdlYktpdEZvcm1Cb3VuZGFyeUQ5T2tvd2ppN2ZNU1VGZVQ=?=123132123;a="
Content-Type:multipart/form-data*,,,,,,,,,,,,boundary==?UTF-8?B?LS0tLVdlYktpdEZvcm1Cb3VuZGFyeUQ5T2tvd2ppN2ZNU1VGZVQ=?=123132123;
```

通用部分

以上两种情况，在最开始获取 paramName 时都会使用parseToken 处理，分割得到的 paramName

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBM9paCibRrJfRtEeNdD6HiaLDKXdxrZJ9ahxhh96mP7K1RuN5t94JA3hrUq4Ckrebic2RvnibWribtY8icDYCOuyP3hMeOlt57nP4P6Q/640?wx_fmt=png&from=appmsg)

调用 getToken 进行处理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBNfaia1Svvbz7hRcdJpSWNglOEIv8wJhm7JayEa4IR87L78Eck91asibzQdf5uoKnYYZG4y2JtehzicJIUXq7dlKibgGKhKAvT4icWM/640?wx_fmt=png&from=appmsg)

使用 Character.isWhitespace 去除空格

构造 Content-Type

```
Content-Type:multipart/form-data*             ,,,,,,,,,,,,,,,,,,,,,,boundary*             ="UTF-8''-%2d-%2d%57%65%62%4b%69%74%46%6f%72%6d%42%6f%75%6e%64%61%72%79%44%39%4f%6b%6f%77%6a%69%37%66%4d%53%55%46%65%54"
```

Content-Disposition（这里其实还没分析完成）

FileItemIteratorImpl#findNextItem方法会进行相关处理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/N8PSUCGBuBN5jE8ck0ibZja4qkHzg8VBjAENkeFTPjkDrLNhJLKsldFSjq0aVtmNZXic4BWiaWjADesBFg8cg1jffxdBicFiasibSMt4R2tEB2HL8/640?wx_fmt=png&from=appmsg)

首先看看fileUploadBase.getFieldName(headers)，会经过一个重载方法

![](https://mmbiz.qpic.cn/mmbiz_png/N8PSUCGBuBMUqVZ0acRqib3J5gcVyDUXia0xFLNcOG5juV88UoOricL2FxZurtvTILicKlxAJOHzOpRQMUeG9p5zHgTUbicoaHalnEXiciaex4kQ5w/640?wx_fmt=png&from=appmsg)

后续还是会使用ParameterParser#pa...