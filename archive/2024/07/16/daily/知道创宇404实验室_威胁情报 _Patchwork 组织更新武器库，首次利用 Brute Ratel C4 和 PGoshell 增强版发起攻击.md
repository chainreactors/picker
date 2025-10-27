---
title: 威胁情报 |Patchwork 组织更新武器库，首次利用 Brute Ratel C4 和 PGoshell 增强版发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650979510&idx=1&sn=15bbbb3f6dcd4ffac9a1ac00ed1de042&chksm=8079fe84b70e7792ec592efa376522b6c235ecd3985cfba7914ea044fb867529bf0a97e5c7d5&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-07-16
fetch_date: 2025-10-06T17:45:01.006423
---

# 威胁情报 |Patchwork 组织更新武器库，首次利用 Brute Ratel C4 和 PGoshell 增强版发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatAteWtCxovakicKn87aEcugjuibbkiafuXvoAnGB0iasoLicZIbzp5XjQ0FQ/0?wx_fmt=jpeg)

# 威胁情报 |Patchwork 组织更新武器库，首次利用 Brute Ratel C4 和 PGoshell 增强版发起攻击

原创

404高级威胁情报

知道创宇404实验室

**作者：********K&********XWS******@知道创宇404高级威胁情报团队****

**时间：2024年7月15日**

**1. 概述**

参考资料

近期，知道创宇404高级威胁情报团队捕获到Patchwork组织疑似针对不丹的攻击样本，该样本除加载已多次发现的go语言后门(以下称“PGoShell”)外，还大规模增强了功能。与此同时，样本首次使用了红队工具Brute Ratel C4，即近期观察到的比较大的武器更新。该组织在最近2年的攻击活动中，于技术方面比其他同源组织投入的热情更多，并不断更新自身的武器库及加载方式。迄今为止，已发现该组织使用了超过10种不同的木马及加载方式。以下将对本次发现进行分析和描述。

**2. 组织背景**

参考资料

Patchwork （又称Dropping Elephant）是一个极为活跃的高级持续性威胁 (APT) 组织，自 2014 年以来一直在开展活动。Patchwork 主要针对东亚及南亚等亚洲地区的政府、国防和外交组织以及大学，科研机构。

**3. 攻击链**

参考资料

样本链如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatvrOmgJY9y91bU9qNzK3wetvDic2kaookiaUKLDn2RHhUG0KYmFyaZaRw/640?wx_fmt=png&from=appmsg)

**4. 样本综述**

参考资料

此次捕获的样本为Lnk文件，其主要功能是下载诱饵文件和后续载荷。经过对载荷的分析后发现，此次攻击使用的武器包括PGoShell以及红队攻击框架Brute Ratel C4，详情如下：

## **4.1 lnk分析描述**

lnk文件名为Large\_Innovation\_Project\_for\_Bhutan.pdf.lnk，当用户未开启文件后缀显示时，极易将其当作pdf文档打开，在lnk运行后，其中包含的脚本参数也得以运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatuvtWrWXArBib8loQIIia8St3RYQWjO1wo466tAiaOicThft1Nd5toicicvxQ/640?wx_fmt=png&from=appmsg)

lnk参数

参数包含的操作如下。

1.操作一：访问并下载uri（hxxps://adaptation-funds.org/documents/Large\_Innovation\_Project\_for\_Bhutan.pdf）文件至本地 C:\Users\Public\Large\_Innovation\_Project\_for\_Bhutan.pdf，该文件为诱饵文档，下载完成后运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatJiaDuzmMCpQgYxf1qyw3Xib0jdX1kbIfKdDr6s8yufzGmwrxRa44Qt3A/640?wx_fmt=png&from=appmsg)诱饵文档部分截图

诱饵文档内容为adaptation fund(适应基金董事会)关于不丹的项目提案，疑似针对不丹相关机构和个人。

2.操作二：访问并下载uri（hxxps://beijingtv.org/wpytd52vDw/brtd2389aw）数据至本地C:\Users\Public\hal，并将其重命名为C:\Users\Public\edputil.dll，值得注意的是该域名疑似仿冒北京电视台。

3.操作三：访问并下载uri（hxxps://beijingtv.org/ogQas32xzsy6/fRgt9azswq1e）数据至本地C:\Users\Public\sam，并将其重命名为C:\Users\Public\Winver.exe。

4.操作四：从系统目录复制resmon.exe到C:\Users\Public\resmon.exe，创建名为MicroUpdate的计划任务，该计划任务每分钟执行一次，执行目标为C:\Users\Public\resmon.exe。创建名为MicroUppdate的计划任务，该计划任务每分钟执行一次，执行目标为C:\Users\Public\Winver.exe，最终删除lnk文件。

