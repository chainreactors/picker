---
title: PatchWork组织新型攻击武器报告-EyeShell武器披露
url: https://www.anquanke.com/post/id/288891
source: 安全客-有思想的安全新媒体
date: 2023-05-27
fetch_date: 2025-10-04T11:38:09.009334
---

# PatchWork组织新型攻击武器报告-EyeShell武器披露

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# PatchWork组织新型攻击武器报告-EyeShell武器披露

阅读量**348661**

|评论**1**

发布时间 : 2023-05-26 11:12:55

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# 1、PatchWork组织描述

Patchwork APT 组织，也称为 Dropping Elephant、Chinastrats、Monsoon、Sarit、Quilted Tiger、APT-C-09 和 ZINC EMERSON，于 2015年12月首次被发现，使用一套定制的攻击工具，针对多名外交官和经济学家发起攻击。这些攻击通常是通过鱼叉式网络钓鱼活动或水坑攻击进行的。该组织被怀疑由一个隶属于南亚某国的威胁行为者运营，主要攻击目标是巴基斯坦、斯里兰卡、尼泊尔，孟加拉国、中国、缅甸、柬埔寨等国。

近2年来知道创宇404-高级威胁情报团队多次提前&即时发现该组织针对国内重点高校、研究院、科研所等相关研究组织机构开展攻击活动，多次成功预警。

# 2、武器基本信息

|  |  |
| --- | --- |
| 样本来源 | 持续追踪 |
| SHA-256 | 6e0db3722abb04be57696d12f4debf078f053d6e4839e621c864c325f20b8ca4 |
| 武器名称 | EyeShell |
| 武器类型 | 后门程序 |
| 针对平台 | Windows |

# 3、武器功能模块图

![]()

# 4、EyeShell武器综述

近期404-高级威胁情报团队在对PatchWork的持续追踪过程中，发现其武器库中出现了一款由.NET开发的精简后门，目标框架为.NET Framework 4，狩猎追踪过程中我们发现该后门与BADNEWS[1]共同出现，故我们有理由猜测该后门用于配合BADNEWS共同使用，该后门使用的命名空间为Eye，为了方便后续追踪及区分，我们根据命名空间将这款后门称之为EyeShell。

【1】BADNEWS为PatchWork组织专用自研木马名称。

## （1）EyeShell功能描述

EyeShell整体来看是一款非常精简的后门程序，推测其版本为v1.0版本，EyeShell按功能模块划分可将整体划分为三个模块，分别如下：

1. **初始化模块**

初始化模块分为两个部分，间隔点为C2是否在线。

**第一部分用于程序初始化**，内容如下：

本次发现的EyeShell创建的互斥体为“fdghsdfgjhh”，互斥体用于确保程序唯一运行，避免发生竞争问题。

C2地址及端口采用数组的方式保存：

char[] C2Address = new char[13]

{

‘1’, ‘7’, ‘2’, ‘.’, ‘8’, ‘1’, ‘.’, ‘6’, ‘1’, ‘.’,

‘2’, ‘2’, ‘4’

};

int[] C2Port = new int[4] { 2, 0, 2, 4 };

由于EyeShell的C2信息使用的是数组保存，进行Connect(string hostname, int port)API调用时会进行一次类型转换，地址在转换string类型时只需要强制转换即可，EyeShell在处理端口时采用的方式是遍历幂运算累加的方式：

C2Port.Select((int t, int i) => t \* Convert.ToInt32(Math.Pow(10.0, pop.Length – i – 1))).Sum()

EyeShell的所有网络交互均采用AES-128加密：

AESKey = {‘q’, ‘w’, ‘e’, ‘r’, ‘1’, ‘2’, ‘3’, ‘4’, ‘a’, ‘s’, ‘d’, ‘f’, ‘5’, ‘6’, ‘7’, ‘8’};

AESIV = {‘7’, ‘3’, ‘9’, ‘1’, ‘8’, ‘4’, ‘2’, ‘6’, ‘5’, ‘7’, ‘8’, ‘9’, ‘5’, ‘1’, ‘2’, ‘3’}

向服务端发送数据的加密方式与服务端下发命令所采用的加密方式相同，采用的处理流程为原始数据（byte[]）—> To Base64 —> To AES-128 —> To Base64(最终发送的数据)。

**第二部分用于交互初始化**

交互初始化需要一个前置条件，当且仅当C2在线时才会进行交互初始化。

交互初始化主要内容为创建cmd.exe进程并创建OutputData Received事件，通过OutputHandler事件委派将标准输出流重新导向TCPStream写入接口，从而达到将标准输出流重定向至服务端操作，EyeShell在完成事件委派后会创建TCPStream Read/Write两个接口分别为后续交互提供支持。

其中Write接口与OutputHandler事件委派中的重定向产生关联。

1. **上线模块**

