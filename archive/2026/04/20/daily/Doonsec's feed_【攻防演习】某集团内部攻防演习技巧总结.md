---
title: 【攻防演习】某集团内部攻防演习技巧总结
url: https://mp.weixin.qq.com/s/FNZQixy1cejppcaVMcSsfA
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:38.268512
---

# 【攻防演习】某集团内部攻防演习技巧总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IGws6hSXN0zYthiaEs2J1kldITo92tTLeqzjCeehqNy3HFncs3EXGxmb8XtWYJ4sVhpaibmxM3VeOJia03j16VYyru8d4libiciabY6R0EZSHT2f0/0?wx_fmt=jpeg)

# 【攻防演习】某集团内部攻防演习技巧总结

原创

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

回顾以往的攻防演习中，发现一起比较经典的路线：外网信息收集=》外网打点=》Getshell=》内网渗透，改攻击路线也是较为常规而又内含一些小技巧的，需要对渗透测试有着一定的实战经验才能更好的找到该突破口。

    以下内容为历史久远的授权攻击测试，杜绝一切未授权测试！！！

一、攻击线路图

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zdBWjey4J0Q9EHvnY4bvAFwTDglmGub52f3ObbV0FzRbSuEzJGE6EjhQm3jguXgcY6jmrSKjiccFLUEylYtTxz8NHS9sBkQZz4/640?wx_fmt=png&from=appmsg)

二、信息收集

    前期通过信息收集或者各类信息，包含该站点历史存在漏洞，取用了哪些cms网站的模版、历史开放端口、ip域名绑定等事项内容，针对这些可获取到部分敏感信息，为后续“打点”提供有力保障或可持续进攻点。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0wFZia1zMGLdIXxXHIC6qfWJZU6pj3picRrdeGqeSCFYhZVcqF4EfQlGry2UkRvOicuib1dZkgTo90nc5ib9R2Yg9eM52KsyxYvt9zw/640?wx_fmt=png&from=appmsg)

三、外网“打点”

1.弱口令

    通过对前台和后台登录地址进行常规口令爆破，获取web权限。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yyp3YPenJZZlM9EpeEWT2MJQ1znuMdmwCaELibiaeTiaH71n2aL3vgQ45kPqsWUiaDeyWrMIbxibYNkZEoS0Jmg0OwStrxhL8zqB4Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zI33JoNz5gkPoZJoY924ibjy5iayEYUj1dwAPXibkRoMBqHgXJvJkMvxxS0iaH0u9vBkcib17WSj0Rj8A1UW7JbHUEHFoT0qpvzT5M/640?wx_fmt=png&from=appmsg)

2.使用目录扫描

    使用的是之前给大家分享的目录大字典进行扫描获取到的源码信息，该源码中不仅包含了目标源码，还有一些常规配置文件，与之相关的环境信息等。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0ykY9mJibed8EOMqbJkzGBolZfwH6fIGDAJqh9w6lqw4WfPabjicrib4tjY4l2AuWdMGLFdReky61px5RAu08uxJxkC9aBojMNyps/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zibdCAJTjIKib4oARc3Gj2OqrujHqpJlR5VChQSXJ2POb5VlADrDEmyT8ibc49xicMt5hz30icl3RQgxIibexZs6C4E2yxoYm42iaxibg/640?wx_fmt=png&from=appmsg)

3.代码审计获取任意文件上传接口地址

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yicUQnRGGnA76iaDQsNXu1a6tFgVl9VibibzeffpzgJQojMliagovqvtw5awQJwTXNZunq1HOt47iaMqvhqWQ4pj7FB3pWKINXhySibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0xFkfgO19nPns25zegscgRCJcyGW7MoJdLXqgicZboA3nmcpLRMMPNwH7lcRomQK5ibF1dyDnwoLMkrhggveY575TfYtLQUZSkY8/640?wx_fmt=png&from=appmsg)

4.漏洞利用进行Getshell

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zZYicfvEicSOm6vLseffLQspBibyfNO12DB5u4ugK954BoheI4wgLTelYMV2L8tIXoKrahXbbVqoeBrDKgR7uicsHSXIjNiaalgw0Q/640?wx_fmt=png&from=appmsg)

