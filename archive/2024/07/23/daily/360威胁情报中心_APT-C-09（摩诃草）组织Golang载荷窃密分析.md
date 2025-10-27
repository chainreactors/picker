---
title: APT-C-09（摩诃草）组织Golang载荷窃密分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247500125&idx=1&sn=8a897b185a54ec0ce5b068e83bee2eed&chksm=f9c1f254ceb67b4212694ff7499c24a64fd88be63beb7080e92ba851ea9be965e3c6ea6a701c&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-07-23
fetch_date: 2025-10-06T17:46:02.320246
---

# APT-C-09（摩诃草）组织Golang载荷窃密分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7jSEZdhPo6AE8Z1dKBpianJF6mPqPdiaOBVOB6WnMp3tcvzpHRqTbSSUw/0?wx_fmt=jpeg)

# APT-C-09（摩诃草）组织Golang载荷窃密分析

原创

高级威胁研究院

360威胁情报中心

**APT-C-09**

**摩诃草**

APT-C-09（摩诃草）（又称白象、Patchwork、Dropping Elephant）是一个具有南亚国家背景的APT组织，长期针对巴基斯坦等周边国家进行网络攻击活动，以窃取敏感信息为主。尽管这些年该组织历史攻击行动及使用的攻击武器被国内外安全厂商多次揭露，但仍未停止其攻击，反而有越演越烈的趋势，一直处于活跃状态。

近期，360高级威胁研究院发现该组织针对巴基斯坦地区的攻击样本，并捕获到基于Golang的新载荷，这类攻击载荷在摩诃草的历史攻击中比较少见。此外基于后台大数据分析关联，我们还捕获到了该组织在同一时期针对同一地区散布Quasar工具进行窃密的行为。这两种攻击武器的交替出现，表明该组织针对同一目标不遗余力，并不断丰富和扩展其攻击武器。因此，在本文中我们将披露这些攻击组件，特别是Golang新载荷，以便对此类威胁有更深入的了解。

# **一、攻击活动分析**

## **1.恶意载荷分析**

本次攻击行动使用的钓鱼文件信息如下所示：

|  |  |
| --- | --- |
| MD5 | 0aa22fa3333c891a139187442ecf0e81 |
| 文件名称 | Quran.pdf.lnk |
| 文件大小 | 3.78 KB (3874字节) |
| 文件类型 | lnk |

该lnk打开时会调用powershell执行恶意指令。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7Xp3xptWAt0meeZV6Y1ibKAJy0Xiarib5aphTcpjQlGGd5o9uKv4rHFfTQ/640?wx_fmt=png&from=appmsg)

该指令的功能为下载诱饵文件（https[:]//quranchapter.t-cdn.org/wp-content/wp-includes/docaegeegrgseffefaa/22-Quran）和恶意载荷（https[:]//quranchapter.t-cdn.org/wp-includes/javascript/juicesdafekohioshfoshfhiofh/quran），并创建计划任务维持持久化。

部分诱饵内容如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7AdPJInlruuic9xu5PoAw50GmtRuUicv0AzAZSicykTOYhRTfOicYP55TkQ/640?wx_fmt=png&from=appmsg)

## **2.攻击组件分析**

lnk文件下载的恶意载荷信息如下：

|  |  |
| --- | --- |
| MD5 | 4f8bd643c59658e3d5b04d760073cbe9 |
| 文件名称 | Winver.exe |
| 文件大小 | 5.36 MB (5619472字节) |
| 文件类型 | exe |

Winver.exe是一个由Golang编译的恶意软件，并且带有数字签名“RUNSWITHSCISSORS LTD”，具体如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK71JAaQmOU9A1akibNZBamP4CnibEqy7je8XXfMIRZ781icBC4BibiaclZw7A/640?wx_fmt=png)

需要说明的是，我们捕获的Golang载荷除了上述签名外，还有个别样本签名为“COMPUTING AND CODING LIMITED”，其信息如下，该签名疑似被盗取，因此后续要提防此类签名信息的样本。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7f2MKrFbI1jtYvKlFLTvMGKhtDPLdeNGEfDvPAHLZ8liaibjQa63e2D0Q/640?wx_fmt=png)

