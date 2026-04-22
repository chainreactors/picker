---
title: 超全UDS 诊断测试
url: https://mp.weixin.qq.com/s/xLHKR9XjmBpAC6WXcFcerQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:42:57.216997
---

# 超全UDS 诊断测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDwYnds4yv2XibmCvOWeU7DdykuTvToEWQkDNpPsdPf9Hz3hoD6SGwwobyGbMADSjMSf1wQPiaFSNZtFn0ff7sfo1TtT4AteqSxw/0?wx_fmt=jpeg)

# 超全UDS 诊断测试

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**UDS基本概念**

**OSI模型**

UDS（Unified Diagnostic Services，统一诊断服务）是汽车电子设备中电子控制单元（ECU）环境中的诊断通信协议，在ISO-14229中规定。

ISO-14229在OSI七层模型中的位置如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB9SKbbBl5rgSBxe6MYkXJs8wWMXByWxXppmgkYsU2bEH4Oh1wWdibQdg6AmB6KVxOgTMiafyHEK2m7UOfzWRhAxXcibkSIGJ4aaI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAlXARNvT4hLnLVTfGdRTNWDQqV1C7Y8P3bGickf4RHlVsMmecG6ANicxrkBvNkLFnIicYvzfnA4IibXpdBzA3qWTlVorfKb3ZODMI/640?wx_fmt=png&from=appmsg)

**诊断交互方式**

诊断是以服务为基础的两方交互数据和命令的过程，一方是Request，另一方是Response，下面是Request和Response的基本格式：

Request基本格式有两种：

SID + Parameter
SID + SubFunction + Parameter

Response基本格式有两种类型：

Positive Response（Request被正确的执行）：

（SID+0x40） + Parameter
（SID+0x40） + SubFunction + Parameter

Negative Response（Request执行错误或者不能在规定时间内完成）：0x7F + SID + NRC

Physical Addressing：物理寻址，诊断仪与单独ECU进行诊断交互。

Functional Addressing：功能寻址，诊断仪与总线上所有ECU进行诊断交互，即广播模式。

SID：Service Identity

NRC：Negative Response Code

Note1：功能寻址下在Request中SubFunction的最高位bit7若置0x01，正响应会被抑制，即不回复正响应，负响应正常回复。

Note2：功能寻址下NRC=SNS (serviceNotSupported), NRC=SNSIAS (serviceNotSupportedIn-
ActiveSession), NRC=SFNS (sub-functionNotSupported), NRC=SFNSIAS (sub-functionNotSupportedIn-
ActiveSession) or NRC=ROOR (requestOutOfRange），负响应会被抑制，即不回复这些负响应，正响应正常回复。

**诊断NRC**

诊断常用NRC如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCWKU1WWPtVK9fc0Wy2G5JfcZMpVxSEleNJ0RicqrbPsxfYicZ47s3P0qt83PPolZaoyhWfxicvw8JjOceGyOf3ZMaH7U8vZDKEyI/640?wx_fmt=png&from=appmsg)

**02**

**常用诊断服务**

**诊断会话控制**

DiagnosticSessionControl（0x10）

诊断会话控制服务用于在电控单元所支持的诊断会话中转换当前的会话。一个诊断会话使能电控单元的一个特定诊断服务集以及相关诊断功能。某些诊断服务在特定的会话下会限制使用。

诊断功能上电后处于默认会话，当跳转到其他会话时，会启动S3计时器，计时器超时会自动跳转回默认会话，S3计时期间任何服务请求会更新S3计时器重新计时。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCaEL7uHWV4kBBCHrzHyqvyiajicW6UgssrjU8zltAibrwKhxEzZot3fg5wsZ00EyLQgmeAibLpUfUF1ARLSjeKOydT4wcAFkkeNDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAXG2Ce6YGpZhibBpKdFCQAdYYjWhr2KR4SMibYyNibLIbPS4Rx9QDINlKA77TCNBZQw73jjaIPRjE9M2bawhqcl1Qq5bQZjZbwjM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaARqaXRyOokzL58xyVR8qslU6MRL5RlSDfr4gLtsC7o8kLw6GqP8Nj4WQKTBl5GS5gPp3z9Dl6TR4bf17lc3P04ZA5Rdht8Oqk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB9neR3t787YLnl2x1icNNve4lImoXB3dMcnke0qicib3S4tAQRL5zViaKnJnhkcevKzFoKCjkjFnv2yNqpc2r2eaagC34WqmKViadw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaALstJhWIH5t8gQ8rRicbzx3ptWUgQOOIm8clOBkQK76ntku3kUxN14S98bh1QIERY1ZGpZI8e31wAGLjoicuCuKESZPiaN03f4Q4/640?wx_fmt=png&from=appmsg)

