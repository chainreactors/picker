---
title: Fodcha 僵尸网络样本再现更新，3项功能特性发生变化
url: https://www.secpulse.com/archives/199901.html
source: 安全脉搏
date: 2023-05-06
fetch_date: 2025-10-04T11:38:14.178593
---

# Fodcha 僵尸网络样本再现更新，3项功能特性发生变化

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

# Fodcha 僵尸网络样本再现更新，3项功能特性发生变化

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[知微攻防实验室](https://www.secpulse.com/newpage/author?author_id=40030)

2023-05-05

17,300

**0x01**

**背景**

近期，银弹实验室物联网威胁监测平台捕获到一款在物联网中快速传播的 DDoS 僵尸网络样本。该样本与 360 Netlab 在 2022 年发布的文章 **《卷土重来的DDoS狂魔：Fodcha僵尸网络再次露出獠牙》**中分析的样本在行为层面非常相似，经进一步比对，确认是 Fodcha 僵尸网络样本的新升级版本。

本文对此升级版本的Fodcha样本的新增功能和特性进行说明。对于未发生变化的部分，请大家阅读 360 Netlab 之前发布的文章，文章对样本有详细的分析和说明，此处不再赘述。

**0x02**

**概述**

此次捕获的样本涵盖mips、mpsl、arm 等架构，我们选取了 arm 架构的样本作为分析对象，经过对比，Bot 样本与 C2 通信的部分以及 DDoS 攻击的部分没有发生变化，这些主机行为也和之前一致，包括：

* 对运行参数、网络的连通性、是否设置“LD\_PRELOAD”环境变量进行检查，如果不满足要求就直接退出
* 当满足要求运行要求时，则首先解密出配置信息
* 在Console上输出 "snow slide"
* 单一实例
* 进程名伪装
* 操控 watchdog
* 清空特定端口进程
* 上报特定进程信息

除了以上功能，Bot最新增加了以下几项更新：

* 9条新的配置信息
* 设备独占功能
* 使用新的 C2 域名

下面我们将针对上述更新展开具体说明。

**0x03**

**新增配置项**

新增的配置信息通过密文保存，加密的方式和上个版本一样，使用 xxtea 加密算法进行加密，解密用的密钥改为 AE11Fjj43edj2j24e。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-1683266717.png)

解密后的配置信息内容如下，其中黄色字体的是这次样本新增的配置信息。比较有意思的是"投降字符串"也发生了变化，从原来的 "Netlab pls leave me alone I surrender" 变成了 "please. leave me alone netlab. i didnt provoke swear i love you"。

|  |  |
| --- | --- |
| INDEX | VALUE |
| 0 | snow slide |
| 1 | /proc/ |
| 2 | /stat |
| 3 | /proc/self/exe |
| 4 | /cmdline |
| 5 | /maps |
| 6 | /exe |
| 7 | /lib |
| 8 | /usr/lib |
| 9 | please. leave me alone netlab. i didnt provoke swear i love you |
| 10 | GET /geoip/?res=10&r HTTP/1.1rnHost: 1.1.1.1rnConnection: Closernrn |
| 11 | getcred.uk |
| 12 | api.opennicproject.org |
| 13 | watchdog |
| 14 | /dev |
| 15 | TSource Engine Query |
| 16 | /.ffxx |
| 17 | /proc/net/tcp |
| 18 | self |
| 19 | .dynamic |
| 20 | /dev/misc |
| 21 | /fh/extend |
| 22 | /fd |
| 23 | watchdog |
| 24 | / |

这些新增的配置信息主要用来拼接文件路径和匹配文件内容，以实现设备独占排他。

**0x04**

**样本分析**

新增的设备独占功能会阻止用户、后来的攻击者等管理和控制设备，降低Bot程序被发现的几率，形成独占设备的排他能力。该功能在打印 "snow slide" 之后执行，执行之后一些属于用户的进程被 kill 掉，并且用户创建的新进程或者打开的新终端也会被立刻关闭。

**4.1**

**效果**

在ubuntu 中运行此样本的效果如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-1683266718.png)

可以看到样本运行后再执行命令都显示 "Killed"，新的终端和其它程序也无法打开。

**4.2**

**技术原理**

样本通过实时遍历系统中所有进程并结束符合条件的进程来实现这个功能。代码通过一个死循环来不断检查当前的进程数，如果发现进程数发生变化，就遍历 /proc 目录下进程的 exe 文件和 cmdline 文件，并将符合条件的进程结束。循环部分的代码结构如下：

```
sysinfo(v3)
pid_count_1 = v3->procs //v3->procs 为此时系统中的进程数
while( 1 ){    pid_count_2 = v3->procs
    if( pid_count_1 != pid_count_2 ){         遍历/proc 目录下所有进程的 exe 文件和 cmdline 文件，结束符合条件的进程         pid_count_1 = v3->procs    }    else{        sysinfo(v3)    }}
```

Bot 样本在遍历 /proc 目录下的进程信息时，如果发现除自身进程外的其它进程满足下面的条件，就会将对应的进程结束：

