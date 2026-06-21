---
title: 渗透测试实战中url跳转漏洞
url: https://mp.weixin.qq.com/s/XvT5NiH_KapaYRpGlQEjlA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:35.148536
---

# 渗透测试实战中url跳转漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboT6MZFON3mSODevhSMibOc4pIeKX1KszibKXXJ2GkGm1gPsyMn74vyRUz1o8rd9ldHdWJhFLwmAquEW5QhCyVyjhVwPrkv27BQu8/0?wx_fmt=jpeg)

# 渗透测试实战中url跳转漏洞

小猪佩琪
小猪佩琪

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
作者:小猪佩琪原文链接:https://xz.aliyun.com/news/4821
```

# 前言

最近在一些厂商项目中开始接触到一些url任意重定向，虽然是低危，奖金较低，（虽然国外已经是几百$）但是一旦找到突破点，几乎整个站的url跳转都可以bypass，一个厂商所有点的url跳转加起来奖金也比较可观，所以将自己挖掘过程中一点点心得分享一下。

# 简介

先走个流程说些废话，url重定向漏洞也称url任意跳转漏洞，网站信任了用户的输入导致恶意攻击，url重定向主要用来钓鱼，比如url跳转中最常见的跳转在登陆口，支付口，也就是一旦登陆将会跳转任意自己构造的网站，如果设置成自己的url则会造成钓鱼，浅析危害。

```
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><form method="get" action="url.php"><br><br><br><br>username:<input type="text" name="username"><br><br>password:<input type="text" name="password"><input type="submit" value="登陆" name="password"></form><?php$url=$_GET['redict'];echo $_GET['username'];if ($_GET['username']&&$_GET['password']) {    header("Location:$url");exit;}?>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS7BScvCDAC5JuFSOJ31yFCdTurH7VuIZfN42pq0HzVDVyO0kOJRrxL7TE4ic2rRI0QQtuM1iaEnAfte4ITbyZHP2wTGvKjHN1tM/640?wx_fmt=png&from=appmsg)

最简单的代码实例，也是很贴近真实渗透的案例，登陆跳转，后面通常是加上自己业务的url，一旦存在url任意重定向，发送给用户，会毫不疑问的输入账号密码登陆，然后跳转到我们想要他跳转的url，比如：

我们发送给用户这样的url，

```
http://127.0.0.1/url.php?username=&password=&redict=http://127.0.0.1/fish.php
```

用户正常输入账号密码登陆点击登陆。跳转到构造的页面。(我可真是个钓鱼鬼才)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQkVlcr4CoN15pwGAV9HWjKulOmJQHoWUFiaJrgO59Qf5azlLhchNE0DqqYdZjJ7MMuefYr96klTJD32jEuay22uibxWic1dAoUj8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT7WFCyria58LnvibT6Lk110kEoTVPcweQyWbnWTcmZzOas4T00sKd8ialiawl3nSG1xKIEibzLIqN6B9fDBdOKDFYNU6xukDticRCfs/640?wx_fmt=png&from=appmsg)

当然钓鱼界面可以伪造一切你想获取的信息。

# bypass

其实bypass没什么新的套路(我暂时没)，都是网上有的，师傅们可以百度到的，我整理一下，利用上面的代码简单测试，都是本地测试通过的。www.xiaozhupeiqi.com是服务器要求跳转的url。

1.最常用的一条：@绕过。

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.xiaozhupeiqi.com@www.baidu.com //ssrf也可用
```

2.绕过一些匹配特定字符。

？绕过

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.baidu.com?www.xiaozhupeiqi.com
```

#绕过

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.baidu.com#www.xiaozhupeiqi.com
```

3.斜杠/绕过

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.baidu.com/www.xiaozhupeiqi.com
```

