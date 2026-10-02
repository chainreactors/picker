---
title: 【软考网规】第二章数据通信原理（数据编码）
url: https://mp.weixin.qq.com/s/DxHweDcmHDn6FXtIswisNA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:42.205544
---

# 【软考网规】第二章数据通信原理（数据编码）

# 【软考网规】第二章数据通信原理（数据编码）

原创

成渝Sec
成渝Sec

成渝Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICskbgBZNZcrBrm7psTGwcSzTFGgJ6nlNictshJzdGNIVaA33H3K5NQBVxBYkBwslKPMCVxAaCGKRWibOsxJag1iaoCTpDsbeEdC8/640?wx_fmt=png&from=appmsg)

### **软考与证书**

计算机技术与软件专业技术资格（水平）考试，简称软考。

这是由国家人力资源和社会保障部、工业和信息化部领导下的国家级考试，其目的是科学、公正地对全国计算机与软件专业技术人员进行职业资格、专业技术资格认定和专业技术水平测试。

#### **一、曼彻斯特编码**

#### **曼彻斯特编码是一种双相码，在每个比特中间均有一个跳变，**第一个编码自定义。假如下图由高电平向低电平跳变代表“0”，由低电平向高电平跳变代表"1”。

#### 曼彻斯特编码常用于以太网中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICWIc4ic7F98NcIgcOFuPY0NJhdNCOVNyMk0MyjO5aib2zz6icT7JCYZPruVqwxAickqT3EcSg65HKnhT1bIKDpv2BBhich8tUFqug4/640?wx_fmt=png&from=appmsg)

#### **二、差分曼彻斯特编码**

#### **差分曼彻斯特编码也是一种双相码，用在令牌环网中。**

#### **有跳变代表“0”，无跳变代表“1”【有0无1】。**

#### **不是比较形状，比较起始电平（上一个的终止与下一个起点）。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBLMQdUYsyrNSs3tasWUBATPhOGHdMNIpat82wDErGQrGVheb9CAY7KblZ0kzoeMclmJq6g4jkvZv6DibhFsV2voBoUBFoCX8IQ/640?wx_fmt=png&from=appmsg)

#### **三、两种编码的特点**

以下编码：“011010011”分别用曼彻斯特编码标识和查分曼彻斯特编码标识，分别是怎么样的？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICqkMvEeicR7Mu5ZTIuLZRQ93Xx4Ubgy7Nib0HACxTkSxxLHVrREDibOMlB2GRTOCdkp2aO2yXsiay0erXakwNpf3HzXPJKCW1pCac/640?wx_fmt=png&from=appmsg)

曼码和差分曼码是典型的双相码，双相码要求每一位都有一个电平转换，一高一低，必须翻转。

曼码和差分曼码具有自定时和检测错误的功能。

两种曼彻斯特编码优点：将时钟和数据包含在信号数据流中，也称自同步码。

编码效率低：编码效率都是50%。

两种曼码数据速率是码元速率的一半，当数据传输速率为100Mbps时，码元速率为200Mbaud。

#### **练习题**

（1）10M802.3LAN使用曼彻斯特编码，它的波特率是（1 C）.

A.5Mbaud    B.10Mbaud    C.20Mbaud    D.30Mbaud

（2）测得一个以太网的数据波特率是40MBaud，那么其数据率是（2 B）。

A.10Mb/s B.20Mb/s    C.40Mb/s    D.80Mb/s

#### **四、其他编码**

#### **4B/5B编码**：快速以太网100BASE-FX采用4B/5B和NRZ-I编码，先把信息按4bit进行分组，接着转换为5bit编码，多1位用于解决同步问题，最后转换为NRZ-I代码序列发送到传输介质。

#### 8B/6T编码：快速以太网100BASE-T4采用8B/6T编码，原理为：先把信息按8bit分组，然后映射为6个3进制位（比如：0、+、-）。了解即可，具体编码细节不必深究。

#### 4D-PAM5编码：用于1000BASE-T以太网标准，1000BASE-T物理层采用4对5类双绞线，支持全双工。

#### 8B/10B编码：1000BASE-TX采用8B/10B编码，除了1000BASE-T以太网标准之外的编码，都是采用8B/10B编码。

#### **五、编码效率与应用场景**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICiahd0fkqnt8EGGbShAYZhaT1mSGhRNuCyjHiaqoFIqOtzlCBODWt2c0rwcwuXSXE7QWt4UdwAiacfeQNbk7N4OqX6Nr1mY5kGR4/640?wx_fmt=png&from=appmsg)

各种编码效率对比：

曼彻斯特编码效率50%，用于以太网

4B/5B效率80%，用于百兆以太网

8B/10B效率80%，用于千兆以太网

64B/66B效率97%，用于万兆以太网

#### **六、MLT-3编码**

MLT-3编码常用于100BASE-TX，用3种电位状态分别表示“正电位”、“零电位”和“负电位”。

MLT-3编码规则较为复杂，总结如下：2019/（16）、2020/（15-16）

（1）如果输入为数值0，则电平保持不变。

（2）如果输入是数值1，则产生跳变，但跳变分两种情况：如果前一个电平是+1或-1，则下一电平为0，如果前一电平是0，下一个电平和最近一个非0电平相反。

#### **七、真题**

即学即练·网规2020年15-16题

下面是100BASE-TX标准中MLT-3编码的波形，出错的是第（15）位，传送的信息编码为（16）。

A.3 B.4    C.5    D.6

