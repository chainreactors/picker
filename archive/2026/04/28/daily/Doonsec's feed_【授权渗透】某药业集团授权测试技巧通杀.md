---
title: 【授权渗透】某药业集团授权测试技巧通杀
url: https://mp.weixin.qq.com/s/b23KIHfmUzXHO6ahWW3Rww
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:10:10.651123
---

# 【授权渗透】某药业集团授权测试技巧通杀

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IGws6hSXN0xWYXAPmlFvKI1Ujhb8ZFamMqncGRicKqDkSfEDHFibtVWLPlNHAbr47mNjxUAGxNfotG8RoVxHE9Bib76qwSzw7SDQ3FNxP3XC78/0?wx_fmt=jpeg)

# 【授权渗透】某药业集团授权测试技巧通杀

原创

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前段不久的时间中，忙碌于大大小小的渗透测试中，每次的渗透测试好像都是按照模版按部就班，做过安服的师傅们就知道了，每次下来一个任务，基本就是打开渗透测试模版走一遍，然后功能走一遍，再接着就是随心所遇的看看基本就收工了，而且大多数的授权测试都是给到相应的测试账号以及测试权限，这期间就会不经意间漏掉一些隐藏小彩蛋......

一、登录框逻辑绕过

    按照往常一样，每天上班就是接收新的任务指示，然后打开burp进行一顿梭哈，万变不离其中，开头一个登录框.

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zdtcL1e4vOicWo0ibxlrLGvia2ApxhABPyeoTqlwdvH4DCqvO7WXIqFo5STq3dyJHukzB2C2OSjsDywOIAnxdRsCWb4wKQjgu8bQ/640?wx_fmt=png&from=appmsg)

     紧接着输入特定的账号密码进入进行渗透测试，密码错误的时候你们会想着改哪些地方呢？code？还是msg？是改成1,2或者3？

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zKwhuibbLoia3YiaWbZH60kJcfnqWia08kicMSCAQy4iaIgQze2F55F7WvSVWG1T1UDnMicoAE62sUGAJEAHSFebRLtic5iac5bqkZyJNs/640?wx_fmt=png&from=appmsg)

    都不是，在这里需要更改code为200即可绕过验证，是不是很神奇？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0xMNrrAKfWGrY1dS4v7YXuurh2nry86ibZ8efT3Nc5YhmMkMDMBEKlpFX1FfDXX7aP3X5apPORnZ7nwBcgiaicxTsOIanwicG9iahIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zjNBmzEMJh4OiaQI6sFQ0gGwMLlUWeTsfmhbYk0TWg9U3RhAsULlOoddq3dmWpQxaL26Ox2hoXW3YibYfLqRdia9BkjA8pKggKTw/640?wx_fmt=png&from=appmsg)

    正常逻辑这里的code要么是1,2或者3，分别代表的是用户不存在，密码错误，异常；但是这里输入200却能直接进入系统，说明这里存在一定的代码逻辑错误，有以下猜想：

1.代码开发过程预留了直通通道，添加了预留条件；

2.代码本身存在一定的逻辑问题，只要code不包含1，2，3这三种状态跳出逻辑限定绕过进入后台；

     接着，嗯，，就是批量将授权地址的所有登录接口都按照这个方法进行测试了一遍，发现都存在这样的问题，这就给所有系统搞了个高危，马上就可以下班了......

二、刷新登录状态=》进入后台

  依旧开局一个登录框

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yFnuUBBKlFYD2ialyrfzt7ZEfGrIPf31FUlGJtrA2Dib3ibdamxPW2J35RDpZ1Vw6ickUDAwvfGQ6bTGIIT5tgTBlDXiaQY0ASnte4/640?wx_fmt=png&from=appmsg)

  不知道你们发现没有，我们在正常的访问登录界面的时候基本都是login.html、login.action、Login等都是与登录有关的，而这里确实exit.action，这时候我们换种思路，直接访问Login.action试试

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zDibSmyFxdGkqqoXGHNyYFUibAicNhSNV8IMHKkZ4YSiaXSMHRytzAYJ2Ut65KQQqNXWWW4eQbHBtJIaqTcgGH9zT0BupsKib2BqWI/640?wx_fmt=png&from=appmsg)

  没错，你真的没有看错，这直接返回成功的标志，这时候我们再去访问根目录，直接进入了系统

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0xI3sBO0Yd7z9PrbMYHgK5t3iaCEZXibrTVEfWWvn56Xl6CiaT7SpjsvyAzhllplibrWPxhHmboM2OkVsywugCj5eoLwv6vc52xHUU/640?wx_fmt=png&from=appmsg)

也就是这一个小细节，直接后面的类似系统也通过这种方式直接拿到后台管理权限。

**免责声明：**

 本文章仅做网络安全技术研究使用！另利用网络安全007公众号所提供的所有信息进行违法犯罪或造成任何后果及损失，均由**使用者自身承担负责**，与网络安全007公众号**无任何关系**，也不为其负任何责任，**请各位自重！**公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！**让我们一起为中国网络安全事业尽一份自己的绵薄之力！**

---推荐阅读---

[攻防演习系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4480577090483748870#wechat_redirect)

[渗透技术文章系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483666897053253633#wechat_redirect)

[未授权漏洞系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483456618323345413#wechat_redirect)

[HW专项系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483461171911426059#wechat_redirect)

[应急响应系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2735815599062548484#wechat_redirect)

[工具推荐系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483471065368592394#wechat_redirect)

写作不易，分享快乐

期待你的 **分享**●**点赞●在看**●关注**●收藏******

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yC4UvVZTh0GWblmLs0dtN1Sfnf88e3vkpokovgdsQAfPI16CnM3C7S6uNVNGHtnsiaFU1via2Bibo92ria29FVIMstgj6wQDg9XbI/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

网络安全007

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

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