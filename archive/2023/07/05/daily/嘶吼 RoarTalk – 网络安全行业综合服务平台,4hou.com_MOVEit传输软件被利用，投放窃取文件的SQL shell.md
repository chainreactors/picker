---
title: MOVEit传输软件被利用，投放窃取文件的SQL shell
url: https://www.4hou.com/posts/wykz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-05
fetch_date: 2025-10-04T11:53:10.303927
---

# MOVEit传输软件被利用，投放窃取文件的SQL shell

MOVEit传输软件被利用，投放窃取文件的SQL shell - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# MOVEit传输软件被利用，投放窃取文件的SQL shell

布加迪
[新闻](https://www.4hou.com/category/news)
2023-07-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124624

收藏

导语：我们在这篇文章中提供了攻击链的技术细节，以及可用于扫描MOVEit传输漏洞是否可能被利用的狩猎查询和PowerShell脚本。

SentinelOne发现MOVEit文件传输服务器应用程序中的CVE-2023-34362漏洞遭到了野外（ITW）攻击。该攻击投放Microsoft IIS .aspx恶意载荷，使受影响的Web服务器和连接的Azure blob存储之间的交互受到限制。6月5日，Cl0p勒索软件组织声称对这些攻击负责，不过SentinelOne特别指出，针对文件传输应用程序漏洞的攻击与2023年初以牟利为目的的攻击者进行的其他攻击相似。

我们在这篇文章中提供了攻击链的技术细节，以及可用于扫描MOVEit传输漏洞是否可能被利用的狩猎查询和PowerShell脚本。

**概述**

在2023年5月的最后一周和6月初，SentinelOne观察到运行Progress Software的MOVEit Transfer文件服务器应用程序高危版本的Windows服务器被大肆利用。攻击投放了一个精简的webshell，攻击者可以使用它来泄露文件的内容，包括当受攻击的MOVEit实例被配置为使用Azure的blob存储服务时，托管在Microsoft Azure中的文件。6月5日，Cl0p勒索软件组织声称对这些活动负责。

虽然利用漏洞可能是伺机作案，但SentinelOne观察到下列行业的20多家组织受到了攻击，其中最频繁受到影响的是托管安全服务提供商（MSSP）和托管信息技术服务提供商（MSP）：

航空、运输与物流

娱乐

金融服务及保险

医疗保健、制药和生物技术

托管信息技术服务供应商（MSP）

托管安全服务提供商（MSSP）

制造业及建筑材料

机械工程

印刷和数字媒体

技术

公用事业及公共服务

漏洞影响以下版本的MOVEit Transfer：

MOVEit Transfer 2023.0.0：在2023.0.1中已修复

MOVEit Transfer 2022.1.x：在2022.1.5中已修复

MOVEit Transfer 2022.0.x：在2022.0.4中已修复

MOVEit Transfer 2021.1.x：在2021.1.4中已修复

MOVEit Transfer 2021.0.x：在2021.0.6中已修复

**技术细节**

这些攻击是针对运行MOVEit文件传输应用程序高危版本的Windows服务器进行的，攻击者可以通过端口扫描或Shodan等互联网索引服务来识别高危目标。

Progress Software最近发布了一份安全公告，详细介绍了MOVEit Transfer中的一个漏洞，该漏洞可能会导致特权升级和对目标环境的未经授权访问。该公告将此问题详细描述为SQL注入漏洞（CVE-2023-34362），该漏洞允许未经授权的攻击者注入SQL命令，并从目标数据库获取信息。

攻击链利用该漏洞通过moveitsvc服务帐户将任意文件上传到服务器的\MOVEitTransfer\wwwroot\目录。系统的svchost.exe进程启动w3wp.exe，这是微软Internet信息服务（IIS）worker进程，然后将几个文件写入到Temp中的新工作目录。该工作目录和后续文件共享相同的8字符伪随机命名语法，其中一个示例写入以下文件：

C:\Windows\Temp\royq2cir

C:\Windows\Temp\royq2cir\ royq2cir.tmp

C:\Windows\Temp\royq2cir\ royq2cir.0.cs

C:\Windows\Temp\royq2cir\ royq2cir.dll

C:\Windows\Temp\royq2cir\ royq2cir.cmdline

C:\Windows\Temp\royq2cir\ royq2cir.out

C:\Windows\Temp\royq2cir\ royq2cir.err

w3wp.exe进程启动csc.exe将C#代码编译成恶意载荷，恶意载荷保存为human2.aspx。恶意载荷是一个精简的webshell，用于查询有关数据库配置的信息，使攻击者能够执行以下操作：

连接到指定的SQL数据库，

泄露由MOVEit Transfer托管的文件内容。

当MOVEit Transfer连接到Azure blob存储时，泄漏Azure blob存储服务中特定文件的内容。

为了泄露文件，攻击者可以在向webshell发出请求的HTTP头中指定目标对象的File ID和Folder ID。然后shell在服务器的HTTP响应中以Gzip对象的形式返回指定文件的内容。shell还删除名为“Health Check Service”的现有用户，并使用相同的用户名创建一个新用户，这可能是为了持久潜伏。

截止本文发稿时，SentinelOne尚未观察到部署webshell后的后续活动。

**缓解和预防**

使用MOVEit Transfer的组织应立即升级受影响的系统。在无法执行升级的情况下，应该使系统脱机，直到可以升级为止。确保你的安全团队可以访问和分析运行MOVEit Transfer的服务器上的应用程序日志，包括Microsoft IIS日志。

由于攻击者是通过与MOVEit Transfer在应用程序层面的交互来利用漏洞的，因此端点检测与响应（EDR）工具的检测机会仅限于后期活动。SentinelOne特别指出，每个恶意载荷在运行时都是动态编译的，因此每个受害者都有一个唯一的哈希值。虽然我们提供了与通过这些活动投放的恶意载荷相关的哈希列表，但组织不应该仅依赖哈希来检测这些攻击。

我们建议运行MOVEit Transfer的组织使用下面提供的资源进行威胁搜索和日志分析。

**狩猎查询**

SentinelOne提供了以下查询，组织可以用来狩猎与这些攻击相关的活动。虽然这些查询不一定覆盖所有攻击场景，但结果应该已进行调查和分类。此外，防御者应该寻找由MOVEit Transfer服务帐户发起的异常活动：默认值是moveitsvc，不过有些实例可能具有自定义帐户名称。

|  |  |
| --- | --- |
| 查询 | 描述 |
| S1QL:   SrcProcName = "w3wp.exe" AND  TgtProcName   = "csc.exe" AND SrcProcCmdLine  Contains   Anycase "moveitdmz pool" | 识别编译与MOVEit应用程序池有关的DLL的情况 |
| S1QL:   IndicatorName =  "LoadUnreleatedLibrary"   AND  IndicatorMetadata   Contains "w3wp.exe" AND  SrcProcName   StartsWith "DMZ" | 识别IIS worker进程的潜在异常库加载 |
| S1QL:   EventType In ("File Creation", "File  Modification")   AND SrcProcName Contains  Anycase   "w3wp.exe" And TgtFilePath RegExp  "\\moveit[^\\]+"   And TgtFilePath Contains  Anycase   "wwwroot" And TgtFileExtension =  "aspx" | 识别在MOVEit Web文件中写入新的ASPX文件或修改现有ASPX文件的IIS  worker进程 |
| S1PQ:   src.process.parent.name = "w3wp.exe"  AND   src.process.parent.cmdline contains  "moveit"   AND src.process.name = "csc.exe"  AND   src.process.cmdline contains "Temporary  ASP.NET   Files" AND (tgt.process.name =  "cvtres.exe"   OR tgt.file.path matches '.\*?  App\_Web\_[a-z0-9A-Z]{1,40}\.dll$') | 表明存在编译后的后门 |

除了这些查询外，SentinelOne还提供一个脚本来扫描MOVEit Transfer漏洞是否可能被利用的情况（https://github.com/SentineLabs/MOVEit-IIS-Log-Scanner）。

**结论**

基于SentinelOne观察到的活动，我们认为攻击者的目的是建立访问尽可能多的受害者环境的途径，以便大规模泄露文件。

虽然Cl0p勒索软件组织声称对这些攻击负责，但SentinelOne特别指出，这些技术与这个更广泛的趋势相一致：以牟利为目的攻击运行高危文件传输软件的web服务器。这类活动包括针对Aspera Faspex软件的攻击，攻击者在2023年早些时候投放了IceFire勒索软件，以及Cl0p利用GoAnywhere托管文件传输（MFT）应用程序中的零日漏洞进行的攻击。基于使用零日和N日漏洞的文件传输服务器攻击相对增加，外头可能存在一个针对企业文件传输应用程序的漏洞开发生态系统。

攻击者选择使用MOVEit漏洞来攻击Azure云存储中的文件值得注意，如果该活动仅与Cl0p勒索软件组相关。Bianlian和Karakurt等侧重云的勒索组织使用Rclone和Filezilla等多用途文件管理工具。定制的webshell旨在通过目标环境所特有的SQL查询来窃取Azure文件，这明显不合常规，表明该工具可能在ITW攻击之前已开发和测试得很好。

**攻陷指标**

与利用高危MOVEit Transfer实例相关的文件包含以下内容。

SHA1

d013e0a503ba6e9d481b9ccdd119525fe0db7652

34d4b835b24a573863ebae30caab60d6070ed9aa

c8e03cb454034d5329d810bbfeb2bd2014dac16d

eee9451901badbfbcf920fcc5089ddc1ee4ec06d

73f19114d61bd09789788782f407f6fe1d6530b9

7d91f5b03932793ff32ad99c5e611f1e5e7fe561

a2f74b02f29f5b1a9fe3efe68c8f48c717be45c2

c756c290729981d3804681e94b73d6f0be179146

11608a031358817324568db9ece1f09e74de4719

b8704c96436ffcbd93f954158fa374df05ddf7f6

本文翻译自：https://www.sentinelone.com/blog/moveit-transfer-exploited-to-drop-file-stealing-sql-shell/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ariP2Nup)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4ho...