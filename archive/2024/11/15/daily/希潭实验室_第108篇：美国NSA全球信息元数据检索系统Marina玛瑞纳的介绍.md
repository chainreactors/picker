---
title: 第108篇：美国NSA全球信息元数据检索系统Marina玛瑞纳的介绍
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247487200&idx=1&sn=c99c5c5ff6abe236a8a008f369d06531&chksm=c25fc19bf528488df83155a7d80826c791a8faa10d16dd0f0214736ab71e2e0a7681d1c06be6&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-11-15
fetch_date: 2025-10-06T19:20:14.092167
---

# 第108篇：美国NSA全球信息元数据检索系统Marina玛瑞纳的介绍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNojhuiaZtBersOxsrOTQOhedkyVSo90C9ibHOicZ2w1qPMiaRJibhNFtPYcw/0?wx_fmt=jpeg)

# 第108篇：美国NSA全球信息元数据检索系统Marina玛丽娜的介绍

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

## **Part1 前言**

**大家好，我是ABC\_123**。在前期的文章中多次提到美国NSA的量子注入攻击技术，相关情报工作人员会在互联网上可操作性的节点上筛查互联网流量，以寻找目标人物的元数据，包括邮箱地址、网站Cookie、用户ID等。一旦在Marina数据库中定位到目标用户的相关元数据，情报分析人员可以进一步深入分析，查找该用户的其他电子邮箱地址以及在其它网站的Cookie值，例如Facebook、Hotmail、LinkedIn、YouTube、Twitter等网站的记录；**获取目标的元数据信息越多，成功实施量子注入攻击的概率就越大**。然后，通过相关平台可以下发指令对其计算机进行利用，植入后门以获取其系统权限。

## **Part2 技术研究过程**

* ## **Marina系统的介绍与数据来源**

**Marina（玛丽娜）系统是一个元数据收集与检索系统，其数据主要来源于美国NSA在全球的各种流量监听系统，NSA分析员可以借助其检索功能勾画出个人画像**。美国NSA将几乎所有互联网用户的活动信息进行提取，生成元数据存储在该系统中，并可以创建各种分析图表，以便分析人员可以仔细研究。这些元数据包括在线社交网络、论坛邮箱及用户id、邮箱地址、网站Cookie、账单记录、保险信息、乘客清单、选民登记册、GPS位置信息、财产记录等。Marina系统可以查看NSA信号情报收集系统在过去365天的DNI元数据的能力，但电话通信的元数据并未包含在Marina中，存储在另一套系统**MAINWAY**中。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNiaiav9QQbx5UWw8ceNSs45cu2lPlmdfwjPlEyDUJ3FDVJscnkxI1z6PA/640?wx_fmt=png&from=appmsg)

Marina系统的数据主要来源于多个途径。首先是斯诺登曝光的Prism棱镜门计划，通过与主要互联网公司的法律强制“合作伙伴关系”运作，从而允许NSA在没有授权的情况下强制收集其流量内容和用户元数据信息；美国NSA还会从构成互联网支柱的光纤电缆中收集大量的元数据，对海底电缆进行窃听，**由于世界上大部分的互联网流量都经过美国，这使得NSA在监听数据时有了“主场优势”**；此外，还会从商业部门购买一些其他的数据信息，用来扩充Marina数据库的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNjo44PNPbWBS4sMahbkTz27msOQ80bvMLXZkfpiak3licy2eBTLz0o9icw/640?wx_fmt=png&from=appmsg)

* ## **Marina系统的基础知识**

**选择器“selector”**：在美国NSA的Marina系统中，“选择器”（selector）是用于识别和追踪目标的具体标识符。这些标识符可以包括电子邮件地址、电话号码、IP地址等数字痕迹。美国NSA的情报人员利用不同类型的选择器从海量数据中筛选和分析大量通信数据，以进行情报分析并维护国家安全。选择器帮助分析人员高效聚焦于相关数据，提高情报获取的效率和准确性。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNXKwcXyrC6GL4JnfCErEfsicgXJpQYHD368rj8fibG99R1rddto1rRz3A/640?wx_fmt=png&from=appmsg)

**选择器"selector"可以是多种数据类型，具体包括以下几种：**

**电子邮件地址：**用于识别和筛选特定用户的电子邮件通信。

