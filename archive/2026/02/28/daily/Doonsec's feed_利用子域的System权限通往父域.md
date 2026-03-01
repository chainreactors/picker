---
title: 利用子域的System权限通往父域
url: https://mp.weixin.qq.com/s/BMMbEwewy7dfDxYt7ecmzA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:17:39.721353
---

# 利用子域的System权限通往父域

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mwFvjeHDLkhW2qs9tmAPNYfe8SJGIpibzB3icg0yjjLdWdg5g68n0mdTIDIOvD0my4fromK9VNuJMnzD3QWCts0k8ZepAvatpUutGLCfXJrHc/0?wx_fmt=jpeg)

# 利用子域的System权限通往父域

Jumbo
Jumbo

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

## 前言

翻阅笔记发现一篇文章(附在附录)提到通过子域的System权限可以突破获取到父域权限，本文将对此技术进行尝试复现研究。

## 利用分析

环境信息：

```
子域：187、sub.cs.org
父域：197、cs.org
```

首先通过在子域的域控机器上打开mmc.exe->连接ADSI->配置来查看子域的配置命名上下文：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWKCZ12bQjGSENAqI0aC3HNwRnqbzXwrCtlpsbib1IW6MKoAjfMrdVrBQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "null")![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbW1KJ2nQbGrJicmPKvbSzIlAw40EjQ6a8HIRvYibd9WmUibrHqYiabbmoR1g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "null")

从配置中可以看到配置命名上下文的域名实际上是父域cs.org，因此判断子域中看到的信息可能是父域的副本：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWKGY30dvZsyP27AY1VobkW3O26xNVZFd77tyv24QbhVcB8vnUghOmsg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

继续查看配置对象的安全描述符中的ACL，发现子域没有权限去变更：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbW0utbHcmwxetgLEawjJpc8L4ynKl2QVAZ3TDIV5C0hksLKSfhYtTEYw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

但是可以看到除了域用户、域管用户以外，还有一个特权ACL条目叫SYSTEM，该条目拥有完全控制权限：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWNEUffKExA1kLRTfzurBw04MDwhIEuNUb8R3ziadmg6A15dTyvGic2iauA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "null")

SYSTEM属于一个特殊用户，不属于域内用户，因此理论上只要能做到是SYSTEM权限就能控制对象条目而不用关注是不是域内管理员。因此尝试使用SYSTEM权限继续打开配置命名上下文：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWURR20RtCnNnyJ7SicWibBK9ch1XibNwt1UuytWYrbLlXplf351Ev9mnNw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "null")

可以看到当子域拥有了SYSTEM权限后就可以修改来自父域副本的配置对象：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWa7sMF8Bf87elyKU8NEVuddpzv6PUBKuGcohlqX2p88zxnnib0hPUiaeQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "null")

## 利用方式

既然可以控制父域的配置命名上下文，那如何利用呢？网上提到有几种方式，一种是通过GPO、还有的是提到给父域添加一个自己可控的证书模板(ESC1)，这里以GPO组策略为例。先在子域域控上创建一个GPO:

```
New-GPO jumbo_gpo_test
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWKIFJFyJFDG9TqKYaicfTgG8FvbamUSKTdwy4krNmicjDpXT7A1DSYDZA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "null")![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbW1YIKHW9rW6SvkOP76lMEF0YVupr2NW4I6Cq2QcwmyA8ib6P6EC4U36A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8 "null")

设置计划任务:

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWTqtqMiadiaCL9fxp6pkr2zKD6P8kSvSn6qDZDjZpG0Su3Hq8Lk5ISaYw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9 "null")

通过SYSTEM权限把子域的GPO link到父域：

```
PS C:\Windows\system32> Get-ADDomainController -Server cs.org | select HostNane, ServerObjectDN

HostNane ServerObjectDN
-------- --------------
{}       CN=10_4_45_197,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=cs,DC=org
```

```
PS C:\Windows\system32>New-GPLink-Name"jumbo_gpo_test"-Target"CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=cs,DC=org"-Serversub.cs.org

GpoId:76606696-cd03-4349-b0f2-0a45bdf305d4
DisplayName: jumbo_gpo_test
Enabled:True
Enforced:False
Target: CN=Default-First-Site-Name,cn=Sites,CN=Configuration,DC=cs,DC=org
Order: 1
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWdjeRuLNnSianxl8kHBusQJne2DSVdefnop8EZqZwNeF0f5dkxd2pXdw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10 "null")

父域刷新组策略可以看到子域链接过来的GPO：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWXmSAibicJoBopnj5JOBNiaNU2KDv6mIOBSHqteYABCMy1uV9IbOuicAz5g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "null")

父域更新组策略成功执行计划任务notepad.exe：

```
gpupdate /force
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbWia2kgceKXBhp3a5YBQSLJoo49mlZN0nTTI3RdkRpfJC1yRiaLD0jlTCA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "null")

刷新组策略后通过`gpresult /r`命名也可以看到添加的GPO：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyUAaxFgbLheAQ5OdBclAbW6Bic8Mg2geQbKcKdYb4liajBknOUVNsmmoG1wIULKvoWUraDhX47uo0Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "null")

## 总结

本文介绍了除`SidHistory`以外还可以通过子域的System权限进行突破到父域的攻击手法。

## 附录

https://blog.improsec.com/tech-blog/sid-filter-as-security-boundary-between-domains-part-4-bypass-sid-filtering-research

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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