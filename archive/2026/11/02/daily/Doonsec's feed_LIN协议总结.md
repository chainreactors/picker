---
title: LIN协议总结
url: https://mp.weixin.qq.com/s/u5MpOlt5EZNJhWGxIZDJIg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:58.627503
---

# LIN协议总结

# LIN协议总结

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**LIN是什么**

**1、LIN的概念**

LIN是 Local Interconnect Network 的缩写，是基于UART/SCI(Universal Asynchronous Receiver-Transmitter / Serial Communication Interface，通用异步收发器/串行通信接口)的低成本串行通信协议。（串行通信技术，是指通信双方按位进行，遵守时序的一种通信方式。 串行通信中，将数据按位依次传输， 每位数据占据固定的时间长度，即可使用少数几条通信线路 就可以完成系统间交换信息。还规定 LIN总线长度不超过 40 米。

**2、扩展介绍一下同步通信和异步通信的区别**

1.同步通信要求接收端时钟频率和发送端时钟频率一致，发送端发送连续的比特流；异步通信时不要求接收端时钟和发送端时钟同步，发送端发送完一个字节后，可经过任意长的时间间隔再发送下一个字节。

2.同步通信效率高；异步通信效率较低。

3.同步通信较复杂，双方时钟的允许误差较小；异步通信简单，双方时钟可允许一定误差。

4.同步通信可用于点对多点；异步通信只适用于点对点。）

**3、LIN连接结构及节点构成**

LIN 的拓扑结构为单线总线，应用了单一主机多从机的概念。总线电平为 12V，传输位速率(Bitrate)最高为20kbps。一个 LIN 网络最多可以接 16 个节点，主机节点有且只有一个，从机节点有 1 到 15 个。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCqCaZXO2lcoQjNIu98icIRdKGHIDGkbvMrR1kVIg7wjU2sh6ia4SpP8LibJSbfywl7RPHWoAW2Mia57hKP6ia9mUiavicOmuSMaEPvyE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDOpb8aPMB0apQyk7LdHMMcM6zZNRaH30amDWicoUn7VvrI0gibicGFn69KBic2ibqudDJCZAVtyoyunOL48NRmHrYxNlXaU6YStd24/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCsgWIP4AibowxZITlkNlRZraOc7X7lo9hIwG5TcqxkCLDQHDQPrHbWOlczN3b11wYLlFzq5oEEZ9qmGrianfn0ujBvBD1AjLJfU/640?wx_fmt=png&from=appmsg)

**02**

**LIN的特点**

1、网络由一个主机节点和多个从机节点构成。

2、使用 LIN 可以大幅度的削减成本，表现在以下方面：

● 开放型规范：规范可以免费从官方网站获得。

● 硬件成本削减：基于普通 UART/SCI 接口的低成本硬件实现，无需单独的硬件模块支持；从机节点无需

高精度 时钟就可以完成自同步；总线为一根单线电缆。

● 装配成本削减：LIN 采用了工作流(Work Flow)和现成节点(Off-the-shelf Node)的概念，将网络装配标准

化，并可通过 LIN 传输层进行再配置。

● 缩短软件开发周期：LIN 协议将 API(Application Programming Interface，应用编程接口)标准化。

3、 信号传输具有确定性，传播时间可以提前计算出

4、LIN 具有可预测的 EMC(ElectroMagnetic Compatibility，电磁兼容性)性能。为了限制

EMI(ElectroMagnetic Interference，电磁干扰)强度，LIN 协议规定最大位速率为 20kbps。

5、LIN 提供信号处理、配置、识别和诊断四项功能。

**03**

**LIN协议层**

**1、帧的结构**

①帧(Frame)包含帧头(Header)和应答(Response

)两部分。主机任务负责发送帧头；从机任务接收帧头并对帧头所包含信息进行解析，然后决定是发送应答，还是接收应答，还是不作任何反应。

②帧头包括同步间隔段、同步段以及PID(Protected Identifier，受保护ID)段\*\*，应答包括数据段和校验和段\*\*。

