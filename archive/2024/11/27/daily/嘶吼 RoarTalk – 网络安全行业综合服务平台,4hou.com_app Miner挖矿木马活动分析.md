---
title: app Miner挖矿木马活动分析
url: https://www.4hou.com/posts/33O4
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-27
fetch_date: 2025-10-06T19:12:13.749564
---

# app Miner挖矿木马活动分析

app Miner挖矿木马活动分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# app Miner挖矿木马活动分析

安天
[技术](https://www.4hou.com/category/technology)
2024-11-26 15:57:42

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)84862

收藏

导语：近期，安天CERT监测到一起挖矿木马攻击事件，该挖矿木马从2024年3月开始出现，并持续更新攻击脚本。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609483214786.jpg "1732604103336707.jpg")

**1 概述**

近期，安天CERT监测到一起挖矿木马攻击事件，该挖矿木马从2024年3月开始出现，并持续更新攻击脚本。该挖矿木马的典型特点是针对操作系统类型下载对应的挖矿程序、检查系统环境是否有curl、Python、Perl等工具，如果有则使用这些工具下载挖矿程序，如果没有会进行下载适配、根据CPU算力动态调整运行参数，不会饱和使用CPU资源，避免因消耗过多资源被用户感知发现。该挖矿木马因其在脚本中多次出现“app”字符串，故安天CERT将该挖矿木马命名为“app Miner”。

经验证，安天智甲终端防御系统可实现该挖矿木马的有效查杀。

**2 攻击流程**

app Miner挖矿木马首先会执行一系列功能模块中的功能，如根据CPU线程数估算门罗币（Monero）挖矿的哈希率、根据CPU算力动态调整运行参数、遍历指定目录尝试找到一个足够空间投放挖矿木马的目录、根据受害主机操作系统类型和架构等，生成一个格式化的文件名、查找感染系统中正在运行的竞品挖矿进程等等。之后会从指定的URL上下载挖矿程序、设置挖矿配置文件进行挖矿。该挖矿木马还有很多函数具有多种功能，但默认状态下脚本未开启这些功能或待开发中，其中主要包括计划任务函数、服务函数、进程检查函数等等。

![图 2 1 攻击流程图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609484130849.png "1732604020125673.png")

图 2‑1 攻击流程图

**3 脚本功能分析**

根据CPU线程数估算Monero挖矿的哈希率，然后基于这个哈希率动态计算并选择一个端口号。用于配置一个挖矿程序以选择适当的端口进行通信。这样的设计可能是为了在不同机器上运行时根据机器的不同性能选择合适的设置。

![图 3 1 估算Monero挖矿的哈希率.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609485675460.png "1732604009211835.png")

图 3‑1 估算Monero挖矿的哈希率

根据CPU核数的70%，按指定公式调用mathlib计算结果。比如，对于16核CPU，这一结果为4096。通过控制线程数量的方式，让CPU的资源占用不饱和。

![图 3 2 动态调整CPU功率.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609485185733.png "1732603971740001.png")

图 3‑2 动态调整CPU功率

遍历一系列目录（如$HOME，$PWD，/var/tmp，/dev/shm，/var/run，/tmp），尝试在这些目录中找到一个可写的目录，并检查其是否有足够的可用空间。

![图 3 3 遍历指定目录并查看目录可用空间大小.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609486196165.png "1732603957101231.png")

图 3‑3 遍历指定目录并查看目录可用空间大小

根据操作系统类型、架构以及是否需要压缩和加密，来生成一个格式化的文件名。该功能通常用于生成特定平台和配置的可执行文件或包的名称，以便在不同环境中识别和使用。![图 3 4 格式化文件名.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609487201126.png "1732603947124466.png")

图 3‑4 格式化文件名

查找系统中正在运行的竞品挖矿进程，支持精确匹配和模式匹配。它根据系统上可用的工具（如pgrep、ps、pidof）选择最佳方式进行查找，并在这些工具不可用时，通过手动遍历/proc文件系统进行查找，当查找到竞品挖矿进程后，使用pkill、killall、kill等命令进行结束进程。

![图 3 5 查找正在运行的竞品挖矿进程.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609488196140.png "1732603927124986.png")

图 3‑5 查找正在运行的竞品挖矿进程

更改挖矿程序落地目录的权限。

