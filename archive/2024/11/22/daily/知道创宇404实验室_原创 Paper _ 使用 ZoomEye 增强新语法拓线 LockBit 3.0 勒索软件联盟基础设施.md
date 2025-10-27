---
title: 原创 Paper | 使用 ZoomEye 增强新语法拓线 LockBit 3.0 勒索软件联盟基础设施
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650989903&idx=1&sn=296cbc1537b959df28817c4f716e1348&chksm=8079a77db70e2e6bbc6c18ea795d634f873ef44141758d9a637b674fff5f5ed2b39b735568cd&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-11-22
fetch_date: 2025-10-06T19:16:35.232773
---

# 原创 Paper | 使用 ZoomEye 增强新语法拓线 LockBit 3.0 勒索软件联盟基础设施

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT1BLN0ME5NXtzJh11V9VkdNibUIAhl9mIGnmFakYKcWfZf1gIpuw97M8ypNCGH9VaguiaTHO7ElBfag/0?wx_fmt=jpeg)

# 原创 Paper | 使用 ZoomEye 增强新语法拓线 LockBit 3.0 勒索软件联盟基础设施

原创

404实验室

知道创宇404实验室

**作者：******知道创宇404实验室****

**时间：**2024年11月21日****

**1 摘要**

参考资料

LockBit 3.0 是一种知名的勒索软件，由网络犯罪组织通过“勒索软件即服务”（RaaS）模式运作。LockBit 3.0勒索软件联盟是使用该恶意软件进行攻击的独立黑客，他们以分成方式合作。这些成员利用 LockBit 提供的工具和基础设施，攻击各类企业和机构，窃取敏感数据并加密系统。LockBit 3.0 通过威胁泄露数据，逼迫受害者支付赎金。其主要目标涵盖金融、制造、医疗和航空等行业，包括2023年针对波音公司的一起重大攻击事件。

2023年11月21日，CISA发布了一篇LockBit 3.0的调查报告 [1] ，并公布了多个IOC。2023年11月24日，OSINT Team发布了一篇博文 [2]，基于CISA报告数据进行分析研究。

本文借助这两篇文章的IOC数据，利用ZoomEye网络空间搜索引擎 [3] ，使用ZoomEye平台新升级的增强新语法，基于"行为测绘"理念 [4]，针对最近一年时间内网络资产测绘数据进行多维度分析，拓展发现LockBit相关基础设施。

**2 概述**

参考资料

CISA关于LockBit 3.0调查报告中 [1]，第一个IOC表格中出现一个Teamviewer C2的IP地址"185.17.40[.]178"，该IP地址具有一个特殊的SSH指纹。OSINT Team的博文中 [2]，基于该IP地址进行了第一层拓线和数据分析。

这两份报告至今将近一年时间，我们基于最近一年时间内的网络资产测绘数据，仍然使用这个IP地址"185.17.40[.]178"为初始线索，进行第一层拓线和数据分析，进而以第一层拓线得到的IP结果作为基础进行第二层拓线，以期发现更多LockBit相关基础设施。

**3 第一层拓线**

参考资料

在ZoomEye平台上查询IP地址"185.17.40[.]178"，发现其22端口在2023年11月15日的测绘数据，其SSH指纹为：

```
3072 7a:9c:e1:27:43:ef:a8:cf:77:43:d4:ca:55:77:bc:6d (RSA)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSonNkrOhU44BGicFe0WfWq9IgtYuMdBBZKdA5G5gAdn7kDSzUC6ibYzwA/640?wx_fmt=jpeg&from=appmsg)图 1 ZoomEye搜索示意图

ZoomEye平台数据更新方式为覆盖式更新，该IP地址的22端口测绘数据时间显示为2023年11月15日，说明在2023年11月15日之后的某天，该IP地址的22端口服务被下线，且至今仍未恢复。推测是2023年11月21日CISA报告发布之后，攻击者便弃用了该IP地址服务器。

我们基于该SSH指纹，查询最近一年时间内使用过该SSH指纹的网络资产数据，使用如下的搜索语句进行查询，获取了109条结果。

```
"fingerprint: 3072 7a:9c:e1:27:43:ef:a8:cf:77:43:d4:ca:55:77:bc:6d (RSA)" && after="2023-11-06" && before="2024-11-05"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSmMBPSgnOUgI96PzMqyvh7J4diaIOj0khWVbuOicl7Ue26Yw70IFNfTVw/640?wx_fmt=jpeg&from=appmsg)图 2 ZoomEye搜索示意图

