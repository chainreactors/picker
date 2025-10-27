---
title: 攻击DeepSeek的僵尸网络HailBot的三个变种分析
url: https://www.4hou.com/posts/ommL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-28
fetch_date: 2025-10-06T20:35:28.322297
---

# 攻击DeepSeek的僵尸网络HailBot的三个变种分析

攻击DeepSeek的僵尸网络HailBot的三个变种分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 攻击DeepSeek的僵尸网络HailBot的三个变种分析

安天
[技术](https://www.4hou.com/category/technology)
2025-02-27 17:06:18

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)256495

收藏

导语：安天CERT在2月5日发布了《攻击DeepSeek的相关僵尸网络样本分析》报告，分析了攻击中活跃的两个僵尸网络体系RapperBot和HailBot和其典型样本，分析了其与Mirai僵尸木马源代码泄漏的衍生关系。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739437090668472.jpg "1739437090668472.jpg")

**1 概述**

安天CERT在2月5日发布了《攻击DeepSeek的相关僵尸网络样本分析》报告，分析了攻击中活跃的两个僵尸网络体系RapperBot和HailBot和其典型样本，分析了其与Mirai僵尸木马源代码泄漏的衍生关系。安天工程师依托特征工程机制，进一步对HailBot僵尸网络样本集合进行了更细粒度差异比对，在将样本向控制台输出的字符串作为分类标识条件的比对中，发现部分样本修改了早期样本的输出字符串“hail china mainland”，其中数量较多的两组分别修改为“you are now apart of hail cock botnet”和“I just wanna look after my cats, man.”。为区别这三组样本，我们将三组变种分别命名为HailBot.a、HailBot.b、HailBot.c，对三组样本的传播方式、解密算法、上线包、DDoS指令等进行相应的分析。其中也有将输出字符串修改为其他内容样本，但数量较少，未展开分析。

**表 1‑1 HailBot三个变种之间的关系**

|  |  |  |  |
| --- | --- | --- | --- |
|  | HailBot.a | HailBot.b | HailBot.c |
| 特殊字符串 | hail china mainland | you are now apart of hail cock   botnet | I just wanna look after my cats,   man. |
| 传播方式 | CVE-2017-17215漏洞 | CVE-2017-17215漏洞  CVE-2023-1389漏洞  破解攻击（账号密码数量45） | CVE-2017-17215漏洞  CVE-2023-1389漏洞  暴破攻击（账号密码数量96） |
| 解密算法 | ChaCha20算法  key：“16   1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F   17 02 03 13 18”    nonce：“1E 00 4A 00 00 00 00 00 00 00 00   00” | ChaCha20算法  key：“16   1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F   17 02 03 13 18”    nonce：“1E 00 4A 00 00 00 00 00 00 00 00   00” | ChaCha20算法  key：“5E   8D 2A 56 4F 33 C1 C9 72 5D F9 1D 01 6C 2F 0B 77 3D 81 94 58 40 63 0A 79 62 1F   80 5C 3E 16 04”    nonce：“1E 00 4A 00 00 00 00 00 00 00 00   00” |
| 上线包 | 31   73 13 93 04 83 32 01 | 大部分样本：56 63 34 86 90 69 21 01  少部分样本：31 73 13 93 04 83 32 01（与HailBot.a一致） | 56   63 34 86 90 69 21 01 |
| DDoS指令 | 8个指令，指令号0-7 | 15个指令，指令号0-14 | 10个指令，指令号0-7、11、14 |

**2 样本分析**

**2.1 HailBot.a**

HailBot.a，是其最早变种，由于其运行时向控制台输出“hail china mainland”，相关僵尸网络因此被命名为HailBot。本节内容与第一篇分析报告有部分内容重复，主要为了对比不同版本变种间的差异特点。

HailBot.a的样本信息如下表所示。

表 2‑1 HailBot.a典型样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Linux.Mirai[Backdoor] |
| MD5 | 2DFE4015D6269311DB6073085FD73D1B |
| 处理器架构 | ARM32 |
| 文件大小 | 74.78 KB (76,572 bytes) |
| 文件格式 | ELF 32-bit LSB   executable |
| 加壳类型 | 无 |
| 编译语言 | C/C++ |

