---
title: SIM Jacker攻击分析
url: https://www.secpulse.com/archives/205634.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:14.491355
---

# SIM Jacker攻击分析

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

# SIM Jacker攻击分析

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

11,062

# 简介：

2019年9月12日，AdaptiveMobile Security公布了一种针对SIM卡S@TBrowser的远程攻击方式：Simjacker。攻击者使用普通手机发送特殊构造的短信即可远程定位目标，危害较大。sim卡的使用在手机上的使用非常普遍，所以一旦SIM卡上出现什么问题就会造成非常大的影响。在19年的报告纰漏中，在全球估算共有10亿设备的sim卡容易遭受SIM Jacker攻击，这篇也是比较浅显的对整个攻击进行分析。

# 1.一点点背景

在了解整个攻击前需要对整体的一个框架有所了解，现在我们就先来了解一下短信是如何去发送的。GSM的中文就是全球移动通信系统，是由欧洲电信标准组织ETSI 制定的一种数字制式的蜂窝移动通信系统。当初开发 GSM目的是让全球各地可以共同使用一个移动电话网络标准，让用户使用一部手机就能行遍全球，因此GSM 还有一个很接地气的俗称------全球通。

GSM与它以前的标准相比较而言最大的不同是它的信令和语音信道都是数字式的，因此GSM 被看作是第二代（2G）移动电话系统。 短信（Short MessageService，SMS）是基于 GSM（全球移动通信系统）网络标准的通信服务之一，SMS允许通过 GSM 网络发送和接收文本消息。现在来看看整个短信的发送流程。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659385.png)

这里面中最主要涉及到了三个很重要的主体：发送者，短信中心，接收者。也就是我们的短信必须经过短信中心的转发才能到达接收者的SIM卡上。这里面也涉及到了很多基站的不同功能，比较完整的发送详细的可以看这个<https://zhuanlan.zhihu.com/p/41439805>。

以下是具体的步骤：

1. 发送者编辑短信，通过无线信号（SIM）将消息内容发送到基站
2. 基站收到消息内容经过一系列网元处理将其转发到运营商短信服务中心
3. 运营商短信服务中心经过一系列网元处理将数据转发到接收者附近的基站
4. 接收者附近的基站将短信内容发送到接收者

# 2.PDU模式短信的格式

GSM收发短消息又分三种模式：BLOCK 模式、TEXT 模式和PDU 模式。BLOCK模式现在用的很少了；TEXT 模式则只能发送ASCII码，它不能发送中文的[UNICODE](https://so.csdn.net/so/search?q=UNICODE&spm=1001.2101.3001.7020)码（确切地讲，从技术上来说是可以用于发送中文短消息的，但是国内的手机基本上不支持）；而PDU模式开发起来则较为复杂，它需要编写专门的函数来将文本转换为PDU格式，但PDU模式被所有手机支持，可以使用任何字符集，它也是手机默认的编码方式。接下来我们来主要了解在这个模式下短信的格式。

以一个现实里的例子去讲解这个，这些是16进制的表示

0891683108200805F011190D91683188902848F40008FF108FD9662F4E0067616D4B8BD577ED4FE1

---

短信中心地址字段 0891683108200805F0

---

FirstOctet字段 11

消息参考值 19

接收者号码字段 0D91683188902848F4

协议标识 00

编码方法 08

有效期 FF

用户数据长度 F10

## 用户数据 8F......E1

## 短信中心地址字段

这个就是短信中心的地址，一般SIM卡都已经写好了，所以这里还有一个很常见的写法就是00，表示默认。08表示字节长度，9168表示的就是+86,表示的是在中国的号码，然后后面跟着号码。

## FirstOctet字段

这个字段非常重要，涉及到许多设置，每一bit都有用处，先将十六进制下的11换成二进制的00010001，

我们从最低位开始，从右往左看

1. 首先我们看的就是01（对这俩位得连在一起看），这俩位表示的是这个短信的类型，最常见的有俩种SMS-SUBMIT、SMS-DELIVER。SMS-SUBMIT表示移动终端设备发送到短信中心，SMS-DELIVER表示短信中心发送到移动终端设备，对应的分别是01和00，这里是01，表示就是这是一条发送者的短信
2. 接下来就是第2位0，表示是否要接收重复的消息
3. 然后是10，这里表示了短信有效期的形式，10表示使用的相对时间，这也是常用的设置
4. 然后就是第5位啦，这是一个非常有意思的参数，返回短信状态报告。用通俗的话讲就是告诉发送者接收者是否已经接收到了短信，这里面所蕴含的信息在USENIX23上被用来实现了定位
5. 然后第6位就是用户数据头标示，当它等于0的时候就是表明这是一个短信消息，如果是一个OTA消息呢，比如SIM

   > jacker,就得设置为1
6. 第7位是设置回复路径，每个SIM卡都设置了一个短信中心的号码，如果设置为0，那么接收者接回复短信时用的也是发送者的短信中心；如果这个是1，那么接收者将使用自己的短信中心

用一下别人的表，大家可以来对照一下：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659387.png)

## 消息参考值

这个值有点像ID,范围是0~255，如果一个短信被分成了多片，短信中心可以依据这个值将其进行组合

## 目标地址

这个同短信中心的设置，不过这里的0D表示的数字的长度，表示有几个数字

## 协议标识符

它是表明一条短信的用途或协议，它不仅用于传统的短信传输，也用于传输其他类型的信息，如传真、电子邮件或无线应用协议（WAP）消息。00表示的没有什么特殊的协议，静默短信的设置也涉及到这个，需要将这个修改成40，这个静默短信发送给接收者是完全没有任何提示的

