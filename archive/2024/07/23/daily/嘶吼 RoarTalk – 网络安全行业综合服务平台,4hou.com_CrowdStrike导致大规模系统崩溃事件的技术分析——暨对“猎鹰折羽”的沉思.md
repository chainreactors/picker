---
title: CrowdStrike导致大规模系统崩溃事件的技术分析——暨对“猎鹰折羽”的沉思
url: https://www.4hou.com/posts/VWmM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-23
fetch_date: 2025-10-06T17:40:58.621375
---

# CrowdStrike导致大规模系统崩溃事件的技术分析——暨对“猎鹰折羽”的沉思

CrowdStrike导致大规模系统崩溃事件的技术分析——暨对“猎鹰折羽”的沉思 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CrowdStrike导致大规模系统崩溃事件的技术分析——暨对“猎鹰折羽”的沉思

安天
[技术](https://www.4hou.com/category/technology)
2024-07-22 15:11:26

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)97677

收藏

导语：使用微软系统的电脑出现蓝屏现象，至少20多个国家的交通、金融、医疗、零售等行业或公共服务的业务系统受到影响。

**1 事件的基本情况和影响**

北京时间2024年7月19日中午开始，全球多地用户在X（原推特）、脸书、微博等社交平台反映使用微软系统的电脑出现蓝屏现象，至少20多个国家的交通、金融、医疗、零售等行业或公共服务的业务系统受到影响。其原因是使用CrowdStrike公司终端安全产品的Windows操作系统的主机大面积发生系统崩溃故障，即“蓝屏死机”（Blue Screen of Death,BSOD），导致计算机系统无法正常运行。出现故障的终端并不止限于桌面终端，而是覆盖了大量的服务器和云节点，包括导致了多个重要的微软和AWS的云服务和租户服务中断。而且相关主机重新启动后依然会自动进入蓝屏状态，形成了反复崩溃闭环。此事件是今年以来全球波及范围最广的信息系统灾难性事件，也是由安全产品自身导致的最大规模的安全灾难事件，其事件带来的后果影响远远超过了2007年的赛门铁克误杀中文版Windows导致系统蓝屏事件等历史上由安全产品带来的安全事件。

北京时间7月19日19时，安天由云安全中心、安全研究与应急处理中心、攻防实验室人员组成混合分析小组，进行了跟进分析，及时将分析研判进展上报管理和应急部门，开发了CrowdStrike\_Crash\_Fix应急处理小工具，协助求助用户处理威胁，并发布了本分析报告。

CrowdStrike是美国主要的云、终端安全厂商之一，成立于2011年，2024年6月其市值一度接近千亿美元，是全球市值最大的网络安全上市公司之一。其开发的云本地端点保护平台CrowdStrike Falcon，开启了多租户、云原生、智能安全解决方案的先河，结合了下一代杀毒软件、威胁情报、端点检测和响应（EDR）、设备控制、威胁情报搜索和IT安全运营、事件响应和主动服务。平台设置了独立模块用于管理系统漏洞和移动终端检测和响应，还通过跨越多个大型安全市场的SaaS模型提供19个云模块，包括企业端点安全、云安全、托管安全服务、安全和IT运营、威胁情报、身份保护和日志管理等。

就本次事件，CrowdStrike给出的解释是，该公司的终端安全软件“Falcon Sensor”推送的错误的配置更新与Windows系统发生了兼容性问题，导致安装了该安全软件的计算机出现蓝屏情况。后续该公司代表在其客户支持平台回复称公司工程部已确定该问题与其产品的“内容部署（Content deployment）”功能有关，目前已经撤销了错误更新，并在积极调查此事。

**这是一起因广泛使用的安全产品故障，导致大量主机系统崩溃，并连带导致大量基础设施系统无法提供服务导致了多米诺效应的事件**。该事件造成了美国、英国、澳大利亚、加拿大、日本等至少20多个国家和地区的组织机构的业务系统服务中断，全球多地的航空运输、医疗服务、媒体、银行与金融服务、零售、餐饮等行业或公共服务受到了影响。

表 1‑1 受到影响的行业领域、国家地区与相关机构

|  |  |
| --- | --- |
| 涉及领域 | 相关机构 |
| 航空运输 | 美国、澳大利亚、英国、荷兰、印度、捷克、匈牙利、西班牙、中国香港、瑞士等部分航空公司出现航班延误或机场服务中断。美国达美航空、美国航空和忠实航空宣布停飞所有航班。 |
| 媒体通信 | 以色列邮政、法国电视频道TF1、TFX、LCI和Canal+ Group网络、爱尔兰国家广播公司RTÉ、加拿大广播公司、沃丰达集团、电话和互联网服务提供商Bouygues Telecom等。 |
| 交通运输 | 澳大利亚货运列车运营商Aurizon、西日本旅客铁道公司、马来西亚铁路运营商KTMB、英国铁路公司、澳大利亚猎人线和南部高地线的区域列车等。 |
| 银行与金融服务 | 加拿大皇家银行、加拿大道明银行、印度储备银行、印度国家银行、新加坡星展银行、巴西布拉德斯科银行、西太平洋银行、澳新银行、联邦银行、本迪戈银行等。 |
| 零售 | 德国连锁超市Tegut、部分麦当劳和星巴克、迪克体育用品公司、英国杂货连锁店Waitrose、新西兰的Foodstuffs和Woolworths超市等。 |
| 医疗服务 | 纪念斯隆凯特琳癌症中心、英国国家医疗服务体系、德国吕贝克和基尔的两家医院、北美部分医院等。 |
| …… | …… |