③值“0”为显性电平(Dominant)，值“1”为隐性电平(Recessive)，当总线上有大于等于一个节点发送显性电平时，总线呈显性电平。显性电平起主导作用。帧中的所有间隔或总线空闲时都应保持隐性电平。

④同步间隔段：由同步间隔和同步间隔段间隔符构成，同步间隔是至少持续 13 位的显性电平，同步间隔段的间隔符是至少持续 1 位的隐性电平。

⑤从机任务接收帧头的同步间隔段时，以该从机任务所在节点的位速率为准，当检测总线上出现持续 11 位的显性电平时，认为是帧的开始。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAgjV4WbZQFxvENlfyx19lJMPLGRkUwNProfhmCsJ70CwiaVkxAk7XqIxQNyWAlSyFicVk8icFtdOOUfzvF7jkHgNhcftZia06JHsU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBSJXKsojpPuvPglfEicC4HQUceeSEKQV7mavvfDAQLyyNGcCClPEiavu8j2oIRzOV0PvLzOkwFoUeZ3cTym7iaEJRpACAhzG4Yaw/640?wx_fmt=png&from=appmsg)

⑥受保护 ID 段：的前 6 位叫作帧 ID(Frame ID)，加上两个奇偶校验位后称作受保护 ID。帧 ID 标识了帧的类别和目的地：

帧 ID 的范围在 0x00～0x3F 之间，共 64 个。帧 ID 标识了帧的类别和目的地。从机任务对于帧头作出的反

应(接收/发送/忽略应答部分)都是依据帧 ID 判断的。校验公式如下：P0 = ID0 ⊕ ID1 ⊕ ID2 ⊕ ID4

P1 = ¬ (ID1 ⊕ ID3 ⊕ ID4 ⊕ ID5)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDAWe0W2VlkNeOCpPLnvqR1Kq2FdYQpru13wt0CMMGvkJODv8uG7wCgWHkkiaJDq4dd9xgprDVZjbFYbnweyLibCyWZMiaOvibTlBc/640?wx_fmt=png&from=appmsg)

⑦节点发送的数据位于数据段，包含 1 到 8 个字节：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAuz1icMNfagzjiaMRgHS4LGW0I6MnJnicZmaOP38sp6ibwammuX0Za0CrtEdEUP0bicA9ad0xnCySfW1MOQRlDej4aB4Jdd6eOXDOY/640?wx_fmt=png&from=appmsg)

⑧校验和段：是对帧中所传输的内容进行校验。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBsrrmgJ90XwFPsiaWKtPhCWkDLRpkzUxRLuQh0qDjzV8GnXKiapia2t5Pvc7Lolxiatbqw2ic9waVlBjmqyftxCfNBc4e2xpkdTwT0/640?wx_fmt=png&from=appmsg)

⑨帧在总线上传输时间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCDZtkbuPYr2IWiaKTMJKct3xmLsNfCp82z83ksLpQGGk7kEo8huQ7XOOw0OlAVicUgLKZRPstcbkfBFJnIA2bsC2zcKOV1JBXKY/640?wx_fmt=png&from=appmsg)

**2、帧的类型**

如图：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCz2M9ibBtkzFPsnqt0mfhibjyS9hW7ibEN1FkfCSuczuDOeTOojV7H1dHXqdr8U4RzJVHFvwcO8Q4L7Be4E77nd62VupgFgFic068/640?wx_fmt=png&from=appmsg)

**无条件帧**（无条件帧是具有单一发布节点，无论信号是否发生变化，帧头都被无条件应答的帧）。

**事件触发帧**（是主机节点在一个帧时隙中查询各从机节点的信号是否发生变化时使用的帧，当存在多个发布节点时，通过冲突解决进度表来解决冲突）。

**偶发帧**（偶是主机节点在同一帧时隙中当自身信号发生变化时向总线启动发送的帧。当存在多个关

联的应答信号变化时，通过事先设定的优先级来仲裁。）。

**诊断帧**（诊断帧包括主机请求帧和从机应答帧，主要用于配置、识别和诊断用）。