## 数据编码方案

指明这个pdu的编码方式是什么，PDU收发短信有三种编码可用：7-bit、8-bit和UCS2编码，00为7Bit编码，04是8bit,08是UCS2编码，到后面的可以表达的内容更多，7bit简单的英文到UCS2编码可以发送中文。

帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：dctintin，备注 “安全脉搏” 获取！】

① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

## 有效期

这里根据前面常见的设置就是相对有效期，FF表示最大30天，00最小5分钟

## 用户数据长度

后面跟着的数据的长度

# 3.一点点实验

了解到了一个PDU模型，短信的格式，一个标准的pdu可以直接用在线的网站进行生成，<http://www.sendsms.cn/pdu/>，大部分格式限定后，就可以修改部分设置

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659388.png)

现在pdu格式有了，该如何发呢，这种最简单的情况就是去网上买个GSM模块，插上一张可以收发短信的SIM卡就可以直接用了，但考虑到大家只是简单了解一下，也不一定非得买个专门的设备，所以我们这里使用一个大家肯定都有的设备的，一台root过的手机。我使用的是魅族m3note，比较好root，大家也可以试试。

首先先接入adb进行调试，已经确定获得了root权限

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659389.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659390.png)

因为安卓为linux系统修改的，所以一切皆文件，插入的sim卡也会被映射成一个文件，可以进行操作

一个示例如下

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659391.png)

现在我们需要找到插入SIM卡之后的对应的文件，最简单的方式就是对比插入前后的对比找到

查看/proc/devices ,不过并没有变化,这里判断应该是准备着有接口，已经存在。

使用demsg,但是因为数据线处于连接状态充电，会有很多杂乱信息，而且魅族上使用的也不是smd\* ，这里也可以尝试一个一个去找，但也会有很多问题。

这里找到一个比较好的办法，查看设备的radio日志

logcat -b radio | grep dev

先挂起日志监控，在插入SIM卡后，会输出大量信号，这里就成功定位到了SIM卡所映射的设备

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659392.png)

因为每个设备对换行的接收不一样，所以建议几种方式一起去试，一个例子如下：

echo -e "AT+COPS?" > /dev/pts/4\echo -e "AT+COPS?\r" > /dev/pts/4\echo -e "AT+COPS?\r\n" > /dev/pts/4\echo -e "AT+COPS?\n" > /dev/pts/4\echo -e "AT+COPS?;" > /dev/pts/4\echo -e "AT+COPS?;\r" > /dev/pts/4\echo -e "AT+COPS?;\r\n" > /dev/pts/4\echo -e "AT+COPS?;\n" > /dev/pts/4

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659393.png)

之后逐一筛选，选择合适的结尾，这里是\n

然后发送一条短信试试

echo -e "AT+CMGF=0\n" > /dev/pts/4 # PDU模式\echo -e "AT+CMGS=20\n" > /dev/pts/4 # 字符长度\echo -e "0031000D9168xxxxxxxxxxxx00000005E8329BFD0632\n" >/dev/pts/4

之后就可以在接收者那收到短信，32 对应ctrl\^z,是发完短信的结束符，不算入总长度

# 4.SIM Jacker

了解完前面三个部分，大家有了一些基本的了解，接下来我们就来看看SIMJacker这个攻击，一些具体的影响后果啥的就不去细究了，主要还是了解背后的一些原理。

## （1）OTA消息

OTA 消息，也称为二进制消息，是包含一组(U)SIM 应用程序工具包(USAT)命令的特定 APDU 消息，这些消息针对 SIM卡内的特定应用程序，而这些应用程序又执行消息本身提供的USAT命令，这些命令包括：设置呼叫、发送短信、更新SIM 信息、编辑 SIM 文件等。

OTA 消息通常设计为从运营商发送到用户，服务提供商可以引入新的 SIM服务、修改 SIM的内容、执行软件更新、配置设置，甚至更新移动设备的加密密钥。

正是因为这一特性的存在导致了SIMJacker的发生，也就是OTA消息也可以由一个用户发送，而非短信中心。

SIM Jacker发生的条件主要有三个：

1. 短信中心可以接受并转发PDU消息
2. 接收者能够解析SIM应用工具包命令的PDU消息
3. SIM上部署了S@T浏览器技术，并且设置了"不应用任何安全措施"的最低安全级别

其他的一些条件，比如主动 UICC 命令等这些都是默认开启的，这里就不在提及。

让我在回到PDU模式短信那块，在FirstOctet字段中有一位可以将普通的用户数据，变成对SIM卡特定应用的程序的执行命令，就是要将第6位的用户数据头标示设置成1。也有很多是SIMjacker的攻击中的PDU是0041开头的。

先用一张图开始：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411151659394.png)

前面的部分和之前一样，主要来解释一下后面的UD部分：

1. 先开始的是用户数据头，包含了俩部分

   > 一个是是用户数据头的字节长度，另一个是用户数据头的设置，可以设置是否包含安全头。
2. 命令包包含有关消息安全性、消息发往哪个应用程序以及我们想要执行的实际命令是什么等非常重要的信息。
3. 命令包长度是整个命令包的字节长度：
4. 命令头长度是命令头的字节长度：
5. 命令头由6 个不同的值组成：

安全参数指示符（SPI）指定是否对消息应用任何安全性，在SIMjacker中要将SPI设置如下：SPI = 0x0000

加密密...