---
title: 独特的Js接口测试方式
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496212&idx=1&sn=ed865a31f4515b7515417406a3ab3e8b&chksm=e8a5f877dfd27161db2f68da67bb515091b1f3e1a2380fd5afcd7526a7076198e96288eb4a05&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-26
fetch_date: 2025-10-06T18:56:04.715963
---

# 独特的Js接口测试方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MTmB29pJFACjk0jZSkXXAVBavEcfkAnh32V9AsfNdtfPiba8gPr5QtjrdH7qrRR9ab4EqqRlE7aD1AVcbZC3Mhw/0?wx_fmt=jpeg)

# 独特的Js接口测试方式

迪哥讲事

以下文章来源于该账号已注销
，作者echo

![](http://wx.qlogo.cn/mmhead/574VdhMFwaFfLImg5A1CEvy3u7jvATicibOlBqb9a5FgKISWE85CAGhlPTibpU3rfMLGLRFmmovzpc/0)

**该账号已注销**

**前 言**

有很长一段时间没推更了,原因挺多，一是不想分享一些肤浅的测试、二是在做项目上的事情,保密性没法做分享。

今天给师傅们带来一些好用的JS手法测试

1.问题主要还是在内网,一些大厂系统在做运维喜欢把Js统一打包,包括全局的路由、文件读取的点;但这些都是在内网。

2.如果站点在外网、有运维有众测有多轮测试的情况,接口api都会做鉴权，引入token,这时候接口未授权相当于0,肯定挖不到。

今天分享JS接口基础测试不说了,主要分享**两个案例**，

**1.接口找到未授权路由网页,网页引发的sql注入案例。**

**2.多轮测试后发现接口未授权的方法。**

**0X00**

iframePath:"xxxxx/xxxxx/xxxxx/ManualStrategy/page/manualStrategy.html"

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhXDEEn1iahb2MzJrP09qVIfBMg9ROP8IxcgJW9PTKoWqDQgNZq1PvDjA/640?wx_fmt=png)

业务上线系统，有个iframePath的值, Jsfinder看到这个网页.html可访问。大概是这么个图

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnh9BXSAsG3aBsgd5jxp3dsTFp7JVmFBODOadeWl1ZHiciaDXegGOmF0wfA/640?wx_fmt=png)

然后这里有表单，然后这表单有排序点，排序点可注

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhKWfJkjjdaArjBYQaOibO067UyVyo0MQjiaCn0ibXFuQUbfnPuJOk5syZg/640?wx_fmt=png)

在这里拼了if('1'='1','a',1) 后基本判定是mysql，后续交给sqlmap延时了。

sqlmap的延时结果

(SELECT%204259%20FROM%20(SELECT(SLEEP(3)))eHZf)

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhqehSkeq2oqhUYI6ick4ocDoRfS3JtHQe32n40J29MiakQQF62bgUHBaw/640?wx_fmt=png)

**这是个最典型的Js接口发现网页的未授权，网页未授权后有表单，可能有排序，有文件导入，可能有文件上传； 但这不适合用众测、各大Src的场景。**

**0X01**

一些比较苛刻的情况,比如众测、多轮测试后，系统关键api都做了鉴权，

处理办法

1. **发现隐藏资产**
2. **测试chunk文件**

这里侧重谈第二种chunk文件，chunk文件包含很多系统全局的路径，如果站点这样配置

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnh6SFsuGPGDoLmp0QEEuyvx05xV2jtXXqqG0otLQdIR9sxsdEHIIbtKA/640?wx_fmt=png)

加载了全部的chunk文件，可以提取出来，比如main.js文件中路径较少、api较少可以适用。提取后成下面这样

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnh6N4rWjicOzt3ZKOkF6Lu2Uia2oZEhbJhMyC8QWZFqrhJY13pP6P6IK1Q/640?wx_fmt=png)

这时候再通过jsfinder等提取工具提取，就会有很多之前隐藏的接口，一些未授权的301、200

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhl4jAkrDpTsdIR5366RRrBKWxPuTcBKlZiamhxbmOBzqOF6ibgjbCdS9A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhLG9YbZstEMv4oCNGDOp14eB0GSl5v4yyWd46bljjqTAj5Fz3BJHusg/640?wx_fmt=png)

**可能对攻防、众测意义不大，但他就是未授权，可以写报告交差**

![](https://mmbiz.qpic.cn/mmbiz_png/MTmB29pJFACjk0jZSkXXAVBavEcfkAnhupFPLoOH3nrn38vXCZQap78TKJ69P9r5SIrSLTGsIf3VwAW2z4ZLiaA/640?wx_fmt=png)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

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