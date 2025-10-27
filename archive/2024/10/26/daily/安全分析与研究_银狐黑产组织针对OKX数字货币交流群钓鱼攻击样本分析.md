---
title: 银狐黑产组织针对OKX数字货币交流群钓鱼攻击样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489223&idx=1&sn=7b85d2226f0f06a2075cd8cc9389cbf2&chksm=902fb9efa75830f971709a61c2a0b5edbe15d91570e964945c2bc1df4d6afd469c5e63aee80b&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-26
fetch_date: 2025-10-06T18:53:20.052981
---

# 银狐黑产组织针对OKX数字货币交流群钓鱼攻击样本分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEoGJJC3xbhS4Z18Glkx0UCiaO78lzO8gdKrlJSkoSkS4PL1RTXRn8H5A/0?wx_fmt=jpeg)

# 银狐黑产组织针对OKX数字货币交流群钓鱼攻击样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/15941

先知社区 作者：熊猫正正

TG群、暗网是黑灰产的聚集地，也是钓鱼攻击的重灾区，搞钱也是大多数黑产组织最直接的攻击目的，有利益的地方就有黑灰产，最近一些年随着WEB3以及数字货币的流行与发展，产生了很多新型的产业链，同时也催生出了很多新型的黑客攻击活动，例如挖矿、勒索、盗币等。

近日，在某个欧易OKX官方中文数字货币交流群(群成员有快20万人)里捕获到一个银狐黑产组织的最新攻击样本，对该攻击样本加载母体进行了详细分析，分享出来供大家参考学习。

样本分析

1.初始样本是一个MSI安装程序，相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEUrNibS6RHkIDPmiaLb0tXKcGnqZib1gXtIqcutYMzH3atLJNsJvhAb5sQ/640?wx_fmt=png)

2.解析MSI安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEV5KCAicicTXhB9CmA3xBWgZ4uQEGdATVA8UCWzVaeND09a3sNAKM5XTg/640?wx_fmt=png)

3.CustomAction安装脚本，调用DriveAstuteSupporterCSE安装脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEC8qkrbk5kibtfhicPOGic09xicyab0NANqDpibfI67ibo9uNK8FEaeMoC2Fg/640?wx_fmt=png)

4.DriveAstuteSupporterCSE安装脚本，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEYfX0YP10Iy0QZDic1E8RbGlE4ORD0dVrKN0Y3vIbH4mgPBXNQnhMTVw/640?wx_fmt=png)

5.初始化相关的文件名、调用参数以及解压密码等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EE1DiaDlIMvbfAsjh2PdELAwArlt0OIlyP0hzAQibKrVdZ1Ouqy0ub7icBw/640?wx_fmt=png)

6.设置指定的排除文件目录扫描，对抗系统Windows Defender安全软件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEbuFe48qXfhuaTYqhK4K6VcgdWPeCKWZfesFLyicOlGdXwV0uMRf5ibicA/640?wx_fmt=png)

7.在指定的文件目录下生成相关的恶意文件并通过指定的参数调用，然后删除多余的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EECSf8z168Lic24OtMNwA5Pn8sTtYzpuInxffJecJDicaoMo5262FKc6ug/640?wx_fmt=png)

8.生成的恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EE4AicUQx0QU2Jy2lia5j12ZkVAXFIy9R90d65gorl3CP8gmPMnG1rgsAg/640?wx_fmt=png)

9.相关进程信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEicLnDII9VaDqWo3A17lP4XCcEczsoiatNRmTTRJ0gLKyhZjUXiciaCLvAA/640?wx_fmt=png)

10.判断主机是否联网以及解析调用参数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEdQBiarXDMS2HeAW3SWjlibc0rHWIhz97WxdzsnUy47VfnNFdibPr92gicg/640?wx_fmt=png)

11.在内存分配相关的空间，然后将解密出来的shellcode代码拷贝到该内存，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEGIlSuxFg7BeKD5eRKXRQTUt3ofp9YjicpQN2ia8E7fH8IuvDZOmcNtlA/640?wx_fmt=png)

12.跳转执行ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEia8c1vYhNLcMhckaicjL9BFqJWichn03xtTKoUgwPnCoTYicviaYqJZ1N5A/640?wx_fmt=png)

13.ShellCode分配相关的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EE4UkcHXmDDs8h8UFBmPG1jxhB6lqMwCgoHhUdJWJjibYyUDibVGzHxDDg/640?wx_fmt=png)

14.解密ShellCode后面的PayLoad数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEyTxeqYvj84BrZ2S1HnFYxgBrKqTVuj70xz8rAibrZ9fjZ4EicCE0jCXA/640?wx_fmt=png)

15.解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEonibh86V4dz6s9z0onG1WWgRWKcWsZx1fGKypuRD6Zy2Daub1CNuY3w/640?wx_fmt=png)

16.解密出来的PayLoad编译时间为2024年10月15日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEfkf4mE7Q0PFHz1ibicBQOwASVoymtUeKUEtaSibu7HvqS5HUzgYic11vzg/640?wx_fmt=png)

17.银狐木马变种标识性导出函数fuckyou，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EE20k7K2q6icyicBLzI9dqqwAMy7M8FDXicr4IwpmUHoliatsKza7kzoibIEw/640?wx_fmt=png)

18.初始化样本的相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEC09vY1WDW6IMk3NY1woiaGdrH9h9WaRiaSEEcanuduDnxj8E8TGTMM6A/640?wx_fmt=png)

19.远程服务器IP为38.47.232.92，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEW1btFu9DMOpO4uJGQhGKk8WfXd07D6YwvGAyWnUrkoQfyW885PfJew/640?wx_fmt=png)

20.通过威胁情报平台查询相关域名信息，已经标记为银狐木马，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEOSuBgGCTmUmYZraqyUCjibWsJXbJUOsexnaQmkT0ZjdrvLZz10icHS5Q/640?wx_fmt=png)

解密出来的PayLoad与此前发现的银狐变种，基本一致就不重复分析了，同时通过威胁情报可以关联出多个同批次的样本和情报，基本手法与上面一致。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVic1d2511iat4krqsFAjo1EEtic4zT1VUcjLAHDvgvvFFp9KD22Sk7m8iaeHW2NvAkiaa6yiaP06sJmYIg/640?wx_fmt=png)

总结结尾

去年使用“银狐”黑客远控工具的几个黑产团伙非常活跃，今年这些黑产团伙仍然非常活跃，而且仍然在不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，免杀对抗手法一直在升级。

安全分析与研究，专注于全球恶意软件的分析与研究，追踪全球黑客组织攻击活动，欢迎大家持续关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUnNRBvJfnT5ukzfT9tt8lwfevbMrbsOTib8voWQSs6wcBeknN0HNtJjcoYORCDu8ekm6MGHqDibrYg/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

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