**保留帧**（保留帧的帧 ID 为 0x3E 和 0x3F，为将来扩展用。）。

**3、进度表**

进度表是帧的调度表，规定总线上帧的传输次序以及各帧在总线上的传输时间。还规定了帧时隙的大小。

一般情况下，轮到某个进度表执行的时候，从该进度表规定的入口处开始顺序执行，到进度表的最后一个帧时，如果没有新的进度表启动，则返回到当前的进度表第 一个帧循环执行。（LIN总线最小时间单位是时基(Tbase)）。调度表中用来发送一帧报文的时间称为帧时隙(Frame\_Slot)，帧时隙必须是时基（5ms）的整数倍，调度表是由帧时隙组成的。

**4、状态机 实现**

①主任务状态机：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAtKmcgP8OCtlSmEiawMREcVDz4gnpD6Bfbhuiajic3Oxhb51P2M6FseZqLgaqYW1Z2ofUIc01LlfEZiaw8YicgnUTC7ESZcBe7K0zs/640?wx_fmt=png&from=appmsg)

②从任务状态机：

从机任务负责发布或者接听帧的应答。包括两个状态机：

1. 同步间隔段和同步段检查器
2. 帧处理器

5、网络管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDJOyssOIThRd7CMvVnJpYeMqJfr5Pos3icK7TUZx0FvamxlP9zbtibibiahar0dBkicZa03Q6qXibb3nlDjk8as8lLSSjVAcluW1D1Y/640?wx_fmt=png&from=appmsg)

6、状态管理

状态管理是为了**检测运行中的错误**。错误一旦被发现，根据设计需要采取不同的措施进行排除，一种方法是简单替换掉错误节点，另一种方法是让发生问题的节点进入到自我保护/安全模式。

**04**

**帧收发的硬件实现**

**1、组成**

收发 LIN 帧需要的硬件包括协议控制器(Protocol Controller)、总线收发器(Bus Transceiver)和 LIN 总线三部分：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAV469JtHH0JswHUSJNXK6xI2sScZ5JEPFEecqftQjCIJFbaerjPeRSJiaZ74Kicg8ib8IPedTWAwIm0GKULHWLTkpEicO5DAb8qbQ/640?wx_fmt=png&from=appmsg)

**2、硬件特点**

● 从机节点无需高精度时钟源

● EMI（电磁干扰） 低而且可控

● 最高通硬件特点：通信速率 20kbps 。

**3、协议控制器**

协议控制器的主体是一个基于 UART/SCI 的通信控制器，工作方式半双工，可以用“UART/SCI+定时器”实现，也可以使用专用模块实现。特点：协议控制器把二进制并行数据转变成高-低电平信号，并按照规定的串行格式(8 数据位，1 停止位，无校验位)送往总线收发器；接收时，协议控制器把来自总线收发器的高-低电平信号按照同样的串行格式储存下来，然后再将储存结果转换成二进制并行数据。

协议控制器要能执行本地唤醒(Local Wakeup)。需要唤醒总线时，协议控制器通过总线收发器向 LIN 总线送出唤醒信号。协议控制器要能识别总线唤醒(Bus Wakeup)。

实现方案（3类：UART/SCI+定时器+外部中断、硬件 LIN(Hardware LIN)和 LIN 模块(LIN Module)，分别面向对成本和性能有不同侧重的应用）。

**4、总线收发器**

总线收发器的主体是一个双向工作的电平转换器，完成协议控制器的高-低电平与 LIN 总线的隐性-显性电 平之间的转换。LIN 规范要求总线收发器具备这样一种特性：本地节点掉电或工作异常时，不能影响总线上其他节 点工作。协议控制器可以控制 LIN 总线位速率，总线收发器可以控制压摆率。

**5、LIN总线**

LIN 总线是衔接所有 LIN 节点的通信介质。（如果采用 LIN 规范，仅用 3 根线(电源、地和 LIN)就可以实现标准化的数字接口。传感器、执行器通过 总线连接，汽车结构设计可以更加灵活）

