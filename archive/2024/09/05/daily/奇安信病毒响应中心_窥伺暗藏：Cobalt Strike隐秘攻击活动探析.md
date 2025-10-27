---
title: 窥伺暗藏：Cobalt Strike隐秘攻击活动探析
url: https://mp.weixin.qq.com/s?__biz=MzI5Mzg5MDM3NQ==&mid=2247495801&idx=1&sn=8d50bb5244a4e73ea96abe445c660541&chksm=ec698051db1e0947fbabfda6122dff93f288257c994ef15a84e8906a732fb41a3cb3cc733e02&scene=58&subscene=0#rd
source: 奇安信病毒响应中心
date: 2024-09-05
fetch_date: 2025-10-06T18:26:57.584450
---

# 窥伺暗藏：Cobalt Strike隐秘攻击活动探析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3gFCRnusoN7quhTcEtfmj3cIoKScG92AOFFdEicf6abDJZcJ9adZFhDw/0?wx_fmt=jpeg)

# 窥伺暗藏：Cobalt Strike隐秘攻击活动探析

QAX病毒响应中心

奇安信病毒响应中心

**一、背景**

Cobalt Strike是一款内网渗透测试框架，简称为CS，它集成了端口转发、服务扫描、多语言平台木马生成、宏病毒生成等功能，同时提供比较丰富的钓鱼攻击方式。

因其比较全面的攻击测试功能，在攻防、测试中扮演着重要角色，同时也因其功能强大、使用人数众多和安全对抗的高度自由配置拓展，常常被用于真实网络攻击中，因此它被安全厂商重点关注，在很多的公开情报中提供了多维度的检测特征和方案。常见的检测方式大多分为基于内存/静态特征和基于流量检测两种，但相应的Cobalt Strike也提供了针对各种特征的免杀对抗措施，使得Cobalt Strike的对抗战争愈演愈烈。

**二、事件概述**

近日，奇安信病毒响应中心在日常分析运营过程中发现一类较为隐秘的CS样本，它们以诱饵压缩包的形式使用社交软件和SEO引擎进行投递，利用文件系统属性进行隐藏木马文件，动态解密加载多阶段python脚本执行，在流量侧也去除大部分已知流量检测特征。从各大安全厂商检测结果来看，它成功实现了一定程度上的免杀对抗，为此我们将此次攻击事件的过程做一次分享。

**三、攻击方式**

此次发现的诱饵样本主要通过Wechat社交软件和SEO搜索引擎等进行钓鱼攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3nXlcFwpiciaZj7zK7Ty5HXiaOZxsruCicgRBiaicvs1Y90txWfUMD2VYBFSw/640?wx_fmt=png&from=appmsg)

**四、攻击载荷**

|  |  |  |
| --- | --- | --- |
| **文件名** | **MD5** | **描述** |
| 岗位信息.zip | 91183BCB355887737F1F6F144F96492F | 诱饵压缩包文件 |
| 岗位信息.docx.lnk | 21721D3F4D38599AF3869FBCECD702FF | 启动快捷方式 |
| actiontech.py | 41E37957F2090E6F2454A1D797272980 | 启动脚本 |
| browser.py | 64B40F452EA0CE661A539DBA9C0D8880 | 浏览器渠道脚本 |
| china.jpg | 385A2271F65AEE4883A92EFB0A7DCE75 | 脚本负载 |
| bb.png | 3037A0124E516A12DA02C785848F97AC | 加密shellcode负载 |

**五、样本分析**

此次攻击活动主要特点在于隐秘。通过社交软件或SEO进行诱饵投递之后，压缩包包含的启动LNK伪装成DOCX文档文件;隐藏目录requests中FTP进程命令脚本伪装成DLL文件;启动的conhost.exe其实是python程序;核心的actiontech.py脚本也进行了混淆;从云服务器下载的第二阶段python脚本则加密伪装成了china.jpg；而下载的bb.png则是用于注入的加密Shellcode。简略攻击流程如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3qYrPVJ23mibls93xic4Icr2Oibqk8eLeicntCa5h37CfWxq8M23Qt1QuYg/640?wx_fmt=png&from=appmsg)

