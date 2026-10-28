---
title: 【转载】给NTP加把“密码锁”：网络受限场景下的高安全时间同步方案
url: https://mp.weixin.qq.com/s/DHI1KfDC-tSBvlhCr18p4A
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:42:34.491662
---

# 【转载】给NTP加把“密码锁”：网络受限场景下的高安全时间同步方案

# 【转载】给NTP加把“密码锁”：网络受限场景下的高安全时间同步方案

江南信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**编者荐语**

*Editor's Recommendation*

网络时间协议NTP存在安全短板，在网络受限、高安全等级场景下授时风险突出。本文针对该痛点，构建一套高安全时间同步整体方案，依托国密公钥证书体系加固NTP协议，从软硬件与协议维度研制授时终端，支持设备串联转发授时。经原理样机验证，方案安全可靠、部署成本低，可适配网络不可达等特殊工况，对关键信息基础设施的时间同步安全保障具有参考价值。

**文献引用**

何映伟,杨竞,翟巍,等.一种时间同步的安全增强设计方法[J].信息安全与通信保密,2026(9):113-120.

**摘　要**

目前应用系统内部各设备间的时间同步主要通过有线网络和网络时间协议（NTP）来实现。NTP属于开放性协议，缺乏安全防护措施，易遭受网络攻击；对于有高安全需求的应用设备，仅采用网络对时也难以满足用户使用要求。因此，提出了一种高安全时间同步整体解决方案。首先，建立时间管理服务器，引入公钥证书系统，利用密码技术对NTP协议进行安全加固，完成时间服务器之间的时间同步；其次，从硬件、软件及协议多个层面设计授时终端设备，通过人工方式完成时间服务器与应用设备之间的时间同步；最后，对授时终端设备原理样机进行功能验证，证明相互串联转发时间资源信息具有高效、稳定的特性。该设备成本低、安全性高且操作简单，能够满足网络环境受限条件下的使用需求。

**关键词**

授时；网络时间协议；公钥证书；密码技术；时间资源信息

0

**引　言**

授时及时间同步系统是当今社会正常运行的重要保障，比如银行系统支付交易需要依赖精确时序，电力网络需要同步运行及调度，交通系统需要按时调度，通信网络需要依靠时间同步才能正常工作。

目前，国内主要以北斗卫星导航系统和全球定位系统的时间信号作为主时钟的外部时间基准信号，大多支持硬对时、软对时、编码对时及网络对时等方式。当一个系统中的主时钟获取外部时间基准信息后，系统内部主要采用网络对时和软对时方式来实现各信息设备及仪器之间的时间同步功能。

为实现在网络上的高准确度计算机校时，美国德拉瓦大学的Mills教授于1985年提出网络时间协议（network time protocol, NTP）。该协议可估算封包在网络上的往返延迟，并独立估算计算机时钟偏差，但未采用密码技术防范篡改、假冒等网络攻击行为，安全性很差，较适用于内部可信网络系统。

软对时主要采用串口报文方式，但易受传输距离限制，RS-422接口的传输距离为150 m，延长后会造成时间延时。该传输距离（非直线距离）可能超出操作人员的视线范围，易遭受外界干扰和破坏，存在安全风险。

此外，仅通过网络这一单一方式实现时间同步，难以满足部分特殊应用场景的需求。例如，部分设备及仪器没有网络接口，或处于网络不可达的环境中，如何安全、高效、低成本地解决这些设备及仪器的时间同步问题，亟待研究。

基于上述时间同步所面临的安全保障问题，以及应用需求特点，本文提出了一种安全可行的时间同步保障方案，尤其是在网络不可达或不许网络传输的特殊应用场景下，能有效解决时间同步安全性问题，并显著降低系统运行成本，提高系统抗毁能力。

1

**时间同步安全架构设计**

**1.1 整体方案设计**

在网络可达的环境中，有效解决NTP协议安全性问题无疑是实现时间同步的优选方案。本文通过引入公钥证书系统（基于国密算法SM2、SM3、SM4实现），对NTP协议进行安全加固。为实现特殊环境下的时间同步，本文设计了授时终端设备，利用USB高速传输接口（插孔方式进行连接）和串口相结合的软对时方式，对应用设备及仪器完成时间同步。将NTP协议安全加固与授时终端设备二者结合，形成一个较为安全的时间管理系统，可为有特殊需求的系统和设备提供时间同步安全保障方案。

