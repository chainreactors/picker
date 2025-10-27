---
title: 【安全研究】Symbiote分析与检测
url: https://www.secpulse.com/archives/195368.html
source: 安全脉搏
date: 2023-02-07
fetch_date: 2025-10-04T05:50:20.721203
---

# 【安全研究】Symbiote分析与检测

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

# 【安全研究】Symbiote分析与检测

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[安全狗](https://www.secpulse.com/newpage/author?author_id=32873)

2023-02-06

15,112

↑ 点击上方 关注我们

**一、概述**

近期，我们发现一种新型的Linux恶意软件Symbiote被报道出来，该恶意软件被描述为“****几乎不可能被检测到****”。之所以被命名为Symbiote（中文含义：共生体），也是基于该样本的攻击性质：作为非独立运行的共享库文件加载到其他正在运行的进程中。其目的是窃取远程主机的登录凭证以及后门访问。

下面将对该恶意软件的其中一个样本进行详细分析。

**二、详情分析**

**1****加载方式**

LD\_PRELOAD是Linux系统的一个环境变量，它可以影响程序的运行时的链接（Runtime linker），允许你定义在程序运行前优先加载的动态链接库。通过这个环境变量，可以在主程序和其动态链接库的中间加载别的动态链接库。通过覆盖正常的库函数，注入到正在运行的进程，从而达到特定的目的。

该样本使用同名、同参数的自定义函数，通过LD\_PRELOAD的方式加载到其他进程中，进而覆盖掉同名的系统函数，优先调用自定义函数，达到调用过程劫持效果。

所有的劫持函数都如下图逻辑：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654612.png) 图1

**2****进程隐藏**

该样本会隐藏自身加载到其他程序中的共享库痕迹，以及隐藏一起部署的其他恶意程序。

* ###### **隐藏其他恶意程序**

实现方式为，挂钩readdir、readdir64、stat、statx、fstatat、fstatat64等函数，目标文件在/proc下时，获取执行命令，判断是否为需要隐藏的进程，若是，则跳过该条目信息，继续执行返回下一个无需隐藏的文件条目信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654613.png) 图2

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654614.png) 图3

本样本隐藏的进程名

certbotx64

certbotx86
javautils

* ###### **隐藏共享库痕迹**

除了隐藏一起部署的其他恶意程序，还会隐藏自身模块。如用户可通过ldd命令输出指定的每个程序或共享对象所需的共享对象（共享库）。如下图所示，ldd命令会调用execve函数，该样本就通过挂钩execve的方式劫持返回结果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546141.png)图4

通过LD\_TRACE\_LOADED\_OBJECTS环境变量判断是否为列出其动态库依赖项（ldd命令）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654615.png)图5

具体隐藏过程如下，fork一个子进程去执行命令，返回结果到管道。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654616.png)图6

在本进程中，使用后面的字符串数据覆盖掉需要隐藏的自身库字符串再输出，达到隐藏效果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546161.png)

图7

运行效果图如下，该样本目前只是过滤硬编码写入的文件名，改名后就会显示出来，不排除后续版本会更新为自动获取名称。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654617.png)图8

**3****文件隐藏**

除了隐藏进程相关的文件，还会隐藏其他非进程的信息存储文件。

在Linux系统中，使用ls、dir、tree等命令显示出目录下的文件信息，通过挂钩文件相关函数readdir、readdir64就可以实现文件隐藏。

具体细节如下，读取到需隐藏的文件流时，继续读取下一个，直至该文件流为非隐藏文件或为空才返回。这样就跳过了恶意文件，达到隐藏目的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654618.png)

图9

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546181.png) 图10

隐藏的文件列表

certbotx64

certbotx86
javautils
bancodobrasildev
search.so
certbot.h
cert.h

**4****网络隐藏**

该样本采用了三种流量隐藏的方法，分别是劫持fopen函数、劫持注入eBPF、劫持libpcap库函数。

* ###### **劫持fopen函数**

检测到程序使用fopen读取procnet目录下的文件时，便会生成一个临时文件，读取源文件的每一行并将过滤掉指定端口的数据写入临时文件，最后将过滤后的临时文件句柄返回调用者，达到隐藏效果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654619.png)

图11

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546191.png)

图12

* ###### **劫持注入eBPF**

BPF(Berkeley Packet Filter), 中文翻译就是伯克利包过滤器。从字面意思可以知道它的主要功能是用来过滤数据包的。根据介绍，BPF 钩子位于网络驱动中尽可能早的位置，无需进行原始包的复制就可以实现最佳的数据包处理性能，挂载的BPF程序是运行过滤的理想选择。

下面是BPF流程图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654620.png) 图13

劫持方法是挂钩函数setsockeopt，该函数用于设置socket状态。

检测到使用SO\_ATTACH\_FILTER方式调用时，表示该调用用于数据包过滤。此时就会先将自身的BPF字节码添加到其他软件的BPF字节码前，先一步过滤掉需隐藏的流量，再执行其他软件注入的BPF字节码进行过滤。

本样本用此方法过滤TCP连接中指定端口的流量（包括入站出站）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654621.png)图14

* ###### **劫持libpcap库函数**

实现方法是挂钩函数pcap\_loop、pcap\_stats这两个函数。

挂钩函数pcap\_loop、pcap\_stats这两个函数，在函数pcap\_loop中，劫持捕获流量后执行的回调函数，在恶意回调函数中，匹配流量中需要过滤的域字符串，通过包数计数器加一，丢掉这个流量包。

本样本中用此方法隐藏UDP流量数据。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546211.png)图15

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654622.png)图16

**5****恶意功能**

该样本的主要目的有：窃取用户登入凭证，后门远程访问、文件下载命令执行。

* ###### **凭证记录**

当用户使用ssh或者scp并通过公私密钥key进行远程主机访问时，挂钩后的read便会获取调用程序命令行参数，获取远程主机的地址、连接RSA私钥等信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654623.png)图17

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546231.png)图18

使用简化的CR4算法加密后，存放在/usr/include/cerbot.h文件中，并通过 DNS 地址 (A) 记录请求泄露到攻击者的控制的域名。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546232.png)图19

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654624.png)图20

* ###### **后门远程访问**

该样本劫持Linux系统上可插拔认证模块（PAM）的关键函数pam\_set\_item、pam\_authenticate、pam\_acct\_mgmt。其中pam\_set\_item函数用于截取用户登入密码，pam\_authenticate函数用于校验密码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-1675654625.png)

图21

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195368-16756546251.png)

图22

这意味着攻击者可以使用写入的硬编码口令，以任意用户远程访问受害者服务器。

而当其他用户使用远程访问工具（ssh）访问受害者服务器时，便会获取远程主机ip、登入口令等信息，作为凭证窃取的一部分发送至攻击者域名。

* ###### **文件下载命令执行**

在使用pam\_authenticate函数进行身份验证时，若不是攻击者访问，还会向其命令与控制域C&C发送 DNS 地址 (TXT) 记录请求。TXT 记录的格式为%MACHINEID%.%C2\_DOMAIN%。

如果收到响应，恶意软件使用 base64 解码内容，使用Ed25519算法检查内容钥签名，使用 RC4 解密内容，并在生成的 bash 进程中执行 shell 脚本。

**6****CR4**

在该样本中，所有的字符串都是通过简化的CR4算法获取，该CR4算法核心如下：

```
S = [0]*256for i in range(256):    S[i] = i    index = 0for j in range(256):    index = (S[j] + index + initKey[(j%keyle...