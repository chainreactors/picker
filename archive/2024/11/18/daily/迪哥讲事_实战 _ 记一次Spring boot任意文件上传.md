---
title: 实战 | 记一次Spring boot任意文件上传
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496357&idx=1&sn=a65d53958d2fb72f02926d027d247350&chksm=e8a5f8c6dfd271d0e0be8b83b8c4d1d4179ac8c8e89ea7ec34d0f9344ab13944e2e50247d33d&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-18
fetch_date: 2025-10-06T19:15:02.505253
---

# 实战 | 记一次Spring boot任意文件上传

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6DaU1haJfCuEf1coxqTK78Y6R6uNib08Svdp0ylN3upJWzibmCocC8xBrhd9VW2pic3XlAx6nCRcicUg/0?wx_fmt=jpeg)

# 实战 | 记一次Spring boot任意文件上传

迪哥讲事

以下文章来源于HACK学习呀
，作者0003

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM40Ey25ia7icKDtM0hyhYQeTnJdaC9NzZRHPkFM71EAD3Fw/0)

**HACK学习呀**
.

HACK学习，专注于互联网安全与黑客精神；渗透测试，社会工程学，Python黑客编程，资源分享，Web渗透培训，电脑技巧，渗透技巧等，为广大网络安全爱好者一个交流分享学习的平台！

前提：

在一次项目中获取了一套通用系统

框架是Spring boot

启动是War包启动

之前拿是通过替换私钥拿的，但小部分还是没开公钥登录

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0lIFIIZFicAyonT6pXFAbF6Pc0b0Ull46WHRUiaGcNibdf2lNFFJ2nbZNQ/640?wx_fmt=png)

这时候就有人说为什么不通过写在定时任务反弹shell

也试过，不会返回，所以这个方案就取消了

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0dZN0ibLTt2ImLkRANjAeBQV09VmN6o5xibe1g4U7VIHlAVY7Je2MW7fQ/640?wx_fmt=png)

咋不直接上传，因为上传的文件是到另外一个端口，而且不解析

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0EicBiahFUib1z3ndR5p5oibwCEd6gfO1X3s2TuQt7eQOeoWukjYqllgqicg/640?wx_fmt=png)所以就想到一个另外的思路，由于这套是通用的，包括他们安装目录也一样

替换他们的war包,先下载他们的war包

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0Q60ZRnVibjlRwicDfIYrUGzq4YwWTc8TWc93VuvMoJ111MichTORG3O7g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0EicRLuk9zMSvZdS1sSBREHnwiccDR6Kc9TfMC1oxUzmaFqOBqa0S0lkw/640?wx_fmt=png)

把war用压缩格式打开，然后添加马子

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0hKIeF41sW6a8G2CNXFTnTic7CB6TgCze4icKH4cic0D7icdiaRGtcMqJ4IQ/640?wx_fmt=png)然后直接用burp上传抓包不太行，如图，会内容太大不显示，因为我们还是通过跨目录上传

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0skH9Xue9ZyN7zIcat078Sa8ZPGc4NQBfM7fqIIicm34MXQoCibDkfVEg/640?wx_fmt=png)所以写了个脚本

```
1.上传替换2.要定时任务执行kill杀死当前进程 pkill -f ***.war3.要启动war项目java -Dfile.encoding=utf-8 -jar ***.war --spring.config.location=application.properties
```

通用直接写脚本梭哈

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0yhnib5QtrYia8Fpv4KiaADIQsSjmTyyC0KyaD0Eicd3sC6VH4AVpfNNicAQ/640?wx_fmt=png)这里脚本是设置了代理，看看返回的包

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u01iazb9z8W2r76yydO6KoVnVwsibXibTOjw5BRnReknTpmiaVgxicZhVibGHw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u0NHsKQIOQA3cpbk2qECZpnUe6iccD0OCT9nuTl5k94ZOInibB07quZcOQ/640?wx_fmt=png)如果直接替换，不重启war包是没效果的，如图

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9ozBBTI1KFAdicicnn8aM5u08w0cxL1F35IqhpC1ia68uFvpIPAWqmtgtThTXnbAzrnDMsWXibicZDVxw/640?wx_fmt=png)总结：

实战没用，只是说对于通用系统，部分利用的点不能利用的情况下，可以这样弄。所以个人觉得鸡助。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

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