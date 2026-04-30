---
title: 深度分析Sorry勒索软件的加密实现与行为特征
url: https://www.anquanke.com/post/id/315390
source: 安全客-有思想的安全新媒体
date: 2026-04-29
fetch_date: 2026-04-30T05:23:47.604857
---

# 深度分析Sorry勒索软件的加密实现与行为特征

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 深度分析Sorry勒索软件的加密实现与行为特征

阅读量**23290**

发布时间 : 2026-04-29 13:32:51

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

### ****Sorry勒索软件攻击事件****

Sorry勒索软件自今年3月现身以来，利用各类常见企业软件漏洞发起攻击，能够远程加载攻击载荷，并展现出跨平台的勒索攻击能力。****本周，360反病毒团队持续收到与Sorry勒索软件相关的样本反馈与攻击告警信息，本轮勒索攻击的峰值集中爆发于4月中旬的两个周末。****结合样本逆向分析、加密文件结构还原及攻击行为链追踪，本次事件呈现出明显的“利用漏洞自动批量投放”与“目标文件定向加密”的攻击模式。从技术实现角度看，该家族采用分层密钥封装设计。即以RSA+RSA+AES-GCM 的算法组合方案实现文件加密与密钥保护操作。这一设计在兼顾了批量加密速度的同时，也大幅提高了受害者在无密钥的情况下想要破解算法直接恢复文件的难度。

此外，样本在运行时会主动收集主机标识信息，包括但不限于主机名称与基于当前设备环境特征计算出的“host\_hash”值，并将其写入相关数据结构中，供攻击运营侧对受害主机与加密会话进行追踪管理。

综合来看，该变种具备完整的工程化实现。****其整体完成度较高，建议广大安全厂商将本次事件列为中高危等级的勒索事件，启动相应的分级响应流程。同时结合其在周末假期较为活跃的特性，对五一假期期间极有可能出现的新一轮攻击高峰做好安全防护预案。****

### ****本轮勒索事件攻击流程****

本轮的Sorry勒索软件的典型攻击进程链如下：

![]()

图1. 攻击进程链示例

而该勒索软件的加密逻辑流程则如下图所示：![]()

图2. 加密流程示意图

我们的分析人员综合完整的入侵、加密链条并结合我们的技术分析与解决方案，厘清了Sorry勒索家族完整的加/解密流程示意图，供大家更加直观地理解本轮攻击的总体情况。

![]()

图3. Sorry勒索软件攻击概况

### ****勒索样本技术分析****

****环境初始化****

我们以一个典型的勒索软件样本为例，其在运行后会首先停止MSSQL的相关服务。在诸多数据库服务中，勒索软件唯独停止了MSSQL相关服务，可见其勒索目标对服务器系统的针对性极强。

![]()

图4. 定向关闭MSSQL服务

而该样本所要加密的文件扩展名完整列表如下：

db、db3、db\_journal、dbf、dbx、fdb、mdb、mdf、ndf、sql、sqlite、sqlite3、sqlitedb、ldf、sdf、3db、accdb、accde、accdr、accdt、bdb、edb、adf、dbb、bak、doc、docx、docb、docm、dot、dotm、dotx、pdf、txt、rtf、odt、ods、odp、ott、xls、xlsx、xlsb、xlsm、xlt、xltm、xltx、ppt、pptm、pptx、pot、potm、potx、pps、ppsm、ppsx、ppam、psd、ai、eps、svg、png、jpg、jpeg、gif、bmp、tiff、tif、ico、raw、cr2、nef、orf、dng、raf、arw、webp、fpx、dwg、dxf、skp、indd

在加密扩展名的列表外，为避免不必要的系统异常导致加密失败，勒索软件还排除了部分文件的路径、文件名及扩展名。

被排除的文件名及扩展名如下：

thumbs.db, netuser.dat, autorun.inf, iconcache.db, bootfont.bin, desktop.ini, pagefile.sys, .ds\_store, .sorry, readme.md

被排除的目录、路径关键词如下

:\windows, \git\mingw64, \git\usr, \go\src, \go\pkg\mod, \java\jdk, \vmware\drivers, \program files\vmware, \inetpub\temp\apppools, programdata, efi.boot, efi.microsoft, all users, node\_modules, .git, recycle.bin, system volume information, .trash, .cache, \_\_pycache\_\_, ieidcache, \appdata, .recovery, local settings, site-packages, test\_importlib

![]()

图5. 前期初始化代码

****文件加密算法****

该勒索软件采用了AES-GCM算法对文件进行加密。其在开始正式的加密操作时，会首先对每个文件单独生成一个AES密钥和该算法的GCM模式所需的Nonce/IV值。

