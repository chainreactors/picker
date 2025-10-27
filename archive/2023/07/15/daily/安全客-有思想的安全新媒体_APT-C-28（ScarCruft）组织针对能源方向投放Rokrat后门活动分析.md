---
title: APT-C-28（ScarCruft）组织针对能源方向投放Rokrat后门活动分析
url: https://www.anquanke.com/post/id/289701
source: 安全客-有思想的安全新媒体
date: 2023-07-15
fetch_date: 2025-10-04T11:51:10.349901
---

# APT-C-28（ScarCruft）组织针对能源方向投放Rokrat后门活动分析

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

# APT-C-28（ScarCruft）组织针对能源方向投放Rokrat后门活动分析

阅读量**262888**

发布时间 : 2023-07-14 11:29:09

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

APT-C-28（ScarCruft）组织又名APT37（Reaper）、Group123，是一个来自于东北亚地区的境外APT组织，其相关攻击活动最早可追溯到2012年，且至今依然保持活跃状态。APT-C-28组织主要针对韩国等亚洲国家进行网络攻击活动，针对包括化学、电子、制造、航空航天、汽车和医疗保健等多个行业，其中以窃取战略军事、政治、经济利益相关的情报和敏感数据为主。

近期，360高级威胁研究院捕获到APT-C-28（ScarCruft）组织的一起以能源方向诱饵文件投递Rokrat后门木马的攻击活动，攻击者投递内嵌恶意代码和PDF文档的LNK文件，LNK文件运行后从第三方云服务中下载Rokrat后门注入到PowerShell中运行。Rokrat木马是APT-C-28组织武器化后门软件，Rokrat木马可具备获取计算机敏感信息、上下发文件运行、捕获屏幕截图和键盘输入等功能，且惯用云储存API实现后门指令和文件的下发。

**一、受影响情况**

攻击者以Sharara到Mellitah 石油管道信息向目标人员进行投递，该石油管道位于利比亚承担从利比亚Wadi al-Hayaa区到利比亚Nuqat al Khams区的石油输送任务。

**二、攻击活动分析**

**1.攻击流程分析**

完整的攻击流程如下：

![]()

2.恶意载荷分析

攻击者于LNK文件中填充了大量垃圾数据使得文件达到40MB+大小，并在LNK文件中内嵌诱饵PDF文档使用PowerShell对PDF文件进行落地并打开。

![]()

![]()

LNK文件运行后其中内嵌的恶意代码会从LNK文件中分别定位PDF文档和BAT文件数据先后将其落地到%temp%文件夹内执行。

![]()

BAT文件写入的是用于下载Rokrat主体文件的恶意代码。

![]()

恶意代码从OneDrive中下载Rokrat木马主体数据进行异或解密后将其加载至内存中运行。

![]()

释放的PDF诱饵文档。

![]()

扫描的文档经过标注增加诱饵文件可信度。

![]()

**3.攻击组件分析**

由OneDrive中下载执行的Rokrat木马与以往APT-C-28组织中攻击活动中所使用的基本变化不大。利用公共云盘进行指令通行、文件下发上传，获取计算机名称、用户名、BIOS、系统版本等敏感信息，以及通过判断vmtoolsd版本用来确定是否在虚拟环境。

![]()

攻击者在样本中搭载了pcloud、Yandex、Dropbox等三个云盘的API利用方法以及要使用的云盘token。

![]()

确认token有效后使用API从云盘指定目录获取后门指令信息用于攻击指令下发。

![]()

后门指令以及对应后门功能。

![]()

**三、归属研判**

此处捕获的Rokrat木马与以往披露的Rokrat版本变化不大，从文件命名、代码结构以及后门功能都变化不大。网络行为中更是沿用了以往惯用Content-Type信息。

![]()

**以往报告所披露的Rokrat木马中使用的Content-Type字段信息。**

![]()

**附录IOC**

85e71578ad7fea3c15095b6185b14881

4D3464B23DD4FB141C8FCC4CBF541832

7B7C43ED1EB6A423BDCFD0484FE560C3

2C180BF7A1E6DBE84060C3B5AA53FEB7（PDF）

4FE698C235D03A271305DB8FFDAA9E36（OneDrive下载密文）

https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBalFOTHZFRV9DVU9iUFdnLXhPZG8xRXFYckU\_ZT1BM1QwV2Q/root/content

**参考链接**

https://www.cisa.gov/news-events/analysis-reports/ar20-133d

https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/289701](/post/id/289701)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**7赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=169055)

[安全客](/member.html?memberId=169055)

这个人太懒了，签名都懒得写一个

* 文章
* **59**

* 粉丝
* **0**

### TA的文章

* ##### [ISC2023 生态大会：开拓“安全即服务”蓝海市场 共建数字安全新生态](/post/id/290454)

  2023-08-16 10:49:17
* ##### [见证开源力量：DSS 2023数字供应链安全大会成功举办](/post/id/290425)

  2023-08-16 10:41:33
* ##### [ISC 2023 XDR威胁检测与响应论坛成功召开，共议安全运营未来发展](/post/id/290407)

  2023-08-16 10:14:37
* ##### [ISC 2023能源数字化转型安全发展论坛召开，护航智慧能源安全](/post/id/290387)

  2023-08-15 14:32:01
* ##### [ISC 2023高级威胁狩猎分析论坛成功召开，聚焦数字时代安全新挑战](/post/id/290378)

  2023-08-15 14:21:28

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

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