* 启动参数包

  `"``wget``"、"``tftp``"、"``echo``"、``"``ftpget``"、"``curl``"、``"``reboot``"、``"``poweroff``"、``"``shutdown``"`

  中的任意一个字符串；

* 进程从

  `"``/bin``"、"``/sbin``"、"``/usr/sbin``"、``"``/usr/bin``"`

  `目录下启动；`
* 在进程所在目录下创建一个 .ffxx 文件，如果创建成功，则结束该进程，并删除 .ffxx 文件，目的是结束从可写目录下启动的进程。

**0x05**

**新增C2域名**

样本的网络通信部分和上一个版本的基本一致，通过 4 个步骤与 C2 通信：

* 解密密文获得 C2 域名
* 解析 C2 域名
* 建立通信
* 执行指令

其中有变化的部分是解密后拼接的 C2 域名，这次的 bot 使用了新的 C2 域名。样本使用两种类型的 C2 域名，一种是 OpenNIC 域名，另一种是常用的 ICANN 域名。样本会优先使用 OpenNIC 域名，如果 OpenNIC 域名解析失败再使用 ICANN 域名。

**5.1**

**OpenNIC域名获取**

样本先解密包含 OpenNIC 域名的密文，密文加密的算法和上个版本一样，使用的是 xxtea 算法，解密用的密钥是 AE11Fjj43edj2j24e，解密后的内容如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-1683266722.png)

解密后的字符串通过拼接后得到域名。它的拼接过程是这样，先从红框 '/' 符号处将内容分为两部分(上图中蓝色背景的部分)，第二部分只到"..."。第一部分和第二部分根据 ',' 进行拆分，然后从第一部分和第二部分的拆分结果中各选择一个使用 '.' 拼接。

第一部分内容按 ',' 拆分后得到的结果如下：

|  |  |
| --- | --- |
| 域名字符串 | 出现次数 |
| yesfridgexpertscc | 29 |
| weloveyellow | 21 |
| likenetlab | 21 |
| lovechinese | 17 |
| netlabisvalid | 16 |
| letsmakeadeal | 1 |
| notfridgexpertscc | 1 |
| gogogo1337 | 1 |
| changwang | 1 |
| skid | 1 |
| golangopython | 1 |
| 1337mirai | 1 |
| kinkyasskids | 1 |

第二部分按 ',' 拆分后得到的结果如下：

|  |  |
| --- | --- |
| 域名字符串 | 出现次数 |
| libre | 13 |
| geek | 8 |
| oss | 6 |
| ozz | 5 |
| pirate | 3 |
| com | 1 |
| gopher | 1 |
| dyn | 1 |
| indy | 1 |

拼接域名的时会选择一个第一部分拆分的字符串，然后通过算法得到第二部分对应的字符串，将它们用 '.' 拼接。下面是所有能够拼接出的域名：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image.png "image.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image.png)

**关于解密之后出现的字符串**

最开始我们猜测解密出来的一些字符串会两两随机组合拼接成域名，但实际并不是随机的。有些字符串没有用来拼接成域名，原因是这些字符串是占位使用的，Bot 样本生成域名的算法会通过计算 ',' 的数量来控制拼接的域名，这些字符串被用来增加 ',' 数量。作者会把一些口号作为占位的字符串，上个版本用来占位的字符串有

"wehateyellow"、"funnyyellowpeople"、"blackpeeps"、"bladderfull"。

这个版本用来占位的字符串有

"weloveyellow"、"likenetlab"、"lovechinese"、"netlabisvalid"。

**5.2**

**OpenNIC域名解析**

Bot 样本先使用公共的 DNS 服务器解析域名 api.opennicproject.org，解析成功得到对应的 IP，之后向这个 IP 的 80 端口发送 http 请求：

```
GET /geoip/?res=10&r HTTP/1.1rnHost: 1.1.1.1rnConnection: Closernrn
```

之后从接收的 http 响应中取出能够解析 OpenNIC 域名的 DNS 服务器地址，并使用这个服务器解析 C2 域名。

如果解析 **api.opennicproject.org** 域名失败或者接收数据中没有 IP 地址，就使用硬编码的 OpenNIC 服务地址来解析 C2 域名。硬编码的内容和更新前的一样。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-1683266727.png)

样本如果成功解析出一个 C2 域名，就使用该域名，如果解析失败再重新拼接一个 C2 域名进行解析，最多尝试 8 次，如果都不成功就换用 ICANN 类型的 C2 域名。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-16832667271.png)

**5.3**

**ICANN域名获取**

获取 ICANN 域名的方式和获取 OpenNIC 域名的方式相同，先解密包含域名的密文，然后将解密后的字符串进行拼接得到域名。加密 ICANN 域名的算法是xxtea，解密用的密钥是 AE11Fjj43edj2j24e，解密后的内容如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199901-1683266728.png)

按照之前的方法拼接得到 C2 域名，共得到 4 个域名，经过对比，这 4 个域名和更新前保持一致：

```
milfsfors3x.comd
oodleching.com
forwardchinks.com
cookiemonsterboob.com
```

**5.4**

**解析ICANN域名**

解析 ICANN 域名使用的是 7 个公共的 DNS 服务地址，解析时从这 7 个地址随机选择一个，解...