主要受到影响的领域，更多详情见 附录二：受到影响的组织机构清单。

本次事件对国内政企机构影响较小，主要由于CrowdStrike是对中国大陆禁售产品，国内主要相关外资企业和部分使用微软数据中心的企业部分受到此次故障影响了相关业务。如国内希尔顿酒店集团旗下的上海康莱德酒店，其入住和退房服务受到了影响。

当然，这也给小组的分析工作造成了障碍。

**2  应急解决方案**

**2.1 手动删除带有问题的文件（原厂方案）**

CrowdStrike公司的业务支撑体系是高度在线化的，其在仅由注册客户可见的网页发布了解决方案，非其客户无法访问，但有受影响的用户公开分享了该官方解决方案：

1.将Windows重启至安全模式或恢复模式，或用WinPE启动；

2.打开“%systemroot% \System32\drivers\CrowdStrike”文件夹；

3.删除其中文件名为“C-00000291\*.sys”（\*表示任意字符）的文件；

4.正常重启系统。

以下为更完整的事件说明及解决方案，对于公有云等类似环境的用户可通过下图中“备份并挂载磁盘到临时虚拟系统”的方法对错误文件进行处理。

同时，对于使用了BitLocker卷加密的用户，需要准备好恢复密钥，再进入安全模式进行操作。

![图 2 1事件说明及解决方案.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721615132179592.png "1721615132179592.png")

图 2‑1事件说明及解决方案

**2.2 小工具CrowdStrike\_Crash\_Fix（安天发布）**

安天CERT在7月19日晚发布了临时处置小工具CrowdStrike\_Crash\_Fix，已经上传至安天垂直响应平台（<https://vs2.antiy.cn/>）。可将Windows重启至安全模式或恢复模式后，使用该工具一键处理异常文件。根据受影响用户的反馈，该工具可以显著节省处置所需时间。（当前工具更新至V0.5版本，已经支持基于WinPE介质启动后的处置）。

![图 2 2安天临时处置工具CrowdStrike_Crash_Fix.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721615109613031.png "1721615109613031.png")

图 2‑2安天临时处置工具CrowdStrike\_Crash\_Fix

**3 事件的技术分析**

**3.1 CrowdStrike 的工作机理解析**

CrowdStrike Falcon Sensor 是非常典型的具有内核（驱动）级主防的EDR产品，其在Windows平台下安装/预装后，将对应程序文件安装到%ProgramFiles% \CrowdStrike指向的目录下，而将其驱动程序和重要的数据文件安装到%SystemRoot%\System32\ drivers\CrowdStrike 目录下。其主要的防御能力来自于多个系统内核驱动模块。其中CSBoot.sys是Windows 操作系统的提前启动反恶意软件（ELAM）功能模块（利用微软接口实现安全软件要比恶意代码先行加载以保证引导链安全的机制）；CSFirmwareAnalysis.sys是固件安全模块；CSAgent.sys是主防护的核心功能模块；cspcm4.sys为策略解析模块。加载的先后顺序依次为CSBoot.sys、CSFirmwareAnalysis.sys、CSDeviceControl.sys、CSAgent.sys、cspcm4.sys。

表 3‑1 CrowdStrike的主要程序和驱动模块列表

|  |  |  |
| --- | --- | --- |
| 分类 | 文件名 | 描述 |
| 应用程序 | CSFalconService.exe | 主要的服务进程 |
| CSFalconController.exe | 后台控制程序 |
| CSFirmwareAnalysisSupportTool.exe | 固件分析工具 |
| CSDeviceControlSupportTool.exe | 外部设备管控 |
| 驱动和内核模块 | CSBoot.sys | 操作系统的早期启动反恶意软件（ELAM）功能模块，用于保护驱动程序加载 |
| csfirmwareanaltsis.sys | 固件安全模块 |
| cspcm4.sys | 内核注册回调接口模块，为CSAgent.sys提供回调接口 |
| Config.sys | 管理策略配置的模块 |
| CSAgent.sys | 主要的功能模块，它包含文件过滤、网络过滤、进程管控 |
| CSDeviceControl.sys | USB设备过滤驱动 |

