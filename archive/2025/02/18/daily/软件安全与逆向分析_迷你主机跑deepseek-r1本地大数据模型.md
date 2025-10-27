---
title: 迷你主机跑deepseek-r1本地大数据模型
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484767&idx=1&sn=ce02d9b6edd0ec91afa516ff81b4028d&chksm=fcdd0552cbaa8c44450d9a01e1c3149bff858ef9e30988241b66093e5397e73a84ef0f081dbf&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2025-02-18
fetch_date: 2025-10-06T20:39:55.460104
---

# 迷你主机跑deepseek-r1本地大数据模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnbKMOL2weB0iaxoNtuqWnmBBs84ibKCg0jNwpfVVrLJmicPHyZhFPwNOY5gR4bwZKejUr9OUo1GXu1JA/0?wx_fmt=jpeg)

# 迷你主机跑deepseek-r1本地大数据模型

非虫

软件安全与逆向分析

现在开源LLM如此之火，我也跟着玩了一把。测试了m4 pro mac mini与8845hs迷你主机。

以deepseek-r1为例，使用最简单的ollama方式来部署。经过测试，m4 pro跑32b版本有点慢，跑14b还行。8845迷你主机可以自己单独上内存与oculink外置显示，不上的话，我用64g内存也是可以跑的,780m的显卡跑7b与14b都还可以，32b也慢了一点，不过整体比m4要快一点。

配置方法，在mac上执行下面命令安装LLM管理工具：

```
brew install ollama
```

在windows上下载exe安装完启动ollama程序就算准备好了。接着执行：

```
ollama startollama pull deepseek-r1:14bollama run deepseek-r1:34b --verbose
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbKMOL2weB0iaxoNtuqWnmBBSRS6R76xS52kk6GIMPAmaL6G9REKSvOKupTZy7n1dUf54v9ibTSNBow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbKMOL2weB0iaxoNtuqWnmBBJbpuzvib2xNPez50Yg1gxiaIXcQ7YtibTxiap6PFsCmMaHwugib0vsKJiaxA/640?wx_fmt=png&from=appmsg)

成功后，会给出命令提示符状态，输入提问即可：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbKMOL2weB0iaxoNtuqWnmBB9Micz2c5qVBFJBv2DiaVQTJbgzVEC09g1njlDULdShPkt0ktELXzRZlQ/640?wx_fmt=png&from=appmsg)

完整的系统配置指南可以参考这里的流程介绍：

https://github.com/feicong/re-docs

下面我给出了JD上面我用到的设备官方购买链接，想玩玩的可以直接跳转购买，欢迎大家进群交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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