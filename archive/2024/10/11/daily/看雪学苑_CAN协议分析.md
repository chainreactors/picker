---
title: CAN协议分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458577983&idx=2&sn=ecc8784d0787b770919741ce649bd197&chksm=b18ddcb586fa55a336b1123f9bc159fcdaa8aeb3f0e28bc4f8dc30eb7850ae8299d90858ec04&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-11
fetch_date: 2025-10-06T18:52:30.154198
---

# CAN协议分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUIDdTAGUicibOKCCicH3ls74IGqOTpKhxNx42JYrdrFp5autCZRMp27hFA/0?wx_fmt=jpeg)

# CAN协议分析

gir@ffe

看雪学苑

```
一

概述
```

CAN 协议即控制器局域网络 (Controller Area Network)简称，由研发和生产汽车电子产品著称的德国 BOSCH 公司开发，成为国际标准ISO11519以及ISO11898。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicU1d3H47lPw5Yv59BBiaWYelFIiamwaEG41Fr6zkAh9XleNX2e6fZawahw/640?wx_fmt=png&from=appmsg)

CAN 总线协议已经成为汽车计算机控制系统和嵌入式工业控制局域网的标准总线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicU4FBKqQGck0NpeibgN4NSv4gADIeplKiaHJLDCh0TZWnDGEPb7FdE9eAQ/640?wx_fmt=png&from=appmsg)

```
二

CAN协议构成
```

can协议分为物理层和协议层

## CAN协议物理层

###

### 1.通讯方式

CAN使用异步通信，利用CAN\_High和CAN\_Low两条信号线组成的差分信号线进行通讯（和传统的时钟通信不同）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUK1Tv12RdM5Ffq8z44vhVm7SMI8ufCrybib22Ief8HicObY1dvTaxRaicA/640?wx_fmt=jpeg&from=appmsg)

####

#### 传输速率

500kbps和125kbps的总线分别针对不同类型的ECU。

◆500kbps CAN总线连接了ABS（防抱死制动系统），SAS（转向角传感器），ETM（发动机电子控制模块）和ECM（电子控制模块），通常用于传输速率要求较高的控制信号。

◆125kbps CAN接口连接了DDM（所有权门模块）和PDM（电梯门模块），通常用于传输速率要求较低的控制信号。

#### 差分信号

差分信号通信是一种通过两条导线（或信号线）传输数据的方式，主要用于提高抗干扰能力和信号完整性。

##### 概念

在差分信号通信中，同一信号的两个版本会同时在两条导线上传输：

◆**正信号（+）：**原始信号

◆**负信号（-）：**原始信号的反相版本

例如：

如果正信号是高电平（+5V），负信号就是低电平（0V）

如果正信号是低电平（0V），负信号就是高电平（+5V）

##### **信号的产生**

发送端通过一个差分驱动器（或发送器）生成差分信号：

◆**正信号线（D+）：**直接传输原始信号

◆**负信号线（D-）：**传输原始信号的反相信号

例如：

当发送逻辑“1”时，D+线上为高电平，D-线上为低电平

当发送逻辑“0”时，D+线上为低电平，D-线上为高电平

##### **信号的传输**

差分信号通过两条导线同时传输，导线之间的电压差（即差分电压）决定了信号的逻辑状态：

差分电压 = D+ 电压 - D- 电压

◆逻辑“1”通常表现为正的差分电压（例如 +2V）

◆逻辑“0”通常表现为负的差分电压（例如 -2V）

##### **信号的接收**

接收端使用差分接收器来解读信号

差分接收器不直接读取D+或D-的电压值，而是`读取它们之间的电压差`：

◆如果D+的电压高于D-的电压，接收器将其解读为逻辑“1”

◆如果D+的电压低于D-的电压，接收器将其解读为逻辑“0”

##### **抗噪声原理**

当外部噪声（如电磁干扰）影响到传输线时，通常会同时影响到D+和D-两条线，使它们的电压同时上升或下降。

但由于接收器只关注两条线之间的电压差，这种共模噪声不会改变信号的逻辑状态，因此可以被有效抑制。

