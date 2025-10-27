---
title: 初识内存取证-volatility与Easy_dump
url: https://www.anquanke.com/post/id/287019
source: 安全客-有思想的安全新媒体
date: 2023-03-09
fetch_date: 2025-10-04T08:59:25.319817
---

# 初识内存取证-volatility与Easy_dump

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

# 初识内存取证-volatility与Easy\_dump

阅读量**346621**

发布时间 : 2023-03-08 14:30:12

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## volatility

Volatility是一款非常强大的内存取证工具,它是由来自全世界的数百位知名安全专家合作开发的一套工具, 可以用于windows,linux,mac osx,android等系统内存取证。Volatility是一款开源内存取证框架，能够对导出的内存镜像进行分析，通过获取内核数据结构，使用插件获取内存的详细情况以及系统的运行状态。

在不同系统下都有不同的软件版本，官网地址：https://www.volatilityfoundation.org/26

## volatility工具的基本使用

### 命令格式

`volatility -f [image] --profile=[profile] [plugin]`

在分析之前，需要先判断当前的镜像信息，分析出是哪个操作系统

`volatility -f xxx.vmem imageinfo`

如果操作系统错误，是无法正确读取内存信息的，知道镜像后，就可以在–profile=中带上对应的操作系统

#### 常用插件

下列命令以windows内存文件举例

#### 查看用户名密码信息

`volatility -f 1.vmem --profile=Win7SP1x64 hashdump`

#### 查看进程

`volatility -f 1.vmem --profile=Win7SP1x64 pslist`

#### 查看服务

`volatility -f 1.vmem --profile=Win7SP1x64 svcscan`

#### 查看浏览器历史记录

`volatility -f 1.vmem --profile=Win7SP1x64 iehistory`

#### 查看网络连接

`volatility -f 1.vmem --profile=Win7SP1x64 netscan`

#### 查看命令行操作

`volatility -f 1.vmem --profile=Win7SP1x64 cmdscan`

#### 查看文件

`volatility -f 1.vmem --profile=Win7SP1x64 filescan`

#### 查看文件内容

`volatility -f 1.vmem --profile=Win7SP1x64 dumpfiles -Q 0xxxxxxxx -D ./`

#### 查看当前展示的notepad内容

`volatility -f 1.vmem --profile=Win7SP1x64 notepad`

#### 提取进程

`volatility -f 1.vmem --profile=Win7SP1x64 memdump -p xxx --dump-dir=./`

#### 屏幕截图

`volatility -f 1.vmem --profile=Win7SP1x64 screenshot --dump-dir=./`

#### 查看注册表配置单元

`volatility -f 1.vmem --profile=Win7SP1x64 hivelist`

#### 查看注册表键名

`volatility -f 1.vmem --profile=Win7SP1x64 hivedump -o 0xfffff8a001032410`

#### 查看注册表键值

`volatility -f 1.vmem --profile=Win7SP1x64 printkey -K "xxxxxxx"`

#### 查看运行程序相关的记录，比如最后一次更新时间，运行过的次数等

`volatility -f 1.vmem --profile=Win7SP1x64 userassist`

#### 最大程序提取信息

`volatility -f 1.vmem --profile=Win7SP1x64 timeliner`

## 电子取证之Easy\_dump(2018护网杯)

### 查看镜像信息

`volatility -f easy_dump.img imageinfo`

查看结果，推测可能是Win7SP1x64的镜像

### 指定镜像进行进程扫描

volatility -f easy\_dump.img –profile=Win7SP1x64 psscan

也可以使用pslist参数

发现存在notepad.exe，查看一下内容。

### 导出进程中内容

volatility -f easy\_dump.img –profile=Win7SP1x64 memdump -p 2616 -D /xxx/xxx/xxx/

其中procdump：是提取进程的可执行文件

memdump：是提取进程在内存中的信息

### 使用strings查找flag信息

strings -e l 2616.dmp | grep “flag”

发现提示是jpg

### 读取jpg文件

volatility -f easy\_dump.img –profile=Win7SP1x64 filescan | grep “jpg”

发现图片phos.jpg

导出图片

查看图片，无法正常打开

使用binwalk查看，发现存在zip文件

### 分离文件

foremost file.None.0xfffffa8008355410.vacb

分离后自动生成output文件夹，查看内容

解压00004372.zip，得到message.img

继续使用binwalk提取文件

得到hint.txt

### 使用脚本进行转换

查看其他大佬说可能是左边，使用脚本进行转换

#脚本文件

import matplotlib.pyplot as plt

import numpy as np

x = []

y = []

with open(‘hint.txt’,’r’) as f:

datas = f.readlines()

for data in datas:

arr = data.split(‘ ‘)

x.append(int(arr[0]))

y.append(int(arr[1]))

plt.plot(x,y,’ks’,ms=1)

plt.show()

扫描二维码得到提示，一个是维吉尼亚加密，秘钥是aeolus。一个是加密文件被删除了，需要恢复。

### 恢复文件

使用testdisk进行恢复

testdisk message.img

红色为需要恢复的文件

使用ls -a查看

使用strings查看

最后一句字符串尝试解密

得到最终结果

### 参考资料

https://www.cnblogs.com/zaqzzz/p/10350989.html

https://blog.csdn.net/weixin\_42742658/article/details/106819187

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287019](/post/id/287019)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Volatility](/tag/Volatility)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41

### 热门推荐

文章目录

* [volatility](#h2-0)
* [volatility工具的基本使用](#h2-1)
  + [命令格式](#h3-2)
* [电子取证之Easy\_dump(2018护网杯)](#h2-3)
  + [查看镜像信息](#h3-4)
  + [指定镜像进行进程扫描](#h3-5)
  + [导出进程中内容](#h3-6)
  + [使用strings查找flag信息](#h3-7)
  + [读取jpg文件](#h3-8)
  + [分离文件](#h3-9)
  + [使用脚本进行转换](#h3-10)
  + [恢复文件](#h3-11)
  + [参考资料](#h3-12)

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