---
title: 警惕：魔改后的CIA攻击套件Hive进入黑灰产领域
url: https://blog.netlab.360.com/warning-hive-variant-xdr33-is-coming_cn/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2023-01-10
fetch_date: 2025-10-04T03:25:37.043057
---

# 警惕：魔改后的CIA攻击套件Hive进入黑灰产领域

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

[![360 Netlab Blog - Network Security Research Lab at 360 icon](/content/images/size/w30/2019/02/netlab_xs-2.png)
360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com)

—

警惕：魔改后的CIA攻击套件Hive进入黑灰产领域

Share this

[Botnet](/tag/botnet/)

# 警惕：魔改后的CIA攻击套件Hive进入黑灰产领域

* [![Alex.Turing](/content/images/2019/06/turing.PNG)](/author/alex/)
* [![Hui Wang](/content/images/2017/05/WechatIMG1.jpeg)](/author/huiwang/)

#### [Alex.Turing](/author/alex/), [Hui Wang](/author/huiwang/)

Jan 9, 2023
• 17 min read

# 概述

2022年10月21日，360Netlab的蜜罐系统捕获了一个通过F5漏洞传播，VT 0检测的可疑ELF文件`ee07a74d12c0bb3594965b51d0e45b6f`，流量监控系统提示它和IP`45.9.150.144`产生了SSL流量，而且双方都使用了**伪造的Kaspersky证书**，这引起了我们的关注。经过分析，我们确认它由CIA被泄露的Hive项目server源码改编而来。**这是我们首次捕获到在野的CIA HIVE攻击套件变种**，基于其内嵌Bot端证书的**CN=xdr33**， 我们内部将其命名为**xdr33**。关于CIA的Hive项目，互联网中有大量的源码分析的文章，读者可自行参阅，此处不再展开。

概括来说，xdr33是一个脱胎于CIA Hive项目的后门木马，主要目的是收集敏感信息，为后续的入侵提供立足点。从网络通信来看，xdr33使用XTEA或AES算法对原始流量进行加密，并采用开启了**Client-Certificate Authentication**模式的SSL对流量做进一步的保护；从功能来说，主要有`beacon，trigger`两大任务，其中**beacon**是周期性向硬编码的Beacon C2上报设备敏感信息，执行其下发的指令，而**trigger**则是监控网卡流量以识别暗藏Trigger C2的特定报文，当收到此类报文时，就和其中的Trigger C2建立通信，并等待执行下发的指令。

功能示意图如下所示：

