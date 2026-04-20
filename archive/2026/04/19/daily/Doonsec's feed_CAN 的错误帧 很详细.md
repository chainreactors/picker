---
title: CAN 的错误帧 很详细
url: https://mp.weixin.qq.com/s/Z8B6_4xnj3e9fA92OQ0awg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:12.092213
---

# CAN 的错误帧 很详细

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Vgbm9ibpszia5SRicSkc7d1a3phQwR9tMT8TCaBLEDnh3h7prB3hzYAL7iaTLbh1DiaQu2GoTF1FiaRl9KKEYpDVPPHw/0?wx_fmt=jpeg)

# CAN 的错误帧 很详细

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于汽车与基础软件
，作者汽车与基础软件

![](http://wx.qlogo.cn/mmhead/kqodNCVWpEuEIImOFDVgicPibr4NRNWqKIBwORpN1rZQSwbH8VVHD4GPMfsK6a5HDsw4gozVicKzcI/0)

**汽车与基础软件**
.

给我两年 不改变点 汽车行业的学习环境，自己注销账号，

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCQRPm0gclw0Y8ViaG7SKue8vz7dRUPST92WRBBqc5LTtu34RSjLbf4d9kHZFldJgBSDPiaQegTIGt63RK36d8dBaPDLSRUodibvo/640?wx_fmt=png&from=appmsg)

**01**

**帧物理层**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDe7Y3dZFcWZ7BBUvjQdv03Nk75WFEMk3fLxGeY6YpVG85ttqKrh6LLIeo8AgosZC94MnT9vp69RZzkic5WHveN4tajRp0gkjgw/640?wx_fmt=png&from=appmsg)

**1.1 显性与隐形**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB4toEOmSR04r862fzyVsYs46IruWNgbyibd4dzDzHD8nicnLt1Stl8A3TCOGVZyt6Ydxuxll8pE7nNjw7rMib8EZRBz2RpibbbHCM/640?wx_fmt=png&from=appmsg)

**02**

**错误帧的类型**

错误帧的类型有

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDjEa84PnVxpOhDOPM9lWDpqt8B0jV0PaMx76GVTOb36EXQ1MIBQicEveyLx4qwzcsSdWmOaECgPq9a34aZjs3kcH3sFHCyw91I/640?wx_fmt=png&from=appmsg)

1Bit Error [Transmitter]

CAN 总线上的每个 CAN 节点都会随时监控信号电平，这意味着发送 CAN 节点也会 “回读 ”其发送的每个比特。如果发送器读取的数据位电平与其传输的数据位电平不同，则发送器会将其检测为位错误。

如果比特不匹配发生在仲裁过程中（即发送 CAN ID 时），则不会被解释为比特错误。同样，确认时隙（ACK 字段）中的不匹配也不会导致比特错误，因为 ACK 字段特别要求发送器的隐性比特被接收器的显性比特覆盖。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCYlcQIreyAIAehyVvickbRjicr1aTkgwowSK9c0BKsQuI6Via9pXkDm9vNticDBXOumkqzj8u9S6nExibuLnBUZFlDgh5b7zl4sHGs/640?wx_fmt=png&from=appmsg)

1Bit Stuffing Error [Receiver]

如前所述，位填充是 CAN 标准的一部分。它规定，在每 5 个连续的相同逻辑级别的比特之后，第 6 个比特必须是补码。这是通过提供上升沿来确保网络持续同步的要求。此外，它还能确保比特流不会被误解为错误帧或标志报文结束的帧间空间（7 位隐性序列）。所有 CAN 节点都会自动删除多余的比特。

如果在 CAN 报文的总线上（在 SOF 和 CRC 字段之间）发现 6 个逻辑级别相同的比特序列，接收器会将其检测为比特填充错误（又称填充错误）。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBZNYMNVZIzuURmWb1JdF9Etm6tMHvxMbicbfG0bXOPRslk7zkAictGkcCoq1sKdfIvKlnR2JGnoicSibWaqzAnfy0Zq42shzNKBMw/640?wx_fmt=png&from=appmsg)

1Form Error [Receiver]

