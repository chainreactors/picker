---
title: 记录一次逆向实战
url: https://mp.weixin.qq.com/s/7bWoWh6Fwj-HNeMnYKu6LQ
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:56.167990
---

# 记录一次逆向实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmRmyfvY1c0S8sWjnJic4qPPxSG88bgKzhwLocg3cr3jpeZQAxFib0JqAfGFg9uUI5MXdpmAvaoo5JAiaOmIo7r7Tcffeia8KaGf8o/0?wx_fmt=jpeg)

# 记录一次逆向实战

原创

studying-egg
studying-egg

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

上午我们小队的WEB师傅提到需要一个渗透工具，但要激活码，秉持着“能省就省”的原则，我们小队把该工具破解了，这里记录一下学习过程。

## 免责申明

下面的内容仅供学习交流，请勿用于非法用途

## 学习内容

用`DIE`查，发现是`go`语言编写的，但是好像没删符号表，所以函数名都是可读的

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlokea7DyBrREYojX65Q0tWFNPic8iaIsyzItCSBdZb3s7MenGCU1GLptUNXv8yx7xydoSaTtibtg7LDgricOzyfjcT6c4XaSAaYmY/640?wx_fmt=png&from=appmsg)

这里找到了验证逻辑

一开始想直接修改`jz`，但发现好像真正的循环校验逻辑存在于`main_authCheck`中，我们通过运行程序，随便输入一些内容，可以发现出现`密钥格式错误`的字段

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkvd11Y7c3XwOoDlVzic7FZ2b1xxVicLiaNibDwBx2K3P48qRBWPVy4vc1eOMHhWZibMtALOoJHiaBKYBZYaOgu3QvdMF8ibDib8Zd3Rbo/640?wx_fmt=png&from=appmsg)

通过字符串定位到关键位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnBPRn4WbVLlu81pGgRV3jLzew8ibuzhibibenNTBd5Vo59ia3HB2pOtuqyCoyCHsEsJE82rHMibECtF5N5ZY72a7LQ7F1Xf8UJFPCA/640?wx_fmt=png&from=appmsg)

这里输入的长度会放到`rbx`寄存器里面，与`0x40`进行比较，说明输入的长度为64位

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmbBWTvkPvC281N5fhmPQILEGiazHaTSDXK1Uib0ujgXlQNd60BtsRFO7qGmLZRGtdzw5HYwXUquPOoFERTKIIy5cduk51XbHGao/640?wx_fmt=png&from=appmsg)

这里再定位到`密钥验证失败`这个字符串中

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rncWuWChia9ngO81jhYHVp3SblqibJmA65F0x7RaKUibhVDX05JkXT51niczWO6icVQrqfvOdIJBticK3mxYCdFfWAQeXQiaXUltGlmTY/640?wx_fmt=png&from=appmsg)

根据控制流判断出这里存在两个条件，我们反编译一下

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rnJ6giawZjfm8bm1dku8W0NKUtm2jSDpWKa7ianxkPlviaHrw9vLGwURbLggNEkeMUVKdPmictGOLKZkMFcJAENsib1rYcSIpLpYLhI/640?wx_fmt=png&from=appmsg)

基本可以判断出事这里个并列的比较条件 这里我们也不用让这个条件成立（这里牵扯到加密算法，需要花一些精力去搞），直接改判断条件将`jz`换成`jnz`，`jnz`换成`jz`

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkwrYe709YgToYRwPiaaLz3eXDsaHuqbuXEOqmau6yH2A28YicA1F9pc0DmVMxVgE5rgQ1rJ557Z9icaib0DPBwdPO7FmvW0JF0ASk/640?wx_fmt=png&from=appmsg)

这里我的`IDA`好像有点问题，没有办法修改源文件，只能修改`IDA`自身的数据库，这里可以尝试用`010editor`进行修改

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rk21rtlkwyqchW6aV5Zcglz6LupwIvZlhq4R9ic3ew8YpLf3qnAiasabwSuvTJkKVFQmpS87FaXOOAlb6cMsDU9W1gyzfWH3gsbQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rl3cniasQicjbw42zHdSKwWTyw8yx46W99XBkyYHPy3FNMjI0dtECtE9ibS15UJ6JnicPWhX1TJVxdbCdPfxOcMPsStennckKCr8Wc/640?wx_fmt=png&from=appmsg)

改完之后程序运行，程序会出现闪退的情况，程序可能在运行时会校验自身逻辑是否被修改，这里尝试把所有`os.exit`函数全部`nop`掉

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmMprlqwjj7NsM3mLB50xCvEGcuKEOAgvfmE371bfguW1txMtOEQRjzgZFptB4CYhfSrZCAAV5mJJ9q2OdrXc0lork4JKumnmQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rl2WcHz9br6icrkFYpDasQvD12gkKtMiavIafjZtsTM50Sib3ySkZAc6IRpNV8Ctib8FbnRZXRDVa1RtOR2eoG5ZbW1OKRFYia02icjQ/640?wx_fmt=png&from=appmsg)

保存之后在命令行中运行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnpuGJYOTQlIOfRCTiboIc2uIDpY55PlCZxzLGGpHveF1HEpEStsiaLvNQUzjouNINMo2ziboKFHOjgAk8GLzIYcwnOD9Gic2ojCT8/640?wx_fmt=png&from=appmsg)后来重新分析了一下，真正的退出点就在验证函数后面，由参数`v0`决定

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlWaDIhfVaWSuCbCa5VnoGn4sNARqU617Zy3Y8ic4GIppkEO9bO2VIAGg4TswMVyyglgmZSK263C44sSPbklg8m2ClUTNIaB1S8/640?wx_fmt=png&from=appmsg)

## 结语

自我感觉思路比较“野”，不像正规军（本来也不是😐），希望各位师傅能提供一些更好的方法

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

正在思考ing

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

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