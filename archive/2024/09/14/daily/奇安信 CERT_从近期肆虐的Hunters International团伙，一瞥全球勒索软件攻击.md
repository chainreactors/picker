---
title: 从近期肆虐的Hunters International团伙，一瞥全球勒索软件攻击
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502111&idx=1&sn=59a99f6e9c1f536e1511b93c970a869f&chksm=fe79ed87c90e6491a2d03f13ccf8c4170c74c498522d4644494924f58cefed9412f367b5d939&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-09-14
fetch_date: 2025-10-06T18:27:56.609250
---

# 从近期肆虐的Hunters International团伙，一瞥全球勒索软件攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibxuAZvlGHFiaYLM0LkcmHkFJ4cibvdSNhQ8ibbH8oibmpniaVvGMvUA02K1EFtDx1NmL4EXvbMt6MDNrg/0?wx_fmt=jpeg)

# 从近期肆虐的Hunters International团伙，一瞥全球勒索软件攻击

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_svg/uHwLXtyH4IXTars0DEAdy9nZcUtFcGrTy3nibexVh7BkBPMPp5nLfNgt67b5GWcgVibZsbUSHhKbtb6Eibh4vBoiaLfySz3fSygp/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_svg/dx4Y70y9Xcs692v9TjnicxJEZft7mP8uWicBRPuXXzZg069MvuoD4NP9L3WJiaoqponicCib5DMjypusYpLvEsR5g11bPZsUtwfjB/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

勒索软件目前已成为全球各个行业的组织机构面临的一类重大网络威胁，绝大多数勒索软件攻击活动都是以经济利益为动机，背后的网络犯罪世界呈现出高度组织化和产业化的特点。除了通过加密文件对信息系统直接造成可用性破坏，一些勒索团伙还会在加密前窃取受害组织的数据，如果受害者不支付赎金，将以数据泄露进行要挟，从而实施“双重勒索”攻击。勒索攻击团伙的恶劣影响也引发了多国执法机构的打击，但依然阻挡不了攻击者趋利的决心，因此可以见到新出现的勒索软件团伙继承过去的衣钵卷土重来的现象。

奇安信威胁情报中心关注到新兴勒索软件团伙Hunters International在近期显著活跃，该团伙的活动情况也反映出2024年全球的勒索软件威胁形势依然严峻。奇安信威胁情报中心收集了2024年全球多个安全厂商发布的与勒索软件有关的安全报告，根据这些公开报告梳理2024年全球范围内的勒索软件攻击活动，列举其中提及的一些常见勒索软件投递方式，并总结了当前全球勒索软件攻击活动的几个特点。

![](https://mmbiz.qpic.cn/mmbiz_svg/GPyw0pGicibl6FlfJiaNBkMPMFyFOibLIWIcnofJD9HFIEkZM5SEbOlmbksIpNdHnJna42D5LSLYtEA7cbicE6qBeJv0fJ8eeZjfM/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkhBmJZvPXtaUAefuaoJCVTKXplxCtc9ibiav0toECE9GgicrEgxdtJOMFHDgLu3CN01gofEcWnI72wNtR2AicveephI/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other)

**01**

****Hunters International团伙****

Hunters International团伙于2023年下半年出现，其勒索软件的技术特点和操作策略与另一个勒索组织Hive存在重叠，并且兴起时间刚好在执法机构打击Hive的行动之后。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibxuAZvlGHFiaYLM0LkcmHkFvOp02vGibOVqaLG7yaiaHKHMuCh0r503PIJokUvVx5B5k9ReF4RcRicXQ/640?wx_fmt=png&from=appmsg)

**图1 Hunters International团伙的标志**

## （一）起源

2023年1月，包括美国司法部、联邦调查局、特勤局、欧洲刑警组织和欧洲机构在内的执法联盟对Hive勒索软件组织采取行动。Hive勒索团伙自2021年6月起，共向全球1500多名受害者勒索超过1亿美元。执法人员获取到Hive组织内部的网络访问权限，并掌握了用于解密多个受害者被勒索加密文件的密钥。此次行动之后，Hive团伙发布勒索和数据泄露信息的网站被查封，运营受到重大影响。

