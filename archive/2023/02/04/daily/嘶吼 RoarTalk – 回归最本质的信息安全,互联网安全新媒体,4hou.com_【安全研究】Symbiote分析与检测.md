---
title: 【安全研究】Symbiote分析与检测
url: https://www.4hou.com/posts/PJO1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-04
fetch_date: 2025-10-04T05:39:51.503899
---

# 【安全研究】Symbiote分析与检测

【安全研究】Symbiote分析与检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【安全研究】Symbiote分析与检测

安全狗
[技术](https://www.4hou.com/category/technology)
2023-02-03 17:38:58

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144163

收藏

导语：​近期，我们发现一种新型的Linux恶意软件Symbiote被报道出来，该恶意软件被描述为“几乎不可能被检测到”。

**一、概述**

近期，我们发现一种新型的Linux恶意软件Symbiote被报道出来，该恶意软件被描述为“几乎不可能被检测到”。之所以被命名为Symbiote（中文含义：共生体），也是基于该样本的攻击性质：作为非独立运行的共享库文件加载到其他正在运行的进程中。其目的是窃取远程主机的登录凭证以及后门访问。

下面将对该恶意软件的其中一个样本进行详细分析。

**二、详情分析**

1加载方式

LD\_PRELOAD是Linux系统的一个环境变量，它可以影响程序的运行时的链接（Runtime linker），允许你定义在程序运行前优先加载的动态链接库。通过这个环境变量，可以在主程序和其动态链接库的中间加载别的动态链接库。通过覆盖正常的库函数，注入到正在运行的进程，从而达到特定的目的。

该样本使用同名、同参数的自定义函数，通过LD\_PRELOAD的方式加载到其他进程中，进而覆盖掉同名的系统函数，优先调用自定义函数，达到调用过程劫持效果。

所有的劫持函数都如下图逻辑：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rzcqF4u8j1jPR5Vo7nqSYicziaicbribz9bdR3D2QNVckn2QvpfoqC8gPag/640?wx_fmt=png)

2进程隐藏

该样本会隐藏自身加载到其他程序中的共享库痕迹，以及隐藏一起部署的其他恶意程序。

* 隐藏其他恶意程序

实现方式为，挂钩readdir、readdir64、stat、statx、fstatat、fstatat64等函数，目标文件在/proc下时，获取执行命令，判断是否为需要隐藏的进程，若是，则跳过该条目信息，继续执行返回下一个无需隐藏的文件条目信息。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rkqSSLbTc1aft4UY94de8iaEyGiaJeZ5IN6ZdjL5dOh4CDIWjpg9zH60w/640?wx_fmt=png)

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rAlwibJ1wb1XrCwHibgLd3aQIymYCibSwv2EmVicgJQ3IgN0pOBFpFXQFXw/640?wx_fmt=png) 图3

本样本隐藏的进程名

certbotx64

certbotx86
javautils

* 隐藏共享库痕迹

除了隐藏一起部署的其他恶意程序，还会隐藏自身模块。如用户可通过ldd命令输出指定的每个程序或共享对象所需的共享对象（共享库）。如下图所示，ldd命令会调用execve函数，该样本就通过挂钩execve的方式劫持返回结果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0r2k0GoDjicqic50zMEvEczZeFnoAMia2caVppdIfQJicibkRbib9XVxI96WEA/640?wx_fmt=png)图4

通过LD\_TRACE\_LOADED\_OBJECTS环境变量判断是否为列出其动态库依赖项（ldd命令）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rSuujOG1NxnxhaIFdUu7w9FIqDOGMhnahyBu66a76icEhqMAWgWIkMicg/640?wx_fmt=png)图5

具体隐藏过程如下，fork一个子进程去执行命令，返回结果到管道。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0r4IRFQm1t72d5LJYKf0lFHurT9DWCc0taMkbciaNLwCjwaZic0ACh9ic8Q/640?wx_fmt=png)图6

