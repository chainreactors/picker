---
title: mac的arm64下编译debug版mettle与metasploit framework源码联调
url: https://mp.weixin.qq.com/s/p7BgOVPIzo5LioZTA_HnOg
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:04.531637
---

# mac的arm64下编译debug版mettle与metasploit framework源码联调

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBntMQXxBMUPibdRiaRPVdCY7X8toZBGQHRWibHLqv6XnQ0ibA9hyTAHJ9pTbWjIJnoWgqZDAl6Jz7QckWfRSd2swZ6Kiad0FBwMaPX6c/0?wx_fmt=jpeg)

# mac的arm64下编译debug版mettle与metasploit framework源码联调

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

mettle源码下载与编译成debug版本，mac的arm64下编译有一些源码需要调整，同时环境也有不少坑，详细了解扫后面码加微信。

编译成功如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntpJicTXZ9lK7WZXeVp0XnH5NNWswLEiboTUKaOTTRKXI9uNrGFq9vLcUXvYpdhkX6dDhAaXq2VjqMXtXYgrk0qFLiavpknEGZf1g/640?wx_fmt=png&from=appmsg)

启动mettle，为了方便直接用xcode启动调试，先断到main入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnunzszxIakM6Zia36PFFFBIHo3JHfc2Xibj3ktf7YwwWXWIuXDdWhwBJ1Qs5Nt9p4AU2biczsM0utuZLf8Lr1trvPTspEluyVtBiak/640?wx_fmt=png&from=appmsg)

再debug方式启动msf监听起来。

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuR7PSXkyk6MypzhhZCFdHmX9otJGImd79JekMSxdJwgFmj6eoQU1e6NRuW2vlPiaEB6CUoXibyopkVJMQbAsoE4HJ5uPezOyEoM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuba5QdwmibRFm5eUpRiadMWkCGwC0ibDeiavbWEboHuc0ibBpBNR1icd4quIX9bjicf7l1fGw2qzoFqJM4DmQePOaFrzI0EnSsdicWMXo/640?wx_fmt=png&from=appmsg)

下断msf收到上线连接函数，直接断下来了如下图。

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns8IR4HkQvnHicILDbzQroFzHepwd6s85w11TEibiaS293f5D1hTFB3eS3mcKmwglRJ23DicEJdPDoDAABQWichMFYI4GqxTcTv5aRU/640?wx_fmt=png&from=appmsg)

mettle发送上线源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuVPa56dn50WmTAZ57oQpRibS54m8iajhcrnIfalGDdRAVwyzDkDrS8iasG5vv2d9vDNzme2yibyGevuLBQBEqS2Y4h0EOia4WOSrxE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntevfHaHtMB78f7BI5vPs3aHumUdHLQu53Nm7PNiaBaylpVNAnuvuEr12ZcpSKk0PJOktDRVUF8vBDicVr7Uw0diaZEOpUgTDBJ74/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnumc8qhoel0VyFH1Yx33nD28zxSE2fd42PdUaqemHQT0x1kYA6h6icW0LH68icK1caPWXDMg0aHgLZtZ7bLRE4T8FOOyHGzhUC10/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuFVvdJcd9lZohAQ1O1jAW0NmRM8T0OeRxNmoj40OY1Rr37lAGsf40ia5ibP8k19y7FicyWQic5LV4ZwgTzczq1ibF64nE5uWics6JzM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnufjCQB8EFeicUrVicpdDOqapbsuzbTqB1TjibYh4yKZpia7micibuVtvF8cRU5iagzibbncCB9oTFdaQNT8lQwpDpLw1pVZO9Ste6dibF8/640?wx_fmt=png&from=appmsg)

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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