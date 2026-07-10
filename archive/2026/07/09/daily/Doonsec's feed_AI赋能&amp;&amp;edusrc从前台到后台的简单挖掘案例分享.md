---
title: AI赋能&amp;&amp;edusrc从前台到后台的简单挖掘案例分享
url: https://mp.weixin.qq.com/s/mAYZO1XZfft-1xyYICbGSA
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:57:46.494910
---

# AI赋能&amp;&amp;edusrc从前台到后台的简单挖掘案例分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTYLzcywibDEBrEItdyl0Wq6oIvq5RSpS0WNRGAPeym4ycnntURicodWtXbd5ygGZknQAUJlH5Vwt1zicVspics86iaibYc0vTRCNtGo/0?wx_fmt=jpeg)

# AI赋能&&edusrc从前台到后台的简单挖掘案例分享

原创

陌笙
陌笙

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

前言

大多数人挖掘edusrc就是为了练练手，实战可以多测测企业src或者项目上收的漏洞，好为将来打好基础。

信息收集

本次也是资产测绘发现的ip站点，edu的话可以使用这个站点证明资产

https://www.ip138.com/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQUJhIXI6wy3h4tYYt1Muvy615FSaLmtw5klTsnpocIDc9trkJ2u193kCGP5Gm9iaujZvUm84bu2iaDichibvwMntx7WiawlpPBwHibw/640?wx_fmt=png&from=appmsg)

本次测试呢，依旧登录框起手

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQkIouTmQ7B2tmThxxKTIfbFCBzD6pkxnoBJp62eV5fQia7ncayIfV7lRqtWN6rbNtWRJiaZIvlibs1PniaxXXXSaK5QuJrbw9s03Q/640?wx_fmt=png&from=appmsg)

简单看一下,没啥图像验证码，正常打一打

按照自己的思路来就行，我一般按照思维导图，先测用户名枚举

admin1111111111111/123456

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQTsyy8C0GDGLe7cvy26icZibTsyNX8A86g6vNSC5ooPzUD0sADCmXMtA2h0iaAvwWJOlibezj9XOGAtwnAdfrugda76IdvjHYia9vI/640?wx_fmt=png&from=appmsg)

admin/123456

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT3M4mk1aE5V5U2vOx7SzZRgTSKG1oZibDTzytwGbEP2T6AqvgsU2ZshbticrXqGc81KJDXibibo7UrG4PBSYibbdows69HBrftmX5o/640?wx_fmt=png&from=appmsg)

用户如果不存在就是账号不存在，如果存在就是登录密码错误，用户名枚举，漏洞加一

在继续测一测这个有没有注入，万能密码啥的

admin'

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTNAdT08KuWnIA0UmRrn7XU8gC1OSsWT9JaicJyNUeCVWyQGPbw0JDYAmVOpkNcicXLSKI23kR5GbEOQ6kM5VD83pjQy2Fmf13Og/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSjf1EFuhrK3vfCicJiaarM7ibbx8FyETqAzribNKWUd6c1RtUULV9aEVFqq0wQke4AcZgQohW0gTgW6vPVLSPsXBa7dmTnH7z4ud8/640?wx_fmt=png&from=appmsg)

显然'是不解析的

直接看接口，雪瞳这里可以看到有很多接口，但是这个路由的格式一看就是vue

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQm8QsOpN3QYLldEwkeFmd3ib9DIr3qFu4djSrXwrbourS4moVzhFPqk0qF1VWN1MCeTh0h4AibspQ96VuTf7MGx41uEc6z2BS7w/640?wx_fmt=png&from=appmsg)

可以通过这个插件进行查看确定

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTq0h4UbQbg6Ny77ZUFB7dFr6Q1icwzp8fXHkM1uLpMyfAibJ5x3ZLjVpW365svCaibcZOZnpyPDCrZRRxCSrukOOdrLcr2ibIq9ib0/640?wx_fmt=png&from=appmsg)

之前也碰到过很多次了，未授权是很多的，点击打开测试一下路由，会马上重定向到首页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQreC9dmicaLtCywIKBTvPvaCZicnyRYn3VPtC0Nvd1L9CdfQDQ4WqPz4s5VvMFC5DALIS5p4V1qCK0MJbWm9P9RCruTzRhQmG98/640?wx_fmt=png&from=appmsg)

直接使用这个插件AntiDebugBreaker，清除跳转，路由守卫啥的就行，选完这三个选项，需要刷新，然后点击逐个测试路由即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTp5ibgxGSsI5MIaicZlNWagq89crlZfkfXecOvK4gFr73FPQNG5oIZ992lZO0BWle3WwajN0zQo51UrBTH1TpgDibGibKfe1ch0Hk/640?wx_fmt=png&from=appmsg)

