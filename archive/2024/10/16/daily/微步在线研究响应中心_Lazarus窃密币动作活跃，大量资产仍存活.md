---
title: Lazarus窃密币动作活跃，大量资产仍存活
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507123&idx=1&sn=c9291f0c483c9b5d318d48de92ba8987&chksm=cfcabfa7f8bd36b1123f50eaa3f7a780c4582653d39bef1e77a1b8c4984cfd5ebfe6306ef5e3&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-10-16
fetch_date: 2025-10-06T18:54:02.252017
---

# Lazarus窃密币动作活跃，大量资产仍存活

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsX7SicvHug2HvMITCEM7bM4ia1biaa3A2RjKIWLMTqGDicj7gItJibhIbh1g/0?wx_fmt=jpeg)

# Lazarus窃密币动作活跃，大量资产仍存活

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKJPlFpfWeI1jM5LD8DAWc6TwGmTv4yf8e0kcFZlNoATxCNglucjHY3BJOgh10SLuOaLsD0suJ52w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

**1**

**概述**

Lazarus是具有国家背景的东北亚APT组织，至少自 2009 年以来一直活跃。Lazarus攻击目标广泛，当前已发展为包含多个分支机构的复杂黑客团伙。区别于其他APT组织，Lazarus最常见的攻击活动目的为敛财。近十年间，Lazarus对加密货币领域一直保持高度兴趣。微步情报局发现，自Lazarus使用Python存储库PyPI投毒事件以来，Lazarus对于轻量级的python、Javascript武器库愈发青睐。虽然相关攻击事件已经多次被披露，但很多攻击资产依然大量存活。在朝鲜半岛区域政治局势更加紧张的当下，不排除Lazarus在今后更为活跃的可能性。

* Lazarus组织通过在社交平台发布密币相关的虚假招聘广告或相关项目引诱目标人员，目标人员上钩后，进一步引诱目标人员安装视频面试相关的带毒工具或带毒的密币项目，以此展开密币窃取活动。
* Lazarus组织该系列对加密货币领域的活动最早可追溯到2023年5月份，使用的武器库木马包括QT6平台开发的下载器，Python、Javascript木马，目标操作系统包括Windows、Linux、MacOS。
* 微步通过对相关样本、IP 和域名的溯源分析，提取多条相关 IOC ，可用于威胁情报检测。微步威胁感知平台 TDP 、威胁情报管理平台 TIP 、威胁情报云 API 、云沙箱 S、沙箱分析平台 OneSandbox、互联网安全接入服务 OneDNS 、威胁防御系统 OneSIG 、终端安全管理平台 OneSEC 等均已支持对此次攻击事件的检测与防护。

**2**

**事件详情**

# Lazarus组织在LinkedIn、X(Twitter)、Facebook、GitHub、Stack Overflow等多个平台发布加密货币相关的招聘或研究项目，以此物色目标人员。其中伪造的密币相关雇主网站Hirog.io当前依然存活。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCs5bj3fS0QPyRgatL6RzFia3jyCdLhzbyibrziaCNJspMdz7RpP81DzpYIw/640?wx_fmt=png)

Google快照可见多个历史招聘信息。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsicxuibUyicCLMMndV3NZwJfSeXzKpGQ0V1bw0JibGwpzLnl7ptZD8mlyLA/640?wx_fmt=png)

目标人员“上钩”后，攻击者通过telegram等通讯平台进一步引诱目标人员下载安装带毒的程序。基于Node.js的投毒MERN密币项目如下。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCseypZ8G96UVLjoUMpO6anWzS9bDz3yCyezrGmNNyRmhnOG3Z59uC9yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsaicOJPiagwEOiapOFlW9XNxhsIrJesiclVcu0muYniaCdfZibslPIGlZsk7A/640?wx_fmt=jpeg)

伪造的FCCCall视频会议软件如下，存在Windows和MacOS版本。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsQnnf0ulZhExtTmhx8L0L3wAFendYcBJuAsx7icq02yxib8rcQeZkpwKQ/640?wx_fmt=png)

目标人员安装带毒的项目之后，后台恶意代码机会下载安装后阶载荷展开窃密活动。

#

**3**

**样本分析**

# Lazarus诱导目标人员安装的带毒项目覆盖Windows、Linux、MacOS平台，后续使用的载荷多为轻量级的同类型python窃密木马，本文以Windows平台下“伪造FCCCall视频会议安装包的样本”为例进行分析。

