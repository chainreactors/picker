---
title: 网页防篡改2：waf方式
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486791&idx=1&sn=a08d4635bf8d4d7fe59cb7108127c88c&chksm=fdf96652ca8eef4411a9c3d657fe2d353e0a4066e8a3ee523ec4a570d0adb79276373f1ddba5&scene=58&subscene=0#rd
source: debugeeker
date: 2022-11-21
fetch_date: 2025-10-03T23:19:48.392161
---

# 网页防篡改2：waf方式

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN1lm6t73ESLmXNGMZpiaianvicCRxI5TmFdMbRPZrWRX7VwgufYgIMibssLg/0?wx_fmt=jpeg)

# 网页防篡改2：waf方式

原创

debugeeker

奶牛安全

根据上面的论述，可以忽略cdn，可以只考虑站点本身的实现，但站点需要维护页面cache。那么，这个cache应该部署在哪里呢？

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN1M21ROhDjkU6v12nnmVnG7iaFx6yj08G9VFwJcNqEsibyxkBRcn5elsRQ/640?wx_fmt=jpeg)

​

一般站点都在webserver前面加上waf，统一管理站点所有域名的防护。如果这个cache是在waf上实现，可以有这样的优势：

1. 降低运维成本，可以统一对所有站点进行网页防篡改。
2. 提高站点响应速度，由于请求到waf直接可以收到响应，不需要在后面webserver了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN1OQbzs47s8vCf5USfynRv2cg0CdKLSR2wMqUDic44RibnibyCHYric2aXJg/640?wx_fmt=jpeg)

​

那么waf上的cache是如何同步呢？一般同步会有三种方式：

1. 请求触发。每个请求过来，如果在cache没有找到相应的响应，就去webserver同步
2. 定时触发。waf定时对所有域名统一同步，或者定时对每个域名同步，或者对单个域名单个路径同步。
3. 操作同步。运维人员对某个域名配置网页防篡改，waf对该域名同步。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN1lQAXZCicqBu2J51Fwk5bqqrR2xxg7icybSO2Anyaj8IyA1qtXQPp4Xww/640?wx_fmt=jpeg)

​

这三种方式来说，以第三种方式为最优。

1. 如果恶意用户上传了个文件，然后请求，就会把恶意文件同步到cache，网页防篡改完全不起作用。
2. 恶意文件上传了，隔一段时间还是会同步，只是留着后端webserver所在宿主机查杀恶意文件的时间，以分钟为单位。且，web发布一般不频繁，这样只会影响waf的性能。
3. 由于web发布并不频繁，用这种方式，并不会影响waf的性能，留给后端查杀恶意文件的时间非常充足，以天为单位。华为云waf就是采用这种方式。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbxuXpSoFLonBbMASLQgTibXaotcWuwwO8h0YH9rmSICjSHPabb3IibxTHATQVXERVlib8oxBx9DiaBs9A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN1g1FHVibnQd7qg3wniblFePBB5Jcdg7CUBQpOglATiaRNrab6Mg1VsQKOQ/640?wx_fmt=jpeg)

​

但是，由于waf一般不会和发布系统联动，而且也不会和后端数据库连接。所以，这个方案的劣势也是非常明显的：

1. waf无法感知web发布，且，waf负责人员和发布系统人员往往不是同一个人，使得cache并没有更新到最新版本，让用户一直请求旧版本，导致用户对企业失望，从而用户流失。
2. waf无法防护动态脚本的篡改。
3. 网页防篡改功能的不稳定可能会影响到整个waf，乃至整个站点服务断连
4. 它并没有感知恶意篡改和分辨正常更新的能力，这一块工作只能由其它工具完成。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbxHtxw7tia6YEhzrq3FCjeN18x8sMrl6MW1Bvh74awaibO8LicqWxEaHlj9R44KzE0WcDphKoLFMWnsg/640?wx_fmt=jpeg)

​

**觉得好，请关注本公众号和分享到朋友圈。麻烦点击一下右下角的“在看”。谢谢！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

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