利用ZoomEye的聚合统计功能，看出这些IP地址的服务提供商主要集中在"M247"和"ARTNET"这两个，该现象与OSINT Team博文中 [2] 的描述是一致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSiahCFBRu9vL1rcJwaGSSuRCBSOUxHrOhIqj8HKbib3icoIEdpGjbibbicWA/640?wx_fmt=jpeg&from=appmsg)图 3 ZoomEye聚合统计示意图

我们查看这两家服务提供商的信息，Scamalytics站点将"M247 Europe SRL"标记为中等欺诈风险的ISP [5] ，将"Artnet Sp. z o.o."标记为低欺诈风险的ISP [6] 。这说明"M247 Europe SRL"服务提供商对应IP地址存在恶意行为，具有欺诈风险。

我们在VirusTotal上查询这109个IP地址的恶意情况，其中有43个IP地址检测为恶意IP地址，有53个IP地址标记为"LockBit 3.0"。

接下来，我们基于这53个标记为"LockBit 3.0"的IP地址进行后续的第二层拓线。

```
146.70.100[.]81
146.70.101[.]106
146.70.104[.]172
146.70.106[.]171
146.70.106[.]174
146.70.106[.]73
146.70.106[.]76
146.70.106[.]86
146.70.116[.]9
146.70.124[.]70
146.70.125[.]107
146.70.125[.]121
146.70.125[.]82
146.70.125[.]83
146.70.139[.]229
146.70.139[.]231
146.70.160[.]57
146.70.169[.]144
146.70.169[.]159
146.70.20[.]218
146.70.78[.]40
146.70.86[.]235
146.70.86[.]51
146.70.86[.]61
185.17.40[.]153
185.17.40[.]178
185.17.40[.]188
185.244.212[.]103
188.208.141[.]197
194.15.216[.]219
194.15.216[.]23
194.15.216[.]232
194.15.216[.]78
194.37.97[.]179
217.138.215[.]79
217.138.215[.]85
23.227.198[.]203
37.28.156[.]21
37.28.156[.]23
37.28.157[.]16
37.28.157[.]35
37.28.157[.]38
69.46.15[.]167
78.135.73[.]154
78.135.73[.]167
84.252.94[.]179
84.252.95[.]224
84.252.95[.]254
89.238.170[.]250
89.40.206[.]90
89.44.201[.]69
89.44.9[.]88
91.206.178[.]75
```

**4 第二层拓线**

参考资料

在ZoomEye平台上，使用批量搜索功能，上传包含这53个标记为"LockBit 3.0"IP地址的txt文件，如下图所示；然后将测绘时间限定在近一年进行查询，共计获取157条IP资产数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSKjemoCw9SHWSgRdL458Zo7zLdAna1CICZQwzsibFYElXd1GBNZSL0Bw/640?wx_fmt=jpeg&from=appmsg)图 4 ZoomEye搜索示意图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSQwiclEeX9dDGUPv97XnQ7hYYWbGicVmL70FhF0uQtX1TW3n7xibxNo4qw/640?wx_fmt=jpeg&from=appmsg)图 5 ZoomEye搜索示意图

#### **4.1 观察SSL证书指纹**

我们提取这157条IP资产数据中的SSL证书指纹，去重后总计有24个。