另外查看Winver.exe文件的节发现存在.symtab段，.symtab是Linux系统写ELF文件格式的一部分，猜测该样本还有对应的ELF版本。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7eiawXtzJeHPNThwxricfoaaQHycXAX1D1GZeQSzt3OuVNZ9C44oRFRXg/640?wx_fmt=png)

Winver样本执行时先获取C2的硬编码值，接着对RC4的密钥和 User-Agent的值进行初始化。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7N1Lf4wTa9HUXgibhuIEcobuR34LFI8PN7xgkB8l9w7NbECRCkh7dZPw/640?wx_fmt=png)

然后使用wmic命令获取UUID的值，若获取失败，则随机生成。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7XzWBA7ujSqYXzMSaFWw0ibFPG5Rrkhaicz3J5cPBnZvLoibcictFDgrK2w/640?wx_fmt=png)

随后获取用户名、主机名、出口IP及国家代码、系统版本及架构、进程名和进程ID等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK72P7to8ENcn2PnRPYynH77PG8x5Uyrmoic1YnbKrdGP75tbhpfst9Vow/640?wx_fmt=png)

将获取的信息采用RC4+Base64的方式进行加密，并将Base64结果中的“+”替换成“-”和“/”替换成“\_”。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7jwibhAqMlia10k2MibHEE0UbEYrpVxFTe8k18AEOZ4HJGDycAP0qdErhw/640?wx_fmt=png)

将获取的基本信息进行拼接后采用post的方式发送到C2地址，此时HTTP请求头中用户代理设置为如下值“User-Agent:AGCYRNRWWWFZZSWWFWDYDCVDN”。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7icRgT8OjYt5eE6Qc55qQnaufb3DY3eudbtgt7mLLjO6D4WGuhajkR2A/640?wx_fmt=png)

当响应的状态码为“200”时，会读取响应数据进行解析解密，若指令为“suzckdwceefc”，则调用cmd进行命令执行，并将执行结果加密回传。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7ke7kWKdibuPB4fP3wD9t6r2oRDwzPSKWo6qQmHbibLohic2CQXqnQanKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7R79Nn8aFFPTibibJGVPQJrLsaP6ChJh96k8sibZ48Yo3ohjVwCicuxv2rg/640?wx_fmt=png)

若指令为“xlsvepfstvuv”，则使用开源库进行屏幕截屏。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7uNiboQ6b7PdOl03uibGYe4U7Ij5icT0WLoibUQ3jPSuzib0gZZ1sQweUhhA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7sE2NqP63zCZpxxia73iasvU58aFbWTcn3ktMzchnXWRyjFW0lD7WMvfA/640?wx_fmt=png)

# **二、关联分析**

基于后台大数据分析关联，我们还发现了该组织针对同一目标使用Quasar RAT的攻击行为。其样本信息如下所示：

|  |  |
| --- | --- |
| MD5 | 1154b7d8bd2e631f8fcd50a53d6173ba |
| 文件大小 | 238 KB (244,504 字节) |
| 文件名 | msedge.exe |

msedge.exe是一个Rust编译的用于内存加载执行最终载荷的加载器，通过使用更加底层的API函数，以创建线程的方式执行ShellCode，然后通过内存加载的方式，最终执行.Net载荷。此外我们也发现了通过NtQueueApcThread执行shellcode的攻击样本，该样本与msedge.exe只是shellcode执行方式不一致，其他均一致。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7xoBNdLxVoWicSoX0hvknYUeQpfqloCmdccL2ibjwVkcM5bJo3eGRnvbQ/640?wx_fmt=png)

最终载荷是一个被严重混淆过的C#程序，经过分析该载荷属于Quasar远控程序（https://github.com/quasar/Quasar），程序名为Client.exe，该远控程序也多次被摩诃草组织使用。

Client.exe首先使用Base64解码，以及AES-128的CBC模式解密基本的配置信息，如下表。

|  |  |
| --- | --- |
| ProjectName | Office04 |
| Version | 1.0.0.0 |
| rawHosts | 172.81.60.46:1005 |
| DirName | SubDir |
| FileName | Client.exe |
| Mutex | QSR\_MUTEX\_UCsz1CfvA68LlA0O2s |
| SchTaskName | Quasar Client Startup |

在解密配置信息之后，会根据用户类型的不同创建持久化，如果是管理员用户，就创建计划任务以及通过注册表HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run进行持久化，如果不是Admin用户，则只是通过注册表进行持久化。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7sicresK3VcLuFxngccSfEEMWibDrdZ5LJAW9BHfudLEoS3X1631wcloA/640?wx_fmt=png)

