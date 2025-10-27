---
title: 针对SugarGh0st组织最新攻击样本的分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488185&idx=1&sn=b6775bf151fe5b946cd7c801640f159d&chksm=902fbd91a75834871e975a71634c2a7de8b656c26aee1c304cfa2844073f94e806f13346012e&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-05-09
fetch_date: 2025-10-06T17:16:46.883192
---

# 针对SugarGh0st组织最新攻击样本的分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE5LwzWXbZTpz2bLRics9s6MvnuuhlA3JO8HoUubU7mCjXpibwiawL0aSpQ/0?wx_fmt=jpeg)

# 针对SugarGh0st组织最新攻击样本的分析

原创

熊猫正正

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/13745

先知社区 作者：熊猫正正

2023年11月份Cisco Talos发现了一起针对乌兹别克斯坦外交部和韩国用户的攻击活动，攻击活动使用了一种新型的RAT恶意软件SugarGh0st，SugarGh0st是Gh0st RAT的最新的变种之一。

2023年12月份哈萨克斯坦国家技术服务中心发现SugarGh0st组织针对哈萨克斯坦进行大规模网络钓鱼的攻击活动，该攻击活动使用了SugarGh0st在2023年12月更新的最新攻击样本。

对比2023年11月SugarGh0st黑客组织的攻击样本，2023年12月的攻击样本主要在免杀方面进行了更新，加载脚本变成了VBS脚本，利用Windows登录自启动来自动加载执行DLL恶意模块，同时增加了相应的免杀技术，对DLL文件进行增肥免杀，加壳等技术手段以逃避安全软件的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEFJmZa9Q4sTIkLKOMwNQfK1iccK3aXG4oozxJuBWFBdgKd4tLZRr3W9g/640?wx_fmt=png)

笔者从vx-underground下载到该组织最新的攻击样本，并针对SugarGh0st组织最新的攻击样本进行了相关的分析。

样本分析

1.钓鱼压缩包自解压之后，会在相应的目录生成几个恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEzAKjO2WfawXH4tFjLLF78uolTcySaYodTYiaM80rPL7XMCvkJlxvLCw/640?wx_fmt=png)

2.自解压之后会调用VBS脚本，VBS脚本会注册恶意DLL模块为Windows登录自启动脚本来建立持久性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEtqZqxTesDTfwtYGMPicscJmpoKR1aw27FcM7vYafuwD90yn51VHKOlQ/640?wx_fmt=png)

该攻击技术曾被多个APT组织使用，相关ATT&CK实例与APT攻击组织，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEekUp4p342C9HNC3SwxlmyyBf0smicIbEyEHgs6ic26PPKiauT8wdb8vEg/640?wx_fmt=png)

3.加载的恶意DLL模块update.dll有两百多M，并使用VMP加壳处理，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE3ibGHgwbBk5qg4FaZBZZicynzCgNsw2nIC8wnNr397scmjpCH19hiba5g/640?wx_fmt=png)

4.VMP入口点代码特征，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEz7M90mUl8WgHlNyH34HT7MaOP71Qic2fLibNbLW02PdXWAWAE2lXuHHA/640?wx_fmt=png)

5.动态调试，脱壳之后，到达恶意DLL模块的入口点处，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE4JPv9qROobkoxBe0nBYiakNDEsRYWWpfBYuHTkT9C5mb0sMsKqCNcog/640?wx_fmt=png)

6.读取Temp目录下的authz.lib文件内容，并在内存中解密，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySECBNF0B8U3PWl1GbWJL7ibvAhaficibRDWkKfSsoicPvUcwY0CxbN37Shcw/640?wx_fmt=png)

7.动态调试，读取authz.lib文件内容到内存，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEiacTGO229pMRYFMsqFicLTsO2qIRwtekV1JibR0nW9wGfGH1pq6Rl0Nlg/640?wx_fmt=png)

8.异或解密文件内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEJZapcnFIrAnBrbquRolVoQzMd1p7Acvl1OicWlTYSZpFsywtn0S0WZw/640?wx_fmt=png)

9.解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEdwAJKslCcOjVeJglqRvLys939ibUPRyomuKib2SUk2XjzRPFvup5H7Pw/640?wx_fmt=png)

10.最后跳转到解密的shellcode代码执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE25FWcfFbcyk7Q6TdfeBBld2GF4rg8T3vKUFHbaAnbvF5nE8F0icqTicQ/640?wx_fmt=png)

11.shellcode获取关键函数地址，然后调用VirtualAlloc函数分配内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEqzPW7Dze9xJhwiaSArJXpialAWYxkCICefwOr9ydGTDBOSSF3ibNRicX9w/640?wx_fmt=png)

12.解密出payload数据到内存中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE6PvPxLgjnxmibiaSpSSxicGbd0ib0Ojibv7iauiaxHDawQnMk5TMPDjHbr9qw/640?wx_fmt=png)

13.解密出来的payload就是SugarGh0st RAT，与此前Cisco Talos发布的payload相似，创建一个互斥变量，变量名就是该RAT的C2域名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySESBn3oQ29rgUsFDX4iau6S5HJTTn4CVX4hYVsuKXNhK0DibYxYL5BTR9g/640?wx_fmt=png)

14.启动键盘记录功能，在相应目录下生成记录文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEjalGbnO392mlTCzfLvz690ia2j4SIpFgQXpaybNUUibeyA2lEMicPwa4A/640?wx_fmt=png)

15.硬编码记录了样本的编译时间为2023年12月，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEwV5jZRPK0rwa1Q7r7RI0EoJX1uIicIdppImckJFSNv5TMIqYCkP2Mibw/640?wx_fmt=png)

16.通过硬编码的C2域名和端口，与黑客远程服务器建立连接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEDfFEfm78OR82sCRiaiaMKGBhVvlJwFxr4vSCc9YDcic8cZdg9tT0eUFHw/640?wx_fmt=png)

17.对进程进行提权相关操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEXqvJAtp1oS6XZ699iaa574KibmeZhIkjnBdtyicNLc4q3WbDtVQemK7yQ/640?wx_fmt=png)

18.获取主机相关信息发送到远程服务器，然后执行C2命令通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySE4AibQDwAmjEo0ib8kzBIEFia0JNkqnGCwmUZpatP3WwUuQWerHF5eVesg/640?wx_fmt=png)

19.文件操作相关的C2命令，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVjDlMKticWRwia5ibMjmicWySEoiaILEtg6Jjje29S5E0KLSuqyP7icWu7qtReGEarS4tUJHegtibNWJYPQ/640?wx_fmt=png)

其他C2指令可以参考Cisco Talos此前发布的相关报告，这里就不一一列举了。

总结结尾

安全对抗会一直持续存在，有攻必有防，攻与防就是矛与盾的关系，攻击者会不断更新自己的攻击样本和攻击技术，持续对抗安全产品的检测和查杀，安全研究人员需要持续不断的提升自己的安全能力，深入研究这些对抗技术，才能做到知已知彼，更快的发现这些安全问题。

笔者一直从事与恶意软件威胁情报相关的安全分析与研究工作，包含各种各样的不同类型的恶意软件，通过深度分析和研究这些恶意软件，了解全球黑客组织最新的攻击技术以及攻击趋势。

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