点了几个页面，发现确实没什么东西

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRyKiamXMAf2k16qjaJpOuQjxECQaTYDLzehNctpdffthlzDldNUgvicZIbpibQibq535sZV5MGTWhH6GOYCRuQ8wedKAsxico9z2S4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFFia8LOYaM8WKJtWwSGj31CqYoT4vWXfia7cnJpCwoicrdSD9ds7ibTwTiaEvNES6ic21lqic2xry9NHA4HDgn1QJZmlJPztcatudL4/640?wx_fmt=png&from=appmsg)

添加上传啥的也不太行，经过一会的翻找，找到这个可以添加用户的页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQUiaLTnOSjibJRLiaq9jHPZUk74ic3zBibjZzcZtmcWzgvRL1fyKy8hn4UUeGK9bgOWgwFUZOkcicDj37tuvUsyeVianlmgEbYDSNUss/640?wx_fmt=png&from=appmsg)

页面本身，没啥作用，但是可以通过添加用户确认，密码的规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSOpRddDEsicklS8uzfwlmTmicZCJpic2gH9mR0WNGjtCcV5b20EcdGc2Cb1rkJe9Ho6aiabBgPa75L3geh9P3IHiay07Tg4VgFUJ0U/640?wx_fmt=png&from=appmsg)

使用常见的密码123456爆破常见用户应该不太好用了，但是有时候有例外，我们这里通过用户枚举确定用户admin存在

直接常见密码，top9000爆破一手，先不急

抓个登录的数据包，通过这个响应包能确定是shiro

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSezLgrugibhHFgxIoCZKSKJIJibqsTRXRCuDq3SwZCn8WpbXpvpmQxjtvrLLYHcb0ico0X3e5p12ayXrlYynhTCtCdRJK1cW80o0/640?wx_fmt=png&from=appmsg)

这个请求体也比较奇怪，一个参数多个值就行传送，既然还有QQ号，好在是明文传送

KEYDATA=qq31xxx6790fhadmin%2Cfh%2C123456

观察响应体的话可以尝试修改，true,和1，进行简单测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSibCicU2KtOokQSibNcOYjIYfsRtZCQt6chvC6ClloTm7Gmq2iboZwcQOGwV7W7wiaaIM67IeNdbZiaQ2HuOKOuVJicSLABhBuvIUhK8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQwzE41kgEj3tyDVPHYWvdvwKW5lyW1svWFTAo415cjjiahwjOLTuHrD2ibibLN2RDlscIhVBvGKErLQINPWJicIOicEQnNe2ZpJJgw/640?wx_fmt=png&from=appmsg)

进去一下，然后光速退出了，可以尝试丢丢，权限校验的数据报，但是没啥用

直接开爆，密码竟然是1，而且登录成功，会直接返回password的hash值，有点意思

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSSJYODOzhib2QSgsSrfNc1qqBmaQvmfpCY7QhiaGFVZD1zLgzoCDJeb2Fw8MSe798d1SXcBQf17eia06JwSt3gTqCtb5LJENtaLI/640?wx_fmt=png&from=appmsg)

直接进入后台，后台测试，要比前台简单的多的多，所以不要沉迷于登录口的对抗，简单打打，有就有，没有ai梭哈一下，跑就完了

没啥数据，但是看到我最爱的上传功能点了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT6rlFGURUMMvD0HMfLXYQ8z0RiagcjFGrqsS7IoYRQfYcnzHYcDMJVbEZQBdbbZHJeHjZ8Tbdjv9gFyOicVVnw3tOWuHiaPY6cQ8/640?wx_fmt=png&from=appmsg)

简单上传测试一下，直接传个图片，上传成功，没有路径

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSZFWYE6Dj05fDqPStZCPN2PNcyxbmUlA6ibicOsFpgChJKubHVxNIibfscMM2FnhreMdCepic2KFj2trw59O0VzdYr6dcDKFRwQmQ/640?wx_fmt=png&from=appmsg)

试试其他格式

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRicrgla6qxmicodswgM4Wo17ZMv1EY6NuMSMPAg9kzLtWgoLicQcArBn8bsvu33Mru7eRaQOykeoIYpIgIrbkMuLxnbrSzicpVLwU/640?wx_fmt=png&from=appmsg)

各种格式都能传，还以为要r了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSgogQ2Z7M8opBBMsw2kQDkGeSlAF5jumYM9x1qxPonkLk2onVTliboxWccicc8Cqt1F2d3yDgtdgOEQtjLX58mn5RZO4xicbTsia8/640?wx_fmt=png&from=appmsg)

