---
title: 记一次SSRF+文件上传组合拳进行getshell
url: https://mp.weixin.qq.com/s/KdCaUAE8SoRggu_xYJRMKw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:33.754808
---

# 记一次SSRF+文件上传组合拳进行getshell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTiaFCabjZEYokcGdVLXDeMPmPIjZxqlBvplKNCUoibABm4oGRJQroxuSUicrmNluctx8q2o2KVFP8dvEzrz7rCwLGniaIhI3Mkkbg/0?wx_fmt=jpeg)

# 记一次SSRF+文件上传组合拳进行getshell

kirano文乃
kirano文乃

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:kirano文乃原文链接:https://xz.aliyun.com/news/91668
```

前言

目标：某src资产，只有一个根域名，但是拥有多个子域名。

# 0x01 druid弱口令

#

1.前期对这个web应用做信息收集时，没有收集到任何有用的信息，它看上去就像是一个简单静态页面展示（这里就不截图展示了，厉害的大佬能根据页面找到这个web）。但是当我打开浏览器devtools进行抓包时，发现其存在网络请求，并

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTZBYbvWONIECnTn4E9czozWK3oibWMOexLx7jvtSpX6eJ1licIt63UPsk1XHHiaa0XhJqomQPeGD6Fib2Cchh1lU4aRT2V5yDY9ZY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS0m1u2W8w8R3eaibXLjjHGmicKKPiagVgunQKcm6Vk7tuaFfBsGia6OYk2RcIXUBewTEqh5XmBsgW1wwf4ADoquuMVhMqwUjJRcn4/640?wx_fmt=png&from=appmsg)

2.如果是前后端分离的项目，首先想到的就是java web应用（按目前市面上主流开发来看的话）。并且如果是spring的项目话一般是会有默认报错页面的，这里为了验证猜测，我直接在浏览器访问了这个路由。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSNgWYZMtp5ZEHyrA6WfZ7MM952WAhn1UIu92FWKC81Tqp2ERD5f2FdW4aUR5kxia6YnXvuuiatoXgFdCdfn3OVlVU2gZpUcDIa0/640?wx_fmt=png&from=appmsg)

3.显而易见，这是一个java spring的项目。spring项目一般是存在很多敏感目录和敏感文件的，我们可以使用字典来进行进一步的信息收集。这里我用的是曾哥的SpringBootScan：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRBu0voMe8P3g0ZVfvegIVrD7hU7cMgDy5FsIe8V9OfrseyPI6v1oItcsguQUKGicNkZFqvqgqWNCe0FfRx88X1PViaKH3uPyb7w/640?wx_fmt=png&from=appmsg)

4.发现接口文档路径和druid的登陆页面，这里我先打开druid的页面看是否存在未授权或者弱口令。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR6y3qtDoYwfe6sLibV9kGLZ3IHxTLOMMyl0tU8oFEllgiaM8ZXk2OT8WiaMTIukynenibib2iaz9e0PaITkSS3WXpM2kdJCk2K2g1Ck/640?wx_fmt=png&from=appmsg)

5.好吧没有未授权，但是存在登陆页面，只能默认密码或者弱口令爆破了。结果直接默认密码登陆成功了，成功拿到一个druid的弱口令漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT5TG2j9CqQicwSRGRwHLwJs3Tz9QfC6et2dHKTpc9YqzJ5JaeicYFlyz0J8IEJNprH6XfEm1xibzZCibuYIKakFgMRaVibdYSk8uQM/640?wx_fmt=png&from=appmsg)

6.然后我就想能否找到后面页面，通过druid的session监控里面的session爆破session登陆到后台，可惜并没发现任何后台地址或路由信息。到这里只能放弃了。

# 0x02 组合漏洞xss：接口未授权访问+文件上传+xss

1.根据前面SpringBoot敏感信息收集的swagger文档里面，我找到了一个文件上传接口（存在未授权访问）。由于是一个jar包启动的项目，他不像tomcat中间件启动的项目能够解析jsp文件以便于我们获取webshell，对于这类java项目通过文件上传的方式获取shell是不太可能的。于是我就想能否上传一个html页面，实现一个xss。请求包构造payload发送结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSey9OjICc3k1jibiaqiaWiaticMcRicnIZzCItI6upgHvY125VDcibogxlaaOVicwlSyicBicib2uH36WMd8LoUZX9nxpUKdmTL9mTw5a1rg/640?wx_fmt=png&from=appmsg)

2.他是一个图片上传接口，但是我将后缀改为html是没有任何校验的，得到这个返回结果发现只是将文件名重写了并未重写后缀，访问页面，成功拿到一个xss漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT0lia5jqSDb2Pk6IlTSeAu6stB4ib5w4J06JlcEP7JSADMicREoRcjBr4ickgTfAhNoxSYKKhvvd4iaib7z86vdH8ibYOPEZVeWMBgqw/640?wx_fmt=png&from=appmsg)

# 0x03 java组件存在ssrf、任意文件读取等多个漏洞

1.swagger文档没有获取到其他可以利用的点，跑回前端对前端代码做一个简单的审计（主要目的是挖掘更多的路由、url、资产地址等），这个位置存在了大量的接口地址信息，并且有一个地址很独特，看名字像是一个图片预览地址：/preview/onlinePreview?url=

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRpViaVvQ45SxJibxmEmBWb2qyDlHmnBXxYLJic8yC40901GK5akSS6sFvRSwPnQINaV6GvicvI5Osrn7whNtIGPj6RBkW3uNwruG0/640?wx_fmt=png&from=appmsg)

2.访问地址/preview/onlinePreview?url=，页面如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ2rZ1AOfMcBubPpoKzrJUuk8L16QoB2nYE6myI9cATtG3abLnGLJI5WShc5tKLTZia8sRQXSa8qDVXFkgZbLMNAdhsUsL0wzPU/640?wx_fmt=png&from=appmsg)

3.直接拼上百度地址首页图片是springboot默认页面报错，虽然是500报错码，但没有具体报错信息，无法进一步利用。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjsDzsHiaYfxLCpC3Jt9YpcknH5t9VnJ39GtHlllGpRoyicI7SDonbfecs2g7U4ofH3ib76fy2JcQY8IjMB5z5QAuvHOib2GLiac2Q/640?wx_fmt=png&from=appmsg)

4.然后我就去掉了url参数意外发现了报错信息，这里比较关键的是这个包信息：cn.keking → 进行进一步收集发现是一个叫做**kkFileView**的java组件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboShNr5lqeOdXTzsEH7yaia3pugnmdqt3uoaGDSSKwdNl7LOy2EoSibibU5ISRO0h24J4221KF68OKEulnEwJDT7Ns3wCocqGDqL7k/640?wx_fmt=png&from=appmsg)

5.查看官方的文档说明，发现其是一个单独的springboot项目，并且存在一个主页面，上面会记录其最新版本更新说明。

思考：如果我能获取到目标的这个kkFileView服务主页面的更新说明，能否根据其版本信息查询到一些历史漏洞呢？→ **最终得到其版本信息为v4.0.0**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQVa9jLvW9QIOTJiaI3sN4UgRicheL1BvnsadmFNrpVTY6bSZTDxib9G027MQpx4XPsASKyv8EetUZQGKONPUa74D7bvlLVAhe0d4/640?wx_fmt=png&from=appmsg)

6.收集版本对应历史漏洞主要如下：
1）存在zip slip文件解压进行文件替换造成的RCE
2）SSRF
3）文件读取

（第一个漏洞危害有点大了，他会替换文件，实在不行再考虑利用）

## 文件读取漏洞

这里我们主要是用了ssrf和文件读取，最终利用成功，这里我读取了/etc/passwd：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCLK7Swvug88DqNwIFJAPtamh1picia9XxtwKclibLhScRCymzyEwnxjR3Zs7tUz2dXicxTJPmWruGmJEfdAZbreu86LiahwIoBHAA/640?wx_fmt=png&from=appmsg)

## ssrf漏洞

然后读取云服务信息，这里通过whois查询发现是腾讯云服务器，读取元数据信息：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQKxXwa97zf996w3QtibgDqnpuKyrxiaOT8l67Y9lfbYOUIHAb0QJUMYwyQQdBM3a4ImxN6HNkpJ8Smxy3tUIJIiasNgQsvIfwG8c/640?wx_fmt=png&from=appmsg)

后续我想通过元数据信息拿到accesskey接管其账号，没有利用成功（有厉害的大佬可以交流一下），貌似其并没有开通ram信息接口地址等导致我无法获取临时的token。

# 0x04 通过文件上传拿到webshell

1.最终我还是想拿到服务器权限，有没有什么其它方式呢？ → 把想到了办法都用了，搞了半天，最终还是审计源码给了我突破口。

（分享点小经验，当找不到服务源码具体路径或者其它文件路径时：不妨查看一下.bash\_history，说不定有惊喜）

2.通过file协议对其服务jar包进行下载，反编译后审计，找到一个文件上传接口存在路径穿越：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRvVa8XARXuefTGmvleicBcicCvhx1DVEp5qUWJ5ibvuMMeKtc8C8rIZSia0ib2Pxdze7Gf8YLkibDFsPMSgUt4TZrHzPHM5CMGFoc7I/640?wx_fmt=png&from=appmsg)

3.第一部分path是获取的config.properties配置的路径信息，第二部分filename是file.getOriginalFilename()获取的全文件名，后续代码并未对其进行过滤直接进行了路径拼接。这里有一个问题：如果存在文件名为../../../，将会达到一个任意目录穿越的效果，最终形成任意文件上传到任意目录的一个漏洞。

4.这里由于前期的信息收集，我是发现其存在一个tomcat的服务。于是我利用这个任意目录的任意文件上传，上传jsp后们到了tomcat服务中。数据包构造如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTUZSeGiakS71uXong3bxAYCwNAOa251GRS7ShOOgAGibMpy2zpXRjibB5CkxBbeszkBzibpuL143QfNica2jA74BkocAuSib6KJPjRY/640?wx_fmt=png&from=appmsg)

5.通过哥斯拉连接后门，成功拿下服务器权限：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRCUaFRhsg7zvsGx7QpsicgU20VrgQ4HRK6z52aaBcaUV7apSYibqynKDmv5z2moLQtZlMia03muictxeibiaR95vib06dpXv6UjpjSYI/640?wx_fmt=png&from=appmsg)

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY...