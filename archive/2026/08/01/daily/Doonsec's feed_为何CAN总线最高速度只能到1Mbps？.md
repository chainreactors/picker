---
title: 为何CAN总线最高速度只能到1Mbps？
url: https://mp.weixin.qq.com/s/1Hw_67hWOCZRukmwgcDbSg
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:08:53.420370
---

# 为何CAN总线最高速度只能到1Mbps？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAbibIb4GCuSchSUADwYA9wygnStuXYuo3VRbsTHMDpooVKhrpadlJUcWeRDq6lupOcHaC4bf6AUlelk914Vx07DvPz2vjZaQUY/0?wx_fmt=jpeg)

# 为何CAN总线最高速度只能到1Mbps？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575811&idx=2&sn=55c140dd2df955df133478463dd59bbf&scene=21#wechat_redirect)

**01**

**物理定律限制**

保证CAN通信安全最大的特点是它的发送错误自监测要求：发送器将要发送的位电平与总线上检测到的位电平进行比较。如下图绿色字。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKeJtjpicBxdZW7yJadWIK5NwUdicvzwRLEyFeIycBtBBqOqCADnqOlfjg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

这使得所有发送回路必须是带反馈功能的。即发送节点发出一个数据位，传播到最远的接收节点，等待接收节点应答一个数据位，再传播到发送端。电信号在这个回路上传播是有时间的。物理学研究结果，铜线中的电信号传播速度大约为2.310(8次方)m/s。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKNTFYWeZSvb48h0jvpdGFEOdrG37l4s2WFZibb9djcRiaNfgKfvTzD58A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

那么，对于40米长的电缆，来回有5ns/m × 40m × 2 = 400ns\*的延迟，加上\*\*\*1.25倍\*\*\*的设计余量，就是\*\*400ns1.25=500ns\*\*\*，也就是最大2Mbps。如果是20米长的电缆，最大4Mbps。但是电缆太短，通信系统的空间规模就越小。考虑CAN的使用环境，最大按40ms设计。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKMNBluepI0OzkCLfGEF8PFdqUGaWaaDwwkSdBfbr05gBFojmoQaOLBQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**02**

**时钟源振荡器频率限制**

按设计tbit=8Tq,最小的PSEG1=2, PSEG2=2, PTS=4tbit计算，如果最大波特率1MHz, 振荡器频率≥8×1MHz= 8MHz。如果最大波特率2MHz, 振荡器频率≥8×2MHz=16MHz。可见，波特率要求越高，时钟源振荡器频率也要越高。

**03**

**时钟源振荡器频率误差的限制**

一项新技术能否普及，成本是很关键的因素。为了节省线缆成本，CAN通信采用异步传输方式，时钟信号由网络上每个ECU自己承担。为了保证收发时序的同步，所有时钟信号的频率误差必须在一定范围内。理论上，通信速率越高，每个位的时间越短，则时钟频率也要越高，且误差越小。首先，CAN在设计之初就排除了频率误差较大的RC振荡器（误差在1%以上）。剩下的有陶瓷谐振器和晶体谐振器（俗称晶振），晶振的频率误差更低但是价格也贵。

“石英晶体振荡器的核心元件是石英晶体谐振器。陶瓷振荡器的核心元件是陶瓷谐振器。石英晶体谐振器的频率稳定度高达百万分之几（ppm），做成振荡器其频率稳定度可达-6量级。如果是温补振荡器也可达-7量级。如果是恒温振荡器可做到-8~-9量级，多层恒温振荡器更可达到-9量级。做为系统时钟，可以达到几百年不差一秒。用作导弹或航天中，可做到飞行上万公里，误差不到一米。而陶瓷谐振器频率稳定度只有千分之几。与石英晶体谐振器比显然差了很多。但陶瓷谐振器的特点是起振容易，且价格低廉。用在对时钟要求不太高的电路中比石英晶体谐振器在性价比上有优势。”

根据ISO11898-1-2003标准描述，选用N位填充时，频率误差df公式如下，式1)，分母中的13意思是选择5位填充，2\*(N+1)+1=2\*(5+1)+1。

可见填充位的位数N越大，对振荡器的精度要求越高。

分析一下：设计tbit=8Tq,最小的PSEG1=2, PSEG2=2, PTS=4,带入公式1，df≤2/(2\*(13\*8-2)=0.98%=9800ppm。

可见，对于这个误差陶瓷谐振器完全满足。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKgsUFUKHgiboSfQT3TlIhfC2var6TI0lfG4mI3XW0oK35SKwhufvjGBA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**04**

**总线传输延迟的考虑**

在第一个原因里只考虑了总线上信号的传播延迟，事实上发送单元，接收单元的芯片处理信号本身也要时间。则按照单程

5ns/m × 40m = 200ns的时间还不够。按照传播延迟通常有2个Tq考虑，tbit=8Tq,最小的PSEG1=2, PSEG2=2, PTS=4,
对于1Mbps, Tq=125us, 2Tq=250us
对于2Mbps, Tq=62.5us,2Tq=125us
显然，1MHz的波特率能覆盖住这个传输延迟时间。

以下，ISO11898-5-2007标准限制了这个最大时间是255ns。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKFhSib7Z53fKyxK2nuYBxMbXlNqRO0AbFuKCicu8XTenhTLxEhN7VJrOw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicKEBjdIJwK1RrLXceeknuKWic1tiaPNRfdVGfpkoia9sUGpvSWhs3VQQYelhagqXTU5XBvFxWA25icqQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

弄明白了嘛，以上四个原因说明了，CAN2.0 最大波特率是1Mbps

来：汽车电子嵌入式

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575811&idx=2&sn=55c140dd2df955df133478463dd59bbf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chks...