* 其中有20个SSL证书指纹是全网唯一的，在ZoomEye平台上仅能查询到一台服务器使用了该SSL证书指纹。这可以反映出恶意攻击者的谨慎，尽量不体现出"行为特征"，避免被安全研究员利用"行为特征"进行拓线发现更多基础设施。
* 其中有1个SSL证书指纹，在ZoomEye平台上可以查询到233793条数据，经过观察发现其是某系统默认配置证书。
* 剩余3个SSL证书指纹，在ZoomEye平台上仅查询到少量服务器在使用，疑似LockBit相关。下面，我们详细观察使用这3个SSL证书指纹的服务器信息。

##### **4.1.1 第一个SSL证书指纹**

SSL证书指纹是：

```
640D37DE9314BA0D6DFF8B029B0D2E2C19DED001
```

我们使用如下搜索语句进行查询：

```
ssl.cert.fingerprint=="640D37DE9314BA0D6DFF8B029B0D2E2C19DED001"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XS9wUmN5euthB3e3S0KVLvl777o3JZZMGArz1zUcwkQ43QhxPPkfIkwg/640?wx_fmt=jpeg&from=appmsg)图 6 ZoomEye搜索示意图

共计搜索得到7条结果，对应7个IP地址。其中1个IP地址146.70.106[.]86属于第一层拓线结果，我们拓展得到6个新IP地址。

```
193.108.4[.]76
185.62.57[.]11
145.0.6[.]14
20.242.52[.]93
54.163.53[.]159
66.109.142[.]164
```

我们观察这批IP地址，它们的"行为特征"非常一致：

* 开放443端口提供HTTPS服务
* 443端口上使用了相同的SSL证书，该SSL证书的Issuer字段和Subject字段均为空，具备一定的特殊辨识性
* 443端口的Banner内容相同：

```
HTTP/1.1 401 Unauthorized
Server: Microsoft-IIS/6.0
Date: Wed, 12 Sep 2012 13:06:55 GMT
Content-Type: text/html
WWW-Authenticate: NTLM
X-Powered-By: ASP.NET
Content-Length: 0
```

我们在VirusTotal上查询这6个拓展IP地址，发现均标记为恶意IP地址。
综上所述，我们认为这6个拓展IP地址极大概率和LockBit相关。

##### **4.1.2 第二个SSL证书指纹**

SSL证书指纹是：

```
5EDB0E19008FEAE8D487989FED4984ED299A565D
```

我们使用如下搜索语句进行查询：

```
ssl.cert.fingerprint=="5EDB0E19008FEAE8D487989FED4984ED299A565D"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XScg0fiaABAMVfrU4snV2rcQAWcWmPgU3QRZCfnib2vpNcDCLvHibIH1rpw/640?wx_fmt=jpeg&from=appmsg)图 7 ZoomEye搜索示意图

共计搜索得到3条结果，对应3个IP地址。其中1个IP地址146.70.106[.]171属于第一层拓线结果，我们拓展得到2个新IP地址。

```
94.103.183[.]224
185.80.91[.]150
```

我们观察这批IP地址，它们的"行为特征"非常一致：

* 开放443端口提供HTTPS服务
* 443端口上使用了相同的SSL证书，该SSL证书的Issuer字段为空，Subject字段均为CN=0.0.0.0，具备一定的特殊辨识性
* 443端口的Banner内容均为空

接下来，我们观察2个拓展IP地址在近一年时间内的网络资产数据，提取其SSL证书Subject字段、邮件服务Banner内容等网络资产数据中出现的关联域名，共计1个关联域名：tgekh.com

我们在VirusTotal上查询这2个拓展IP地址和1个关联域名，发现2个拓展IP地址没有标记为恶意，1个关联域名被标记为恶意。

综上所述，我们认为这2个拓展IP地址疑似和LockBit相关。

##### **4.1.3 第三个SSL证书指纹**

SSL证书指纹是：

```
949D2578B3E336F2AEAC1C8A92441C911084E53F
```

