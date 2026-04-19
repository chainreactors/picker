---
title: 2026 大唐杯-智能通信系统 赛前临时抱佛脚
url: https://mp.weixin.qq.com/s/xh_uEVezqf2LIwbwoC7ZPA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:50:17.624512
---

# 2026 大唐杯-智能通信系统 赛前临时抱佛脚

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hjtlibzdr5X9pXLXjW75Cz5nNvjtbYcrJNppiarCmoQjbsrNk1qXAyzXed4JtBPnKYZMQnEXJFohuUlnwiarNdTnVmwN8ZLPhpUSryjicibm0LBs/0?wx_fmt=jpeg)

# 2026 大唐杯-智能通信系统 赛前临时抱佛脚

原创

小志z
小志z

志在片语

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 为了加强记忆打了个文档 方便回头复习一下下（

红军在长征途中紧急召开一次重要会议。 请你作为本次会议的指导员快速完成智能作战指挥部通信系统的搭建。

1、 用对讲机调到频道2 通知4公里外（功率1瓦对应1公里传输距离）的电话局搭建电话系统

2、 完成电话配置，拨打 010-8888 6666号码通知广电部门安装电视系统和wifi系统

3、 将PAD设备连接到wifi网络，打开蓝牙功能完成扫地机器人联网

4、 搭建移动通信网络，用手机远程控制扫地机器人清扫会议室，保障会议顺利召开。

### 配置对讲机

> 没啥说法 最简单的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XicYxVLOvh38RMrLicdWFYsCvV5KGAhE0OdWu8IUNuv0PjzbhBibbf8A2OzeicicxDiaA5UWkA5TBh3UOuOFxnjB13WWbficeiaIgyEpb0/640?wx_fmt=png&from=appmsg)

### 配置固定电话通讯

#### 通话信令对应

1. **IAM (Initial Address Message) —— 初始地址消息**

* **含义**：这是呼叫建立时发出的**第一条关键信令**。它包含了被叫号码、主叫号码以及呼叫所需的电路信息。
* **场景对应**：当你拨完号并按下“呼叫”键时，你的交换机就会向对方的交换机发出IAM。它相当于在说：“**听着，有人要打给号码XXX-XXXX，请准备一条从A到B的通话线路。**”

2. **ACM (Address Complete Message) —— 地址全消息**

* **含义**：对方的交换机收到IAM后，检查被叫号码，确认找到了被叫用户（比如找到了对应线路或手机），然后回送的确认消息。它表示**路由已经找到了**。
* **场景对应**：对方的交换机回复：“**收到，根据号码XXX-XXXX，我找到那个用户（或那条线路）了。**”
* **你的感受**：这时你开始听到“嘟...嘟...嘟...”的**回铃音**。因为网络已经准备好，正在等待对方接听。

3. **ANC (Answer Signal) —— 应答信号**

* **含义**：当被叫用户**拿起话筒接听**电话时，对方的交换机发出的信号。
* **场景对应**：对方拿起了电话。对方的交换机告诉你的交换机：“**他接听了！**”
* **你的感受**：回铃音停止，通话计时开始（如果是计费电话）。**这是计费的起始点**。

4. **CLF (Clear Forward Signal) —— 前向拆线信号**

* **含义**：当**主叫方（你）** 先挂断电话时，你的交换机发出的释放线路的信号。
* **场景对应**：你按下挂断键。你的交换机说：“**我这边挂断了，这条通话可以结束了。**”
* **注意**：如果是**被叫方**先挂断，通常不会发CLF，而是发**RLG**（见下）。

5. **CBK (Clear Backward Signal) —— 后向拆线信号**

* **含义**：当**被叫方**先挂断电话时，被叫方的交换机发出的释放线路的信号。
* **场景对应**：对方先挂了电话。对方的交换机告诉你这边的交换机：“**他挂了，结束吧。**”
* **你的感受**：你会听到忙音，或者通话直接中断。

6. **RLG (Release Signal) —— 释放信号**

* **含义**：这是对CLF或CBK的**最终确认**。当一方发出拆线信号后，双方交换机会交换RLG，确认线路两端的资源都已经**完全释放**，可以被下一次呼叫使用了。
* **场景对应**：你的交换机回复对方的交换机：“**收到，我这边也释放了。**”
* **作用**：如果缺少RLG，线路可能会被“吊死”，导致下次呼叫失败。**RLG是通话结束的最终句号**。

#### 网络配置

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XibhwDCK7w8FCUIy0sUiamdwE54kOO9CxLZee8AuyWKumNzlTHbWUJeRuZPg0S59ztzibL8bHQTZMjPrjajSrDyFZhKAWrKnHwwzY/640?wx_fmt=png&from=appmsg)

#### 信令流程

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5Xicz1niaGLrOdfibZomlU2ZJgOMJ4QHc9nMxsMU0s5NAClicXMVbp9rMsIAjiaPI6tWRN8FQ2gAKpAu9p4hCDctzjBoZeqz24ON8eaQ/640?wx_fmt=png&from=appmsg)

完成电话配置，拨打 010-8888 6666号码通知广电部门安装电视系统和wifi系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9xXa2yoCIK8ibyagfM38iaTc0r1n8iaJ1Uauq0sGsoNaW9yMuayphPPnbOXCibiaNl2Krj5BrmibCGxoovz3ECQx8ahfY0oO3iaPqvgk/640?wx_fmt=png&from=appmsg)

### 手机配置

#### 网络配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9Ypzujxw6qMOxEkmUPib9RMHKtefsgR4Iia7rrQexrzOicIic9mdlQ3hGMqzNmHbOiaOZwow9icSEFSquYfI9dthaRtt34cmxwYXdia0/640?wx_fmt=png&from=appmsg)

#### 开机流程

0. 系统消息

**解释**：基站持续向外广播的系统信息，告诉手机“我是谁、我怎么用这个小区、我支持什么功能”。手机必须先收到这些消息，才知道如何接入。

---

1. 随机接入

**解释**：终端（手机）向基站发起的第一条消息，用于“敲门”请求接入，获得上行同步和临时资源。

---

2. RRC建立过程

**解释**：手机与基站之间建立一条专用的控制通道，用于后续所有信令交互。

---

3. 初始UE消息

**解释**：基站在RRC建立后，将手机的第一个高层请求（如注册、上网）转发给核心网。

---

4. 鉴权和加密

**解释**：核心网验证手机身份是否合法，并协商出后续通信的加密算法。

---

5. 安全模式建立

**解释**：正式激活加密和完整性保护，之后所有信令和数据都被加密传输。

---

6. PDU会话建立

**解释**：手机与核心网（UPF/网关）之间建立一条数据通道，获得IP地址，可以上网。

---

7. 执行扫地任务

**解释**：扫地机器人（或智能家居系统）启动清扫程序，进行地面清洁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8lAyHykS2b49oYuYrkgsE3p64ClfKm8ibHYlmJ94OxGKhyD9qbSRj552vx72IUrlnynH9gT5LADAFJ2Q90I4gdicHqnU27yZpiac/640?wx_fmt=png&from=appmsg)

### 电视配置

分为三个区域记忆就好 左侧为卫星 下面是各种器 右侧就比较简单 国干 省级 还有个自编节目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X99PoG5bILKqpvKuhO0qDcN0HmV1qmOVzk8CDXWxuyntzEyyDkk7eqE0r7bjGKicya9ykV2xDI7jzetOKrv7r3QBGAciaAMicsK40/640?wx_fmt=png&from=appmsg)

### Wifi配置

#### 网络配置

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X95TFaIQMzR1LNqSicqZ4AY6bMLjibkAhvgpaV9MP6Lh02Us0ptN3RoVkwVQX2KqWgGNALRI4nLT8vz7KFNRM8ZoBlGuxA7nKiaJU/640?wx_fmt=png&from=appmsg)

#### 参数配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XicYIzw3Ec2XxDneZVy4KTLOibj3mdCAkiaHbrmY7z8uCTQIuRLKs9yAjoGWJYBLwqteicem3fIgvP9MTnCgR2vjMB0pJJWl7BmLmE/640?wx_fmt=png&from=appmsg)

### 扫地机器人和Pad配置

#### 打开扫地机器人蓝牙

> 记得记一下蓝牙名称 等一会pad要连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibSMyqoP8gC1PugO2HaxzxXOIXp8UnMYLY3cy21oGAhKlVAohjYaLgia34raxXx3zXpz369luWEr2YAOUeLdIcaUicl64cVicq2Cg/640?wx_fmt=png&from=appmsg)

#### 配置Pad的网络和蓝牙连接

和之前配置的wifi的ssid以及蓝牙名称对上就行 其余的能打开就打开

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8Q4uRRuNuvvcoCpRZXIPVR8bvfbGZy6iaxj7spe8XjlXugsaFiaH2pV9JNQ5WqXsj1uzM1FSKo8NqeheiaF3XHOJAianRibk8EFh4Y/640?wx_fmt=png&from=appmsg)

最后完成就这样 比较简单

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicUZZdRG7AVgIGbjIdTHzdzDqS2EhdCRWqCteTR03UOwX99ibBaBxBYFoe3NqgnyeKm5fFTaL8J4GTUVRhJ5KJ7tKG5z28Z3gRw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

志在片语

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

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