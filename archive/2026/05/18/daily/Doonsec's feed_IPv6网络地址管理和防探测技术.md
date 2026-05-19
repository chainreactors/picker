---
title: IPv6网络地址管理和防探测技术
url: https://mp.weixin.qq.com/s/2NbYgqepLDAVK03CTlEmSw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:02:38.180058
---

# IPv6网络地址管理和防探测技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdbic91ePXJCsDicIDJTF0e4G0aIXz1uL6KR2MOxJY2nqJGkYibqTtLVwNjReT1ibKeDwVQ84t1IzSLuWHH1Xe5kxYsuZ6EKAcKlCgs/0?wx_fmt=jpeg)

# IPv6网络地址管理和防探测技术

原创

Cismag
Cismag

信息安全与通信保密杂志社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语

本文提出一套主动防御组合拳：通过加密生成稀疏分布的IPv6地址，让扫描工具“大海捞针”；同时融合蜜网和隐马尔可夫干扰流量，让攻击者真假难辨。这套方案从侦察源头延缓攻击节奏，为IPv6大规模部署提供了可落地的内生安全思路。

**引用本文**

韩百然 , 刘雷刚 , 郭长杰 , 等 .IPv6网络地址管理和防探测技术[J]. 信息安全与通信保密 ,2026(1):91-102.

**文章摘要**

IPv6作为下一代互联网基础通信协议，世界各国正加快对其的部署与推广。收集资产信息是发起网络攻击的前置准备之一，已有大量研究基于深度神经网络等算法预测IPv6编址规则，在已知种子地址的场景下，探测命中率近20%。通过特定的地址生成和管理方法，在不损失IPv6地址层次划分信息的基础上，生成在地址空间中呈稀疏分布的IPv6地址，同时结合蜜网融合，造成IPv6地址空间内海量资产活跃的假象，并利用未分配地址集，诱捕网络攻击流量。针对被动探测方式，提出一种基于隐马尔可夫模型的随机干扰流量生成算法，在真实网络流量中加入干扰噪声。最后通过实验比较，采用地址生成和管理方法后，已有IPv6探测工具扫描命中率大幅下降。

**0 引  言**

IPv6（Internet protocol version 6）是IPv4协议的升级版本，其在地址空间大小、编址能力、协议安全性和性能等方面均有提升。随着边缘计算、协同感知等信息技术的成熟应用和需求增加，世界各国正在积极部署IPv6协议升级，并探索IPv6+创新应用场景。根据罗兰贝格咨询公司的报告数据，中国、日本、美国、法国等国家在IPv6渗透率、应用效果、创新等方面处于领跑者地位。

许多在IPv4网络中存在的攻击方式，在IPv6网络中仍然存在，但由于IPv6地址空间大、协议工作机制变化等原因，针对IPv6的攻防模式也同步发生改变。MITRE公司开发的攻击链模型将网络攻击在战术层面分为侦察、资源准备、初始访问、执行攻击等步骤，其中收集目标资产信息是发动攻击的首要环节。本文提出一种地址生成算法和网络防探测技术，在实现IPv6地址资产易于管理的同时，可以有效降低活跃地址探测命中率。

**1****相关研究**

1.1 IPv6地址结构、分配方式和探测研究

1.1.1 IPv6地址结构

IPv6地址共128位，地址类型主要包括全球单播地址、回环地址、组播地址、链路本地地址和未指定地址。其中，全球单播地址类似于IPv4的公网地址，其结构由3个部分组成，即全球路由前缀、子网ID和接口ID，如图1所示。一般而言，全球路由前缀和子网ID共64位，接口ID为64位。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdarrVNLBNDSzWXLA9mccK6PjQldtibFfUhmObaZcWm8iaXmQtRzVdp6QRg3VKpJNOU52nUaOLP4WpUic2pFSXqN05Grqh9hLupevY/640?wx_fmt=png)

图1  IPv6 地址结构

IPv6地址的自动获取方式主要包括IPv6动态主机配置协议（dynamic host configuration protocol for IPv6, DHCPv6）和无状态地址自动配置（stateless address autoconfiguration, SLAAC），2种方式的分配流程如图2所示。DHCPv6分配方式定义于RFC3315标准中，其分配过程大致分为4个阶段：

（1）客户端广播发送DHCP Server Solicitation请求；

（2）DHCP Server处理请求，并回复DHCP Server信息或丢弃处理；

