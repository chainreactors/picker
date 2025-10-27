---
title: Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532601&idx=3&sn=395c0027e1cc56e09658e1ee7f2a5f5e&chksm=fa93f6f8cde47feed619f8937f14ffb2236ef6bc886ede806fb76ced776fc54f88453597a309&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-10
fetch_date: 2025-10-03T22:15:33.291747
---

# Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nAgNjibOxsNqZsMMOIIXF6XYHxRUYKfCemnr4zY1PDePRLTFmJtb8ILR10Z6QcgycFWd5QNPAzoOw/0?wx_fmt=jpeg)

# Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176nAgNjibOxsNqZsMMOIIXF6XIpkTX4XarR6Gjz5OIxT0CXgZIeLW4jibmxDXPJthiaCMkF6aInX5c0UQ/640?wx_fmt=png)

在基本上销声匿迹了近五个月之后，臭名昭著的Emotet恶意软件团伙再次大肆发送恶意电子邮件。

Emotet是一种恶意软件，通过含有恶意Excel或Word文档的网络钓鱼活动来感染系统。一旦用户打开了这些文档并启用宏，Emotet DLL就会被下载并加载到系统内存中。

一旦被加载，该恶意软件就会搜索和窃取电子邮件，用于将来的垃圾邮件活动，并投放额外的攻击载荷，比如Cobalt Strike或通常导致勒索软件攻击的其他恶意软件。

虽然Emotet过去被认为是传播最广的恶意软件，但它在2022年6月13日却突然停止发送垃圾邮件。

**Emotet卷土重来**

Emotet研究部门Cryptolaemus的研究人员报告称，大约在美国东部时间11月2日凌晨4点，Emotet团伙突然重新活跃起来，向全球的电子邮件地址发送垃圾邮件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrW8oocVFJDC2v3IOZfnWqFYAAwer6yic6wKiaicztJod0us6KaZoXVclQcg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1

Proofpoint的威胁研究人员、Cryptolaemus的成员Tommy Madjar告诉IT安全外媒BleepingComputer，今天的Emotet电子邮件活动使用窃取的电子邮件回复链来分发恶意的Excel附件。

BleepingComputer从上传到VirusTotal的样本中看到了以不同语言和文件名称针对全球用户的附件，假装是发票、扫描件、电子表格及其他诱饵。

下面列出了示例文件名称的部分内容：

Scan\_20220211\_77219.xls

fattura novembre 2022.xls

BFE-011122 XNIZ-021122.xls

FH-1612 report.xls

2022-11-02\_1739.xls

Fattura 2022 - IT 00225.xls

RHU-011122 OOON-021122.xls

Electronic form.xls

Rechnungs-Details.xls

Gmail\_2022-02-11\_1621.xls

gescanntes-Dokument 2022.02.11\_1028.xls

Rechnungs-Details.xls

DETALLES-0211.xls

Dokumente-vom-Notar 02.11.2022.xls

INVOICE0000004678.xls

SCAN594\_00088.xls

Copia Fattura.xls

Form.xls

Form - 02 Nov, 2022.xls

Nuovo documento 2022.11.02.xls

Invoice Copies 2022-11-02\_1008, USA.xls

payments 2022-11-02\_1011, USA.xls

今天的Emotet活动还采用了一个新的Excel附件模板，其中含有绕过微软受保护视图（Protected View）的指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrWQeUbV7QgE2WZMnkhSJ6hegahunjfJ2bpFe3ia0jx2o0aSDkOkETtn8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2. 恶意Emotet Excel文档（来源：BleepingComputer）

当一个文件从互联网上下载时（包括作为电子邮件附件），微软就会为该文件添加一个特殊的Web标记（MoTW）标志。

当用户打开含有MoTW标志的Microsoft Office文档时，Microsoft Office会在受保护视图中打开它，以防止执行安装恶意软件的宏。

然而，在新的Emotet Excel附件中，您可以看到威胁分子在指示用户将文件复制到受信任的“Templates”文件夹中，因为这么做可以绕过Microsoft Office的受保护视图，即使是含有MoTW标志的文件。

"RELAUNCH REQUIRED In accordance with the requirements of your security policy, to display the contents of the document, you need to copy the file to the following folder and run it again:

for Microsoft Office 2013 x32 and earlier - C:\Program Files\Microsoft Office (x86)\Templates

for Microsoft Office 2013 x64 and earlier - C:\Program Files\Microsoft Office\Templates

for Microsoft Office 2016 x32 and later - C:\Program Files (x86)\Microsoft Office\root\Templates

for Microsoft Office 2016 x64 and later - C:\Program Files\Microsoft Office\root\Templates"

虽然Windows会警告用户将文件复制到“Templates”文件夹需要“管理员”权限，但用户试图复制文件这一事实表明，他们很有可能也会按下“继续”按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrWYjGSic1c6OCH7SQOx8z7rrZfZJGw4wFQOA8VyRibia0lh59u986VQsI1w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3. 请求管理员权限（来源：BleepingComputer）

当附件从“Templates”文件夹启动时，它会直接打开，并立即执行下载Emotet恶意软件的宏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrWyQZjchbo2yshjicE15iceo1lThNgxaVMnCicXbeBEibzHLlJCLxVa7EGxQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图4. 绕过Microsoft Office受保护视图（来源：BleepingComputer）

Emotet恶意软件以DLL的形式下载到%UserProfile%\AppData\Local下的多个随机命名的文件夹中，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrWbmoiaEDYLke1BVwGB0I4nUEbOBBjoricstbebH77A4MpNDvlGBDjwzxA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图5. Emotet存储在%LocalAppData%下的随机文件夹中（来源：BleepingComputer）

然后宏将使用合法的regsvr32.exe命令启动DLL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29o6Y1I74J3rIWCibcbVJDrW1zprw3jA0mgl4j6c7097fazxJ9Fuk91FkFsbiajJWCGD2jJoxJ4CTJw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图6. 通过Regsvr32.exe运行的Emotet DLL（来源：BleepingComputer）

一旦下载，恶意软件将在后台悄悄运行，同时连接到指挥和控制服务器以接收进一步指示，或安装额外的攻击载荷。

Madjar告诉BleepingComputer，今天的Emotet感染活动还没有开始在受感染的设备上投放额外的恶意软件载荷。

然而在过去，Emotet因安装恶意软件TrickBot、最近安装Cobalt Strike信标而臭名远扬。

这些Cobalt Strike信标随后被勒索软件团伙用于获得初始访问权，这些团伙在网络上横向传播，窃取数据，并最终加密设备。

Emotet感染在过去被用来让Ryuk和Conti勒索软件团伙初步进入企业网络。

自6月份Conti关闭以来，Emotet被认为与BlackCat和Quantum勒索软件团伙相勾结，以获得已经被感染的设备的初始访问权。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/emotet-botnet-starts-blasting-malware-again-after-5-month-break/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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