时钟源：LIN 网络的主机节点必须设置较高精度的时钟，而从机节点则不必。换句话说，主机节点是 LIN 网络的时间基准，这保证了位速率的准确性。

**6、时钟源**

LIN 网络的**主机节点必须设置较高精度的时钟**，而从机节点则不必。换句话说，主机节点是 LIN 网络的时间基准，这保证了位速率的准确性。

**7、EMI及其控制**

对于 LIN 而言，EMI 主要由位速率和压摆率共同决定。位速率决定单位时间内电平变化次数，压摆率决定电平跳变的快慢。

设计电路注意事项：片上振荡器容易受到环境温度和电源电压的影响，石英晶体容易受到冲击振动的破坏。在选择时钟源时， 一定要考虑使用环境的温度范围、电源电压范围和冲击振动情况。

**8、线与特性**

‘’线与‘’一词常在单片机 二进制罗辑电路中出现，在单片机内部CPU要通过总线，地址对各单元以及单片机外单元进行管理，这时就需要用到罗辑电路，在某单元如有两根地址线，当这个单元被CPU选中，那么这两根线就是‘’线与‘’关系，两根线缺一不可，否则无法完成信息传递。

**9、ESD（静电）危害防护**

LIN 规范要求总线收发器的电源和地应直接连接到 ECU 的接口处。

**10、补充**

①时基(Time Base)为LIN子网的最小计时单位，通常设定为 5ms或 10ms

②网络层传输的包（packet，又称分组），在数据链路层中传输的是“帧”（frame）。数据包到达数据链路层后加上数据链路层的协议头和协议尾就构成了一个数据帧。在每个帧的前部加上一个帧头部，在帧的结尾处加上一个帧尾部，把网络层的数据包作为帧的数据部分，就构成了一个完整帧。

③当数据数据链路层 传输的时候叫做“帧”，当一个帧被接受并提交到第二次处理：剥开帧头帧尾，获得数据包（对于第二层来说它只认识帧头和帧尾，其他包括包头等都是帧承载的普通数据）；然后这个包被提交到第三层：它能识别包头，得到被包在里面的信息（信息包含第四层TCP数据报头，对于第三层来说也是报头也是它承载的普通数据），第三层结束以后把去掉报头的数据给第四层，这些数据就是报文。

**05**

**信号处理、配置、识别、诊断**

**1、介绍**

信号处理、配置、识别和诊断，这四项功能共同构成了 LIN 的 应用层，传输层是配置、识别和诊断这三项功能的通信载体，实现应用层消息与帧之间的格式转换和传输，LIN 为应用层和传输层定义了 API 接口。

**2、传输层**

充当一个“翻译官”，把来自诊断服务的消息(Message)“翻译”成协议层可以处理的PDU (Packet Data Unit，分组数据单元)，或者反过来，把协议层收到的 PDU“翻译”成诊断服务需要的消息。

3、PDU结构

从发送格式上，\*\*PDU 单元可分为\*\*单帧(Single Frame，SF)、首帧(First Frame，FF)和续帧(Consecutive Frames， CF)三种。从发送源上，主机发送请求 PDU，从机发送应答 PDU。

**4、PDU 格式**

包括节点地址(NAD),协议控制信息(PCI),LEN,服务 ID(SID),应答服务 ID(RSID),消息字节段(D1~D6)。首字节 NAD 首先发送，末字节 D4,D5,D6 最后发送。下图：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBUU7KogBngyibMHfW9IKPQhcVxgUTxllhqichTxgZB2icQZWDK3R0Evic6vKy7Kx746z0icIjqdHHeCh7ezbBgMRR3eeHxt2X7gLq0/640?wx_fmt=png&from=appmsg)

①PDU 单元的第一个字节是**NAD**（node address），用于**区分不同从机节点的地址**。

②PDU 单元的第二个字节是 **PCI**

（Protocol Control Information）信息，包含了 **PDU 单元类型和消息字节长度的信息**：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCxIJAibhNx3wLoIf9oy2CEl7WAibCak...