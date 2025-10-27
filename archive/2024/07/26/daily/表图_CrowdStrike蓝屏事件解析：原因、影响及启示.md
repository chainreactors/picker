---
title: CrowdStrike蓝屏事件解析：原因、影响及启示
url: https://mp.weixin.qq.com/s?__biz=MzUzOTI4NDQ3NA==&mid=2247484628&idx=1&sn=7141917d915f7e5a26967c43e68a095e&chksm=facb8241cdbc0b57d99f7f08a3c1d2eb455f3417ccfdfef408559339a87956d9e392b8370665&scene=58&subscene=0#rd
source: 表图
date: 2024-07-26
fetch_date: 2025-10-06T17:43:34.693019
---

# CrowdStrike蓝屏事件解析：原因、影响及启示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yj84I2oLjvn0pU1Zic2RRqW3nwWExXAglLGYNbshxckUxunWJ7IGsMsQ/0?wx_fmt=jpeg)

# CrowdStrike蓝屏事件解析：原因、影响及启示

四楼南侧东

表图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yCJ9DianJNtGca9UzOLKnjKa1JJ895bcvBicGy2z4MS5wumH2sxwe1sgw/640?wx_fmt=png&from=appmsg)

本周网络安全行业的头条新闻无疑是CrowdStrike引发的Windows蓝屏事故。包括航空公司、金融机构、医疗机构和政府机构在内，共超过850万台PC和服务器受到影响，其中最严重的达美航空取消了7000多个航班。尽管事件并非由攻击引起，但其对可用性的破坏仍然是广义上的信息安全事件。经过几天的调查，事情已经明朗，我们来探讨一下事件的发生经过、严重性及未来影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2ypWSQBQ2AWPy9uArpHmict5XyXITzhtTkIgWfbiczjmptGdCM16rlwmWg/640?wx_fmt=jpeg&from=appmsg)纽约拉瓜迪亚机场

## **发生了什么**

CrowdStrike Falcon 是一款先进的端点检测与响应（EDR）解决方案，利用云端分析和机器学习技术，提供实时威胁检测和响应。但特征检测永远是终端安全软件的基础，Falcon平台会每天多次的向终端代理推送检测规则，即下发C开头的.sys文件到Windows的以下目录：

