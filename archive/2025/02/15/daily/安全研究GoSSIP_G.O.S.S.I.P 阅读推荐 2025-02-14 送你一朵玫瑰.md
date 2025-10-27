---
title: G.O.S.S.I.P 阅读推荐 2025-02-14 送你一朵玫瑰
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499732&idx=1&sn=d50c541ef8966e4ba48c304e9874babb&chksm=c063d10df714581b8fd10ccc49eee6eee993b9edbec419a2416a8ebdba3314eb5fc5b98a82e6&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-15
fetch_date: 2025-10-06T20:37:45.271539
---

# G.O.S.S.I.P 阅读推荐 2025-02-14 送你一朵玫瑰

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9RmPrZUyAYmRg0B6ocicFC8Btp8IeHkPicPlpx2Bjq8dweeHU5HEyp43w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-14 送你一朵玫瑰

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9cg4kLbVzdsicuMfiaC2lVxibCGZdicxQTVhlImmZDNia5icLV2m6SX1OGNcQ/640?wx_fmt=jpeg&from=appmsg)

今天大家都在陪自己的电子计算机吗？情人节这天，你是否拥有甜蜜的爱情，抑或是让你的奶奶轻声给你念出Windows的激活密钥哄你入睡？我们在去年的9月9日（天长地久）曾经写过一篇《G.O.S.S.I.P 阅读推荐 2024-09-09 The Horton Principle及其它》的文章，里面介绍了一个叫做Microsoft Activation Scripts（MAS）的好东东，今天我们继续介绍MAS研究团队的最新成果——TSforge：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9JSgwsXnTfWHQrkrtzn7qOa6IGszlEUOFclia9lKJ3u2iaGC2Sd6kDlzg/640?wx_fmt=png&from=appmsg)

去年9月9号那篇文章介绍过，MAS研究团队发现了一个针对Windows Client Licensing Platform（CLiP）的绕过方法，以及相关的exploit——`keyhole`，不过这个漏洞同时被Cisco的Talos Team发现并报告了，因此`keyhole`实际上“出师未捷身先死”。MAS研究团队很生气，于是攒了个大招，在今天情人节放出来了一个Windows 7（及后续版本）和Office 2013（及后续版本）通杀的激活exploit——`TSforge`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9w01epcx7Ewt5YG1Jj3PFWEhjRvkMGvXqaruqSCImqPicXTTLWMhjA8Q/640?wx_fmt=png&from=appmsg)

这个`TSforge` exploit针对的是Windows的SPP服务，也就是上图里面这个Software Protection相关的应用程序`sppsvc.exe`和它对应的底层驱动`spsys.sys`（这个驱动在Windows 8以后就没了，跟`sppsvc.exe`合并了），还有一个用来验证product key的`sppobjs.dll`动态链接库。

再介绍一个历史，当然今天的小朋友肯定听不懂，那就是当年（最早应该是1999年微软开始推Office 2000）微软搞出来*软件激活*这个神操作的时候，有一个选项是“通过电话激活”，当你打电话去激活产品的时候，会得到一个东西叫做 Confirmation ID（CID），这个可以帮助你激活那些无法访问网络的微软软件产品。MAS研究团队发现，这个CID的验证逻辑就在`sppobjs.dll`里面，可以被patch掉（~~非常简单的爆破，小学逆向水平~~），于是就实现了如下视频演示的效果：

【视频参见公众号推送】

接下来，MAS研究团队注意到（注意力并不惊人）一个很简单的现象，那就是在上面的crack（爆破）操作之后，Windows竟然就不会再次去验证刚刚的激活是否合法：即使重新启动`sppsvc.exe`并且不再让`sppobjs.dll`忽略检查，刚刚的激活依然有效。这样不就说明，只要能找到`sppobjs.dll`生成特定的记录（当年玩破解的同学都很熟悉，要么就是去搜索注册表，要么找最新生成的数据文件，还有一个名字叫做“暗桩”），就可以利用这个记录来激活系统，而且如果能模仿`sppobjs.dll`，那么甚至都不需要去和Windows/Office那一套DRM机制大战三百回合（还要去搞定内核的一堆检查）就可以简单激活系统了！