发生蓝屏的模块CSAgent.sys是其主要的功能模块，该模块带有CrowdStrike和微软的双重数字签名。根据安天攻防实验室的初步分析，它包含文件监测、运行监测、网络过滤等功能，是其主动防御和主机防火墙的核心驱动。基本的运行原理是：驱动程序加载后首先读取策略配置，根据策略对文件读写、进程加载、内存执行、API调用、网络访问等动作，做出放行与阻止操作；优秀的主机安全软件为了快速敏捷的对抗威胁，即时更新防护能力，往往都支持在线分发、可动态接收、即时解析生效下发的策略，这样可以灵活变更配置处理突发事件而不用重启系统，CrowdStrike就使用了这种机制。但由于驱动程序直接调用系统内核接口，模块的稳定性对系统内核会有直接影响，可能是由于某个不当的策略配置，在解析执行策略时，未能正确处理好和系统间的同步机制或者是系统资源分配不当，造成系统死锁问题，引发蓝屏保护。

**3.2 对相关文件格式和机理的分析猜测**

该事件中“蓝屏”故障的错误代码为“PAGE\_FAULT\_IN\_NONPAGED\_AREA”，蓝屏信息中出现错误的驱动程序为“CSAgent.sys”。结合官方处置建议中删除“C-00000291\*.sys”文件的处置方案，可以明确判断本次事件直接原因是由于“CSAgent.sys”加载和解析使用存在错误设定的“C-00000291\*.sys”文件所致。

与CSAgent.sys 等驱动程序相同目录下（%Windows%\%System32%\drivers\CrowdStrike），存在多个文件名前两个字母为“C-”，且均以sys为拓展名的文件，我们需要严肃指出：这些C-\*.sys命名的文件并不是驱动程序文件，网上对本事件一些分析中，将这些也称为系统文件或驱动程序文件，有望扩展名生义的错误。Windows中sys为扩展名的系统文件（或称为驱动文件），格式上是以|4D 5A|为文件头的PE可执行文件，例如发生崩溃的CSAgent.sys就是一个PE文件，而在对应目录下以“C-“为统一开头的“sys”为扩展名的文件，应是一类自定义格式的数据文件。这些文件均以|AA AA AA AA|为文件头，并不具备执行能力，或者至少不具备在系统下直接执行的能力。在CrowdStrike所公布的信息中，将这些文件称为“通道文件”（Channel Files），声明其是 Falcon Sensor的配置文件，用于CrowdStrike防御机制的日常更新。因此可以基本判断相关文件主要类似规则/策略/基线的数据文件。

这些“通道文件”以C-xxxxxxxx-00000000-xxxxxxxx.sys格式进行命名，其文件第一个字符C，含义推测为CrowdStrike的首字母。随后有三个阿拉伯数字节，每节长度均为8位，其中第一节数字为通道号，转换为16进制后与文件中的固定偏移0x6处数值对应；采集到的全部文件的第二节数字值都固定为0，故只能猜测其与固定偏移0xC处数值（所有数值亦均为零）对应；第三节数字值转换为16进制后与文件中固定偏移0x10处数值相对应。

![图 3 1 事故对应的通道文件的文件头与其中的值和文件名的对应关系.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721615071121990.png "1721615071121990.png")

图 3‑1 事故对应的通道文件的文件头与其中的值和文件名的对应关系

由于相关产品机理复杂，尚未能判断这些通道文件具体的功能。对文件内容观测，判断文件经过了一定的编码变换，但似乎未使用分组算法进行加密。我们分析了文件的命名规律，含义猜测如下：第一节数字即通道号，是为其规则/配置库编号，而且设定了对应的值域范围对应的规则/配置分类，第二节为保留段，第三节为对用的规则/配置库更新的次数（即版本）。

![图 3 2 C-系列文件的类型序号(猜测)和更新次数(猜测)关系分布.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721615055113626.png "1721615055113626.png")

图 3‑2 C-系列文件的类型序号(猜测)和更新次数(猜测)关系分布

![图 3 3 C-系列文件的更新次数（猜测）与文件大小的关系.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721615026363041.png "1721615026363041.png")

图 3‑3 C-系列文件的更新次数（猜测）与文件大小的关系

基于以上两个统计分析，我们可以看到管道号是按照值域部分连续分布的，而相对大的文件，我们猜测为更新次数的数值越大，基本验证我们对于文件命名规则的猜测是有依据的。

CrowdStrike对于相关漏洞的官方解释为：

此次涉及到的 以“C-00000291”作为文件名开头、 “.sys”作为扩展名的文件属于配置文件，也被称作“Channel Files”。这些文件是Falcon Sensor行为防护机理的一部分。这些文件在日常运营中根据CrowdStrike 监测到的每日威胁技战术情况，一天会更新若干次。

文件以C开头，每个“通道文件”被分配了唯一的编号作为标识。此次造成影响的是291，相关文件以“C-00000291-”开头，用“.sys”作为扩展名。虽然使用驱动文件的扩展名，但这些文件不是驱动程序。
 291通道文件，控制Falcon对Windows上的“命名管道（Named Pipe）”执行动作进行评估。“命名管道”是常用技术，通常在Windows环境中用于进程间通信或系统间通信。

该文件的更新发生在UTC 时间 ...