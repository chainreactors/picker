---
title: 图数据库在攻击链路场景下利用的可行性
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzczOTA3OQ==&mid=2247486059&idx=1&sn=5c712dec829c9bcb9f21e215e2ac0858&chksm=cf1f2743f868ae55092d0d1e665166ae9d90652169efd6bb6fa6ace6607c8ed5cd7d8f981433&scene=58&subscene=0#rd
source: RainSec
date: 2024-07-23
fetch_date: 2025-10-06T17:45:50.488806
---

# 图数据库在攻击链路场景下利用的可行性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichc9Qic6SjsMd8P6HOO0G6WCynfRKuglJIPaSkYA5bPx4nzzicghKloZKicQ/0?wx_fmt=jpeg)

# 图数据库在攻击链路场景下利用的可行性

原创

KID

RainSec

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkb1yDnVcgIlvd3KG3vX76egiaDfKT3XbKmjGJjIa3foicznOnreTcvrRwtccfNAZ4I8TuibyIuNnkiatQ/640?wx_fmt=png)

## 前言

图关系型数据库已经出现很久了，也或多或少的应用在了安全领域，如：

1. 1. 代码审计，漏洞挖掘，如：https://github.com/wh1t3p1g/tabby-path-finder/；
2. 2. 资产关联：各个态势感知平台会用作来展示关系；
3. 3. 漏洞信息/威胁信息等：

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichco1W7eGVx067lUtmlrjyN9wVPrqhZvHdumANTicmLtvVXZ7RhhWB8ricQ/640?wx_fmt=png&from=appmsg)

1. 4. 还有很多通过日志去还原攻击链路：https://xz.aliyun.com/t/11147?time\_\_1311=Cq0x2Dg7GQKWqGNDQiuAxAx7weQw9gELbD、[https://mp.weixin.qq.com/s/ofP4j2TEfNoCYqrLhMsvZA](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect")。

     这些都或多或少的增强了安全的实力，图可以用更直接的方式来展示和分析各个节点之间的关系，在分析日志的时候，大家的文章考虑过分别用流量日志、主机日志来用图去分析，也讨论过去综合分析，现在来考虑，在流量/主机日志都尽可能抓到的情况下，结合图数据库，能做到什么地步。

## 场景搭建

     逻辑很简单，通过文件上传，上传一个webshell，在通过webshell工具去连接、通过cs来进行后渗透，如：进程注入等其他工作等。这些东西很简单，几个虚拟机都可以完成，就不详细说明了。流量日志使用支持snort规则库的引擎来进行，主机日志是在windows上的sysmon，因为他们都有不错的检测规则，特别是sysmon，对于windows，基本上所有需要的字段都能得到（不愧是微软自己的），然而，虽然有SysmonForLinux，经过简单测试，并不理想。

## 思路介绍

先看下绿盟的文章

[https://mp.weixin.qq.com/s/ofP4j2TEfNoCYqrLhMsvZA](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect")

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichcibLQ3YNU6Ljblib5wXhvThh0LWBqYbJzRZKj71gKPgzbnD1UNBpE3XiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichcdJ2CtkuId8QbbSrBSBTxziaMeZvMb8hsyFJx6TRIexxY9dUKo75CJ8A/640?wx_fmt=png&from=appmsg)

其实给了不错的思路，通过5元组来进行配置来尽可能的将主机和网络侧的日志来进行关联。

### 主机事件

     sysmon可直接参考微软的官方教程：https://learn.microsoft.com/zh-cn/sysinternals/downloads/sysmon 里面涉及到网路连接、文件的增删、进程的注入等等，详情可根据具体情况分析。

| ID | 标记 | 事件 |
| --- | --- | --- |
| **1** | ProcessCreate | 进程创建 |
| **2** | FileCreateTime | 文件创建时间 |
| **3** | NetworkConnect | 检测到网络连接 |
| **4** | 不适用 | Sysmon 服务状态更改（无法筛选） |
| **5** | ProcessTerminate | 进程已终止 |
| **6** | DriverLoad | 驱动程序已加载 |
| **7** | ImageLoad | 映像已加载 |
| **8** | CreateRemoteThread | 检测到 CreateRemoteThread |
| **9** | RawAccessRead | 检测到 RawAccessRead |
| **10** | ProcessAccess | 进程被访问 |
| **11** | FileCreate | 文件已创建 |
| **12** | RegistryEvent | 已添加或删除注册表对象 |
| **13** | RegistryEvent | 注册表值已设置 |
| **14** | RegistryEvent | 注册表对象已重命名 |
| **15** | FileCreateStreamHash | 文件流已创建 |
| **16** | 不适用 | Sysmon 配置更改（无法筛选） |
| **17** | PipeEvent | 已命名管道已创建 |
| **18** | PipeEvent | 已命名管道已连接 |
| **19** | WmiEvent | WMI 筛选器 |
| **20** | WmiEvent | WMI 使用者 |
| **21** | WmiEvent | WMI 使用者筛选器 |
| **22** | DNSQuery | DNS 查询 |
| **23** | FileDelete | 文件删除已存档 |
| **24** | ClipboardChange | 剪贴板中的新内容 |
| **25** | ProcessTampering | 进程映像更改 |
| **26** | FileDeleteDetected | 文件删除已记录 |
| **27** | FileBlockExecutable | 文件阻止可执行 |
| **28** | FileBlockShredding | 文件阻止粉碎 |
| **29** | FileExecutableDetected | 可执行文件已删除 |

