---
title: 打通最后一公里！只需一句话轻松拿捏小程序
url: https://mp.weixin.qq.com/s/xFHGvHC6ca4pO4QHKDY-4g
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:04.448277
---

# 打通最后一公里！只需一句话轻松拿捏小程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dEyB3AYJqQnWDv2By3eWtcuvV1daEGFpEuLm4IGkHBGhvbKNNJepOfxK2fCGIYptHXa8aPmUCBJibnvAujrADf1lpeicxwpY4DGNX8o74ZXvc/0?wx_fmt=jpeg)

# 打通最后一公里！只需一句话轻松拿捏小程序

原创

Windsss
Windsss

听风安全

![]()

在小说阅读器中沉浸阅读

本篇文章主要来介绍一下最近写的一个分析微信小程序的Skill，平时在对小程序测试的过程中难免会遇到数据包加密的情况，尤其是金融行业这些小程序，此时我们就需要强开debug断点调试或者反编译小程序去进行分析，虽然现在有了AI可以辅助我们进行分析但是相对来说还是比较繁琐的，需要先反编译，然后打开ide或者cc...一顿操作之后才能开始分析，为了解决这个问题，这个Skill就诞生了，不过这个Skill不只是可以做加解密的分析，还能做接口提取、敏感信息提取、漏洞分析、加解密分析，这四个主要功能，基本覆盖了日常的测试需求。

先来介绍一下这个Skill的设计思路，刚开始是打算采用纯LLM的方式驱动，因为小程序的分析跟Java或者其他语言的代码审计不太一样，小程序的代码量相对来说是比较少的，但是改了几个版本之后去跑测试发现效果不太好，主要是如果全使用LLM驱动会非常考验模型的能力，如果使用弱模型跑Skill就会有很大的偏差，导致生成的报告效果非常不好。所以最终决定使用脚本+LLM驱动，先让脚本去提取接口、提取敏感信息，然后生成相对应的文件让AI去进行分析，这样既保证了效率又可以让AI通过上下文分析保证准确性。不过漏洞分析和加解密分析依旧全部使用的是LLM驱动，这两个可以让AI尽情发挥，测试效果发现还不错。这个Skill本身没有什么太大的含金量，不过至少可以让我们在测试过程中节省大量的时间去挖洞。

再来说一下怎么使用效果更好，通过一个案例来介绍一下。

我是比较建议结合burp或者yakit这些抓包工具的mcp来使用的，因为有部分小程序是动态密钥，可能会先向服务端发起请求拿到生成的密钥再去进行加密，这个时候如果是纯静态分析代码或者是直接把单个数据包给AI效果会差一点。

建议使用的提示词：

/wxmini-security-audit 分析这个小程序"要分析的小程序目录"，结合burp mcp的数据包重点分析/api/co\*\*\*\*/V\*\*/\*\*\*Info这个接口的请求包和返回包加密方式,尝试解密请求包，严格按照skill流程执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dEyB3AYJqQk0vic3KZHOo3aAfsolxukTyv1UiaBKqQgknK07xuLCuapibf3bubUMol29trLSro2qMmIhbq7Uz3CibAEfygvyryMOhTSC8wLm2icQ/640?wx_fmt=png&from=appmsg)

首先会解析用户的需求

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQl0stTcFSmDnjskB5utiawBxL6rswcADDuYyOHtKyWm647GaaqW5vPN9VZ6pWLLF81DJ3DaLtxlg7dGVZvm8I9PYRK9JdSxRWib8/640?wx_fmt=png&from=appmsg)

如果是没有反编译的包会进行反编译，相反如果给的是已经反编译之后的则直接进行分析跳过这一步（这里要说的是在GitHub项目上没有打包unveilr文件，使用之前需要手动把unveilr放到tools目录下即可）

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQnUVNMujg7VBpZdTacgNwanuRSK7m0lY3Yk1H9Imvbu33BUNPiaQkvUrr3VH8NkriaSMyx2lGjyJviauBUz74lZM8U4pPg6k0iaUMM/640?wx_fmt=png&from=appmsg)

在反编译之后通过脚本提取接口和敏感信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dEyB3AYJqQn8GyZ6KlVhj8tpdwA3usAWOsaIxYKwrS6wXpGiaJIJGppc3N5kRBtz9dh9qBI5svUKjibiaSqyfbFicJOtHTURZ5YBFoP5zb4uibibE/640?wx_fmt=png&from=appmsg)

然后会启动4个agent，各司其职做自己该做的事情

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQlHIGdDxb6wfAgomrrEvE9k0Euia2jwxqF6zPFvIRLt7t3RoOgvvWorE6ibcy3ogDBMYgxicCcNY0C2Rh4CVvz0R7xT0bUBocIibbs/640?wx_fmt=png&from=appmsg)

4个agent执行完成之后会输出对应的文档

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQm5gmhbTsrtFGeWb4Zzvo6Q9BtrT4Hj0KoBxPqiaG9hb85lokicvJiaK4Iy0R0uleow9VRSfat5br6hYg6ic5PqMbkMWEXm87h3QCQ/640?wx_fmt=png&from=appmsg)

如果用户有自定义需求，那么就会进入到这一步，也就是我们刚开始指定要分析的那个接口，这里是调用burp mcp，结合其他数据包成功分析出来了加密算法包括key和iv值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dEyB3AYJqQlpdYjLfdpAZHT2eIsqF2ibxicGzp4RS2MJ9Um97icmouiaL0Yv9cTbM4aIicv1DCBn8ggJ5DIjVkx6BibQyhjZc8QedXialcVGVYNpl0/640?wx_fmt=png&from=appmsg)