![]()

图6. 生成随机AES密钥

与此同时，勒索软件还会调用RSA算法生成一对公私钥，对用于加密文件所使用的AES-GCM的密钥进行加密。而在生成了该RSA密钥对之后，勒索软件会再次使用内置的主RSA公钥，加密上述现场生成的RSA私钥，并对现场获取到的用户名和机器名等信息进行加密。

![]()

图7. 生成RSA密钥对

勒索软件内置的主RSA公钥如下：

![]()

图8. 内置的RSA公钥

样本还会以独占或绕过保护的方式打开文件，以防止文件被占用时无法读取，影响其对文件的加密操作。

![]()

图9. 独占方式打开文件

勒索软件会基于NTAPI直接调用系统操作，该操作可以有效绕过大多数软件的常规API调用（如文件读/写操作），而直接向系统内核发起调用。这种做法主要为了规避包括EDR在内的各类安全客户端对于用户态接口调用的监控，实现所谓的“盲区加密”。

![]()

图10. 利用NTAPI进行盲区加密

****数据结构****

完成所有加密操作后，最终被加密完成的文件输出结构如下：

****Magic头部****
1字节，固定内容0x11

![]()

图11. 写入Magic头

****CHUNK长度值****

4字节，长度数值大端顺序

![]()

图12. CHUNK\_LENGTH数据

****RSA封装块****

前置4字节，长度值大端顺序。后续为密文块。

![]()

图13. RSA封装块

****各数据区域独立分块的CHUNK\_CIPHER****

前置为4字节chunk\_cipher\_length，大端顺序。后续为与之长度对应的密文数据，且chunk\_length = plaintext\_chunk + 16。

![]()

图14. CHUNK\_CIPHER\_LENGTH数据

****终止数据****4字节长度，固定使用0x00数据填充。

![]()

图15. 终止数据

分块大小均为0x100000字节（1MB）。

![]()

图16. 分块大小定义

而加密后文件附加数据大小计算公式如下：

具体到本次分析的样本，最终L1和L2的值为：

* L1=2048
* L2=256

因此：

综上所述，被Sorry勒索软件加密后的数据长度计算方式如图所示：

![]()

图17. 附加数据长度计算方式

根据N值的不同，Δ的值如下表：

|  |  |  |  |
| --- | --- | --- | --- |
| ****原大小**** | ****N********值**** | ****计算：2317 + 20×N**** | ****加密后附加数据大小 Δ**** |
| 1 MB | 1 | 2317+20 | +2337 |
| 5 MB | 5 | 2317+100 | +2417 |
| 10 MB | 10 | 2317+200 | +2517 |
| … | … | … | … |

表1. Δ值计算

****勒索信****

勒索信内容是采用了亦或加密后的一段固定长度（0x184字节）的数据，勒索样本会在加密完成后，将其内容解密到一份ReadMe.md文件当中。

![]()

图18. 释放ReadMe.md勒索信

早期版本的勒索信中还附带了手动输入的用户ID，而由于新样本采用了将用户ID及加密后的私钥信息写入加密文件的操作，所以勒索信中不再需要ID。

![]()

图19. 内置的勒索信内容

最终勒索信README.md文件锁展示的内容如下：

![]()

图20. 释放出的勒索信文件内容

****信息窃取****

除了上述常规的加密操作外，该勒索软件还会对加密情况以及用户机器信息进行回传。其会向服务器发起GET请求来获取一个IP地址，并在User-Agent中拼接传递关键信息。

具体传递的字段如下：

Firefox-type=stats
&hostname=360AntivirusTeam &host\_hash=09b3e7a2acd05155eba33cfff8388374&ts=1775829511
&level=1
&ok=1999
&skipped=3
&failed=20

其中host\_hash的计算逻辑是：用“机器的一些固定信息”拼成一串数据，之后做SHA256算法的HASH运算，再取前一半（即前16字节）的32位小写 HEX字符串作为唯一指纹。

该数值可以理解为是给每台电脑生成一个“唯一身份ID”，这些固定信息包括：

* ****HOSTNAME****: 机器名
* ****USERNAME****: 用户名
* ****PROCESSOR\_IDENTIFIER****: CPU信息
* ****NUMBER\_OF\_PROCESSORS****: CPU核心数
* ****SystemDrive****: 系统盘（如C：）

最终，勒索软件会将上述信息通过GET请求在User-Agent字段中传递到黑客服务器上。

![]()

图21. 通过GET请求的User-Agent字段传输信息

详细的上传数据字段及含义示例如下：