2023年10月，多名安全研究人员基于Hunters International和Hive勒索软件之间的代码相似性，发现Hive的运营者可能将资产转移到Hunters International。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibxuAZvlGHFiaYLM0LkcmHkFhlNkmcqbowDhnSIBePMuvIcakt6ibgATiaGNd8N6CPTmib95LLbffMF9Q/640?wx_fmt=png&from=appmsg)

**图2 安全研究人员发现Hive与Hunters International存在关联**

而Hunters International针对这些猜测发布了一个声明，声称他们不是Hive的继承者，而是一个独立的勒索组织，收购了Hive的源代码和基础设施，并且他们的运营重点也与Hive不同，更关注窃取数据而不是加密数据。后续国外安全厂商在对Hunters International攻击活动的追踪过程中认为该声明具有一定可信度，因为所有已知受害者都存在数据泄露，但并非每个受害者的数据都被加密。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibxuAZvlGHFiaYLM0LkcmHkF4FV9UziakDd3bc26jGz2cVAhECUQ43IodowQdtIPHh9GYIpFs8NTaHA/640?wx_fmt=png&from=appmsg)

**图3 Hunters International发布的声明**

## （二）攻击目标

Hunters International的攻击目标覆盖多个行业，受害者涉及医疗保健、汽车、制造、物流、金融、教育和食品领域，还包括能源公司、学校和动物园。受害目标大部分在美国，但也有欧洲、加拿大、巴西，以及新西兰和日本的公司和组织。

可以看出Hunters International对攻击目标的行业和地域并不挑剔，该团伙似乎只是寻求任何可以牟取利益的机会，因此挑选的攻击对象通常是那些没有足够网络防护能力的组织，或者是因为数据窃取和加密而感到压力不得不付费的机构。

范围广泛的受害者类型反映出Hunters International团伙适应和渗透各个领域的能力，使得该团伙对全球各种规模和领域的组织都构成重大威胁。与许多勒索软件事件一样，Hunters International勒索攻击活动的影响是多方面的，包括重大数据泄露、经济损失和声誉损害。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibxuAZvlGHFiaYLM0LkcmHkFugeejEjEM8Al2IEeDNKYM3bY84fwPVMOe0iagHMNvbc5Ntibmv3onrLg/640?wx_fmt=png&from=appmsg)

**图4 Hunters International用于发布受害者数据的网站**

在2024年前7个月，Hunters International团伙就攻击了超过130个组织，已成为全球活跃度排名靠前的勒索组织，该组织将自己定位为勒索软件即服务（Ransomware-as-a-Service, RaaS）提供商，从而使其他能力稍弱的攻击者能够使用该团伙的工具发动攻击。

Hunters International团伙的出现和活跃，体现了网络威胁持续存在且不断发展的性质，尽管打击勒索团伙的运营已有不少努力，但也不乏新兴勒索组织出现继续肆虐。

