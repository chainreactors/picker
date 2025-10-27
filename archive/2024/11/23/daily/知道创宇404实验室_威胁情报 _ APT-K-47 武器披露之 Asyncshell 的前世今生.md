---
title: 威胁情报 | APT-K-47 武器披露之 Asyncshell 的前世今生
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650989978&idx=1&sn=8ca4005d50af2514a6e6cbd9e863b502&chksm=8079a7a8b70e2ebe3a771e0e13a01ad9b818f6883672bb0f7f0449044ef3dcfd727ed8473831&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-11-23
fetch_date: 2025-10-06T19:18:50.219616
---

# 威胁情报 | APT-K-47 武器披露之 Asyncshell 的前世今生

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT2ib8AiaDoJqlrbicvlmrFFTvvxagc3MGjukZHnSqYDJaPiayGxqzmiazBqMj1eU3ic00PicJ7EV5neLzNOg/0?wx_fmt=jpeg)

# 威胁情报 | APT-K-47 武器披露之 Asyncshell 的前世今生

原创

404高级威胁情报

知道创宇404实验室

**作****者：**知道创宇404高级威胁情报团队****

**时间：2024年11月22日**

**1 分析概述**

参考资料

近期，知道创宇404高级威胁情报团队在日常跟踪APT过程中发现了APT-K-47组织利用“朝觐”话题发起的攻击活动，攻击者利用CHM文件执行相同目录下的恶意载荷。最终载荷功能比较简单，仅支持cmd shell，且使用异步编程实现，这与团队在2023年-2024年上半年的跟踪周期内该组织曾多次使用的“Asynshell”极其相似。根据我们的跟踪观察，此前掌握的Asynshell进行了多个版本的更新，基于代码逻辑和功能，我们有理由怀疑本次捕获样本为升级后的Asynshell。相较于以往，此次样本有如下特点：

1. 利用base64变种算法隐藏字符串。
2. 伪装成正常的网络服务请求来下发C2。
3. 去除大量的log信息。

为方便后续描述，将最新样本记为Asynshell-v4，以下将围绕本次捕获样本以及团队发现Asynshell版本变化的过程展开描述。

**2 组织背景**

参考资料

APT-K-47，也被称为Mysterious Elephant，是知道创宇404高级威胁情报团队首先披露活动细节的APT组织[1]。据推测该组织发源于南亚地区，其攻击活动最早可追溯至2022年。在对APT-K-47的技术手法、战术策略、工具运用以及行动目标进行深入分析时，可以看到南亚多个其他APT组织的影子，包括但不限于Sidewinder、Confucius和Bitter等。

**3 样本分析**

参考资料

#### 本次发现的初始样本为zip文件，包含加密的RAR压缩文件，并将包含解压密码的“Password.txt”置于同目录下。值得注意的是，由于文件被加密，导致无任何杀软报毒

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNW3o8J1ZTtXib6M0UWyYvV7z8qwml7VKq5jicEfkYpXfCDjVicQ7DOf3IA/640?wx_fmt=png&from=appmsg)图1 加密的压缩文件

RAR压缩文件解压后其中包含了一个chm文件和一个pe文件，其中PE文件被设置为隐藏：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNwy49Nia2vE749XzEy6Ltibj7PbJIBMYy0RCXsvdseG1T0SGYhc16iaDXQ/640?wx_fmt=png&from=appmsg)图2 解压后的文件

chm的主要功能是显示诱饵文件并使用快捷方式静默运行同目录下的“Policy\_Formulation\_Committee.exe”。

诱饵文件主要是关于宗教“朝觐”相关事宜：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNkF3EHk6OenhkVs4KemV8mKyX16gt5yJXWqGzUVAOF84L5N7zJBNicdw/640?wx_fmt=png&from=appmsg)图3 诱饵文件

#### **3.1 Policy\_Formulation\_Committee.exe分析描述**

Policy\_Formulation\_Committee.exe功能比较单一，通过特殊算法解密出伪装成正常的网络服务请求地址，并连接该请求下发的C2服务器完成cmd shell，利用这种方式能够灵活的改变连接地址，以保证长时间的控制受害者主机。

利用变种的base64编码解密出伪装成网络服务请求的服务器地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNnD4QflL49AcqU8rWsGiar3F9ozTUMXFd6Afa7LPQDgFPqdq42UWy0uQ/640?wx_fmt=png&from=appmsg)图4 伪装成网络服务请求的服务器地址

服务端返回数据为json，再对其中 RequestId对应的值进行标准base64解码得到最终shell连接的C2。