该方案主要由时间管理服务器、公钥证书服务器和授时终端设备组成，构成一个具有安全保密措施的授时管理系统。该系统从源头获取时间基准信息，在系统内安全同步后，为应用设备安全授时。在构建某个特殊应用场景下的安全授时管理系统时，可采用北京时间或北斗授时系统作为单一时间源来设计处理。安全授时管理系统中各类设备围绕该时间源，在同步过程中实现的主要功能如下。

（1）时间管理服务器：建议采用主机、备机（热备份）机制，以提高系统的可靠性。时间管理服务器可根据当前系统时间，生成特殊需求的同步时间，并通过授时终端设备下发至各个应用终端设备中，完成时间同步，执行相关任务。

（2）公钥证书服务器：基于成熟的商用国家公钥证书系统，构建二级数字证书认证系统，对时间管理服务器和授时终端设备签发数字证书，为设备间信息交互提供身份认证和数据完整性保障服务。

（3）授时终端设备：该设备可以提供多个接 口 类 型（USB、RS-232、RS-422、RS-485）和通信协议，可为各类应用设备提供时间资源，满足不同系统间的时间同步需求。授时终端设备从授时管理系统获取同步时间，并存储在本地，但只能查看，不可更改，以保证时间基准的一致性。同时，授时终端设备成本低、数量多，相互间通过串联转发同步时间，可提高时间同步效率。

以安全授时管理系统为核心，对特殊应用场景下的应用系统提供时间同步保障，其保障体系组成如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdYuEW9xecAgxGYewBgxhc8Ax2hDgvIPuhQz7Yf3Wf9ajUqmrSnkdKXKCKSpDibRML6EMOicynkNiaJugg1sOzWr5Xk0BDJZBfLIAs/640?wx_fmt=png&from=appmsg)

图1 时间同步安全保障体系组成

1.2 **工作流程**

该时间同步安全方案的工作流程如下：

（1）时间校准与网络同步：时间管理服务器中的主服务器依托北京时间获取同步时间资源信息，从服务器定时发起时间同步命令，主动与主服务器保持时间同步。

（2）时间资源信息导出：授时终端设备通过串口或USB接口从时间管理服务器获取时间资源信息，完成时间同步。

（3）时间资源信息串联转发：多个授时终端设备之间采用USB插孔方式串联，通过一键触发自动转发时间资源信息。当上一个授时终端设备完成时间同步后，立即自动向下一个设备发送时间资源信息。

（4）时间资源信息自动载入：授时终端设备通过串口或USB接口与应用设备及仪器连接，自动完成时间资源信息同步载入。自动同步载入过程分为挑战阶段和载入阶段。其中，挑战阶段主要从应用设备获取设备编号或证书信息（可选），以及串口传输速率等信息，通过挑战应答，完成通信双方身份鉴别，并产生认证码；载入阶段主要按照挑战阶段的认证结果，结合认证码信息，完成时间资源信息同步。

2

**NTP协议安全增强方法**

本文设计了一种基于公钥证书系统的NTP协议安全增强方法，能够保障时间同步信息在同步传输过程中的机密性、完整性和身份可鉴别性。发起方在保留协议交互流程和基本格式的基础上，通过SM3杂凑算法计算报文的校验值，并使用公钥证书系统提供的私钥进行签名，再将签名值和证书附在协议报文后。接收方接收到时间同步报文后，先验证发起方证书的合法性；证书通过后，读取其证书中的公钥，对签名值进行验签。如验证通过，则证明该协议报文未被篡改且发起方身份合法。该NTP协议安全增强方法的原理及流程如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdZoWOTRicNzxP3QV74TV9y7ViawicL4nTr70qSQsibKU0DD4ufAZzQcQKf9UXHN6ID0wb8mm5N71TFw8gKVO6VEiaNFL5wohpzXicwHo/640?wx_fmt=png&from=appmsg)

图2 NTP协议安全增强方法原理及流程

