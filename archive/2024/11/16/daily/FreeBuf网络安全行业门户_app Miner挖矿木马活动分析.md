---
title: app Miner挖矿木马活动分析
url: https://www.freebuf.com/articles/network/415382.html
source: FreeBuf网络安全行业门户
date: 2024-11-16
fetch_date: 2025-10-06T19:17:50.468334
---

# app Miner挖矿木马活动分析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

app Miner挖矿木马活动分析

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

app Miner挖矿木马活动分析

2024-11-15 15:32:16

所属地 北京

# 1 概述

近期，安天CERT监测到一起挖矿木马攻击事件，该挖矿木马从2024年3月开始出现，并持续更新攻击脚本。该挖矿木马的典型特点是针对操作系统类型下载对应的挖矿程序、检查系统环境是否有curl、Python、Perl等工具，如果有则使用这些工具下载挖矿程序，如果没有会进行下载适配、根据CPU算力动态调整运行参数，不会饱和使用CPU资源，避免因消耗过多资源被用户感知发现。该挖矿木马因其在脚本中多次出现“app”字符串，故安天CERT将该挖矿木马命名为“app Miner”。

# 2 攻击流程

app Miner挖矿木马首先会执行一系列功能模块中的功能，如根据CPU线程数估算门罗币（Monero）挖矿的哈希率、根据CPU算力动态调整运行参数、遍历指定目录尝试找到一个足够空间投放挖矿木马的目录、根据受害主机操作系统类型和架构等，生成一个格式化的文件名、查找感染系统中正在运行的竞品挖矿进程等等。之后会从指定的URL上下载挖矿程序、设置挖矿配置文件进行挖矿。该挖矿木马还有很多函数具有多种功能，但默认状态下脚本未开启这些功能或待开发中，其中主要包括计划任务函数、服务函数、进程检查函数等等。

![](https://image.3001.net/images/20241115/1731655886_6736f8cef073a089fcf8a.png!small)

图 2‑1 攻击流程图

# 3 脚本功能分析

根据CPU线程数估算Monero挖矿的哈希率，然后基于这个哈希率动态计算并选择一个端口号。用于配置一个挖矿程序以选择适当的端口进行通信。这样的设计可能是为了在不同机器上运行时根据机器的不同性能选择合适的设置。

![](https://image.3001.net/images/20241115/1731655874_6736f8c25b053ace92de8.png!small)

图 3‑1 估算Monero挖矿的哈希率

根据CPU核数的70%，按指定公式调用mathlib计算结果。比如，对于16核CPU，这一结果为4096。通过控制线程数量的方式，让CPU的资源占用不饱和。

![](https://image.3001.net/images/20241115/1731655865_6736f8b9520ce6f01ddec.png!small)

图 3‑2 动态调整CPU功率

遍历一系列目录（如$HOME，$PWD，/var/tmp，/dev/shm，/var/run，/tmp），尝试在这些目录中找到一个可写的目录，并检查其是否有足够的可用空间。

![](https://image.3001.net/images/20241115/1731655853_6736f8adf32b10de489f3.png!small)

图 3‑3 遍历指定目录并查看目录可用空间大小

根据操作系统类型、架构以及是否需要压缩和加密，来生成一个格式化的文件名。该功能通常用于生成特定平台和配置的可执行文件或包的名称，以便在不同环境中识别和使用。

![](https://image.3001.net/images/20241115/1731655843_6736f8a3dbc098bb03382.png!small)

图 3‑4 格式化文件名

查找系统中正在运行的竞品挖矿进程，支持精确匹配和模式匹配。它根据系统上可用的工具（如pgrep、ps、pidof）选择最佳方式进行查找，并在这些工具不可用时，通过手动遍历/proc文件系统进行查找，当查找到竞品挖矿进程后，使用pkill、killall、kill等命令进行结束进程。

![](https://image.3001.net/images/20241115/1731655830_6736f896d3dd6dd23ce31.png!small)

图 3‑5 查找正在运行的竞品挖矿进程

更改挖矿程序落地目录的权限。

![](https://image.3001.net/images/20241115/1731655817_6736f889536d4c05b873d.png!small)

图 3‑6 更改挖矿程序落地目录的权限

从指定的URL下载挖矿程序，并根据受害者机器上的工具进行下载操作。如wget、curl、perl、Python 2.x和Python 3.x等。

![](https://image.3001.net/images/20241115/1731655806_6736f87ee0f081caa3380.png!small)

图 3‑7 下载挖矿程序

设置挖矿配置文件，矿池地址为207.180.217.230:80。

![](https://image.3001.net/images/20241115/1731655797_6736f875777258f348cd5.png!small)

图 3‑8 设置挖矿配置文件

# 4 事件对应的ATT&CK映射图谱

针对攻击者投放挖矿木马的完整过程，安天梳理本次攻击事件对应的ATT&CK映射图谱如下图所示。

![](https://image.3001.net/images/20241115/1731655781_6736f865b538ecc98c48c.png!small)

图 4‑1 事件对应的ATT&CK映射图谱

攻击者使用的技术点如下表所示：

表 4‑1 事件对应的ATT&CK技术行为描述表

|  |  |  |
| --- | --- | --- |
| **ATT&CK****阶段/类别** | **具体行为** | **注释** |
| **执行** | 利用命令和脚本解释器 | 使用bash脚本命令 |
| **持久化** | 利用外部远程服务 | 创建服务 |
| 利用计划任务/工作 | 创建计划任务 |
| **提权** | 滥用提升控制权限机制 | 修改文件权限 |
| **防御规避** | 修改文件和目录权限 | 修改文件权限和目录权限 |
| **发现** | 发现系统信息 | 发现系统架构等信息 |
| **影响** | 资源劫持 | 占用CPU资源 |

# 5 IoCs

|  |
| --- |
| **IoCs** |
| 157.230.106[.]100 |
| 111.48.208[.]225 |
| 207.180.217[.]230 |
| 185.213.26[.]27 |
| 199B790D05724170F3E6583500799DB1 |
| C0ED4F906576C06D861302E8CF924309 |

# 网络安全 # 挖矿木马 # 安天科技

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)