#### CAN 协议中的差分信号规范

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUgHYk1hONu690qDw8sFSy8siak2dZNJ6wPsOwzLjBMSrM8pUh1Oq3Sow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUNIlG0WNLgt0zaQs3ic7DccQFo4KjWadReAPeRJLdKLJdepITXOujQoQ/640?wx_fmt=png&from=appmsg)

CAN 总线协议的物理层，只有 1 对差分线，在一个时刻只能表示一个信号，所以对通讯节点来说，CAN 通讯是半双工的，收发数据需要分时进行。

CAN 的通讯网络中，因为共用总线，在整个网络中同一时刻只能有一个通讯节点发送信号，其余的节点在该时刻都只能接收。

### 2.总线网络

can的物理层的形式有两种

◆ISO11898 标准的高速、短距离“闭环网络”

◆ISO11519-2 标准的低速、远距离“开环网络”

#### 闭环网络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUNrkpujgbLR77obpyg4B2vsJ1VpGYicK6FDNz0DdE6WD7icAYQZegcIGA/640?wx_fmt=png&from=appmsg)

◆总线最大长度为 40m

◆通信速度最高为 1Mbps

◆闭环总线两端各有一个120Ω的电阻

#### 开环网络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUo3ibwPMT1hkxUfZ6icUrGoSQVc1vy8iaCBMF7GzkGW4BJUm2jUhvYSSLw/640?wx_fmt=png&from=appmsg)

总线最大长度为 1km

最高通讯速率为 125kbps

每根总线串联一个2.2kΩ的电阻

### 3. 通讯节点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUxNJiarQcWeibcseeXcYDbElpZlM6WwPWS8Fyoicx5peHQhficFic4ACNjRw/640?wx_fmt=png&from=appmsg)

####

#### 通讯节点构成

◆一个 CAN 控制器及 CAN 收发器构成

◆通过 CAN\_Tx 及CAN\_Rx 信号线连接控制器与收发器

◆通过 CAN\_High 及 CAN\_Low 信号线连接收发器和 CAN 总线

◆CAN\_Tx 及 CAN\_Rx 使用普通的类似 TTL 逻辑信号

◆CAN\_High 及 CAN\_Low 是一对差分信号线

#### 多通讯节点挂载

一个总线可以挂载多个节点，CAN 通讯协议不对节点进行地址编码，对数据内容进行编码的。节点个数理论上不受限制（总线的负载足够即可，通过中继器增强负载）

#### 通讯节点通讯流程

接收和发送流程相反

##### **发送数据**

◆控制器把要发送的二进制编码通过 CAN\_Tx 线发送到收发器。

◆收发器把这个普通的逻辑电平信号转化成差分信号。

◆通过差分线 CAN\_High 和 CAN\_Low 线输出到 CAN 总线网络。

##### **接收数据**

CAN 总线网络将数据通过差分线CAN\_High 和 CAN\_Low 发送。收发器把总线上收到的 CAN\_High 及 CAN\_Low 信号转化成普通的逻辑电平信号，最后通过 CAN\_Rx 线输出到控制器中。

### CAN电平转换芯片（部分）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicU0Km7QlY5cVwx9ySic8HJiadnhZflMjm35GOwd5ErmDL4bibicSQBufWMWg/640?wx_fmt=png&from=appmsg)

##

## CAN协议协议层

### 1.波特率及位同步

#### 通讯的波特率

==总线上的各个通讯节点只要约定好 1 个 Tq 的时间长度以及每一个数据位占据多少个 Tq，就可以确定 CAN 通讯的波特率==

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUNAaPRPAYl9pGwm3JmXfbG6lKUQ3ZTAKr9libtsEfaGX1el5XCpWkhKg/640?wx_fmt=other&from=appmsg)

```
SJW[1:0]再同步补偿宽度
TS1[3:0]时间段1
TS2[2:0]时间段2
BRP[9:0]波特率分频器
SS同步段恒等于1
设置APB1的时钟频率，STM32F1通常为36MHz（外部8M晶振）
```