**2.1.1 传播方式**

HailBot.a利用漏洞进行传播，其长期使用的CVE-2017-17215漏洞存在于特定版本路由器的UPnP（通用即插即用）服务中。攻击者可以通过发送特制的HTTP请求在目标设备执行任意代码。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739437050202840.png "1739437050202840.png")

图 2‑1 HailBot.a构造漏洞利用载荷

**2.1.2 解密算法**

HailBot.a运行后首先对域名进行解密，其解密操作采用了ChaCha20算法。key为“16 1E 19 1B 11 1F 00 1D 04 1C 0E 08 0B 1A 12 07 05 09 0D 0F 06 0A 15 01 0C 14 1F 17 02 03 13 18”，nonce为“1E 00 4A 00 00 00 00 00 00 00 00 00”。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739437030567137.png "1739437030567137.png")

图 2‑2 HailBot.a使用chacha20解密字符串

**2.1.3 上线包**

HailBot.a运行后发送上线数据包，内容为：“31 73 13 93 04 83 32 01”。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739437020756818.png "1739437020756818.png")

图 2‑3 HailBot.a发送上线数据包

**2.1.4 DDoS指令**

当接收到攻击者发送来的指令后，HailBot.a将根据不同指令执行对应的DDoS攻击。HailBot.a支持的DDoS指令如下表所示。

表 2‑2 HailBot.a支持的DDoS指令

|  |  |  |
| --- | --- | --- |
| 指令号 | 功能 | 影响 |
| 0 | TCP泛洪攻击 | 创建连接发送大量500至900字节的TCP请求消耗受害者网络带宽。 |
| 1 | SSDP泛洪攻击 | 利用简单服务发现协议（SSDP）发送大量“发现消息”请求使受害者进行响应，消耗受害者内存和CPU资源。 |
| 2 | GRE IP泛洪攻击 | 发送大量封装有IP网络数据包的GRE协议数据消耗受害者网络带宽。 |
| 3 | SYN泛洪攻击 | 发送大量SYN数据包，使服务器创建具有大量处于半连接状态的请求，消耗系统内存和CPU资源。 |
| 4 | UDP泛洪攻击（512字节） | 发送大量512字节的UDP请求消耗受害者网络带宽。 |
| 5 | UDP泛洪攻击（1024字节） | 发送大量1024字节的UDP请求消耗受害者网络带宽。 |
| 6 | TCP STOMP泛洪攻击 | 发送创建连接发送大量768字节数据消耗受害者网络带宽。 |
| 7 | TCP ACK泛洪攻击 | 发送具有随机源端口、目的端口及数据等信息的ACK数据包消耗受害者网络带宽。 |

**2.2  HailBot.b**

HailBot.b同样是基于Mirai源代码二次开发的僵尸网络，输出的字符串为：“you are now apart of hail cock botnet”。

HailBot.b的典型样本信息如下表。

表 2‑3 HailBot.b典型样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Linux.Mirai[Backdoor] |
| MD5 | BB9275394716C60D1941432C7085CA13 |
| 处理器架构 | AMD64 |
| 文件大小 | 93.34 KB (95,576 bytes) |
| 文件格式 | ELF 64-bit LSB   executable |
| 加壳类型 | 无 |
| 编译语言 | C/C++ |

**2.2.1 传播方式**

HailBot.b同样利用了CVE-2017-17215漏洞进行传播。

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739437001143465.png "1739437001143465.png")

图 2‑4 HailBot.b中的CVE-2017-17215漏洞利用载荷

部分样本有利用CVE-2023-1389漏洞进行传播。

此外，HailBot.b样本中还发现用于暴破攻击的用户名和密码，如下表所示。

表 2‑4HailBot.b暴破攻击使用的用户名和密码和对应产品服务

（表格内容基于DeepSeek整理输出，并做人工修订，特此说明）

|  |  |  |
| --- | --- | --- |
| 用户名 | 密码 | 可能关联的服务/品牌/设备类型 |
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

**2.2.2 解密算法**

HailBot.b的域名解密算法与H...