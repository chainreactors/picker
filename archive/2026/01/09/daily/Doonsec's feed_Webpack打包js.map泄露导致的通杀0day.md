---
title: Webpack打包js.map泄露导致的通杀0day
url: https://mp.weixin.qq.com/s/G8_DI-HJqe8GuB0zTLDnGg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:25.696919
---

# Webpack打包js.map泄露导致的通杀0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5qwmLSZVvicJvyvf2DMnUZtONovR9Cyh8X9KD9NJU9gwibpTtI8ogpngg/0?wx_fmt=jpeg)

# Webpack打包js.map泄露导致的通杀0day

猎洞时刻

赤弋安全团队

![]()

在小说阅读器中沉浸阅读

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn6mG6TyJornrhz9JticBo3Nx4zhzUFXcggEDw1lkfzMI0KuLp7dW4dDCvbfgAKlLSX3yGmYg0gtXcw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
本公众号“猎洞时刻”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知
```

本次分享一个js.map泄露造成的高危0day，设计站点近千，不喜勿喷，感谢观看！

开局一个经典的登录口，直接进行登录口对抗。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5BsmjaicNVz3ibShPvNnaj5223IJY743MBSG9e74B8SO3OWTu3SMiaJeGA/640?wx_fmt=png&from=appmsg)

常规对抗登录口方法如下内容，都可以测试一下。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5naH2icnSFUUeVzUJq2ic7bLwiaQ2W35k43F3QticMriatiblBW5DFDvVcbKg/640?wx_fmt=png&from=appmsg)

如果上面方法都干不动，更加建议你去多审计js，说不定有意外之喜。

直接F12查看js，发现存在一个文件，这个算是一个Webpack打包的特征。

app.xxx.js 这个文件算是一个webpack打包的特征文件。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda50CWuzZJAXZkibTERr1ok21sibOticQn3GQ4SWq4UkicmatdC2nWXic3Xr4Q/640?wx_fmt=png&from=appmsg)

并且在浏览器插件，也是能够很明显看出来，确实是webpack打包的站点。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5QnoVtfBdhGu0pfd5v4F5dzprXs52WibtT6MwUibMk0OTXsQMDbODL98g/640?wx_fmt=png&from=appmsg)

于是直接访问这个app.b0aaa943.js文件

**访问后是下面这样。**

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda54BepqFibkFEvp9d49S9Bqwdh3pDWia3meS7IRJwibcHibg4lfaY1EPMK7g/640?wx_fmt=png&from=appmsg)

**然后进行拼接.map后缀。**

app.b0aaa943.js

拼接后

app.b0aaa943.js.map

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5GdRP0tKbRic0wVZJ0W5ibjrxLQsRdA4htWrDgyzcXpDZ25BVWKMEHkDw/640?wx_fmt=png&from=appmsg)

**于是就可以成功下载js.map文件**

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5nHgfRjjPibMQ1F239qlDstB3T6r0ialnIs6nzUsMI0Cp5hcq9XwRicbIA/640?wx_fmt=png&from=appmsg)

进行对js.map反编译还原，如果没有反编译环境，网上搜一下安装一下。

reverse-sourcemap --output-dir ./  app.b0aaa943.js.map

**一、信息泄露已登录学生token**

还原后可以成功看到打包前源码，里面泄露了各种各样的接口信息。

于是可以对接口进行审计，然后测试有没有未授权接口。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5OKBVP24X0jDtozSJVTQtXyHcCT9bJDuQjrlr9s3L9jpJAqskSWNJtg/640?wx_fmt=png&from=appmsg)

然后我们查看

http://xxxxx/api/Monitor/GetActiveUsers

这个api网页是登录的日志，只要有人登录成功就会泄露其信息，可以发现暴露了一些敏感内容。比如有用户名和密码暴露，还有登录成功的token值。

在下面内容，可以找到可以使用的用户token。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5UjZbdUMoLPQaUR9pmEtic8ruDkOrHexGqJNBH5c47AibaVkvkdwCkpnQ/640?wx_fmt=png&from=appmsg)

**二、拿到任意学生的账号密码**

于是我们根据api给的内容，我们获取到了一个学生的登录token，使用另一个接口，于是构造路径：

http://xxxxx/api/user/getinfobytoken/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiMjAyMzE1MTAwMTM1IiwianRpIjoiMTUwNDM3IiwiaHR0cDovL

通过该接口，成功返回该学生姓名，手机号，学号，以及md5的密码值。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5zenQtEwLRBP1GfvdqNFWOlYjUMShOqfd9eBSCH0icphkjQkN0qspymg/640?wx_fmt=png&from=appmsg)

然后对MD5密码值进行解密，比如密码123456.有了学号和密码，就能够使用登录接口进行测试，发现获取登录token成功！

再使用第三个接口，验证账号密码是否可以利用，经过测试可以成功返回该用户的JWT值，也就是证明账号密码可以使用(低权限账户没法直接登录管理后台，通过该接口也验证账号密码是否成功)。

http://xxxx/api/login/jwttoken3.0/?name=202315xxxx&pass=123456

下面是成功证明，该账号密码正确，并且可以拿到JWT

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5hSj2knGwjPVCl9Cw6ptovrFwCicyciaqgzyb8enqRlCWnnx6wCZBVWIA/640?wx_fmt=png&from=appmsg)

**小总结：**

因此，使用上面的方法，可以先通过

/api/Monitor/GetActiveUsers

接口，拿到学生泄露的token，再通过学生泄露的token去调用/api/user/getinfobytoken 接口，是可以拿到该学生的密码MD5，进行解密后，可以成功拿到多个学生的账号密码。

但是直接进行登录，会提示无权限，因为这是管理后台，学生登录是无权限的。必须要拿到admin的泄露密码才行。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5bFMDLBUxvJWichV6dG49umqd7C6786Q2cRSMeT45UynheNtomE6Bxbg/640?wx_fmt=png&from=appmsg)

**三、登录管理后台**

刚才上面那个，因为只泄露的学生的，所以没法登录后台，但是这个是通杀漏洞，试试其他站点，有没有泄露admin的信息的。

**通过进行指纹提取，发现有九百多条。**

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5bS49U1JKcKyIehoicbT9riawAZ7r3CHJSu51YCqXjDOUDd24jC6G53tA/640?wx_fmt=png&from=appmsg)

如果不会指纹提取的，看我下面这个文章，点击就能查看：

[如何在日常渗透中实现通杀漏洞挖掘](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247487436&idx=1&sn=be143102d776f443d8512a4f3d8684c6&scene=21#wechat_redirect)

然后找一个其他站点，还使用上面的方法，先访问下面接口获取泄露的信息。

api/Monitor/GetActiveUsers

成功找到了一个泄露admin账号的信息泄露，并且还泄露了token。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5GibCwticdAflAdRl93DAHLjObAhuYxvtcF0PkJS4yuibKGUm0IDaQqfzA/640?wx_fmt=png&from=appmsg)

其实拿到了token就已经可以登录后台的，但是为了危害扩大，继续去拿账号密码，访问

/api/user/getinfobytoken/?token=xxx

成功拿到admin的密码的MD5，进行解密成功拿到明文密码。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5uLpfFv3o4z778QruNtJoWAUjbzOTkAKMNiaIB1WPomfQma9Xqbpiczkg/640?wx_fmt=png&from=appmsg)

通过CMD5可以成功查到，直接动用我们团队内部API去拿该明文，或者你花钱买个VIP也行。

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5oJiaqdzGWkooNyjPQ1ut0I8mb0Y3UdCf586GRo8ibQ4icTfEAEHhwic7OA/640?wx_fmt=png&from=appmsg)

**通过账号密码，成功登录后台。**

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Lbe9KICSQuvwicibXsrfda5bCE4tEibVCV9GiaEYGiaRkQ4uiasY5rqn1jPRywboTgRhkHCoE1xUPSeeQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Tb6OwBlojEicRyZT8n81n70HIFAaVPfaGp7SicSOyTQXAYUCfiaQvR8kqEo2x5KNo9dINkCR9W2ibibKSnbRchwItyg/0?wx_fmt=png)

赤弋安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Tb6OwBlojEicRyZT8n81n70HIFAaVPfaGp7SicSOyTQXAYUCfiaQvR8kqEo2x5KNo9dINkCR9W2ibibKSnbRchwItyg/0?wx_fmt=png)

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