这种报文级检查利用了 CAN 报文中某些字段/比特必须始终处于特定逻辑级别这一事实。具体来说，1 位 SOF 必须是显性的，而整个 8 位 EOF 字段必须是隐性的。此外，ACK 和 CRC 定界符必须是隐性的。如果接收器发现其中任何一个比特的逻辑电平无效，接收器就会将其检测为形式错误。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBxcgW36ciahxbMfkx5eXd5sgBKx4NWzVK2KjBZeqjxIspfTDDYnxE3ibK8gAKcmauhIYuCES73JMtyNvt4eqxiart5goia9dyyDVA/640?wx_fmt=png&from=appmsg)

1ACK Error (Acknowledgement) [Transmitter]

当发送器发送 CAN 报文时，报文将包含 ACK 字段（确认），其中发送器将发送一个隐位。所有监听的 CAN 节点都要在该字段中发送一个显性位，以验证是否收到报文（无论节点是否需要这个报文，所以这个ack变成显性，和软件本身没有关系）。如果发送机在 ACK 时隙中没有读到显性位，则发送机会将其检测为 ACK 错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCxtOOPQYEpM8vXcmlHwRl6jUrbFD2ENBUuzv4kD7WuFn5aiadrohicN0FcgsFJyKjokotAYcl5Zf2tu9K6iaBUiczmU6srqgotf3c/640?wx_fmt=png&from=appmsg)

1CRC Error (Cyclic Redundancy Check) [Receiver]

每个 CAN 报文都包含一个 15 位的循环冗余校验和字段。在这里，发送器计算出 CRC 值并将其添加到报文中。每个接收节点也会自行计算 CRC。如果接收器的 CRC 计算结果与发送器的 CRC 不一致，接收器就会将其检测为 CRC 错误。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBfpVme1icWMhEsTSiaSXmB3GqyEFkC6w37568wudCQYVdmrMZicg2z1MPHaiaHqIIL5GTqFw3cGpnzNzftzPJ3H0JI1gFicKTnP4SE/640?wx_fmt=png&from=appmsg)

**03**

**节点状态与 TEC,  REC**

**3.1 CAN节点状态**

**1主动错误状态**

每一个节点的默认状态，其实就是主动错误状态，这并不是错误状态，而是你现在还有能力去主动上报错误的状态。大家要知道，主动上报错误，实际上是需要干扰到总线发报文的。

**1被动错误状态**

当REC 或者是 TEC 到达了一定的数量后，就会进入被动错误状态，注意这个被动错误状态，也不代表你真的就有故障，这只是说，你上报故障的电平就需要改变了，你往外发报文的时机就有限制了，因为这时候你有问题嫌疑，尽量不要影响总线。

**1Busoff 状态**

完犊子了，这时候你确诊了，真的有问题，那么进入busoff状态，把自己隔离开，不要收，也不要发，影响总线。

**3.2 Counter 增加与减少**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCzS9GDVhgCebmeNickcn9Mjkr3vbVW1neJ8icZUmAnicibKibPDIHSIPibe7YB7NCyI00yAaeRiaaVftFPu8ZHtcA26BTXNpO1LF61XM/640?wx_fmt=png&from=appmsg)

这三个状态，的counter 到底是如何增加减少的呢？ 为什么有时候 +8, 有时候 +1， 有时候 -1 呢。

故障标识，分为主要故障，和次要故障(我不知道这里我命名的合适不合适，不过不重要了)。主要的目的是区分开，节点真正的识别到了总线的错误，和别人通知的错误，我们只是收到了而已，所以也可以理解为，我发现了问题，和别人给我说有问题。这里counter的不同点就是+8 还是 +1。

**3.2.1 TEC +8**

举个例子 当发送节点，发送bit为隐形，但是回读到的是显性，那么这个发送节点就应该把自己的TEC +8， 当然还要主动通知一下总线，我好像不对劲了，发6个连续的显性位.

**3.2.2 REC +1**

这时候接收节点收到了连续6个节点的显性位，就知道，哦当前总线可能不对劲，那么我们自己的REC +1。所以这样的事件，对于接收节点为 次要故障。

**3.2.3 REC +8**

如果接收节点收到的报文，发现E2E不对了，帧错误了，那完了，是不是我要不行了，怎么收到不对的内容了，这时候我要给自己的REC +8。

**3.2.4 TEC -1**

当发送节点，完全发送正常 则给自己的TEC -1

**3.2.5 REC -1**

当接收节点，完全接收正常 则给自己的REC -1

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

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

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽...