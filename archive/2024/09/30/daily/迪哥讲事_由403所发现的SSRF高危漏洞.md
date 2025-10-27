---
title: 由403所发现的SSRF高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495980&idx=1&sn=3836d926af7f7a250ab81bb9cc036cbb&chksm=e8a5fb4fdfd2725902b8f15a8ac5c96133a29105f8175c5c833bf2b84988af37080230c81532&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-09-30
fetch_date: 2025-10-06T18:25:44.582841
---

# 由403所发现的SSRF高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4O9XwictrgmSVIR1a0wiaJ1Ka8HET8fKMic0SqVibqq3a3omGzq3n7PzsyGIwczITBAU6uWwnDibxoy6g/0?wx_fmt=jpeg)

# 由403所发现的SSRF高危漏洞

aedovo

迪哥讲事

## 前言

在某次金融类众测项目中，笔者发现了一个几乎无从下手的系统，直接访问系统无任何功能，几乎相当于404 Not Found，甚至连JavaScript文件一个都不存在，最终通过渗透经验和一定的运气，拿下了这个高危SSRF漏洞，获得高额漏洞奖金，在此分享一下漏洞挖掘过程，带给大家渗透测试中的一点另类思路~

## 404 Not Found？

首先，给定的系统地址为：http://xxx-desktop.xxx.com/

直接访问一下目录看一看：

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MlpUuERw19hvfMCRxKS729nGmJpic8icVWHMwD1ibtzfWPQxAXPpkMAs9Q/640?wx_fmt=jpeg)

打开发现一片空白，但是页面空白并不代表是真的空白，HTML源码中可能会加载一些JavaScript文件，渗透测试时，往往会通过页面中直接泄露加载的**JavaScript**文件，进行审计**JavaScript**源码，从而挖掘出更多有用的信息。

对如何挖掘JavaScript文件中漏洞，可移步笔者之前发布的真实漏洞案例文章：https://www.freebuf.com/vuls/255640.html

回归正题，下一步找寻HTML源码中可能存在的泄露点，直接查看网页源码：

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MJI1CWhaAQu6B8ibyiaS2eqau0mK7x0KEb3zTRoclYbM8ETic4XJs82FzA/640?wx_fmt=jpeg)

仔细阅读源码，不知道细心的同学有没有发现，其中有3个线索可以延伸利用。

```
libs/plugins/jquery.js
./html/apply.html?data=
cxx/token/decrypt
```

第1点：**libs/plugins/jquery.js**，加载了JavaScript文件，其路径是：**http://xxx-desktop.xxx.com/libs/plugins/jquery.js**

不过，此处**jquery.js**完全为前端文件，无任何可利用的信息，于是略过。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MKuVwDdcz03ice9C3yOkUvraeFBl0HPrWS6soq59xSkWQ9DAr8JibDLNQ/640?wx_fmt=jpeg)

第2点：**html/apply.html?data=**，加载了当前目录下一个html文件，路径为：**http://xxx-desktop.xxx.com/html/apply.html?data=**

结果也是一无所获，经典Nginx的404 NOT Found。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9M5TtnqseaJx8ydUDVgBBaLlNZicMpXOwFfVK9ibqDiatsmDZg5qoLn1SxQ/640?wx_fmt=jpeg)

第3点：**cxx/token/decrypt**，猜测为接口路径。

访问发现也是404，大概是还存在一层接口目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9M0Gg4D65mJue0szibvib9dVPFFeye9SxqKmIHBwkRDUdTniaG5CHog9xJg/640?wx_fmt=jpeg)

一番信息收集后无果后，接下来就是展现真正的技术了！

## 403 Forbidden？

虽然上面的3个可用信息都Pass掉了，不过我们还是猜测，在两个路径之前，可能还存在一层Web应用目录亦或是接口目录，随后展开对Web目录的尝试性爆破，选用一些常见的一级目录。

最终获取到3个403禁止访问的目录：

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MfeiaiakCR9w7twl7L0s9QwlQCJZK4Z3fdxThlakZyszWuRAlVCfWngnA/640?wx_fmt=jpeg)

```
http://xxx-desktop.xxx.com/html/
http://xxx-desktop.xxx.com/css/
http://xxx-desktop.xxx.com/js/
```

看来第一次发现得**/html/**目录确实存在，不过可能是**apply.html**不存在导致页面的404 Not Found。

一级目录爆破，未发现可用一级目录，仅仅发现了3个**静态文件目录**。

渗透测试的思路到这也即将中断了，不过此时突然萌生出一个想法：既然不存在能够正常使用的文件，那么我就继续去挖掘**403**目录下的文件，至少**403**比**404**要好多了，至少它是真实存在的目录！

## SSRF漏洞

继续对**/html/**目录、**/css/**目录尝试进行敏感文件扫描，未果。

使用**Burpsuite**的**Intruder**模块对**/js/**目录进行**JavaScript**文件爆破，终于获取到了可用信息！

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MkoGiaxwCe7kAMvW6XBuVFRSK80sO9AXcURuDjtTRwQ6S8s4qgxhcACQ/640?wx_fmt=jpeg)

天哪，终于是获取到了3个JavaScript文件，是什么时候变成了连发现JavaScript文件都无比激动？

JavaScript文件如下：

> http://xxx-desktop.xxx.com/js/apply.js
>
> http://xxx-desktop.xxx.com/js/pagination.js
>
> http://xxx-desktop.xxx.com/js/common.js

通过进一步的信息收集，在**/js/common.js**文件中发现发现了一级接口目录：**/xxxapi/**

一级接口目录都做的这么复杂，也难怪目录爆破的时候没有成果了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MTicZFuDeJ7gQPRXfIIeOr7CfB2jHTJ96AINP2jgFyRQtNU7sZwBkvgg/640?wx_fmt=jpeg)

在**/js/apply.js**文件中发现了系统接口：**file/pdf/view?file=**

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MDHIuKAcaic1NjmdCZjsSKv0zOSFpExpxYLicAe1riaMJvQh3CwcjztU2Q/640?wx_fmt=jpeg)

将一级接口目录**/xxxapi/**与系统接口**file/pdf/view?file=**进行拼接，组成可用接口：

```
http://xxx-desktop.xxx.com/xxxapi/file/pdf/view?file=
```

并且发现JavaScript代码中的逻辑是：**接口 + ecsUrl**，因此猜测**file**参数为一个URL。

接下来尝试调用接口进行SSRF利用。

首先，使用VPS监听端口，尝试直接利用SSRF访问我们的端口，发现成功接收到了Java语言进行的HTTP请求！

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9Mph9NBBCXRHBe1uvuHbaibEgL6uzp7iaJump3xvfxGyz1icicCtt0T7MMgw/640?wx_fmt=jpeg)

至此证明了漏洞是存在的，接下来利用**SSRF**进行内网资源的请求尝试，由于在之前的测试中，已经收集到了一部分内网资产，所以直接拿过来测试访问即可。

测试访问内网**Elasticsearch**服务：**http://10.x.x.191:9200**

```
GET /xxxapi/file/pdf/view?file=http://10.x.x.191:9200/ HTTP/1.1
Host: xxx-desktop.xxx.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9MyFictjFoFiaSjhooAUVj5uxEtuiboqKjjmEuF7SDHIkKPZiaqYMic1y61yQ/640?wx_fmt=jpeg)

测试访问内网**Web应用**服务：http://10.x.x.65:8081/

```
GET /xxxhapi/file/pdf/view?file=http://10.x.x.65:8081 HTTP/1.1
Host: xxx-desktop.xxx.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj48Ul9dxl0EhcJXQ6TZibic9M4oIbsHbp7bGlaRcDB4bCHxjVN99X1ubkbjSAhlDaCUNVDP3g7yCB1w/640?wx_fmt=jpeg)

至此，捕获了一枚相当于搭建了一条内网HTTP隧道的高危SSRF漏洞。

## 结语

此次漏洞挖掘中总结到如下几点：

**1.  系统无功能、无JavaScript文件、访问空白，尝试在HTML源码中获取一些信息；**

**2.  尽可能的在有用的信息中发掘更多的利用点，拓展思路；**

**3. “404”确实是“404”，而“403”有时候并不是“403”。**

> 从开始的 “404” Not Found，
>
> 到中间的 “403” Forbidden，
>
> 再到最后的高危SSRF漏洞；
>
> 每一步都仿佛是被上天安排好的剧本那样，
>
> 像是一次运气游戏，
>
> 又像是一场美丽的相遇。

也许挖洞一直都是这样，简单的漏洞随手可得，艰难的挖掘过程才会让人回味无穷~

希望能给大家带来一些简单的挖洞思路~

## 福利视频

笔者自己录制的一套php视频教程(适合0基础的),感兴趣的童鞋可以看看,基础视频总共约200多集,目前已经录制完毕,后续还有更多视频出品

https://space.bilibili.com/177546377/channel/seriesdetail?sid=2949374

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4eZjLhWic8G3TzELUR8ib1Mjr5HB1dhVJibpMFjrU0zYmTOOl05nYtSFOAbETlzVicVRY2BJAjPPQGjg/640?wx_fmt=jpeg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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