A.11111    B.0000000    C.0101010    D.1010101

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Shiamu7mxKICziaXZHibyVC1nVIlZj3hxWNH0ysyeAicvZlINvCJkDFFibyl0ySkn0OyTaYBU1ia7tNhtX5ePuQmZ10rQYnmISkOjkNm0wDQkwDYU/640?wx_fmt=jpeg)

【参考答案】C  A

MLT-3跟NRZI码类似，遇1跳变，遇0保持不变，MLT-3编码规则：

（1）如果下一输入为数值0，则电平保持不变；

（2）如果下一输入是数值1，则产生跳变，但又分两种情况：如果前一个电平是+1或-1，则下一电平为0，如果前一电平是0，下一个电平和最近一个非0相反。

观察第二个电平有变化，结合第一个规则，判定第二个位是1，排除BD；其次每个编码都有跳变，则全部是1，选A。

即学即练·网规2019年15-16题

下图是采用100BASE-TX编码收到的信号，接收到的数据可能是（15），这一串数据前一比特的信号电压为（16）

A.0111110    B.100001    C.0101011    D.0000001

A.正电压    B.零电压    C.负电压    D.不能确定

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICNZOicGC6F7BOjGghlu2ZThHfic9Aw0GXexhB3ylac9pZ0vjGRgkahg9qZdxn6bdHJVia5NwaEtQn3rCQWZujQoVRzxThLWRcPcQ/640?wx_fmt=png&from=appmsg)

【参考答案】A B

100BASE-TX采用的是4B/5B编码方式，即把每4位数据用5位的编码组来表示，该编码方式的码元利用率=4/5\*100%=80%。然后将4B/5B编码成NRZ1进行传输，使用MLT-3（多电平传输-3）波形法来降低信号频率。

题目的图不是NRZI码，而是MLT-3编码。

MIT-3编码规则：多电平传输码，MLT-3码跟NRZI码有点类似，其特点都是逢"1”跳变，逢“O”保持不变。与NRZI码不同的是，MLT-3有”-1”"O"“1”三种电平，所以数据是：0111110。

即学即练·网规2017年11月第12-13题

100BASE-TX采用的编码技术为（12），采用（13）个电平来表示二进制0和1。

（12）A.4B5B B.8B6T    C.8B10B    D.MLT-3

（13）A.2    B.3    C.4    D.5

【参考答案】（12）D（13）B

100BASE-TX先采用4B/5B，再采用MLT-3编码，联系上下文选MLT-3更合适。

即学即练·网规2018年11月第12题

下图中12位差分曼彻斯特编码的信号波形表示的数据是（12）。

A.001100110101    B.010011001010

C.100010001100    D.011101110011

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIBcZhQ7xwoNicluIDQapRwdhU0gxyy2muWGVNjWDe6H3mPNC79jsianDAicANR07c2hJibIkv0ARUCicz57cdbU4BpzY7rVEUaMickY8/640?wx_fmt=png&from=appmsg)

【参考答案】B

【解析】差分曼彻斯特编码中，编码规则是“有0无1"，即后一个波形的起始电平跟前一个波形的结束电平相比，有变化就表示0，如果没有变化表示1。差分曼彻斯特编码中，只能从第二个波形开始推断具体编码。第一个波形结束电位是负电平，第二个波形的起始电位是正电平，明显有变化，所以第二位肯定是1，其他位依此类推。

即学即练·网规2018年11月第12题

100BASE-X采用的编码技术为4B/5B编码，这是一种两级编码方案，首先要把4位分为一组的代码变换成5单位的代码，再把数据变成（13）编码。

A.NRZ-I

B.AMI

C.QAM

D.PCM

【参考答案】A

4B/5B编码方案是把数据转换成5位符号，供传输，因其效率高和容易实现而被采用。这种编码的特点是将要发送的数据流每4bit作为一个组，然后按照4B/5B编码规则将其转换成相应5bit码，再把数据转换为NRZ-I编码。

即学即练·网规2019年11月第18-19题

IEEE802.3z定义了千兆以太网标准，其物理层采用的编码技术为（18）。在最大段长为20米的室内设备之间，较为合理的方案为（19）。

（18）A.MLT-3    B.8B6T    C.4B5B或8B10B    D.Manchester

（19）A.1000Base-T    B.1000Base-CX    C.1000Base-SX    D.1000Base-LX

【参考答案】（18）C    （19）B

曼彻斯特编码效率50%，用于以太网，4B/5B效率80%，用于百兆以太网，8B/10B

效率80%，用于千兆以太网，64B/66B效率97%，用于万兆以太网。题目没有8B/10B编码，只有C最接近。1000Base-CX传输距离是25米。

即学即练·网规2021年11月第12题：

1000BASE-TX采用的编码技术为（12）。

A.PAM5    B.8B6T    C.8B10B    D.MLT-3

【参考答案】C

1000BASE-T采用5类或超5类双绞线传输，使用编码方案是4D-PAM5。1000BASE-X采用光纤或短距离铜缆传输，采用8B/10B编码技术。1000BASE-TX技术对传输介质要求高，只有6类或更高的布线系统才能支持，同时其编码方式也相对简单，采用8B/10B编码（8B/10B简单，PAM5复杂），相当于用更好的硬件传输介质去弥补编码技术的缺陷。

###

**![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)如果文章**对你有帮助，请关注我的公众号：****

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4U7y70dsprCjIyYyHgQufrWbicAMWEzOdQGaibvZL3xqtoYyyrmWzhOWSFTJ84u4UwKb6FicXF3DHxiakOAjPw0eHg/0?wx_fmt=png)

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