**ECU重启**

ECUReset(0x11)

电控单元复位服务用于要求电控单元根据复位类型参数值来有效执行复位操作。电控单元复位服务的肯定应答报文一般在复位操作执行之前发送。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBSwaobdxBS0vNnN4eIwaHJiau01hpGPFsFNWospa8NmZBhdkvhnpTTEkEjQZsx8dia5AZ8cVyuqM6Qpfsb3oB55lKBHSQDA5xcE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC21yhhtJBYibCXGpBf6wJjrg6sGMI6XcLT2YMNENibn25Lbq92ibkA3JmEseCe2gl8Fu9Ae7EptAyDQ3y1TkSiah4ZebE7zSxozicI/640?wx_fmt=png&from=appmsg)

**安全访问**

SecurityAccess(0x27)

由于保密、排放或安全的原因，安全访问服务提供一种方法以便访问受限制的数据或诊断服务。该安全方法采用种子和密钥的算法。种子和密钥都为32位（4字节）。

安全访问服务一般会定义最大尝试访问失败次数和达到最大尝试访问失败次数后的延时时间用于防止被破解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCTicXbVh0wAWURTeMp25gtY3AZl5pKbFva7gLemfSdcn9kTNn0bmIHLuubW86BicW4kf8rOicbXIkxH3gLRwHZHEG8NrYEQRia8Rc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaApKSNlR1t4CPXwDEmaRCpwHULMsyMD8YtjjT7c9fH4pAyT9BicX49AcpicJickUXY8bTOCaMH0up2QTMkFs5O0vCUFZCHJh2HdaU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCibgaCib0WODRiaQ4cO28q8Ar1pv4lkUbQx1gsEdnYSWGenxo0aJRHrH4hakicibLCgZ7RfUErt4AWrvXtPOEVprrUPA7lGOhAU7lY/640?wx_fmt=png&from=appmsg)

诊断仪与ECU安全访问交互过程:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDYlBCk4OokibGltp6mJpIuI5Y8TTZC9wTIbj2yEP8r2HnD58wz2T0K2NTcO09KaQPvdWuXIzvSWuPSSib4ib3yaYf9eiba9qdic2s0/640?wx_fmt=png&from=appmsg)

**通讯控制**

CommunicationControl (0x28)

通讯控制服务用于开启/关闭电控单元对某些报文的发送或接收。

通讯类型一般为应用报文和网络管理报文。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB3gDKUXKxQHCokSZknFiciclCtBtndvPMwhd11LNjbYctNCfYicx7WlSgyGxCJOXicibg9A168e45fTg93A6K89uDAeIQrATrWowtk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDjfD6Bp83LTqnTvVzkuaAuXdYu3yQKPZczl2BibP106Bb8GFkzTqCHzkAHGlqPct4eFvBaPCoicDJr7LAiamI4iajkBSDGib9xZRAQ/640?wx_fmt=png&from=appmsg)

**诊断仪保持连接**

TesterPresent (0x3E)

测试工具保持连接服务用于告知电控单元测试工具仍在线。该服务一般周期性发送，用于重置S3server 计时器并维持当前激活的非默认诊断会话。

诊断处理模块同一时间只能处理一个诊断请求，正在处理当前请求时忽略其它所有诊断请求，只有一个例外情况是功能寻址下的诊断已保持连接服务且开启正响应抑制位，即 0x3E 80。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDTv3vGUcSm2QGuuibhXg4aqZLF7Av6EIPHibQ2EDQODBCUuvEmibkMDVSn6PMuDDzttebFK2ibOuQQ3DQibewY9ChXbe16xIsJL69E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCMXybD1Dgd0ZC15IwvMiaQKlhPOOiaT9OBDyM3ficiae8438q2SYdtZ3XTTMMUEc9aKVuzdVx9IcTXM4b3n1F060szT7B9lTOEW28/640?wx_fmt=png&from=appmsg)