最后通过socket方式连接C2服务器，并通过事件方式用于接收数据以及执行对应的远控操作，具体远控指令如下。

|  |  |
| --- | --- |
| 指令 | 含义 |
| DoClientDisconnect | 断开连接 |
| DoClientUninstall | 卸载客户端 |
| GetProcesses | 枚举进程 |
| DoProcessKill | 杀死进程 |
| DoProcessStart | 创建进程 |
| GetDrives | 获取驱动器信息 |
| GetDirectory | 获取目录信息和文件信息 |
| DoDownloadFile | 下载文件 |
| DoUploadFile | 上传文件 |
| DoMouseEvent | 鼠标事件 |
| DoKeyboardEvent | 键盘事件 |
| GetSystemInfo | 获取系统信息 |
| DoShellExecute | 执行Shell |
| DoPathRename | 重命名 |
| DoPathDelete | 删除文件 |
| GetStartupItems | 获取启动项信息 |
| DoStartupItemAdd | 添加启动项 |
| DoStartupItemRemove | 删除启动项 |
| DoDownloadFileCancel | 下载文件管道 |
| DoLoadRegistryKey | 注册表检索 |
| DoCreateRegistryKey | 创建注册表键 |
| DoDeleteRegistryKey | 删除注册表键 |
| DoRenameRegistryKey | 重命名注册表键 |
| DoCreateRegistryValue | 设置注册表值 |
| DoDeleteRegistryValue | 删除注册表值 |
| GetScreenshot | 截图 |
| DoDownloadDirectory | 下载目录 |

**三、归属研判**

通过对样本整体分析，我们发现本次攻击行动与摩诃草组织之前使用的攻击手段相符合。

1.恶意lnk的参数及使用方式和恶意载荷所携带的签名“RUNSWITHSCISSORS LTD”都与我们之前关于该组织的报道一致[1]。

2.本次载荷通联C2中包含“b-cdn”、“t-cdn”等字符串，这类字符串经常出现在摩诃草组织以往C2中。此外多个C2服务器使用“Let’s Encrypt”颁发的免费证书，这与之前摩诃草的BADNEWS木马服务器也类似。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrHSjxhzVHGKgYgw0HbIWK7PepTrD8ENWU5XI8EUTVeeTA82u8YAOecBlANEgQkWbPgthjSw0LYzw/640?wx_fmt=png)

3.Golang新载荷使用RC4+Base64的算法，该类算法在该组织其他载荷中也被使用过。另外，针对同一目标使用的Quasar RAT之前也被披露过。

4.最后结合样本上传地址为巴基斯坦，符合攻击者目标，综上将其这类攻击归属于APT-C-09(摩诃草)组织。

#

##

**总结**

APT-C-09（摩诃草）组织从2013年被披露后，从未停止相关攻击活动，长期针对巴基斯坦等周边国家进行攻击，在最新的攻击样本中，我们观察到该组织使用Golang编写的后门载荷，以及使用Rust编写的加载器加载Quasar的攻击组件，这都进一步揭示了其在不断演进和提升技术水平的过程中，还在积极地扩展其攻击武器，以更好地适应网络安全防御的不断升级。

在这里提醒用户加强安全意识，切勿执行未知样本或点击来历不明的链接等操作。这些行为可能导致系统在没有任何防范的情况下被攻陷，从而导致机密文件和重要情报的泄漏。

#

**附录 IOC**

#

**MD5:**

0aa22fa3333c891a139187442ecf0e81

4f8bd643c59658e3d5b04d760073cbe9

dfb97438f0ec94e78a2a1e3d32bc11d5

13dcd6f1fd44f7f15651153167b646cc

1154b7d8bd2e631f8fcd50a53d6173ba

**C&C:**

https://quranchapter.t-cdn[.]org/wp-includes/javascript/juicesdafekohioshfoshfhiofh/quran

https://ruz98.b-cdn[.]net/22

https://daily-mashriq[.]org/goyxdrkhjilchyigflztv

https://espncrics[.]info/goaimdzfecbgrjjxdamdoo

172.81.60[.]46:1005

**参考**

[1]https://mp.weixin.qq.com/s/SAt5NU-hCbS0D6jI8gkkFQ

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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