**（一）DownLoader**

首先攻击者向受害者投递诱饵文件，这些文件常常以“岗位信息.zip、后台BUG复现过程.zip、申请材料文档.zip、报错材料文档.zip、\*\*物业物流合作需求.zip”等诱导性名称的压缩包形式存在。普通用户如果直接解压缩文件，会发现原本大于6M的压缩文件，解压缩后却只有一个大小2kb的docx文档文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP33riafM6pibsS8ibkPF6Infw3oswymqGFmjpaCn90dpZKm6J3jNcRBKdMw/640?wx_fmt=png&from=appmsg)

那么，真实的文件又是什么呢？使用天擎客户端进行扫描，发现显示的docx文档其实是一个lnk快捷文件，而其隐藏目录中也包含了多达649个文件，同批样本中也有使用多层级隐藏目录来增加迷惑性的版本，如多级“\_\_Macosx\_\_”、“\_\_image\_\_”等。其实这是一种通过修改文件属性隐藏文件的技术，普通用户最好的方式是安装有查杀能力的安全产品进行防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3pmeZYPZ42Z7yA1S86sHfDRBicANXIuv6JtxnQtAIAbuGTtduW9Tgfgg/640?wx_fmt=png&from=appmsg)

伪装为docx文档的快捷方式实际是使用ftp.exe进程执行了隐藏目录下的脚本命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3qDEfRLGbkA11xGeAuWQI63XAOIib8awJzvHrYicJs72UNfrrmJ5UZRIA/640?wx_fmt=png&from=appmsg)

从lnk的目标中，我们也能猜到“requests\request.dll”也不是一个dll拓展，request.dll文件中使用“conhost.exe”执行了pyw文件，那么“conhost.exe”自然就是改了名的pythonw程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP36fILGXIdNqaJEg1NMtzPlcfISQC5ZYLlGvhdkOWodm0jhWmZ9icwQ0A/640?wx_fmt=png&from=appmsg)

“mainer.pyw”中只有一个import语句，导入了“actiontech.py”，而其主要功能是从云盘下载一个jpg文件后解密执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3yiajicibWHQnKPfrRmj1nqyNXyGyOaRwxWSDDkBTYDhde0afMyFNb8egQ/640?wx_fmt=png&from=appmsg)

“china.jpg”解密后主要功能是使用ctypes模块申请内存并执行从云盘下载的一段伪装成bb.jpg的shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3l2p5fYltqTcbNh5K2RFAEk2XV8d20UiapjmdBOV8o11mibI6ZHs9071Q/640?wx_fmt=png&from=appmsg)

**（二）Shellcode**

从上面解密的python脚本注释中猜测bb.png中可能是使用了base64和xor进行了加密，其实未注释加密代码的版本也被捕获到，而此次讨论的升级版本为了对抗将解密过程放在了shellcode中，并且在其它的变种中我们也监测到将ctypes模块相关代码又进行了多一层加密的样本，其不断演变的目的都是在试图逃避检测。其实从bb.png的数据中也可以发现一些疑似特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3FjYYEJb4k657g4Cp68ibv2DETOam9Bjtib4ErMfPlXySZXDrhlKYicwJQ/640?wx_fmt=png&from=appmsg)

在分析的过程中，也验证了我们的猜想，同时也可以看到shellcode在内存中的解密后的状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3icTcaKibG4qiarRGNytLwzd9C5hmk4rHnmmLnoibzicbEvhS1FDQL39CUSQ/640?wx_fmt=png&from=appmsg)

在完成解密之后，跳转到loader继续执行，程序首先会遍历寻找0x5941，然后寻找自定义E\_1fanew，最后通过shellcode目标长度范围内的0x4A51来结束循环，最终返回目标扩展地址，随后进行加载执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP39p57WicRX0fmyjiaBBpywbTU45AuBPQiasmCabIYuGF4XJd7V3mpooXIQ/640?wx_fmt=png&from=appmsg)

