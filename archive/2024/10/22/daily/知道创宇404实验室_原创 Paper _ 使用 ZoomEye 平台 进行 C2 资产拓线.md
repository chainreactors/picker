---
title: 原创 Paper | 使用 ZoomEye 平台 进行 C2 资产拓线
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988895&idx=1&sn=51fcf8297fdf1dbe24ca59dc04d64c39&chksm=8079a36db70e2a7bdeb078d3e8f6a9fe162e91141fa229d47348891ec85ffeb09bf211f0e20b&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-10-22
fetch_date: 2025-10-06T18:52:10.091746
---

# 原创 Paper | 使用 ZoomEye 平台 进行 C2 资产拓线

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8gI3ViakgSS5PO2UG67b1Ks2iayicRGYlSI8YftrFWR1IsONRaOJeYe1pQ/0?wx_fmt=jpeg)

# 原创 Paper | 使用 ZoomEye 平台 进行 C2 资产拓线

原创

404实验室

知道创宇404实验室

**作者：******知道创宇404实验室****

**时间：**2024年10月21日****

**1 摘要**

参考资料

本文基于推特社交平台上一则C2的IP地址及其相关文件信息，以此作为线索，使用ZoomEye网络空间搜索引擎 [1] 进行C2资产拓线，发现更多属于该黑客组织的C2网络资产；并针对这些C2服务器上的木马程序进行分析，获取黑客组织的惯用攻击手法和独有特征。

**2 概述**

参考资料

2024年9月8日，推特社交平台上有一位安全研究员发布了一则C2的IP地址及其相关文件信息，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8M2pTAd3gwfZLHic1kFAWS68Xl0UJHEaNfrpJRIu6Pxib4YjRrib8vLK1A/640?wx_fmt=png&from=appmsg)

图 1 推特社交平台线索信息示意图

我们基于该C2的IP线索89.197.154.116，使用ZoomEye平台，来进行C2资产拓线。

**3 摸底C2服务器**

参考资料

### **3.1 开放端口**

我们首先使用ZoomEye平台搜索该C2 IP地址89.197.154.116（下文简称“IP地址A”）的信息，如下图所示，发现“IP地址A”位于英国伦敦，开放两个端口：80和3000，两个端口均为HTTP服务。

*ZoomEye平台搜索语句为 ip:89.197.154.116*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8JKiadCc7IdStfbQY2Xhuia3SeQGicF09sicVMGdbsSbiaT7F9lKWnY2hkYA/640?wx_fmt=jpeg&from=appmsg)

图 2 ZoomEye搜索结果示意图

我们访问“IP地址A”80端口的HTTP服务，发现“IP地址A”的服务器上存放了多个文件。图3是2024年9月10日访问的页面截图，图4是2024年9月13日访问的页面截图。对比两张示意图，发现该黑客组织在2024年9月12日更新了5个文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8vbsC3Oliaa0EliaaHJrPcT0Q6TLTeaicmZEhibutI5c1IjkWocI5SDtfnQ/640?wx_fmt=png&from=appmsg)

图 3 2024年9月10日访问示意图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8bx21mwP3v7REGkQdbpMJwwjUVMicE4n4piadSGyjRhf1Tg3azpiaBVOEQ/640?wx_fmt=png&from=appmsg)

图 4 2024年9月13日访问示意图

### **3.2文件分析**

我们对服务器上的文件进行网络行为分析，发现这些文件多为C2（CobaltStrike）木马文件，其中大部分在近期被人提交至互联网恶意软件分析平台进行过分析。结合上文中黑客组织在2024年9月12日更新5个文件的信息，可以推断出黑客攻击者在近期时间内处于活跃的攻击状态。

此外，还发现“IP地址A”服务器上C2通信端口为7810端口。

经过对服务器上的文件hash值进行比对，发现文件“lazagne.exe”是一个GitHub开源应用程序，用于检索存储在本地计算机上的密码；文件“AvosLocker.exe”是2021年新兴勒索组织AvosLocker所使用的勒索软件，根据国家关键基础设施安全应急响应中心在2021年09月17日的《近期活跃的四个新型勒索软件组织分析》报告 [2] 来看，该组织于2021年6月底开始活动，在2021年7月4日首次被发现。

2024年9月12日，“IP地址A”服务器新增文件中有一个名为“Meeting.exe”的文件，经过分析发现该文件运行后会释放icon.exe、word.png、word\_favicon.ico三个文件，其中icon.exe运行后会与“IP地址A”服务器自身建立连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8woEl1nppMBku8WjMRUsK3DZYvu6cYhE5AKL3MhGU0viaWHbz5ia8nJkg/640?wx_fmt=png&from=appmsg)

图 5 “Meeting.exe”文件执行路径示意图

### **3.3结论**

基于以上信息，我们可以猜测：

