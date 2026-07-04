---
title: 分享一次利用大模型对SM2加密的APP绕过的案例
url: https://mp.weixin.qq.com/s/3nL0ZEPJzD6Rz2y66P8erQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:37.553106
---

# 分享一次利用大模型对SM2加密的APP绕过的案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pms46XiaGB2ydw1rxrUich65uBGziaEFmsSTOkdoiblZSficSDK7M7jxTmNsRG5XGxXLJp15kWSLGsMdXI3oibtYezAiaXV70IuR4Cia5UKR6wUjUaI/0?wx_fmt=jpeg)

# 分享一次利用大模型对SM2加密的APP绕过的案例

原创

Vlan911
Vlan911

我不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

首先APK没有加壳，可以直接frida

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zm1FaYYVZVTGibVWLXyolGlGiadawJe2RARBraNFQKyG6yRTHPiaRQJ9hVOr8wuvZmJga5WoN2ffYPTJfliahbNgicGhIjmiaiaBAvfk/640?wx_fmt=png&from=appmsg)

经过测试发现，实际上APP对http代理进行了简单的检测，直接抓包是断网的，这种情况大概率是存在SSL Pinning，使用socks代理就绕过了，这里可以使用Proxypin或者Reqable，Proxypin是github开源的一款工具，轻量化也很方便，缺点就是有的时候会卡死，会被检测导致部分数据包抓不到，但是Reqable目前没遇到这种问题，所以推荐两款工具结合使用；

两款工具都有PC端，Proxypin手机端连接手机需要设置外部代理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yYHvn3tfS0w1JdZfMTRr7vciaS9eFyaqkCqOwZzZ8ElEibDmnSiaolNIh8chZhvBhHMaSib9eucTy0jSF9dzwL4OLyt9np0Ezowh0/640?wx_fmt=png&from=appmsg)

而Reqable的移动端和PC端都登录后，移动端可以不单独设置外部代理直接PC端

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zhLgEhNeeI2ib9eYe4ahXXIsXiatahEqUD6TXWicECxCuibYd6c0QvUib2Qmx7TnL0ic8Gic4843Yg4CaYXjns7FZiaWwCXsRcxEyfoPA/640?wx_fmt=png&from=appmsg)

简单对比一下二者，仅代表个人观点

|  |  |  |
| --- | --- | --- |
|  | Proxypin | Reqable |
| 是否需要证书 | 是 | 是 |
| 是否免费 | 是 | 基础功能免费 |
| 是否存在维护 | 是 | 是 |
| 是否支持多端 | 是 | 是 |
| 是否支持移动端白名单 | 是 | 是 |
| 是否支持二级代理 | 是 | 是 |
| 移动端与PC端是否需要额外设置代理进行连接 | 是 | 否，可以扫描连接 |
| 是否支持HTTP/2 | 未知 | 支持 |
| 是否具备脚本能力 | 否 | 付费功能 |

而后可以将reqable的代理给到burpsuite，我们看一下流量的表现形式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2x422KQhJjCEDXFXYMDm0cm5ictBibj20eRnc4sfDv1ZatvIfDlf9EsmWrBSB08m5xhjwVsmJsgJWOxqKgZ3ucrMfFkWSs7KRLU8/640?wx_fmt=png&from=appmsg)

一般情况下，同一个请求触发两次查看数据包是不是变化来简单判断是对称加密还是非对称加密，但是现在的请求很多都带时间戳、uuid、验签之类的东西，就导致结果不准确，特别是app的也不好做动态调试查看堆栈，如果对app不是很了解，或者加密方法采用国密，那么就很难使用github的通用hook脚本去获取解密方法，那么这种情况以前需要我们去app逆向看有哪些加密的库，然后去hook，但是现在有了大模型后，可以直接让大模型就帮我们调教

本地环境准备：

|  |  |
| --- | --- |
| jadx | 配置jadx环境变量，用来 |
| Python 3 | 运行python脚本 |
| Java / JDK | 运行jadx工具依赖 |
| adb | 连接移动端 |
| apktool | APK反编译 |
| Frida | 动态hook |
| frida-tools | 工具使用 |
| rabin2 | Native so分析 |
| Android Studio | SDK相关 |