在shellcode运行过程中，会使用循环向不同服务器不断发送信息，请求static目录下的js文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3c6dRaBtOvtPUXSxZv0AB93915cCLCKqQOWYrwq6JpMvJXtzzn5YLkQ/640?wx_fmt=png&from=appmsg)

使用流量分析工具对其网络行为进行分析，在握手过程中，其SNI虽然显示了正常的前置域,但是其DNS响应中，包含了多个A记录和一个CNAME记录，且在类似心跳的频繁行为中，所使用的变化的前置域都是这种技术，CNAME属于同一家服务商。虽然这种行为无法确定其为域前置（Domain Fronting），但是通过其它分析技术我们最终确认其确实利用了域前置来隐藏真实的网络流量，以此绕过网络监控和审查，其真实访问host为“rjf56.com”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3Fo93lH05rEyH5cfoxsUZXLolsz51eic7qMic1UAQibvCTKbuEfAqOdclw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3VHxyEpzuJy2ic1OERZdP9xa5yVT9giaTQCuJM2uH8ZEQOfu4vIIZHWSw/640?wx_fmt=png&from=appmsg)

**六、溯源关联**

在木马运行过程中，天擎识别到攻击活动为Cobalt Strike。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3hLEhh07dUJJ5eymtxmACz5FtWUbicCgW79tJZMn6Uyhv3zrmLWSbAtQ/640?wx_fmt=png&from=appmsg)

使用天擎对解密后的shellcode进行扫描，识别到样本属于Cobalt Strike。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3ia33VyLzgAJ5EDP0iasOJTECZHt1fv3pxdI1iaTiaV20VF8hJK1DGI04NQ/640?wx_fmt=png&from=appmsg)

此次CobaltStrike利用攻击不仅使用了上述的自定义加载结构，而且修改了checksum8 、空证书、JA3/JA3S和DNS特征等，规避了大多数的安全检测特征，截至报告发布时，只有极少数的安全厂商能识别此样本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6vzicPmLEG3fnmcrEttsSaP3l87kFKmibbIvGWTfQIWb9pWnN1GGWLUZ8TosIN9FqJaNUVFzrVh9Adg/640?wx_fmt=png&from=appmsg)

**七、总结**

Cobalt Strike原是用于对手模拟和红队行动的商业软件，但因其具有全面而强大的功能，使得它被用于真实的网络攻击中，并且在各种渠道上充斥着多版本的破解版，进一步为其广泛的恶意使用提供了土壤；需要警惕的是，在攻防不断进化的情况下 ，Cobalt Strike也会不断更新对抗蓝队检测的技术，这也给真实网络攻击下的安全厂商不断提出新的挑战。

从本次的攻击来看，样本在一定程度上具有比较复杂的对抗策略 ，普通受害者一旦被攻击，很难靠自身常识发现其被感染和被控制的行为，这也形成了比较大的安全隐患。

**八、防护建议**

奇安信病毒响应中心温馨提醒用户，提高安全意识，谨防钓鱼攻击，切勿打开社交媒体分享和邮件接收的来历不明的链接，仔细辨别发件人身份，不随意下载和点击执行未知来源的附件，不以猎奇心理点击运行未知文件，不安装非正规途径来源的应用程序，如需使用相关软件，请到官方网站和正规应用商店下载。为了更好的防护自身免受感染侵害，可选择可靠的安全软件，同时保持系统和程序的更新。

目前，基于奇安信自研的猫头鹰引擎、QADE引擎和威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、奇安信天狗漏洞攻击防护系统、天擎、天机、天守、天眼高级威胁检测系统、奇安信NGSOC（态势感知与安全运营平台）、奇安信监管类态势感知等，都已经支持对此类攻击的精确检测。

**九、IOC**

|  |
| --- |
| **MD5** |
| 91183BCB355887737F1F6F144F96492F |
| 21721D3F4D38599AF3869FBCECD702FF |
| 41E37957F2090E6F2454A1D797272980 |
| 64B40F452EA0CE661A539DBA9C0D8880 |
| 385A2271F65AEE4883A92EFB0A7DCE75 |
| 3037A0124E516A12DA02C785848F97AC |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

奇安信病毒响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

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