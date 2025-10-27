---
title: 一起来逆向分析某黑产APP
url: https://mp.weixin.qq.com/s?__biz=MzkwMTE4NDM5NA==&mid=2247486205&idx=1&sn=2b489f8336bc06a62fd1497518635336&chksm=c0b9e418f7ce6d0e16701880002d9222889aa273267d5291437802a669077572dd6d4bf80446&scene=58&subscene=0#rd
source: 无害实验室sec
date: 2023-01-05
fetch_date: 2025-10-04T03:04:44.645378
---

# 一起来逆向分析某黑产APP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ewSxvszRhM4VOAfpT2qdJiar5XaHeUuhY5rMGYX88N6jCicb8P2MkpiaYaRJr2Eibs8DqKr8UcVSAEO6VicHCXT69kg/0?wx_fmt=jpeg)

# 一起来逆向分析某黑产APP

渗透测试网络安全

以下文章来源于小道安全
，作者小道安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM58pVKC3t2yc9YZFyHgibgLnGkJtN8xicgfIs2fiapMut7rw/0)

**小道安全**
.

以安全开发、逆向破解、黑客技术、病毒技术、灰黑产攻防为基础，兼论程序研发相关的技术点滴分享。

首先这是一个挂羊皮卖狗肉的黑产APP,它通过文字和图片展示几个主流游戏和各种游戏皮肤可以实现作弊功能的APP，还有每次抽奖必中一箱茅台或一百元的话费福利。这一系列的钓鱼手法下来总有人愿意为这些诱惑买单。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDOWt24xe25ZsbYxtfWq1hTaujROFkIsbFUFG1h69bRpibH7uZDQpp2VQ/640?wx_fmt=png&random=0.3279751632040564&random=0.28825722790055863&random=0.610723515888143&random=0.08815536854432349&random=0.5073400843271871&random=0.5886216955279053)

下面就分析下这个黑产APP的一些功能和一些赚钱模式。

基础分析

这个APP伪装成为一个安逸防闪框架，从界面展示实际上是一个作弊APP的集合，该APP也并没有采用市面上那些提供免费版本的加固厂商提供的加固或者开源的加固进行对核心功能的保护，实际上是没有什么核心功能。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNID6DuWhpVAnPicsyV9WbsVjC65Rv7I68ZSD5EC5hDkeKmwTpicEtt7RM8A/640?wx_fmt=png&random=0.651789154032699&random=0.23525677920168464&random=0.9428591814057594&random=0.2872992025161558&random=0.31797026635501213&random=0.13364406161316045)

下面是该APP所申请的所有权限信息，通过这些权限信息可以大概知道APP大概会做哪些敏感的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDEbHpicAZqLPcaIMQiaTVib23qA0Hl54YfGSaQyKnLia2j0kulBNQ9yr30g/640?wx_fmt=png&random=0.21154686950123702&random=0.6129636657895301&random=0.8005393305635062&random=0.005176468894605657&random=0.9854599445826007&random=0.19863210732738024)

Java层的基本保护：类名混淆、函数名混淆、变量名混淆，这种混淆的保护在现在就是一种掩耳盗铃的方式。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDDrUoJJd7Vl8FPjjhGyPvhwk6aWzkvMozvmymAqTTcQKrYWIf5Lzwrw/640?wx_fmt=png&random=0.16217192703352556&random=0.47515605084735935&random=0.5378543977273076&random=0.49083449946236946&random=0.7884970181544582&random=0.6998068856945685)

防作弊分析

在APP中实现防作弊方案之一，一般就是采用构建用户画像模型，然后基于用户画像数据进行判别用户是否有作弊的行为。构建用户画像就离不开设备指纹信息的采集以用于实现一机一码的功能。通过一机一码保证功能业务的正常花。

在APP中实现防作弊方案之二，通过检测识别APP运行过程中是否有被第三方分析工具注入到自身进程中，还有识别当前环境是否是危险的环境。

这个APP主要集成了友盟的SDK和快手联盟的SDK，这两个SDK都有做一些防作弊的行为，友盟的sdk主要实现设备指纹信息的采取和崩溃信息的手机，快手联盟的SDK在防作弊方面主要实现了对运行环境信息 的识别和第三方注入工具的识别检测。

**友盟SDK功能**

友盟中用于构建用户画像，获取设备指纹属性有：包签名MD5，包签名SHA-1，APP名称，APP版本号，CPU，anroid\_id，IMEI，GPU，IMSI，wifi，meid，GUID，IDFA，MIUI，serial，ICCID，OAID，IP地址、MAC地址，GPS地址。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDQjy8CuV4ic6y2tj71nXVNJiaEg7ZKrwqjNEA4ox5f50Qv0alTozyGLDA/640?wx_fmt=png&random=0.23813559270193285&random=0.5426523013225903&random=0.6860771080872288&random=0.11979417613202115&random=0.6234656171991533&random=0.4852752675173637)

**快手SDK防作弊**

