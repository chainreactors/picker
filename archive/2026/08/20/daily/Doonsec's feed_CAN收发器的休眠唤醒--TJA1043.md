---
title: CAN收发器的休眠唤醒--TJA1043
url: https://mp.weixin.qq.com/s/KvOXIn909qeejUNmp2lYlA
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T02:59:48.862634
---

# CAN收发器的休眠唤醒--TJA1043

# CAN收发器的休眠唤醒--TJA1043

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

**01**

**引脚描述**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCoXesicGc24UxXHvNFib3qD10sjrhzZO6l7ias87vxSIHHFX1T6EZmOtESthb7MEXM9nfwRS7nSGlo5Dav3j7sDhEHeZ3Lqyns2Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAxMGqslWEVqYJKdjUc1shYObCJtBIZRkFU1sT8Dmk3olP0cItGtJH2ibsgiahMqhukNJA0sPRV7rEUEfY4TzQjUW2Iwe0baoApc/640?wx_fmt=png&from=appmsg)

**02**

**工作模式**

TJA1043 支持五种作模式。控制引脚 STB\_N 和 EN 用于选择作模式。在模式之间切换允许通过引脚 ERR\_N 访问许多诊断标志。表 4 描述了如何在模式之间切换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBlbn5q3qFxzY375PUozSKpO0OUmfCCAhogxHR1oHZcHRVoJKgsSH1rwA6DjVVkwvzm4gjlc8Mx0v8yYBXEQxa0wMH94UF6fYw/640?wx_fmt=png&from=appmsg)

**2.1 normal mode 正常模式**

在正常模式下，收发器可以通过总线线 CANH 和 CANL 发送和接收数据。差分接收器将总线线路上的模拟数据转换为数字数据，输出到引脚 RXD。总线线路上输出信号的斜率由内部控制，并以保证尽可能低的 EME 的方式进行优化。总线引脚偏置至 0.5V （通过 R）。引脚 INH 处于活动状态，因此由引脚 INH 控制的稳压器也将处于活动状态。

**2.2 Listen-only 模式-监听模式**

在 Listen-only 模式下，收发器的发射器被禁用，从而有效地提供了收发器 listen-only 功能。接收器仍会将引脚 CANH 和 CANL 上的模拟总线信号转换为数字数据，可用于引脚 RXD 的输出。与正常模式一样，总线引脚偏置为 0.5V，引脚 INH 保持有效。

**2.3 standby 模式-待机模式**

待机模式是 TJA1043 的第一级省电模式，可降低电流消耗。在 Standby 模式下，收发器无法发送或接收数据，并且低功耗接收器被激活以监控总线活动。总线引脚在接地电平上偏置（通过 R）。引脚 INH 仍然有效，因此由该引脚控制的稳压器也将有效。

引脚 RXD 和 ERR\_N 将反映任何活动的唤醒请求（前提是存在  V IO 和 V BAT）。

**2.4 go to sleep模式**

Go-to-Sleep 模式是进入 Sleep 模式的受控路由。在 Go-to-Sleep 模式下，收发器的行为与 Standby 模式相同，此外还会向收发器发出 go-to-sleep 命令。在进入睡眠模式之前，收发器将在最短保持时间 （t） 内保持 Go-to-Sleep 模式。如果引脚 STB\_N 或引脚 EN 的状态发生变化，或者在 t 过去之前设置了 Wake 标志，收发器将不会进入 Sleep 模式。

**2.5 sleep模式**

休眠模式是 TJA1043 的二级省电模式。睡眠模式通过 Go-to-Sleep 模式进入，当 Vor V 上的欠压检测时间在相关电压电平恢复之前也进入。在 Sleep 模式下，收发器的行为与 Standby 模式相同，但引脚 INH 设置为悬空。由该引脚控制的稳压器将关闭，进入引脚 V 的电流将降至最低。引脚 STB\_N、EN 和 Wake 标志可用于将节点从 Sleep 模式唤醒。

**03**

**本地唤醒和远程唤醒**

**3.1本地唤醒**

当收发器检测到本地或远程唤醒请求时，将设置 Wake 标志。当引脚 WAKE 上的逻辑电平发生变化时，会检测到本地唤醒请求，并且新电平至少保持稳定 t wake 。唤醒标志可以在 Standby mode、Go-to-Sleep 模式或 Sleep 模式下设置。设置 Wake 标志会清除UVnom 标志（欠压标志位），并且定时器 。设置后，Wake 标志状态立即在引脚 ERR\_N 和 RXD 上可用（如果 V IO and V BAT 存在）。此标志也在上电时设置，并在设置 UVnom标志或收发器进入 Normal 模式时清除。

**3.2远程唤醒（通过CAN总线）**

当在总线上检测到专用唤醒模式（在 ISO 11898-2：2016 中指定）时，TJA1043 将从待机或睡眠模式唤醒。

唤醒模式包括：

1. 一个至少持续 twake(busdom) 时间的显性电平阶段，随后
2. 一个至少持续 twake(busrec) 时间的隐性电平阶段，接着
3. 又一个至少持续 twake(busdom) 时间的显性电平阶段。

上述相位 之间分别短于 twake（busdom） 和 t wake（busrec） 的显性或隐性位将被忽略。

完整的显性-隐性-显性模式必须在 t\_wake 内接收，才能被识别为有效的唤醒模式（见图 5）。否则，内部唤醒逻辑将被重置。然后，需要重新传输完整的唤醒模式以触发唤醒事件。引脚 RXD 保持高电平，直到触发唤醒事件。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBJewWsGSic1u12n6IBGLj6hsibFdtlSIoGSbuHibTZ2X6RpMwN9sWv2Hcq1uq9ykVetaN1dxnq1N8IeQ1gsFpR6YyuHpPq8dClko/640?wx_fmt=png&from=appmsg)

如果在接收到有效的唤醒模式时发生以下任何事件，则不会在 RXD 上标记唤醒事件：

* TJA1043切换到正常模式
* 在t\_wake内未收到完整的唤醒模式
* 检测到V CC 或者 V IO欠压

总结通过CAN 总线上的显性电平（Dominant Bus）唤醒，无需本地信号。显性电平持续时间要大于t\_wake。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAlvAZUJMZLiau7LZ50ibIHTbeLXU1iaxBrK53VDbk8v4X9ViaBic4brOEvd4JjrKFQnITSPIl55jDt6zLXna2TekWt6sMaJLJYuWEc/640?wx_fmt=png&from=appmsg)

t\_wake(busdom)和t\_wake(busrec)典型值是1.75us。以500kb/s的发送速率为例，一个bit的时长是2us，那么报文中包含 0 1 0连续的三个bit就可以唤醒收发器。以上是硬件唤醒，也可以用软件验证唤醒。

**3.3 唤醒源标志**

唤醒源识别通过 Wake-up source 标志提供，该标志是在本地唤醒请求通过 WAKE 引脚设置 Wake 标志时设置的。在 Normal 模式下，可以通过 ERR\_N 引脚轮询 Wake-up source 标志（参见表 5）。此标志也在上电时设置，并在收发器离开 Normal 模式时清除。唤醒源标志只记录本地唤醒，不记录远程唤醒？

来源：CSDN博主「weixin\_46022218」

https://blog.csdn.net/weixin\_46022218/article/details/148211436

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

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

[关于涉嫌仿冒A...