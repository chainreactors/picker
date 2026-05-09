---
title: 某知名证书站简单挖掘
url: https://mp.weixin.qq.com/s/isdzxW0gg4kod65W_iGHGg
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:04:12.580867
---

# 某知名证书站简单挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhjdxia1eianEr79CgFZiaicfXgGeibDuC6tddJuNg1drhsUWnN9cCeAQjyvDvfkI9aWZ92kGku9icNc4QCJTwGL9OnIvNjc9tAtjURdo/0?wx_fmt=jpeg)

# 某知名证书站简单挖掘

原创

魔术师
魔术师

B1ackTide安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

有一次闲着无聊，想搞一本证书玩玩

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhia6FYdCM4dgibY651EfMCETRR9H9pAOEpUKAyqc0s0PJbqicnlAHrQOCPhc4OvdJcBvASp9N1SIb1n07NkAFVFh3ibj57GFEiaEIic0/640?wx_fmt=jpeg)

看到如下界面，结果通过目录发现存在

xxx/xlicense

大家都知道license是用来认证的

这时候我试着去访问它状态

![](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhjRzgia0ntk6omkD71ibyFhV3rpeRDqLIMSmyFZlh4K81UFvSqtLqpv6sqhg0D6bWMnzibY6WTicvCEAWSCISNA2IRcLGxYIOuf1XI/640?wx_fmt=jpeg)

没错，是开启的

然后当时主播大胆了一点，因为它是有个签名算法的，想着去关一下它

于是就发送随机license试试

license=xxx

为什么是随机，因为后端只做了格式/长度简单校验，没做加密签名+设备指纹绑定的强校验

没想到直接关闭了

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhiaDmicsdu11dFzMvfI2wYF8pVFpycZzzT6MM5CLDYCcPIicc0xzfnL3WVwlz5Iib6QqXkRicgGo0icUfiaK4CB1YPwcpJVnXApRbcib8A/640?wx_fmt=jpeg)

此时密码不管正不正确都登不进去

吓得主播只能去请罪

还好，有惊无险

最后拿下三分，得吃

但是最后还是奉劝各位，别随便去修改，这次是主播无意间修改并及时调整报备才化险为夷，不是每个都这么大度的，特别是企业那些

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

B1ackTide安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

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