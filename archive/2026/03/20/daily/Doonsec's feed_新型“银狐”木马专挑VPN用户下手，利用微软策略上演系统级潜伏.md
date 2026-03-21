---
title: 新型“银狐”木马专挑VPN用户下手，利用微软策略上演系统级潜伏
url: https://mp.weixin.qq.com/s/d_ShDhTy5HzYgsXNTUPPuQ
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:12.416062
---

# 新型“银狐”木马专挑VPN用户下手，利用微软策略上演系统级潜伏

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zfoRGB81MxObvFqp2xrELBFic0acmzQqUribjD2npegt9XDDI6j7Nd80mtZ4BEXP8Vqx6pKEjjibrEEnwHrsFUuax8MTnPUUrWQzCPNhp19VeI/0?wx_fmt=jpeg)

# 新型“银狐”木马专挑VPN用户下手，利用微软策略上演系统级潜伏

360数字安全

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

**近日，360数字安全集团监测到一个新的银狐团伙，其主要攻击目标为VPN用户。**在攻击过程中，该团伙伪造“快连VPN”、“Chrome”等应用的下载页面，诱导用户下载执行恶意程序。

该木马运行后不仅会释放Gh0st远控木马，窃取用户敏感信息并实现持久化控制，还会利用微软WDAC策略，阻止安全软件及相关签名程序的启动。以伪装成Chrome官网的钓鱼站点为例，其链接为hxxps://chrome01.gg.zemhx.cn/#，页面制作精良，极具迷惑性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMjSIp6bRVmibaiba60xsDvkZFDMjsIqKCC9AL7YCWXfY2L3iahtSf8XicTxe9HGqm0FbAAneHulGYKEVV3gXDCOc56W75DiaicEo0HQ/640?wx_fmt=png&from=appmsg)

**套壳Chrome引诱下载**

**深植远控木马窃取信息**

此次360捕获的木马样本将自己伪装成Chrome浏览器，不仅采用Inno打包，还精心设计了软件图标，目的就是诱导用户下载运行。一旦用户下载并运行，它便会在%userprofile%\appdata\local\programs\c3a0420d8\nsggo\ecjrb\目录下释放某游戏的主程序文件。

用户运行的这个主程序本身是一款正常的游戏应用，不含恶意代码，其作用是为后续攻击行为提供掩护。然而，该程序在执行过程中会默认加载同目录下的“cas.dll”文件，从而触发其中隐藏的恶意代码。完成恶意操作后，木马还会将该临时目录设置为系统隐藏属性，以实现自我隐藏。

恶意代码启动后，首先将精心构造的代码段注入系统服务进程WmiApSrv.exe，随后采用线程池注入方式，将另一段完整的可执行代码注入系统服务宿主进程svchost.exe中。此后，该木马还在%windir%\system32\CodeIntegrity目录下释放一个名为SiPolicy.p7b的隐藏文件，利用微软WDAC策略禁用安全软件及相关签名程序的启动。360安全智能体解码该文件后发现，其拦截策略借助系统管道协议构建通道，并通过RPC创建服务，以实现持久化控制。

最终，该木马将属于Gh0st远控木马家族的后门模块注入系统进程sihost.exe中。该模块不仅会窃取用户的系统版本、主板、CPU、磁盘空间、内存等设备信息，还具备屏幕监控、剪贴板读取、文件下载执行等一系列高危远控功能。

**多节点纵深布防**

**360终端安全智能体蜂群绞杀银狐**

**事实上，在恶意代码进行进程注入时，360终端安全智能体能通过系统内预置的监控点，第一时间发现并有效拦截此类敏感操作。**

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxNC4EbQVEE2MPYVXylVVNxeyyqibkntaNk95MDoQTJUjmUYiakeldWNibwsWibO7VuWL1yjicFw7E1BxeRORtblKzwdsRiaRVhV9FOlk/640?wx_fmt=png&from=appmsg)

然而，若终端未安装或启用360终端安全智能体，该木马一旦先行感染，便会禁用包括360在内的常见安全软件。即便事后发现异常再安装，也为时已晚。

因此，针对银狐木马，最有效的防范除了在于主动识别钓鱼信息并严格遵守安全规范外，还应采取体系化、针对性的防护措施，筑牢安全屏障。

**作为国内兼具数字安全和人工智能双重能力的企业，360在自研安全大模型的赋能下，将安全专家的能力和经验进行固化，并结合过去20年积累的海量样本数据、情报能力以及终端安全上1200余项能力点，打造出终端安全智能体蜂群。**

为有效应对银狐木马威胁，360依托终端安全智能蜂群体赋能的云安全立体防护体系，构建起涵盖传播拦截、行为监测、深度清理的银狐木马全周期防御矩阵。

**在木马传播的初始阶段**

该体系中的下载安全防护模块已实现对主流通讯软件的全链路覆盖，可对通过钉钉、微信、QQ等渠道传播的恶意文件进行实时检测，在木马落地前即完成自动查杀。

**针对攻击者精心设计的对抗手段**

比如遭遇掺杂大量干扰文件的多文件攻击，抑或是面对超大文件规避检测的传统伎俩，以及针对加密压缩包和“配置型白利用”等新型攻击方式，该体系皆可依托终端安全智能体蜂群赋能的智能分析系统，将安全专家的分析经验汇集于模型之中，快速从各类扫描数据中找出符合以上攻击特性的样本，从而实现自动阻断拦截。此外，还会对无法识别的可疑文件进行标记，并持续监测其后续行为。

**对于传输过程中的漏网之鱼**

360主动防御系统会对用户电脑提供强力保护。近期，银狐木马常用的攻击包括PoolParty注入、模拟用户点击、WFP断网、安全软件驱动利用、Windows Defender策略滥用等，360主动防御对这些攻击均能进行有效防御，并对发现的漏网之鱼进行清剿。

**在终端处置环节**

360云安全立体防护体系中的远控·勒索急救模式展现强大应急响应能力。该模式可一键切断攻击者控制通道，为深度清理争取宝贵时间窗口。此外，该体系不仅支持对各类驱动级木马的清理、对被篡改的系统配置进行修复，也支持对被银狐木马利用的合法管理软件的智能检测与卸载。

**据360终端安全智能体蜂群监测，近两年被滥用于攻击的合法软件已达数十款，常见包括IPGUARD、阳途、固信、安在等，360终端安全智能体蜂群已支持对此类软件的全面检测与一键清理。**

目前，360云安全立体防护体系已经实现对银狐木马病毒的全面查杀，建议广大政企机构尽快部署。

**如需咨询相关服务**

**请联系电话**

**400-0309-360**

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 2026两会观察 | 周鸿祎为智能体人才培养献策，360先行落地 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585196&idx=1&sn=411d31527985da5cfb73f1beb83c429b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ●  360龙虾卫士重磅上线：九大能力专治OpenClaw“裸奔” | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585414&idx=1&sn=eda1a5e0a9282e83255dfe33c7de4ab7&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● IDC双报告首推：360以绝对实力护航每只“龙虾”安全 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585375&idx=1&sn=e70a863eb3baac335080bdc9c4d0143a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 360安全龙虾「养虾速成课」正式上线ISC.AI学苑！ | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585434&idx=2&sn=9e145e933928722c36df13f6cdbd53dd&scene=21#wechat_redirect) | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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