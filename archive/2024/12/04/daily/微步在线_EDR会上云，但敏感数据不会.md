---
title: EDR会上云，但敏感数据不会
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182607&idx=1&sn=77a3610f6772bacf564055095d15fd7d&chksm=f4486873c33fe165f47befc285e8854a31a7b3c9729e835c105d31c03f0ed6b83b3490e2a6e0&scene=58&subscene=0#rd
source: 微步在线
date: 2024-12-04
fetch_date: 2025-10-06T19:39:34.065000
---

# EDR会上云，但敏感数据不会

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZ85L5JkQQnfND9MKofoibZRPrJopDXaPhaxMJDE7vGSN1Myq5TRw07cg/0?wx_fmt=jpeg)

# EDR会上云，但敏感数据不会

原创

ThreatBook

微步在线

![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6iaBoFgqTpPricWCuX7uIb4Rj7eibLo3ibOiaOtqo7vXEnibKhxuInrceOoibg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

微步终端安全管理平台OneSEC推出以来，来自金融、央企、大型互联网企业等头部客户纷纷接受并认可 OneSEC 的安全云服务，充分体现了微步SaaS EDR的安全性和高可靠性（SaaS 部署占比超过95%）。

但在选择SaaS之前，EDR到底会采集哪些数据？这是每一个用户最为关心的问题之一。如果打开EDR的后台就会发现，EDR日志主要是操作系统底层行为，包括进程、账户、注册表、内存等。至于文件、应用内数据等涉及到敏感信息的内容，并不在采集范围之内。

尽管EDR能看到特定进程对特定文件和域名的操作，但在操作系统内部，进程只负责任务和资源的调度，并不能看到文件、聊天会话、网页以及其他应用内数据的具体内容。

**EDR只采行为数据**

在所有EDR原始行为日志中，大多数以进程为主体，即哪些进程执行了哪些操作，这主要是因为恶意活动一般都是通过独立进程或者利用白进程来承载，EDR通过观察进程行为就能够判断终端上是否存在恶意活动，而不需要直接采集文件和敏感数据本身。

而且过量的数据采集，只会给存储、传输带宽以及服务端的分析计算带来巨大的压力，导致EDR无法部署实施。

|  |  |
| --- | --- |
| **需要的数据（部分）** | **不需要的数据（部分）** |
| 进程行为：创建、句柄拷贝、挖空等 | 文件内容 |
| 文件行为：创建、访问、删除等 |
| 账户行为：登录、登出等 | 登录凭据、账号密码 |
| 网络行为：IP、域名 | 浏览器历史记录、访问凭据、网页内容等 |
| 内存行为：申请、属性修改等 | 聊天记录、应用内数据 |
| 注册表行为：创建、修改等 |  |

以OneSEC数月前检出的黑产团伙GanbRun钓鱼活动为例，来看EDR需要的数据类型。

木马运行后，进程“起诉材料和借款证据.docx.exe”加载了三个DLL，注入内存中执行恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZPtDKuF3yYNhaZ9t2cS0NU89DYKlMphdcH1a8Wj8gMAXphOcOMVoQfw/640?wx_fmt=png&from=appmsg)

“起诉材料和借款证据.docx.exe”尝试读取Edge浏览器文件，其目的为窃取敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZhBF6seqOIibf7FrzO8nwJeDowappSPp9PtMSicibibzlmA2keK3V6vh4Zw/640?wx_fmt=png&from=appmsg)

除上述基础行为外，随着攻击手法会不断翻新，恶意活动会表现出一些新的行为类型，例如修改内存的读写属性、加载内存执行、进程句柄拷贝、进程挖空等。

如图所示，进程gogogo.exe加载的DLL被挖空，使恶意代码可以隐藏在其中，逃避安全软件的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZyFicdHAP5XpuyOdnx2twDp1nAHicIic6aX4nkP8mv8Ol2o93dRXbRHpGA/640?wx_fmt=png&from=appmsg)

