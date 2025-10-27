---
title: 原创 | 真假顺丰官网，小心密码又被钓鱼！
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535607&idx=1&sn=55556fe209ba22156f9862333f85d987&chksm=fa93fd36cde4742085067211890ae0138236a2bca46f6f1bf0c6767686a51309e1f8833bbe38&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-21
fetch_date: 2025-10-04T10:09:38.907115
---

# 原创 | 真假顺丰官网，小心密码又被钓鱼！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzXCGDrjzRyOdRSSd9W8lrJ9eFaMqqibwc5dYzXujGeCSiatvA0mTTiaFWg/0?wx_fmt=jpeg)

# 原创 | 真假顺丰官网，小心密码又被钓鱼！

原创

CACTER邮件安全

网络安全应急技术国家工程中心

# 作者：CACTER邮件安全

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOz7ZeJrqR0icfSamrc6ia98L9W9RXzGs6WS40ke9HZHibqPKNL1Beww1T5g/640?wx_fmt=png)

# 日前，备受关注的旅日大熊猫“香香”，乘坐顺丰航空O37564全货机航班飞抵四川成都双流国际机场，随后被送往位于四川雅安的中国大熊猫保护中心。这次的“回家之旅”，不仅是顺丰航空首次执行大熊猫的运输任务，也是国内快递业首次服务大熊猫的跨境运输。

**作为国内领先的快递物流综合服务商、全球第四大快递公司，顺丰同时也是我国物流运顺的关键基础设施单位，长期以来成为黑产团伙重点攻击目标，近期，Coremail邮件安全团队发现，黑产团伙正大量使用不同的攻击手段组合假冒顺丰官方www.sf-express.com网站 进行钓鱼，套取用户密码。**

# **攻击案例1：html附件钓鱼**

#

本案例中钓鱼邮件攻击手法已由传统的正文+链接钓鱼转变为正文+html附件攻，黑产团伙通过对受害人发送【SF发票下载】主题的钓鱼邮件，引诱用户打开html附件套取密码。

由于这种方式钓鱼网站URL出现在正文中，黑产团伙尝试以此规避钓鱼URL检测。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzGljeicAQxxsMQmYosXoMNmQhLOJgbiaORXqFGvB3QGic7HIFtdhwpot9A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOz21wu5vcWJsnK5t3s3qD5Wpe4JEOSsGFa3w8cwSLHYBMbavNeyl9DTQ/640?wx_fmt=png)

打开HTML附件，受害者会进入黑产仿制的顺丰官网

针对此类威胁，Coremail邮件安全AI实验室现已将此类钓鱼邮件特征更新至反垃圾特征库，对此类威胁进行阻断，但不排除攻击者在近期使用类似的手法继续进行攻击。

对于该案例，Coremail也与中睿天下团队紧密协作，合作进行深度溯源，通过分析得知钓鱼链网址为

“hxxp://www.tsatcr.com/Eng/xG/SF/SF-Express/?login=xxxxxx.report@”，直接访问该域名得知此站疑似被控，未获得其它有用信息，附件详细信息及分析过程如下所示。

###### **(一）附件分析**

附件为一份名为“SF Outstanding Invoices”的html文件，该文件中主要是让收件人点击后访问“hxxp://www.tsatcr.com/Eng/xG/SF/SF-Express/?login=xxxxxx.report@”该链接。源码中的内容如图一所示。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzTNSibZeZ87rLpU8BXNiaZFWCdzoFj2Wsj4mZ7ZIic6L0UzwAo7ngl9acw/640?wx_fmt=png)

图一

附件源码中的网址为钓鱼页面，如图二所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzUYqfVNvGtiaU7XmQC3FCTfaHmTMib7PDNay0r63NHcSYBgdmA60XKCBg/640?wx_fmt=jpeg)

图二

（1）直接访问正文中链接的域名“hxxp://www.tsatcr.com”，该网站为正常的网站。如图三所示。说明攻击者利用失陷的正常网站搭建钓鱼网站页面。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzcON52BIctUWxQfvTJ0HZ1jx3BnQE3icMuv0A4asc182SkdPmvD07qVQ/640?wx_fmt=png)

图三

###### **(二）钓鱼邮件发信源IP分析**

(2）发信邮件服务器Ip为，79.141.164.176，ip归属地为荷兰 北荷兰省 阿姆斯特丹。此ip及发件的域名（inbox.0nnya.com）威胁情报标记为“垃圾邮件”。如图四所示。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzvDInKhticrU6ibyNd5Jepkq4e8aNDOKnGGI8vHHmeJIQCqias4HpHSkBA/640?wx_fmt=png)

图四

(3）邮件是由0时区发送至东八区。如图五所示。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzL58nTPLOib93VL32USfLraNT0owMu6PJoj5RoPsm6PAQmxP826YkuZA/640?wx_fmt=png)

图五