在初始初始化完成后，EyeShell会尝试进行C2在线检测，直到C2在线后才会进行后续操作否则将持续检测C2是否在线。

如若C2在线EyeShell收集的上线信息分别为UUID、UserName、OSVersion，上线格式如下:

<UUID>+ “\*” +<UserName>+ “\*” +<OSVersion>+”\*1.0″

其中根据经验来看上线信息尾部的硬编码字符\*1.0我们猜测为EyeShell版本号v1.0。

完成上述操作后EyeShell进入交互模块。

1. **交互模块**

交互模块是一个死循环模块，交互开始是通过从TCPStream Read接口读取服务端下发的指令，根据EyeShell的命令控制列表我们可以确定EyeShell支持十三条指令，相关指令及功能如下所述：

“drive”

该指令含义为枚举并向服务端上传当前主机的逻辑卷名称，上传格式如下：

<vol1.Name> +”\*”+ <vol2.Name> +”\*”+ … + <voln.Name>

“fileData”

该指令含义为获取指定文件大小，如果为目录则会获取当前目录其子目录大小。异常则返回“0”。

“FileRec”

该指令含义为获取当前目录其子目录名称。上传格式为：

fo\*l\*d\*er +”\*”+ <folder1> +”\*”+ <folder2> + …

“FileList”

该指令含义为列举当前目录、子目录及目录中文件名称，类似于ls 指令上传格式类似由”\*”分割。

“downFile”

该指令含义为将受害主机中指定的文件上传至服务端，若长传成功服务端返回”Done”。

“upload”

该指令含义为从服务端下载文件保存至受害主机指定路径,成功则返回”asdf”。

“Exec”

该指令含义为执行受害主机中的指定文件,执行成功返回”asdf”,否则返回异常信息。

“Delete”

该指令含义为删除受害主机中的指定文件,执行成功返回”asdf”,否则返回异常信息。

“Rev”

该指令用于执行服务端下发命令,并更改OutputHandler事件委派中的返回状体为开启,此时服务端与客户端建立起交互式Shell。

“RevEnd”

该指令用于关闭交互式Shell,更改OutputHandler事件委派中的返回状体为关闭,此时服务端与客户端关闭交互式Shell。

“ScreenS”

该指令用于获取受害主机当前桌面屏幕截屏。

“UplExe”

该指令有两个操作：

操作一：从服务端下发文件并保存至受害主机%temp%路径下的指定文件名称并立即执行。

操作二：获取当前进程的ID并将该数据保存在%temp%\\ip1.txt文件中。

“Alive”

无操作,使客户端进入等待状态。

## （2）EyeShell细节描述

![]()

网络流加密流程

![]()

网络流解密流程

![]()

AES-128 KEY&IV

![]()

互斥体创建及初始化C2

![]()

初始化Shell并创建事件委托

![]()

事件委托

![]()

创建TcpStream 读写接口

![]()

构建并发送上线信息

![]()

交互入口

![]()

获取文件列表

![]()

获取逻辑卷信息

![]()

文件上传

![]()

获取文件大小

![]()

获取屏幕截图

![]()

文件保存执行及PID获取

![]()

创建指定进程

![]()

删除指定文件

![]()

启动交互式Shell

![]()

获取目录信息

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**知道创宇**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288891](/post/id/288891)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [APT组织](/tag/APT%E7%BB%84%E7%BB%87)
* [攻击武器分析](/tag/%E6%94%BB%E5%87%BB%E6%AD%A6%E5%99%A8%E5%88%86%E6%9E%90)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t013a73ac4f61755c65.png)知道创宇

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013a73ac4f61755c65.png)](/member.html?memberId=133646)

[知道创宇](/member.html?memberId=133646)

知道创宇是一家基于AI和大数据驱动的云安全公司，专注于为政府机构、企事业单位提供全方位的网络安全解决方案。

* 文章
* **48**

* 粉丝
* **40**

### TA的文章

* ##### [狡诈之狐，伪装成flash插件的最新银狐攻击活动分析](/post/id/310759)

  2025-07-31 10:10:15
* ##### [视未成年人为草芥！海内外文生图大模型人脸生成乱象堪忧](/post/id/302063)

  2024-11-21 16:11:52
* ##### [ChatGPT倒数第一！海内外大模型在自杀诱导与谣言辨识上频“触礁”](/post/id/301395)

  2024-11-12 17:42:40
* ##### [13家热门Web大模型内容风险评测，短板竟然隐藏在这里！](/post/id/300792)

  2024-10-12 10:59:43
* ##### [知道创宇发布《海外大模型应对中国核心价值观能力评测报告》（文末获取完整报告）](/post/id/299674)

  2024-08-30 14:37:36

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [（1）EyeShell功能描述](#h2-0)
* [（2）EyeShell细节描述](#h2-1)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)