[![](https://blog.netlab.360.com/content/images/2022/12/hive_function.png)](https://blog.netlab.360.com/content/images/2022/12/hive_function.png)

Hive使用**BEACON\_HEADER\_VERSION**宏定义指定版本，在源码的Master分支上，它的值`29`，而xdr33中值为`34`，或许xdr33在视野之外已经有过了数轮的迭代更新。和源码进行对比，xdr33的更新体现在以下5个方面:

* 添加了新的CC指令
* 对函数进行了封装或展开
* 对结构体进行了调序，扩展
* Trigger报文格式
* Beacon任务中加入CC操作

xdr33的这些修改在实现上来看不算非常精良，再加上此次传播所所用的漏洞为N-day，因此我们倾向于排除CIA在泄漏源码上继续改进的可能性，认为它是黑产团伙利用已经泄漏源码魔改的结果。考虑到原始攻击套件的巨大威力，这绝非安全社区乐见，我们决定编写本文向社区分享我们的发现，共同维护网络空间的安全。

# 漏洞投递Payload

我们捕获的Payload的md5为`ad40060753bc3a1d6f380a5054c1403a`，它的内容如下所示：

[![](https://blog.netlab.360.com/content/images/2022/12/hive_logd.png)](https://blog.netlab.360.com/content/images/2022/12/hive_logd.png)

代码简单明了，它的主要目的是：

1：下载下一阶段的样本并将其伪装成`/command/bin/hlogd`。

2：安装`logd`服务以实现持久化。

# 样本分析

我们只捕获了一个X86 架构的xdr33样本，它的基本信息如下所示：

```
MD5:ee07a74d12c0bb3594965b51d0e45b6f
ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
Packer: None
```

简单来说，**xdr33**在被侵入的设备运行时，首先解密所有的配置信息，然后检查是否有root/admin权限，如果没有，则输出`Insufficient permissions. Try again...`并退出；反之就初始化各种运行时参数，如C2，PORT，运行间隔时间等。最后通过**beacon\_start**，**TriggerListen**两个函数开启Beacon，Trigger两大任务。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_main.png)](https://blog.netlab.360.com/content/images/2022/12/hive_main.png)

下文主要从2进制逆向的角度出发，分析Beacon，Trigger功能的实现；同时结合源码进行比对分析，看看发生了哪些变化。

### 解密配置信息

xdr33通过以下代码片段**decode\_str**解密配置信息，它的逻辑非常简单即**逐字节取反**。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_decode.png)](https://blog.netlab.360.com/content/images/2022/12/hive_decode.png)

在IDA中可以看到decode\_str的交叉引用非常多，一共了152处。为了辅助分析，我们实现了附录中IDAPython脚本 Decode\_RES，对配置信息进行解密。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_idaxref.png)](https://blog.netlab.360.com/content/images/2022/12/hive_idaxref.png)

解密结果如下所示，其中有`Beacon C2` **45.9.150.144**，运行时提示信息，查看设备信息的命令等。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_config.png)](https://blog.netlab.360.com/content/images/2022/12/hive_config.png)

# Beacon Task

Beacon的主要功能是周期性的收集PID，MAC，SystemUpTime，进程以及网络相关的设备信息；然后使用bzip，XTEA算法对设备信息进行压缩，加密，并上报给C2；最后等待执行C2下发的指令 。

## 0x01: 信息收集

* MAC

  通过`SIOCGIFCON` 或 `SIOCGIFHWADDR`查询MAC

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_mac-1.png)](https://blog.netlab.360.com/content/images/2022/12/hive_mac-1.png)
* SystemUpTime

  通过/proc/uptime收集系统的运行时间

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_uptime.png)](https://blog.netlab.360.com/content/images/2022/12/hive_uptime.png)
* 进程以及网络相关的信息

  通过执行以下4个命令收集**进程，网卡，网络连接，路由**等信息

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_netinfo.png)](https://blog.netlab.360.com/content/images/2022/12/hive_netinfo.png)

## 0x02: 信息处理

Xdr33通过update\_msg函数将不同的设备信息组合在一起

[![](https://blog.netlab.360.com/content/images/2022/12/hive_compose.png)](https://blog.netlab.360.com/content/images/2022/12/hive_compose.png)

为了区别不同的设备信息，Hive设计了ADD\_HDR，它的定义如下所示，上图中的“3，4，5，6”就代表了不同的Header Type。

```
typedef struct __attribute__ ((packed)) add_header {
	unsigned short type;
	unsigned short length;
} ADD_HDR;
```

那“3，4，5，6”具体代表什么类型呢？这就要看下图源码中Header Types的定义了。xdr33在此基础上进行了扩展，新增了0，9俩个值，分别代表**Sha1[:32] of MAC**，以及**PID of xdr33**。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_type.png)](https://blog.netlab.360.com/content/images/2022/12/hive_type.png)

xdr32在虚拟机中的收集到的部分信息如下所示，可以看出它包含了head type为0,1,2,7,9,3的设备信息。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_deviceinfo.png)](https://blog.netlab.360.com/content/images/2022/12/hive_deviceinfo.png)

值得一提的是type=0，Sha1[:32] of MAC，它的意思是取MAC SHA1的前32字节。以上图中的的mac为例，它的计算过程如下：

```
mac:00-0c-29-94-d9-43,remove "-"
result:00 0c 29 94 d9 43

sha1 of mac:
result:c55c77695b6fd5c24b0cf7ccce3e464034b20805

sha1[:32] of mac:
result:c55c77695b6fd5c24b0cf7ccce3e4640
```

当所有的设备信息组合完毕后，使用bzip进行压缩，并在头部增加2字节的beacon\_header\_version，以及2字节的OS信息。
[![](https://blog.netlab.360.com/content/images/2023/01/hive_devicebzip.png)](https://blog.netlab.360.com/content/images/2023/01/hive_devicebzip.png)

## 0x03: 网络通信

xdr33与Beacon C2通信过程，包含以下4个步骤，下文将详细分析各个步骤的细节。

* 双向SSL认证
* 获取XTEA密钥
* 向C2上报XTEA加密的设备信息
* 执行C2下发的指令

### Step1: 双向SSL认证

所谓双向SSL认证，即要求Bot，C2要确认彼此的身份，从网络流量层面来看，可以很明显看到Bot，C2相互请求彼此证书并校验的过程。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_certi.png)](https://blog.netlab.360.com/content/images/2022/12/hive_certi.png)

xdr33的作者使用源码仓库中kaspersky.conf，以及thawte.conf 2个模板生成所需要的Bot证书，C2证书，CA证书。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_certconf.png)](https://blog.netlab.360.com/content/images/2022/12/hive_certconf.png)

xdr32中硬编码了DER格式的CA证书，Bot证书和PrivKey。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_sslsock.png)](https://blog.netlab.360.com/content/images/2022/12/hive_sslsock.png)

可以使用`openssl x509 -in Cert -inform DER -noout -text`查看Bot证书，其中CN=xdr33，这正是此家族名字的由来。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_botcert.png)](https://blog.netlab.360.com/content/images/2022/12/hive_botcert.png)

可以使用`openssl s_client -connect 45.9.150.144:443` 查看C2的证书。Bot，C2的证书都伪装成与kaspersky有关，通过这种方式降低网络流量的可疑性。

[![](https://blog.netlab.360.com/content/images/2022/12/hive_c2cert.png)](https://blog.netlab.360.com/content/images/2022/12/hive_c2cert.png)

CA证书如下所示，从3个证书的有效期来看，我们推测此次活动的开始时间在2022.10.7之后。
[![](https://blog.netlab.360.com/content/images/2022/12/hive_ca.png)](https://blog.netlab.360.com/content/images/2022/12/hive_ca.png)

### Step2: 获取XTEA密钥

Bot和C2建立SSL通信之后，Bot通过以下代码片段向C2请求XTEA密钥。
[![](https://blog.netlab.360.com/content/images/2023/01/hive_teakey.png)](https://blog.netlab.360.com/content/images/2023/01/hive_teakey.png)

它的处理逻辑为：

1. Bot向C2发送64字节数据，格式为"设备信息长度字串的长度（xor 5） + 设备信息长度字串（xor 5） + 随机数据"
2. Bot从C2接收32字节数据，从中得到16字节的XTEA KEY，获取KEY的等效的python代码如下所示：

   ```
   XOR_KEY=5
   def get_key(rand_bytes):
   	offset = (ord(rand_bytes[0]) ^ XOR_KEY) % 15
   	return  rand_bytes[(offset+1):(offset+17)]
   ```

### Step3: 向C2上报XTEA加密的设备信息

Bot使用Step2获得的XTEA KEY 对设备信息进行加密，并上报给C2。由于设备信息较多，一般需要分块发送，Bot一次最多发送4052字节，而C2则会回复已接受的字节数。
[![](https://blog.netlab.360.com/content/images/2023/01/hive_teadevice.png)](https://blog.netlab.360.com/content/images/2023/01/hive_teadevice.png)

另外值得一提的是，XTEA加密只在Step3中使用，后续的Step4中网络流量仅仅使用SSL协商好的加密加密套件，不再使用XTEA。

### Step4: 等待执行指令（xdr33新增功能）

当设备信息上报完...