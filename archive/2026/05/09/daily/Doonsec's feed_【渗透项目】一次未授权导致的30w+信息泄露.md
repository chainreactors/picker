---
title: 【渗透项目】一次未授权导致的30w+信息泄露
url: https://mp.weixin.qq.com/s/ZmUPVxLPPcpHow4cP9XwsQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:29:48.890640
---

# 【渗透项目】一次未授权导致的30w+信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rz592WOpic8voRehC0BnzeyURBLeFcYO2icYEYLvPR8TL8ypu3qGqegeDp2dpicm5Cj2FXsyDJ1v77RUBQnibUKSsEs0GSZh5vjnPibL7kSlUSqs/0?wx_fmt=jpeg)

# 【渗透项目】一次未授权导致的30w+信息泄露

原创

观止安全
观止安全

观止安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rz592WOpic8s2nO3U1ZkrXe9nGkTztEa2icxkzHaLxIEOXp5R4IW10EDemTIHTicn1jYib8B7O8z3mHph6xuomWz8aXMibuNn98eQfh0Hr7ZQ9jU/640?wx_fmt=gif&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rz592WOpic8srEQxZXb36uqJOjVSO5Qtoqz7rYy0CP5ICMRDqTMictUl4KzcZKReW3JUictE8pdqqNzb8s8hFLuwtHibz7X1XrJCDKuIGoniaTiac/640?wx_fmt=png&from=appmsg)

联系方式

**vx：gzaqSec888**

**免责声明**：本公众号所发的内容仅供学习用途使用，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责！如有侵权，烦请告知，我们会立即删除！观止安全拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

**PART.0****1**

**渗透流程**

![](https://mmbiz.qpic.cn/mmbiz_gif/rz592WOpic8v7fNicrspbRRdqQRrMgzHacricxNZuq4l8eakqt32BXlhiaicv2a9CTrhUGuhvlCuniayDKcG4x1zeq1qc6wic27WCBzcHUoQmRRulE/640?wx_fmt=gif&from=appmsg)

进入系统发现是一处登录口，进行一些简单弱口令尝试未果

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8v845N0rstezR68V3pVKfWYQoMCwb2HcTyEnEoJlLDmicSZWsLicqia4fPXgVGaxtuaOsAZUFNe8GXicLP42ic3n9sUexZ6yHeBwIVE/640?wx_fmt=png&from=appmsg)

后面尝试使用插件vuecrak

（具体使用在我工具分享模块有介绍）

随意点击接口尝试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rz592WOpic8vKENo3vJicqfXes7J8YicCyWVSwmdQgc6BSVu0ib4jr8ISFkf7M4reSxmgCLwHcUQcyRrLKOlhQ3jX7Lz1Y3eBjt4uWkffR3M80k/640?wx_fmt=png&from=appmsg)

成功进入系统里面，账户显示admin，但是没有信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rz592WOpic8sqbQ5M8NU4u4qu55OqH5V3CXDloXdt8xr6OWdmJoC42DPebVRGqTicDmDvVokibVwoSmHX4LfugEicOzRgVw4JDd3zC2b7DJvLvU/640?wx_fmt=png&from=appmsg)

后面的话也是找了很多接口，都是一样的没有信息，接着就想着点点按钮尝试，发现导出按钮有数据，并且下载时间还挺长

第一个未授权：

点击导出按钮

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8sCc7oRKooxic9UWBF8g7NMHV2337XpOXGs7NNViaNfibUQ3G8NOy3Pe56B0diczt6r8wQmDiccBoUvUWicfkSXCIFkqnu2SONdVaudU/640?wx_fmt=png&from=appmsg)

最后导出信息，发现有6w+条信息，手机号，姓名，身份证等信息泄露

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8uYQXFZQhxfruRw5AnyCcaIouXEaia69h21Wia4tx2baqzEwQ69eYbFic282icU5szKEDokMnfTQJibgcic4EY6ka19YKTx7Cho9P3u4/640?wx_fmt=png&from=appmsg)

接着就是重新从头开始找按钮了，遇到了都点一下功能点

第二个未授权：

这里也一样的操作，泄露姓名，手机号，开户行等信息，还有票据单的照片地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rz592WOpic8s7rTCdkjxjkarAyxTpQ97BTSoCnMEN3Ycicwf58QkUiaLOwvVxqFDXk8IIRqLQQOF1RicUvRwgwrMQoReh2iaM8kXVDUzt4Nm8QicY/640?wx_fmt=png&from=appmsg)

第三个未授权：

这个和前面的有点区别就是时间可控，但是只能导出三个月的数据

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8vgiaFvzlIQPKABicv24M4K0KuZ85329q5ibmco2c159GMriaoLMM2sPFn3DB5rwrmjLrhhAmT7oqXlg7dMIdUo3uIXa58iaBm9wLTs/640?wx_fmt=png&from=appmsg)

通过测试，他在23年才有数据

下载到了26年1.1到26年4.1，从23年开始，共计3年3个月，大概计算有4.6w+信息

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8vccG8EKQddaMeHwlla9bWWS8FHQYF4tFhvEUBDFrubZQHPwQUBB853rR7CRnC9mX0p2bygbzYfg5Dlwo54y9vV02eQM3td1oc/640?wx_fmt=png&from=appmsg)

第四个未授权：

这个未授权也是时间可控，和上面的区别是不用下载，点查询即可，不过要加上时间，所以第一次尝试的时候才没东西

![](https://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8tb3iawdME7XMI6lWSrVleUp6JEaRg8z7fAibia7rMCVbicRkiaAAFr44uDt61AWiaGliadvGRcABYKjyYVHSVN2C5avlB2Gzfyb8lw78/640?wx_fmt=png&from=appmsg)

通过数据包调试时间，发现20W+信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rz592WOpic8tg1fezib5dbjYGwEXVXotaYJPjaW72JIVYGeDiaZrR4w9hkcBeRBM88sWZzehdhHFGaSo6THaVtVbia6qhpK1VZvuzrCU41jTNww/640?wx_fmt=png&from=appmsg)

**PART.02**

小结

![](https://mmbiz.qpic.cn/mmbiz_gif/rz592WOpic8v7fNicrspbRRdqQRrMgzHacricxNZuq4l8eakqt32BXlhiaicv2a9CTrhUGuhvlCuniayDKcG4x1zeq1qc6wic27WCBzcHUoQmRRulE/640?wx_fmt=gif&from=appmsg)

> 在未授权进入前端页面时，可以尝试多点点功能点测试，可能其中某个功能点就未授权操作！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8uD5goelaVkLjdNOiasia7blumw5rya5PDIoU51gUBwZO58dicZ31wHb55zibp7gzBHzTuWtKicK1Q6lGZqFXoyVgy4gsXybcBPaIxg/0?wx_fmt=png)

观止安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rz592WOpic8uD5goelaVkLjdNOiasia7blumw5rya5PDIoU51gUBwZO58dicZ31wHb55zibp7gzBHzTuWtKicK1Q6lGZqFXoyVgy4gsXybcBPaIxg/0?wx_fmt=png)

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