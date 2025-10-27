---
title: Bluetooth 蓝牙协议栈技术初探
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497350&idx=1&sn=408c2c2d9e1c1963bbfc89a854b3f89c&chksm=fa522338cd25aa2e6b891127f958069d8aaf0829e3fa1c7a462b7546bb615aace09f8b053a21&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-11-05
fetch_date: 2025-10-03T21:46:02.493782
---

# Bluetooth 蓝牙协议栈技术初探

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPqOicmFOqpjFjqliaoGkKXHjv2YicPmTXt4xibGDnAb8wcagIjB8hP3sGow/0?wx_fmt=jpeg)

# Bluetooth 蓝牙协议栈技术初探

原创

智能安全实验室

山石网科安全技术研究院

**0****1**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPgMRuXKMvBtv5TMJtQ2oicAor2Ap6BiauzEib41KBurJaicwjrBFD9xwJ6g/640?wx_fmt=gif)

**概 述**

“蓝牙”（Bluetooth）原是一位在10世纪统一丹麦的国王，他将当时的瑞典、芬兰与丹麦统一起来。用他的名字来命名这种新的技术标准，含有将四分五裂的局面统一起来的意思。蓝牙技术使用高速跳频（Frequency Hopping）和时分多址（TIme DivesionMuli—access）等先进技术，在近距离内最廉价地将几台数字化设备（各种移动设备、固定通信设备、计算机及其终端设备、各种数字数据系统，如数字照相机、数字摄像机等，甚至各种家用电器、自动化设备）呈网状链接起来。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPbpnv9mrxwgeyoS5j9sShe86dfwz1Vl1l89OMeE0zdBYZx0eWGvg8EA/640?wx_fmt=png)

蓝牙技术在发展至今，衍生出了多个版本，如老的经典蓝牙版本和4.0后的低功耗版本，下面主要讨论蓝牙低功耗也就是BLE。

**0****2**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPgMRuXKMvBtv5TMJtQ2oicAor2Ap6BiauzEib41KBurJaicwjrBFD9xwJ6g/640?wx_fmt=gif)

**蓝牙工作过程**

- 配对：配对是指两个蓝牙设备首次通讯时，相互确认的过程，在通过配对后的数据传输不需要再重复进行确认

- pin：个人识别码，蓝牙使用的pin码长度为1-8个十进制位数

- DB\_ADDR：蓝牙设备地址。每个蓝牙设备被分配了类似mac地址的唯一的一个48位数的设备地址。用于通讯地址确认.两个蓝牙设备在通讯开始时通过询问的方式获取蓝牙设备地址

所以蓝牙的工作过程为：

```
启动 --->> 扫描设备 --->> 设备配对 --->> 数据传输
```

**配对过程：**

**1 ping码配对**

在老的蓝牙2.0协议，配对过程需要输入一个pin码。长度为4到16个数字，在配对过程中通过pin码来生成link key(链路密钥)。两个配对后的设备共享一个link key，这个行为叫绑定。绑定之后下次两个设备接近后，用link key进行认证，认证通过后生成加密密钥进行会话通信的加密。认证的过程采用challenge-response(咨询-响应)的模式，以claimant and the verifie的方式来验证linkkey。认证完一方之后交换身份，再认证另一方，若认证失败，蓝牙设备会间隔一段时间后重试，间隔时间会成指数级增长，以避免攻击

**2 密钥交换配对**

在蓝牙核心规范中，有三个主要的架构层：控制器，主机和应用程序，在主机层中，有一个名为安全管理器(GM)的模块定了一了配对和密钥分发的方法和协议和相应的安全工具箱，以及定义配对命令帧格式，帧结构和超时限制的安全管理器协议(smp）

在建立密钥后，使用这些密钥去加密连接，然后进行密钥共享，这些密钥将用于重新连接后的加密链接，验证签名数据后执行随机地址解析，通常分为以下三个阶段：

- 第一阶段：配对功能交换

- 第二阶段(BLE传统配对)：生成短期密钥(STK) （注：蓝牙4.0和4.1规范定义）

- 第二阶段(BLE安全连接)：生成长期密钥(LTK) （注：蓝牙4.2及以后规范定义）

- 第三阶段：特定于传输的密钥分发

完整的配对流程图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPyI0x7cnDDxjCka9icJj6yjEC4NJTq6woeFZrsU0SVmnsaz6VvxtRAaQ/640?wx_fmt=png)

第一阶段：

配对是安全功能的交换，包括输入/输出(IO)功能，中间人保护的要求等，俩个设备之间的配对信息交换是通过请求和配对响应数据包完成，内容如下表配对请求/响应所示

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPP3iaqtJBHQbHAib1bZ0bKmPg0hF7S2ayGZVDKKOuwx5FfZo6xbYjagiag/640?wx_fmt=png)

第二阶段：

在配对特征交换后，发起方和响应方确定使用密钥生成方法，当密钥生成后，会进入身份验证阶段，用来防止中间人攻击(MITM）攻击，同时根据密钥生成方法去生成用于加密连接链路的密钥，然后进行密钥配对，认证过程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPRcFxjVVzlZIz59jokgzZQE4zk5MuHeDOtaMKjgLmWmTKsWNiaGQODZQ/640?wx_fmt=png)