（3）客户端根据收到的DHCP Server信息，向DHCP Server发送Request、Renew、Rebind、Release或Decline消息；

（4）DHCP Server处理并回复客户端请求；

（5）客户端进行重复地址检测（duplicate address detection, DAD），检测通过后启用地址。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdbXFvXFqE03ic3COj7yaau7zRb6GnQcm7baa1DnNoyZYL2TInquBrrstmGc1x9nofCO66icu4vQJU0DA8k9MDWO969dyNHiczUQKs/640?wx_fmt=png)

图2  DHCPv6和SLAAC地址分配流程

SLAAC分配方式定义于RFC7527标准中，其分配过程大致分为3个阶段：

（1）客户端从路由器通告（router advertisement, RA）中，获取路由前缀及是否启用SLAAC等信息；

（2）客户端根据前缀信息以及本地媒体访问控制（media access control, MAC）地址或随机信息生成IPv6地址；

（3）客户端进行DAD，检测通过后启用地址。

1.1.2 IPv6地址生成方式

RFC4291标准中定义了“IPv4-Mapped IPv6 Address”，其后32位嵌入IPv4地址，用来映射IPv4到IPv6地址。张博文等人通过在IPv6地址中嵌入网络租户信息，提升了对租户流量的溯源和访问控制能力。何林等人设计一种需求驱动的IPv6地址生成系统，将地址生成操作归纳为翻转、插入、拼接等简单操作，以及加密、哈希等复杂转换，根据不同的生成需求，在地址中嵌入相应的特征信息。陈越等在IPv6地址中以加密方式绑定主机身份信息，安全网关通过对身份签名进行验证以判定主机是否可信。Liu等人提出了网络身份与时序生成地址（network identity and time generated address, NIDTGA），在IPv6地址中嵌入网络标识（network identifier, NID）和时间信息。

1.2 IPv6地址探测研究

IPv6地址探测主要有3种方式：一是依赖域名解析系统或众包平台等公开网络资源进行获取；二是被动探测方式，通过内容分发网络（content delivery network, CDN）、网络时间协议（network time protocol, NTP）及核心交换设备的日志和流量信息提取地址；三是主动探测方式，根据是否存在种子地址又分为有种子探测和无种子探测，主要借助深度学习、聚类、生成对抗网络等算法推测地址编址的规律，生成候选地址集并进行探测。

在已有研究中，方亚开等在IPv4和IPv6双栈运行的过渡阶段，先通过地址解析协议（address resolution protocol, ARP）探测得到活跃的IPv4地址，然后借助域名系统获取其关联的IPv6地址。宋光磊等人通过神经网络挖掘边界网关协议（border gateway protocol, BGP）前缀与地址配置模式之间的潜在关联，并引入预探测机制对生成的地址进行特定比例的探测。陈勇群等人基于生成对抗网络产生IPv6地址候选集并进行探测。Williams等人利用强化学习算法逐步缩小IPv6地址空间搜索范围，以提高扫描命中率。Song等人设计了AddrMiner地址探测系统，并对层次聚类算法（divisive hierarchical clustering, DHC）进行改进，提出了基于密度的动态反馈算法（DET）。AddrMiner系统包括有种子探测（AddrMiner-S）和无种子探测（AddrMiner-N），系统借助深度学习、强化学习等方式分析地址生成规律。在AddrMiner官方网站上，团队持续维护IPv6地址探测集合，并定期进行复测。

**2****IPv6地址采集和分析**

2.1 数据采集

本文从RIPE网址公开数据集（https://ftp.ripe.net/ripe/ipmap/）收集了近百万条IPv6地址、经纬度等信息。

2.2 数据分析

同一组织往往采用相同的地址编址规则，因此可以通过对相同地区的IPv6地址进行经纬度聚类，将聚类后的地址集合视为隶属于相同组织，以进一步分析其编址规律。以数据集中的2个不同地区为例，图3为聚类后的结果，可以看出地区1和地区2经聚类后分别划分为6个不同的组织。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdaak4tY3ux6KHicTo24faY2g1Ybx2w9M9I2wQMmxlo4fPwS2689DesFtTT8W8ERiamGQT0FpDymaQEqwTa9ytF9pyADvlJ5M9maM/640?wx_fmt=png)

图3  根据经纬度聚类后的地址集合

通过计算每个聚类后IPv6地址集合的信息熵，可以评估IPv6地址生成的随机性。信息熵常用于描述信息源事件发生的不确定性：事件随机性越高，其所包含的信息量越大，信息熵越高；反之，随机性越低，信息熵也越低。信息熵的计算式为