在本进程中，使用后面的字符串数据覆盖掉需要隐藏的自身库字符串再输出，达到隐藏效果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rCJBFOQ1Uw20wZwNatNc47QQMvQoaHZb2RGQHVChjEhXkWZvxZsic6HA/640?wx_fmt=png)

图7

运行效果图如下，该样本目前只是过滤硬编码写入的文件名，改名后就会显示出来，不排除后续版本会更新为自动获取名称。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rGN9Uy6Irovm66lKUH0L33X3YyjAdGGw88BjgpMYicvqOMqCrpCGDaoQ/640?wx_fmt=png)图8

3文件隐藏

除了隐藏进程相关的文件，还会隐藏其他非进程的信息存储文件。在Linux系统中，使用ls、dir、tree等命令显示出目录下的文件信息，通过挂钩文件相关函数readdir、readdir64就可以实现文件隐藏。

具体细节如下，读取到需隐藏的文件流时，继续读取下一个，直至该文件流为非隐藏文件或为空才返回。这样就跳过了恶意文件，达到隐藏目的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rMc2Ist6yacjdSGrhPBn8ggNyUSoem2vXezjn1b4iay8q8y65nzZibE4Q/640?wx_fmt=png)

图9

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rhEBOauZq2z2l6XJDqs4micjtLCkfzgcch8f8yKW3PzlFE7vNQ6xiaFhw/640?wx_fmt=png) 图10

隐藏的文件列表

certbotx64

certbotx86
javautils
bancodobrasildev
search.so
certbot.h
cert.h

4网络隐藏

该样本采用了三种流量隐藏的方法，分别是劫持fopen函数、劫持注入eBPF、劫持libpcap库函数。

* 劫持fopen函数

检测到程序使用fopen读取\proc\net\目录下的文件时，便会生成一个临时文件，读取源文件的每一行并将过滤掉指定端口的数据写入临时文件，最后将过滤后的临时文件句柄返回调用者，达到隐藏效果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rBKge08xSMppHjLsAfsSgUY8EzIarzPSQcfhe6t7odcsEenz8r9nVNA/640?wx_fmt=png)

图11

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rxrYnYdWCicuQ9DAd07TzI4aASMR7skzcZhhXf5Kp4qLSp1feVCPn1Ig/640?wx_fmt=png)

图12

* 劫持注入eBPF

BPF(Berkeley Packet Filter), 中文翻译就是伯克利包过滤器。从字面意思可以知道它的主要功能是用来过滤数据包的。根据介绍，BPF 钩子位于网络驱动中尽可能早的位置，无需进行原始包的复制就可以实现最佳的数据包处理性能，挂载的BPF程序是运行过滤的理想选择。

下面是BPF流程图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rpjCoQbjYCP6cib17nnmCDjzic9ze5PjibBLLrJGoEJ1hVrs5QbbDG5ykA/640?wx_fmt=png) 图13

劫持方法是挂钩函数setsockeopt，该函数用于设置socket状态。

检测到使用SO\_ATTACH\_FILTER方式调用时，表示该调用用于数据包过滤。此时就会先将自身的BPF字节码添加到其他软件的BPF字节码前，先一步过滤掉需隐藏的流量，再执行其他软件注入的BPF字节码进行过滤。

本样本用此方法过滤TCP连接中指定端口的流量（包括入站出站）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rcCTeKt2jP9eSOUJ48fYG6CGk2xIjJwtxQ3ribV68xBRD4ebmyoGEwhQ/640?wx_fmt=png)图14

* 劫持libpcap库函数

实现方法是挂钩函数pcap\_loop、pcap\_stats这两个函数。

挂钩函数pcap\_loop、pcap\_stats这两个函数，在函数pcap\_loop中，劫持捕获流量后执行的回调函数，在恶意回调函数中，匹配流量中需要过滤的域字符串，通过包数计数器加一，丢掉这个流量包。

本样本中用此方法隐藏UDP流量数据。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rY9GX2OHCI16wOJBK85lpfbDUCDDrw629h3Hia6lyybbNjwSTyHjnqCw/640?wx_fmt=png)图15

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rNDibCiaWZLE1furv6O0Vwg6RgyN1bekkxaSjCdd6hRuica3mnCfic4WSGQ/640?wx_fmt=png)图16