通过实例化名为“MagicFunctions”的类，并调用其中的“GraciousMagic”函数实现cmd shell的功能，cmd shell在交互过程中使用AES+标准Base64进行数据加解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNRdC6217mNkacSedzz5GOhCWGl74rs2g3QBlar7ROniaZ2yzMHy4qI2g/640?wx_fmt=png&from=appmsg)图5 相关代码

**4 版本描述**

参考资料

知道创宇404高级威胁情报团队在披露APT-K-47组织后对该组织使用的多款武器进行了持续跟踪，就Asyncshell而言，团队根据部分特征的变化将其分为4个版本，详见下表：

表1 Asyncshell的4个版本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNic1CUGRdCpzfI6zXmOe7HHgPteBgk861flkMz9OlZKSuVaddf0xDyJg/640?wx_fmt=png&from=appmsg)

以下将对以时间线为主轴就Asyncshell的发现过程及版本更新进行描述。

#### **4.1 首次发现Asyncshell**

团队首次发现Asyncshell要追溯到2024年1月份，当时我们发现一个利用CVE-2023-38831漏洞的恶意样本，整体攻击链如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNcouUfqmtWBHHL7AYnCQSmDEX2sp5TguVv2V4rxDK7DiaRCNmp6e3cYA/640?wx_fmt=png&from=appmsg)图6 攻击链

攻击者利用关于在外地临时休假期间的公务员及临时公务人员的薪酬相关内容作为诱饵：![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNB59SO0KTjbc2qNlPWKsnibLbVvDrSqc1f3FWzI3MiaW4Rhvr8rv5jgLw/640?wx_fmt=png&from=appmsg)图7 诱饵文件

最终载荷使用Async编程实现shell功能，故将其命名为AsyncShell，为方便后续版本描述，记为AsyncShell-v1:![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdN5w7UUWCwNPibS8CpSydGHQ9Wr3USy6H7hbI8RnLeyN9s729dibwiauDnQ/640?wx_fmt=png&from=appmsg)图8 相关代码

AsyncShell-v1支持cmd命令和powershell命令：![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdN858lfff0LILLsD8yrRah7EWL0Mmo0cxf73VDN2lo41jpsoTlPtxNNQ/640?wx_fmt=png&from=appmsg)图9 相关代码

在对AsyncShell-v1分析后，我们从样本库中，关联出一个同类型样本，样本代码非常一致，最终接收的指令仅支持使用powershell进行解析执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNUmrm0umZuIp8E2oaoLicWpuF37aQNqibiaGQDHlxjdNiaiaxxqjRevskUUQ/640?wx_fmt=png&from=appmsg)图10 相关代码

对AsyncShell-v1进一步拓线后发现了多个同类型样本，并且猜测文件原始信息与入侵时间有一定的联系，根据目前拓线分析，此类型攻击首次投递可能在2023年9月份，针对的国家及主体包括巴基斯坦、孟加拉国、土耳其等，这与我们此前通过知道创宇遥测大数据观察到的该组织的攻击目标基本一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNHw9MrjopibCyJCKcm9b5WUkicVmX4ayQdUWtVyw1YxNNKbtmxyuxSuvw/640?wx_fmt=png&from=appmsg)图11 多个同类型样本

#### **4.2 利用CHM执行Asyncshell**

从样本库中入库时间来看，2024年3月，团队曾发现过APT-K-47使用Asyncshell的攻击活动，这也是我们首次发现APT-K-47利用CHM执行Asyncshell。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNgwy7OYojMQ5ZGGrHrVgXH7FupB6MRaqzF7NUXaRvMDJvdG74Of7Jgw/640?wx_fmt=png&from=appmsg)图12 利用CHM执行Asyncshell

同类型样本还包括：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNicE0aGFYFRmopS72ZPAEkIepABw7OiaChg2KJEWiaeIcoRcwyowMJ2vrw/640?wx_fmt=png&from=appmsg)

图13 样本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNr7V6MjWibARMb6KLvnHj0bn7IQibGhIsevlVlAhXtgChzQw3HDpKcNOQ/640?wx_fmt=png&from=appmsg)图14 样本

部分诱饵如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdN8VJrHhgo273IjlcDTR8MlNcGiaAtrcxicGbwiaG2psyPBLib6HUicAveeZg/640?wx_fmt=png&from=appmsg)

图15 诱饵文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNwPxGBiaEabWBuMnLmteUXtSLl6vibsk72ibEv7B8pIzgia8reXA7Vn2VQA/640?wx_fmt=png&from=appmsg)图16 诱饵文件

#### **4.3 从tcp到https的转变**

