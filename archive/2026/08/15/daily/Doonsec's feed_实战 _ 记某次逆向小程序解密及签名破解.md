---
title: 实战 | 记某次逆向小程序解密及签名破解
url: https://mp.weixin.qq.com/s/lkYJ6BlCEoBDnhlc806i6A
source: Doonsec's feed
date: 2026-08-15
fetch_date: 2026-08-16T02:55:10.159397
---

# 实战 | 记某次逆向小程序解密及签名破解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFEaOT8kMVXudFRiabMr2ibJShnGVgl85zoVk2Ej3wy8pPwTq86DRXSOGpjUDznFehouomACpXd63GjYn9NkzPWibpWeHia1pPbLujQ/0?wx_fmt=jpeg)

# 实战 | 记某次逆向小程序解密及签名破解

小艾
小艾

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 关注我回复加群即可进入项目群

# 0x01 前言

碰到了一个对外宣传是否安全的站点，但实际测试下来并不安全。不过在这次获取权限的过程中还是有点曲折，记录下来并分享给大家。
**整个测试过程均在授权的情况下完成，漏洞详细已经提交并通告相关知情。**

# 0x02 过程

### 1. 进入

https://xxx.edu.cn/a/login
使用弱口令进行登陆

### 2. 寻找上传点

进来后找到一处文件上传的地方进行测试

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFF5hEyFiad0SSRUOeADvy4icibicTQC4Xr7bQAeUoxrT1Izo5AeKDsPOZib7caZ65Lzp4Xxd9Xt3UmLHZuHVa7sKZTrT3RP2CbyeSibU/640?wx_fmt=png&from=appmsg)

前端对上传的文件类型做了初步校验，这里我们上传一个空文本后抓包

![image-20220413194850530.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGCoKc9kOnfrib0fwsE8gvwxaZfumLJN9qTw8AMtohEuysdENUg0Yveo6z9u7BmbxvCq3kdMo76HLib3iaOzD0fgFj5jQGxYAqXFo/640?wx_fmt=png&from=appmsg)

发现路径可以被操控，而且返回了绝对路径。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFsNvgkVfCybLu1nyJCRwicuTpUh3P87MMR5a3m22znLfQhdibEkcZwIASoVE09Uq1m6LDSaia7O3icQBSeiaV32DeHXtD7kJaYGWI0/640?wx_fmt=png&from=appmsg)

尝试访问后发现不能被解析只能下载。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFTf9WXhQSvXhxtUtV60kd3FgTgtibYSW6M6MxzZZPw1en4FClWNkRjlIcILHexgZWZicltM6HX6uTNoAlauD2aUwLDaH4mzKLHU/640?wx_fmt=png&from=appmsg)

再次寻找上传点，发现有头像上传的地方。这种上传点一般都能被解析。

![image-20220413195538939.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGPicC5azvZUxLzjaD2BJlRGohZOUPw4RlAD10h6HbvxazPNCJrjQZibJ35CmSCNDvaauC6oFlJWmjxKf4qEklNfU9BL0wxeAGro/640?wx_fmt=png&from=appmsg)

上传正常图片

返回了上传成功的提示，但没发现返回的地址。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGp9cc8f6L98XHhxwAwRibobjOwDJIIichndN4Uh6DkmP56hmDuty0he5hhXSiaHsO6wndGiandqPGnLhjAOJqYS8Bnyru0wEaqbXA/640?wx_fmt=png&from=appmsg)

而后在个人资料出发现了图片地址

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF0P46PynBs6ymbgXcEoicJcvyEYvUtGMZaicyGA0EfLggeTdJUiafcVw3DW7QXyK4kTa59icPppH5pMW5RWGaWPdUaAe8dXkoApuc/640?wx_fmt=png&from=appmsg)

我们再次尝试构造请求报文重发，这里直接将后缀改成 jsp 上传成功

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF4TiaObicaDWPOm47To3IuaEgmu67WaD9pLtS6ktftpydTlSkjCw5NQcThFnic6iaEQqGSywxRgjlEUBXpFxv9x5LpAksEuOFxiam8/640?wx_fmt=png&from=appmsg)

刷新个人信息，找到访问链接。发现仍然是只能下载。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHeoVwPKC3sVGmA3kCTc1kRiaWGaakbBGVJu0mxicaicl73ly2BAx5Z2B3XiaTUZf6mFo5hCZbf4guFOzrlnhictNf2OUFb9iaVjjVib0/640?wx_fmt=png&from=appmsg)