四、内网渗透

       现在就是进入快速拿分的阶段了，主要是对主机、web权限、打印机、ftp、敏感数据、数据库等内容进行全量的搜集，无线在这几样中进行循环利用，在内网中每一个信息都至关重要，有可能一个密码可以打通全段，一本内部自定义目录字典可以获取到各大系统的登录地址或直接进入管理后台......

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0yTUgemtyeFv6VnzTUKvlCx6omCkXVq5JCWkT6MwlZ64MgK3icFiag8FKSP4ogWmJc7U3DKn4g7ex78IMsBCIW7Kr2h2EvG9xQsk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0xHAAYqPbQiahWEarKdSyVWCmf46zAPIUbMCSU0VKdVVvh0ZiaUGCPPmqwyoTiatia3s1cr7eqMRwsmiaqaobibc7lL4pd0wL5CZCvP0/640?wx_fmt=png&from=appmsg)

五、大字典获取

**关注公众号后台回复“大字典****”均可获取下载链接**

**免责声明：**

 本文章仅做网络安全技术研究使用！另利用网络安全007公众号所提供的所有信息进行违法犯罪或造成任何后果及损失，均由**使用者自身承担负责**，与网络安全007公众号**无任何关系**，也不为其负任何责任，**请各位自重！**公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！**让我们一起为中国网络安全事业尽一份自己的绵薄之力！**

**●****推荐阅读**●****

******[应急响应系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2735815599062548484#wechat_redirect)******

**[未授权访问漏洞系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2740221722897186819&scene=126#wechat_redirect)**

**[Nessus漏扫神器之攻防两用](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484603&idx=1&sn=ab7748ce50815e8d9b113a0c047323a5&chksm=ea3b5a27dd4cd331ced13977630dcc1c321f9cba291f28ac17f4108fb0071df964ac5051e670&scene=21#wechat_redirect)**

******[红队如何在攻防演练中一夜暴富？](https://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247485324&idx=1&sn=b63f8d1a5eaf712297402bc2757938e3&scene=21#wechat_redirect)******

# **[浅谈Nacos漏洞之超管权限后续利用](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484671&idx=1&sn=6f268b7dd7e922b7bf7a84e5d4589651&chksm=ea3b5a63dd4cd375f19f69818b1d13a8b0d28775a7ce421673ef25a2f8172e4c83755885d2a6&scene=21#wechat_redirect)**

******[超级弱口令工具+超级字典，攻防必备！](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484816&idx=1&sn=db1111e7c521d4be5c52a373e4a8e228&chksm=ea3b5b0cdd4cd21ab4dfe20b60dbe88c010d376b6cb4be6d993433332e188e24ef6fc77e0d01&scene=21#wechat_redirect)******

********[记某APP服务端渗透测试实战GetShell](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484519&idx=1&sn=8a4322ac773f4147589a0a1b9dc9d3c2&chksm=ea3b5afbdd4cd3edabc9c553bbb5566f2401b9fabc05505c43a7d9a80a9965ec23ea6fbcba96&scene=21#wechat_redirect)********

******[日常实战渗透小技巧，掌握就无需担心漏洞产出为零！](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484957&idx=1&sn=a79f132cc4a21f4776be5550adf273e7&chksm=ea3b5881dd4cd197fea3594bb21397a5a943378eefd251033bacd8ccbaf203847af66117cba7&scene=21#wechat_redirect)******

********[实战|某网站未授权访问=》数据库权限=》服务器权限](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484547&idx=1&sn=541a371ace13e94aa87cf87f5f2e532b&chksm=ea3b5a1fdd4cd30923c52bcb6ea27c19c502f0eea80e5d84d96c1c6021c7c6f98292d2729148&scene=21#wechat_redirect)********

****[全方位揭秘：50多种横向渗透提权终极技巧，一篇文章彻底掌握！](https://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247485311&idx=1&sn=3c9c2f5fec222438aec1fcb543bf0c1e&scene=21#wechat_redirect)****

---

写作不易，分享快乐

期待你的 **分享**●**点赞●在看**●关注**●收藏******

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0z6Bd8LS7WQcGZf5boy4b9Lq0CkLh1ib2RjiaCK7ia3yk2k2rFQBFGVzFicJ1mKXgSDLQFcNf8csNich0X9tc0gGBia4G9xFTRNETKNU/640?wx_fmt=png&from=appmsg)

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