> `C:\Windows\System32\drivers\CrowdStrike\`

这些文件虽有.sys后缀，但并不是内核驱动，而是CrowdStrike新发现的战术、技术和程序（TTP）的配置文件，用以检测终端的异常行为，并不包含代码。

从世界协调时7月19日04:09（北京时间中午 12:09）开始，Falcon平台向终端代理推送新的TTP检测规则配置文件“C-00000291-\*.sys”。291是今年 2 月底更新的 7.11 版 Agent 新增的检测方法，针对进程间通信的恶意行为，这个新的规则配置文件包含一些新发现的、在网络攻击中被C2框架利用的命名管道（named pipes）的异常行为。但由于该更新存在bug，越界内存读取并触发异常导致Windows操作系统崩溃。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yGmprAfdic53wUm2bHxKZQdeRCdTC2vK6L1N004qEjvcibZNibnXSiakicfg/640?wx_fmt=jpeg&from=appmsg)

> CrowdStrike的Falcon EDR的Agent进程是CSAgent.sys，导致崩溃的指令是汇编指令“mov r9d, [r8]”。这条指令将r8地址中的字节移动到r9d地址。问题在于r8是一个未映射的地址（无效），因此进程崩溃。

到05:27，CrowdStrike发现问题并停止推送该更新。

## **为什么会这么严重**

规则更新引发系统崩溃是直接原因，但从04:09到05:27这短短78分钟内，配置文件就被分发到了850万台Windows主机。尽管这些文件不包含代码，但没有分批次更新而是全量更新，这在工程设计上是不可取的，也是造成此次事故如此严重的主要原因。

在昨天CrowdStrike发布的事故审查初步报告中，在未来配置文件更新分发的改进方面，有这么两条：

1. 实施分阶段部署策略，将快速响应内容逐步部署到更多的传感器基础中。
2. 通过允许客户精细选择更新的时间和位置，为客户提供更大的快速响应内容更新控制权。

其中，第一条是早就该实施的，第二条则是大型客户的必备需求。此前，CrowdStrike将版本升级和规则升级分开处理，并不向客户提供自定义规则升级的分发配置功能，这种做法我认为是不好的实践。

此外，恢复措施需要逐台人工处理，缺乏批量化和自动化的恢复手段，也是让事件如此严重的一大原因。尽管CrowdStrike推送了新更新，但由于蓝屏和离线状态，Windows终端难以自动恢复。

## **对行业的影响**

CrowdStrike多年来在Gartner EDR魔力象限中排名第一，在这个成熟且竞争激烈的市场中取得这一地位，实属不易。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yVTwGeAlTUYfJiazZQVS7mkopaq1XzxqniaH3gH8icIZKj2CvRiaZ7NtTIA/640?wx_fmt=jpeg&from=appmsg)

其市值在全球网络安全公司中也仅次于Palo Alto Networks，超过800亿美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yqXlibt9S1P2aaoA4uBtgTj3GRXz7y7HYQeuDjxJrV7IXib80HZo5NiaXA/640?wx_fmt=jpeg&from=appmsg)

然而，中断事件发生后，股价从345.1美元跌至最低257.4美元，跌幅达25.4%。参考2月20日Palo Alto Networks在季报电话会上宣布加速平台化计划后股价暴跌的情况，五个月后的今天，其股价仍未恢复到当时的366.09美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cicjwWJEiaibIAlQ4ORNib0IbQkRTCNcCy2yN9RUnWy3NNSN8oDpicx2eLyHVH0f49N0xmJa3GvlpZvtyFhxSGAhl2g/640?wx_fmt=png&from=appmsg)

这次中断事件对CrowdStrike的影响是巨大的。网络安全行业对信任有着极高的要求，CrowdStrike通过多年的努力才建立了如今的客户信任和市场地位。然而，这次事件暴露出的流程问题对一家网络安全公司来说是致命的。要恢复用户的信任和股价，CrowdStrike需要付出加倍的努力，并且需要很长时间才能重新赢回客户的信赖。

### **内核空间和用户空间的争议**

EDR的功能包括监控系统进程、分析网络活动和记录文件操作等，为了有效实现这些功能，EDR必须在PC启动过程的初始阶段加载，并且运行在操作系统的内核中。内核级程序具有全面监控和拦截系统事件的权限，从而有效地检测和响应威胁。

相比 Linux 和 Mac，Windows对内核权限的管控更加宽松，这即是历史惯性，也是与监管机构反垄断纠缠的一部分。但从安全性的角度考虑，对内核空间加强限制是重要的技术手段。经过这次中断事件，估计会再次掀起一阵热议。

## **总结**‍‍‍‍

最后，总结几条启示：

1. **所有的分发都应该分阶段逐步进行，并做好监控和回滚机制。**
2. **配置文件的分发要参照代码分发来执行，配置文件如代码（Configuration file like code）。**
3. **不要自动化、对客户无感的推送更新，给客户特别是大型企业客户更多对软件更新的控制。**
4. **业务连续性计划必须要有，当IT系统崩溃时，如何减少对业务的影响，快速恢复需要什么资源和准备。**

**‍‍‍**

当类似事情发生在你的组织时，结果会不一样吗？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cicjwWJEiaibIATmZ0xv3e9LQCVI2fYEItFiaNZEVjk6BKRicPmaSGSfL6GuVTUoKfFXDxFX9XHzvGeuaTyDFF5ofEw/0?wx_fmt=png)

表图

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cicjwWJEiaibIATmZ0xv3e9LQCVI2fYEItFiaNZEVjk6BKRicPmaSGSfL6GuVTUoKfFXDxFX9XHzvGeuaTyDFF5ofEw/0?wx_fmt=png)

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