### 流量事件

     流量的基础信息为五元组（源ip、目的ip、协议、源端口、目的端口）、预警信息等。

### 综合考量

     主机日志与流量日志所共用的点在于网络连接信息即四元组（源ip、目的ip、源端口、目的端口），那么我就可以通过这个来将两个日志类型关联起来。然后就是对日志事件的字段进行分析，如：

1. 1. 网络连接：源ip->告警日志->进程->目的ip；
2. 2. 创建文件：进程->文件；
3. 3. 进程注入：进程->目标进程；

理论上通过自定义的规则就可以将所有的行为与进程串联起来了。

## 具体分析

前面已经说了思路，那么我们来一步步来测试下情况，原始情况：

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichcETZZcxj3Pl45TetKriaN3f3Qa1rbD7p6jm64t2dfyLLaIXlx7v8jIiaw/640?wx_fmt=png&from=appmsg)

因为存在扫描行为，和正常请求行为，所以不可避免的造成爆炸，那么我们先去掉扫描的事件和一些不重要的请求日志：

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichc81ST9CGslsrm0lvP6aNb4lnZD8P0GagdFwk12DibkvHRNp1icLGBWJ1g/640?wx_fmt=png&from=appmsg)

然后具体分析下

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichc81ST9CGslsrm0lvP6aNb4lnZD8P0GagdFwk12DibkvHRNp1icLGBWJ1g/640?wx_fmt=png&from=appmsg)

可以看到根据流量告警关联到了httpd.exe，httpd.exe下的php-cgi.exe创建了一个cs.exe，并且执行

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichc9TibQG4S2h14WRdj6VAA0r9NlMLFummEjRQRqEquAzKYr5eOsHAibvUQ/640?wx_fmt=png&from=appmsg)

这是在webshell工具上执行的命令，通过主机日志可以弥补流量日志的不足，了解攻击者到底做了什么。

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkZibI4ibWDC9GgC6OOoBvtichcSpWJMO4NuWd74po9JZVIf2kb6aD6QZBz66NKT6fXlI5bibvH5OJ3Krg/640?wx_fmt=png&from=appmsg)

然后攻击者通过cs木马连接到攻击者的c2上，也可通过流量/主机日志进行关联。通过日志的综合分析，可以将攻击者的整个行为串联，在复杂情境下，对于通过免杀或者流量混淆绕过安全设备的行为也可以尽量找出踪迹，发现攻击者。

## 一点点思考

     在实际过程里，很多设备的日志都是割裂开来的，流量是流量，终端是终端，导致大家进行分析溯源分析都比较割裂，无法准确的还原攻击链路，虽然edr等设备已经出来很久了，但实战上与流量设备的配合并不太理想。实验只使用了很简单很简单的场景，对于日志自定义了一些处理规则，实现了将整个攻击链路展现的情景。然而，真正情况下，会有一下问题：

1. 1. 流量告警的数量超级多，数据清理和策略的编写是个大问题；
2. 2. 攻击者的阶段性攻击可能并不发生在同一时间，那么日志关联的时间颗粒度也是问题；
3. 3. 不管是流量/终端日志都会有存储不完全的情况，没有监测到行为或者被攻击者kill掉/删除，之所以使用windows实验，也是没在linux下发现类似于sysmon一样好用的日志记录工具；
4. 4. 正如绿盟的文章说的：完全利用图分析算法进行复杂攻击识别是有天花板的，外部知识的引入是一种有效的手段，但是当前外部知识只是简单的根据规则抽象出一些已有攻击的威胁子图，利用ATT&CK相关的攻击战术手法。需要在实战不断去试验、反馈、结合算法、ai、大数据等技术去发展；

安全运营的概念提出好久，产品也更新换代了很多，攻击溯源依然是实现主动防御的一种思路，希望某一天真的可以看到有真正好用的落地产品。

## 参考文章

1. 1. [https://mp.weixin.qq.com/s/ofP4j2TEfNoCYqrLhMsvZA](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247488568&idx=1&sn=34cdb63e1dc0125df6206257efd5eeff&scene=21#wechat_redirect")
2. 2. https://xz.aliyun.com/t/11147?time\_\_1311=Cq0x2Dg7GQKWqGNDQiuAxAx7weQw9gELbD
3. 3. https://github.com/wh1t3p1g/tabby-path-finder/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkY86urnibFC82ElAnl936OYpgurccPJLeWWfS9jjC6aNOyHhbicBKkNw8O8dpyR5boygH1pzBVDakaQ/0?wx_fmt=png)

RainSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkY86urnibFC82ElAnl936OYpgurccPJLeWWfS9jjC6aNOyHhbicBKkNw8O8dpyR5boygH1pzBVDakaQ/0?wx_fmt=png)

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