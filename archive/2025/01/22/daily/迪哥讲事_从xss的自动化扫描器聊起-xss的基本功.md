---
title: 从xss的自动化扫描器聊起-xss的基本功
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496922&idx=1&sn=f8c212b3d3e0fb45af733f56c776a356&chksm=e8a5feb9dfd277af68c2f94335499c7ee8b25a1a135dc168ad072328c4490be4b4e4ea34114d&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-22
fetch_date: 2025-10-06T20:11:28.530639
---

# 从xss的自动化扫描器聊起-xss的基本功

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7L0beTn90VaDOtFI2YicbsH5ib3hWJ5owf8NmbS5bSO7DffxM5ZAnZCE3STvMPsmGUNFYqan8AqC9Q/0?wx_fmt=jpeg)

# 从xss的自动化扫描器聊起-xss的基本功

原创

richardo1o1

迪哥讲事

从xss的自动化扫描器聊起-xss的基本功

## 正文

文章来源星球:

前面谈过xss自动化的一些姿势:

`https://t.zsxq.com/EQlQd`

`https://t.zsxq.com/o72PX`

有时候会看到一些群里的人会发一些用xss自动化扫描器来扫描漏洞的图片，惹得一众人羡慕

但是有的人用同样的扫描器却弹不了窗,为什么,搞不好有些小白可能会以为扫描器在别人那有用,在我们自己这"没用"。这里我们就祛祛魅

往下看之前务必了解一些扫描器的常规原理(星球里面文章也有)

其实市面上xss扫描器大多以发现反射类型的多,我这里就主要以kxss和xscan来举例,这两者非常具有代表性

笔者曾经做过测试,kxss这类扫描器主要是单参数为主,什么意思呢,这里我举个例子来阐述

```
target.com/query?p1=xx1
target.com/query?p2=xx2
target.com/query?p3=xx3
......
```

正常的反射类型的xss,如果你在查询参数里面输入xxx,那么在响应里面也应该有xxx

但问题是有时候xss的触发需要两个或者多个,比方说`target.com/query?p1=xx1`的时候xss不会触发,但是`target.com/query?p1=xx1&param=xxx`

的时候xss才会触发,这就说明kxss这类扫描器有天然的缺陷,xscan这类多参数的扫描器在这方面要比kxss要强

第2个问题是过滤和waf

其实xscan这类扫描器只是帮助你发现xss漏洞的触发点,距离你拿到赏金还有一段距离

一般xscan这类扫描器发现的点位我自己分为两类:

1.几乎没有任何过滤和waf--->这类就是拼手速,解决思路:对厂商实行严密的资产监控,在厂商业务变化的时候及时扫描,及时提交漏洞

2.有过滤和waf

这类没办法,你只能去尝试绕过过滤和waf,这里就体现出个人的专业素养了,直接考察你的xss基本功了

所谓基本功就是你要知道在什么场景之下是大概率有xss的,什么场景下是没有的,什么场景下是不用去绕过过滤和waf的,什么场景下是可以去绕过过滤和waf的,并且怎么去绕,其实都是有特定的思路和步骤的.

除此以外,你还需要提高扫描器的精度,这里就不具体展开叙述了.

有时候想写写基本功相关的,后面想想如果写出来可能会让市场更加卷,想想算了,目前只在星球里面写一些吧,哈哈,

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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