结果不解析，点击下载继续测试，抓包可以看到这个filepath参数传递的还是路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboToG4BzLOBtuu9bDMoUm2NjoZDAXaTTjtIDBummLOKib3Ln4PWxlXjI6u8MxMOoc9IBWjQq9xth3yMfaKhgoyeic6foicvIJpVF48/640?wx_fmt=png&from=appmsg)

直接测一测任意文件读取

filePath=C:/windows/win.ini

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRMZ263osvibzDao8EEDlo0sHaicKX39WUFvDIwO7sibbYibT4ict1NuWZiaW8wdBhFlvpQHChQicexlSG1AULFz3JeIuLib8O3IvNZwe4/640?wx_fmt=png&from=appmsg)

漏洞存在

继续看看其他的点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTe6HfBT6CRN1qSpPbHwEpuMgRQDA92drfReb9QjMibicP8L93nM3cdFzfyU27CBS4dHW4jnIW2kdtYbIMeAIkOdAFvOxarPBjxo/640?wx_fmt=png&from=appmsg)

点击这个删除抓包，可以看到通过id传参，这里我们是管理员什么都能干，如果创建一个低权限用户，然后替换接口和参数，大概率能越权。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS6Fo3jZffn26UqvHDoe7FjBUiaq9dXCHLTwN3Jy1gT23yg1kiawKTSXUxzFZa5bPNibmsnfl2ISv7KTFmO9ia10LBfAr85LAGV7s4/640?wx_fmt=png&from=appmsg)

有这么多功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT6hWUwVXfUkVvKEyWyia4ZQ97wmqbNzNddaCfdCFmByMjcP6aJSElBicnZTpczzrZWZichKsglGI0J4R0icfgwicg3Hxd9KCUfXg6Y/640?wx_fmt=png&from=appmsg)

不在一个一个进行测试

逐个点击功能，让流量过burp,不要点击增加和删除，主要测试一下查询的sql注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSlfp4oRzZIE0B8Pkniaqk78KWtkrXTgzRh2ag6vW3QiaplaTma54vHK9v6icLbnx3TlrLJ9yIc5KIOWQgiaiaCsialvvhJx2z5pJI8Q/640?wx_fmt=png&from=appmsg)

插件大发神力，我们挑一个，看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQyVicrYcgRdX5pqsXtnR189rdwFryVVNQj4CtUud3qOfhiaAibJWLDOrAI14bbH5M0TTBsnBkuIEiaQbDASF5ia4FDZV2hibbLtNcac/640?wx_fmt=png&from=appmsg)

mysql数据库，而且这么明显的报错，有能力有兴趣的师傅，自己手动注入，但是目前这个时代，丢给ai了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRIassL9nchC1UtXCyDEAHtNlicW4AXbkPuA4UAcgItQ7K2suQ9QswTkERdsnYwwaBItEqouDvUicZw4lQEH5o4mULmQPJL8459g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRSNticEmBBvw7ooJd5iboNiaBnvqUd9mc9NNHSJQlF9HCZeWbQWqetp4IsHicqKBphWUevjAgzWjYhyV9tTYr2hYXdo4HrYAd0uxM/640?wx_fmt=png&from=appmsg)

拿这个poc手工测试一下，直接回显

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ123OPjq98faD2ufcMduG7B5MhM20PHJPAHibV1qVaVNnLIMMZe8mKpZ1RZW8nbw1iaVKicgjlc8O2nS19UEKxTc9B34mMNibt5dc/640?wx_fmt=png&from=appmsg)

查个用户，试试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTtgV6Zf4m3tibJHia08xD9T1ahd6cw7a6PHS0ukNAJRwvAiahicxtjxkzO0iavWfMK8rjlQGPbazWY4ibNZibbpdK1zB3ucEMGRwLMSE/640?wx_fmt=png&from=appmsg)

其他接口不在一一测试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQNjcz8eubmEN5Iu9kEJBZdvydsYeYpmAEsEZCFGicqGGibsmmjX7xy54jx8BMGibezypmNNY4TlWrmk5TAPj6MlXeGrLVK1ibPvhM/640?wx_fmt=png&from=appmsg)

提取后台所有接口，删除cookie，测测未授权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR4N7Ha6E5Iw7wQDlLicBbAKS1VaQwExnwldGe3DEhlmnsfOfkSEujAiaB2AiaZJ7Jtj75JO7UxNlKfAqJ1EVaMPNPUmr3YCdsPps/640?wx_fmt=png&fr...