|  |  |  |
| --- | --- | --- |
| ****字段名**** | ****示例********值**** | ****说明**** |
| Firefox-type | stats | 请求类型，表明是统计数据上报 |
| hostname | 360AntivirusTeam | 客户端主机名称 |
| host\_hash | 09b3e7a2acd05155eba33cfff8388374 | 基于主机标识生成的sha256哈希值[16].hex(）（用于设备唯一化ID） |
| ts | 1775829511 | Unix时间戳，加密数据生成时间戳 |
| level | 1 | 级别标识（日志级别或维度） |
| ok | 1999 | 成功完成加密的文件数量 |
| skipped | 3 | 被跳过加密的文件数量 |
| failed | 20 | 加密失败的文件数量 |

表2. 上传数据字段及含义

另外，我们也接到一些Linux用户被加密的反馈，说明本轮勒索攻击并不局限于常规的Windows系统平台。Linux用户设备的感染情况如下：

![]()

图22. Linux受害设备情况

综合静态与动态分析结论，Sorry勒索软件可以通过直接调用底层 NTDLL 接口并主动跳过关键系统目录，有效降低加密初期被EDR等各类安全终端动态行为监控拦截的概率，具备较强的对抗检测能力。

具体技术特征如下：

* ****加密链路完整****采用RSA+RSA+AES-GCM的分层加密保护机制；
* ****文件格式结构稳定****可识别固定Magic头+RSA封装段+分块密文+终止块的完整结构；
* ****密钥生成无明显弱点****AES会话密钥来源于系统级随机接口，未发现固定种子等可利用缺陷；
* ****具备受害者标识管理逻辑****存在基于HOSTNAME、HOST\_HASH的主机侧标识构造，与攻击运营侧的受害者管理体系相关联。
* ****跨平台攻击****支持Linux系统环境文件加密。

从实战角度判断，该家族并非粗糙型勒索工具，而是一套具备可扩展性与可复用性的成熟实现。经对加密算法的详细分析可以确认：在没有攻击者RSA主私钥的情况下，无论是暴力破解还是提取内存残留密钥，文件恢复的可能性基本为零。

### ****防护建议****

对此，360反病毒团队提出以下防护建议：

1. ****入口防护****
   立即排查并修复对外暴露的系统与第三方组件漏洞，重点核查近期高危漏洞的利用面。
2. ****最小权限原则****
   收敛本地管理员与域高权限账号，关闭不必要的远程管理端口，清除弱口令服务。
3. ****勒索行为检测防护****
   部署可靠的终端安全防护软件，启用勒索专项防护能力并保持实时防护开启。
4. ****关键资产隔离****
   对文件服务器、数据库、备份系统实施网络分区，阻断单点入侵后的横向传播路径。
5. ****备份策略****
   执行 3-2-1 备份原则，确保包含离线或不可变备份副本，并定期演练按业务优先级的恢复流程。

****IOCs****

****HASH****

6603bde2ec697a7b3a25a562fbb77aed3e34ac221b5a3729ccbfcf77d5e12eb9

97CCA21E82A6ED203D57D49B0F155D0558B2D9867A96E5042E188CF9D82B7F3B

6660339AF05F97F1741FE8C2F5E6B0B1F2801E3BCB7129958CD84A276B9EF942

7bc13bc54c6f9370d56e5722eab90d53dfda024d990a09707e84b7e5b33d3f09

9e26470532eaec05f7817b37e9da1e80

****IP & URI****

209.97.175.77

http://1001fangruan[.]oss-cn-shenzhen.aliyuncs[.]com/update.msi

****RSA-Master-Pubkey****

—–BEGIN PUBLIC KEY—–

MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA9FDS8hGaEUcJo0TwuAnR

GAf6DvFX7TI8GDm1lO5wqOOz40UImC+W5KW6kpocrvPu5sa0M4AufxGeXnvqrBMs

RFQxKDlmGMlGkyzwmgZv+1+Lm9V3xt7bJQiDrKWLDFys6L4BoRmAynre0Bcv/l2J

MmFxaeXm4sb9QRuDGVFXFnA3MxTYYv+KjWBEzWOBDdwSuJ2V80t0kbkQbr+ib3B6

SrcBh0JBX4WmyTmAi7mL3ECl+ihvWioflpLUptGkqHQX4VxhYk6mqytnl++YG05b

lyAGg8Czh51hXIl8tJaGszfNTZ/eY4LvnIDKg1b2gdjpiZDbXrefW7AFvcuC2FVC

JwIDAQAB

—–END PUBLIC KEY—–

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315390](/post/id/315390)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1091**

* 粉丝
* **6**

### TA的文章

* ##### [深度分析Sorry勒索软件的加密实现与行为特征](/post/id/315390)

  2026-04-29 13:32:51
* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布...