时间来到2024年4月，团队发现该组织1个新的Asyncshell攻击样本，攻击者将诱饵文档与载荷置于同一目录下，并将载荷文件名与诱饵文档设置为相同，在未开启文件后缀显示时，诱使受害者将载荷视为pdf文件点击执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdN7RQwC7Zw1MuibibibLTaVTBebh8VE7ml8qX4Y7nAYLPT4JlVxrwV4JKGQ/640?wx_fmt=png&from=appmsg)

图17 诱饵文件

当恶意载荷执行后将去掉文件路径的后4个字符，并执行该路径所指文件，即诱饵文档：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNmOIIhNmcztfWg2YPCP0TYbS21GOE2C2blPXnvuRdyIogUKjick0r4hA/640?wx_fmt=png&from=appmsg)

图18 诱饵文件

诱饵文档主要内容为PSC会议纪要：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNqPLJMkBb9pOxDqc3CxpXQjDXYYEKfHGtTBXlcQpc20WEqrRoS4YsDw/640?wx_fmt=png&from=appmsg)

图19 诱饵文件

载荷通信从tcp变为https，记为Asyncshell-v2:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNnXug0tbPBVbTuiblaFCx3uVlLSWg8MAl7QRjo1ohzfia2QJex2Ug1N5A/640?wx_fmt=png&from=appmsg)

图20 相关代码

样本计划使用“file.dat”回传执行结果，但实际对应的功能函数实现后并未调用。

根据以上信息，团队从样本库中关联到另外一个使用相同C2的同类型样本，部分诱饵如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNEftzhOXwPShaCgENIygSc1lpbMKR9wrgf1QlotgGItOGLphwtiaWAJg/640?wx_fmt=png&from=appmsg)图21 诱饵文件

该样本使用名为“commands.txt”的文件分发cmd指令，最终执行结果被上传到服务端。

#### **4.4 从文件中解密C2**

在2024年7月，团队捕获到Asyncshell变种，与此前版本不同的是：此次捕获样本整个攻击链条已经更新，记为Asyncshell-v3,详细见下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNgGWjxOnfCld0majMBF5xABgFCRFu8dpSckRTia5VY2Jzlt1uUFBzicDg/640?wx_fmt=png&from=appmsg)图22 攻击链

初始样本为zip文件，初始目录下的lnk文件主要完成VBS脚本的执行，VBS创建名为“WinNetServiceUpdate”的计划任务，计划任务执行主体为“cal.exe”（即Asyncshell-v3）。

诱饵文档如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNMtibibyRsTibwSp9jibQZniayXaSOdyKiaDg3k6NFtCKrnN40Dgzq2GzAE1Q/640?wx_fmt=png&from=appmsg)图23 诱饵文件

cal.exe运行后，将读取同目录下的“license”并使用AES解密，从中获取“ServerIP”和“ServerPort”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNicmPIsial13IP1B4D2BF0IdDTOVFysnB8A7qq4CZyz8KBHGeaFk0XJhA/640?wx_fmt=png&from=appmsg)图24 相关代码

同类型的攻击还使用了以下诱饵：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNbux5QicyuUCHNPK2HDoelDbGHb1kDkjiaEI1jz0I7jzRvesj9n6fd6VQ/640?wx_fmt=png&from=appmsg)图25 诱饵文件

最终载荷使用ConfuserEx进行混淆，读取并解密“SysConfig.enc”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNgjAAvUT3TicMhMib5xgGNGJia6Xy0YbicWWFdiaPVwpibrTy4g4SJkee5EfQ/640?wx_fmt=png&from=appmsg)图26 相关代码

**5 总结**

参考资料

基于以上分析，可以看出APT-K-47从2023年开始频繁使用Asyncshell发起攻击活动，并逐步对攻击链和载荷代码进行升级。而在近期的攻击活动中，该组织更是巧妙的利用伪装的服务请求来控制最终shell服务端地址，从之前版本的固定C2变换为可变C2，可见APT-k-47组织内部对于Asyncshell的重视。

知道创宇404高级威胁情报团队自2023年披露该组织细节后，一直密切跟踪该组织动向，对于其使用的包括ORPCBackdoor、walkershell、Asyncshell、MSMQSPY和LastopenSpy等武器都有着深入分析，后续团队将持续对部分已掌握武器进行披露。若您对相关内容感兴趣，可联系Intel-APT@knownsec.com交流探讨。

**6 IOC**

参考资料

Hash：

5afa6d4f9d79ab32374f7ec41164a84d2c21a0f00f0b798f7fd40c3dab92d7a8

5488dbae6130ffd0a0840a1cce2b5add22967697c23c924150966eaecebea3c4

c914343ac4f...