### 3.突破口

![image-20220413200236737.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEvEye9K5tJ6V8ECxthdTrfnCo7TLQic4Nmw2p3UkQCNXwxI1ZOu27f3aJXs0BBibZVKMswuMRlBTEFAf2NQURibjSocWwJZc1nfw/640?wx_fmt=png&from=appmsg)

我在 Cookie 中发现 jeeplus 的字眼，尝试搜索 getshell 方法

![image-20220413200321834.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEcsVflia7DBhrFMNwJPaqm7O990CFiaKdPUfWtU1Ee4j8wwod6U9uWPWQWP48nYcbEmMQ1B37tEzSTicNvE80qRbtTbI6viamUECU/640?wx_fmt=png&from=appmsg)

发现早已有前辈做过代码审计。

#### 1）SQL注入

```
/a/sys/register/registerUser?roleName=wangba&mobile=13300990099\*&randomCode=2131&loginName=test1&password=123123&confirmNewPassword=123123&ck1=on&randomCode=2131&loginName=test1&password=123123&confirmNewPassword=123123&ck1=on
```

更具已有的 poc 进行尝试 sqlmap 跑起来，`*`号的地方是注入点。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEjw370gZUxEibIRm9THWBTfib3JmZelc40vjcEtyNG2cgQG2kKz8Zdfb9uicMCwVoaMuL1P4Jm5ricCU8Pj6ZQVt1YOJo7K84xJNs/640?wx_fmt=png&from=appmsg)

通过 sqlmap 跑出来是 oracle 数据库。尝试一些查询和提权无果放弃。注意，oracle 注入的 sql shell 只能做查询语句。

![image-20220413202358543.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHiaXFoibbqFmyGzCa4xrMPZds0BnfUKAFXKZsFwDfH4rVVSDfJrcsic0pHc7e9XqZBfebMgIqAnUhv7k18IBZfuFFrxyibMkn3yZY/640?wx_fmt=png&from=appmsg)

#### 2）文件管理

直接访问 https://xxx.edu.cn/a/sys/file 就能越权进入到文件管理页面

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF0VtxZzmct5ufNK4QkCbVeAqPoJjCia6r9tX5JuwN9bLuj2UGCjAAIqoQBbyZAy8naFQicCByOCnLQrsYVLfib0LMuQRKic4bDaYQ/640?wx_fmt=png&from=appmsg)

这个目录下面的文件都只能下载，我们对这里的文件上传、删除、下载都做了测试。

##### a. 任意文件读取

下载接口可以返回文件内容，存在任意文件读取。

![image-20220413202831585.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGbDrXWfRw2NKCeQwXR2IKeDSE3d06InFbVCXSNMdcAUhmF6iaA5c7dN2CpNvB5as31pbZVllicOOibVXV52tibYhO0B9050ZQcc68/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHpM2D007HlSv1asAEB6ah9Yg6t4GNdDA7sf1ajqKYgjNwVSk3O4cPLIU98djYX5R4d2CZA4BMAEUKJMHgjwYezxSu9GjxGNB0/640?wx_fmt=png&from=appmsg)

##### b.任意文件删除

这里甚至可以直接删除文件夹

![image-20220413203037016.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHK8chSTOCqaNLGZCjcW1NZLzmebrYmt7Acc3Vg6qFmhPIFAJmsRxu1NOWPicIzTcuHDXuo4zjraRXD4FicXDGiamEiaHTic6BP7HYg/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHpu7vNHtUkONxmJzHEiaHOiciaiaGLfE4pic6Xgl0uregUsjHDmHAqP3cbVxfsj77XSkhEyu8mqLZ1icobER2xtgdbbj3JY1iagNAB1E/640?wx_fmt=png&from=appmsg)

##### c. 任意文件上传

![image-20220413203146352.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGEoSEjaFJricqVUAQfm1M7geD8Gria0icnibmFSpicrlgPDMIiaufxhvK42MeGxthImHCvz4YicCEsOnE6ZpngTe8StXE9eJHBU515pY/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFseeFQrOic6iadPnlsFaqMTqkJOhD7qs4uDp1DKRR0aRMZqjVStS7OVJicsIQbh7HUKjds3csqCXk5VSh6ToMZKOgoBnLE1wnx7I/640?wx_fmt=png&from=appmsg)
这里可以自定义上传路径，如果路径不存在则创建目录并上传。

#### 3）尝试上传文件到可解析目录

