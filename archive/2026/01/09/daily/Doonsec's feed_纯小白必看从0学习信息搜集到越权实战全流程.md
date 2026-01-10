---
title: 纯小白必看从0学习信息搜集到越权实战全流程
url: https://mp.weixin.qq.com/s/OgpywKMO5aYCBbg4zqF9rw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:38.084394
---

# 纯小白必看从0学习信息搜集到越权实战全流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcppXicpia8OchXcIa662BVib6lZNqicHwf01AqMnrNkaUlvzSLWFGEqW3icJLCDHQ5Vd8sogQTnbFPeMNQ/0?wx_fmt=jpeg)

# 纯小白必看从0学习信息搜集到越权实战全流程

原创

zkaq-腾风起

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

# 本文由掌控安全学院 - **腾风起** 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

## 0 前言

连着看了三天师傅们社区发的高质量文章，在充分吸收和整理到自己的笔记上之后，一方面有些手痒了，另一方面看到还有同学在社区求施舍金币，就想写一个还没有自己上手挖洞的纯小白，看完也能开始挖洞的文章，靠别人不如靠自己，我相信看完这个你会茅塞顿开，恨不得立马上手（大佬勿喷），等大家出洞之后再给我来点打赏。
随便找了个有证书的大学开挖。

## 1 信息搜集：

#### 1.1 找域名

在edusrc礼品中心这里随便找了个有证书的大学，直接百度搜某某大学，进他的官网get到他的域名（XXX.edu.cn），
这里以北大为例子，这就是他的域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6laX4OKqnpcG0bYbPbB0HaNkLd6tDAPSs6j4eJH9KMp8ldbZ2VaqqLjA/640?wx_fmt=png&from=appmsg)

#### 1.2 找ip

然后把域名放到多地ping，ping他的ip地址
多地ping链接：https://www.itdog.cn/ping/
还是以北大为例子吧，不打码效果更好一些

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6l0uMVhDUlq03tF6Q8s2vWQZ7SHSz2EV1x0FCnzIkMcCWZ5dibtyUv5rg/640?wx_fmt=png&from=appmsg)

拿到ip之后，我们到hunter测绘平台里面，搜集此ip的资产，依旧以北大为例。

#### 1.3 找资产

可以看到当子网掩码我们设置为/24的时候，只有74个资产
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lj15ibPoFL2juXTHgZ1odkt8H1wo5v9wIk1z6M42FYKhbH3TvAjkV95Q/640?wx_fmt=png&from=appmsg)
感觉有些少，我们可以设置为/23，/22，资产会变得很多，就很可能找到一些边缘资产，非常非常好测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6llFTJqPowQLz4mehox8AmDlfXHBxicwH6x9ibaia8FFah2LejOSWVIhv4A/640?wx_fmt=png&from=appmsg)

好我就这样找到了某大学的某管理平台，有一个登录框如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lLHeSyyIT1Ghcfias7eRpUXRic9xGLiblCYTic4bRFHmxe96CWQuP7EYdMw/640?wx_fmt=png&from=appmsg)

#### 1.4 浅测试看能否知道要搜集什么

我一般挖edu都是找到某系统，才开始学号、工号、电话号这方面的搜集。以这个某管理平台为例子，先弱口令随便试一试，密码很复杂，爆破的几率感觉不大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lnemV0EZEYnSqzgiaurZqdeoXkktGXj6zP1QMFhoXMFLbC9GQVLLO8ow/640?wx_fmt=png&from=appmsg)
但是他接着自己跳了下面这个页面，这时候就要考虑一下为啥会跳这个页面？是因为有admin这个账号嘛？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6liaYA6Ls6tc749aoNGJr6cdP1SiaH3ZVrg753Es11oUqdtPCXu6oHiaqhA/640?wx_fmt=png&from=appmsg)
我们返回登录框重新试一下一个肯定不会有的账号，看看会不会再跳这个修改密码的框，可以看到依旧跳了
这说明我们还是不能确定账号是否存在，再加上密码如此复杂，就没必要爆破浪费时间了。（验证码可重复利用，我试过了）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lqCtbkJsZjXf2h2gDglzKcoX6tZ55ojiasic8XIM4C1uHL8XrRfV9Fqwg/640?wx_fmt=png&from=appmsg)

接下来看看注册接口，诶知道了，要搜集学号和工号
这里我自己也注册了一个，注册之后说需要校方审核，所以我注册完之后就没再管（这里后面会提）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lDJWm7IT4Hf8Z3ch2BumZ4csz1LgrmrI9iah7ib0OxRqK1AqDvCynWBHw/640?wx_fmt=png&from=appmsg)
再看看密码找回接口，哦还需要手机号，那接下来开始搜集这些敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lSqazt41yiaFTqFAXAcSnIAQQ5dGGYSxxxtBFpeMiaxj3FI14ZhDeXrzg/640?wx_fmt=png&from=appmsg)

#### 1.5 Google搜集敏感信息

小白刚上手用这个就行，把括号里换成，学号，工号，手机号，手册，默认密码，你要打的系统的名字这些。慢慢翻会翻到很多