**4.2 Brute Ratel C4(edputil.dll)分析**

4.2.1 Brute Ratel C4 loader分析描述

resmon.exe为系统文件，运行后会加载edputil.dll。基于windows默认加载原则，与resmon.exe同目录下的edputil.dll将被加载，edputil.dll使用themida加壳：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatmkke7Ac8miahBQt7Gz4c0nddgCVENGUggMTtD7YURMt5kiaseVav3zUA/640?wx_fmt=png&from=appmsg)edputil.dll区段中的.themida段

最终resmon.exe加载EdpGetIsManaged导出函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatHWTodzibFmqChhKHyYibibBUG1wWNwYa7jvDhXCXSFlCtlkgiclOpr7fwA/640?wx_fmt=png&from=appmsg)edputil.dll导出表

EdpGetIsManaged导出的主要功能既是Brute Ratel C4 loader，攻击者首先会利用自定义的hash算法获取api地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iattibN2TgHTr6YR4HFicfr3AibhYP2uBDyJJicddHTXox3tjV9Jpe07vy3xw/640?wx_fmt=png&from=appmsg)通过hash获取api地址

为达到unhook和反调试的目的，攻击者将获取对应函数的系统调用号，然后获取“syscall”指令地址，以NtProtectVirtualMemory函数为例，其中调用号为“0x50”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatibpb9kEZ7L9ibEsHx66fP1MzwiaTNXqbW9yXSqtD9JCEgDuexoV1W5sbw/640?wx_fmt=png&from=appmsg)获取调用号及“syscall”地址

后续若需要调用NtProtectVirtualMemory，则只需要将调用号（0x50）传入eax，再调用“syscall”的地址即可完成函数的调用，利用此调用方式，传统的下断点将失效：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatrqib2907uBqLW3t0MqJxVpCp34L5rGmheiaCtXLEyZoVVTCicO0nKVN7A/640?wx_fmt=png&from=appmsg)syscall调用代码片段

将shellcode写入申请的内存中，更改新分配的内存的保护，通过NtCreateThreadEx创建线程并执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatymTNicgdRvVicB3N3vpZVumH07t8cbJ2wf3ICgbdfMMTjQTCqmhnYicVg/640?wx_fmt=png&from=appmsg)Shellcode运行

Shellcode的主要功能是加载最终载荷（Brute Ratel C4），它首先会进行调试器检测，接着对PEB中的NtGlobalFlag值进行对比，若为0x70则结束运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iat00E0HsW6xcVpaklicMkS5Vjp7ic55dO7aV9EmuQx3ofJ8p6T79icUE7Ig/640?wx_fmt=png&from=appmsg)调试器检测

获取后续需要使用的api地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iat4HB4LBRfNJiaFmLFJ1vlbIvibbor4Xc58aP7CR9NIFYLoeusiagqQyrrQ/640?wx_fmt=png&from=appmsg)获取api地址

接下来进行系统时间检测，若当前系统时间超过硬编码的时间戳（0x66c0666d），则结束运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatdue6uGiaY8zGVQeulB0SnN0QmRPvXe1MmXicjXjInMEOEGS70dia0icu6Q/640?wx_fmt=png&from=appmsg)运行时间检测

使用RC4算法解密出后续需要加载的文件名（chakra.dll），该文件主要作为Brute Ratel C4的载体：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatGVbGjV3l5vJyZCicRHL5Fn85gkC0dFvYhYKP1MeWfLnaFlC5aBUlNbw/640?wx_fmt=png&from=appmsg)解密数据

chakra.dll被加载后，将去除“MZ”头的最终载荷Brute Ratel C4写入chakra.dll的地址空间，并模拟加载Brute Ratel C4：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatuIN39x03BOiak7TSKhCoTwXxF4QyBhicc8icfS4OquYpdCpjKA4oorurA/640?wx_fmt=png&from=appmsg)去掉”MZ”的Brute Ratel C4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatU8CNshxW0cjNIib2GL3VDNe4RcgZoE9cgniaibo3B67X9UcliaYN9zxlhw/640?wx_fmt=png&from=appmsg)将数据写入chakra.dll内存空间

获取OEP并跳转执行，最终执行载荷既是Brute Ratel C4：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iat2qFSPz0sYJbrALaFcICAbaR2QiaicCqwUVG8JXMoa4lt4ibtJGRW6KE2Q/640?wx_fmt=png&from=appmsg)跳转OEP执行

