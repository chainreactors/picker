---
title: 【域攻防】约束性委派的利用
url: https://mp.weixin.qq.com/s/lC9M_e07qoqQ1MKJsobWtA
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:59.317239
---

# 【域攻防】约束性委派的利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kibYIhwqxpuicKFI2qnQBJA3I3ZSYtYb7l5kNFBf06BkIQS24SgYt9Zfqv8MqOLQPuW7gOeqyj3p2SGhiaMxramGUjOibK9tA7mbU8Q9x0Paw9M/0?wx_fmt=jpeg)

# 【域攻防】约束性委派的利用

原创

平凡在修行
平凡在修行

平凡在修行

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**「别混日子了，小心让日子把你们给混了」**

## **「免责声明」**

本公众号分享的所有文章仅用于信息防御技术研究，切勿用于其他用途。由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

## **「约束性委派的利用」**

### **「原理」**

非约束性委派被委派的机器会直接得到发布委派的用户的TGT，是十分不安全的，因此微软推出了约束性委派，还扩充kerberos协议，添加了s4u2self与s4u2proxy协议，以增加安全性。这两个协议的具体细节可以查看:windows中关于委派(delegation)的理解这篇文章。下面我简述一下约束性委派的过程，假设有这么一种情况，用户A委派service1去访问service2,那么大概的访问过程如下：

```
用户A访问service1。
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuibzo4gpeoAheasNMaTujDndmic8zpHUOoMz9t6C27aKO52E7zLVgvhKJn3vibqMxTibjZtbvDO7dliao6ickhY0hn0MnaayZckWTe98/0?wx_fmt=png)

平凡在修行

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuibzo4gpeoAheasNMaTujDndmic8zpHUOoMz9t6C27aKO52E7zLVgvhKJn3vibqMxTibjZtbvDO7dliao6ickhY0hn0MnaayZckWTe98/0?wx_fmt=png)

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