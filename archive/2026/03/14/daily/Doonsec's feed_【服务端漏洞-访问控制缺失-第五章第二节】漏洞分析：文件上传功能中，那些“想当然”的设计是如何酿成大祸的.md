---
title: 【服务端漏洞-访问控制缺失-第五章第二节】漏洞分析：文件上传功能中，那些“想当然”的设计是如何酿成大祸的
url: https://mp.weixin.qq.com/s/-tsHUkzrbitz1tnIS0X1jQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:14.557684
---

# 【服务端漏洞-访问控制缺失-第五章第二节】漏洞分析：文件上传功能中，那些“想当然”的设计是如何酿成大祸的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGHtIU3D5ZYU7UEicc21WzqBdAXVWUo5vkvlTFJpSleqNiaakfyAVcXIgAfTrPaMxFAjqJNzE1pnDUU0oXeXa7iaJ5jl8OUH6VrzCs/0?wx_fmt=jpeg)

# 【服务端漏洞-访问控制缺失-第五章第二节】漏洞分析：文件上传功能中，那些“想当然”的设计是如何酿成大祸的

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

在上一章节[【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797965&idx=1&sn=7f50945921f1eaa1d50f3f659d81e0ff&scene=21#wechat_redirect)中，大家对文件上传漏洞的基本原理和产生这种漏洞的原因都有一定的了解了。今天这边就结合着上一节的内容，来给大家进行一个比较简单的文件上传漏洞实战演练。

文件上传漏洞都是出现在有文件上传的地方，比如一些文件、资料上传功能、一些更新头像功能，只要系统中存在可以上传内容的功能，都要注意。在今天演示的系统中，是在登录后，存在一个上传个人头像的功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHLia1lPyhjf7qgtiaRvia7tZMiaRlKWzhAmHO5eoXO687ExSOQADbuy3MgXHicfISqjB81UnNnat23BPjjDIYMS96sp62rVxgegWgM/640?wx_fmt=png&from=appmsg)

在上传文件时，我们就要开始注意抓包，看看后台是如何处理上传的文件的。图片上传中规中矩，没什么特别的。具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGGxhB06WexJXDXhLFshehhmnC1kQc2eaqz9s0RswaD2Tm5tOFIBsrYIAjicY4VHJ5U85cEPQMjGiaDrPKtJ8MTqEXwWMGbaFW3C4/640?wx_fmt=png&from=appmsg)

既然上传的地方没啥特别，我们继续看看上传文件后，是否返回了统一格式的文件名称，这边发现上传成功后，系统是按上传时的名字存入服务器的，而且存入服务器的路径也是明确告知，这边可以直接访问已上传到服务器的文件的。具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFCrLFH0PfD7EjIyysGLSuu00yMGibsZeAj6O6VKvpbwp7ZJ2UIf1s0L1m5wTlHibgtCdT5iahf19M3SHwKKrzPfsnR2Ghg5VBVYQ/640?wx_fmt=png&from=appmsg)

服务器的这种处理方式很重要，直接决定了我们的下一步动作。既然上传后的文件名不会被服务器改写，而且也能得到具体的访问路径，那么如果系统没有控制上传文件类型的话，是不是我们就可以上传SHELL脚本来获取服务器内容？

说干就干，这边编辑保存了一个 test.php 的一句话木马脚本，包含以下内容：

```
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

发现系统并未限制上传的文件格式，这个木马文件上传成功了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGGCeIBGfXsgIDibVFmwUWuQaSAFicibavciabMMoBSegqkl3bVwuHibMwTqqaEqjwSZdt3Ta0775uqshqKx4UZnKJG0Dq8RMhO3x71w/640?wx_fmt=png&from=appmsg)

仅仅只是成功上传了木马文件可不够，文件上传漏洞的重点在于“执行”，根据前面我们对系统的分析，上传图片后，返回的图片链接来看，这个木马文件也是可以通过相同路径来进行访问并被服务器执行的。果然，直接访问系统返回的上传成功后的路径，就直接实现对木马文件的执行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGH9trWI2UClg5B5pDwQLkpiaGWOxnSCXDcGFrJiamTD9IxHXIKic6JxNdTbGkH6EjvTib4HBU4Tpn2ByAhg1eufibNRDvvibnxKJjocQ/640?wx_fmt=png&from=appmsg)

最后，通过以上操作，我们就成功利用系统的文件上传漏洞，获取到了系统中我们想看的资料。比如我们可以将一句话木马文件修改为如下：

```
<?php echo file_get_contents('/etc/passwd'); ?>
```

就可以获得服务器的用户密码信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFljibFiaKjs2Q9KiaSibVzm6ItPtZG06kRolKqSXD65RYpvV1z9FNFlkbvL3NgxpqtDmRgVAOQ4As5TQGfv9VwnW3x4sLor4ibKPGs/640?wx_fmt=png&from=appmsg)

好了，今天关于文件上传漏洞的简单案例分享，就分享到这了。后续这边还会继续分享有关文件上传漏洞的更多内容。感兴趣的话，欢迎搬凳关注，提前占位。

觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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