“帮我分析xxx.apk的加密算法”，只需要告诉大模型我要做什么，大模型就可以根据你问的东西进行自动化逆向

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zqHOZjiaSYAVTFJ0gt47kyZPCEwjjicAVKchV5hRtlZZ06CbnuvudMicmhY1c2F3sibrl2ibQMiacSD8c1e1e0Uct29ZYgcrdZg3fSM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2z7LhBRVhHBV3LRicmTznLLlYIoTnIN6DogdwWJDxcX5399NP1HqQfV6ibE4hxagJsK6HIbqkSicIuUfA6dffJHQiasiceDqSl8Hv60/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2xc5TwoBHqorZlzaZoSsVibcv0uO6UBprdhWialz9mYOVb1DOo0784ibkSVs0T4NVoicAcAnibzFw2Tz67ekKXaO6bD2Vf0eaAMAGsc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2yhUgqLSbiaHuqciaSrkIKjHm6BW9iaxSmAJFGuNIx0RzVHq3ibhccltLkRtny4YODBWBkeyK7elpCPEiaqUeC3PtMsIJXemicxzTqWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2xzYdS54emR4oloOcRVR8VAT0MiaIiactkOcdibKswtjZwnCpXX0se9k9rTVGPSVBcLXWjNMHG60DVLaHoeULvarv45Etic8pKthzo/640?wx_fmt=png&from=appmsg)

分析的非常好，通过解密还原的源码是能对应上的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yjSRcZOibFFDeviaEU6s6YRll0cID8ICF3X8OscktPUUBDicryox0ZoXEzu66tjgPFeXhehFqHkNKsW4YICMQ5O9ATCEiaUNJMFVA/640?wx_fmt=png&from=appmsg)

frida 脚本这块，可以直接让ai生成，但是其实jadx是支持一键生成的，只需要给封装下就能直接用

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2za6jLw5IsQibdecQKqNVn5voMicn3wo17ukbhM4adqNZ82lICycTVbroRfMdPSR8HUIQiar6y67gQ8oRtN5hfmlJ2cMWd5CKECkw/640?wx_fmt=png&from=appmsg)

简单封装下看下效果，已经能看到请求和返回的明文了

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2yRwicYIZLfibfT2TybxaWG4cFiaPoe4734ANFXhlqcic4UtTGtpLNRnuoqdSXJiaGCJaLeicv9NYMQPFAfuDSlxf9a1q77ZibLSiaaSOw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zqBDmn8kDovxAxAl1WCf2bUdgib7vC6xF7fOCojTkH6VOf6OwOLtRwaWHbxCvmAbJhbbxIpviacU7ibicvXf1U4y1R1s5kQbfhEKo/640?wx_fmt=png&from=appmsg)

app的hook相对于web端或者小程序端的来的都腰方便，特别是这种请求和返回用的不是一套公私钥的，很难使用类似autodecoder这种插件去自动化加解密；但是常规的apk hook只能解决密文问题，并没有办法直接改参数去进行测试。

在得知了返回包私钥的情况下，使用在线sm2解密的时候并没有成功解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zzSibCzhjv9ibVU3CuL6ksLKbgsocOkwITZcNkHFenR8EfKdYlm0ibdoU4nibq0cZv4cndtYM3h1uR1cVU8IY9pqtDyjyzibjevP0U/640?wx_fmt=png&from=appmsg)

但是不要紧，直接告诉大模型，给我生成调用app原生的加密解密方法的hook脚本，再生成python版本的rpc调用，实现直接调用app原生的方法进行加解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wms1VPgjpv7xaibrKFrDYqBicXfWYoRMCp0dDKHe5otiaOvVH1y2GTAPrIRibnLWm95TKAvG9Lyp4KdT9icUBUjWCbfzoOiaMNUJGV8/640?wx_fmt=png&from=appmsg)

由此完美的实现了原生的参数加密、返回解密，最起码这样可以做简单的测试了，当然了如果想完全实现burpsuite全自动化的话，也许需要单独接两个mitmdump脚本单独对请求、返回的自动化加解密

apk部分解决了，接下来看服务端，在获取了服务端的代码后，可以让大模型帮我们进行自动化路由分析、参数构造和代码审计，而后将审计出来的结果输出到文档内

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zicq9A6XL2xiciavQyDE4FHHnsXFnNOmRgbsfAkHArQROgPA7AGMZQ5mFuOzrWDAhYqe2QNEn1Vq1ic7dPcsH2pRCA9Uk46gG3E3I/640?wx_fmt=png&from=appmsg)