# **攻击手法2：仿冒顺丰官网进行链接钓鱼**

#

除了使用HTML附件攻击，Coremail安全团队也发现仿冒顺丰官网的链接钓鱼十分猖獗，如下图所示拦截的主题为：【SF快递到达详情确认】的链接钓鱼。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzLNjSGUzX5W9JibycCYLNNiaZ7GtOtUznmNorUGqtIdQMUic0s8vvhLssA/640?wx_fmt=png)

与传统链接钓鱼不同的是，该案例中钓鱼URL并不以超链接形式出现，而是以纯文本形式出现。黑产团伙引诱用户复制链接进入以下钓鱼网站，企图获取用户账密。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOztD5yHeLWVAFwf1WTcWNn3ftFXVWdSlqzG9ZhPaHamrBF0ELfbHeLAw/640?wx_fmt=png)

经中睿天下溯源分析邮件源码可以发现发送邮件的IP地址为198.252.107.103

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOznZwXs0u4TdicdeBpq6W8nKuZjlS6iaicyhCrynf24xaoziaXiawNMhiaicYYQ/640?wx_fmt=png)

查询此ip发现其归属地为中国/香港

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzavUW5hCymaKkTGupw3Fqiayd5NZ6r9FoLF3YTng0YfAlwT9NqRd5e1w/640?wx_fmt=png)

经初步判断此ip可能为攻击者的网络出口地址，或者代理转发地址。

对该ip进行开源情报查询，发现此ip被标注恶意

###### **(一）钓鱼链接分析**

邮件正文显示诱导链接为 https://nivandcc.ir/svedew/index.html

目前仍可以访问，页面预览如下：

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzv0ROic1nW5Ieic8uRJEElUbCGRVicm9xic31Ts8lcVl7Fcq6niamh4gCUjg/640?wx_fmt=png)

测试暂未发现此网站有跳转现象，解析此域名ip为195.201.55.155，

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOz7EQl8gF0arbL4WtDnnsf5FD2P3IcaPUJ204q7nlrFib895RG10HUA8w/640?wx_fmt=png)

查询此IP归属地点来自德国/萨克森自由州/法尔肯施泰因。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzbOSMx4YjAyvsHt0XjQuj5gq5aVqziaMIhDtfh7ZAl2m1ic5cE3SOuF4g/640?wx_fmt=png)

且查询此域名发现spf校验为软拒绝，即此域名可以伪造，该域名无可继续追溯价值。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzItNsEcmV8RneUegd7oxAA4tQEzicdYNVzFHm9FxFpLyeiaMiadNiaLCZ8g/640?wx_fmt=png)

根据开源情报发现该ip关联多个恶意木马程序，包括Emotet恶意软件木马病毒、Generic盗号木马等。

Trojan.Generic属于一种常见的盗号木马，启动后会从体内资源部分释放出病毒文件，有些在WINDOWS下的木马程序会绑定一个文件，将病毒程序和正常的应用程序捆绑成一个程序，释放出病毒程序和正常的程序，用正常的程序来掩盖病毒。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOz1znldptPctQFoiaFCS0KP7stKZ83UzoMQbQIurmiaicUDoC6QDnMeV8cg/640?wx_fmt=png)

Emotet是一种计算机恶意软件程序，最初是作为一种银行木马病毒开发的。其目的是访问外部设备并监视敏感的私有数据。Emotet 会骗过基本的防病毒程序并保持隐匿。一旦被感染，该恶意软件会像计算机蠕虫病毒一样传播，并试图渗透到网络中的其他计算机。Emotet 主要通过垃圾电子邮件传播。相应的电子邮件包含恶意链接或受感染的文档。如果您下载文档或打开链接，则其他恶意软件会自动下载到您的计算机上。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzn8icAB92eQSRmia68OatZE8bsXBicTDlXcbuGSibkHO4jbzicLhnwOlqRMg/640?wx_fmt=png)

判断该ip为攻击者购买使用国外服务器ip，该服务器开放995/pop3s、443、80等多个端口。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOz0WKDw3kh99lEh1z4iaSDR7XrbP6fT1eDxGFEy4ibbbibicxVPPWEdp9gzg/640?wx_fmt=png)

在此，CAC邮件安全与中睿天下提醒广大用户：

**1、不要轻易在可疑网站中输入个人身份证信息、银行卡号、密码。**

**2、提高警惕，切勿轻易点击邮件中的可疑链接/附件 或扫描二维码！**

**3、可选择使用邮件安全设备如Coremail邮件安全网关进行拦截防护。**

**4、加强意识安全教育，定期对全公司员工进行【反钓鱼演练】，并对公司重要岗位职工（财务、管理层）进行重点教育；**

**5、积极举报威胁邮件，携手共建邮件安全环境：举报邮箱:cac-team@coremail.cn。**

转载请注明来源：CNCERT国家工程研究中心

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

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