**电话号码：**用于监控和分析电话通信。

**IP地址：**用于定位和跟踪特定设备或网络的互联网活动。

**用户名或社交媒体ID：**用于跟踪特定用户在社交媒体或其他在线平台上的活动。

**关键词：**用于扫描和过滤文本内容中的特定词语或短语。

**URL或域名：**用于监测访问特定网站或在线服务的行为。

**设备标识符：**如IMEI、MAC地址，用于识别和追踪特定设备。

* ## **Marina系统的检索追踪过程**

如下图所示，假设攻击对象是一家跨国公司的高管或者某位政要，其已知电子邮箱地址是test111@yahoo.com。首先需要收集到与目标人员相关的更多的选择器selector，以备可以更加准确过滤和识别目标的各种通信方式和网络活动，不遗漏任何相关的重要数据或者攻击事件，更好地绘制出目标的活动模式和社交网络，揭示隐藏的关系和目标的潜在意图或关联实体。情报分析人员可以使用Marina系统进行检索，**在系统中输入该邮箱地址作为“选择器/关键字”**，并指定检索时间范围为3个月，以查找与目标人员test111相关的其他“选择器”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNGUoBnZUHGAjiaJiatsIHPdzE21saNy8EmXmJErBLlAb7c7lcDf71p5Uw/640?wx_fmt=png&from=appmsg)

通过Marina数据库查询结果如下，“已知选择器（Known Selector）”是目标人物的雅虎邮箱地址test111@yahoo.com<yahoo>，**“New Selector”列出了与该邮箱地址相关联的Marina找到的其他“选择器”**，可以看到有一个输出结果是相关联的Gmail邮箱地址。如果想对Gmail选择器进行进一步检索，则必须与英国GCHQ 的同事合作，因为两国在此领域有合作协议。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNxyYxINpbtWlfpAlQvRZ3vwIZ4yVwKHb2ib13BOmgSYlam3lMFeQiahcQ/640?wx_fmt=png&from=appmsg)

如果“选择器Selector”有雅虎邮箱结果，可以点击“Machine ID”选项来获取该用户最近使用的<yahooBcookie>的值。这些标识符对于一台计算机通常是独一无二的，在不清空浏览器缓存的情况下，**该值可以揭示出在该计算机登录过的关联的其它的yahoo账号**。如果Marina查询结果出现多<yahooBcookie>值，可以直接查看最近的“Last Headrd”的值，该值越大，则用户的该值最有可能保持不变。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNB2b6Gxvc4s5NppAXfJcJY2XJ2trHLhUBWn6ZpVqDEVUic8LfkmwoicRA/640?wx_fmt=png&from=appmsg)

至此，通过Marina系统，情报人员查询到test111用户的3个选择器：test111@yahoo.com<yahoo>、test111-222@gmail.com<google>、xxxxxxxxxxxxx<yahooBcookie>。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNSjrWIUvDPjibO8hSzXbGTRKZRdvfXsicrEe49cSaYlYNzKgsdSHW6fKA/640?wx_fmt=png&from=appmsg)

对于前面查询到的“**新的<google>选择器**”test111-222@gmail.com<google>，可以继续尝试在Marina系统中查询该Gmail地址是否与其他账户相关联。需要注意的是，美国NSA的Marina系统在当时无法针对<google>选择器进行检索，需要结合英国GCHQ的资源。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwN2Pr9T1ib296shmxRguicEiaAEWDva7CHOJbucQvKfuibK4sTAyLCv4b3ibg/640?wx_fmt=png&from=appmsg)

具体查询方法如下，在Marina系统中，对该<google>选择器进行操作时,点击右键选择“Selector Profile”选项中的“Range”选项，会弹出一个对于“选择器”搜索的配置窗口。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNeR7Jz7EwWZBSyFQWsjPCNKpEaMgjnlzbX5IvAweIp3iacxl0OMxcU3w/640?wx_fmt=png&from=appmsg)

在配置窗口中，指定时间范围为过去3个月，然后点击“Submit”提交，Marina系统将开始查询。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNatDAobP47KBAf2SrCiaommEhiby33LQJUm6Ticg9iaujGFZ6bjAVrTuang/640?wx_fmt=png&from=appmsg)