**记客户端A和服务器B的对应的证书分别为![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdZIpibHPOTwxbwkwv2aenp1hDOGYICLwRv0KXx6bWicavFOIbvPph9KHkYAibB6sYqwEHricLL5QuQPmE8rSrr90sB9Hzx7DytLEE4/640?wx_fmt=png&from=appmsg)，客户端A和服务器B的身份信息分别记为![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdZia22uogiaQicTX8sGtempteagooPNWV49icD4gTTPemOh4XPLK7iaJTESVhiaXA1anmXfEvicQicQhbfZWqZ79ScOiaic8ZhnjtibRMT5ZY/640?wx_fmt=png&from=appmsg)。![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYuWLmtWsH9q8xdx4QgKX8FV51RL4nkcT0MsTGsAibmHQlap3IGl9MtwaclEy7xuGibYQdyn2POs3BsSUqKBO7Cs7OiceLDiaYK0ibs/640?wx_fmt=png&from=appmsg)表示时间戳，H表示SM3杂凑算法，Sign表示SM2签名及验证算法。**

（1）客户端A计算：在原协议报文的基础上增加身份标识、证书信息和校验码，记基本信息为![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdasjmbEffSNPQlTNM4xz4ic3Awib23wYUJmBAF7OOMzK4caRicW2ibDCiaGZ61ATFc6icibXp1kPmnhFWM6JUg1ItJicy8cFOMT4HHrqOo/640?wx_fmt=png&from=appmsg)，使用自身私钥对C进行签名，![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdYAy7ia9nPicL3byR3yYc29dpsokO7uLkSiaVDZTOO11iczz1c8c3nhfVLxpFKnERPBQofqaV8gr6YVYoYNWeFZed5yybqNZEv3YSY/640?wx_fmt=jpeg)，组成时间同步报文![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdY7zR90icphlIAnGAcjVd2tw7D2kMqYIpQb8qy2fic7IwSMGurvDqHVvD2pmbtXdicWJmwdl9IjFnjVQRJ5FD7SRXT83aiaXpVpyNM/640?wx_fmt=png&from=appmsg)后发送给服务器B。

（2）服务器B计算：服务器B收到报文后，使用杂凑算法计算报文中C的摘要值 H(C)，再使用证书![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYClDNUgdNBNjib007ibzhJcOPh13o9lRMaGeQUl20grERZicuqWgCDYGG8j7cmGxiaFicmMtWribk9JHfA3o2ribsnvTzSibafLrFnNMk/640?wx_fmt=png&from=appmsg)中的公钥对M进行验签，并与计算出的 H(C)比对。如果通过，则证明收到的报文确实来自客户端A，且协议报文在网络上没有被篡改。

同理，服务器B组织应答报文，记基本信息为![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdZaxXrHlj3q4Bx4ECH2aDvUk9S3Z0khoQ0HY95DicEvGIC8czGcGtNSqHlSGb6IZ1LfVRJdDHgBogfruFx3ibLrc4FI9AW7hMz0o/640?wx_fmt=jpeg)，再使用自身私钥对C进行签名，![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdYAy7ia9nPicL3byR3yYc29dpsokO7uLkSiaVDZTOO11iczz1c8c3nhfVLxpFKnERPBQofqaV8gr6YVYoYNWeFZed5yybqNZEv3YSY/640?wx_fmt=jpeg)，组成时间同步应答报文![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdbGYLFZQlMWtks9njjeUcfzUyoTdX3edtAouQCN5CrbbatPP4XsVsGBflDiapZnUbrwibd09qJeaF6HnQkoxwibNHXXvTQ0Gic1fBs/640?wx_fmt=png&from=appmsg)后发送给客户端A。

（3）客户端A计算：客户端A收到应答报文后，使用杂凑算法计算应答报文中C的摘要值H(C)，使用证书![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdapCWc0bnQzOL02PAAzCZSkaDSt5ymV3MPbqrgNicnplYETnxrOrl57g5KI8EiaWibdFw0FgaGa7Xtjej8icw4ypS9WehZqKhe9iaFY/640?wx_fmt=png&from=appmsg)中的公钥对M进行验签，并与计算出的H(C) 比对。如果通过，则证明收到的报文确实来自服务器B，且协议报文在网络上没有被篡改。客户端A通过时间戳![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYuWLmtWsH9q8xdx4QgKX8FV51RL4nkcT0MsTGsAibmHQlap3IGl9MtwaclEy7xuGibYQdyn2POs3BsSUqKBO7Cs7OiceLDiaYK0ibs/640?wx_fmt=png&from=appmsg)信息，计算本机保存的时间资源信息，完成与服务器B的时间同步。