果然，MAS研究团队就是用了上世纪的那一套软件破解思路，而且最好笑的是用了微软自家（收购的也算）的Process Monitor去监控`sppsvc.exe`，发现了它写入注册表和文件系统的数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9BjqXeYFBCCDXwHDKTmhkU8QHJibZBhPEGyMyyEaLm709u7dtlykaxAQ/640?wx_fmt=png&from=appmsg)

这里比较特殊的是Windows 7，`sppsvc.exe`没有直接写注册表或者文件，而是间接利用`spsys.sys`驱动来往system32目录里面写了文件。总之，如果能分析出写入这个（加密的）“暗桩”数据（微软管这个叫做**trusted store**）的逻辑，那就能够打破微软激活机制的保护啦。可是微软也是对`spsys.sys`、`sppsvc.exe`这些关键的文件做了一些还比较强力的混淆，MAS研究团队一时间有点一筹莫展。

不过搞研究贵在思路开阔，研究团队集思广益，在某个“偷跑”（leaked）的历史版本的Windows 8里面找到了没有混淆还带了符号文件的spsys代码！**虽然这是个ARM版本**~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9PdqhKfJFgxTibGmLNnWowW6hmvenLLHof8K5pH4t5iaLRxJ5tOE7Txaw/640?wx_fmt=png&from=appmsg)

这下微软就丸辣，不过MAS研究团队负责领导这个工作的小朋友`WitherOrNot`好像逆向水平跟我们编辑部很像，就是没有IDA和动态调试观察的帮助，光靠静态看代码就两眼一抹黑。不过好在费了一番周折之后，`WitherOrNot`还是避免了用QEMU和GDB去调试，而是想办法让IDA那个巨难用的debugger（上次我们用它好像还是在2015年）运行起来，并且成功定位到了关键的加密函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9BRukdhzlictYt76Lfp6iccH56POfcqOP30OBjXeKdU484hDXZHYj9G2A/640?wx_fmt=png&from=appmsg)

通过动态调试，MAS研究团队搞清楚了`sppsvc.exe`对**trusted store**数据加密前的数据格式，接下来，要给Windows写出“注册机”，只要能把一个格式合法的**trusted store**明文数据依照`sppsvc.exe`的流程加密，就可以用来欺骗微软的代码啦（下面就是一个成功构造的效果）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EZGRib6O4wAkRrrVfw7lrd9pt1paq1cklicvvG4BaT0cwIzYMlvqdVLd2WhIVz8ZM6LZVdLs0bxHkQ/640?wx_fmt=png&from=appmsg)

至于**trusted store**明文数据这个格式，关乎到微软的知识产权，我们就不过多讨论。MAS研究团队在实施最后一步操作——执行**trusted store**明文数据加密——的时候，一开始是让`sppsvc.exe`作为加密的oracle，不过这个很不优雅，还要用调试器去注入并且调用`sppsvc.exe`的加密函数，于是他们进入到了最后的逆向分析阶段，最后还原了整个加密流程。实际上，`sppsvc.exe`就像是一个勒索软件：先用了一个RSA私钥去加密一个AES key，然后再用这个AES key去加密前面的**trusted store**明文数据，生成最终的**trusted store**数据写入到注册表或者文件系统。Bingo！

最后，我们要祝所有今天还在搞技术（写博客、公众号）的朋友们（damn single）情人节快乐！有情人终成眷属 ~~山盟虽在，锦书难托。莫、莫、莫~~！

---

> 文章：https://massgrave.dev/blog/tsforge
> 工具：https://github.com/massgravel/TSforge （微软还是很赞的，没有在GitHub上拿掉这个项目，大气！）

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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