![图 3 6 更改挖矿程序落地目录的权限.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609489152129.png "1732603909104197.png")

图 3‑6 更改挖矿程序落地目录的权限

从指定的URL下载挖矿程序，并根据受害者机器上的工具进行下载操作。如wget、curl、perl、Python 2.x和Python 3.x等。

![图 3 7 下载挖矿程序.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609489198268.png "1732603888135667.png")

图 3‑7 下载挖矿程序

设置挖矿配置文件，矿池地址为207.180.217.230:80。

![图 3 8 设置挖矿配置文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609490198141.png "1732603865972971.png")

图 3‑8 设置挖矿配置文件

**4 事件对应的ATT&CK映射图谱**

针对攻击者投放挖矿木马的完整过程，安天梳理本次攻击事件对应的ATT&CK映射图谱如下图所示。

![图 4 1 事件对应的ATT&CK映射图谱.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609494173203.png "1732603837113194.png")

图 4‑1 事件对应的ATT&CK映射图谱

攻击者使用的技术点如下表所示：

表 4‑1 事件对应的ATT&CK技术行为描述表

|  |  |  |
| --- | --- | --- |
| ATT&CK阶段/类别 | 具体行为 | 注释 |
| 执行 | 利用命令和脚本解释器 | 使用bash脚本命令 |
| 持久化 | 利用外部远程服务 | 创建服务 |
| 利用计划任务/工作 | 创建计划任务 |
| 提权 | 滥用提升控制权限机制 | 修改文件权限 |
| 防御规避 | 修改文件和目录权限 | 修改文件权限和目录权限 |
| 发现 | 发现系统信息 | 发现系统架构等信息 |
| 影响 | 资源劫持 | 占用CPU资源 |

**5 防护建议**

针对挖矿攻击，安天建议企业采取如下防护措施：

**1.安装终端防护**：安装反病毒软件，针对不同平台建议安装安天智甲终端防御系统Windows/Linux版本；

**2.加强SSH口令强度**：避免使用弱口令，建议使用16位或更长的口令，包括大小写字母、数字和符号在内的组合，同时避免多个服务器使用相同口令；

**3.及时更新补丁**：建议开启自动更新功能安装系统补丁，服务器应及时更新系统补丁；

**4.及时更新第三方应用补丁**：建议及时更新第三方应用如Redis等应用程序补丁；

**5.开启日志**：开启关键日志收集功能（安全日志、系统日志、错误日志、访问日志、传输日志和Cookie日志），为安全事件的追踪溯源提供基础；

**6.主机加固**：对系统进行渗透测试及安全加固；

**7.部署入侵检测系统（IDS）**：部署流量监控类软件或设备，便于对恶意代码的发现与追踪溯源。安天探海威胁检测系统（PTD）以网络流量为检测分析对象，能精准检测出已知海量恶意代码和网络攻击活动，有效发现网络可疑行为、资产和各类未知威胁；

**8.安天服务**：若遭受恶意软件攻击，建议及时隔离被攻击主机，并保护现场等待安全工程师对计算机进行排查；安天7\*24小时服务热线：400-840-9234。

建议企业用户部署专业的终端安全防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀本次发现病毒样本。

智甲客户端通过主动防御能力实时检测本地脚本执行行为，对执行脚本进行威胁检测，一旦发现启动脚本为恶意文件，可自动拦截并向用户发送风险告警，保障终端环境安全。

![图 5 1运行恶意脚本时智甲成功拦截.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609495163356.png "1732603799142211.png")

图 5‑1运行恶意脚本时智甲成功拦截

智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。

![图 5 2 通过智甲管理中心可对安全事件统一管理和处置.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732609496362882.png "1732603783618638.png")

图 5‑2 通过智甲管理中心可对安全事件统一管理和处置

**6****IoCs**

|  |
| --- |
| IoCs |
| 157.230.106[.]100 |
| 111.48.208[.]225 |
| 207.180.217[.]230 |
| 185.213.26[.]27 |
| 199B790D05724170F3E6583500799DB1 |
| C0ED4F906576C06D861302E8CF924309 |

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?EAMSxzkb)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/10/a4d310d551660a09a8f6.jpg)

# [安天](https://www.4hou.com/member/e3QQ)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/e3QQ)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?...