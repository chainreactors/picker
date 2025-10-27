---
title: 揭秘APT-C-26（Lazarus）组织利用PyPI对Windows、Linux和macOS平台的攻击行动
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247499462&idx=1&sn=7cc55f3cc2740e8818648efbec21615f&chksm=f9c1cdcfceb644d9a6f169ca81188a0e3ab4a9799437f6c57b71ede3ac6aab6d121dd023d42a&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-07-06
fetch_date: 2025-10-06T17:45:07.123179
---

# 揭秘APT-C-26（Lazarus）组织利用PyPI对Windows、Linux和macOS平台的攻击行动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsV14eRrlrtIs3DP2uEia9k3vmiaVfrH3XMa4Vv7gRHgPVicE3gg2iaBMQyAQ/0?wx_fmt=jpeg)

# 揭秘APT-C-26（Lazarus）组织利用PyPI对Windows、Linux和macOS平台的攻击行动

原创

高级威胁研究院

360威胁情报中心

**APT-C-26**

**Lazarus**

APT-C-26（Lazarus）组织是一个高度活跃的APT组织。该组织除了对金融机构和加密货币交易所感兴趣外，也对全球的政府机构、航空航天、军工等不同行业开展攻击活动，主要目的是获取资金和窃取敏感信息等。其攻击方式主要包括网络钓鱼、网络攻击和勒索软件攻击，并且它们的攻击行为具有高度的技术复杂性和隐蔽性，也具备Windows、Linux、MacOS系统攻击能力，以及拥有多种攻击载荷武器。

360高级威胁研究院捕获到了Lazarus组织通过恶意Python包下发攻击载荷的多个攻击样本，然后通过层层加载，最终完成攻击行为，并且这些样本针对了Windows、Linux、MacOS等不同操作系统，可见该组织针对目标人群不遗余力的开发各类攻击武器。鉴于该组织近期频繁通过将恶意载荷存放于Python包的方式攻击多个平台，因此我们在这里进行详细分析，希望经过曝光披露，相关的企业和个人可以提高安全防范意识，保护企业财产和相关用户财产免受损失。

# **一、攻击活动分析**

## **1.攻击流程分析**

本轮攻击中，Lazarus组织通过PyPI仓库向各个平台的用户投递恶意样本进行攻击，其中Windows系统下的安装包携带加密载荷，通过层层解密，内存加载Comebacker恶意样本；Linux系统下的恶意安装包加载后，完成初始化时会远程下载ELF恶意文件，该文件具备完整的远控功能；在MacOS系统下，我们捕获的恶意样本和Linux系统下的恶意样本功能相似，文件名也类似，并且还具有相同C2，因此我们推测MacOS系统下的执行流程大概率与Linux下相同，也是通过PyPI仓库进行投递。相关攻击流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVNEOxVBLxDMbqLFocgh4SnUXdQ8ibhnYIlygsJmGKdb48ekQ4y4rsppQ/640?wx_fmt=png)

## **2.Windows载荷分析**

### **2.1 载荷投递方式**

本次我们捕获到了多个利用Python包投递的恶意样本，这些样本通过在Python包存储库PyPI进行传播，现均被下架。具体样本信息如下：

|  |  |
| --- | --- |
| **MD5** | **文件名** |
| 8c351d35369a63d6c4a1478428a593d7 | pycryptoenv-1.0.7.tar.gz |
| 267ef172f81bb8577e5371fbf20f7306 | pycryptoenv-1.0.7-py3-none-any.whl |
| 1352f2621107e503cddde3bcc0d53d52 | quasarlib-1.0.8.tar.gz |
| 133b1621d76bd7f1f4c814f53cd501bc | quasarlib-1.0.8-py3-none-any.whl |
| 5a25375f2b23680690fe82c99cf3d314 | pycryptoconf-1.0.6.tar.gz |
| 10f190b9bbb875d3b2582ae9229da634 | pycryptoconf-1.0.6-py3-none-any.whl |
| 494f2cc788afc585b4a5bd39ecb6dcca | swapmempool-1.0.8.tar.gz |
| 11c0ce888a5aedf82c509c4dca1b5b00 | swapmempool-1.0.8-py3-none-any.whl |

这些软件包都携带相似的恶意代码且功能相同，但是这些软件包安装后都不会自动执行恶意代码，需要在一定条件下调用函数才能执行，因此在这里猜测这些Python软件包可能不是最终的版本。以其中之一（swapmempool-1.0.8-py3-none-any.whl）进行分析说明，包文件结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVL6BfDPQ3ryHch9TBPtVLUBSiaDiaICUQ63R1ceGDXx4UdTATmiaxEbU4g/640?wx_fmt=png)