5恶意功能

该样本的主要目的有：窃取用户登入凭证，后门远程访问、文件下载命令执行。

* 凭证记录

当用户使用ssh或者scp并通过公私密钥key进行远程主机访问时，挂钩后的read便会获取调用程序命令行参数，获取远程主机的地址、连接RSA私钥等信息。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0ryTBEZpqBsSeyvRevlok28IYu1aVAJpibgfsfWbedFBTNGIPw7IPeCtQ/640?wx_fmt=png)

图17

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0ryMDc0Da8g8zTOT8TzxibUL50Yd8yBD9B3ibCtIhR2NgjbxxNVjicXjJzA/640?wx_fmt=png)

图18

使用简化的CR4算法加密后，存放在/usr/include/cerbot.h文件中，并通过 DNS 地址 (A) 记录请求泄露到攻击者的控制的域名。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0ribwHNfM1O1wTgKqoeWX6DE8wzUjnlY56PCO7qaRL8Y2LeoCxckoDDvw/640?wx_fmt=png)

图19

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0ropEUzbXrkawWJWxTrdYqF1ic3FWTKj4iaxYSXcflKNSKOR0yeKP3Djtg/640?wx_fmt=png)图20

* 后门远程访问

该样本劫持Linux系统上可插拔认证模块（PAM）的关键函数pam\_set\_item、pam\_authenticate、pam\_acct\_mgmt。其中pam\_set\_item函数用于截取用户登入密码，pam\_authenticate函数用于校验密码。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rWQNVf4nYpPRku3voDzbia5tn9iaa4vOVw8OBiablf3c9m2Wib7TNsmgmyw/640?wx_fmt=png)

图21

![图片](https://mmbiz.qpic.cn/mmbiz_png/tLPRyPAiapwLQEuHE1YPWKvAasZcpNX0rUq1M1RUia9onHibDXUSYBEM3VqKLR2ibGvvRCEAfKj7NicibtEwKV4U7YFg/640?wx_fmt=png)

图22

这意味着攻击者可以使用写入的硬编码口令，以任意用户远程访问受害者服务器。

而当其他用户使用远程访问工具（ssh）访问受害者服务器时，便会获取远程主机ip、登入口令等信息，作为凭证窃取的一部分发送至攻击者域名。

* 文件下载命令执行

在使用pam\_authenticate函数进行身份验证时，若不是攻击者访问，还会向其命令与控制域C&C发送 DNS 地址 (TXT) 记录请求。TXT 记录的格式为%MACHINEID%.%C2\_DOMAIN%。

如果收到响应，恶意软件使用 base64 解码内容，使用Ed25519算法检查内容钥签名，使用 RC4 解密内容，并在生成的 bash 进程中执行 shell 脚本。

6CR4

在该样本中，所有的字符串都是通过简化的CR4算法获取，该CR4算法核心如下：

```
index = 0j = 0for OdrText in range(textlen):    j = (j+1) % 256    index = (index + S[j]) % 256    S[j],S[index] = S[index],S[j]    hexList[OdrText] ^= S[(S[j] + S[index])%256]
```

**三、检测思路**

底层函数绕过：该样本是通过挂钩用户层的一些关键函数进行隐藏，可以通过更底层的文件操作函数进行检测。

特殊工具：还可以使用完全静态编译的工具，如busybox，该工具静态编译Linux常用命令，不依赖共享库，此方式可以破解该样本的隐藏手段。

行为特征检测：该样本目前还未隐藏export与环境变量显示相关的命令结果，所以还可以检测环境变量LD\_PRELOAD，进而发现问题。

流量特征检测：既然在终端上不好检测流量，那就在在网络出口处进行流量检测。

欺骗检测：针对搜集到的隐藏文件信息，创建同名文件判断是否被隐藏，也可以检测。

内存特征匹配：经过测试，...