**控制DTC设置**

ControlDTCSetting (0x85)

控制诊断故障代码设置服务用于停止或重启电控单元设置诊断故障代码。

当接收到子功能参数为“开”的控制诊断故障代码服务请求，会话层时序参数超时（电控单元进入默认会话）或电控单元执行复位操作后，诊断故障代码状态信息应重新开始更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDrtzjPCplVeUfpCjew9GBiboibwpJSUTJwNslStU5AF94LC7Sicgic5Eec887Coc2TFia9U8pWLqmzLLBNKiavp4SXzib95RjbicbfQ9k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCic3hhp9n8XTBiaP8yYhnY5tof8njCdzsnAoabwUQ1DSoVYicTLYbaJrnaiaLWiaGvyTT3l8LNt8d9W7W3Z4ZdqTSpNXsfbyFfZnSw/640?wx_fmt=png&from=appmsg)

**通过标志读数据**

ReadDataByIdentifier (0x22)

根据标识符读取数据服务用于从电控单元存储器中读取由数据标识符所确定的数据记录值。根据电控单元的支持情况，这些数据记录可能包括模拟输入输出信号、数字输入输出信号、内部数据和系统状态信息。

该服务的请求报文支持一次读取多个数据标识符的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBYtuoZNxdTgCfKEP6QAFMsMO5IfLcG9vibj4JebHDusvYRKia3ib9Euzq6ib0QgdYAekZuiax7kGeu9K6YWpgkMmjjibnDPEEzSfphk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCozKljsHJHJZKujlq3sVXAUWMpOtial7j6a7Qibo94TdSqnawtWoasID73Jzf9sJK9siaXtxQLhNf8187JITPlP75Zpobg6Fnxics/640?wx_fmt=png&from=appmsg)

**通过地址读内存**

ReadMemoryByAddress (0x23)

根据地址读取存储器服务用于从一个连续的地址区域读取数据。该服务一般用于电控单元开发阶段时读取无法通过其它诊断服务获取的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAPEJHhPd8AfShkXu0eSRZuD1YvNGMbQ3MV6VW0RJibwTqPvH37XOMJXOBIdNlW9JpUfHS6iaDsnS3GObQYhHWPq9cHnQlnaibstU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBtA0hPgn3rMmGMqpeRdiaSlW1ksxyDoUtLzJeT1bBicsF7xS1TSAuhhb1ID03ib1AYVuHdYffg8uU9O0Cm5V2XGib6tpCB80bbZVo/640?wx_fmt=png&from=appmsg)

**通过标志写数据**

WriteDataByIdentifier (0x2E)

根据标识符写入数据服务允许测试工具将数据写入由数据标识符指定的内部存储单元。电控单元应在数据已写入非易失性存储器后发送该服务的肯定应答。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDibYQAiaNMoiaxkunpd46weIs8PpK7O20JsaGmMEYDte3N2MhibKAS0qED4jQ4EM19HNRU60u3xzibIHVPbMWLNR0icSCGuicia8n9BEo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDKnTjPlPqAYSib6z2MDqAvwXxJic3z4bCbWGnVP7KPGkfCMRic5TfZ7L8OW4O6e1wysLbHwA5yWu0SVLU4UKkffQRKiaZJDhGTZO8/640?wx_fmt=png&from=appmsg)

**通过地址写内存**

WriteMemoryByAddress (0x3D)

根据地址写入存储器服务用于向电控单元的一个或多个连续存储单元写入数据。该服务主要用于电控单元开发阶段时写入无法通过其它诊断服务修改的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCibxy1XX0mcePSCMfYjUPwocB5eIibtuDbCJZsT9CibTJu9vggzopOqzSnehnAer5t2F2fOPCkIYvadJ3Gicn1DZrdkecwyU7aAHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpRHxiaXDIyp8ZxExj0eo1d97c2vPpaVwlpDMX2MicicLXToIU5icsxukhBZQMEErF6P83pmuegHhFjRz0yGOwqR6FhGXBzVQEMXc/640?wx_fmt=png&from=appmsg)

**清...