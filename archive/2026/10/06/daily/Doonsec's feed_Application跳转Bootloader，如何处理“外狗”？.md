---
title: Application跳转Bootloader，如何处理“外狗”？
url: https://mp.weixin.qq.com/s/R32K_YqdniC9CohSVZbAEQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:05.013330
---

# Application跳转Bootloader，如何处理“外狗”？

# Application跳转Bootloader，如何处理“外狗”？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于开心果 Need Car
，作者开心果 Need Car

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7xmZWjMxkpzia4Ft2qUbKVib3waicn3vUKRjoL8iaKrC191A/0)

**开心果 Need Car**
.

号主：开心果 Need Car，主要从事汽车Autosar开发，公众号主要分享 通信、诊断、存储、网络管理、标定、Bootloader等工程开发问题。致力于将学到的知识，分享给更多的Autosar从业者，努力解答一线开发工程师的困顿！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

提到“看门狗”（WatchDog），我们自然就和功能安全挂上钩。或者说，看门狗属于功能安全的范围，当系统因故障（eg：程序死循环、硬件异常等）导致“卡死”时，看门狗主动触发复位（Reset）或安全响应机制，强制系统恢复至可控状态。如果细分看门狗，又可分为内狗和外狗，示意如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vyyibkoOxMS3CiclbkN87ykYY555TfnB6aBzdIVUianGcHHW0HkNs03g25V93af5NfdiawDNmzbnC7MIw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**01**

**Application和Bootloader**

对于一块芯片，在软件设计之初，会考虑不同进程之间的内存划分。这里的进程包括：信息安全的Bootloader（如果需求要求）、信息安全的Application（如果需求要求）、用户Bootloader、用户Application等进程。假设：仅考虑用户Bootloader、用户Application进程，在上电（PowerOn）或者复位（Reset）过程中，会涉及到两个进程间的跳转问题，示意如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/eEEQvxEw8vyyibkoOxMS3CiclbkN87ykYYibFJr9vUQSA4sMXdy0x8nBWXblvqEysLrG1FhOfjjl7NBJQlj7Sp5ZA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

如此，会引伸出一个工程关注的问题：在软件升级的过程中，即：Application跳转Bootloader的过程中，外部看门狗应该如何处理？为什么需要关心这个问题？由于外部看门狗独立于uC，在Application和Bootloader中均需要独立操作，如果处理不当，可能会引发Bug问题，比如：软件升级过程中，Application跳转Bootloader，没有及时“喂狗”，导致程序复位，软件更新失败。

**02**

**Application跳转Bootloader过程中，如何处理外狗**

Application跳转Bootloader过程中，该如何处理外狗呢？或者说，怎样操作外狗，避免复位等异常工况呢？

这里，以小伙伴的问题为起点：“需要通过SPI喂外狗，在boot中，使用异步SPI喂狗还是使用同步SPI喂狗，如何使用同步方式，是否会引起诊断报文的中断处理与喂狗操作的相互干扰？如果使用异步SPI喂狗，是否需要通过Polling（轮询）或者中断方式确认喂狗成功？”

**Q1：在boot中，使用异步SPI喂狗还是同步SPI喂狗？**

A1：个人理解，不管使用异步还是使用同步处理，区别在于获取请求结果的快慢。同步就是请求发送以后，“死等”请求的状态。异步不是死等请求的结果，可以注册一个回调函数（callback），当请求处理完成后，请求的结果由注册的回调函数通知。如果没有注册回调函数，可以通过模块的主函数，Polling请求的结果。所以，使用同步还是异步，没有优劣之分，具体使用哪种方式，需要结合实际的项目评估，因为每个项目的背景和特点不同，不能一概而论。

**Q2：使用同步方式，是否会引起诊断报文的中断处理与喂狗操作的相互干扰？**

A2：细化一下问题，在Boot中，诊断报文的接收采用中断模式，且使用同步SPI方式喂狗，是否会引发潜在问题？这里的诊断报文（假设为CAN报文），按照描述，可以理解为：诊断报文采用中断模式接收。所以，CAN和SPI本就属于两种不同的硬件单元，不管使用中断、轮询或者同步、异步。两者之间不应产生干扰，当然，特定的工程场景，问题千变万化，不能一概而论。进一步理解，使用SPI同步喂狗的过程中，是否会被CAN的中断打断。如果SPI同步喂狗过程中被中断打断会带来什么影响？

假设SPI在发送喂狗指令的过程中，被中断打断，可能导致喂狗失败。所以，引伸注意点就是，SPI同步喂狗的过程中，可以使用临界区保护，避免SPI同步喂狗的过程被打断。

**Q3：如果使用异步SPI喂狗，是否需要通过Polling（轮询）或者中断方式确认喂狗成功？**

A3：使用异步SPI喂狗，如果没有注册callback中断通知请求结果。那么，通过Polling获取喂狗请求结果是必要的。

**Q4：Application跳转Bootloader过程中，Boot怎么知道什么时间喂狗，跳转Bootloader前，必须先关闭外狗吗？**

A4：在软件升级的过程中，eg：进入拓展会话。程序需要从Application跳转Bootloader。这个过程会涉及外狗处理的问题，即：如何喂狗。策略有如下几种：

1. 如果喂狗周期（假设是窗口看门狗）在Application下，可以延长喂狗周期，即：增大喂狗窗口。可以在进入Bootloader程序前，增大喂狗窗口，避免程序跳转时间过长导致外狗触发复位；
2. 如果功能安全不强制约束，可以在进入Bootloader程序前关闭外部看门狗，进入Bootloader后，重新使能外部看门狗。如果功能安全不允许关闭外部看门狗，此方案不可行。
3. ......

**Q5：Flash操作与喂狗操作**

A5：在Boot中，尤其Flash操作过程中，喂狗是一个需要格外注意的问题。怎么理解呢？在刷写的过程中，会涉及到Flash的擦除和写入动作。Flash的最小擦除单位是Logical Sector，擦除和写入（最小写操作单位Page）需要一定的时间。所以，临近喂狗时间，如果Flash占用时间长，没有及时喂狗就会导致复位。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

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

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin...