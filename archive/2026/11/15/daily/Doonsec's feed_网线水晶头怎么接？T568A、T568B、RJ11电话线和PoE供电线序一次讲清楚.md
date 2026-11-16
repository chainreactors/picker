---
title: 网线水晶头怎么接？T568A、T568B、RJ11电话线和PoE供电线序一次讲清楚
url: https://mp.weixin.qq.com/s/Eu3q6HR9T3gu-RPywXsebw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:32.947211
---

# 网线水晶头怎么接？T568A、T568B、RJ11电话线和PoE供电线序一次讲清楚

# 网线水晶头怎么接？T568A、T568B、RJ11电话线和PoE供电线序一次讲清楚

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在网络工程项目中，网线制作几乎是每个网络工程师都绕不开的基本功。

办公室网络布线、机房设备连接、交换机与服务器互联，甚至监控摄像头安装，都可能涉及网线水晶头制作。

看起来只是把8根颜色不同的线插进水晶头，但里面有明确的标准。线序接错，轻则网络不通，重则出现协商速率异常、通信不稳定等问题。

今天把综合布线中最常见的几种线序整理一下，包括RJ45网线、T568A和T568B标准、直通线与交叉线、RJ11电话线，以及PoE供电线序。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04CicH7ymF2BDrHDsm3mvHt5f1PFrMmX1ddFa3bKT4HUTSp1LTaJpzXVTFKuAYAY7egh7ibyphpQEVBt61YJ9GL0oA4JDbWsg7ZU/640?wx_fmt=png&from=appmsg)

## RJ45水晶头

我们平时使用的以太网网线，大多数采用RJ45接口（工程上常这样称呼，严格来说是8P8C模块化连接器）。

一个标准RJ45水晶头有8个金属触点，对应网线中的8根铜芯。

这8根线并不是随便排列的，而是按照国际布线标准规定的线序进行排列。

目前最常见的两种标准是T568A和T568B。

**T568A线序：**

1. 白绿
2. 绿
3. 白橙
4. 蓝
5. 白蓝
6. 橙
7. 白棕
8. 棕

**T568B线序：**

1. 白橙
2. 橙
3. 白绿
4. 蓝
5. 白蓝
6. 绿
7. 白棕
8. 棕

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05lPIA8KtPI4OvMMibc56t0LzalOBkIUIdMqrH0AE3vJtJZfTaQeYP0GkdR3KBHYyLDXDF89EPOfNBvn9Op07qSRlcQ7HAHRnQY/640?wx_fmt=png&from=appmsg)

在国内的网络工程和综合布线项目中，T568B使用得比较普遍。

制作网线时，可以记住一个简单规律：先确定水晶头的观察方向，再按照标准从1号脚排到8号脚，千万不要一边看线序、一边把水晶头方向拿反。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06dd3UcyXsd5cEUXSLhJzP3eMxtPHGKDYQ7GJJD7Z8sLnMXQN41T04Ct2oYTUYIxib6Qibllr0cOAibHjCQTh0VK3s3JQiafqvQyibY/640?wx_fmt=png&from=appmsg)

## 直通线和交叉线有什么区别？

网线制作中，还有两个经常出现的概念：直通线和交叉线。

**直通线：两端采用相同线序。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05aLWpIvu0FZtCj4yDBxk6fnjicVCcabBhVYEjiceqhu5iaj0mmKib8cgsbk1WN47AHfxicpS5jRiaHKGibibuwfkUWZgVYGZPKlOa4uQI/640?wx_fmt=png&from=appmsg)

例如，两端都使用T568B标准，或者两端都使用T568A标准。

直通线是日常网络布线中最常用的类型，常见于电脑连接交换机、交换机连接路由器、服务器连接交换机等场景。

**交叉线：两端采用不同线序。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06vDiaIBra4pgqADZUsrJiadTBXbplhqzaWUE4YiaVNarQ6Y7gZ1UkC9Em6seTguAFMjxEPyic9vMR1PicYp9yFOHJT5mX2cQtwxffA/640?wx_fmt=png&from=appmsg)

例如，一端使用T568A，另一端使用T568B。

交叉线主要用于传统以太网设备之间的直接连接，例如早期同类型设备互联。

这里需要特别说明，现在很多交换机、网卡都支持Auto MDI/MDIX（自动线序识别），可以自动适应直通线或交叉线，因此实际项目中交叉线已经没有以前那么常见了。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba042EuTeWY9RUFzVzlCxic6LicAJ2VIIl3gWSlC0K5v5z03eIzoClTG4FnkuBdiaGY2NDMLpZtoia87aJtHgrlM9I7c9gkr6VFtMfVs/640?wx_fmt=png&from=appmsg)

不过，T568A和T568B的区别，以及两种线序如何组合，仍然是综合布线必须掌握的基础知识。

## RJ11电话线

RJ11主要用于传统电话线路连接，常见于固定电话、电话配线架以及部分语音设备。