鉴于NTP协议报文主要防范篡改和假冒等网络攻击行为，对机密性要求相对较低，本文仅对摘要值进行签名即可有效防止协议报文被篡改或替换；通过增加证书机制，可有效识别身份，防止假冒行为。此外，由于设计方案中增加了签名、验签环节，在时间同步过程中需要计算摘要值、签名和验签时间，这些时间属于本机处理报文时间，需计入时间资源信息中。至于计算摘要值和签名对设备中央处理器及时间同步精度的影响程度，具体分析见文献[7]，此处不再赘述。

如果某个应用系统确定需要增加机密性防护，各设备之间需先完成基于证书的身份认证和密钥协商，再利用协商出的密钥加密协议报文数据（使用对称密码算法SM4实现），计算出完整性校验值，实现网络传输过程中的机密性与完整性安全防护。

3

**授时终端设备安全设计**

本设计强化顶层设计，采用标准化、模块化设计思路，采购同一型号时钟产品，扩展物理接口，设计并开发定制化管理软件，可为应用系统及其设备、仪器提供时间同步服务，有效保障多个系统领域时间同步应用的精确性、安全性和可靠性。本文从硬件、软件和协议3个部分对授时终端设备原理样机设计进行描述，并对其安全性进行分析。

**3.1 硬件设计**

授时终端设备作为独立设备，对外接口主要有串口和USB接口，用于完成时间资源信息的接收、串联转发及载入等功能。如图3所示，授时终端设备硬件主要由管理模块、接口适配模块、串联模块及电源模块等组成。其中，管理模块用于完成时间资源信息的接收、解析、存储，以及自身硬件的管理、调度等功能；串联模块用来实现多个设备之间时间资源信息的快速转发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYiaILJhcSXogKLTyaB9gAHHQ1DvkyEfe293iadd8nCG7ZZf2yudpVxdz5zEzK6uos7ziblSjjmMXhqibbFsSe9KH8h63C8k46I7tA/640?wx_fmt=png&from=appmsg)

图3 授时终端设备硬件架构

3.2 **软件设计**

授时终端设备软件设计遵循功能全覆盖、性能达标、安全可靠、可扩展、低耦合的设计原则。如图4所示，授时终端设备软件架构包括系统平台软件和应用功能软件，遵循高内聚、低耦合的技术原则，基于软件模块化、层次化、标准化的设计思想，尽量降低各软件模块之间的耦合性，提高软件模块的独立性和可继承性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdbf2MyNvibcdTktibX3XC3pRFkvKzhTNwTl2ovicCrrfTboTu6vzZicPJey5nmqNAUcqoYZemajUQuYeiarVSpicj0hl1vKKQtLmf5to/640?wx_fmt=png&from=appmsg)

图4 授时终端设备软件架构

（1）应用功能软件：应用层包括时间资源信息的接收、管理、销毁，以及串联转发、证书管理等多个应用功能组件。

（2）系统平台软件：设备硬件驱动程序负责上层功能软件与设备硬件之间的数据交互，管理并分配设备硬件资源，支持多线程并发处理。硬件抽象层是位于操作系统内核与硬件电路之间的接口层，使硬件平台与操作系统适配，实现上层设计的平台无关化。

3.3 协议设计

以授时终端设备向应用设备通过串口输出时间资源信息为例，其交互流程如图5所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYnCGZoQ11LzybiaP63DTmO6W4THTUTUksibGpGGZtZhpLufF5icKMVkN4MxIIdSnDU4MV6DsvdSRy1E6BAXNRdLwmOWKEQRA8qO0/640?wx_fmt=png&from=appmsg)

图5 时间资源安全传输协议交互流程

授时终端设备向应用设备发起通信挑战请求，应用设备回复挑战应答报文后，完成身份认证并确认双方共享的认证码参数，后续时间同步报文均需要认证码参与，最终完成时间同步。

通信协议可分为两层：上层为应用层，组织同步时间数据报文，由消息体和消息校验码组成。下层为通信层，如果采用的是串口方式，则使用串行线路网际协议进行封装；如果采用的是高速USB接口方式，则使用USB2.0全速传输协议进行封装。协议结构如图6所示。

![](https://mmbiz.qpic.cn...