详细计算方式参考：CAN总线波特率的设定——以STM32F103为例 - 知乎 (zhihu.com)

**示例：**

假设1Tq=1us，而每个数据位由 19 个 Tq 组成，则传输一位数据需要时间；

T1bit=19us，从而每秒可以传输的数据位个数为：1x10次方/19 = 52631.6 (bps)

每秒可传输的数据位的个数即为通讯中的波特率，CAN 属于异步通讯，没有时钟信号线。连接在同一个总线网络中的各个节点会像串口异步通讯那样，节点间使用好的波特率进行通讯。（同时使用“位同步”的方式来抗干扰、吸收误差，实现对总线电平信号进行正确的采样，确保通讯正常）

#### 位时序分解

CAN 协议把每一个数据位的时序分解成SS 段，PTS 段，PBS1 段，PBS2 段

，四段的长度加起来即为一个 CAN 数据位的长度。

分解后的最小时间单元为Tq（一个完整的位由 8~25 个 Tq组成）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUkvN5ysKXKVibph7Yj6h5c6lVQqUgibTGIcCoVPyxmlaEztRqxl971zOA/640?wx_fmt=png&from=appmsg)

（此处高低电平直接代表信号逻辑 0 或逻辑 1）

示例的的数据：位长度为19Tq

◆SS 段占 1Tq

◆PTS 段占 6Tq

◆PBS1段占 5Tq

◆PBS2 段占 7Tq

##### **SS段**

同步段（大小固定为 1Tq）

==检测到总线上信号的跳变沿被包含在 SS 段的范围之内，则表示节点与总线的时序是同步的==

##### **PTS段**

传播时间段（大小为 1~8Tq）

==补偿网络的物理延时时间==，总线上输入比较器延时和输出驱动器延时总和的两倍

##### **PBS1 段 (PHASE SEG1)**

相位缓冲段（大小为 1~8Tq）

==补偿边沿阶段的误差==，它的时间长度在重新同步的时候可以加长

##### **PBS2 段 (PHASE SEG2)**

另一个相位缓冲段（大小为 2~8Tq）

==也是用来补偿边沿阶段误差的==，时间长度在重新同步时可以缩短

#### 同步过程分析

简述同步：使数据接收方能够正确地解释和处理从发送方接收到的数据，确保接收方能够准确地识别出每个数据位的开始和结束。

CAN的同步分为两种：硬同步和软同步

#####

##### **硬同步（针对短帧传输）**

硬同步是当CAN节点在总线上检测到一个**显性边沿**（即从隐性位跳变到显性位）时进行的同步操作

###### **隐性位跳变到显性位：**

◆**显性位（Dominant Bit）：**表示逻辑“0”

◆\*\*隐性位（Recessive Bit）：\*\*表示逻辑“1”

◆**边沿（Edge）：**边沿是指信号从一个状态转换到另一个状态。例如，从隐性位（逻辑1）跳变到显性位（逻辑0）时，这种转换称为“显性边沿”

###### **工作原理：**

◆帧起始位（SOF）：

◆触发硬同步：

###### **示例：**

假设有两个CAN节点，节点A（发送方）和节点B（接收方）（同一个CAN总线上通信）。

节点A准备发送一帧数据，节点B则负责接收该帧数据。

1.总线处于空闲状态

在开始通信之前，CAN总线处于**空闲状态**，此时总线的电压处于隐性位（逻辑1），节点A和节点B都在等待总线的变化。

1.节点A发送数据帧起始位（SOF）

节点A开始发送一个数据帧。CAN通信的规则规定，帧的开始由一个**显性位**表示，称为**帧起始位（SOF）**。因此，节点A从隐性位（逻辑1）切换到显性位（逻辑0），即电压变化使CAN H和CAN L线之间的差异增加。

1.节点B检测到显性边沿并进行硬同步

当节点B在总线上检测到这一从隐性位跳变到显性位的电压变化（显性边沿）时，它会执行“**硬同步**”操作：

◆节点B内部的**位时钟**会被立即**重置**，并开始一个新的计时周期

