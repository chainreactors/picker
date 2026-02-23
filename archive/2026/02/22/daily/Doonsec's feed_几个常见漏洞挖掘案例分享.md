---
title: 几个常见漏洞挖掘案例分享
url: https://mp.weixin.qq.com/s/v6bW3AwyovI0R2YN7F3viQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:00.361281
---

# 几个常见漏洞挖掘案例分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTu0cZjeAERsCGtQuLj8vHn1GsxMLS5OmBl9GoCic9hts5ia3KIROX5ykYLsqxulGsyydELK1c0Nu69ZNjpNVjHpIF2gNz7TguxE/0?wx_fmt=jpeg)

# 几个常见漏洞挖掘案例分享

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:用户j7LlalOmNY原文链接:https://xz.aliyun.com/news/19133
```

未授权漏洞

未授权漏洞我认为可以说是另外一种越权，相当于从没有权限变为有权限的垂直越权，主要还是由于未鉴权引起的，如果想遇到它，我想必须在前期做好信息收集的准备，未鉴权接口就是绕过登入限制的一种方法

#### **案例一(未授权接口实现的越权操作)**

下面的案例是在挖掘某证书站时遇到的，利用不难，主要是需要收集好接口信息

在某学校的资产中，我找到几处接口，通过不断摸索发现其就是查看资源状态的一处接口，具体的效果如下，其中包括资源的发布人 发布时间以及对应资源的状态信息如是否上线等

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRfVa2tcrD8fzI0IHyS8lMqOuJMVjA7DVBPD3iciaJLmGEiaJD1iaLOoDLYW6vyWN1IDQk7fTibD0wcePcTQ2yiaOibPADFbMV9SibeOrc/640?wx_fmt=png&from=appmsg)

我们查看对应的资源与上面的信息呈现出来是一样的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbdyUJr3ylibAGMrL9LoY2v7JpFULkYeaOMeiaf6XcmsbVQb23HfE6XJscddnm5ibKUibd1bM1kNQUHaukrmshkYokVyzcaFDuNDA/640?wx_fmt=png&from=appmsg)

上面还不足以实现未授权，真正的突破点就在不同的方法请求时，常见的请求方式有GET/POST以及常用的DELETE/PUT方法，通过返回结果就发现我们是有希望的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT2oRyibag35hRtBThu1HyibdL2UY2OuelJTHnZRVasYPH24IaxXoITyOkElvy9EzWyCOod7Oa7BrVXyiayhtk3XQb1OXK9VH8QibM/640?wx_fmt=png&from=appmsg)

通过不断修改真正实现将对应资源下架，以及通过其它接口实现资源上线

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS7W2h31rpJMYEDmyEow6nKBTp8DDuS36icCxxzY06R8AHRVZWrTQySnQyK5GObcsRJE7LXsfkJpVBWIAnfCAWBeceAOuEU9Bv8/640?wx_fmt=png&from=appmsg)

#### **案例二(前端校验导致的认证绕过)**

在对于访问后，后端页面部分一闪而过的情况，我们拦截响应包并修改实现一个欺骗或许会有不错的结果

目标依旧需要登入，但是我们依旧无法获取账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS2dF9uC1Q1LgdicAFzbdgTjShIzMoLln2MsFskLdtjvTpsvEA2CdsMYnPQbvACicBZk6iaCVpicBMYzJRVD9uBgGhk2GmHtab5lTA/640?wx_fmt=png&from=appmsg)

开启拦截，拦截返回包

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRd6PUTXL5OjFjI82yibicqLkueQpWTH6pjibH72E0hXXsE0ZtwpmDT3g2ib9OU6FSn4XJgkm6s6cYm2AxyiaQGe9OlYq0vxxPvqDbc/640?wx_fmt=png&from=appmsg)

接下来放包即可，找到我们涉及鉴权的地方，这里它的鉴权比较特殊，通过后端返回响应包中的js一部分代码，对一段时间后进行身份认证，如果我们直接去除或者添加延长时间同样可以达到对应效果

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT3E1japEVkmyR6CHJ60fCwgMCokHiaHX5QI3J7rPQ37yWNkgMx8cwicSQEjyJyJoJr65eCIuZsKouB4T6Rib99kicEu1iaN2LSVS8Q/640?wx_fmt=png&from=appmsg)

最后放包即可进入系统后台，以管理员身份实现对数据的增删查改等，以及获取近几年所有的订单信息，以及对应的其它漏洞如sql注入与xss等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTQVgFFZggh1TpA7KLlAcnLlgia0Z0ILHYHmYXiaVrmRKo06ycnXakZm8FbbiblibdkSdN46aVFKiaTUpbKje1YqQFe8PDjBEyM5e24/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTiaM6IsAGpibulEeeFUSmzeeZ5ibxrDkofFcicUxD2n8JQdSsiawHFqgwk2oSWZ6FXlmnMicU3ke5BTplDDEeN0pPEEqULibRa4S31n8/640?wx_fmt=png&from=appmsg)

###

### **SQL注入漏洞**

面试官喜欢面sql server如何注入是有原因的，下面就分享两个实战中的sql server注入

#### **案例一(从注入到rce 回显带出)**

攻防中对于勤劳的人总会有收获，在实现某一政府单位的系统撕口子时，发现存在一个较为新的系统站，并且可以实现注册登入，在一处接口中我们可以添加人员信息，但是对json参数进行单引号闭合时发现报错，后面在不断尝试后发现其为sel server注入，并且可以实现堆叠注入

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSiaEJ9kMMsuQaeAA3MvNU3b3P2hFXKnLhXTrKkeIVM8D1mKCF4rrqLxhXrcgQOZzAgrqpsMPMg7wjsqcjXoqWrDobmT4ia6a08I/640?wx_fmt=png&from=appmsg)

下面就是通过xp\_cmdshell实现rce，由于该主机为mysql低权限以及windows主机，许多命令都无法正常调用，curl命令正常回显存在记录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboScq0wKsib6vnTibfV4icxsIRurfjfIUZYdRJia5t5vcafqIsr2XwMkP2zJCGCjqyc15JEqg0M1p0pDntMqdwpzv3ibhicxoT2Chbncg/640?wx_fmt=png&from=appmsg)

最后实现命令外带

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRaibadiaGyqnxdDjicEC6XcWyC6DoJSNOPtgNHyobJRN1dzI76zupx2hOOBqU8xJGjevic7sTMFYzZjhZSpvgm32uM7xOBia4owUwo/640?wx_fmt=png&from=appmsg)

#### **案例二(从响应结果中出来的布尔盲注)**

下面是在渗透测试某一系统时的结果，日常查看拦截记录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRxJAgFEKX6jKTXEzEn5zBByWaZ2TY7p145Gf6gHabYD3HClkdRaqQCNB9GDYiaST4u3n0AmlKLy6sgmDSCZTGR96hEspnp5MnA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQbU6HF7icvZjJSwiaPvibzUae9R8D9mSB8yrposND6cuPLia6tJ3TrM8wYyDQr5YfhTcBqYzu2DPJSo7QFQ7QC8TYoBUOlicMLeg4g/640?wx_fmt=png&from=appmsg)

对上面的接口解码后，对传入的参数进行不同个数的单引号测试时，双单和单个回显的结果是不一样的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVpS1x4ONGfzl2eVhm81GYoTDwfUNZ6vOmA9ozGsDJjtbib5HXK9NtD9NOVOArJic4rkpADq54Duic82j4Rb5yfFibg8ibsGzia3Pbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT6Eiciakb6B4gzybrO8yic1V4cFzj4xpoIyIvX2MLIZhymTa2M1auibGCWicBZ9d62N24STjJKGVF60Wibdgt13SicHlo5ZWb2cVmzlc/640?wx_fmt=png&from=appmsg)

很显然它并不是偶然，可能报错信息被防火墙或者代码层拦截了导致我们无法查看报错回显，下面通过回显不同打一个布尔盲注，好在整形溢出还是能行介于709与710之间，最后打一个模糊匹配实现注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSeDlIdHzy0cXPGibpziamUZYyzmYpWrkSkPgXdK6GD3rVNT94vmzR57APskrLibOiaLKUIH3h1QkibImhF4KGlxPia2Faf7ExeoXPV4/640?wx_fmt=png&from=appmsg)

### **XSS漏洞**

xss漏洞是最为简单的，不同的payload对应不同的情景，而漏洞点的挖掘可以是任意可修改的地方以及文件上传导致xss，多试一试总会有的

#### **案例一（通用型多网站下的xss绕过）**

对与最开始的试探最好通过h1标签，它是最温和的，其次才是一些payload，基于不同waf下的检测，下面的案例是通用型edu站的不同形式

最为简单的必然为script标签带来的弹窗，一般是基于没有waf的站点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRTSaL1Ek8UmEkCUkE2gohy9pqgLRCpu0VaLau8oW8hukJicpmiaoZUWSfzMslo9ibxKabOMDMicZDQRJibQ2xnMusEurJvicIAiakJNg/640?wx_fmt=png&from=appmsg)

而如果禁用的script，以及一些敏感的字符串可以通过编码优先绕过，或者fuzz加绕黑名单等

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS4kVzE9w6UDbgB83rtcoWO9YusKjgl6GM9nhLibkvvfobnhB75QczkkCs7CfHwaQ25fZchN3POVLXnJkTUvYC0D0s91APod9RY/640?wx_fmt=png&from=appmsg)

最后是基于waf本身的特性实现绕过，多次尝试后终于通过下面的payload实现绕过

```
<a %herf="javascript:alert('a')">aa</a>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGia0ELnTBg5lMwnprpYIjjicDTXSWibATsQmUegLgS0EHQY7Uv4PCoG9fsGYoXAYIwL86gIMKhwWViadB0MG5eKLSSJN1NxpM0ibY/640?wx_fmt=png&from=appmsg)