![](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**02**

******2024全球勒索软件攻击活动******

纵观2024年的勒索软件攻击活动，全球各地多个行业的组织和个人都受到影响，活跃的勒索软件家族数量众多，并且还出现了一些新型勒索软件和变种，足以反映出这个网络犯罪产业的繁荣。

## （一）概览

奇安信威胁情报中心收集了2024年全球多个安全厂商发布的与勒索软件有关的安全报告，对安全报告中涉及的勒索软件或勒索组织、受害者所在国家地区和行业进行整理，如下表所示（表格中“/”符号表示报告中未明确提及相关信息）。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **报告主题** | **报告发布机构** | **勒索软件/组织** | **受害国家/地区** | **攻击目标** |
| 针对Akira和Royal勒索软件受害者的后续勒索活动 | Arctic Wolf | / | / | Akira和Royal勒索软件受害者 |
| 攻击者积极针对MSSQL服务器，以投递Mimic勒索软件 | Securonix | Mimic勒索软件 | 美国、欧盟和拉丁美洲国家 | / |
| Babuk勒索软件变种的新解密器发布 | Cisco Talos | Babuk勒索软件变种（Tortilla） | / | / |
| Medusa勒索软件攻击活动 | Palo Alto Networks | Medusa勒索软件 | 美国、欧洲、非洲、南美、亚洲 | 高科技、教育和制造业等领域 |
| 门罗币挖矿程序以及Mimus勒索软件正通过各种漏洞进行分发 | AhnLab | Mimus勒索软件 | / | / |
| 伪装为注册机程序的勒索软件通过国内收款码收取赎金 | 360 | / | 中国 | 个人 |
| MSSQL服务器BCP功能被用于部署Trigona勒索软件和Mimic勒索软件 | AhnLab | Trigona勒索软件，Mimic勒索软件 | / | / |
| LIVE勒索软件利用IP-Guard漏洞 | 奇安信 | LIVE勒索软件 | 中国 | / |
| Kasseika勒索软件部署BYOVD攻击、滥用PsExec和Martini驱动程序 | Trend Micro | Kasseika勒索软件 | / | / |
| Phobos勒索软件变种（FAUST）发起攻击 | Fortinet | Phobos勒索软件变种（FAUST） | / | / |
| 勒索软件综述：Albabat | Fortinet | Albabat勒索软件 | 阿根廷、巴西、捷克共和国、德国、匈牙利、哈萨克斯坦、俄罗斯和美国等 | 公司、个人 |
| 阻止Akira勒索软件：通过TTP的预防和分析 | Morphisec | Akira勒索软件 | 北美、英国和欧洲 | 政府、制造、技术、教育、咨询、制药和电信等领域 |
| 勒索软件综述：Abyss Locker | Fortinet | Abyss Locker勒索软件 | 欧洲、北美、南美和亚洲等 | / |
| 包括Black Basta在内的威胁组织正在利用近期的ScreenConnect漏洞 | Trend Micro | Black Basta勒索组织，Bl00dy勒索组织 | / | / |
| 多阶段RA World勒索软件使用反AV策略，利用GPO | Trend Micro | RA World勒索软件 | 拉丁美洲地区 | 多家医疗保健组织 |
| GhostSec联合Stormous团伙对多个国家实施双重勒索攻击 | Cisco Talos | GhostLocker勒索软件，Stormous勒索软件 | 古巴、阿根廷、波兰、中国、黎巴嫩、以色列、乌兹别克斯坦、印度、南非、巴西、摩洛哥、卡塔尔、土耳其、埃及、越南、泰国和印度尼西亚 | 科技公司、高校教育、制造业、政府机构、交通运输、能源等领域 |
| Shadow勒索组织攻陷俄罗斯多家公司 | F.A.C.C.T. | Shadow勒索组织 | 俄罗斯 | 多个行业的公司 |
| Phobos勒索软件：分析8Base勒索组织使用的网络基础设施 | Intel-Ops | Phobos勒索软件，8Base勒索组织 | 美国、巴西、英国、加拿大等 | 商业服务、制造业、建筑、零售等 |
| 新勒索家族出现，Donex公布多名受害者信息 | 安恒 | Donex勒索软件 | / | / |
| Mallox勒索软件攻击事件 | 深信服 | Mallox勒索软件 | 中国 | / |
| StopCrypt勒索软件变种在野外传播 | SonicWall | StopCrypt勒索软件 | / | / |
| TeamCity漏洞利用引入Jasmin勒索软件和其他恶意软件 | Trend Micro | Jasmin勒索软件 | / | / |
| TellYouThePass勒索软件目标锁定财务管理设备 | 360 | TellYouThePass勒索软件 | 中国 | 财务管理 |
| Agenda勒索软件通过自定义PowerShell脚本传播到vCenter和ESXi | Trend Micro | Agenda勒索软件 | 美国、阿根廷、澳大利亚以及泰国等 | 金融、法律、建筑业等 |
| 秘鲁军方勒索事件及相关勒索组织深度分析 | 启明星辰 | INC Ransom勒索组织 | 秘鲁 | 军队 |
| 勒索软件Crypt888技术分析 | Stormshield | Crypt888勒索软件 | 东南亚 | 个人 |
| Evil Ant勒索软件分析 | Netskope | Evil Ant勒索软件 | / | / |
| TargetCompany勒索组织对配置不当的MSSQL服务器进行攻击 | AhnLab | Mallox勒索软件 | / | / |
| Makop通过loldrivers关闭安全软件 | 深信服 | Makop勒索软件 | / | / |
| 攻击者利用IcedID传播Dagon Locker勒索软件 | THE DFIR REPORT | Dagon Locker勒索软件 | / | / |
| LockBit勒索软件家族最新动态 | 360 | LockBit勒索软件 | / | / |
| Trinity勒索软件分析 | Cyble | Trinity勒索软件 | / | / |
| 攻击者在针对MSSQL服务器的攻击活动中利用PureCrypter部署Mallox勒索软件 | SEKOIA.IO | Mallox勒索软件 | / | / |
| Phorpiex僵尸网络正在大规模分发Lockbit Black勒索软件 | Proofpoint | LockBit勒索软件 | / | / |
| Storm-1811组织滥用Quick Assist工具部署勒索软件 | Microsoft | Black Basta勒索软件 | / | / |
| Ikaruz Red Team：利用勒索软件收获注意力而非金钱的黑客组织 | SentinelOne | LockBit勒索软件 | 菲律宾 | / |
| ShrinkLocker：将BitLocker变成勒索软件 | Kaspersky | / | 墨西哥、印度尼西亚和约旦等 | / |
| 勒索组织Ransomhub瞄准西班牙生物能源工厂的SCADA系统 | Cyble | Ransomhub勒索组织 | 西班牙 | 能源 |
| 新型勒索软件变种Fog | Arctic Wolf | Fog勒索软件 | 美国 | 教育、娱乐 |
| RansomHub：源自Knight的新型勒索软件 | Symantec | Ransomhub勒索组织 | / | / |
| TargetCompany的Linux变种针对ESXi环境 | Trend Micro | Mallox勒索软件变种 | / | / |
| 勒索软件综述：Shinra和Limpopo勒索软件 | Fortinet | Shinra勒索软件，Limpopo勒索软件 | 拉丁美洲、泰国 | / |
| P2Pinfect僵尸网络不断发展以部署勒索软件和挖矿程序 | Cado Security | / | / | / |
| 勒索新秀Brain Cipher | 深信服 | Brain Cipher勒索团伙 | 印度尼西亚 | 数据中心 |
| Volcano Demon勒索软件组织活动追踪 | Halcyon | Volcano Demon勒索团伙 | / | / |
| Eldorado勒索软件活动分析 | Group-IB | Eldorado勒索软件 | 美国、意大利、克罗地亚 | 房地产、教育、医疗保健、制造业等 |
| 利用未修补漏洞的Veeam软件的攻击事件 | Group-IB | EstateRansomware勒索软件 | 阿联酋、法国、马来西亚、美国等 | / |
| Akira勒索软件攻击拉美航空业 | BlackBerry | Akira勒索软件 | 拉丁美洲 | 航空公司 |
| Play勒索软件Linux变种针对ESXi环境 | Trend Micro | Play 勒索软件变种 | 美国、加拿大、德国等 | 制造、专业服务、建筑、信息技术等 |
| UNC4393威胁组织攻击活动 | Google | BASTA勒索软件 | / | / |
| Hunters International勒索组织使用的新木马SharpRhino | Quorum | Hunters International勒索组织 | 美国、加拿大、欧洲、巴西等 | / |
| Magniber勒索软件攻击激增影响全球家庭用户 | BleepingComputer | Magniber勒索软件 | / | 个人 |
| Inc...