我们使用如下搜索语句进行查询：

```
ssl.cert.fingerprint=="949D2578B3E336F2AEAC1C8A92441C911084E53F"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0EWMdN8lVp4lmf8zaOib4XSaEibod4BxT4vu2jfp0ZibWHfm5ibX31GV1wpaNezcqibpYMlLuT9dxl2xA/640?wx_fmt=jpeg&from=appmsg)图 8 ZoomEye搜索示意图

共计搜索得到22条结果，对应18个IP地址。其中1个IP地址84.252.94[.]179属于第一层拓线结果，我们拓展得到17个新IP地址。

```
176.32.39[.]22
185.246.118[.]114
194.147.87[.]221
194.87.68[.]164
194.87.68[.]88
194.87.69[.]245
195.133.52[.]206
45.129.2[.]242
45.129.2[.]63
45.129.3[.]107
45.130.147[.]73
45.131.46[.]193
45.140.19[.]105
45.8.159[.]172
46.17.41[.]17
46.29.162[.]81
46.29.163[.]230
```

我们观察这批IP地址，它们的"行为特征"非常一致：

* 开放443或80端口提供HTTPS服务
* 443或80端口上使用了相同的SSL证书，该SSL证书的Issuer字段和Subject字段均为空，具备一定的特殊辨识性
* 443端口的Banner内容均为空
* 80端口的Banner内容绝大多数为空，仅2个IP地址例外

接下来，我们观察17个拓展IP地址在近一年时间内的网络资产数据，提取其SSL证书Subject字段、邮件服务Banner内容等网络资产数据中出现的关联域名，共计5个关联域名：

```
inforussia.org
konghuo.com.cn
romanet-alu.fr
lyufulreamagmalaw.site
hello.machine-from-china.com
```

我们在VirusTotal上查询这17个拓展IP地址和5个关联域名，发现其中有2个拓展IP地址和1个关联域名被标记为恶意。

综上所述，我们认为这17个拓展IP地址疑似和LockBit相关。

#### **4.2 观察SSL证书JARM**

我们提取这157条IP资产数据中的SSL证书JARM，去重后总计有23个。

其中22个JARM值的使用范围非常广，在ZoomEye平台上可以查询到很多IP地址使用了该JARM值的SSL证书；仅有1个JARM值使用范围有限，我们认为使用该JARM值的SSL证书可能是一个特征，因此基于这个JARM值尝试进行分析拓展。

```
00000000000000000043d43d00043de2a97eabb398317329f027c66e4c1b01
```

在第一层拓线结果的53个IP地址中，有6条网络资产数据使用了该JARM值的SSL证书，如下表所示。

表 1 6条网络资产测绘数据

| IP | PORT | Issuer | Subject |
| --- | --- | --- | --- |
| 84.252.94[.]179 | 80 | Blank | Blank |
| 91.206.178[.]75 | 31337 | CN=operators | CN=multiplayer |
| 185.17.40[.]153 | 8443 | Blank | Blank |
| 185.17.40[.]153 | 31337 | CN=operators | CN=multiplayer |
| 146.70.106[.]171 | 443 | Blank | Blank |
| 146.70.106[.]171 | 31337 | CN=operators | CN=multiplayer |

使用该JARM值SSL证书、开放31337端口、SSL证书Issuer字段值为"CN=operators"、SSL证书Subject字段值为"CN=multiplayer"是Sliver C2的默认配置。虽然不能将这些特征直接作为拓线依据，但我们可以与LockBit基础设施的其他确定特征相结合进行拓线。

上文章节中，我们知晓LockBit基础设施的服务提供商主要集中在"M247"和"ARTNET"这两家。因此，我们将上述特征与服务提供商为"M247"或"ARTNET"的特征相结合进行拓线，对应搜索语句如下：

```
jarm="00000000000000000043d43d00043de2a97eabb398317329f027c66e4c1b01" && port=="31337" && ssl="Issuer: CN=operators" &...