当Python包被安装时在特定情况下会执行\_\_init\_\_.py文件里的load函数，该函数通过传入参数对同目录下的utilities.py和command指令进行XOR解密，解密文件保存为config.py，该文件实际为DLL文件，然后通过rundll32 "config.py", AddNumbers jweo执行恶意功能。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVZMb6tqXJHWbZ19zhxIkJ8HUs2Dhu37vjz5aGFUckL7gFQs4AhbQZhQ/640?wx_fmt=png)

### **2.2 攻击组件分析**

解密得到的config.py恶意载荷信息如下所示：

|  |  |
| --- | --- |
| MD5 | 330fff5b3c54a03fd59a64981e96814d |
| 文件大小 | 342.50  KB (350720字节) |
| 文件名 | config.py |
| 编译时间 | 2024-01-16 07:36:44 UTC |

DLL的导出函数AddNumbers为空，当传入参数为宽字符时，对AddNumbers调用实际会执行AddNumbersW函数。该函数将传入参数 “jweo”进行拼接得到密钥：“jweoED]YC^Yn124Na&+a1p1=HPZ]<7p5”用于解密出新的DLL载荷，接着内存加载该DLL的入口函数。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsV2CotlgGLibicZucw2okXicHyibkmAiaX89KWY1Oezew1WhFj7XoxyZlmW5g/640?wx_fmt=png)

解密后的DLL被加载起来时采用相同解密算法对自身数据继续解密，并释放Local\\Microsoft\\OneDrive\\OneDrive.pri和\\Local\\Microsoft\\Windows\\credential.sys文件，其中前者是恶意DLL,后者为数据文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVT7fEFaWoOUucbOhXzPddk51jJNl5D0Dw4ON1Jm7j6FpmaFOLfH7rSQ/640?wx_fmt=png)

接着尝试三种方式进行持久化，依次为创建计划任务、设置注册表和启动目录。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVgNbDaXdR9f5u9UkhQY0gnMiaOLSTlF70CWSZS4FcJlO0jicXfBbS3nMg/640?wx_fmt=png)

三种方式都执行相同的指令，如下：

```
cmd /c start /b rundll32 "%APPDATA%\\..\\Local\\Microsoft\\OneDrive\\OneDrive.pri,UpdateData %APPDATA%\\..\\Local\\Microsoft\\Windows\\credential.sys n0Yw "
```

OneDrive的UpdateData函数被调用时，实际也是执行UpdateDataW函数，该函数通过读取credential.sys文件进行解密出新的载荷并内存执行。与之前解密不同，本次采用两次解密，首先读取文件，获取实际数据大小，并判断标志位是否正确，若不符合直接返回，接着读取数据到缓冲区，然后继续读取数据“GgoC!ur|fJFt8rwM{{$;4k#p\*b>:Q”与传入的“n0Yw”参数组成新的密钥用于第一次解密，接着再采用之前相同的方式进行第二次解密出PE文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVGgnic5KRQv3sYcuyBvohBPcsNPBzpNuvZU42tNKcw4ib1zC70NiaClyEg/640?wx_fmt=png)

通过credential.sys文件两次解密得到的DLL，该DLL类型为Comebacker，其主要功能是继续下载下一阶段payload并执行。

其流程首先是获取C2地址，接着向服务器发送的POST请求。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVibFBP4ERmnTcQrqgia7PZMXHA3HH9fb61BIyXx5UKK6mIDnbZRicCWdMA/640?wx_fmt=png)

请求参数按照如下方式进行拼接,共有七对参数，下图是其中六对参数，图中备注了一些重要参数的说明，其中参数的key基本都是随机大写字母，最后一对参数其key和value都为随机大写字母。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVkEI3wjdzjpcLOZ6pV55Zx2sCh4BO6IpZzLkiacGY4HK9YDkFtXU5kWg/640?wx_fmt=png)

若请求到后续载荷并校验通过，则对payload进行解密并执行。需要说明的是，同期我们也捕获到多个该下载器类型的恶意样本，猜测这些样本可能是通过Python包或npm 软件包[1]进行投递，但没获取到后续载荷。

## **3.Linux载荷分析**

### **3.1 载荷投递方式**

Lazarus组织在Linux下分发恶意软件过程跟Windows类似，将恶意程序隐藏在Python软件包，并上传至Python包存储库PyPI中，遗憾的是现在官方PyPI已下架，不过在某些自动同步PyPI的镜像站还能看到攻击者上传的部分Python包，下图展示的只是coloredtxt包，此外攻击者还上传了real-ids、beautifultext、minisound等Python包。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVG3tNrlKkN43okYicwOib6CBmD3EJO3KdQFnDGjnqml89Sy1LtMHfSoxA/640?wx_fmt=png)

我们以其中coloredtxt-0.0.2.tar.gz文件为例分析。

|  |  |
| --- | --- |
| MD5 | 73850470a358c79b0a67eb809491dfdb |
| 文件大小 | 132 KB |
| 文件名 | coloredtxt-0.0.2.tar.gz |

这些恶意载荷存放在os.py文件中，当用户安装coloredtxt库时，会调用\_\_init\_\_.py完成包的初始化，该过程会导入此OS模块，执行有效负载。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVQDm80UUiceF3LfW2QKk2icWfgSwNxciabOjSFXbj0llylkxo6cBib8K1sQ/640?wx_fmt=png)

os.py模块中关键代码如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsV4kS19ibtBm1uTbLkV71ib78bGAM4qLnpqFCd74K2H1Nu4zVCu3vicLicgw/640?wx_fmt=png)

攻击者主要代码通过base64加密多次，经过base64多层解密后通过exec执行，解密后的代码如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsV9DoM4AO1jfmTr1s6x4Gb5oiaMu0jWloCAoriaDNZiaL1wW53SQfbC23Xg/640?wx_fmt=png)

主要功能是通过curl从pypi.online下载下一阶段文件，命名为oshelper，并设置cookie为 oshelper\_session=10237477354732022837433。另外下载过程中会判断系统版本，如果是windows则不会进行下载,下载的链接为https://pypi.online/cloud.php?type={系统平台首字母}，如果是linux则为https://pypi.online/cloud.php?type=l，如果是MacOS，则URL末尾替换成type=m即可，现已无法下载。

特别需要说明的是，在其他恶意安装包，攻击者关键代码不是通过base64加密，而是通过十六进制编码，如下所示，解密后的代码基本类似，都是通过curl下载下一阶段代码，只是下载链接变成了https://arcashop.org/boards.php? type={系统平台首字母} ，这里不再详细分析。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVKdOg02v93QZ6pkh1iaAPZCzGgqQ5QyAowyytIZRdYNpwu8WAxMNpotw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsV5mcQWw22JTib07Ofej21U4icUOo1s8P1CZ29SXsYiaCDFB57QCUBCicL2w/640?wx_fmt=png)

### **3.2 攻击组件分析**

下载的Linux样本基本信息如下：

|  |  |
| --- | --- |
| MD5 | 33c9a47debdb07824c6c51e13740bdfe |
| 文件名称 | oshelper |
| 文件大小 | 2.60 MB (2,734,385 字节) |
| 文件类型 | ELF |

oshelper是一个由GCC编译的64位ELF可执行文件，但在编译的时候并没有去除符号信息，我们可以通过工具查看到函数名。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVNk549PSHGbH4F7rePIQetA9WMgUJEXuHLYicFEvGfQJpIBlzwsicTrdg/640?wx_fmt=png)

在分析过程中，我们发现oshelper默认使用https协议和C2服务器进行通讯，以加密通讯过程中的流量，但是作者也提供了http协议的选项，只是该开关并没有启用。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVViaplzXljW2Vh5AaGCPNsA7c5mMlSmBLQC2zAfZeeRUHE2ZFvtxiarGg/640?wx_fmt=png)

另外oshelper使用了特定的http报文头部与C2服务端进行通信，以避免被空间测绘工具识别。接着将获取的pid以及tuid信息加密编码，以“lkjyhnmiop=&odldjshrn=odlsjdfhw&ikdiwoep=”形式发送到https://jdkgradle.com/jdk/update/check，待服务端返回“OK”字样说明通讯正常。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqFcpXLEfyCicAtY58Zb5IsVMhLXzLKj1ZH6k4nvbbOFdt5T1dGOVevDpR0RsPCdcicfQ9xibpMJ6fHA/640?wx_fmt=png)

经过分析，oshelper是远控程序，下表是具备的远控功能。

|  |  |
| --- | --- |
| 命令号 | 功能描述 |
| 0x892 | 发送响应，并休眠 |
| 0x893 | 上传文件 |
| 0x894 | 下载文件 |
| 0x895 | 发送响应，不休眠 |
| 0x897 | 命令执行，不回显 |
| 0x898 | 命令执行，并回显 |
| 0x899 | 退出进程 |

## **4.MacOS载荷分析**

### **4.1 载荷投递方式**

在MacOS系统下，我们捕获的多个恶意样本和Linux系统下的恶意样本功能相似，文件名也类似，并且还具有相同C2。此外在分析Linux的载荷投递流程来看，攻击者在下载链接时只选择了判断是否为Windows，因此结合这些我们推测MacOS系统下的执行流程大概率与Linux下相同。

### **4.2 攻击组件分析**

我们以其中一个MacOS样本进行分析，基本信息如下：

|  |  |
| --- | --- |
| MD5 | 05957d98a75c04597649295dc846682d |
| 文件名称 | os\_helper |
| 文件大小 | 169 MB (173,792 字节) |
| 文件类型 | macho |

os\_helper是一个Mach-O文件，Mach-O是MacOS以及IOS上一种用于可执行文件、目标代码、动态库的文件格式。

![](https://mmbiz.qpic....