```
1. site:域名("想找的东西")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lTJ7Aicic44fgN6RRC7ZTI6QA4AmKicr8cctOzQmo0Etk1RibibFwpAd02rw/640?wx_fmt=png&from=appmsg)
身份证也可以试试，身份证一般都会 星星 处理一部分，如果登录默认密码是身份证后六位、后八位，可以搜集一下万一 星星 掉的是中间那些，后六位可以继续来用。
如: 身份证：38798720*\*\**11789X 姓名：翠花
这时候知道了翠花的身份证，就可以把想要的东西换成”翠花”
有很大概率就又找到了翠花的手机号和学号，那你就有很大的概率去登录成功。

#### 1.6 身份证搜集

我个人也没有特别好的办法，我一般喜欢去抖音，小红书等等搜某大学考研上岸，或者某大学高考录取通知书，或者四六级证书，很多学生都打码不严谨甚至不打码，你就可以搞到他们的身份证
如图：（码是我自己打的）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lARApXUs1GLfUqlADWBhzCTY3xib3kHUthCSibibEunrMGPq1LtibBakcJA/640?wx_fmt=png&from=appmsg)

还有这种渐变的，变得透明度百分百才打码（无效打码），趁他还没打码隐约能看到信息的时候搜集下来
我直接把下半部分全打了一点点打码有点麻烦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lUC55tc6FEPqkdSRlib83Ba1IUiaHric7r8hBPS7BmzafrEib9TMlgPFQfA/640?wx_fmt=png&from=appmsg)
还有需要你细心看的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lVbZtQce3ziaicHZMSOA5Olf3XiatcdqGYwNjOfMRC9I0nZxZJbEAaM6NA/640?wx_fmt=png&from=appmsg)
好了，差不多就说到这里叭，相信你肯定也想上手挖洞啦

## 2 漏洞挖掘（简单越权适合新手）

我这里通过搜我挖的这个系统的名字，找到了手册

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lmRfzdDK5aiaCEYksmWq9jaGibZAjL9tUiaWPN4lULD5wdIyNY37loKib7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lHE7uvOcSScD0mZwZgSzvQlKLyiaoaHQVvYzxukoXT9jsfjcqrice1NHA/640?wx_fmt=png&from=appmsg)

然后一点点看这个手册，有默认密码是啥，继续往下翻还有没打码的测试账号嘿嘿豪横

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lZA0TCfiaMtOLWBITNmA7f3bvBjdpKeIKdnaiazjYagvAEfjpCIBwERLA/640?wx_fmt=png&from=appmsg)

这里我自己注册了一个，能看到是待审核的状态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6l43cgmCNVE45vWSUMxFv0ThjCrlD40mnXuqzH9hqZ5H4Ubl3U28icZwQ/640?wx_fmt=png&from=appmsg)

看到熊猫头发现的接口不少，就bp跑了一下，没什么有价值的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lTwFVFt44Zgg7qPkBvqGEQQibSI7c0H6EsR0SW1AMriamy1ia8jhN4Via8w/640?wx_fmt=png&from=appmsg)
然后开始手工看js，有接口拼拼试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lFWiaqylHcSwjdHHFcRsJ8ETAYdb5piakncOzupN2ppryXnPdx913J3VA/640?wx_fmt=png&from=appmsg)
找到有个查询功能点，有数据返回，到这我就知道有东西了，可以看到八千多条

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lqw73A5YHwpibmSuldHlDiaicusRqqt4C1JzCnMRuhQbHKeUoWNcuWkC2Q/640?wx_fmt=png&from=appmsg)

开bp抓包，看看有没有其他信息，有id值返回，这里我找到了系统管理员的id值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6l3fuKX5ZWRHNIKaBAjW0jPQcHzr7m72wVpMdeiaLWJoCUaE3YBUyQrzw/640?wx_fmt=png&from=appmsg)
ok有删除功能点，不敢尝试（设计到删除的操作都一定要谨慎，谁也不知道里面有没有重要东西，就算是测试账号我也不敢乱删）
那就重新访问这个接口，有id值传入，修改为这个管理员的id值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lM6cguU5rhzOG4QWJib3XJIXBQBOYTcNFYUuK92SuwjkaTv525hP01Tg/640?wx_fmt=png&from=appmsg)
界面都不一样了，这就证明已经越权了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lYjibiagCKeZfGeYRjDns4J3ExrVWibrHmFWb2xKqe9mW8dPmzVvIhGyMw/640?wx_fmt=png&from=appmsg)

返回的数据也不一样了，再加上前面的，只要在访问接口的时候修改id值，可以实现近9千的任意用户越权看其数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6ltj6xWxOFh6ibrXKC7OYSjMbxSrxXxmia8ErqCdTibXmQxcPvBK0drGfFw/640?wx_fmt=png&from=appmsg)

删除不敢测，测添加，我自己注册的未审核的账号通过审核

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lc1mHMVvutwtoSFia9t1cTpv0BXA0smuibDwYcR5wPsTZE40YKOeJ26Cg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lYpP8rJU6cOB3IEgvXJmTxdkIZHaOSaiceY6QPOLw2rVymBdCfiaEJxKw/640?wx_fmt=png&from=appmsg)
其他接口一样，换成任何人id可以看任何人的数据，单是一个科研组的人的数据就九万多，这里提供一个截图证明其危害。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcppXicpia8OchXcIa662BVib6lk3W4Nqhpq5aicMmSnGvSFIcXZUGUfkFkIRRGe3vL1I7oxN5v0JiaUUaQ/640?wx_fmt=png&from=appmsg)

## 3 总结

此文极致详细，说实话这样写真的蛮浪费时间，因为我自身也是刚开始挖，这是我目前自己用的方法，在此分享出来，我能挖到，相信纯小白看完肯定也能从0到1，从1到n，希望师傅们指点，我当继续砥砺前行。

```
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

没看够~？欢迎关注！

分享本文到朋友圈，可以凭截图找老师领取

上千教程+工具+靶场账号哦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

 分享后扫码加我！

回顾往期内容

Xray挂机刷漏洞

零基础学黑客，该怎么学？

网络安全人员必考的几本证书！

文库｜内网神器cs4.0使用说明书

代码审计 | 这个CNVD证书拿的有点轻松

【精选】SRC快速入门+上分小秘籍+实战指南

## 代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！

![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=web...