### 4.2.2 Brute Ratel C4简述

Brute Ratel C4是一个红队框架，并被视为Cobalt Strike 的替代品。该框架能够实现诸如文件管理、端口扫描、文件上传下载、屏幕截图等功能，以下为本次该载荷的配置截图，各项配置间使用“|”进行分隔：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iat6b2dp3YcZNDOvcPraSs6xF62CMJcNx9P8RMSvH4aGPr4qyXZITDNRg/640?wx_fmt=png&from=appmsg)

Brute Ratel C4配置截图

**4.3 PGoShell（Winver.exe）分析**

PGoShell由Go语言开发，总体来看其功能较丰富，包括远程shell、屏幕截图，载荷下载执行等，由于首次发现该武器时主要功能为远程shell故而得名。相关详细逆向分析内容如下：

初始化URI、RC4密钥，User-Agent,本次样本中RC4密钥内容为“0g8RXt137ODBeqPhTv2XYjgmnxUsijfc”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatxoPMCPdHhXictsLKlyBdpo2X6TwSViaPgYUFDibTdEcGhIbguuN6DiaobQ/640?wx_fmt=png&from=appmsg)初始化URI、RC4密钥

检测HKCU\Software\Microsoft\WinTemp是否存在，若存在则获取temp键对应的值；若不存在则生成随机字符串，并使用RC4+base64加密后写入，该值将作为ID被上传到服务端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatlcibqQpUC4UwAyBy1NLpGPx5TdZPx1RoVic0LF1Y4BGhiae9OLdaCu0cg/640?wx_fmt=png&from=appmsg)

进入信息收集&交互模块后，PGoShell首先会尝试获取主机信息(主机名、用户名、当前主机对公IP、当前主机所处国家(IP及国家信息由查询ip-api.com获取)、当前系统版本、当前执行路径、进程PID、PROCESSOR\_ARCHITECTURE信息)，获取成功后将对应的数据进行拼接，各信息数据使用“||”进行分隔。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatmK4YVK5FsQJA5GDy2EnKSF7iabrl3wCc1gyNaWcFxibibBu205TBAWkJw/640?wx_fmt=png&from=appmsg)获取主机信息并拼接

PGoShell获取到的所有数据均使用RC4+base64进行编码（截图中main\_AESENC为攻击者迷惑分析人员编写的函数名，其内在实际为RC4+base64）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatibBCIIeOyshTSTbRVajrJuibdicd4ncZiciagzWEwDVib4emZL4L1PLHh1Yw/640?wx_fmt=png&from=appmsg)RC4 Key及其解密数据

随后将拼接的数据发送到服务端，并从服务端获取数据，上线信息以及交互信息上传方式均采用POST方式。

PGoShell部分功能如下表：

| 功能号 | 功能 |
| --- | --- |
| c?d????????e | shell |
| vypjtvwudmta | 文件下载 |
| zdqxjjiueled | 下载执行 |
| mldijkppffollpps | 下载执行 |
| s?p????????t | 屏幕截图 |
| ssaphdnu | 下载powershell bypass脚本并运行 |
| tcvbwmdddqls | 检查文件是否存在，存在则上传 |
| egdhdnipjhfn | 从指定url下载shellcode并注入 |
| jhudjphsmunee | 利用WMI枚举设备信息 |
| getmdjfhhkjhsdfdc | 获取域控信息 |
| nemszyrsmuns | 下载Solo.zip到temp目录，解压后执行其中的powershell脚本 |
| nfjdnteslbt | 下载shellcode并通过QueueUserAPC注入执行 |
| ndhbnmesnefdmu | SMB端口扫描 |
| rdptidjkeephdnmak | RDP端口扫描 |

**5. 总结**

参考资料

本次捕获的攻击活动主要以adaptation fund(适应基金董事会)关于不丹的项目提案作为诱饵，针对对象疑似为不丹相关机构和个人。在此次攻击活动中，首次发现Patchwork组织使用Brute Ratel C4作为武器。整个Brute Ratel C4加载运行过程为纯内存加载，能够有效对抗终端设备检测。在加载过程中，多次进行反调试和解除挂钩操作，并在执行周期上进行了限制。这表明该组织正在积极扩充其武器库。根据网络信息，Brute Ratel C4的作者来自于印度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatvJ6QOuAhqXOImQp2wydics67CaOn1MyWoMwz5CRz4fIzmJCrhs7AhaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT06iaYcdBtLK3icLHtficgV3iatRIpvtuocHgBPopcgGwZWKrsg9dAvIZicZVicNIzoPuq7B...