|  |  |
| --- | --- |
| **文件名** | **FCCCall.msi** |
| MD5 | 8ebca0b7ef7dbfc14da3ee39f478e880 |
| SHA1 | 5cce14436b3ae5315feec2e12ce6121186f597b3 |
| SHA256 | 36cac29ff3c503c2123514ea903836d5ad81067508a8e16f7947e3e675a08670 |
| 文件类型 | MSI |
| 文件大小 | 152.37 MB |
| 描述 | 伪造的FCCCall视频会议安装包，密币窃取。 |

**1.**FCCCall MSI安装包如下，启动程序FCCCall.exe即初始窃密木马。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCs33szv3S3C7spDS71xOXCZGAu8fS9QHeNHp1IxMrvlyicVufNoWEeazg/640?wx_fmt=png)

**２.**木马采用QT6环境开发，通过指向freeconference.com的视频会议窗口掩盖后台恶意代码执行。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsH2P8AhoMJiaTlrkuFuzXl03l0ia1ibhyU7bOJ64pUwJn4ISsZYzdGLKnA/640?wx_fmt=png)

**３.**恶意代码初始化，C2（http://185.235.241.208:1224）、浏览器密币钱包扩展程序ID。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCs7lDEEThibicXcluRE1SmIZIPUaCJaf8EmRC90lKxiaeDNH1GZaRVVX0uw/640?wx_fmt=png)

**4.**根据默认的密币钱包扩展程序数据存储路径，窃取数据回传，URL：http://185.235.241.208:1224/uploads。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsiclXicUP753L0PpVH4CapRz2bQ5MpJ46cpPcxXeDFMblooeFZicT31b9g/640?wx_fmt=png)

**5.**此外，木马进行python环境下载、python client木马下载。

* http://185.235.241.208:1224/pdown -> python安装包；
* http://185.235.241.208:1224/client/99 -> python木马。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsKX6aIH94T8oTvfM68wavQ6iboE6UWQnd2ib0AkyoKZsXiczLVltzMD26g/640?wx_fmt=png)

**6.** http://185.235.241.208:1224/client/99 -> main99.py，下载的python载荷使用lambda函数进行多层嵌套的倒序、base64解码、解压缩处理得到最终python代码实体。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsVC48FECWosM6O019HdOcR8Iu1z0fbaKVhGdFmt4q6O5TsHz8zlH0eA/640?wx_fmt=png)

**7.**main99.py实际为下载器木马，下载三个后阶python木马分别实现远控、窃密、按键及窗口监控等恶意功能。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsYS6g7OBqkCaK3UbJ7Gt3xW3zj7kjvlcTA7IXkfEJuGm4hibhpaAO8icw/640?wx_fmt=png)

**8.**简要总结三个下载的python木马功能如下。

|  |  |  |
| --- | --- | --- |
| **URL** | **落地路径** | **描述** |
| http://185.235.241.208:1224/payload/99/root | %userprofile%/.n2/pay | 主机侦察、文件窃密、用户监控、shell，配置anydesk无人值守 |
| http://185.235.241.208:1224/brow/99/root | %userprofile%/.n2/bow | 针对主流的浏览器窃密 |
| http://185.235.241.208:1224/mclip/99/root | %userprofile%/.n2/mlip | 窗口监控、剪切板监控、按键记录 |

%userprofile%/.n2/pay主机侦察代码如下，攻击者侦察重点为加密货币相关。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsyITrOiaNQ0SDrR7WyPGTEJ2BElCARBzSJ1vojnWJhcm0wE8TfxqhhIw/640?wx_fmt=png)

使用下发的配置文件启用anydesk客户端对中马主机进行更为直接的远控。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsj3XWicOIvCA8db7wulCIyKywrxTbmmxkz7uGFaIGGbXWndmpaJP9M6A/640?wx_fmt=png)

使用多个python库用于窗口监控、进程监控、剪切板监控、按键记录。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsMgReLlFfyEliaVIUE7HnDUXBZn8jjQy0T9VLyiaNictH6iaxO47sx11atA/640?wx_fmt=png)

Python窃密木马适配Windows、Linux、MaxOS三大PC平台。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsS0H2IHMVbI5YxF3YXsvSEUu8XKbNWaeogqjiaE2tWXy1BpibQsqAFM1w/640?wx_fmt=png)