再例如攻击者通过WMI在远程计算机上创建一个进程，从而完成横向移动。如果只关注进程本身，很可能无法还原横向移动路径。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZ8K6lJ59891SfsfzVwzugibw12icP0BOvKk3hcTdvBYNcOboFkoeuzpiaw/640?wx_fmt=png&from=appmsg)

基于采集到的这些行为，就可以通过关联分析得到终端恶意活动的全貌。如下图所示，OneSEC还原了银狐木马恶意活动轨迹。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZeGv7RIDYBnBibK7KlPGCvI3xfiaDtkb2VgJibf94w7IbWibQSdGdIYWRMA/640?wx_fmt=png&from=appmsg)

**无法看到的敏感信息**

####

#### 尽管如此，EDR在观察进程的同时，难免会涉及到进程对上层应用和数据的操作。但在操作系统内部，进程只负责任务和资源的调度，并不能看到数据是什么。

具体包括以下三个部分。

**第一是EDR不会读取内部文件的具体内容。**

EDR采集的是进程创建、打开、重命名或者删除文件的动作，并不知道文件内容是什么，更不需要像杀毒软件那样采集文件进行特征匹配。

如图所示，当中招用户下载并解压钓鱼文件时，进程“WinRAR.exe”创建了一个文件。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZld7scXf7cfl2I7XEQXKNdr6Yc3dCZRnianRh1gFM6q3OD5iabulOib5KA/640?wx_fmt=png&from=appmsg)

不过EDR在采集文件行为时，可能会涉及到敏感文件名。OneSEC提供了特定关键词的文件名加密功能，确保采集到的是加密后的文件名。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZnQvgHickVqZomlc9fHvFciclf09xtYfqJLsJRu1gHz4wwI6l5cF07CeA/640?wx_fmt=png&from=appmsg)

**第二是EDR不会读取浏览器历史记录、访问凭据以及网页内容。**

浏览器历史记录、保存的密码和凭据等数据，通常会被存储在指令路径下，并不会体现在进程上。EDR只会采集是哪个进程读写了哪个文件，无法知道到底保存了什么内容。

尽管EDR会采集网络活动的日志，但也主要为浏览器进程外连的IP、请求的域名，用于检测是否存在反连C2的行为，并不关心网页具体内容和网页内操作。

如图所示，OneSEC检测到火狐进程在访问钓鱼域名，但看不到具体的网页内容。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZdThueom9MctkXJz4wRNQXZIrLafnoMia6QOuwujMlL9TibiamtFxCEnuQ/640?wx_fmt=png&from=appmsg)

**第三是EDR不会读取IM内的聊天信息。**

IM软件都会通过点对点加密传输，聊天记录也会加密存储在数据文件中，EDR无法读取。

同时，EDR采集文件创建是为了定位木马投递的路径，即是否来源于聊天软件；采集数据文件读写行为也是用于检测信息窃取行为。

如图所示，OneSEC检测到微信创建了一个木马并对其进行重命名，但文件内容是什么不得而知。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQQdPb0Yq2ibmFDOiab156sIZ7pzSKzfAP5iazck7Vj2fWgAnzHVE0HkswaHumpPywxqBUuzIMw50fVA/640?wx_fmt=png&from=appmsg)

####

**全面满足数据安全合规**

####

#### 尽管OneSEC可通过数据分析显著提高终端威胁可见性与对抗能力，但采集信息主要是操作系统层的进程行为，**不会外发内部文件以及IM、浏览器等应用内数据，满足EDR上云过程中的数据安全合规需求。并且OneSEC支持用户自定义数据采集类型，所有外发的数据有明确的字段可供查询**。

· END ·

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSA5A4iaspRVClFku4KVwkOUriclTaohLibE2oQKMTrQ8hvSFFHevq88eibd7mstuZbeNLm5U1tPJT3xQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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