---
title: 攻击DeepSeek的僵尸网络HailBot的三个变种分析
url: https://www.freebuf.com/articles/network/421737.html
source: FreeBuf网络安全行业门户
date: 2025-02-14
fetch_date: 2025-10-06T20:35:57.022237
---

# 攻击DeepSeek的僵尸网络HailBot的三个变种分析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

攻击DeepSeek的僵尸网络HailBot的三个变种分析

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

攻击DeepSeek的僵尸网络HailBot的三个变种分析

2025-02-13 16:53:27

所属地 北京

## 1、概述

安天CERT在2月5日发布了《攻击DeepSeek的相关僵尸网络样本分析》报告，分析了攻击中活跃的两个僵尸网络体系RapperBot和HailBot和其典型样本，分析了其与Mirai僵尸木马源代码泄漏的衍生关系。安天工程师依托特征工程机制，进一步对HailBot僵尸网络样本集合进行了更细粒度差异比对，在将样本向控制台输出的字符串作为分类标识条件的比对中，发现部分样本修改了早期样本的输出字符串“hail china mainland”，其中数量较多的两组分别修改为“you are now apart of hail cock botnet”和“I just wanna look after my cats, man.”。为区别这三组样本，我们将三组变种分别命名为HailBot.a、HailBot.b、HailBot.c，对三组样本的传播方式、解密算法、上线包、DDoS指令等进行相应的分析。其中也有将输出字符串修改为其他内容样本，但数量较少，未展开分析。

表 1‑1 HailBot三个变种之间的关系

|  |  |  |  |
| --- | --- | --- | --- |
|  | **HailBot.a** | **HailBot.b** | **HailBot.c** |
| 特殊字符串 | hail china mainland | you are now apart of hail cock botnet | I just wanna look after my cats, man. |
| 传播方式 | CVE-2017-17215漏洞 | CVE-2017-17215漏洞  CVE-2023-1389漏洞  破解攻击（账号密码数量45） | CVE-2017-17215漏洞  CVE-2023-1389漏洞  暴破攻击（账号密码数量96） |
| 解密算法 | ChaCha20算法  key：“16 1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F 17 02 03 13 18” nonce：“1E 00 4A 00 00 00 00 00 00 00 00 00” | ChaCha20算法  key：“16 1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F 17 02 03 13 18” nonce：“1E 00 4A 00 00 00 00 00 00 00 00 00” | ChaCha20算法  key：“5E 8D 2A 56 4F 33 C1 C9 72 5D F9 1D 01 6C 2F 0B 77 3D 81 94 58 40 63 0A 79 62 1F 80 5C 3E 16 04” nonce：“1E 00 4A 00 00 00 00 00 00 00 00 00” |
| 上线包 | 31 73 13 93 04 83 32 01 | 大部分样本：56 63 34 86 90 69 21 01  少部分样本：31 73 13 93 04 83 32 01（与HailBot.a一致） | 56 63 34 86 90 69 21 01 |
| DDoS指令 | 8个指令，指令号0-7 | 15个指令，指令号0-14 | 10个指令，指令号0-7、11、14 |

## 2、样本分析

### 2.1、HailBot.a

HailBot.a，是其最早变种，由于其运行时向控制台输出“hail china mainland”，相关僵尸网络因此被命名为HailBot。本节内容与第一篇分析报告有部分内容重复，主要为了对比不同版本变种间的差异特点。

HailBot.a的样本信息如下表所示。

表 2‑1 HailBot.a典型样本标签

|  |  |
| --- | --- |
| **病毒名称** | Trojan/Linux.Mirai[Backdoor] |
| **MD5** | 2DFE4015D6269311DB6073085FD73D1B |
| **处理器架构** | ARM32 |
| **文件大小** | 74.78 KB (76,572 bytes) |
| **文件格式** | ELF 32-bit LSB executable |
| **加壳类型** | 无 |
| **编译语言** | C/C++ |

**2.1.1、传播方式**

HailBot.a利用漏洞进行传播，其长期使用的CVE-2017-17215漏洞存在于特定版本路由器的UPnP（通用即插即用）服务中。攻击者可以通过发送特制的HTTP请求在目标设备执行任意代码。