目标浏览器包括chrome、opera、brave、yandex、msedge五个常见浏览器程序。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCsLo2MGPqWYdgib58gHyMC7FsPE8FnGMGaB6Naa8PKOKACVJZl4A0rVhw/640?wx_fmt=png)

**9.** 核心的远控代码初始化如下，解析各类型指令功能如下表。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIEMNp2edmORaaibSFgpESCs6lwlq6VSasuXW79ZGJOGNzEzSoj6CdRArtRpCd8hER7pWOKDeqRs2A/640?wx_fmt=png)

|  |  |  |
| --- | --- | --- |
| **Index** | **代码符号** | **功能描述** |
| 1 | ssh\_obj | 执行shell |
| 2 | ssh\_cmd | 结束python进程 |
| 3 | ssh\_clip | 剪切板数据监控 |
| 4 | ssh\_run | 执行bow浏览器窃密木马 |
| 5 | ssh\_upload | 指定文件上传 |
| 6 | ssh\_kill | 结束目标浏览器进程 |
| 7 | ssh\_any | 启用anydesk远控 |
| 8 | ssh\_env | 匹配\*.env命名的主机文件，目标侦察 |

**附录-IOC**

135.181.242.24

140.99.223.36

144.172.74.108

144.172.74.48

144.172.79.23

147.124.212.146

147.124.212.89

147.124.213.11

147.124.213.17

147.124.213.29

147.124.214.129

147.124.214.131

147.124.214.237

166.88.132.39

167.88.164.29

167.88.168.152

167.88.168.24

172.86.100.168

172.86.123.35

172.86.97.80

172.86.98.240

173.211.106.101

185.235.241.208

23.106.253.194

23.106.253.209

23.106.253.215

23.106.70.154

23.254.244.242

45.140.147.208

45.61.129.255

45.61.130.0

45.61.131.218

45.61.158.54

45.61.158.7

45.61.160.14

45.61.169.187

45.61.169.99

45.89.53.59

46.4.224.205

67.203.0.152

67.203.123.171

67.203.6.171

67.203.7.163

67.203.7.171

67.203.7.245

77.37.37.81

91.92.120.135

95.164.17.24

blocktestingto.com

de.ztec.store

hirog.io

freeconference.io

ipcheck.cloud

mirotalk.net

regioncheck.net

b8e69d6a766b9088d650e850a638d7ab7c9f59f4e24e2bc8eac41c380876b0d8

36cac29ff3c503c2123514ea903836d5ad81067508a8e16f7947e3e675a08670

6a104f07ab6c5711b6bc8bf6ff956ab8cd597a388002a966e980c5ec9678b5b0

f474c840501076b1aceba06e1376cee142a7ff1fa642822f7592c92ae70578c2

6156127355d8016c8e741de98ee4ef2a4cb5cb02cd44f22fd3c8fef033b69830

5b70972c72bf8af098350f8a53ec830ddbd5c2c7809c71649c93f32a8a3f1371

6465f7ddc9cf8ab6714cbbd49e1fd472e19818a0babbaf3764e96552e179c9af

9abf6b93eafb797a3556bea1fe8a3b7311d2864d5a9a3687fce84bc1ec4a428c

7f1f51d216e621ed4fd9f5346044685a0e04c6a7fdd2c177f5d6233a67e2fd4e

000b4a77b1905cabdb59d2b576f6da1b2ef55a0258004e4a9e290e9f41fb6923

fca6351f0a913e3ca9df5cb0e0d5c0a05bcf580bcc57c4e858ee5378969430cd

dfb8c0525681d6fa8f65bbd62293c619a778f4080ebe29e41fe31b4f122000cf

94076a58c29d7e7f8b5f61739ab85ada09e41cd9212bc610b89e0fde30d5de70

bbad95905eb7a2b62685da98ba46aa3f19cb8a340ea71e5f85ee5b5a57aa27cb

247b10932d52c9a66ef073b7bc4461828081ffe07e06f6f20e4e32895acb61ba

6a104f07ab6c5711b6bc8bf6ff956ab8cd597a388002a966e980c5ec9678b5b0

6a104f07ab6c5711b6bc8bf6ff956ab8cd597a388002a966e980c5ec9678b5b0

6a104f07ab6c5711b6bc8bf6ff956ab8cd597a388002a966e980c5ec9678b5b0

8a23dd86da0aff9b460b8ebc9dd3e891d44ea0183ac...