快手sdk中主要分为两部分一个是快手联盟的功能一个是访问设置拉取快手视频播放的功能，这里面主要集成了通过用特殊文件、特殊路径、特殊包名进行做识别检测运行是否在root环境下、是否有被xposed和frida注入

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDTM0DwQB4vh2UgHlYDeDd4MWxSdeW4d88nJlR27CZW0kiadcu1PJd37g/640?wx_fmt=png&random=0.6092813678764812&random=0.2093784542834909&random=0.2286713256476931&random=0.35646238564492694&random=0.24729352121183212&random=0.034649822749746484)

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDeYMrIiaia125VVxNPSp927yfCGjetenyQVBBpph2eqwRZGLms8iagmGwg/640?wx_fmt=png&random=0.6529202462010273&random=0.6015621603241119&random=0.7750507980844916&random=0.9902106190958841&random=0.5172752312967621&random=0.5509829492825555)

赚钱模式

基于对APP的分析，想下载利用该黑产APP所展示的那些具有作弊功能的APP，需要先看15秒的快手联盟广告视频，还有要下载注册使用15秒以上捆绑在视频中的APP应用。通过这一系列的事情后才能获取都网络搬运收集集成的那些可以作弊的APP应用。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDIKrMdicamdxia0SIuED3ibDe6Rl86lcoZ0NlPVkiaEpVIVGsJOhZS38z7Q/640?wx_fmt=png&random=0.4480579264634894&random=0.7336613050270413&random=0.9696617149023781&random=0.6999328234559246&random=0.8440394863430634&random=0.8204698971711231)

https://u.kuaishou.com/ 这个快手联盟就是个用于接投广告的平台，这个APP主要通过集成这个快手联盟的sdk，然后实现用于推广快手联盟里面视频广告任务和推广APP下载任务(都要15秒及以上才算有效)。

这个快手联盟接推广任务的时候需要先提交公司名称、APP应用名称、域名信息。门槛还是相对比较高的，一般个人想这个推广联盟平台上赚取一笔收益还是比较难的(虽然有各种充斥着500块钱可以注册一家公司的广告)。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDo6aibP4uHaF07mQ4ibRtkQXia2LZXCM8Mj5qdO96gdWnDaVbPJV28QGhQ/640?wx_fmt=png&random=0.7794296825868117&random=0.9710703914584038&random=0.3767581424351434&random=0.7666319059524602&random=0.4895903026540136&random=0.7499418114228373)

各种可以进行作弊的APP，不就是那15秒视频吗，看下就可以获取到，不心动？

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDneibuTUHL3xIJsbzmjPz24iaSqbOWKcqKwiaTibOeP4xRhDjgoBTOqyKFQ/640?wx_fmt=png&random=0.7252967416244334&random=0.7745292806330826&random=0.5343415814025481&random=0.28358152507239787&random=0.5771645561443273&random=0.5257902049568657)

简单溯源

通过APP中的java代码部分(SO部分主要crash捕获还有推广的SO，没有其他过多功能)，分析到该APP采用明文硬编码方式，通过固定链接进行下载并安装具有威胁性的APP。

这个APP在网络通信方面也是没有采取相关的混淆或者校验保护，都是基于明文的方式进行的，这其实也正常因为这些APP上不了台面，不需要合规审查，只要能割韭菜就可以了。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDLh0Erx2F8DuNmDDTeS5wcXZ2FWZoMKQc3Z7EWzGFJSbHIpoFMrdT7Q/640?wx_fmt=png&random=0.2227603528360016&random=0.7846955015526051&random=0.9945992334539737&random=0.6796118175306938&random=0.8677915561477585&random=0.583655914314291)

通过360威胁情报中心 https://ti.360.cn/#/homepage 进行查询，可以通过下图看到该域名已经被检测出属于黑灰产信息并且具有不良的信息的标识了。

![](https://mmbiz.qpic.cn/mmbiz_png/jVCRndy8Lr5RVOY9bPPTY5MSdEaUDNIDzC71z6UtjlKTtDoxOnZgg74ZeAmX8OMica9THWobmDQWceqiaL9RJTQA/640?wx_fmt=png&random=0.5765407174834742&random=0.4976858430565114&random=0.235864197000762&random=0.23063705787480937&random=0.884909949934436&random=0.5073437178818412)

其实这个可以延伸挖掘该作者更多固定资产信息。然后再对这个服务器去做入侵或渗透的一些事情。

总结

网络上充斥着各种各样诱惑，总有些人会把持不住，自己还傻傻的不知道已经在为网络攻击者赚钱，最终不得不为自己的行为买单。

前面的那些分析，只是简单的分析该黑产的实际模式，并没有涉及过多的技术方案和对抗分析方案。这种模式其实和早些年在window端上那些网络上一键安装系统、2345浏览器、360安全卫士的各种推广一模一样，但是由于移动端的快速发展，这些搞广告联盟接推广的就开始将重心转移到移动端，这些只不过是换汤不换药的一个模式。

结束

**关 注 有 礼**

关注本公众号回复“718619”

可以免费领取全套网络安全学习教程，安全靶场、面试指南、安全沙龙PPT、代码安全、火眼安全系统等

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片关注学习吧！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

渗透测试网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

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