![](https://image.3001.net/images/20250213/1739436663_67adb277738f1d8691c04.png!small)

图 2‑1 HailBot.a构造漏洞利用载荷

**2.1.2、解密算法**

HailBot.a运行后首先对域名进行解密，其解密操作采用了ChaCha20算法。key为“16 1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F 17 02 03 13 18”，nonce为“1E 00 4A 00 00 00 00 00 00 00 00 00”。

![](https://image.3001.net/images/20250213/1739436650_67adb26a92452b765be7f.png!small)

图 2‑2 HailBot.a使用chacha20解密字符串

### 2.1.3、上线包

HailBot.a运行后发送上线数据包，内容为：“31 73 13 93 04 83 32 01”。

![](https://image.3001.net/images/20250213/1739436640_67adb260776d2a8b965a2.png!small)

图 2‑3 HailBot.a发送上线数据包

**2.1.4、DDoS指令**

当接收到攻击者发送来的指令后，HailBot.a将根据不同指令执行对应的DDoS攻击。HailBot.a支持的DDoS指令如下表所示。

表 2‑2 HailBot.a支持的DDoS指令

|  |  |  |
| --- | --- | --- |
| **指令号** | **功能** | **影响** |
| 0 | TCP泛洪攻击 | 创建连接发送大量500至900字节的TCP请求消耗受害者网络带宽。 |
| 1 | SSDP泛洪攻击 | 利用简单服务发现协议（SSDP）发送大量“发现消息”请求使受害者进行响应，消耗受害者内存和CPU资源。 |
| 2 | GRE IP泛洪攻击 | 发送大量封装有IP网络数据包的GRE协议数据消耗受害者网络带宽。 |
| 3 | SYN泛洪攻击 | 发送大量SYN数据包，使服务器创建具有大量处于半连接状态的请求，消耗系统内存和CPU资源。 |
| 4 | UDP泛洪攻击（512字节） | 发送大量512字节的UDP请求消耗受害者网络带宽。 |
| 5 | UDP泛洪攻击（1024字节） | 发送大量1024字节的UDP请求消耗受害者网络带宽。 |
| 6 | TCP STOMP泛洪攻击 | 发送创建连接发送大量768字节数据消耗受害者网络带宽。 |
| 7 | TCP ACK泛洪攻击 | 发送具有随机源端口、目的端口及数据等信息的ACK数据包消耗受害者网络带宽。 |

###

### 2.2、HailBot.b

HailBot.b同样是基于Mirai源代码二次开发的僵尸网络，输出的字符串为：“you are now apart of hail cock botnet”。

HailBot.b的典型样本信息如下表。

表 2‑3 HailBot.b典型样本标签

|  |  |
| --- | --- |
| **病毒名称** | Trojan/Linux.Mirai[Backdoor] |
| **MD5** | BB9275394716C60D1941432C7085CA13 |
| **处理器架构** | AMD64 |
| **文件大小** | 93.34 KB (95,576 bytes) |
| **文件格式** | ELF 64-bit LSB executable |
| **加壳类型** | 无 |
| **编译语言** | C/C++ |

**2.2.1、传播方式**

HailBot.b同样利用了CVE-2017-17215漏洞进行传播。

![](https://image.3001.net/images/20250213/1739436604_67adb23c540c7fde14a0b.png!small)

图 2‑4 HailBot.b中的CVE-2017-17215漏洞利用载荷

部分样本有利用CVE-2023-1389漏洞进行传播。

此外，HailBot.b样本中还发现用于暴破攻击的用户名和密码，如下表所示。

表 2‑4HailBot.b暴破攻击使用的用户名和密码和对应产品服务

（表格内容基于DeepSeek整理输出，并做人工修订，特此说明）

|  |  |  |
| --- | --- | --- |
| **用户名** | **密码** | **可能关联的服务/****品牌/****设备类型** |
| leox | leolabs\_7 | Leox（显仕）设备或定制设备（如某些工控系统或私有网络设备） |
| root | wabjtam | 可能为某些旧款路由器或摄像头（如中国小品牌设备） |
| telnetadmin | telnetadmin | 某些网络设备（如交换机、路由器）的Telnet默认账户 |
| admin | gpon | 某些光纤终端设备（如中兴/华为GPON光猫） |
| admin | admin123 | 常见通用默认密码（常见于路由器、摄像头，如TP-Link、D-Link） |
| e8ehome | e8ehome | 电信或联通部分光猫/路由器（上海贝尔光猫、中兴ZXV10 H618C路由器、ZXA10 F460光猫） |
| default | default | 部分设备通用默认配置（如某些旧款路由器或IoT设备） |
| root | root | 部分设备和服务通用默认密码 |
| default | OxhlwSG8 | 可能为特定品牌设备（如某些企业级交换机或防火墙） |
| root | hme12345 | 海康威视（Hikvision）相关设备（如部分摄像头或NVR） |
| admin | aquario | 可能为Aquario品牌设备（如温控系统或工控设备） |
| root | Zte521 | 中兴（ZTE）光纤调制解调器或路由器 |
| root | 1234 | 通用默认密码 |
| root | antslq | 可能为安防设备（如某些国产摄像头品牌） |
| default | tlJwpbo6 | 复杂密码可能用于企业级设备（如防火墙或服务器） |
| root | default | 网络设备（如某些交换机的默认配置） |
| admin | 1988 | 可能为某些摄像头或DVR（如年份相关默认密码） |
| adtec | adtec | Adtec品牌设备（如监控系统或广播设备） |
| root | hkipc2016 | 海康威视（Hikvision）IPC摄像头 |
| admin | hme12345 | 海康威视（Hikvision）或关联设备 |
| hikvision | hikvision | 海康威视（Hikvision）设备的默认账户 |
| root | login!@#123 | 企业级设备（如服务器或高端路由器） |
| telecomadmin | admintelecom | 电信运营商设备（如华为/中兴光猫） |
| telnetadmin | HI0605v1 | 可能为Hikvision（HI）设备的Telnet登录 |
| admin | qwaszx | 通用简单密码（常见于低端路由器或IoT设备） |
| support | support | 技术支持账户（如服务器或网络设备） |
| root | 5up | 极简密码可能用于测试设备或嵌入式系统 |
| root | a | 未知 |
| root | icatch99 | 使用iCatch芯片的摄像头（如某些国产摄像头品牌） |
| Admin | a | 未知 |
| Admin | Admin | 通用管理员密码 |
| root | adminpassword | 通用管理员密码（如某些新型路由器） |
| root | vizxv | 不确定，可能为某品牌定制设备 |
| root | unisheen | 可能为UniSheen品牌设备（如摄像头或工控设备） |
| root | a1sev5y7c39k | 复杂密码可能用于企业级设备（如防火墙或VPN设备） |
| root | cxlinux | 基于Linux的嵌入式设备（如某些工控系统） |
| root | sr1234 | 可能为监控设备（如某些DVR或NVR） |
| root | neworang | 新橙科技（NewOrange）摄像头或物联网设备 |
| root | neworange88888888 | 新橙科技（NewOrange）摄像头或物联网设备 |
| root | neworangetech | 新橙科技（NewOrange）摄像头或物联网设备 |
| root | oelinux123 | Linux系统或嵌入式设备的默认凭证 |
| root | hslwificam | HSL品牌WiFi摄像头 |
| root | jvbzd | 不确定，可能为某小众品牌设备 |
| admin | stdONU101 | 光纤网络单元（ONU）设备（如标准配置的光猫或运营商设备） |
| admin | stdONUi0i | 光纤网络单元（ONU）设备（如标准配置的光猫或运营商设备） |

**2.2.2、解密算法**

HailBot.b的域名解密算法与HailBot.a相同，均为ChaCha20。且解密使用的key、nonce也与HailBot.a相同。其中：解密使用的key为“16 1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F 17 02 03 13 18”，nonce为“1E 00 4A 00 00 00 00 00 00 00 00 00”。

![](https://image.3001.net/images/20250213/1739436585_67adb229e13ba0c755650.png!small)

图 2‑5 ChaCha20算法的key和nonce

**2.2.3、上线包**

HailBot.b样本中，大部分样本的上线包保持一致，均为：“56 63 34 86 90 69 21 01”。少部分样本（如MD5：F0E951D1ACFDF78E741B808AB6AB9628）的上线包与HailBot.a相同，为“31 73 13 93 04 83 32 01”。

![](https://image.3001.net/images/20250213/1739436572_67adb21cab2de6fb39959.png!small)

图 2‑6 发送上线数据包

**2.2.4、DDoS指令**

HailBot.b相较HailBot.a支持的DDoS指令有所增多。HailBot.b支持的DDoS指令如下表所示。

表 2‑5 HailBot.b支持的DDoS指令

|  |  |  |
| --- | --- | --- |
| **指令号** | **功能** | **影响** |
| 0 | TCP泛洪攻击 | 通过创建连接发送大量512字节的TCP请求消耗受害者网络带宽。 |
| 1 | UDP泛洪攻击（512字节） | 通过大量512字节的UDP请求消耗受害者网络带宽，不具备异常处理。 |
| 2 | GRE IP泛洪攻击 | 通过大量封装有...