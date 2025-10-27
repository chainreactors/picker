---
title: 威胁情报 | ADS 之殇，Confucius 组织利用 ADS 隐藏载荷攻击宗教相关人士
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988737&idx=1&sn=b8775b1bc9b159024497056a959eccf6&chksm=8079a2f3b70e2be551d85ccb0612acabd5ae1a8b983c7b0682ce397c437725eaceb1e8dd773e&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-26
fetch_date: 2025-10-06T18:29:37.181442
---

# 威胁情报 | ADS 之殇，Confucius 组织利用 ADS 隐藏载荷攻击宗教相关人士

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vS5H8ADFu3AjtuxZM8Hm9HeBJ7rV1znWAu435dP13s4Sy0J6S1jc0ib5g/0?wx_fmt=jpeg)

# 威胁情报 | ADS 之殇，Confucius 组织利用 ADS 隐藏载荷攻击宗教相关人士

原创

404高级威胁情报

知道创宇404实验室

**作****者：**知道创宇404高级威胁情报团队****

**时间：2024年9月25日**

**1.1 事件背景**

参考资料

近期，知道创宇404高级威胁情报团队在日常跟踪APT过程中发现了疑似Confucius组织针对某国宗教人士的攻击活动，攻击者通过宗教相关的诱饵诱使相关人员点击并加载最终的窃密木马。

此次攻击活动有如下特点：

1. 首次发现利用NTFS文件系统ADS(备用数据流)进行载荷隐藏，隐蔽性较高。
2. 利用windows系统文件fixmapi.exe侧载恶意载荷。
3. 继续使用特有C#木马WooperStealer进行文件窃取。

整个攻击活动杀伤链与Confucius近两年来的攻击极其相似，此类型攻击需提前关注，并加强防范。

**1.2 组织概述**

参考资料

Confucius组织（又称“魔罗桫”）于2016年被国外安全厂商披露，据悉最初的攻击活动可追溯到2013年。该组织主要针对南亚及东亚地区政府、军事等重要单位，近年来不断发现针对国内重点单位及行业发起攻击活动。

**1.3 分析描述**

参考资料

根据分析整体攻击链如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSp0tN3icTRSp2bN2VTY6e20SxUKtHa0H5h3fM2NiaxVxhP4iasMX141cibQ/640?wx_fmt=png&from=appmsg)

本次捕获的初始载荷攻击者利用NTFS文件系统数据流机制对恶意载荷和诱饵文档进行隐藏，正常使用WinRAR查看该压缩包只能看到其中的LNK文件。

若使用7Z对压缩包进行查看则能够发现其中包含2个备用数据流（ADS）。在NTFS文件系统中的每个文件至少有一个流，即其默认数据流，除此之外还允许添加一个或多个备用数据流，ADS最初的设定是存储主文件相关的修订信息等，此类信息在NTFS文件系统中默认是隐藏的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSZ0TORibrFh2eMTribLAfiaiaguermkGJJibgHm24RJtEtO9lsBQr27Me0Iw/640?wx_fmt=png&from=appmsg)

ADS在windows系统中即使是隐藏全开的情况下也是无法显示的，可以通过powershell命令进行流解析或者dir命令“\R”选项进行查看，图中的“Apple”和“Banana”即是攻击者附加的备用数据流：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSXLjORUicZpOnTnVuRhF35vRzgnJFHUq9Ug3L9cKuQ4qSc3j7QKlW3EA/640?wx_fmt=png&from=appmsg)

LNK文件指令参数解析如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSQ8kfS2ovxctfTs8pvnhAYaGbCw7fbiaG9HcJQFQWqEdB4vzsUcL0G8w/640?wx_fmt=png&from=appmsg)

指令的主要功能为：

* 查看主机是否存在“C:\Program Files\Avast Software”目录，若存在则后续文件复制到“'C:\ProgramData”目录，反之则复制到%appdata%目录下：
* 读取Banana文件流，并将其存储为%temp%\file.pdf，运行该文件。
* 读取Apple文件流，将其存储为“mapistub.dll”。
* 从系统目录将fixmapi.exe复制到mapistub.dll同目录，命名为“BlueApple.exe”并运行。

目前，在win10部分版本的powershell中“Get-Content xxx -Raw”解析的数据会失真，导致最终载荷运行失败:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSribgMbLicUaB6F5kcrezg7FJf5tvzqWfAy1Wtg6MaicdVMuicLyUzs2Ovw/640?wx_fmt=png&from=appmsg)

可以使用“Get-Content -Encoding Byte xxx”解析获取正确的载荷，以下分析均基于正确解析的前提下进行，例如解析后诱饵文档如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSiaFkslrpibtm308QVqTF0WrwDI2Zibr8SP04XU7dfguaFnCmClHNNYOfA/640?wx_fmt=png&from=appmsg)

### **1.3.1 mapistub.dll分析描述**

BlueApple.exe通过侧载的方式加载mapistub.dll，并运行其导出函数FixMAPI。

mapistub.dll是C#编写的dll文件，FixMAPI导出函数中攻击者在代码中添加了大量的无用代码，以此来将整体功能代码进行分割,加大分析难度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSicd7oibaWXXvevjeN3rFXq7ECKZKSJuDpbmj3VgHK2sspxbMAY5AQGCg/640?wx_fmt=png&from=appmsg)

硬编码的下载地址有addres和address2，实际上两个地址下载文件相同，攻击者用备用下载服务器的方式保证整个攻击活动的成功率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSRibcYdLz0ZEECKDibkicciaZuj8UVqfenzaaFoDM3cYSicx5wLZXr4RugMA/640?wx_fmt=png&from=appmsg)