◆这个计时周期与节点A发送数据时的周期对齐，确保节点B能与节点A同步读取接下来的数据位

##### 重新同步（针对长帧传输）

在长帧传输时，（时钟漂移导致节点的时钟和总线的时钟出现偏差）确保节点的时钟与总线保持同步

###### 基本原理：

CAN节点的内部时钟（位时钟）与总线上的信号发生了偏移，

重新同步通过检测==普通数据位的跳变沿（从高电平到低电平，或从低电平到高电平）==来对齐时钟

###### 相位超前（时钟快）：

节点的时钟比总线时钟快，这意味着节点会比总线更早检测到数据位的跳变沿

==通过延长相位缓冲段1（PBS1）的时间来使节点的时钟与总线对齐==

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUwSiblRwA1bAyHIicricNnd2PU2TShEibehj4g3pXTfhTw5JQ2PbqFIVMCg/640?wx_fmt=png&from=appmsg)

###### 相位滞后（时钟慢）：

节点的时钟比总线时钟慢，节点在总线跳变沿之后才检测到信号

==通过减少相位缓冲段1（PBS1）的时间来赶上总线时钟==

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUDPCknxCw1ZQNlnVETo0viaOAqleuPCjgAYsic0LicIJwh1dJXE3UdkzEw/640?wx_fmt=png&from=appmsg)

##### 重新同步补偿宽度（SJW）

调整时钟的一种机制，用来修正节点时钟与总线信号之间的偏差

###### 最大SJW的限制

CAN控制器通常会为SJW设置一个最大值(单次同步操作中，时钟的调整范围不能超过设置的最大值)

偏差超过最大值（不能再一次完成），只能通过多次小幅度的调整完成

###### PBS1 和 PBS2 的调整

◆**PBS1**（相位缓冲段1）：

◆**PBS2**（相位缓冲段2）：

### 2.报文种类及结构

SPI 通讯，片选、时钟信号、数据输入及数据输出这 4 个信号均有单独的信号线。

I2C 协议，包含有时钟信号及数据信号 2 条信号线，异步串口包含接收与发送 2 条信号线。

但是CAN只有两条差分信号线（只能表达一个信号），所以CAN协议==对数据、操作命令 (如读/写) 以及同步信号进行打包，打包后的这些内容称为报文。

#### 报文种类

```
传输起始标签+片选（识别）标签+控制标签+原始数据段+CRC校验标签+应答标签+传输结束标签
```

把上述的内容按照特定格式打包，可以用一个通道表达各种信号，对应设备按照格式去解读就能还原数据——CAN的数据帧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUkFHmUicWpmumnUibQFjyhNzkcS60IyfAgyxfRWuOBhwkdOOOiaRLF5Cog/640?wx_fmt=png&from=appmsg)

####

#### 数据帧结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUTFNUYt5wJaFPvSHnWJ36ZEl5Of6xNWpNo3OpKHa8EYNPHOpYRCFMug/640?wx_fmt=png&from=appmsg)

开始：（帧起始）

一个显性位 (逻辑 0)

中间：

仲裁段，控制段，数据段，CRC 段，ACK 段

最后：（帧结束）

7 个连续的隐性位 (逻辑 1)

#### 仲裁段

==多个报文发送时，根据仲裁段决定具体的传输报文==

##### 仲裁原理：

◆物理协议基础：总线上同时出现显性电平和隐性电平，总线的状态会被置为显性电平

◆==若两个节点同时竞争 CAN 总线的占有权，当它们发送报文时，若首先出现隐性电平，则会失去对总线的占有权，进入接收状态==

◆示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGV8qib5bWjnCGzDjoodkicUw7lNTZtzHNwdXm68MQ4Uu70dyHlSrEnaFhFTeHH0r4DSTYCTfjWymQ/640?wx_fmt=png&from=appmsg)

开始阶段，两个设备发送的电平一样，所以它们一直继续发送数据。

箭头时序处，节点单元 1 发送的为隐性电平，节点单元 2 发送的为显性电平，总线的物理协议基础使它表达出显示电平单元 2 竞争总线成...