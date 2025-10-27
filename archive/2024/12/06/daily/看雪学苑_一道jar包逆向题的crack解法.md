---
title: 一道jar包逆向题的crack解法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585394&idx=1&sn=4757ca6eff63ddc474a03bdeecb280b6&chksm=b18c39b886fbb0ae4bd2b5c3825ee9622d0d19ec352e6cf83fc4cd014bb09e2b18212f182671&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-06
fetch_date: 2025-10-06T19:39:07.895242
---

# 一道jar包逆向题的crack解法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nVkDcLoMFibRFvuny22JJ10TwWAwiakmb9rr01LItAichxtCBxGtzYSFfg/0?wx_fmt=jpeg)

# 一道jar包逆向题的crack解法

Jtian

看雪学苑

这道题目是2024网鼎杯玄武组的REVERSE02，从答题率来看算是简单题了（难的也不会），不过作为一个Java的小游戏题目，感觉还是挺有意思的。关于这道题目，目前网上的WriteUP提到了两种解法，一种是硬逆，解AES，另一种是非预期解，直接可以在class文件中找到flag明文字符串。这里提出了第三种解法，crack时间限制，把5秒超时改为5000秒超时，因为游戏不难，进而很容易通关获得flag。具体操作过程如下。

启动游戏，提示得20分就可以获得flag，但是有时间限制，只有5秒。

```
java --module-path E:\program\javafx-sdk-17.0.13\lib --add-modules javafx.controls,javafx.fxml -jar WhackAMoleGame_flag1.jar
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nCCfeof8PUArPaHcm8Node2YCFZibgDBEcfKr0FK8D5TVpibHvoPyNR6w/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nkzbeENqmgkDPkdkkGE5Jr40kavoQ7L9OxTIw1hwictibM6WmmnhPGYzw/640?wx_fmt=other&from=appmsg)

对编程熟悉的话，推测5秒在反编译代码中大概就是个5或者5000的整数，并且应该和时间函数或类有关。使用recaf打开WhackAMoleGame\_flag1.jar，可以在startGame函数中看到相关代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nnYibqvzPH7oQbpIFMfeiaLcZTLEep1BgT4wWOePVrv020DfKlmLrniaEw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1naXfXiacNLKsKjySbEuwkFyib45dzhcsTA3McVKVth3rvmqribcU7NdB7g/640?wx_fmt=other&from=appmsg)

接下来开始crack，在startGame函数名上右击，选择“Edit with assembler”，把5000改成5000000，然后Ctrl+S保存，最后"File->Export program"导出为patched.jar。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1noCft06aFkFOGhzS8qByRmzWvjxMlicpNxP568L0jMqYerPWpxKekOhQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nqtS4mVSHHep0tj96XJOBF912ib06iaST9fYF1acLSp4mn1FkkY8DV4Qw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nqtS4mVSHHep0tj96XJOBF912ib06iaST9fYF1acLSp4mn1FkkY8DV4Qw/640?wx_fmt=other&from=appmsg)

Ctrl+S保存，然后导出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nMdml50L0sUGI4mgQ6icarLnKOITDVT6SwWxErRQpXFKAjBMndz7ABXw/640?wx_fmt=other&from=appmsg)

执行patched.jar

```
java --module-path E:\program\javafx-sdk-17.0.13\lib --add-modules javafx.controls,javafx.fxml -jar patched.jar
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nVjTYjkhOiaOaTj4DZwaMiamRrwxgQy1iclpjSlXeUb0R6tw5qTvDlloLw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nqicxXUdAvlYRbicabgk1XlciampEIJlclnBGicOQ5Ck4ZRUo2ib75hPqN9Q/640?wx_fmt=other&from=appmsg)

最终获得flag，值为wdflag{yma9vtcmfJxtP33qQ2ZGY58SHMawuK2V}，通关画面上还贴心的给了“复制内容”方便复制，所以crack解法才是作者的预期解？

# 其他说明

## 1.遍历当前目录，找到含有flag字符串的文件。

```
grep -rl "flag" .
strings ./lLilllL1lIL1/I111LL1lL11/iIIilIii11.class |grep flag
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nCCjXACyicNenBy5DWU53CCFcHgE96sltdNZia2e9Im4hNic3HibzSSecaw/640?wx_fmt=other&from=appmsg)

##

## 2.JavaFX下载地址

https://gluonhq.com/products/javafx/

#

# 参考

解密AES
[https://mp.weixin.qq.com/s/g3uLQL4zhpzCaHu24vSP6A](https://mp.weixin.qq.com/s?__biz=MzU3ODc2NTg1OA==&mid=2247490957&idx=1&sn=af1881c0944754b2f3d08fc079a9b3bd&scene=21#wechat_redirect)
[https://mp.weixin.qq.com/s/ig4wPMX76FyUzJ2gTspCAA](https://mp.weixin.qq.com/s?__biz=Mzg4MjcxMTAwMQ==&mid=2247488643&idx=1&sn=3d4493dc59cb56c294e3f87fa7655e27&scene=21#wechat_redirect)
[https://mp.weixin.qq.com/s/Vt5xRUE2mshBjgJ4c-9IVg](https://mp.weixin.qq.com/s?__biz=MzA4MTE2NTAxOA==&mid=2247489107&idx=2&sn=42d4f73f334d9970b3120a0a96ff6b03&scene=21#wechat_redirect)

非预期解
[https://mp.weixin.qq.com/s/ig4wPMX76FyUzJ2gTspCAA](https://mp.weixin.qq.com/s?__biz=Mzg4MjcxMTAwMQ==&mid=2247488643&idx=1&sn=3d4493dc59cb56c294e3f87fa7655e27&scene=21#wechat_redirect)

recaf操作
https://github.com/Col-E/Recaf/releases
https://bbs.kanxue.com/thread-270972.htm

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nkamuHHOurHvyWGa24tWrk7EickCv2zPa4TAR9OqJarFurMXEIm8M0bA/640?wx_fmt=png&from=appmsg)

看雪ID：Jtian

*https://bbs.kanxue.com/user-home-598931.htm*

\*本文为看雪论坛优秀文章，由 Jtian 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=21#wechat_redirect)

4、[关于安卓注入几种方式的讨论，开源注入模块实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579138&idx=1&sn=fef09513ae9f594e68a503f69a312f4f&chksm=b18dc04886fa495e440990cd2dbddb24693452562e53bd8cb565063ddee921b7e288477f4eea&scene=21#wechat_redirect)

5、[2024年KCTF水泊梁山-反混淆](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579017&idx=2&sn=a97dacde8a6c913108999da8a96a667f&chksm=b18dc0c386fa49d57ce9f0ce6923690d6eb8efb3ccb8032e8c6b923184af3dd29b1b4471f9a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1n9miaYjLn9TpM7hcwibjsyGIg90ttzNepeW6Kiaiae47A6Ak399gg7mv12Q/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1n9miaYjLn9TpM7hcwibjsyGIg90ttzNepeW6Kiaiae47A6Ak399gg7mv12Q/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1n9miaYjLn9TpM7hcwibjsyGIg90ttzNepeW6Kiaiae47A6Ak399gg7mv12Q/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hcaxica3dxibiaReqiciaWb8b1nveiapHXibG8Poz2uuCF4zHy29t239YA1LxQ9fKS6OhItR7FOvLCII58Q/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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