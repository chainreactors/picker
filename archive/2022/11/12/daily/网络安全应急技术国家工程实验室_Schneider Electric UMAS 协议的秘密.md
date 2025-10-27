---
title: Schneider Electric UMAS 协议的秘密
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532672&idx=1&sn=885c6f16832b6563b84ad08126cd2237&chksm=fa93f641cde47f575cf6808a421134dad3bbe2e0177a8f0354ec9357b8e6fd5a76253f2b958f&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-12
fetch_date: 2025-10-03T22:33:04.422287
---

# Schneider Electric UMAS 协议的秘密

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mvUjsggs7btQtSWc06u50v3oB0dIL2Y5FVNXPVZGG48blMJz6ezoCsiaRjLibySFUqjtAdDMbGrS8g/0?wx_fmt=jpeg)

# Schneider Electric UMAS 协议的秘密

网络安全应急技术国家工程中心

本文翻译自Kaspersky ICS CERT研究报告。UMAS（统一消息应用程序服务）协议是施耐德电气（SE）的专有协议，用于配置和监控施耐德电气PLC。早期已有多篇关于UMAS协议的研究文章，卡巴斯基报告再次对协议做了细致讲解，同时对施耐德后期引入的安全机制、存在的安全漏洞进行了深入分析。故在此对报告进行了翻译，以飨读者。

使用UMAS协议的施耐德电气控制器包括：Modicon M580 CPU（部件号BMEP\*和BMEH\*）和Modicon M340 CPU（部件号BMXP34\*）。控制器使用工程软件EcoStruxure™Control Expert（Unity Pro）、EcoStruxure™Process Expert等进行配置和编程。2020年CVE-2020-28212漏洞，未经授权的远程攻击者可以利用该漏洞，以已在控制器上通过身份验证的操作员的权限获取对PLC的控制。为了解决该漏洞，施耐德电气开发了一种新的机制，即应用程序密码，该机制应可防止未经授权访问PLC和对PLC进行非法篡改。

卡巴斯基ICS CERT专家进行的一项分析显示，新安全机制的实施也存在缺陷。在研究过程中发现的CVE-2021-22779漏洞，可允许远程攻击者绕过身份验证对PLC进行更改。可以确定的是，在修复CVE-2021-22779漏洞的版本之前实施的UMAS协议存在重大缺陷，这些缺陷对基于SE控制器的控制系统的安全性产生了严重影响。截至2022年8月中旬，施耐德电气发布了EcoStruxure™Control Expert软件以及Modicon M340和Modicon M580 PLC固件的更新，修复了该漏洞。

本报告介绍：

·不使用应用程序密码安全机制的UMAS协议实现；

·如果未启用应用程序密码，则绕过身份验证；

·应用程序密码安全机制所依据的原则；

·可用于攻击CVE-2021-22779漏洞的机制（在配置应用程序密码的情况下绕过身份验证）。

·更新的设备保留机制的工作原理。

**研究对象**

UMAS（统一消息应用服务）是施耐德电气的专有协议，用于配置、监控、收集数据和控制施耐德电气工业控制器。UMAS基于客户端-服务器体系结构。在研究过程中，我们使用EcoStruxure™Control Expert PLC组态软件作为客户端，Modicon M340 CPU控制器作为服务器。

# **UMAS协议**

## **网络数据包结构**

## ![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7T1JNfMGNg4BYHibef0NHNl6vIQvlLBrRWcWriazpqkCjiaKTdP4q0IDsdA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

UMAS协议结构

Modbus/TCP协议的规范，包括开发者可以根据需要使用的保留功能代码，可从Modbus/TCP协议官方文档中查阅。施耐德电气使用功能代码90（0x5A）来定义数据字段中的值符合UMAS标准。

网络数据包结构如下所示，以读取PLC上的内存块（PU\_ReadMemoryBlock）的请求为例：

·红色：功能码90（0x5A）

·蓝色：会话密钥0（0x00）（请参阅会话密钥)

·绿色：UMAS函数20（0x20）（请参阅UMAS协议功能)

·橙色：数据

每个函数在数据中都包含一组特定的信息，例如相对于内存基址的偏移量、发送数据的大小、内存块号等。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TIf54tCJI6Slf7fSYQicXCTH9IRNgGJvBN0NKKkLibZicXTBB3ULNEsF9g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**网络通信**

UMAS还继承了Modbus客户端-服务器架构,下面提供了客户端和服务器之间通信的结构图。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TBjla6N3OTfIJghuFdk9t1Ep3MXwSBTkAq67zXJgAUDxLT7OH2nT8ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

客户端（EcoStruxure™Control Expert）与服务端（PLC）之间的通信过程示意

在UMAS网络数据包中，功能代码0x5A后面紧跟会话密钥:

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TIlhCibI0WL0lmSd15WGPj7CtpA5Hdxibbsjcs8aRBlr2S8UJdL9mVtIw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

UMAS网络数据包结构

下面，我们通过分析示例真实流量片段来检查客户端和服务器（PLC，以下也称为“设备”）之间的通信。下面的屏幕截图显示了从客户端（EcoStruxure™Control Expert）发送到服务器（PLC）的包含函数UMAS\_QueryGetComInfo（0x01）的数据包。报文的结构为：