从服务端下载的后续载荷依然是C#编写，加载执行其中的“Bsdfwiyersdkfh”方法。

### **1.3.2 wooperstealer分析描述**

由于最终C#窃密木马中屡次使用“wooper”字符，根据内部命名规范将其命名为“WooperStealer”，它使用与前一阶段downloader类似的无用代码将功能代码进行分割：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSlJuNDEHPKRXdAXHGatO6ZUgQz3rVMhfDkdcy3a4UyLGUFtWFB3Q23w/640?wx_fmt=png&from=appmsg)

获取主机名及用户名后利用“\_”进行拼接，最终作为参数拼接到URL后发送到服务端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vS4Hu9Jk8FMR8gibqIkiayaFobPk0FM5z2sD5C5xObib5wphLiaTVia74jFSQ/640?wx_fmt=png&from=appmsg)

收集指定文件夹下指定后缀文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSSKZvibXicV56mwM5kQqDHHaJmN5IiaBOQiaaE4GNpO6FbGTYyM7ibgAxYMQ/640?wx_fmt=png&from=appmsg)

将满足条件的文件进行上传，上传时的url格式为http://[Host]/VueWsxpogcjwq1.php?value1=[SerialNumber\_pcname\_username]&value2=[filepath dirname]，最终将上传文件的hash也同步回传到服务端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSjyQfB6NoIpkcfRXPDtJv2sAGTH8Dk3AOAj4KGlZ04lWGnwmmqGyk7A/640?wx_fmt=png&from=appmsg)

**1.4 归因及总结**

参考资料

Confucius在本次使用的攻击链相对于之前有些许变化，但最终加载运行的载荷是一致的，例如2021年国外安全厂商曝光的最终窃密木马与“WooperStealer”在代码逻辑及功能上几乎一致：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSLfXN80Momcic6vr8MjyLSIt3vx3uXEXP9cWQtHfmb8vEZn7CBqXlqIA/640?wx_fmt=png&from=appmsg)

在7月份捕获的该组织针对国内单位的攻击活动中，攻击者利用项目填报模板相关诱饵发起攻击：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vStV7qrPib8ZU8sCiaUEuxnEeE3qgzgYt5JRjeNI9gQlRGhK4zT9nZTMWQ/640?wx_fmt=png&from=appmsg)

在7月份的攻击活动中，初始载荷同样为RAR压缩包，其中利用的白文件以及最终载荷均相同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSxRw8Fj38t7FZdsLCFAJ2tGqcRp7ajfev45Thl5JdLgHIO9GDv4sBhw/640?wx_fmt=png&from=appmsg)

基于以上分析，我们基本确定本次攻击活动出自Confucius之手。从以往曝光的事件来看，暂未发现有APT组织通过ADS来隐藏攻击意图。从实际效果来看，ADS能够在一定程度上加大分析难度，同时能够避开一些基本的安全检测。

尽管本次攻击中可能因为系统版本导致攻击失败，但无法否认Confucius组织在攻击方面“付出的努力”。目前国内暂未发现相关的攻击样本上传，但不代表此类型的攻击活动未在国内进行，因此提醒广大的互联网用户，需要谨慎对待未知的邮件，特别是带有极强诱惑力的文档，要知道攻击者正是利用你的好奇心来诱导你落入其设下的圈套。

**1.5 IOC**

参考资料

Hash：

fd96ac431474ce6ba502f89a1d4f3bdaa182428a22aab15dd05483dd0b46de2d
f74820b855153c373ccb745852c551ea087e4376af761b2fffa1216ecfc2dc85
1ee756cd6608235454f0877c51881803d52c0887479838925b3caf4a976a17f0
23e8e162cce4228c34d5a0a7104d0908c194f1fa185b3f4279b3bf2958d27e13
4219db375e62680fb0de6ba35a1c4180d10e25ae0fe88fddd6f2b20e89cb4481

C2：

coldchikenshop29.info
greenearthtreeh.info
whitemissycorp.info

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT0Z79Hq9GCticVica4ufkjk5xiarRicG97E3oEcibNSrgdGSsdicWibkc8ycazhQiaA81j3o0cvzR5x4kRIcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**往 期 热 门**

(点击图片跳转）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2OVmxDyJicjufFMKd825S8D4EIWeBMuAAjJOibiahygyOfMhdQoK8SzCZ5WCyWzvm3gM66QyUGUr5cw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650985033&idx=1&sn=eb8264e9eb4f3dec90c22ecb464e5e9e&chksm=8079907bb70e196d58b310e5733e4c9cb0f7a6d4c4d51c3afeca35f73b14cbfc828e2d2afb95&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxltIJSd9MIY6u8ORKtZZNG0oxfmTK2Iuo7rgYc7ujXmqVWYbygYAYkcg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650984694&idx=1&sn=7ba5d62b933542ac64cecc692e8fc282&chksm=807992c4b70e1bd2f0588c7c9f865cc4200bce4a37f718e61a4d8c85eaaf9bd84e6498ad191a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GZ2mYNZYnqOD2pAicQctCmNHw5fre6QTGr4XJ0CJGqmEncGw9z0z7BYA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650986722&idx=1&sn=683cdf211094018be422a0e4ef628522&chksm=80799ad0b70e13c6ae3b436f74551c84a1d3d93e1653e6610787182e935d2238b33c9c8ab14c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT3XlD8Odz1EaR5icjZWy3jb8ZZPdfjQiakDHOiclbpjhvaR2icn265LYMpu3CmR1GoX707tWhAVsMJrrQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

戳“阅读原文”更多精彩内容!

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

知道创宇404实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

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