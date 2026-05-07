---
title: 分享一次EDU实战，辗转突破登录口到达后台
url: https://mp.weixin.qq.com/s/PcSUlm665bDbDhHRRisZEg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:29:18.322245
---

# 分享一次EDU实战，辗转突破登录口到达后台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F4N4AId99Xc7QLFAib2lvrnGupdRZHV9ia2cLwOln8esMnkzJOIfsuhy1YmgsTeDk8XDO97pkIMRx5g3RcI6hYSczf6IWooGNhBJpcIctcGLk/0?wx_fmt=jpeg)

# 分享一次EDU实战，辗转突破登录口到达后台

原创

小帅安全
小帅安全

小帅安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责申明**

```
本公众号“小帅安全”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf2wibr0HBDdCyUKwjT9Z3dibaDKmVFGBEIw2OsfyK5n9aSbwr2YicOEwSNaXziaBiat4pZVp9czEkqbvZrBZSgtG6Dd1froYPbhWmw/640?wx_fmt=png&from=appmsg)

**点击蓝字 关注我们**

**1**

上来就是一个登录口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xc3QpoHialUhO4XFgFINzU1OXRnxuOVKPI0ricjqfhDbgtic8qJjlqLChdjfZJw2Y6kusb8mJiaVfuZd4hLQOc0M3sy9V57NUUtQJI/640?wx_fmt=png&from=appmsg)

这里可以证明存在一个用户名枚举

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XeuArk4qIq7cRSe9741IIWTMUFmQyNXhfDhyGUegnn7kfuWFmJM7wSYqIXCiczJRbicLXtiaVOIWgXKv7fib8wnJrlaMDzZ6dFZ88s/640?wx_fmt=png&from=appmsg)

我还没有这种邮箱账户的字典，于是挨个猜测，直到admin@admin.com

会提示密码错误

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdM5g3yeN750f425zdMMlGvhInXCK4IEJomQSIl68Hr5OQuSN9W6TIibSGyMzgScs9Fl79zSSk3cB4CSCUXicuz7uicB91JWwgkUM/640?wx_fmt=png&from=appmsg)

我这里尝试爆破了一下，但是没有结果。

那就尝试一下忘记密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XenGpegAJbou2NwBK8g4TwlsKXc4YOD4Ubic7rYunSxMNmSzxcIpFvxFtgiaEwcZZhu3aGajOWZvQDWyFGjRJK8wqjknB8732Tg8/640?wx_fmt=png&from=appmsg)

显示是发送成功了，但是我又收不到这个邮箱的验证码。

没招了。

那就尝试一下注册吧

结果它不让注册

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XeocF8hSuuda69KNw4REZCWV2IiaOqK5oPTDiboyPRmunsSzHczEfFDbIElYQ3l1LkiaUgq5ZibpjAjeKd3CMvl1unTHf8coLM7XR8/640?wx_fmt=png&from=appmsg)

根据弹窗的关键字，找到下面这一段代码，给他删掉，然后放包

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XficXMFj8HoJbVNYT7auhEOKF3Eew5vmdsTtEUpBlu4FtPMqxjUsRNCoFeJ7fqJjl0Ntiak4sLrJB8oflF1gC5RaxpnVLemWZrtE/640?wx_fmt=png&from=appmsg)

填好所有信息以后点击注册

它会提示验证码错误，验证码当然会错误，因为我根本没有发送验证码

这个验证码是我随便填写的，参数confirmCode就是验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XfN0ZwFlr8avPAfPibGzyWaAlW3BMGYIA0kNm1C8W9C2icUHRtVUPiaL7QG2BrHDh6MdZjtCmPxyg8UxFibakFWbvIqdOu3uE287CA/640?wx_fmt=png&from=appmsg)

并且

在前台输入手机号，一直提示手机号格式不对，即便是正确的格式。

然后我就找直接发送验证码的接口，构造请求包

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcebdxqhyDDFQRZ0yTQNRnaBLESmFfHib71lyn4SX3hv0Dazp6DIgSIVSH08d8wPk3Uc9jynS8wJH7kXHK5aGic7xic727HxhJWAI/640?wx_fmt=png&from=appmsg)

输入我自己的手机号，提示发送成功，但是我迟迟没有收到

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xd6oEz57PzYqetImjzsD9KbQvZvVcseaXDYZxxERtVOiapI5PbndhYgibPRymdrXJoxK705oCtWUdPk1b3MxDItmsFibPaZka9X4c/640?wx_fmt=png&from=appmsg)

后面直接修改手机号为12位、13位、14位这种乱七八糟的手机号，也都提示发送成功。

我就知道，后端根本就没有配置发送短信的服务，说不定连之前忘记密码处的发送邮箱的功能也没有配置。

之前注册用户的时候响应里面的result参数值是false

我想通过修改返回包达到注册用户的目的。

将false修改为true然后放包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XfZAW8cMQLlEdF9t15kPwogTywo59dv2PSuTcEgjI23NQgzx0mxibR5QESwHyxfaPmTfrGTVdEeGDMzv14e2he8D5ibcycDPuoBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcGr6Fvoc0llAq4zREjqAdMEboxdZGiar1Jsv6xUFkO4QuY7LCDLnzkQGshVsIg6s0syF4xKZWuz1Kic1Whn2R1PAFwyZ7khTWibs/640?wx_fmt=png&from=appmsg)

修改返回包以后跳转到了登录界面

我以为是注册成功了，赶忙输入邮箱和密码

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XduUxmcOtfPcFkhhPtxXZj2vvQibA0RO4EJLk8FuI9jOxGWLJPRWcQg7CTDzl86GQqrvp1VPnv1Auic1zf91xWkZibIKFfU3quJwc/640?wx_fmt=png&from=appmsg)

直接是提示用户不存在，根本就没有注册成功

到此，那注册用户的这条路是走不通了。

**2**

那还说啥呢，我累死了，不弄了，先躺会儿吧。

休息完了以后，我还是不太甘心，我都知道存在用户名枚举，并且还找出来了一个admin@admin.com但是就是得不到密码。

于是我就呆滞的在登录界面茫然的徘徊，不断的输入一些内容，点击登录，突然我眼睛一亮。

出现了一个不一样的东西。

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XfRHHaibfL3qUb9UGKtMfNX3bY87ic74pibsgyErJQrSA8VianVvgLVfmnfCaeT4iakuNKn8U2aEp45cRdNQdRiaIkrSrXrP3jtuyQ3U/640?wx_fmt=png&from=appmsg)

这个提示是密码错误，证明存在这个用户。那就按流程上弱口令字典跑一遍喽。

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XexYic7pkxWMb0mnorJAF2xFgEHB4eiaZl3ofFhQ2w6SsQX5zfOakTcwAjNY4uicFKhoYQUy471KmtUOS0IFoLkeOoeq4p5ztwGNU/640?wx_fmt=png&from=appmsg)

本来是没抱什么希望的，呆滞的盯着电脑屏幕的爆破进度，想着跑完关电脑休息。

结果，一个东西一闪而过，我赶忙排一下序。我去，出来了，爆出来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf1RDr1baa1y5goSeSCvMesMJMKgpA5Tic9hHw3sk29FjIG3bmBlHX4QuT2dM1Q92PR8MSteuyJmOZpZ1m2Wp2AjUDleiaKFDqnc/640?wx_fmt=png&from=appmsg)

**3**

总结

后面我意识到我缺少爆破邮箱的字典，所以去网上找了一个

https://gitee.com/molok/Blasting\_dictionary

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xel8AZl1dvLB35K3IpNEibFyLwP8KicoQWVbYoMJSKTHYA5qtK1rWUUDj1skRIMlkjGia5rwPcIaOWM6PHxZFe4LqHXbiaaKiaaldTI/640?wx_fmt=png&from=appmsg)

我在这个字典里面搜了一下，是有我爆出来的这个的，不过就是这个字典太大了30w+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XdyC6ONDE7GAYpvk1aPDlHd4T9YR9QCSVFV9XCoEZzFmfX8g5ibiaALhWWLicjicU5QiakCM5cnzfGKicp2wuIWBwK0GG7oJqwJrWEpo/640?wx_fmt=png&from=appmsg)

我还想爆破其他的用户来着，但是这个字典太大了，不能直接用。后面再找找有没有那种特殊的测试邮箱的字典。

大家如果有好用的字典欢迎推荐。

已经到这了，前面不是爆破出来一个123@qq.com很自然可以想到试一下1@qq.com、12@qq.com这些邮箱，过程和上面一样，结果显示存在1@qq.com、1234@qq.com、123456@qq.com、12345678@qq.com、123456789@qq.com这些用户，然后再去爆破这些用户的密码。不过都没有爆出来。

后续就是证明危害了，没啥好说的进去以后把所有接口都看看，证明能干什么

后面再试一下能不能爆出admin的密码。

文章中提及漏洞已提交漏洞平台并已修复，请勿恶意复现

获取更多工具和实战技巧

关注 小帅安全

**往期推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XeqrffLgRnnnh9ImV3J4pZWGrKIIFXia91nm5ibNynsoJHBgxiaGlgPWk2uXDJRZQDicVH2icjHo2rCIQ2DN7raadjIEd1DIM2slicGM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483962&idx=1&sn=ea2a00b7fa821b99422e4d893ff43cab&scene=21#wechat_redirect)

用户名/昵称内容注入漏洞

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcPAHeE5c9M5ZC1tUJ61B8W4HrbfCh3nRmfPJKNPicLbaABsbCbJKFI3n9GeDp89ap3a4wiamLnuSibzLXxU9aQcvYdC7NqOsVkQU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483947&idx=1&sn=5968556dc7169ee862c3842981a3a198&scene=21#wechat_redirect)

最近捡漏的一个验证码相关的实战案例分享

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xd7kwlLwpEbUGYjxibDp2xxTrOuEZQSnenPiaBSd4olCXOGlAxfFXCq1V2nnN7o3KX2akAQ4qqUhrpA5Jib4hwvzImf3gWS6WzPCI/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483882&idx=1&sn=c3203a266955b29770706abc96f5e816&scene=21#wechat_redirect)

微信小程序反编译工具推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XeK30SvVGbo4Szt9kdUTHetDzK2icFnHFmYAjRbcS4F9EPZCibjJc88Q5kATIvFHzmpo0mdQ3AuS41fN8a8xqG3DHVnIR8YQBtI8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483745&idx=1&sn=210b474b3666c4b90564400c388ad46a&scene=21#wechat_redirect)

EDU挖到的简单满分漏洞之Vue框架实战加资产收集语法

如果文章对你有帮助，欢迎一键三连，点赞，关注加转发，后续我会更新更多优质文章。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/F4N4AId99XdIraiaSOaLDHfOvSqX3xia3zqIlbzVgibKZ4kxLiaVhxE55qKo61MM0wfkpobTd6N6l0ibcbCOKic27I7ELabB8PsxPWsN14o7FsJPg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/F4N4AId99Xf09ZC9xkJsEquQCRDf4BG7z1mdACUO9r5CLbPDOkGFqUgetyB3BbTamwRpGicHXm0CibYhQOEq6R3GwGj0H0YR7cFCAiacXIJA9w/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/F4N4AId99XcQUYQ67ITwEyEnKeSgtiaia6JfdO6jZiaW6uK4Gj15xicyqlSQNh5ao93lSFknaaf4sAebJ9qoibuicEToq9YVj8eY28vKrtu3TObXQ/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd9Nbt3OIoHdW8397TLDEpw56RIGjuvl0yibyiaF509zluBKQnk8pFFa7WiaAEebAyEvyibicu7ddTIkcMWtvODFZJuAbo4HQrOticAw/0?wx_fmt=png)

小帅安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd9Nbt3OIoHdW8397TLDEpw56RIGjuvl0yibyiaF509zluBKQnk8pFFa7WiaAEebAyEvyibicu7ddTIkcMWtvODFZJuAbo4HQrOticAw/0?wx_fmt=png)

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