和RJ45的8个触点不同，常见RJ11电话接口通常采用6位模块化接口，其中实际使用的触点数量可能是2芯或4芯。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05skhptzqibNsF5VAAcRLxvicOst3lWkUx41zjY2iajE3bm7vHDburqZfe7POzppl1eGBBa78FvWmIhGfSAhgnocJEDibiaeekdD3WQ/640?wx_fmt=png&from=appmsg)

**两芯电话线：**

通常使用中间的两个触点连接一条电话线路。

**四芯电话线：**

通常使用中间两芯作为第一条电话线路，外侧两芯可以用于第二条电话线路。

需要注意，电话线的颜色并不像T568A、T568B那样有统一的通用颜色排列，实际施工应以线缆标识、设备接口定义和项目规范为准。

另外，RJ11和RJ45虽然外观相似，但接口尺寸、触点数量和使用场景并不完全相同，不能直接混为一谈。

## PoE供电

PoE是Power over Ethernet的缩写，也就是以太网供电技术。

简单来说，就是通过一根网线，同时为网络设备传输数据和提供电力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06QuHRWzgnP5Od4O1Pta72wePABbKypIoa0F5hLKEA7V9YSV95k64z5F6ALPu8Dqicia7xCX5qyODqZ4XcfN13DcEn4on4MRUXEw/640?wx_fmt=png&from=appmsg)

常见的PoE设备包括无线AP、网络摄像头、IP电话以及部分无线网桥。

在IEEE 802.3af标准中，定义了两种典型供电方式：Mode A和Mode B。

**Mode A：通过数据线对供电。**

![Mode A](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07bZPzNEVnJc2gHLBdsApnfYfL4fX658LfsUGC2HiaCvh5iamKAhVVVfjia64mszLvGWbpnqHys0RbaUC4q6FhOkQ7bRSAykhaYhQ/640?wx_fmt=png&from=appmsg)

Mode A

使用RJ45的1、2、3、6号针脚，也就是传统10/100Mbps以太网使用的数据线对。

**Mode B：通过空闲线对供电。**

![Mode B](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04rBa7FPY191PkAaoK5PjuibGVUicjto9CefPTTgaILPry76f7o1HibTOFYGSyeUrwKZyJPJp35KVKVd49rsibJ0SibwgQWOVapOsZ8/640?wx_fmt=png&from=appmsg)

Mode B

使用4、5、7、8号针脚，也就是传统10/100Mbps以太网中没有用于数据传输的线对。

这也是为什么早期PoE设备经常会提到Mode A和Mode B两种供电方式。

不过，随着千兆以太网和更高功率PoE技术的发展，情况也有所不同。

千兆以太网的四对双绞线全部参与数据传输，PoE仍然可以通过线对共存方式供电。

IEEE 802.3bt标准还支持通过全部四对线进行供电，以满足更高功率设备的需求。

所以，不能简单认为PoE供电一定使用空闲线对，也不能认为千兆网线就不能使用PoE。

实际施工时，应确认交换机或PoE供电设备、受电设备的标准兼容性，以及网线质量和传输距离是否满足要求。

## 网线制作时容易出现的几个问题

网线线序看起来简单，但实际施工中仍然有不少细节值得注意。

首先，两端线序必须符合设计要求。直通线两端使用相同标准，交叉线两端使用不同标准。

其次，网线剥皮时不要伤到内部铜芯，压接时尽量减少双绞线解绞长度。双绞线的绞合结构本身就是为了降低电磁干扰，解绞过长会影响传输性能。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06b5LLCQYuaUsJ3iaibqxgQkprbGUyTJbxWPfzs47J0Uu86C1tX5eAiawiba2lXj3Wt02QICckT3w1NoLswLZv5NdhQ4kFnfAsyDXA/640?wx_fmt=png&from=appmsg)

另外，水晶头压接完成后，不要只看灯亮不亮。最好使用专业网线测试仪检查1到8号线是否全部连通、是否存在错序、短路或断路。

对于要求较高的综合布线项目，还应使用认证测试仪检测链路性能，而不是仅凭普通测线仪判断网线是否合格。

最后，涉及PoE供电的项目，还需要关注线缆线径、长度、连接器质量以及线路电阻，避免因线缆质量问题导致设备供电不稳定。

---

T568A、T568B、直通线、交叉线、RJ11和PoE线序，都是网络工程师和综合布线人员需要掌握的基础知识。

平时可能觉得这些内容很简单，但到了机房施工、网络故障排查和无线AP部署现场，这些基础知识往往能直接影响工作效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04RGbKEfmOppkJWnkGFbALsgia88XdLOrNglDfy4dJQaEvDiaaChjIutwtSWEm24UCpdqRWwfvDFIkoXqJ0VhMLVWEqkiasjpDs6g/640?wx_fmt=png&from=appmsg)

尤其是现在PoE交换机、无线AP和网络摄像头越来越普及，网线已经不只是传输数据的介质，还承担着设备供电的任务。

基础线序看似简单，真正施工时却不能马虎。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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