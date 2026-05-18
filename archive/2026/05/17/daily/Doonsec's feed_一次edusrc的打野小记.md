---
title: 一次edusrc的打野小记
url: https://mp.weixin.qq.com/s/6tg4-tqlTDDC5b7yDmZ27Q
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:09:32.326845
---

# 一次edusrc的打野小记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibeMgKhFUfbQTQxEibCguHjEf7tPh8jhNC49aWK4pKQuUuia48t1vNSS4xUXZQjpBU6RxQdyWmn13zjZw36BvLOdjDKeL1tyW6MqJfaudU1DE0/0?wx_fmt=jpeg)

# 一次edusrc的打野小记

原创

狗窝
狗窝

狗窝集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

起因是小伙伴初入网安，自己尝试挖掘了一些edu的漏洞，在怒肝一个星期后获得了一个证书站的单洞，奈何分数不够，叫我帮他水点分

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRLxNKEGsRxnia1bpOeTDy7vlWW8hKUPQayud7ia7ym3uZCGWPDmjWAVVSE6QmFmmrb4V1b0iaHzgM9CUIMo5qoZWRJVYiczZdeiaqU/640?wx_fmt=png&from=appmsg)

于是有了这篇打野小计，对于edu想快速上分，我感觉就俩条路，一个是专门找通杀去刷，运气好亦或者实力够，测出通用资产的漏洞可以上波不小的分。还有一种就是找一些为了方便学生或教师使用的小程序，这些小程序往往偏向实用性而忽略了安全性，通常存在未授权访问、sql注入、弱口令等漏洞，一些小程序是可以通过手机号快捷登录从而可以进入后台测试。

资产一番筛选后找到了一个大学的学业讨论的小程序

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQp7KFBqq9qPu8nQeXoSolXlGodBJia9qzURxjPpibWPOZ3R2IqRIXHbLQNDaQDcK2znnWlYMlgnevkicqfHQkb8ibFfZURjBWGkRY/640?wx_fmt=png&from=appmsg)

右下角有个发布文章，一般这种地方很容易存在越权漏洞、文件上传、存储型xss、敏感信息泄露等问题

这里进行上传测试，随便传了个图片，测试一下上传功能是否正常

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbTOP5Qp7keInoic4gRhGuJoia7Giapgzq8I5fFia1EeBib0Oz5eewjBjibgEQeMzEhiaiccMgXFYrnicYLXjQJ7JIIVdYcHkNfgYr6aibsKg/640?wx_fmt=png&from=appmsg)

上传数据包如下，看接口跟上传后的保存路径，是传到了存储桶中的，cos云是腾讯云，对于传到云存储桶的地方，可以尝试去访问一下存储桶的地址，或许存在未授权上传、覆盖、删除等问题对于云存储桶的打法，上一条文章有写，不熟悉的小伙伴可以看看上一篇文章，这里不多赘述了。

不过这个站不存在未授权，于是尝试上传.html的xss

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbSLI4BibJibcLY6FKI140EeIUNggqyiaCpn7Bn7eqgS4fMKiaVYQEL6vINszBfu09niciaPDpVWeMAAn6ehUqMchOWnD94zhJeLgiaNDo/640?wx_fmt=png&from=appmsg)

显示上传成功了，访问一下地址看看，成功解析，这里可以水个低危。这里也多说一下，如果是存储在桶中的文件，是不存在上马的，因为桶内并没有环境去解析，即便上传成功也无法解析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbRj2viaQb8NUrDPOjk9SmQoTbdqibPZlz3yibc6HM4dhg3riaFHU3dCIy7ia8JF1OTc2WKOZyND3TuNQu61afTBINMPN0ibOWniawQAiac/640?wx_fmt=png&from=appmsg)

这里在上传的时候也观察到了数据包，因为我这个是快捷登录后进行上传操作的，按道理来说我的数据包中应该带有token的，但是此处的数据包中并不存在鉴权字段，后面使用别的功能也不存在鉴权字段，所以此处猜测还存在未授权漏洞，浏览器访问Web端

访问web端如下，这里可以看见是使用了vue，很明显的前后端分离

前后端分离的特征就是xxx.com/#/xxx

再加上前面已经猜测这个站是存在未授权的，使用工具去提取js，找路径拼接

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQKFISJx4CsKFibIzSlxnD9ibdMo9gJugBIv64UK6P9F00HySgPYX6x29spAib6JfBaSLaibbKnZL0ZArDWZEnM5yhBQBqV3UNjaicI/640?wx_fmt=png&from=appmsg)

不想自己收集的话可以使用工具VueCrack

下载地址：https://github.com/Ad1euDa1e/VueCrack

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbQeexDhNuLwUiahaLQXlzkNnpxrv6r7mLJ1eaQTOXibB4mUOB7zLRlGfibShkFCphBoiaK07UyVdG1iaaKByoGExKYYcoq0OXfFxy2Y/640?wx_fmt=png&from=appmsg)

此处拼接路由直接进入后台，所有操作也均可以正常使用（又水到个未授权）

在这个页面看见还有个查询操作，输入数据点击查询，尝试是否存在sql注入，老演员sort

单引号报错

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbThRsHLCALj4XMYajbzuW1TNhpyeM4CHI8BRz1pxJHZCTwytBe1UMpgCNG5lBjSago6h16AFibeBXont9oxKMmjsfvHR6CI9CPY/640?wx_fmt=png&from=appmsg)

这个站没waf，常规报错注入就出了，这里就不放图片了，后续是刷了几个接口的sql。

这里通过sql注入可以获取到管理员的登录账号和密码，如果不是特别缺分的话不推荐去跑，非要跑的话速率开小一点别把站跑死了

最终打野成果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbSMCT3AaLhOO5ELiaWdKviccbbDLw9LaZOh8QzFagkzTvsacdXKeqMHXFViarsoicVaibJH0zSgibxX6V0EPagKZ24sxthWdibib1y5mkw/640?wx_fmt=png&from=appmsg)

结尾打个广告

狗窝小课堂开课啦！

课程分配：50%理论课程+50%实践学习(导师直播带)

形式为直播互动教学以及一对一答疑，每次直播都会有录播(敏感操作除外)

每周两次直播，每次直播一到二小时，第二期课程周期预计三个月

贴一张师傅直播带学员过WAF截图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibeMgKhFUfbTW1qdENIjI4zPgBF8PLtbEJVGqXFibzmVmq8iaHMichnzA7GACpiaviamXyEdBEVWmiaMSjdIaXoiakGTepc6MI4FIprRCxZvQ0GSIyI/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/57W11VialTL95PQibvFehAyWX4sUttLiboVdPQ7qpRRMI1qibJgkxxv5fnIU6VHrEbVgeJVJ4kbTedPcu8OwvIFkOg/0?wx_fmt=png)

狗窝集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/57W11VialTL95PQibvFehAyWX4sUttLiboVdPQ7qpRRMI1qibJgkxxv5fnIU6VHrEbVgeJVJ4kbTedPcu8OwvIFkOg/0?wx_fmt=png)

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