* “IP地址A”服务器资产疑似属于AvosLocker勒索组织，攻击者使用C2控制端控制失陷主机，通过收集密码等方式进一步横向拓展来传播勒索程序
* 截止2024年9月12日，“IP地址A”服务器资产仍处于使用状态，该组织仍在活跃

**4 拓线C2资产**

参考资料

###

### **4.1 基于资产特征拓线**

通过ZoomEye平台查看“IP地址A”的资产详情，如下图所示，主机名为“89-197-154-116.virtual1.co.uk”，形式为“*-*-*-*.virtual1.co.uk”，存在一定的特征；自治系统编号为“AS47474”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8JxEAQibnWiaNQxxmka4AF6tTUH0rRoFv6Uq9mNCtPls9IM7Z9picicrVRQ/640?wx_fmt=jpeg&from=appmsg)

图 6 ZoomEye平台IP详情示意图

我们利用主机名的特征，结合其80端口页面标题“Index of /”的特征（参见图3），通过如下搜索语句在ZoomEye上平台进行查询。

*hostname:".virtual1.co.uk" +title:"Index of /"*

查询获取17条结果，结果IP地址均位于英国，详细信息如下表所示。我们针对这17条结果依次排查，并对2个IP地址“89.197.154.115”和“193.117.208.148”进行详细描述。

表 1 拓线结果列表

| IP地址 | 端口 | 测绘时间 | 存活状态 |
| --- | --- | --- | --- |
| 193.117.208.154 | 80 | 2021-05-28T14:09:48 | 存活 |
| 89.197.85.226 | 8080 | 2021-09-18T19:45:15 |  |
| 89.197.199.219 | 443 | 2023-02-14T18:25:33 |  |
| 193.117.232.154 | 80 | 2022-03-25T05:52:54 |  |
| 193.117.208.149 | 80 | 2022-12-16T05:20:27 |  |
| 193.115.235.251 | 80 | 2024-07-20T22:49:12 |  |
| 193.115.218.2 | 443 | 2024-07-17T02:30:56 | 存活 |
| 89.197.94.11 | 4443 | 2024-07-16T05:34:49 |  |
| 193.117.209.43 | 10443 | 2024-07-01T22:00:34 |  |
| 193.117.238.38 | 443 | 2023-06-20T21:11:26 |  |
| 193.117.208.148 | 80 | 2024-04-16T04:07:58 |  |
| 193.117.208.101 | 80 | 2024-09-10T18:46:37 | 存活 |
| 193.115.235.251 | 443 | 2024-07-17T02:30:34 | 存活 |
| 193.117.210.47 | 10443 | 2023-07-23T00:40:39 |  |
| 89.197.154.116 | 80 | 2024-07-20T14:42:53 | 存活 |
| 89.197.198.150 | 443 | 2024-04-19T14:01:23 |  |
| 89.197.154.115 | 80 | 2024-07-20T14:43:05 | 存活 |

### **4.2 IP地址89.197.154.115**

首先排查与“IP地址A”位于同一个C段的相邻IP地址“89.197.154.115”（下文简称“IP地址B”）。

根据zoomeye平台测绘数据来看，“IP地址B”开放了80端口，提供HTTP服务。我们访问“IP地址B”80端口的HTTP服务，如下图所示，发现“IP地址B”服务器与“IP地址A”类似，存放着多个文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8WlJSV1weDm2jzzFKABbDib5RwvMA4hriaG7baHc4CEQFgeqDiaZIVLyww/640?wx_fmt=png&from=appmsg)

图 8 IP地址80端口访问示意图

这些文件时间的最早日期为2024年7月11日，推测“IP地址B”服务器在2024年7月11日之前就已经被黑客组织所使用。

我们对各个文件进行分析，发现“IP地址B”服务器C2通信端口为7700，文件名与木马运行方式与“IP地址A”高度类似，且两者都使用“Debian”操作系统和“Apache httd”服务软件。

针对文件“UpdaterLOC.dll”文件的分析中，发现该文件中绑定的C2服务器回连地址“192.168.180.11”是内网地址。回连地址为内网地址的原因，大概率是攻击者为定向攻击活动做准备，测试C2木马能否通过免杀正常回连上线；也不排除是为攻击目标内部网络横向拓展，但受网络限制因素只能回连上线至内网IP地址主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8SzJAbaY3mibVLWluuCCTJicBicc2IUSoSegiaZT1Q5yhhEaJqKqNXSm2EQ/640?wx_fmt=png&from=appmsg)

图 9 文件反编译信息示意图

其中有一个名为“meeting.sfx.exe”的文件，与“IP地址A”服务器上“Meeting.exe”的文件命名相似。经过分析发现该文件运行后会释放word.png、Meeting.exe两个文件，其中Meeting.exe运行后会与“IP地址B”服务器自身建立连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8ew6uFBnbicdVAl8DEf4pvWahI4RyEJOBmUiaL2Xojy9WvlYNYvHob9Ow/640?wx_fmt=png&from=appmsg)

图 10 文件执行路径示意图

