---
title: 新型钓鱼诈骗：贪小便宜吃大亏！！
url: https://mp.weixin.qq.com/s?__biz=MzkwMTE4NDM5NA==&mid=2247486120&idx=1&sn=a03981113a8588bfaf08e77dcad61613&chksm=c0b9e44df7ce6d5b196525b62adee2fb7085852a716f1b854269474af71035917980d955a20e&scene=58&subscene=0#rd
source: 无害实验室sec
date: 2022-10-20
fetch_date: 2025-10-03T20:23:37.501006
---

# 新型钓鱼诈骗：贪小便宜吃大亏！！

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd90xk3Wc3b2bAeAl6tCTicv2qMx2prIKBAkdnxfvruqbzPpC1ulWjf09w/0?wx_fmt=jpeg)

# 新型钓鱼诈骗：贪小便宜吃大亏！！

渗透测试网络安全

以下文章来源于潇湘信安
，作者嘞萌

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

这篇文章由“潇湘信安技术交流群”@嘞萌师傅投稿，@3h整理发布，记录的是他在无意中发现的一个新型钓鱼诈骗方式，从技术层面简单分析了下。

目前微信官方已对这类诈骗链接进行了屏蔽处理，而且“武定警方”官方公众号同时也发布了针对此类诈骗手段的揭秘文章，大家可以去看一下。

[警惕！武定公安民警潜入“骗子群”为您揭秘：“免费领取微波炉”是诈骗！别再转了](http://mp.weixin.qq.com/s?__biz=MzA5MTU3MTE2OQ==&mid=2653194326&idx=3&sn=0dbd83b4db803a3b82215e7d9b1435f8&chksm=8baa7ed8bcddf7cec08b2d582b7008684abb01148ad8eab326a7a01b243a0c60de1ca85d37dc&scene=21#wechat_redirect)

**0x01 前言**

前几天在微信朋友圈看到有人晒图并配有文案，只需扫码转发朋友圈就能免费领取小米微波炉的一个活动。

当时忘了截图了，但图片和文案基本与下图一致。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9zw8mW1Qic2kTgNuSBqDpF2EibXp9k35xeV0WyJejZj6UZvmQqMMf6xbg/640?wx_fmt=png)

图片来源：武定警方公众号

扫码后会跳转到一个“小米客服”的聊天页面，点击免费领取后就会要你按要求转发他们的文案和图片。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9EpMLt3mWC3Qibf9emjt1EDmtY0O30nmRoRcVQSGWtm6T3iaYe9cz2Qeg/640?wx_fmt=png)

**0x02 分析过程**

右上角查看链接时发现猫腻，并不是小米官方域名，而是某些G0V域名，找了几个案例都是G0V域名。

```
https://*****.qinghai.gov.cn/uploadfile/2022/0905/20220905130919799.xmlhttp://****.jl.gov.cn/u/cms/swcx/202209/08092103g0xe.html?Q3yw=
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9TkN2NBtu2UWpBwxBS6eqRXkLuUgRO8UKOyXDcn4Us52mPJYujengGA/640?wx_fmt=png)

查询备案是某市政府机关域名，怀疑是漏洞被利用了，被上传了.html和.xml等文件。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9KAlEicV1HHvyZPsCpdfHZgmibqYbrF57GUVia0Vwpye347YgbPGKzlIxw/640?wx_fmt=png)

.html、.xml这类文件中被嵌入了恶意的JS，只能用微信访问，用浏览器访问会跳转。

通过Burpsuite抓包修改UA头，这时可以看到包含的恶意JS链接为：http://liink.cn/dfjrj 。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9nHPF0dgCkjS9ia63tXCPRGicYYB0lct22Nh26aG3nx42ib8GPe79YK5ww/640?wx_fmt=png)

这个域名的解析IP为：125.77.168.209，是福建泉州【电信】的一个IP地址，胆真大...。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9ficLskd9lTiac0019jtIVV68BOfaheHG0xY41zJoUdgWehpVYh2vDptQ/640?wx_fmt=png)

恶意JS链接会识别你的平台是Windows还是Mac，如果都不是将会跳转到一个新的链接。

```
http://fanyi.youdao.com/server/webtrans/share?fileID=e01bceae5c8d439fbf192749774a83ee&salt=1662522510039&product=fanyiguan&entid=dfjrj&njmtnb=bc2209b4b19c99f2f00e817513a9e989
```

‍![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9j7LMVHeWX3lLBpHAsxf5Y4yyWB6vyviavOVBic1tAwRcQgdvrW6h5JAw/640?wx_fmt=png)

这是有道翻译对外提供页面的服务，直接访问会出现以下提示，简单的一句话完事，官方都不带审核的，着实让人有些无语......。![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9h6loqS1TmFp4o6ibRXiaPt9xdcRibbyVtXgqyxzwXxHqDfHB4z5IUSbaQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9IkngNgP8mhOfY68iax7T0hBKJ18VpIPoh6xY5f8LcKc4wicTJqjI0EdA/640?wx_fmt=png)

但是这里进不去相关页面，因为有道翻译的第三方服务是直接解析的诈骗网页源码，里边还会判断平台，也会根据以下网址获取到的IP判断地区。

```
https://only-72244-222-188-46-25.nstool.netease.com/info.js
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd94z4hA0Dy73niavLUx5WWI3qke33CVIcN3FqW6J3TKmUELW8LF6mdQcQ/640?wx_fmt=png)