TCP数据–Modbus报头–0x5A–会话–01（UMAS功能代码）–00（数据）

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TsoaaOpo6M943iaP13LzicGExRZzzwgc9okFKFAkricv2yJlZ8rNttbEPA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

设备应对收到的每个请求发送响应，截图下面显示了设备对客户端请求的响应报文：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TicsdMmPL5t7lCjialCCxwkcypXrQiaQX4x5ibdDTNCJd9aNkNXm1AR0juQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

状态代码是设备执行客户端在前一请求中发送给它的功能的状态。值“fe”对应于功能的成功执行，“fd”则对应于执行失败。这些值出现在设备发送给客户端请求的每个响应中，其中包含对应功能码，状态代码始终紧跟在会话密钥之后。

## **PLC预订流程**

对PLC进行更改前需要发起“预定”程序，此过程相当于身份验证。只有一个客户端（例如，工程工作站）可以在任何特定时间保持设备用于配置或状态监控。这是为了防止在没有预定的情况下对设备进行并行更改。

下面的屏幕截图显示了工程软件向PLC发出的请求，以在其不使用应用程序密码安全机制的基本变体中执行设备保留程序。

UMAS\_QueryTakePLCReservation（0x10）函数用于占用设备。

为了占用设备，客户端向设备发送包含0x10函数的请求，该请求包括占用该设备的客户端的名称和等于该名称长度的值。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7T7RFGBltj2ImUFDqdWg4Fdcs5hvyRic0D47PjGicIDzkd8Omf1X5rkSLA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**会话密钥**

完成占用后，设备将新的单字节会话密钥的值发送给客户端。该密钥随后用于授权设备修改请求。随着新固件版本的发布，会话创建机制发生了一些变化：

·在2.7之前的固件版本中，Modicon M340设备的会话密钥在其保留之后具有固定值0x01；

·在固件版本2.7或更高版本中，Modicon M340设备的会话密钥具有随机值，即从0到0xFF，因为会话密钥的大小为1个字节。

在预约过程完成之前，使用具有值“0x00”的服务会话，不需要预定功能也可以在该会话中执行。设备的响应包括状态代码（0xFE）和新的会话密钥，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7T1vSZH7Xf6nINib7PhTib2po9S4jEnFxEic2jXKVQuCAmxo1yvgsHHQAng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

状态代码“fe”表示预约过程成功。

在这种情况下，设备发送新的会话密钥值，新会话密钥在当前“保留”会话期间的所有后续请求中使用。

下面的屏幕截图显示了在设备成功预定后，客户端立即使用新的会话密钥向设备发出的请求。在此示例中，请求使用Ex\_GetPlcStatus（0x04）函数。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TGjoZFo5dbIVNTwYRTfe5geM07JBGDOBayyall7nLKGgMic9fBkKm25A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

当对设备进行更改时，预定过程起到身份验证的作用，这意味着从安全角度来看，该机制至关重要。以下各节介绍了与在默认配置中保留设备和使用安全功能相关的问题。

**UMAS协议功能**

UMAS协议具有许多用于与目标设备通信的功能。功能可分为两组：

1.需要占用设备功能。通常这些是要对PLC进行更改操作；

2.不需要设备占用功能。这些功能不会对PLC进行任何更改，也不会影响其运行；

3.UMAS协议中可用功能码列表如下所示，此为固件版本3.30的、具备PLC占用功能，但未启用应用程序密码安全机制的Modicon M340设备：

**PLC预定过程中使用的函数**

1.0x10–UMAS\_QueryTakePLCReservation–保留设备。

2.0x11–UMAS\_QueryReleasePLCReservation–解除设备的保留状态。

3.0x12–UMAS\_QueryKeepPlcReservation–保留状态。

**需要设备预定的功能码**

##### **初始化功能码**

0x01–UMAS\_QueryGetComInfo–UMAS消息初始化。

##### **用于请求设备信息的功能码**

1.0x02–PU\_getplcinfo–请求关于设备的信息

2.0x04–PU\_GetPLCStatus–查询PLC状态

3.0x06–PU\_GetMemoryCardInfo–请求有关的信息设备的SD卡

##### **下载和上传PLC逻辑的功能码**

逻辑是PLC用来执行其主要功能的一组指令和数据，即控制终端设备，例如使某个工业过程自动化。

1.0x30–PUMEM\_BeginDownload–初始化从PC到PLC的上传。

2.0x31–PUMEM\_下载包–将策略块从PC上传到PLC.

3.0x32–PUMEM\_结束下载–结束从PC到PLC的上传。

4.0x33–PUMEM\_BeginUpload–初始化从PLC到PC的下载。

5.0x34–PUMEM\_UploadPacket–将策略块从PLC下载到PC.

6.0x35–PUMEM\_EndUpload–结束从PLC到PC的下载。

### **不需要设备预定的功能码**

从设备存储器0x20读取信息的功能–PU\_ReadMemoryBlock–读取PLC存储块。将值写入设备内存的功能