我第一时间想到上传到 static 目录，因为这个目录是可以被直接访问的。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFH93DnjMbYoTAy8X1pxYAk2bXWZXzgPNBw3HgVUQzYb7Id8RWXAxpyibMxdJktFvoJyYHdDtjawdibnUiaGeXdaVY82zLBsTMRkA0/640?wx_fmt=png&from=appmsg)

然后尝试访问仍然是 404。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHgqCGwXcCdy6nAxfAib2BoQ55MAu7ZarAlib1qtCE12YOnZrGRsljjpvNA2O8p7fQZbxOu3sEgq8IgaXtXMgOHBgTI6gKvIUvrw/640?wx_fmt=png&from=appmsg)

这里就是我没有找到真确的路径。想去官网直接下载源码，点击下载后回要求注册，注册之后也没有发现哪里有下载源码的地方。

![image-20220414092738726.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF43NWWR6jwuprWdd9IKURmxv0iaqVOhic39wgicu12bxiaRmWV3NEk6NmIUsKFdNzMVJ0W3GqZfA4Ig2sasSB6StzibRFUWmibJLSGc/640?wx_fmt=png&from=appmsg)

没办法就去凌风云网盘搜了一下，发现存在历史的版本，我感觉差异应该不会那么大。

![image-20220414092826967.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHRzxarCjTYaQflfVJavvpdF5F2qTZ0Gf3cibW0lLItrgA7uM10L7iaQTWO2ezBw2BUYHJ8O22hDWOTsrVXNlAjhk6JmddEbWKz4/640?wx_fmt=png&from=appmsg)

挑了一个比较大文件的下载，解压后可以查看目录结构。

![image-20220414093004440.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGskiaMP60RDCOf6Mc4NE6K5dwibkU1Q1x60qiauTZQYOzMGialDf3CMXKLo3kYsibabe1iaMiahicaRF1u07dnXI8fwIVhvMG0Qqzs7pM/640?wx_fmt=png&from=appmsg)

看到有存放配置文件的地方，我想看看能不能通过读取配置来找到绝对路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEPB1S9NBUEzyfgZolW6iaS8zjM4HlfLAiaUGM98ZmOE0gn51SpY8I7NeqaTibsVMUDAkyZo7oCY9GLT1tknLH71pUaQkVlcibB6SY/640?wx_fmt=png&from=appmsg)

结果还是路径不对。一番尝试后无果，突然想起来站点的目录还没扫过，直接 dirsearch 来一波。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFF81ibeIpybBjjJMcksegFUcEIGh43cYScfsZdPhqTiblFQkiaTUkaIEjblibolvseV5IxHBrMMEEjykeXwyX8twe2gswVVfcceCHE/640?wx_fmt=png&from=appmsg)

当我看到扫出来 web.xml 这些配置文件我就知道有戏了。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGtJ0MyUNeMD2J6ygehcExaubfsNYNxs3a5s8Cj66XITjOnJHxWWlBBhLAdZp2ODtGXEXlU3SU8XM91kk9Te07nKk346LOXh1E/640?wx_fmt=png&from=appmsg)

在 web.xml 中没有发现东西，但是在 `conf/server.xml` 发现了站点的另一个路径，我觉得这就是前端访问的路径。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEyL97eibxsIseMNncQkYeap7HPd6gaWvHE881Q6zoAoPZgIPCb8jLxias5MA4ibyD3OmticZgJ3efB9uxd1CK7pgibaw3JouY2icoBg/640?wx_fmt=png&from=appmsg)

通过任意文件接口尝试构造路径 `C:\tomcat\webapps\xxxx\WEB-INF\web.xml` 发现有内容返回说明我找对了路径，然后发现了 404.jsp 存放的路径，对比我们之前拿到的源码发现我们成功找对了路径——上传文件到 `webpage` 这个目录**绝对能解析**。

![image-20220414094047472.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFyrt9UYOzS8yzQoe6tkNFzF2rib6qzxWLUpWe8brHicn7Mk5IG2ichic4p99tcHvlv2Picg10Fw5dibBM7lbFMWtQBUHpkqI0Xk867U/640?wx_fmt=png&from=appmsg)

尝试直接上传 webshell。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEE1pVE10FYqL5rd3mPE96siaT4iaT4dzJcdxAeS39UzOfnQicro1lFH68mpnvI4nlkjGicaJIsFmRfCRIojTDfd7ReiaHuEEGuQxPk/640?wx_fmt=png&from=appmsg)

发现文件真实存在，但是没有返回东西，我用任意文件读取查看。

![imag...