H(X)=∑P(X)log2P(X) （1）

式中：P(X)为事件X取某个值的概率。

本文针对图3中2个地区聚类得到的地址集合，计算了IPv6地址每个半字节位的信息熵，结果如图4所示。从图4可以看出，在IPv6地址的接口位，高比特位的信息熵普遍较低。这是因为在IPv6地址的层次结构设计中，高比特位常绑定地理位置、组织机构、业务属性、身份标识等信息，随机性较低；而低比特位的随机性则相对较高。在地址探测过程中，结合收集的网络位（Prefix）信息、种子地址的接口位编址规则，可以有效提高地址探测的命中率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdYqW75vkFTPFn7luHy5d8uTdMQ58hmUibHqVibjZmOBSwrTImbGuzYibwmWnVk9KAKrhwASIWT5c0chiciacBRd8e701YLu1jfhpS70/640?wx_fmt=png)

图4  信息熵热力图

**3****地址生成管理系统设计**

传统的全量资产探测方式已不适用于IPv6网络。以一个64位网络前缀位对应的地址空间为例，可以分配的IPv6地址数量约1.84×1019个。假设按每秒100万个数据包的速率进行探测，遍历该地址空间需要约580万年。通过地址生成管理系统对IPv6地址资源进行统一管理，并结合地址生成算法，能够有效降低主动探测的命中率。

3.1 地址生成算法设计和应用场景

为便于IPv6地址资源管理，所设计的地址生成算法应具备如下特征：

（1）网络位与组织内部路由规划关联，不改变原有编址结构；

（2）生成的地址不损失原地址规划中的业务和身份等信息；

（3）生成的地址在地址空间中分布足够稀疏，难以被推测出规律；

（4）地址管理无需绑定额外标识信息，不引入复杂的密钥管理流程，数据结构简单清晰。

图5是地址生成算法设计原理。该算法通过密钥管理服务器，结合8位随机序列作为salt值（即盐值），派生出具有随机性的加密密钥，并基于此生成加密转换后的地址。该过程在隐藏原始IPv6地址生成规则的同时，使分配地址在地址空间中呈现高度稀疏分布。此外，该系统还融合蜜网策略，响应全部探活请求和攻击流量，造成全部资产活跃的假象，并帮助防守者锁定攻击来源，有效识别零日漏洞等攻击风险。以下结合4个典型应用场景，详细描述地址生成算法的运行方式。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdad8sy0MhJba4ZDbofibuaRWfdeCtGOPkcQlvZmwmho9PzP45UZCWBN8YnN60orEtChfATb6J8c9KoZialD3ibhYqFAlwpD0hOb8Q/640?wx_fmt=png)

图5  地址生成算法设计原理

3.1.1 场景1：用户地址分配

步骤：（1）用户发送DHCP地址请求；（2）系统根据用户接入信息预分配IPv6地址；（3）IPv6地址接口位预留8位作为盐值，其他56位使用AES CTR模式加密；（4）将（3）加密后的地址返回给用户。

3.1.2 场景2：非法地址违规使用检测

步骤：（1）用户配置IPv6地址后，发送邻居请求（neighbor solicitation, NS）进行DAD检测；（2）系统处理NS，若用户使用的地址不在规划地址集中，则判定为违规使用，需构造虚假邻居通告（neighbor advertisement, NA）阻断连接；（3）记录告警信息。具体过程如图6所示。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdbszsercJicPc6V5NpibWCpGjGjkBGdoSicnCAgHKSq3QCC7pzhnq01LAia7qO6ERKB1QD2Q5d4JeUPomhycEDy9CR57WZ9OiaFdm1w/640?wx_fmt=png)

图6  非法地址违规使用检测和蜜网流量诱捕

3.1.3 场景3：蜜网流量诱捕

步骤：（1）镜像网络访问流量到系统。（2）若数据包目的地址不在已经分配的地址集中，则通过代理将请求流量转发到蜜网系统。（3）判断数据包类型，若数据包为资产探活类请求，则构造虚假资产在线响应；若数据包为Web服务、漏洞探测等请求，则由蜜网服务进行响应。（4）将非法地址和攻击告警上传至统一告警平台。具体过程如图6所示。

3.1.4 场景4：安全设备访问策略配置