最后就是生成报告

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQmssMqXDobP0RGGoKIm6Ig6h2jySPkJ8piaz56vWyLrIGf60nbiaSxsPTC6PHd4DqlsSKVuzH73wW2u2ITOwgT0T6ia6NeAaXWVSE/640?wx_fmt=png&from=appmsg)

我们先来手动验证一下跑出来的key和iv是否能成功解密数据包

请求包和返回包都是加密的

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQmufCZHf5y0zZuFTcZtAAqXklWY4d8S2UonMCySm1fawRSLQTj9nzMHa8PcsunAd70m7pKrcmjzGaGcJz2WzXnmARmNFYrY2yY/640?wx_fmt=png&from=appmsg)

这里要特殊说明的是这个小程序采用的就是向服务端请求获取key和iv值，但是这个key和iv值也是经过加密的，需要本地做解密然后再用这个值去对数据包进行加密，这里AI都分析出来了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dEyB3AYJqQnVqWjo0ccuf1B8U0h485R6MuPO5KbnTVqZuaFaTXOZbJ0tMOk65YriaPbSRLmGuKvsDbB3ibqMia7M4mt6TDYWWKQsEPD1elgL7E/640?wx_fmt=png&from=appmsg)

通过AI分析出来的密钥成功解密请求包和返回包

接下来实现自动化加解密就很简单了，不熟悉的师傅可以翻之前的文章

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQmYOrp60xUiaoWJldwhqnpvn8O7A88c6eqDLgdqThN38pXZWyQIg6y4N4ry01YruT7gr9Xviaf7ZAqJQxicziajrdghpe4uWd9NlJw/640?wx_fmt=png&from=appmsg)

或者如果感觉手动解密还是麻烦，还可以一句话让AI搞定

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQlPP5ub3oIvWxRiaMqqeyWsvZbRXUWO2W5O7XJSIUX2r9uQO6nPjf5IWKdqKNiaSBNUu31TT6r2CPNaNncW2bhbEHfWA4wddpMFk/640?wx_fmt=png&from=appmsg)

加密算法分析完了，再来看看提取的接口效果怎么样

效果也是嘎嘎的，这个小程序也是之前测试过的，甚至还发现了之前没有发现的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dEyB3AYJqQk5hfSiaeSzBiaaYh006H6y6tmP1bnDCSGW3vMf4Feiaa4J7sFrvIuSyCicD0eMq02Kvia0o4oB3rNsRQnoBOrH7XpX2F7zYcrOicsnI/640?wx_fmt=jpeg)

这里使用的环境是Claude code + 智谱的glm5，也使用过其他模型效果非常一般（建议使用能力强点的模型）

上面的这个流程跑完大概只需要二三十分钟，相比之前的操作，节省了不少时间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dEyB3AYJqQmYn2x7icX4FO2oLNkiaT9ddUpkQSxl03wG1O4KCQTqLEnlhYvq8rAJGyGicZ24ZSzUJdCyqzTaHHCWfb7sF6vBH8HGD1TpsBYZq8/640?wx_fmt=png&from=appmsg)

假如说逆了加解密后做了测试，又跑了接口等等，还是没有发现有价值的漏洞，就可以尝试使用下面这款小程序去测一测

这个是前几天花了两个小时搓出来的一个小程序，简单介绍一下这个小程序是做什么的：这是一个通过AppID跳转指定页面的小程序，可以直接复制app.json文件内容自动解析或者直接上传app.json文件自动解析，并批量生成跳转按钮，可以更方便的测试未授权等

![](https://mmbiz.qpic.cn/mmbiz_jpg/dEyB3AYJqQkn8dlxOLkekibsFqzNEQXg0ME5Oa1m7uzPpB8sFfiaAsLdr0GG3AdWu80exQC5OUE2qjhsdticravSoBDYJalWcNPMZ8gibeTrlY4/640?wx_fmt=jpeg&from=appmsg)

小程序唯一入口：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dEyB3AYJqQkavqgNsCTftDicDyrSl0Otm4icBia0mGzEiaOwRD1FOOAlHIFH2IDI8B4y4x3ibhN2sj3SV9ukjibw2IXAB6a8ugAia1SPBaY7b8xT6I/640?wx_fmt=jpeg&from=appmsg)

效果长这样

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dEyB3AYJqQlLVvVjPeOCE4LyXRGkpNE4jCPmiaEHCtICh8Avp0ic691ojPpTdf2qMWxwqgKztUHhBy8rU6meKV7QyPN2ibAEfNw0Liag0xASczI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dEyB3AYJqQlrp2NYYYKMV7ibJWSa0Vdxvtd4UBXiaxWAue33W1WS3E9f2VGiblBoHw09TFbPdrvt4U8eYial0IgLmXJhFQhkA1gJoYeUZRE5VibU/640?wx_fmt=jpeg&from=appmsg)

GitHub地址：

https://github.com/sssmmmwww/wxmini-security-audit

如果感觉有用的师傅可以给个star，您的支持就是最大的动力！

关于Skill或者小程序有什么问题或者建议都可以在后台留言！

![](https://mmbiz.qpic.cn/mmbiz_png/dEyB3AYJqQmCaBqx8DlhQiaGNzNBFzm1estCCnvLxrjUYkm9RXu5lcCkLlP3QwBibduGs2J6sKjK7tTicakpxlaKpRRgDpicibGnVUKnDLoJz0VA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycicRSPJOu3U0ibcANsALhypGSOJURbEuKF7g5rJsWOuF8U8OWdHxicyYEYGiadgR9NnxsBBOZ8EHqpJw/0?wx_fmt=png)

听风安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycicRSPJOu3U0ibcANsALhypGSOJURbEuKF7g5rJsWOuF8U8OWdHxicyYEYGiadgR9NnxsBBOZ8EHqpJw/0?wx_fmt=png)

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