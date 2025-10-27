---
title: 高安全等级密码模块安全技术设计
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535728&idx=1&sn=9327d798dc9e89f383fa4cee53ac992c&chksm=fa93fab1cde473a7fd74b5349b48bc1eb0edd34bf52e5fda62610fd9223a7bcaf067f450c50b&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-25
fetch_date: 2025-10-04T10:38:26.941539
---

# 高安全等级密码模块安全技术设计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mZbjrkEiaVHlcMzBfCKet1y36hz1Mcj38w8qNhKjbullMbsuldF7E1ib3RFyfPUDWQ0vxGVZUp5gfQ/0?wx_fmt=jpeg)

# 高安全等级密码模块安全技术设计

网络安全应急技术国家工程中心

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**摘要：**随着金融、大数据等行业的普及和发展，对密码设备的依赖与日俱增，并且业内在数据安全领域提出了多方面更高的要求，例如密码模块的物理安全、抗非入侵式攻击、抗环境失效等，迫切需要更高安全等级的密码模块来支撑行业的实际应用需求。依托安全二级密码模块，提出了新的高安全等级密码模块，在既有功能和安全技术设计的基础上，新增了物理安全、实体鉴别、环境失效性检测、非入侵式攻击缓解 4 个重要的安全技术。该模块设计对数据安全要求极高的行业和领域具有重要的实用意义。

密码模块作为基础密码设备，在金融、电力、大数据等行业中为各类安全应用提供身份认证、算法加速、敏感安全参数管理和保护等服务。目前市面上的商用密码模块按照国家密码管理局提出的相关标准 进行研发，大多满足安全一级或安全二级的规范要求，仅提供基本的安全功能。

由于标准对高安全等级密码模块规定了更多的新功能和新机制，技术要求较高，因此国内在该研究领域仍处于起步阶段，且安全技术设计的相关论述较少。然而随着对数据安全有极高要求的行业的发展，业内对高安全等级的密码模块的需求与日俱增，面临巨大的市场空缺。因此，研究如何通过各种设计和技术路径来满足高安全等级的要求就显得迫在眉睫。

本文首先简要介绍高安全等级密码模块的设计架构，其次分别从高安全等级特有的物理安全 、实体鉴别、环境失效性检测（Environmental FailureTesting，EFT）、非入侵式攻击缓解技术这 4 个方面详细说明高安全等级密码模块的设计和工作原理。本文的研究不仅可以填补高安全等级密码模块安全技术设计方面的空白，也可以指导研发具有实用价值的商用密码模块，满足相关行业的技术需求和市场需求。

# **１、高安全等级密码模块设计架构**

**1.1　硬件架构**

设计高 安 全 等 级 密 码 模 块， 以 高 速 串 行 扩 展 总线（Peripheral Component Interconnect Express，PCI-E）接口密码模块为例，由主控单元、PCI-E总线接口单元、密码运算单元、存储单元、环境失效性检测（Enviromental Failure Test，EFT）单元、功能单元组成，如图 1 所示。

**![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzDAgwHExdvicUgAgaHxC06yvvzibtbricbNVC3jibs3ey2eA15mw4bmrm4A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)**

**图 1　高安全等级密码模块硬件架构**

高等级密码模块中：（1）主控单元由带嵌入式操作系统的中央处理器（Central Processing Unit，CPU）实现，实现对密钥的管理和对应用层下发命令的解析和响应；（2）PCI-E 总 线 接 口 单 元 由 大 规 模现场可编程逻辑门阵列（Field Programmable Gate Array，FPGA）实现，是数据进出密码模块的主要传输通道；（3）密码运算单元基于效率和性能的考虑，由两颗专用密码算法芯片组成，分别实现 SM1 算法和 SM2 算法，另由逻辑器件实现哈希算法 SM3 和对称分组密码算法 SM4；（4）存储单元由双倍速率内存（Double Data Rate synchronous Dynamic Random-access Memory，DDR SDRAM）和闪存（FLASH）组成，分别存储密码模块运算过程中的数据和板载芯片的可执行程序；（5）EFT 单元负责实现 EFT 功能，由电压和温度两部分组成，分别实现对电压和温度的感知和响应；（6）功能单元中，由开盖销毁装置、按键销毁按钮实现紧急状况下的关键安全参数置零功能，状态 LED 灯指示密码模块的实时状态，USBKey 接口供身份鉴别的 UKey 使用，另有多片物理噪声源用于产生质量合格的随机数。

**1.2　软件架构**

设计密码模块处于主机应用层之下，受应用层各种安全应用程序的调用。其软件架构由安全服务接口、设备驱动程序、嵌入式软件3部分组成，如图 2 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzneLt6XZUrrxOFDfQrRVbgTgiciajoL9dmnh9SBhYBapfEkoucK3hwic7A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 2　高安全等级密码模块软件架构

该软件架构中：安全服务接口提供密码模块的功能接口，由应用程序直接调用；设备驱动程序为密码模块的宿主设备提供驱动能力；嵌入式软件，运行于密码模块的主控单元，响应和执行应用层的调用指令。

**1.3　密钥体系**

密钥是密码模块的核心资源，完善的密钥管理体系是密码模块的核心功能。在高安全等级密码模块中，密钥管理采用了技术合理、安全性高的 3 层密钥结构体制，如图 3 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzoYZRRPTPGgVGS7sU8hR04oLqbKzYgIJKS0lcUfYOb3BNsJibHRVwyAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 3　高安全等级密码模块密钥体系

在分层密钥保护体系中：保护密钥位于最上层，主要用于加密保护其下层的用户密钥对和密钥加密密钥；用户密钥对和密钥加密密钥位于中间层，用户密钥对除用于非对称密码运算外，还作为保护密钥保护其下层的对称会话密钥；密钥加密密钥主要用作保护密钥，保护其下层的对称会话密钥，且会话密钥处于层次化密钥结构中的最底层，是仅在一次会话中使用的对称密钥。不论何种密钥，除公钥外的所有密钥都不能以明文形式存在于密码卡外部。通过上述层层保护的原则，满足了密钥管理中的“分层结构，逐层保护”的安全原则。

# **2、物理安全性设计**

高安全等级密码模块在研制时采用的物理安全设计要点如下文所述。

(1）选用经过国密局认证的对称和椭圆曲线算法（Elliptic Curve Cryptography，ECC）专算芯片。该类芯片的抗攻击能力高，能够确保芯片内部包括密钥数据、算法代码等敏感信息的安全。

(2）高安全等级密码模块将所有重要的元器件均放置在电路板的正面，并采用硬质金属材料的外壳对电路板正反两面进行全包裹，防止外部的窥探，并防止外部通过探针进行测量。金属外壳可采用铝合金 6063，如图 4 所示，在国家标准 GB/ T 3190-2020《变形铝及铝合金化学成分》中规定其成分范围，是 AL-Mg-Si 系中等强度的可热处理强化合金，Mg 和 Si 是主要合金元素，其硬度为 95 HB，在抵御外部的撬、钻、击打等常规拆破行为中表现较好。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRze7gRR57INTHbbTpPoGKMfIwFPg8uVUJ9AJlLjibyr8ficBlCRyiadTSFw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 4　硬质金属外壳

同时，该外壳内部的四周设计有一圈金属丝网，如图 5 所示。在外壳压合时，可以紧紧贴合电路板，消除外壳与电路板之间的微小缝隙，在一定程度上有防止电磁干扰和抵御非入侵攻击中电磁分析攻击的作用。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRz3aiasVNyO6kPbQBVjDhUpog5858boCY30tDqIg5FYiaX31stFpeCiaYlw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 5　外壳内层金属丝网

(3）高安全等级密码模块在进行印制电路板（Printed Circuit Board，PCB）排版时，将重要的总线信号和专用算法芯片的数据信号设计在了印制版的里层，可有效防止外部将 PCB 表面涂层刮开直接使用探针探测电信号的行为。

(4）如图 6 所示，高安全等级密码模块固定外壳的螺母采用私有的非标设计，只有使用厂家特制的工具才能开启，且在螺丝上方使用金属薄片进行遮盖，并在金属薄片表面粘贴有拆卸存迹的全息封条，可以清楚地指示密码模块外壳是否曾被拆卸开启过。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzDeUIlOB6f30ZITG5utkrWEBvF1LyNZrOicNIL1oFjOZ3Gl3Aic62InMQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 6　高安全等级密码模块的私有非标螺母

(5）高安全等级密码模块设计有拆卸响应电路，主要由机械检测电路和触发通知电路两部组成。机械检测电路采用多单元并联模式工作。为保证检测拆卸动作的可靠性和准确性，防止撬起某个部位逃避检测的行为，在密码模块的 3 个角上设置了机械检测电路，任意一点的检测电路检测到拆卸行为后均可以触发通知电路工作。这 3 个点位分别检测不同位置的金属外壳上盖与模块印制版之间的垂直间距，可以快速地判断上盖的拆卸情况，并通过触发通知电路向 CPU 发出报警信号，使其知晓应该对未受保护的关键安全参数进行置零。拆卸响应电路的设计原理如图 7 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzGnfqcGC1ce0aN4191OK6FF6kGxK9icegibh2Me1NaR1ibJ241SO7NEtzg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 7　拆卸响应电路设计原理

# **3、实体鉴别安全性设计**

高安全等级密码模块在使用 UKey 进行身份认证时，首先需要对 UKey 进行实体鉴别，以确认插入的 Ukey 是与该密码模块一一对应的实体，防止外部使用相同型号的 UKey 进行混淆和攻击。在本密码模块的安全技术设计方案中，采用数字签名技术规范要求中的两次传递单向鉴别机制 。具体鉴别过程如图 8 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzvvxz25vVG9jesIziad0z19dDY48DyiaZiaaibPEQiaGvfPZrZ4QVfo70DMA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 8　基于数字签名技术的两次传递单相鉴别流程

(1）创建操作员时模块调用身份认证 UKey的智能密码钥匙密码应用接口规范（smart token cryptography application interface specification，SKF）[7] 接口产生非对称密钥对，私钥保存于 UKey中，公钥导出到模块内保存。（2）需要进行实体鉴别时，将操作员身份认证 UKey 定为声称方 A，密码模块定为验证方 B。（3）B 使用随机数生成器产生 32 字节随机数Rb，并调用 A 的接口将Rb送入 A 以备后续签名使用，密钥指定为第一步操作生成的私钥。（4）A 收 到 Rb 后， 产 生 32 字 节 的 随 机 数Ra，将 Ra 与 Rb 进行拼接，并进行一次 hash 运算，将 hash 运算的结果进行签名，密钥为第一步操作生成的私钥。签名完毕后，A 连同 Rb|Ra|sign(Rb|Ra) 一同送出给 B。（5）B 获取 A 送出的签名数据后，对随机数Rb|Ra 进行 hash 运算，将得到的 hash 值使用第一步操作中获得的公钥对签名数据进行验签操作，若验签通过，再比较数据中包含的随机数 Rb 是否等于之前产生的 Rb。（6）若上一步操作中的两个操作均通过，则表明实体鉴别成功。

# **4、EFT 安全性设计**

高安全等级密码模块具有 EFT 功能，包括检测温度和检测电压两部分。具体检测 4 种异常环境状况：低温、高温、大负电压、大正电压。下面分别介绍温度和电压异常状况下，EFT 的设计原理和生效机制。

**4.1　异常温度检测**

密码模块在关键器件如可编程逻辑器件、专用算法芯片等附近布置多片温度传感器，对密码模块内部的环境温度进行多点监测。设置好密码模块的工作温度区间，当环境温度不在该范围内，则认为环境失效，密码模块主动断电。具体的工作原理是模块上电后，处理器周期性地主动读取各片温度传感器的温度寄存器，以获取它们附近环境的实际温度。若任意一片温度传感器的温度不在工作范围内，则处理器做一次记录。当连续多次记录到该现象时，表明环境温度持续处于正常工作范围之外，工作环境确实失效，此时处理器告知开关电路切断密码模块的电源，以达到置零模块内未受保护的关键安全参数的目的。一旦开关电路切断密码模块的电源，电源指示灯也会熄灭。温度失效性检测技术的设计原理如图 9 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzTmK3pXasKVeSib0bU9ncGL1VSVwg3O2XqFe7tkFUMBLBSXVqAdTJHQg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 9　温度失效性检测原理

**4.2　异常电压检测**

PCI-E 接口的输入电源分两路：一路通过一个模数转换器（Analog-Digital conversion，A/D）接入CPU；一路则接入开关电路，并通过开关电路对密码模块进行供电。设置好密码模块电压的正常工作范围后，CPU 周期性地对输入的电压进行检测，若连续多次检测到电压处于正常范围之外，则表明工作环境确实失效。此时，CPU 记录好环境失效的日志后告知开关电路断开电源供应，使得后端的电路掉电，以置零密码模块内未受保护的关键安全参数。可通过观察模块的侧面板上电源指示灯来确认模块的上、下电情况：当模块正常工作时，电源灯长亮；一旦电源管理模块切断密码模块的电源，电源指示灯会熄灭。电压失效性检测技术的设计原理如图 10所示。

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzD7sOSPPITqnUJibIEbVt7yic03lx41k4eAnsC0RHIULmxcATx2licF3Sg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

图 10　电压失效性检测原理

# **5、非入侵式攻击缓解技术**

**5.1　计时攻击缓解技术**

在算法层面，由于对称密码算法 SM4 没有基于密钥的分支运算，因此对称算法对计时攻击天然免疫，故无须针对上述算法做专门的计时攻击防护设计。

针对 SM2 公钥密码算法，点乘计算采用安全点乘算法，能有效防御计时攻击和简单能量攻击。安全点乘算法如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzyianugCNmaJHXzJfsZEqy3hpPhEiaYoAXqxqW2qCBNflsiaCZ4y7arFQg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

该方法一次扫描 1 位密钥位，每次进行 1 次点加运算和 1 次倍点运算，可以实现任意相同长度的密钥位运算都没有时间区别。

**5.2　能量分析攻击缓解技术**

针对 SM4 算法，采用掩码技术，通过随机化密码模块所处理的中间值，使密码模块的能量消耗不依赖于此中间值，消除密码设备能量消耗的数据相关性。采用如下文所述的思路进行操作。

引入随机掩码，实现全寄存器掩码以及掩码 S盒。例如一共生成 16 个各不相同的掩码 S 盒，第一轮使用编号为 1~4 的掩码 S 盒，第二轮使用编号为 5~8 的掩码 S 盒，第三轮使用编号为 9~12 的掩码 S 盒，第四轮使用编号为 13~16 的掩码 S 盒，第五轮又重复使用编号为 1~4 的掩码 S 盒，以此类推。这样使 SM4 算法在加解密的每一个运算步骤均有掩码参与，达到每一个运算步骤结果均与原算法无关的目的。

假设单个 S 盒的输入为![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzGRQXVQo0JKyn0YDjrGxQ7owpsn8dfBLeCmmzyQe2Zr64Wy4icCUZyEw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)，输出为![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ3xueJvWibf4mskRzxpzb9QQ6Ll5LjdI1SgdicciaMAmPf4rIeCGzeibqrxq3Jdeic1qlibn9Krw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)，则有![](https://mmbiz.qpic.cn/mmbiz_png/maicFpJ7zhDKGib6xRJ...