或者反斜线

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.baidu.com\www.xiaozhupeiqi.com
```

4.白名单匹配绕过

```
比如匹配规则是必须跳转，xiaozhupeiqi.com 域名下，?#等都不行的时候，如果匹配规则为xiaozhupeiqi.com，可以尝试百度inurl:xiaozhupeiqi.com的域名，比如aaaxiaozhupeiqi.com，这样同样可以绕过。接下来实战中会用到，
```

5.xip.io绕过

```
http://127.0.0.1/url.php?username=1&password=1&password=1&redict=http://www.xiaozhupeiqi.com.220.181.57.217.xip.io
```

6.理想化方法

```
如果有机会在自己的页面设置url跳转，比如目标网站的bbs论坛自己的资料页面设置url跳转，既然是服务器的网站，那么url是不会限制的，可以用一个漏洞去构造另一个漏洞。
```

7.白名单网站可信

```
如果url跳转点信任百度url，google url或者其他，则可以多次跳转达到自己的恶意界面。
```

8.协议绕过

```
http与https协议转换尝试，或者省略http://127.0.0.1/url.php?username=1&password=1&password=1&redict=//www.xiaozhupeiqi.com@www.baidu.comhttp://127.0.0.1/url.php?username=1&password=1&password=1&redict=////www.xiaozhupeiqi.com@www.baidu.com//多斜线
```

9.xss跳转

```
这种就没啥说的了，就是XSS造成的跳转，下面也有案例，在有些情况下XSS只能造成跳转的危害。  <meta  content="1;url=http://www.baidu.com" http-equiv="refresh">
```

# fuzz几个参数

```
redirecturlredirectUrlcallbackreturn_urltoUrlReturnUrlfromUrlredUrlrequestredirect_toredirect_urljumpjump_totargettogotolinklinktodomainoauth_callback
```

# 实战几个案例

1.最常见的登陆跳转

登陆跳转我认为是最常见的跳转类型，几乎百分之七八十网站都会url里设置跳转，所以在登陆的时候建议多观察url参数，通常都会存在跳转至于存不存在漏洞需要自己测试。

上面的类型四,

漏洞url ：

```
https://xx.xxx.com/User/Login?redirect=http://xxx.com/
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQCjCNMbrW640gavotBkG4YvBdMQ3IUjm6libdQKgEx4L2nMp1alKiagak6OIse0TViapNM4XAngxFiaHeueBR53E0AMpq0K0gicDzI/640?wx_fmt=png&from=appmsg)

为登陆页面，如果登陆成功那么跳转http://xxx.com/，但是所有方式都无法绕过，但是发现可以跳转aaxxx.com，也就是匹配规则为必须为xxx.com的网址，但是aaxxx.com同样也可以。

方法：

百度 inurl:xxx.com，即可百度到很多域名包含xxx.com的url，即可实现跳转,不小心百度到一个黄域，正好证明危害登陆跳XX网。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQFSd8qY7D6UDJH8H2L6NDWKBNNehYb3MXOicoNNPJ9q5lzC8pBLwnDYluBF5ZO5XRe5GBBRia7CTk1pWhzVLkfX7OFWyibTPNm2M/640?wx_fmt=png&from=appmsg)

还有一些花里胡哨的base64加码了的跳转，解码就是需要跳转的url,其实本质都一样，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSDiacib6knNqFpyoKnqpsm8ZmpazqhOxSaQs5EWTb0IiaNK07HeLQzibvIZhfhG8EV8tZGOXFpIzBeeDX5uVuf0H2QLztdl2RYEkw/640?wx_fmt=png&from=appmsg)

2.@绕过

@是最常见的一种绕过。

漏洞url

```
https://xx.xxx.com/user/goToLogin?toUrl=https://xx.xxx.com@www.baidu.com
```

这种跳转在chrome浏览器可以直接跳转，但是在火狐会弹框询问，但是并不影响它的危害。

火狐下@的跳转。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSibOlufPnOYqClbILiaPpVkTiabPSsmvcTmEkj1zAYM1PnicOJuHuo2OPfmqBk2AicicZHK7lalYDseib1hzibJiaqhFoIMWCvdDpMzKm4/640?wx_fmt=png&from=appmsg)

还有一些是跳转目录的，

如：

```
https://xx.xxx.com.cn/?redirect=/user/info.php
```

修改为

```
https://xx.xxx.com.cn/?redirect=@www.baidu.com
```

这种情况通常@也可以跳转，大胆的去尝试

3.充值接口跳转

通常充值接口都会进行跳转，如充值成功会跳转到充值前访问的页面，因为充值接口需要充值才能知道到底存不存在漏洞，所以测试的人相对少一些，大胆去尝试，单车变摩托，充值完成后还可以提现其实并不影响，不嫌麻烦就多测测。这些都是跳转成功的案例。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQIdf4uSCZb8qoZcBaqLqibMusX0QgxTm0LsBqCLpII2414aDGQj3UpNoupfFuuDrl65zMg17BUaicPsPhww1o9FApoicl27ibK1xQ/640?wx_fmt=png&from=appmsg)