0x21–PU\_WRITEMEMORYBLOCK–写入PLC内存块。

### **控制PLC状态的功能码**

以下功能可用于启动或暂停PLC的运行，若应用程序密码安全机制未激活，则这些功能码函数无需PLC占用机制，在这种情况下，设备将使用服务会话（0x00）成功处理请求（请参见会话密钥).

除非启用应用程序密码设置，否则攻击者可以使用这些功能来停止PLC，从而对工业过程造成重大损害。

1.0x40–Ex\_启动任务–启动PLC操作。

2.0x41–EX\_STOPTASK–停止PLC操作。

**CVE-2020-28212：未启用应用程序密码情况下绕过身份验证**

不使用应用程序密码的基本保留机制的主要问题是，攻击者可以使用会话密钥发送请求并更改设备的配置。

在Modicon M340设备2.7之前的固件版本中，每次预定设备时，会话密钥都具有相同的值，并且等于“0x01”。这意味着攻击者可以在自己保留设备或合法用户保留设备后，通过调用相关函数对设备进行更改。

攻击工作流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TkiaB9REos85T5LlCgiaTILa54D19ULskkzehj5fGyfzYEibcyK2bXibMWg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Modicon M340固件版本低于2.7的攻击示意流程

如果在攻击时尚未预定该设备，则攻击者可以使用UMAS\_QueryTakePLCReservation（0x10）函数来保留该设备，以便对其进行更改。

对于Modicon M340固件版本2.7或更高版本，会话密钥在设备保留后采用随机值。但是，会话密钥的长度为一个字节，这意味着只有256个可能的会话ID值。这使得未经授权的远程攻击者能够暴力破解合法用户与PLC之间会话的现有ID。

要执行此类攻击，远程攻击者需要使用不同的会话ID值在PLC的端口502/TCP上发送一系列网络请求，并查看PLC返回的响应。如果发送了正确的会话ID，攻击者将获得状态代码0xFE，这意味着请求已成功完成。否则，攻击者将获得状态代码0xFD.

上述操作可使用任何编程语言实现——攻击者无需使用EcoStruxure™Control Expert或任何其他专用软件即可与设备通信。

# **应用程序密码**

为了修复CVE-2020-28212利用该漏洞，未经授权的远程攻击者可以使用已在PLC上通过身份验证的操作员的权限来控制PLC，施耐德电气开发了一种新的安全机制。施耐德电气认为，实施使用加密算法计算会话ID并增加会话ID长度的改进安全机制，可以防止可用于破解单字节会话ID的暴力攻击。

从Modicon M340设备的固件版本3.01开始，施耐德电气积极开发安全机制，以防止攻击者滥用UMAS功能码来修改设备操作。在客户端和设备之间实施身份验证，应在“项目设置”（“项目和控制器保护”）中启用应用程序密码，该机制旨在提供保护，防止未经授权的访问、不必要的更改以及未经授权下载或上传PLC程序。

当使用EcoStruxure™Control Expert软件启用密码访问机制后，其作为设备占用机制的一部分，客户在连接设备时需要输入密码，应用程序密码机制亦会改变占用机制本身，这些变化将在下面的章节中讨论。

**应用程序密码机制绕过**

不幸的是，卡巴斯基ICS CERT专家进行的一项分析表明，新安全机制的实施也存在缺陷。在研究过程中发现的漏洞，CVE-2021-22779，在存在设备占用机制的情况下，可能允许远程攻击者绕过身份验证对PLC进行篡改攻击。

为了更全面地了解“改进的”安全机制的缺陷，让我们更详细地了解身份验证和PLC占用机制的过程原理，新的安全机制基于在客户端和服务器之间交换随机生成的字节序列（随机数），并随后生成单个秘密会话。下图显示了发送的请求和收到的响应的顺序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogs2oTBIChiarbsxLASOQhVLDMnbZfqawpIBmWzp2vHhswaIDSWfxwGHkxSxFH5HBSOLp0iaWBXiauZBw/640?wx_fmt=png)

应用程序密码机制启用下的设备占用流程

下面我们将更详细地介绍这一过程：

建立TCP会话后，EcoStruxure™Control Expert软件向PLC（端口502/TCP）发送请求，以使用UMAS功能0x20读取内存块，这不需要身份验证：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TxbeSYOG4ricwv7Uounm3lriaQL16pXtx6mgmTTSxbdZf2WaYFpuAL2cA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

接下来，客户端接收来自PLC的响应：内存块需要进一步计算，因为它包含组成密码哈希的两个base64字符串。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7T17T1FQgFs0YOk80BRunvjwFiansAntQnDLZdLBIeKuIcgXSMGEAbFsw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

之后，EcoStruxure™ControlExpert会生成一个长度为32字节的随机字节序列（nonce），并将其发送至PLC：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUaJ29qbz1O2EmOyic07VIn7TfS5MrevDj3F8QVvmRzJTkFtsHwgia4sFaEsdAibbZc7uHeyFPQWlhQuQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

作为对接收到随机数的响应，PLC还会向EcoStruxure™Control Expert发送一个字节序列（随机数响应），其长度也是32字节。

![](h...