实际运行“meeting.sfx.exe”的文件，发现其伪装成一个安装包，当用户双击运行之后并不会立即上线到C2，而是在用户点击“Install”按钮之后再释放用于上线C2的“Meeting.exe”，同时还会打开一个正常的png图片用于迷惑攻击目标，如下方图12所示。

与章节3.2中的分析进行对比，“IP地址A”服务器的“Meeting.exe”文件具有极其类似的行为，区别在于释放的迷惑文件不一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8Jxbyhfwm63RZevHic8Fiasic8excG5w5MiandtnTyiaib0fMaF6uFRkGEzrg/640?wx_fmt=png&from=appmsg)

图 11 文件点击后伪装成安装包示意图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8FhrR1fceJReHV0ib4ibry5XN8RicO9PISnV9pHY6Yu7A2HpGSS0cQ95Sg/640?wx_fmt=png&from=appmsg)

图 12 打开正常png图片迷惑用户的示意图

综合以上分析结果，我们推断“IP地址B”和“IP地址A”归属于同一个黑客组织。

### **4.3 IP地址193.117.208.148**

IP地址193.117.208.148 （下文简称“IP地址C”）的端口服务，当前已经无法访问，但是通过ZoomEye平台历史测绘数据，可以看到该IP服务器上曾存在过一些文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8Ou6h9jKCFibfBjmLNWMXP8wiaLz7eDQPibmoAg2dhc7N8fu2cvYQAPO1w/640?wx_fmt=png&from=appmsg)

图 13 ZoomEye平台搜索结果示意图

文件列表:

Journal.exe 2024-04-12 15:37 321k

Organiser.zip 2024-04-08 20:07 2.4k

Session.exe 2024-04-08 15:54 19k

这些文件的命名与“IP地址A”、“IP地址B”服务器文件命名非常类似，同样是使用“Debian”操作系统和“Apache httd”服务软件。

鉴于“IP地址C”的ASN、运营商、主机名等信息与“IP地址A”、“IP地址B”都保持一致，因此判断“IP地址C”也曾经归属于同一个黑客组织，目前已经被下线不再使用。

### **4.4 基于ASN编号二次拓线**

介于目前已获得的IOC资产具有很强的地域性，于是将ASN作为特征再次进行C2资产拓线，通过如下搜索语句在ZoomEye上平台进行查询。

*asn:47474 +title:"Index of /" +"HTTP/1.1 200 OK"*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8Z7ibibgPW7Y1vfRUUeibib9xicL4ibfThZ3nDvHxzftViaLiaofXeCmpLJtoMg/640?wx_fmt=jpeg&from=appmsg)

图 14 ZoomEye平台搜索示意图

查询获取26条结果，结果IP地址均位于英国。我们逐个对这些IP地址进行精细化检索排查，筛选出与C2相关的IP地址，信息如下表所示。我们针对这些结果依次排查，并对IP地址 “193.117.208.101”进行详细描述。

表 2 拓线结果列表

| IP地址 | C2通信端口 |
| --- | --- |
| IP地址A 89.197.154.116 | 7810 |
| IP地址B 89.197.154.115 | 7700 |
| IP地址C 193.117.208.148 | 7800 |
| 193.117.208.101 | 7777 |
| 193.117.208.106 | 7100 |
| 193.117.208.107 | 7200 |

### **4.5 IP地址193.117.208.101**

IP地址193.117.208.101（下文简称“IP地址D”）服务器上的木马文件命名与“IP地址A”、“IP地址B”、“IP地址C”的风格不同，但是在其服务器上发现了一个文件“Cloudshare.vbs”，该文件与“IP地址A”服务器上的文件高度相似。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8SPOHs5vUn60JhS8rh67F2xlnpDmKaHib8uh07NiaLOkn5BicX8LibL1dOQ/640?wx_fmt=png&from=appmsg)

图 15 IP地址80端口访问示意图

“IP地址D”服务器上文件“Cloudshare.vbs”与“IP地址A”服务器上文件“Macro.vbs”进行对比可以发现，两个文件除了混淆变量不同，其他内容完全一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx829uhUDO6QZwHDj5lrVXxg6jooLLN3Z7d3ibiabwicroxDSibwg2RSqg5dw/640?wx_fmt=png&from=appmsg)

图 16 文件内容对比示意图

通过沙箱可以直观查看到两个程序的执行路径，首先释放文件“wscript.exe”文件，然后再次释放一个随机名称的exe文件，C2回连至自身服务器。两个文件的行为近乎一致。

“IP地址A”服务器上文件“Macro.vbs”的执行路径如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8NKYjMLLn8KWuhPsxBRexwUKlID73X6clJPpRia2mYooOW9KuWo4Pz9Q/640?wx_fmt=png&from=appmsg)

图 17 文件执行路径示意图

“IP地址D”服务器上文件“Cloudshare.vbs” 的执行路径如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dwZTx0Cox7UBOic8XmzTx8e8eAIltZQT...