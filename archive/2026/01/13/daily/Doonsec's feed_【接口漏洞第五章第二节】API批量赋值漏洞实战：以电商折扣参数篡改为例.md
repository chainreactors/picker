---
title: 【接口漏洞第五章第二节】API批量赋值漏洞实战：以电商折扣参数篡改为例
url: https://mp.weixin.qq.com/s/0Bg6aTiSrDTPu8y-zcSOjQ
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:56.218046
---

# 【接口漏洞第五章第二节】API批量赋值漏洞实战：以电商折扣参数篡改为例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JaKyaqIuTKq7LluMSdAKFEVVib2uREexiajEeibCSDktVVAbO0fDJoialcw/0?wx_fmt=jpeg)

# 【接口漏洞第五章第二节】API批量赋值漏洞实战：以电商折扣参数篡改为例

原创

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

我们在上一节[【接口漏洞第五章第一节】当API“过度热心”：批量赋值漏洞的狩猎笔记](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797709&idx=1&sn=cc68df4ba1f0d4bdeba5cfc3a7e3ae2e&scene=21#wechat_redirect)中，有聊到api接口的隐藏参数和自动赋值参数的内容，但如何在实际场景中进行挖掘和利用？今天我们就结合实际实验场景来给大家做下演示，让我们利用这个漏洞原理来实现商品自动打折，并实现“0元购”

首先，在进入系统后，同样的，我们还是先用自己的账号先进行登录，并访问系统中的各大功能，如添加商品到购物车、查询商品等操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JXIUFFWh0micJyPfBapDOdNicwbxXEfj4gzlquAPa1peXpXXPzjGtlbpw/640?wx_fmt=png&from=appmsg)

然后，还是要仔细地去查看以上操作过后的一些接口请求接口内容，看看是否存在api接口路径，如果有，就要特别留意，并发送到repeater中备用了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2J5TzbjopCiaQX3WMdkJs2uFTA0If8PcKhhxPpVlE3Ya7tYiaaw7dZ6ENA/640?wx_fmt=png&from=appmsg)

如上图，发现了两个一样的api接口 /api/checkout ，只是请求方式不一样，这很可疑，值得我们深入挖掘。先查看get方法请求该接口是什么内容：【比较明显的是该get请求方法只是用来查询该商品的名字、价格还有折扣信息的】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JtibJEibZ4PlzCYo4u0vBGYX5ibN8D7VhSCR3Icou1Ficbmf6kW2DpvqeyQ/640?wx_fmt=png&from=appmsg)

我们继续，接下来看POST请求方式下，该接口又做了哪些事情：【从请求参数上来看，就是将商品ID的还有要添加到购物车的商品数量，发起提交到服务器请求】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JwLiankOGtXpzmkAW9LXeHKd2WZ5icYG9VM9P9icIPh40ibGX1BynJpAZug/640?wx_fmt=png&from=appmsg)

重要的点来了，因为我们看到前面 GET 请求该接口的响应内容中，是有返回商品折扣参数及值的内容的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JYGcdpuEcLRevGYjrt5rFd42mRIAgJVPY6HFGiaPByjKcSptXYW4VCEQ/640?wx_fmt=png&from=appmsg)

这样的话，结合上一节的“自动赋值”理论内容，我们就可以大胆猜测在这个POST 请求方式中，是不是可以直接将这个隐藏的自动补全折扣（percentage）参数放入请求参数中，并将提交商品的折扣设置为100，发现能够正常提交数据到服务器中，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0fZEQI0QdNRn1Yzxc9cB2JkicribicYbBQq4A8xeAGHzyJNn2QUbBjp40IG9He3ViaNKP9jGY1ibibp9lw/640?wx_fmt=png&from=appmsg)

提交后，我们再到系统的购物车中查看我们添加的商品，就发现刚添加的商品折扣为100%，直接实现了0元购。

关于api接口自动补全参数的挖掘和利用的实际操作，今天就先给大家演示到这里。关于api接口漏洞，远不止这一块哦，更多内容，这边会持续输出。感兴趣的话，别忘了点个关注~

如果以上内容对你有用或无用，欢迎点赞或留言建议，这边会不断改进的哈。

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