查询完成后，可以查看Equivalent IDs页面的结果，“Entity B”列表给出了与该Gmail地址关联新的选择器：<yahoo>、<hotmail>、<yahooBcookie>。**通过重复上述操作可以继续查找与目标人员关联的更多的其他选择器**。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNSTtjiavAeeCiaq67WrOMxJTHYsbsNkW7FbNZazCkFSfnF0r4m4CialSCg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNECP8M5GO1PQXn7YnJ7HpmFAX2cV6MszcDWpj7YSsNplcHo4dhXSy0A/640?wx_fmt=png&from=appmsg)

如下图所示，情报分析人员一旦获取到与目标人员相关的选择器列表，可以通过Marina逐个分析每个选择器，以判断哪个更容易被量子注入攻击系统利用。我们需要检查这些选择器是否可以在美国的数据库系统中被识别，并且确认其是否处于活跃状态。为了进行进一步分析，在Marina系统的Web界面中选中“Active User/Presence（Federated）”，查询过去14天的记录，可以对Facebook ID这个selector选择器进行活跃用户搜索。**如果希望结合英国的GCHQ数据库进行检索，请勾选“Include Mutant Broth（All TDIs）”**。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNwHZMGRfdZtWT9OABPiaOowmV7zf30EiacuyBldkQdSn0ibjFqLvYcRVLw/640?wx_fmt=png&from=appmsg)

在使用Marina系统进行查询时，可能有返回结果也可能没有返回结果。重点是要看这些结果的SIGAD，并且判断该SIGAD是否可以实施量子注入攻击，从而最大可能获取目标机器权限。为了检查这些SIGADs是否能被NSA或者GCHQ量子系统利用，可以在浏览器中打开“GO QUANTUM”链接地址。查看Marina系统的结果并且注意每个活跃用户的最常见的SIGAD/IP CIDR。

如下图所示，选择器\*\*\*\*<yahoo>页面下可以看到量子注入攻击任务处理的状态：如果“tasked for survey”界面中的Technique的值为QUANTUMTHEORY或QUANTUMNATION，则目标系统已经被执行过攻击任务。**Last Attempt显示酸狐狸攻击平台上最后一次尝试量子注入攻击的时间，Fail表示攻击失败，success表示攻击成功**。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNDGk8nQD8ugmak6EkyYOF0kOeQYeK92TkVyFN1tZ3fHsZa9STibbhXvQ/640?wx_fmt=png&from=appmsg)

如下图所示，目标分析器会显示选择器\*\*\*\*\*<facebook>是否易受量子注入攻击。如果目标适用于QUANTUMNATION，目标分析器中将出现一个“Vulnerable to: Quantum”的URL链接地址。点击该链接即可发送电子邮件请求QUANTUMNATION任务的处理，接下来需要分析人员填一个表格，以备申请使用量子注入攻击平台对目标进行渗透。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNXUxaVcT7xEBaxEbCweg4uu9ccXQ4iacamkNyWSreaxbZibBHCvwc4DGw/640?wx_fmt=png&from=appmsg)

一旦获得授权对目标实施攻击，量子系统会在NSA监控的光纤电缆和路由器设备传输的数据包中，重点筛选包含目标电子邮件地址或Cookie的流量。系统会迅速发出警报，并确定目标正在尝试访问的网站。接着，激活Foxacid酸狐狸浏览器0day漏洞攻击平台，利用量子注入技术对目标进行攻击，使目标人员在毫无察觉的情况下访问来自NSA服务器的URL地址，在毫不知情的情况下，导致受害者浏览器被控。因此NSA不需要对目标发送大量的垃圾邮件，只需要等待目标任务访问特定的网站即可，一旦访问，系统会迅速将验证器后门植入目标计算机中，从此成为NSA的一个据点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450CaHQOEyEUu72hSTLPWMDwNQdFY53cHNzavmzzshJBws8Oa27STRd21xp8oH2F9dDVA6Rib8IeKXkw/640?wx_fmt=jpeg&from=appmsg)

**Part3 总结**

**1.**  该系统也可以与Xkeyscore配合使用，相互协作，共同检索个人信息。

**2.**  美国NSA还有其它的不同用途的数据库检索系统，如Mainway、Pinwale、Trafficthief等等，后续ABC\_123再详细给大家介绍。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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