- 配对由启动设备将其 PKa 发送到响应设备来启动。响应设备会使用自己的 PKb 进行回复。交换公钥后，设备可以开始计算密钥;。

  之后，每个设备选择一个随机的 128 位随机数。此值用于防止重放攻击。

  -Na，起始设备的 128 位随机随机数。

  -Nb，响应设备的 128 位随机随机数。

  在此之后，响应设备然后计算承诺Cb，该承诺使用Nb、PKa、PKb和0进行计算。如步骤 3 中的图 1 所示。

  步骤4，响应设备在接收到发起设备的Na之前必须共享Cb。

  步骤5，发起设备在接收响应设备的Nb之前必须共享其Na。

  步骤6，发起设备在收到响应设备的Nb后，必须检查来自响应设备的Cb。

  此时，启动或响应设备已经知道对等设备的公钥和随机随机数。发起设备可以从响应设备确认承诺 （Cb）。此时发生故障表示存在攻击者或其他传输错误，应配对进程中止，步骤 6.a。

  假设承诺检查成功，两个设备将分别计算 6 位数的确认值，这些值将在其各自的设备上向用户显示。用户应检查这些 6 位值是否匹配，并确认是否存在匹配项。如果没有匹配项，则配对将中止

- 第三阶段：

  身份验证成功后，俩台设备开始计算将用于链路加密的LTK，LTK用于对设备的身份验证，然后建立私密链接，用于传输私密信息。

**03**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPgMRuXKMvBtv5TMJtQ2oicAor2Ap6BiauzEib41KBurJaicwjrBFD9xwJ6g/640?wx_fmt=gif)

**浅析蓝牙协议栈（Bluetooth LE）**

蓝牙协议规定了两个层次的协议，分别为蓝牙核心协议（Bluetooth Core）和蓝牙应用层协议（Bluetooth Application）。蓝牙核心协议关注对蓝牙核心技术的描述和规范，它只提供基础的机制，并不关心如何使用这些机制；蓝牙应用层协议，是在蓝牙核心协议的基础上，根据具体的应用需求，百花齐放，定义出各种各样的策略，如FTP、文件传输、局域网等等

蓝牙协议是由许多层和功能模块组成，有些是必须的，而有些功能和层是可选得。这些部分分布在被称为主机和控制器得两个主要的体系结构块上，而这两个组件的通信方式由他们之间的标准逻辑接口去定义。主机通常是类似于操作系统的东西，而控制器通常是芯片上的一个系统，但蓝牙的规范并不强制此类的实施细节，而主机和控制器作为独立的逻辑，使得架构中的容器可以以某种方式在独立的组件中实现，并为他们之间的通信定义标准接口，从而使得蓝牙可以由不同制造商的主机和控制器的组件组成，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPiagyXibrJk7ceibaG1pIP4suFdvkCCDdCcfYYcUV5LWvS5jwdEXVN8s5A/640?wx_fmt=png)

图2是蓝牙协议栈，图三是osi模型协议栈

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPibfz7nQEjZ2XdsVTFZjOPJ9hpuwWq096aqHzMhIYkgu3e9dA0lwkiapg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhP64ooyFbpibDnvRVKec0N8FHSiaJzrCGA5FOiaPicwiaFzpLVjsT0sibg6eicw/640?wx_fmt=png)

**PHY层浅析：**

蓝牙LE工作在2400MHz到2483.5MHz范围内的2.4GHz的频段，该频段分为40个通道，每个通道的间距为2MHz，但如何使用这些通道是由链路层和数据传输体系结构去定义的，而在这40个信道中，有3个信道是广播通道，分别是37、38、39，用于发现设备、初始化连接和广播数据；剩下的37个信道为数据通道，用于两个连接的设备间的通讯。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPcrWxP57JCudUHR0tmCANQZ0VtrAMib2R9K93OUspzNlfnFQyg0UC6fg/640?wx_fmt=png)

**LL层浅析：**

LINK LAYER层主要用于控制设备的不同状态，具体状态分为一下几种

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhP6UWgztFVgPiaMGHw6ic3R51heic4hsPxhne6tOib70l7wKZv0u6N3FYmYQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPzF85MDEzQBILe8zGLeR6yUiaXCR1qyeqXhekM5glZAVicgX9qnKCTGKg/640?wx_fmt=png)

当两个蓝牙设备链接时，他们采用的时面向异步连接的逻辑传输(简称为acl)

在acl连接上基本包的变换如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPa8doDZQA3C1BXW1icMZlrJWvmPLnpEMVFOF1Olx5vVpbKefJMN2M42g/640?wx_fmt=png)

由c>p知识的两个连接期间，报文传输由中心设备完成，p>c由外围设备完成

在acl过程中连接过程如下

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPWl1MtUqE6j5DcEKHvMCgbdo7WcCxH5yArbvo6MocBARtSwL1feZlfA/640?wx_fmt=png)