#### **案例二（文件上传导致的XSS）**

一般情况下很多文件是传入特定的存储桶或者特定目录，在无法getshell时可以尝试是否可以上传html svg文件等，下面的案例由于对文件后缀格式校验，所以通过上传xml文件实现的xss

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRV7pibIzzKBkiaEKzZFk2bPrpMH76d3xL5iakq9U1ydZIXD93W5FiasDFACS5WpdAIXsbDxxDEZJbdcJmJoj2SvibgicJKVcU8HVDjE/640?wx_fmt=png&from=appmsg)

页面正常解析，并弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQSJukGKaPgVnGder3TGA0llGPxabOSa0ZX2ZlHKRQG2lgeuiaeLhyfWibvchnn9CoLVWLfHvQJRh5RI1s5oyZehNzodf5MYU0gQ/640?wx_fmt=png&from=appmsg)

## 总结

漏洞挖掘不是一个一蹴而就的过程，每一次积累、新的思考以及新的尝试可能都是可以破局的关键，一些漏洞开始难挖真正遇到后慢慢在积累中就熟悉了，对于不同的情景、不同的功能点当用心去感悟它将成为你破局的关键，希望师傅们可以每日产高危

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSHaicovS7GZavY7ZDVjYtibm4kKibfHNonrHZyNYEP2apKicYGDhTMn0olJ5d6qhrvu8uqicZW5L4YdCjoZ3vqgsq4xau4ic1ZicVw9k/640?wx_fmt=png&from=appmsg)

后台回复加群加入交流群

有思路工具需要的师傅可以加入小圈子

主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/src学习资料等）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg)

部分思维导图展示

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg)

其他内容懂得都懂，可以扫码查看详情，目前300多条内容，持续更新中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboR62DgT5O1EN2BAoeuib0MK0Pl43pvCLVia2lKAnotaUfutyQ9licdV0TFBr4A6jnzbPX9rHsTtWdThK6kpSiaGEGWCEGesecVo3PE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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