---
title: 记一次ASP站渗透测试经历
url: https://mp.weixin.qq.com/s/vAcUKyEYYn-lFFONAk7Ziw
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:26.344207
---

# 记一次ASP站渗透测试经历

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRqDXvKaEibgXKcOHy3YO2CiaJWIoVMLZIFunZndEVV4pRZaNNMnDNznvOTXeP4QzeRLT5A2PAuQ4oWPz69MrQ7wPKgadOlz9Or0/0?wx_fmt=jpeg)

# 记一次ASP站渗透测试经历

1575265746823585
1575265746823585

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
作者:1575265746823585原文链接:https://xz.aliyun.com/news/91174
```

## 0x 01 前言

在日常渗透测试中，总感觉ASP站打起来比较吃力，通常一些比较旧的站都使用`ASP.NET WebForms`这种类似桌面开发的框架来写Web程序。这类站点在登录界面甚至整个站点都很难见到一些JS文件，也就少了很多测试接口的机会。在没有口令登录的情况下，大大增加了渗透测试的难度。故记录一下一次打穿某ASP站点过程。

## 0x 02 渗透过程

起手是某学校教务系统的后台，观察路径为`/Login`，一般路径是大写字母打头的路径都是ASP站点居多，或者可使用`Wappalyzer`识别一下。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT0Pvia5GnnibJxJCmElRWSrGJw4homVLYgUo07pWXIjfooeKB9icLQJ1B541XGpfL9anAP8E4Advq4qOdxKKR4g4ayc5kfibN8Zbc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQSicj2UoibicUic4oYvp4dFcSaWfGF9kt1MEUUEFwLGYrOU1YicL0c4IoWzDhgj2QiaVsx1M6MMk7XU4ibN8GGUtyZW5V9qjloq9W54k/640?wx_fmt=png&from=appmsg)

简单尝试了弱口令登录，但由于存在验证码限制，只能手工测试了几个常见口令，最终也未能成功登录。没有弱口令，没有JS文件，只能开扫目录，还好没有WAF拦截。

这一扫，还真扫出东西了，/dev目录没删，一看就是开发老哥调试的接口。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSwD7gzQ8MoYbhMRqe7tLicgqAULPDLnlRB21Esqa62jicCA7udLWzmwuJ9XoD7hR2I8lHF6a6R1sAUlLVchkK1y8pRRPOAhq4Ls/640?wx_fmt=png&from=appmsg)

访问/dev，一看我去这不数据库账号密码吗，赶紧扫一下端口，看看数据库有没有开端口到外网。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRjWPATWJcEX0aQZqjwjqZKTAEImC7icY3tebY8ibwcrlJOdicXcctuLFm7USrWk3aASY435hJjWVXjAicqFqoJZqftLORYSRMbSNw/640?wx_fmt=png&from=appmsg)

简单使用 Goby 进行扫描，发现目标存在 MSSQL 数据库服务，思路逐渐清晰，随即尝试直接连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTBG9bM71zT6GYNT3sM1nicWaibyFvz4SKAx2icHcgfPRLbA1EAXfwTr4j7YNHlregeNrwHxq32ug2Z54db7UxVOUxDRExPWetSj4/640?wx_fmt=png&from=appmsg)

Navicat启动，发现存在大量师生信息，可惜没有身份证，只有学号、手机号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ73q6qO03UGP94rfb8kFdF7teStyPaXRK6X4Ujcibthd6WLlgDOoiah09ANYs563tOa2RKzgbCBub4alsicETPU8PwgtHspKsS1s/640?wx_fmt=png&from=appmsg)

虽然有系统后台账号和密码哈希，但是密码哈希是加盐的，也不好直接爆破。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboROB5syGxianiavibethkuV7a0icXlZmHA4tArbBDAJ4DtxYd0AAr9Mxa3lmI2HIdmibU9l8InIuomMcLwTxRnvgN5icVBpz1icZMdpAI/640?wx_fmt=png&from=appmsg)

回头看看开发老哥还给我留了一手大惊喜，居然有admin账号直接能重置密码，而且重置完密码是多少告诉我了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRDWzozHrGViaNGficicDuUwqzvxdXRsyu5QcBc7Rl6wvEy7utdsEYGLia8wKevohTt3nVCVStdMfovEpP5alU1eHR6YYrOic1bMB3c/640?wx_fmt=png&from=appmsg)

重置完，admin/admin成功进入后台管理员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQJZ0IIaHduCEicfia5EUaIf4VdHtVvouibBhV0kvqnHI4Y3NxChWFO5ZrlxR7DeSKIW1xpk8H6fibiavkD0RQHZXeh2EcyNciaRthfk/640?wx_fmt=png&from=appmsg)

随便点点查看一下功能点，发现学生管理地方可以上传头像

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSXkBXiay3dokfGvoZgLDICldQd5wbUvm3Eq7buC1uhRoNvWA3QJayPyoibY5EZ0iclL5jFgoGgGNGH16CnxKENmReVkz9tfwkQKg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRlmtk2uoE6tZqV0LicXqbH4rZyEiaxticZlekVlveHyQVx1jGcPJBN7X4r3zsI9lLg3dALs19bibrEFtQMLe0KYqEjfDq4FdXOcpg/640?wx_fmt=png&from=appmsg)

直接上传asp文件，显示上传文件不合规，先上传正常文件，再抓包修改后缀名，都是一些常见的思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQibTBicsPLy80Wem7KIg24liaicYS2qtKZAuj0oKrJrVxKXalnYTKz42TXCYCUXg5oVOEbQ3XiawMrnQ7O9bibLYE29PdA4EtMjYibqA/640?wx_fmt=png&from=appmsg)

抓包上传后，显示未找到路径，也是十分奇怪，传png文件也是无法找到路路径，但是访问路径

/Files/Student/1/2025122812201752676661.aspx确实是传上去了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSw1uLDPXm3KWts3tA7HGicze0YGK66a4uH1IT8iaHsW6Be7uwSIT6Fz1XpTrr8zr7PbxjWd6JN7fK33JRkvtaJzwmcibq3W1HWw8/640?wx_fmt=png&from=appmsg)

直接antSword启动连接，上马成功，点到为止，也没有进行查看服务器其他东西。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTgNuJkgOr7MibtJNgBYpfulNjPcmlia5YEBUicDSlwQ1INhdKucAQSh7Jgf3Yrq5ib2OW86I3cjAPUQ6zahdQ6ROTm5tS9hRnJ6BM/640?wx_fmt=png&from=appmsg)

资产测绘上搜索了一下，发现是一个通用的CMS，而且这个开发接口也有很多系统没有删除，想到这种ASP.NET WebForms站点比较旧，后台有SQL注入的概率估计比较高。依旧是代理开起来抓包，后台除了删除和添加数据的功能点都点一点，保证参数都能抓到，再一个个包简单测试一下。

也是十分幸运，/Grade/Report接口下的参数ctl00%24cphMain%24txtWhere单引号报错了，根据参数名猜测应该是拼接到SQL关键字where后面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQjqUh8JfkoelibgcbycA69b070BjbU9UkuldF0TsHkll6RE59PHZt26X1dMLw65y3ibZRIYcl1IuZ4Uy63A4f7oynm5nEibyxKuQ/640?wx_fmt=png&from=appmsg)

刚开始使用SQLMAP还跑不出来，开了level5都没用，思路一下子断了，感觉不太可能注不出来才对，MSSQL相关注入还是学得太少了，有空还是得补补。

简单把报错语句贴给AI，才明白少加了括号闭合，其实后面看报错语句其实很明显，当时估计太激动了。。

sqlmap -r sql.txt --dbms="mssql" --prefix="')" --level 5 --batch

SQLMAP指定一下前缀--prefix="')"就秒出，看来还是不能太心机，容易头昏脑胀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRclNFXrvLoeOfANOIu3gIFdywZDXZOqgnRicT2TzfoEzS66qupjRz6FmyGpgbqRTTSX2wtkml9qD05juaiaYT23Zt9zcJWjogyw/640?wx_fmt=png&from=appmsg)

如果一个参数存在注入的话，大概率其他接口这个参数也能注入，开发编写ORM配置基本都是如此，除非是特意修复过，不然出货概率很大，在一堆的Yakit HTTP请求包中直接搜参数ctl00%24cphMain%24txtWhere，果不其然，又找到一个接口/Grade/Report1，除了接口不一样，参数啥基本一致，就不贴了。

## 0x 03 反思

相比Java站点，ASP.NET WebForms这类站点，在没有口令情况下属实难以动手，但一旦能进入到后台，文件上传很大都没有限制后缀，不像现在一些Java框架，直接在配置文件里面写了限制后缀jsp等，SQL注入出现的概率也会相对高一些。其实看到ASP.NET WebForms框架第一时间想的是打ViewState反序列化，但是貌似开了ViewState MAC（主要还是研究得少，下回系统研究一下），没那么好打。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjYTeyXHUPicL2ldpL7ZEocamWUsbjc42j2sKMl2z4hIDdeHPsDJBVs02Iyw1ynmfOhibFeUrDtrK9oChofFhHJDERcvwZpPx30/640?wx_fmt=png&from=appmsg)

## 0x 04 后续

在资产测绘搜索过程中，发现这个框架存在不少资产，其实也不多就几百个，根据接口批量进行扫描，在其他站点发现了一些其他接口存在SQL注入。首先是在后台有个高级搜索功能，点击之后会有能筛选字段，随便点击进行搜索。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSIt8O3C003pUFrq0Bop7rXtBrX681lZ7AMDrXPPh9DDOKWWWwkz9mzb0xx3Gc7kZqYSkaT37lfGGPu60gplA6gmuHjMauay5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnGIsUNFT1gAoFLyZaOqjYtjhB5ibMVVanScrhhGibfUC0MtvrAY8lJo7VhdLFLJ1Tw6Gl70plDOUJbuxjterlw3y8hTnxnS3lY/640?wx_fmt=png&from=appmsg)

使用Yakit抓包发现存在POST请求包，这个包中的很多字段跟前面那个包基本一致，所以也均存在SQL注入，大致FUZZ了一下

ctl00%24cphMain%24txtSearchTitle

ctl00%24cphMain%24txtSearchCreated

ctl00%24cphMain%24txtSearchStart

ctl00%24cphMain%24txtSearchEnd

这些参数均存不同拼接的SQL注入，大致的注入语句都差不多

使用payload：' AND 1/DB\_NAME() ='就可以成功注入，这里使用1/xxx，xxx为字符串，这样可以让数据库类型转换失败而导致报错，至于后面拼接=是为了表达式值为bool类型，否则SQL语法会执行不了（根据单引号报错出来的SQL语句以及报错信息），忘了截图。。。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSMzA9P4h0vZEZtUN0pIMzlxgEOQSWbtKwsmImkjh9Jm1mHPqvVKmDNviaYZibIOvSspMv9pykz2ELMWONepwAImu8FGibZOUfkyE/640?wx_fmt=png&from=appmsg)

根据这个高级搜索功能，猜测其他接口也很可能会调用这个接口，毕竟是筛选功能，果不期然，也是找到三四个接口可以直接打，最后报告交上去也是刷了38Rank，可惜教育资产使用这个系统并不多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTuiaZtRBt6mHd2ZZCq2PmkBtXywTsdqFibhDk71YjXCeIrnKnOtrbUFVdR6N9k88Tu3s7b7icVEyVykowJmJocib0jqKwJe8feqw0/640?wx_fmt=png&from=appmsg)

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中）**

```
信息收集(会永久提供fofa-key助力)弱口令漏洞任意文件读取&删除&下载漏洞sql注入漏洞url重定向漏洞未授权访问漏洞挖掘XSS漏洞挖掘等等常见漏洞EDUSRC证书站挖掘案例分享SRC挖掘实战针对各种常见功能总结的常见测试思路等经典常见Nday漏洞复现等各模块不在一一介绍
```

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSWarKnFiaUicnq701hWQaiaA94FmgLNE8SVmrJiaJwluiavCE2VRvDV3ZYnwhib2pSNEpPp3Qp3beicPIAsVs3dS4A2MoYQXcsticwlqQ/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRD8gJdgFicMTaYcSMHydxPNJvagOaOrNbrM6S2tDPEcmjyECKacjmNJBCtwGAKMNdMes7tztJfWZGqjKxC7tkg99v4uDXDTpSE/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=...