但是审计完效果暂时还没有达到百分百成功的效果，七个关键风险只有一个成功了，只可惜的是并不能解析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zVFrUHMHr4MHnnj6QOMK4nV9wkaHqoFLn4RXicjA57pkqvKAngWBNndghPicXIBibZxrYHMlOVicYP7xooFfGrA0CR34aKSpuBArM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2z4mkOc6IvhYxDwtukhtRy98aEqRYjXm0ib6JqIa4Q5Bfp0qcxCBqicXkuaZwiax7TuK2mxwwiaCqcLo8mLmXUTdyUQkWvFI3l4icdY/640?wx_fmt=png&from=appmsg)

但是很尴尬，因为即便上传成功了，但是并不知道上传到了存储桶的哪个位置，也不知道存储桶在哪，这里掏出了古法代码审计，追踪到某一个接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zI5WOe8fr4JIDJE6fkeB3GqstuHAnY5QUx5njJQkjRWK8h0AuiaRrUduHKwUks6PTNeNAWRxM4KQw4KGuLc9tqDVUkxJxIT9Kk/640?wx_fmt=png&from=appmsg)

查看参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2x0uzyCDCZOxE4Rc6wvD1Y7QSy2mC7PkWypHhl3Da6gNiapKbjhhpKFIZ9JFE4XfLJFN0v8PSG1wicbAegeI4QFklN16X43ruWmQ/640?wx_fmt=png&from=appmsg)

由于知道了所有的json参数都是需要加密的，所以直接构造参数，然后利用rpc直接加密

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2ztmEEKlDDqwzb4cFO3LsCibibyicKUG8nkFVX3a1fiazAhB4q59qQcRIzyWUs56ftiaAqe0KeulRDX3RUMnGFZu7A8PKI0siaLDxdlQ/640?wx_fmt=png&from=appmsg)

将生成的body参数发送到拿到的接口

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2yudX8qibzIQF6ptFfHQupdtmcQibP8WeN7R5M6kW7IpjQYkXxkic6Gd1QWV3hxBJs8muiagASogVbdm6mN9hBzhMfZCtzAiarCc8sE/640?wx_fmt=png&from=appmsg)

此时虽然返回包加密了，但是依然可以使用rpc调用去解密，打厚码了，凑合看吧

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wT8xwlZaeKbTTmobKLklfibJcLUDtOhmbEcyJEomKicY3sqbYzhKhO5luPzEku2ujMjLickMiaAKn2VRcDwSGM7fMwZ28mkS6eH7Q/640?wx_fmt=png&from=appmsg)

此时访问拿到的存储桶地址，成功访问

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2yibrSYVmmIJYkZFIYZaR4hTofPRp8Sldt9KeKJUqKmYSicGeNeB1Sz6hgLI0nvbZUYibO9iaB9oMRBxdRaiaw46tFm1PQbDBW2w9sg/640?wx_fmt=png&from=appmsg)

但是并没有什么用，因为这个存储桶配置了只读，不能进行解析，连最基础的xss都触发不出来，就这么一个烂洞怕不是要不好看，于是只能返回代码层看看有没有什么逻辑漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2x1bbzVHibBvcCyGvUvI7IzWGfc906eWGmTBbneZQ1OetLlOMgNqVx7K63icRmrqy5APsohel5LdrnS9ZCgQM2TpDvdURkleJeV0/640?wx_fmt=png&from=appmsg)

发现了一个隐藏的创建用户接口，并且接口只校验用户是不是登录，没有校验用户身份，于是直接构造数据包进行参数加密

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wibmj5ribfA4TLXMRDHBpCm0KknxDN82uxSicxZGaN82wDJd0LpGFDdGicyJOK31WZK32uic5cZz6ZXuajkywQ5rXJf9ho5T3U3xOY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yf0PC3IiaKibfVyjGmuRic4Eqt0mLw61jJQrKR2Wa493Tq4SOvQQxU7Is4rNRuciaf8SJ3hsFapP5PprYtu83iaCvk2iaAFWOchyHJE/640?wx_fmt=png&from=appmsg)

此时使用app使用新创建的用户，登录成功

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2zxdM4RP0dhjSOU2iamuRFIuwn271F9hpXkKnKFs2bNCOTrlGRO4pia9WGVwvRua8rXE6FDhuUf3FJKBbiawDWvJHxzGeKyG9SV7M/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53CvPTYtF0MQwGlmN2KPXrVZY3NOceKBhsuicQD311jGc16ktCkbrTWicoNe6SibKmkov45Nib5qntvug/0?wx_fmt=png)

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