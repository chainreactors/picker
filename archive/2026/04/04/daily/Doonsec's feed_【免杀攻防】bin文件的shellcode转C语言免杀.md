---
title: 【免杀攻防】bin文件的shellcode转C语言免杀
url: https://mp.weixin.qq.com/s/6A60o5kSesL-tApbl8eeHA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:04.065128
---

# 【免杀攻防】bin文件的shellcode转C语言免杀

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kibYIhwqxpu9Cib7Qiaf4QmTEbR4KrCF0oPjqjhGWmyOQD9zUKbJhKVQJXMvqpBnHibicyhpicdkAiayq95NFExibbHic4J5jBfTWZu29WibhJQet3Uick/0?wx_fmt=jpeg)

# 【免杀攻防】bin文件的shellcode转C语言免杀

原创

平凡在修行
平凡在修行

平凡在修行

![]()

在小说阅读器中沉浸阅读

**「到底要怎样努力，才能超脱那芸芸众生的苦海」**

## **「免责声明」**

本公众号分享的所有文章仅用于信息防御技术研究，切勿用于其他用途。由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

## **「bin文件的shellcode转C语言免杀」**

msf生成32位的弹计算器的bin格式文件

![](https://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpu9fI2KyWy4xzHKSKrpL3ialnVCrZpdiaFE8Mbp23SU9N8wx69UwZWVfx2SsbgL2WqPSwbR1lqHy9YhMDhrR7B481nR7csF7xfIGE/640?wx_fmt=png&from=appmsg)

使用 python 将 生成的 32位的弹计算器的bin格式文件进行转换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpuicZqj8BH7ZcyF4DFeibo1Bbbe3hD0hKdYnevKrnYkZ5WgylGfGIG8LibeibMOloBzM5BP4zYTF9jJTEm2MODVhkibyXTnabIa7kKQM/640?wx_fmt=png&from=appmsg)

在C语言中对字符串的定义是使用char buf[]="\x00\x00..."的格式，会把shellcode存放在数据段，buf是个指针，导出的shellcode是代码段，所以不会一起导出数据。使用char buf={'\x00','\x00',....}的格式会存放在代码段，会随着导出shellcode一起导出。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuicHvJgOCgAs1ddRTEagDKtcuicAd3zDpIY1wicYslUgCWBBc0HRB1qBibD8lFUkJavYkspibIT42DAtqKU6Nx8Csdn6NmIW0NvFWsE/0?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuicHvJgOCgAs1ddRTEagDKtcuicAd3zDpIY1wicYslUgCWBBc0HRB1qBibD8lFUkJavYkspibIT42DAtqKU6Nx8Csdn6NmIW0NvFWsE/0?wx_fmt=png)

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