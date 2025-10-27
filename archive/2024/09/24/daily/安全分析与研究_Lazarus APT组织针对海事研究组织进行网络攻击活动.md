---
title: Lazarus APT组织针对海事研究组织进行网络攻击活动
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488915&idx=1&sn=dadd7fdc8ddb2d51d886522ddf1ad4f9&chksm=902fbabba75833ad7a5cb5c3ed6fd79596936488a64a0010bb6cf664ec594307a57c1e4e3fd0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-09-24
fetch_date: 2025-10-06T18:27:56.084999
---

# Lazarus APT组织针对海事研究组织进行网络攻击活动

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdVK5z3SJbQldC8ct9oN6m2efU970I1GDrLDcVsJrpIcnEURfB0VzH2w/0?wx_fmt=jpeg)

# Lazarus APT组织针对海事研究组织进行网络攻击活动

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/13901

先知社区 作者：熊猫正正

前不久，美国总统拜登签署加强海事网络安全的行政命令，该行政命令增强了美国土安全部直接应对海上网络安全威胁的权力，包括通过网络安全标准确保美国港口网络和系统的安全，旨在通过制定加强该领域网络防御的新要求来改善海事安全，同时扩大美国海岸警卫队应对网络安全事件的权限，明确赋予海岸警卫队七项权利。

近日，国外安全研究人员曝光了一例朝鲜Lazarus APT组织通过供应链攻击其他国家国防部门潜艇开发计划的研究材料，笔者跟踪分析了该此攻击活动，并详细分析了此次攻击活动中下载使用的攻击武器NukeSped恶意软件。

攻击活动

Lazarus APT组织通过对海事研究组织的网站的维护和维修供应商进行渗透测试，通过补丁管理系统PMS下发安装NukeSped恶意软件进行商业机密窃密活动，国外安全研究人员对该攻击活动进行了溯源分析，笔者根据国外研究人员提供的相关信息对该攻击活动进行了简单的还原。

第一步：Lazarus APT组织通过渗透测试网站供应商，窃取的SSH密钥访问目标Web服务器。

第二步：进入Web网络服务器后，Lazarus APT组织使用curl从C2服务器检索下载Ngrok工具和使用Base64编码的Python下载器脚本。

第三步：利用SSH在整个网络中进行横向移动，并使用TCP Dump收集网络数据并窃取员工的帐户登录凭据信息。

第四步：Lazarus APT通过窃取到的员工帐户登录凭据访问安全经理邮箱，熟悉了解补丁管理系统PMS，然后通过PMS服务提供商请求部署新补丁，安装NukeSped恶意软件进行商业机密窃密活动。

整个攻击活动流程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdiaYb6yxsk9yNVHIoSbgiceVickb91icUliamntoPKdj4X8J7ibvNic9aCS7Bw/640?wx_fmt=png)

样本分析

1.样本使用如下异或算法，解密样本中的加密字符串，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdrC2094cDwAEeKwX37pebz8R8s614KhsXbf8CgiaKaG6x0w0ib9eF8LQg/640?wx_fmt=png)

2.通过LoadLibraryA加载所需要的解密出来的DLL模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdclcO93tMicObsu7G0RAgathugA36u6KhCFErOeqCHpL2r9nV3qBWicYg/640?wx_fmt=png)

3.调用WSAStartup初始化网络请求，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQd3Nl8LPVicdkYIJ77hiaDCYw2IKHRjjv8ibcBq64ExPBuLHtLfgZaeb9UA/640?wx_fmt=png)

4.获取黑客远程服务器C2地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdcbrYXEKdIz3ruelEjxzkGZuDej8Mcr1fxgibcKVOzNK1uuPgOLpfHLQ/640?wx_fmt=png)

5.计算拼接远程服务器请求URL连接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdYJfYCzTNf5IzvU1mgtUMBmcnLbmqSr0VcLc2Ar3yWibuCAdksFPLKyQ/640?wx_fmt=png)

6.添加HTTP请求标头，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdhpstcib6u0ZCP4Kwu7RqQRxOjhBNqOR8LKxrlhChwkGaqJQHtGQYPyw/640?wx_fmt=png)

添加的HTTP标头列表信息：

Cache-Control: no-cache

Accept: \*/\*

Content-Type: application/x-www-form-urlencoded

Content-Length: 41

7.通过URL链接向黑客远程服器发送HTTP请求，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdK1B0Btab0h0JutO3iaXkbUia3og8riax5ulbQjWknx3pqHOricqU1qlhgg/640?wx_fmt=png)

8.将请求数据写入HTTP服务器，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQddLPn3QEHW9o5nuxc0fhxoIIBHO0IJQx3WOjUXxicp9LZuFNicibiaia6qCw/640?wx_fmt=png)

9.获取HTTP请求响应状态，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdWPO6uiazibFVAUoFpJSjGgt3UF0qWeOc87f0ApzPticewcd9iaxJhgBib7g/640?wx_fmt=png)

10.获取服务器资源，返回服务器数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdA31XLVn1WGRzl2P1beicc24hftwfniaohM8Qj79ic8IlHEc5FgEjCm65w/640?wx_fmt=png)

11.获取相关信息，向黑客服务器发送HTTP数据请求命令，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdoS3hTNBviafo6vxuH89YMNYN1ibzr7mBFxhrU48IYsKB4uFPibwckJr0Q/640?wx_fmt=png)

12.通过不同的返回命令，执行不同的操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdo0fOa6Tr5t5pXibKxBNYDMccJJ0icTIebFF3h8cuAFW0SBfaaY4qkJZQ/640?wx_fmt=png)

执行文件的上传、下载、读写操作，以及进程相关操作等，与此前Lazarus APT组织攻击活动中使用的FallChill恶意软件非常相似。

关联分析

查询黑客服务器C2域名connection.lockscreen.kro.kr，显示为可疑域名，同时关联到上面的NukeSped恶意软件样本与该域名通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdqGwPjCN1M30rFiaickMaAsDBtMROciaJ3eD14BPB4gABAiaD1PE0a4gOAg/640?wx_fmt=png)

关联到的NukeSped样本就是上面详细分析的攻击样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdfbicCDWZbvKHyniay6wquiaiap4t2I45uBvKkfNHVW5CaW02K0uKdKj2ng/640?wx_fmt=png)

2018年，Lazarus APT组织针对全球各地的银行以及其他金融公司进行攻击活动，通过建立一些虚假的合法网站，上传一些带有木马功能的交易应用软件，借助邮件传播到目标公司内部，受害者下载安装这些第三方应用软件，感染FallChill恶意软件，该攻击活动被称为Operation AppleJeus。

2019年该组织利用NukeSped恶意软件进行攻击活动，NukeSped的主要功能结构和此前Lazarus APT组织的另一款远控工具FallChill相似。

此次攻击活动Lazarus APT组织同样使用了NukeSped恶意软件进行攻击，同时使用的域名URL等特征与此前攻击活动相类似，所以将此次攻击活动归因到Lazarus APT组织。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWKu9tlbicWEgqyp7kqF7hQdFm0c2h2kXRw9HbdtbBpl4KmXPElo05uo8ias2Bdo4jUQ3CVpx00zNSg/640?wx_fmt=png)

总结结尾

APT是全球企业面临的最大的安全威胁之一，需要安全厂商密切关注，未来APT组织还会持续不断的发起网络攻击活动，同时也会持续更新自己的攻击武器，开发新的恶意软件变种，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源与应急响应的难度，安全研究人员需要不断提升自己的安全分析能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过