4.xss造成的url跳转

在一次渗透测试中，碰到一个站点，对<>"这些字符都是进行了过滤。且没有其他姿势配合，基本上告别了XSS等漏洞。如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQQBAgZ4s5yI1kld8E45D8xC9bvnGPLxuicFv4KQaUKLuASNIjB3UWUYDKOUniavhv6v3NgCYcBNlpOAia5pbSrR3ZgwqGLJyia58I/640?wx_fmt=png&from=appmsg)

可以发现我输入了xsstest<>"，但是<>被直接删除过滤掉了，但是发现双引号还在，先看下源码是怎么处理的。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTuLPxD88Dkk5oKyiaoia6BSYtF0HgL7tX4erpFarlg4wWOOJ3Q01Zzb4vfsCmicOaJH8xlhQbwuNwWYLa8CZ6PnBHLt3PiafSKyq8/640?wx_fmt=png&from=appmsg)

乍一看双引号也被转义了，输入的xsstest 搜索有十七处，大部分被实体化了，还有一部分双引号被url编码了，但是此时突然发现我箭头指的一处并未对双引号进行转义或者过滤，虽然<>已经完全被过滤掉了。

此时构造meta的url跳转。

payload：

```
http://xxx.com/search?w=1;url=http://www.baidu.com" http-equiv="refresh&fsearch=yes
```

其中输入

```
1;url=http://www.baidu.com" http-equiv="refresh
```

最终闭合掉得到的源码为。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSNZ1Htu8Xic2ibjhkQwQib6ILru45nnuZTnGYvb3o01zHM61Y4iaYiaHeKf5GiaAXuNMknb9FH4HtP4YUicxFfavgAVUg18kzduN0rrM/640?wx_fmt=png&from=appmsg)

最终点击payload会跳转百度页面，其实这个严格意义上来说算XSS造成的跳转，构造应该也可以XSS。

5.业务完成后跳转

这可以归结为一类跳转，比如修改密码，修改完成后跳转登陆页面，绑定银行卡，绑定成功后返回银行卡充值等页面，或者说给定一个链接办理VIP，但是你需要认证身份才能访问这个业务，这个时候通常会给定一个链接，认证之后跳转到刚刚要办理VIP的页面。

通常这个点都会存在跳转至于存不存在任意跳转，师傅们自测,有些跳转业务不好码就不发了。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQMYhMENR1zmfTCO5ia1kHGOZsK2FKbqh2btJbksps6YcFk7YibrdqRDMiau352ho3BrWtSj54zsBQJFBBRO3tiatFmhDmQeTOADlI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSGUBfEPERIhRibnKZkcAIyicdRHXASDiceGhbKAHRvoYxLS4LybKQIFvhZ08459G9fvSz0LHWibowoIFM5BOC0a0UqCwoWibbKo5sM/640?wx_fmt=png&from=appmsg)

6.用户交互

在一些用户交互页面也会出现跳转，如请填写对客服评价，评价成功跳转主页，填写问卷，等等业务，注意观察url。

问卷调查提交跳转。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT5HA2ibJmQibdGWodQaZWt7glrESRMI1EDsBf1sOtySJu6qhKsKJFOBxuKzUric0rqOS3oCbpa3icRejF3vmkjicBaYiabEma5uAxK4/640?wx_fmt=png&from=appmsg)

7.漏洞构造漏洞

一次渗透测试中碰到一个任意文件上传漏洞，但是不幸的是没办法解析任何后端语言，没办法进一步利用，只能前端造成一点危害，但是存放文件的服务器一般比较偏远，此时可以利用我们任意文件上传的html，然后来进一步利用，绕过本来无法绕过的url跳转漏洞。因为存放文件的域名肯定是符合网站跳转范围。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTYNf63XGvAR5IhaOedcMtKxB2ROQicFs8QhE2ZODicsqPtxRNcibAvuSxGiboHCCLGoBYYKWhGyX9hhj0C0xfaoQaW2LLejmBZI1w/640?wx_fmt=png&from=appmsg)

最终构成url跳转漏洞，当然可以获取cookie造成更多的危害，本文仅讨论url跳转。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt...