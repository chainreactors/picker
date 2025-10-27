---
title: IPSec和SSL国密数据包分析
url: https://www.secpulse.com/archives/200670.html
source: 安全脉搏
date: 2023-05-19
fetch_date: 2025-10-04T11:37:23.375106
---

# IPSec和SSL国密数据包分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# IPSec和SSL国密数据包分析

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-05-18

15,016

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397416.png)

## ***0x01 IPSec***

IPSec协议实际上是一套协议集合，包括IKE协议、认证头（AuthenticationHeader，AH）协议、封装安全载荷（Encapsulating Security Payload，ESP）协议和用于网络身份鉴别及加密的一些算法等。

从工作流程上看，IPSec协议可分为两个环节：IKE是第一个环节，完成通信双方的身份鉴别、确定通信时使用的IPSec安全策略和密钥；第二个环节是使用数据报文封装协议和IKE中协定的IPSec安全策略和密钥，实现对通信数据的安全传输。

IPSec工作模式分为**传输模式**和**隧道模式**。传输模式一般用于端到端的应用场景；隧道模式一般用于创建虚拟专用网隧道链路。

### 1、IKE协议

**通过数据包对IKE进行详细分析和介绍**

IKE协议用于**鉴别通信双方身份、创建安全联盟（Security Association，SA）、协商加密算法以及生成共享会话密钥等**，其中ISAKMP是IKE的核心协议，定义了建立、协商、修改和删除SA的过程和报文格式，并定义了密钥交换数据和身份鉴别数据的载荷格式。ISAKMP的一个核心功能就是创建和维护SA。SA作为通信双方之间对某些要素的一种协定，是IPSec的基础，协定的内容包括数据报文封装协议、IPSec工作模式、密码算法等安全策略和密钥。IPSec的两种封装协议（AH和ESP）均使用SA中协定的内容保护通信安全。另外，**SA是单向的**，一个SA为单一通信方向上传输的数据提供一种安全服务，通信双方需要产生属于自己的SA。若使用多个安全服务保护数据流，例如，同时提供认证和加密服务，那么应该创建多个SA来分别实现不同安全服务对数据的保护，即每个SA对应一个安全服务。

IP Sec 9个包分析 主模式（前6个包）+ 快速模式（后3个包）

#### 第一阶段主模式：ISAKMP协商阶段

工作流程如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397417.png "null")

**下面针对数据包来分析主模式的协商过程**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397419.png "null")

**包一：**发起端协商SA，使用的是UDP协议，端口号是500，上层协议是ISAKMP，该协议提供的是一个框架，里面的负载Next payload类似模块（SA载荷），可以自由使用。可以看到发起端提供了自己的SPI值，以及SA的加密套件，加密套件主要是加密算法、杂凑算法、认证算法、秘钥长度、生存时间等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397423.png "null")

**包二：**响应端收到发送端发送的加密套件后，对比自己是否有相对应的加密套件，如果有就使用和发送端相同的加密套件加密数据，把自己的SPI值和选择好的加密套件发送给发送端。如果没有相同加密套件则IKE建立失败响应。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397427.png "null")

在包二中响应方同时还发送自己的签名证书和加密证书（双证书）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397432.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397436.png "null")

**包三和包四：**

在包三和包四中，双方进行数据交换，交换的内容包括Nonce载荷（Ni和Nr）、身份标识载荷（IDi和IDr）等，其中Nonce载荷是生成工作密钥所必需的参数。这些数据使用双方各自随机生成的临时密钥SK进行对称加密保护，SK用对方的加密证书中的公钥进行加密保护。双方各自对交换数据进行数字签名，这一过程使用签名证书对应的私钥来完成，并将签名结果发给对方。同时，发送端的双证书也在包三中发给响应端，这样发送端和响应端都有了对方的签名和加密证书，可以使用对方的公钥。

包三和包四完成后，参与通信的双方利用Nonce载荷等交换数据经伪随机函数（PRF）派生出基本密钥参数，并通过PRF用基本密钥参数派生出三个**对称密钥**，分别是**用于产生会话密钥的密钥参数、用于验证完整性和数据源身份的工作密钥及用于加密的工作密钥**（注意这里没有生成会话密钥）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397439.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397441.png "null")

**包五和包六：**发送端和响应端对前面协商过程内容进行鉴别确认。这两个消息中传递的信息使用包三和包四产生的用于机密的工作密钥来做对称加密保护。对称密码算法由一开始双方协商的算法，这里使用的是SM4-CBC。为了检查交换内容，双方通过计算HMAC验证身份和协定的SA信息。第一阶段主模式到此结束。

#### 第二阶段快速模式：IPSec SA协商阶段

第二阶段快速模式的工作流程如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397443.png "null")

快速模式用于协商建立通信时使用的IPSec SA，包括**IPSec安全策略和会话密钥**（会话密钥在快速模式中产生）。

会话密钥有两个，均为对称密钥，分别用于通信数据加密，以及完整性校验和数据源身份鉴别。

快速模式交换的数据由主模式协定的ISAKMP SA提供保护，即除了ISAKMP头外所有的载荷都是加密的，加密密钥选用**用于加密的工作密钥**。同时，在ISAKMP头之后会紧跟一个HMAC载荷，用于验证交换数据的完整性和数据源身份。

在快速模式中，数据包都是加密的，简单放一张快速模式数据包的图片看下吧

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397444.png "null")

最后，将主模式包三和包四中派生出的用于产生会话密钥的密钥参数经PRF计算得到会话密钥。PRF的输入还包括双方的Nonce载荷、从主模式建立的ISAKMP SA中获得的协议值和安全参数索引（SPI），其中SPI用于唯一标识一个数据报文对应的SA。用于加密的会话密钥与用于验证完整性和数据源身份的会话密钥则按照密码算法要求的长度，从会话密钥素材中依次选取。

#### 野蛮模式

除IKE模式外，还有野蛮模式

书上没有对野蛮模式进行讲解，我这也没有野蛮模式数据包，就简单说下

野蛮模式只用到**三条信息**：前两条消息1和2用于协商IKE安全提议，交换Diffie-Hellman公共值、必需的辅助信息以及身份信息，并且消息2中还包括响应方发送身份信息供发起方认证，消息3用于响应方认证发起方。

### 2、AH协议

AH协议提供了数据源身份鉴别、完整性和抗重放等安全功能，**没有提供加密服务**。因此AH协议不能单独用于封装IP数据报文，应和ESP协议一起使用。AH协议不支持NAT穿越。

AH协议的主要作用是为整个IP数据报文（IP头和IP载荷）提供高强度完整性校验，以确保被篡改过的数据包可以被检查出来。在传输模式和隧道模式下有不同的放置位置，如下图所示。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397447.png "null")

### 3、ESP协议

ESP协议相对于AH协议增加了对数据报文的加密功能，**ESP协议可以单独使用**。在ESP协议和AH协议结合使用时，无需开启ESP提供**数据源身份鉴别服务**。**ESP协议支持NAT穿越。**

ESP头在传输模式和隧道模式中分别有不同的放置位置，保护范围也有所不同，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397448.png "null")

### 4、IPSec VPN产品

IPSec VPN产品工作在**网络层**，对应用层协议完全透明。

IPSec VPN产品主要用于**站到站**和**端到站**模式，也用于端到端模式（较少）。其中站到站和端到站采用隧道模式，端到端可以采用隧道模式或者传输模式。

前面在分析数据包时，可以看到算法对应的属性值，如下表所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397450.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397453.png "null")

IPSec VPN产品的密钥体系也分为三层：**设备密钥、工作密钥和会话密钥。**

①设备密钥：**非对称密钥对**，包括签名密钥对（设备内部产生）和加密密钥对（外部密钥管理机构产生），用于实体身份鉴别、数字签名和数字信封等。其中，用于签名的设备密钥对在IKE第一阶段提供基于数字签名的身份鉴别服务；用于加密的设备密钥对在IKE第一阶段对交换数据提供保密性保护。

②工作密钥：**对称密钥**，在IKE**第一阶段**经密钥协商派生得到，用于对会话密钥交换过程的保护。其中，用于加密的工作密钥为IKE第二阶段交换的数据提供保密性保护；用于完整性校验的工作密钥为IKE第二阶段传输的数据提供完整性保护及对数据源进行身份鉴别。

③会话密钥：**对称密钥**，在IKE**第二阶段**经密钥协商派生得到，直接用于数据报文及报文MAC的加密和完整性保护。其中，用于加密的会话密钥为通信数据和MAC值提供保密性保护；用于完整性校验的会话密钥为通信数据提供完整性保护。

## ***0x02 SSL***

### 1、SSL协议

SSL协议是由多个协议组成的两层协议集合，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200670-1684397455.png "null")

下层协议包括记录层协议，主要用于封装不同的更高层协议的数据，为数据提供保密性、完整性和数据分段等服务，特别是它可为B/S的交互提供传输服务的超文本传输协议（HTTP）提供安全服务。

上层协议分为：**握手协议、密码规格变更协议和报警协议**

其中，握手协议实现了服务端和客户端之间相互的身份鉴别、交互过程中密码套件（公钥密码算法、对称密码算法和密码杂凑算法的集合）与密钥的协商；密码规格变...