步骤：（1）基于访问需求，确定访问控制规则；（2）根据原始地址集，生成转换地址集；（3）将转换地址集批量导入安全设备。

3.2 生成地址数据分析

采用3.1节的地址生成算法，针对图3中2个地区聚类得到的地址集合进行转换，转换后的信息熵如图7所示。接口位每半字节信息熵接近最大熵8，即转换后地址的每半字节在取值上趋于平均分布，具有极大的随机性。生成的IPv6地址在地址空间中呈高度稀疏分布，攻击者难以通过主动扫描探测，大量的网络噪声也使其信息收集行为更易于暴露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdakQQAcb3V4o5aM7YYXaNouABBUbYfcE6vSrwnkTYKZxwNicjAiaM82qQxCXicPkyHSuDbZ0PBAszYZR00icsBUQCAP3hH4qCONDOQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdbwDtqPVib8xocRN46C3J7IZ7MibwTtJkdIsh3YQneCVEPic1ILWE4ZZN4nPRylGzQART3gWiaiarPhCn7nSicUveeBG5GImqopjmYpM/640?wx_fmt=png)

图7  转换后地址集信息熵热力图

**4 网络防嗅探系统设计**

除主动探测外，被动探测也是常用的探测方式。被动探测主要采用网络流量分析技术，对流量中的数据包指纹特征进行分析。网络嗅探技术根据网络环境的不同，主要分为以太网嗅探和交换机网络嗅探等。常用的嗅探工具有Wireshark、tcpdump等。以太网嗅探是在以太网环境中，通过将网卡设置为混杂模式，以捕获流经该网卡的所有数据包。交换机网络嗅探包括ARP欺骗等方式，诱导交换机将所有数据包发送给攻击者。

4.1 基于隐马尔科夫的防嗅探系统设计

为干扰攻击者网络嗅探行为，本文设计一个防嗅探流量干扰系统。该系统部署于全部网络接入层设备，通过地址生成模块获取管理系统中未分配的IPv6地址，在不影响网络链路正常使用的前提下，伪造IPv6节点在局域网和跨路由网络中随机发送数据包序列。防嗅探系统架构设计如图8所示。

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdbNmC5ujXNqxS3icHcdnQJlW2AdxHZWiaUIFXocuAjjsBibJhsoAGWP8L286p6OH8ddJQy6dwoianeW842kJy7ok3cesTvEYAPyIEw/640?wx_fmt=png)

图8  防嗅探系统架构设计

随机数据包序列为A，A[i]是第i个数据包，A[i]=[direction,protocol,time]，其中，direction表示数据包是发送或接收，protocol表示邻居发现协议（neighbor discovery protocol, NDP）、超文本传输协议（hypertext transfer protocol, HTTP）、传输控制协议（transmission control protocol, TCP）等网络协议，time表示上一个数据包发送后，到发送当前数据包所经过的时间。基于历史流量数据，利用隐马尔科夫模型生成随机干扰数据包序列。隐马尔科夫模型是一个随机过程，其参数包括隐藏状态集合、观测状态集合，以及状态转移概率矩阵和观测概率矩阵。在生成随机数据包序列时，状态转移概率用于表示从一种协议转移到另一种协议的概率，观测概率用于表示从上一种协议转移到当前协议所经过的时间概率分布。假设当前数据包取决于前序3个数据包的协议和方向，状态转移概率可基于历史数据包序列，通过自然语言处理的Ngram语言模型（文中N取值为4）统计得到。

隐藏状态引入nul空状态节点，表示模型的初始状态或截止状态，若隐态协议转移的时间超过设置阈值，则在原始数据包序列中插入nul，表示在生成新的随机序列时，遇到nul可以终止生成。在原始数据包序列起始位置插入2个nul，用于补齐四元组，在末尾插入1个nul，表示序列结束。基于相同源和目的IP地址对，统计得到状态转移概率表如表1所示，\_i表示收到数据包，\_o表示发送数据包。

表1  状态转移概率表

![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxda1bYFAiahdFt6kBibtLXLYoo0LuibVXP12znEvEDkWNBkTKQ1JPXtx4oibQibQPrePLvGEpv2iaa86Dtcwx1QcyMAv8nCiaiawecwdhPo/640?wx_fmt=jpeg)

图9是当隐藏状态为https\_o和tcp\_o时，其前2个状态及转移到当前隐藏状态的时延分布。由图9可知，对于相同的隐藏状态，前序的隐藏状态序列不...