数据包在发送后，设备B会进行crc检查，然后将NESE设置为设备A想要的值，然后设备A会使用SN作为设备B的确认，确认它正确的接收了最后一个发送的数据包，但如果设备B收到SN值错误的报文，它就会认为该报文时错误的，设备B会重传接收到的前一个数据包，然后再确认它，但是不会将他进行下一步的处理

但是如果设备A在设备B的回复中收到了非预期的NESN值，或者在设备B的回复中没有收到的时候，设备A会使用原来相同的SN的值重新发送数据包，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPTC2vCzeyOiaPI7v47yk8xPKu28jBETbpl7otUKXt9BzJM2fWvtVMwsg/640?wx_fmt=png)

**HCL层浅析：**

在HCL中，是通过包的方式来传送数据，命令和事件的，所有在主机和主机控制器之间的通信都以包的形式进行，包括每个命令的返回参数都通过特定的事件包来传输，HCL有数据，命令和事件三种类型的包。命令包COMMAND(0X01)只能从主机发往主机控制器，其中数据包是双向的，分为两类：ACL（0x02）、SCO（0x03），而事件包EVENT（0x04）始终是主机控制器发向主机的。

命令包和数据包发送在主机和控制器交换如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhP00vfTeJK52EZvqrKmPIM6vvGMm49OJEZ1XvfaqVxgg6ibjZgyZiap3icw/640?wx_fmt=png)

主机发出的大多数命令包都会触发主机控制器产生相应的事件包作为响应，在传输过程中会有一个句柄，用于识别主机之间的逻辑通道和控制器，共有三种类型的句柄：连接句柄、逻辑链路句柄和物理链路句柄。

在传送的数据包中我们重点关注ACL数据包：

ACL数据包格式：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPj4BWVRoDxicfsfEicDQeyE3aXVERSxlhkdUgFKOppsoECfzkaHUdS0gw/640?wx_fmt=png)

**L2CAP层浅析：**

L2CAP使用通道的概念来分离在堆栈层之间传递的数据包序列。固定通道不需要设置，立即可用，并与特定的高层协议相关联。还可以动态创建通道，并通过指定的协议服务多路复用器(PSM)值与协议关联。

如果将acl理解为ip的话，可以将L2CAP层理解为tcp/udp协议，L2CAP层实现了更为完善的数据传输功能，实现的主要功能如下：

- 分割和重新组装

- 重传和流量控制

- 封装和调度

- 分片和重组

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPw8TOfRpMxicibkgbL9iau9r1PlPNefYTDDWRjeHD85NLseHrkJdHoWfTA/640?wx_fmt=png)

相关术语：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPUqPEiceeAKSu54VJibGT68iclOe4APGP7RQNKvMk1giaicsPjrBePBRonJQ/640?wx_fmt=png)

链路层数据包的PDU字段可能包含各种不同的协议数据单元(PDU)，这取决于蓝牙LE的使用方式。固定频率扩展信号(CTE)只在使用两种测向方法(AOA或AOD)中的一种时才会出现

L2CAP数据包格式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPUWhno6DJknQOQ8V4ibNVOqq3Itpbcnby2eIr55woXHarrFYYvARWvHA/640?wx_fmt=png)

**ATT层浅析：**

ATT由俩台设备使用，一台为客户端，另一台为服务器，服务器会公开一系列称为属性的组合数据，而这些属性由服务器组织在一个被称为属性表的索引列表中

每个属性包含一个句柄，一个唯一标识符(uuid)，一个值和一组权限，而属性可以理解为一个信息，比如温度，湿度，时间等信息，被服务器存储并开放一些方法供客户端读取和去修改这些属性

**GATT层浅析：**

GATT基于属性表中的属性定义更高级别的数据类型，这些数据类型被称为服务，特征和描述符。它还定义了通过ATT使用这些数据类型所涉及的一系列过程，应用程序通常使用映射到这些过程的平台api。

服务是一种分组机制，它提供了一个上下文，在该上下文中使用它们包含的特征并具有已定义的类型。服务通常与设备的主要功能或功能相对应。

特征是状态数据的单个项，具有类型、关联值和一组属性，这些属性表明如何根据相关GATT程序集使用数据。例如，可以定义一个连接的对等设备可以读取一个特定特性的值，但不能写入它。

特征属于一个服务。相同的特征类型可以是多个服务的成员，根据这些服务提供的不同上下文，使用特征的规则可能会有所不同。服务规范将提供这些细节。

描述符属于某些特征，可以包含元数据，比如特征的文本描述，或者可能提供控制特征行为的一些方法。

服务，特征和描述符的层次结构如图所示

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhPQiambZRibYSvgvSNtorW5q65VXibWCOtGgxt1ibAf1SByPvIgtGl8agxgQ/640?wx_fmt=png)

**GAP层浅析：**

GAP层定义了四种设备角色，分别如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8libhP8LUwQ0gnjRvPKPzQMFJBNwAAsll38UmvQicdOkfUwroNsFwvTRnBGHQ/640?wx_fmt=png)

**BLE报文类型:**

链路层定义了两种报文类型。第一个是由未编码的PHY使用，LE 1M和LE 2M，第二个是由LE编码的PHY使用。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTOicKPFbt1TBLqBmUK8...