因为这里也判断了平台，所以只有通过微信扫码才会跳转到有道翻译这个链接进入“小米客服”聊天页面。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9EpMLt3mWC3Qibf9emjt1EDmtY0O30nmRoRcVQSGWtm6T3iaYe9cz2Qeg/640?wx_fmt=png)

当你按要求转发完朋友圈后他会向你索要姓名，电话，住址等个人信息，最后再给你发一张快递单的截图来博取你的信任，很多不懂的人就会上当了。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9mg4SeCgwZXGmehQ6KOicnxrlccCh2FGN0XYOicptc5DeVszZPmCCMibAw/640?wx_fmt=png)

本以为是他给你打印的单号糊弄你，没成想后面发现居然是网页生成的这快递单图片，真是零成本钓鱼。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9VXWiaBbpUgjv4fHCElibBySmBjJt2eSzn13ljtalhQbeMNbbY6h1zSsA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9WXZdkauDBoxkEJHGgKDKqf7FFnlPMklDbTnicgKM57ibeMyPZExg9VgQ/640?wx_fmt=png)

而且他会引流到QQ群，注：必须进群后才能安排发货......，至于这个QQ群具体是用来干什么就不细研究了，肯定不是用来做啥“好”事的！！！

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd9wtlicjls57C4wHiawgiaDgqSdSHiaj0hK8aHa9BfQmlnP0tBvJXviaQQWww/640?wx_fmt=png)

https://c.liink.cn/code.php?dir=KF 这个链接中有这样一段代码，看着像是经过反转的QQ群链接，应该还需要拼接下，没有再去验证了，有兴趣的可以看下。

```
{"data":{"url":"f3MfNeyQZTGfscQm1PYMVjgplw=k?rq/mq/nib-igc/moc.qq.mq//:sptthiICgjMpypNlmpOuo1iDGm8BYih131Sn1H8ReD77o=yeKhtua&DBrenz0=ecruos_edocrq_lanosrep&0=yfirevon&LY2WPSPhh4tou5yyXcCemJPT"},"code":0}
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOdRNCqbDHjyzGmlJ14tTCd96tIYRqnf31ZVumuJpmlERmPDyGn7C8ep6mjuk0fK1tCaY7znm4BKXw/640?wx_fmt=png)

到这里整个分析过程就算结束了，估计后面就会出现电信诈骗了，例如：你的某某快递被拦截，需要交保证金才能放行，或者带你兼职刷单、投资理财等诈骗方式。

天下没有免费的午餐，不要想着天上掉馅饼！！！

天下没有免费的午餐，不要想着天上掉馅饼！！！

天下没有免费的午餐，不要想着天上掉馅饼！！！

**关 注 有 礼**

关注本公众号回复“718619”

可以免费领取全套网络安全学习教程，安全靶场、面试指南、安全沙龙PPT、代码安全、火眼安全系统等

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片关注学习吧！

---

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUo3aUqQLOAfnCTViaQrOSKwkOaib7FX1N3tHIJutubibgicoAbGicv1vPXbw/640?wx_fmt=png)

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