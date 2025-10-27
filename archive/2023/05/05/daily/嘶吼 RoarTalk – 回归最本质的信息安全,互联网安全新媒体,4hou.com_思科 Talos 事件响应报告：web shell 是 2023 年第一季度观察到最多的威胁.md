---
title: 思科 Talos 事件响应报告：web shell 是 2023 年第一季度观察到最多的威胁
url: https://www.4hou.com/posts/onQN
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-05
fetch_date: 2025-10-04T11:37:57.184595
---

# 思科 Talos 事件响应报告：web shell 是 2023 年第一季度观察到最多的威胁

思科 Talos 事件响应报告：web shell 是 2023 年第一季度观察到最多的威胁 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 思科 Talos 事件响应报告：web shell 是 2023 年第一季度观察到最多的威胁

xiaohui
[新闻](https://www.4hou.com/category/news)
2023-05-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)129464

收藏

导语：这些web shell的功能以及它们针对的平台中的特定漏洞和弱点各不相同。

思科Talos事件响应(Talos IR)报告称，与前几个季度相比，web shell是2023年第一季度最常见的威胁，占Talos IR发现的近四分之一。这些web shell的功能以及它们针对的平台中的特定漏洞和弱点各不相同。尽管每个web shell都有自己的基本功能集，但当每次攻击中存在多个web shell时，攻击者会将它们链接在一起，以提供更灵活的工具包，以便在整个网络中传播访问。这展示了攻击者在组合多种访问方式和工具方面的技能，并增加了他们部署额外恶意软件或获取敏感和私人信息的可能性。

勒索软件在本季度的威胁中所占的比例比过去有所下降，从20%降至10%左右。鉴于Talos IR在本季度末观察到勒索软件事件的激增，这种减少并不一定意味着一般勒索软件活动的减少，因为它反映了针对Talos IR客户群的活动。然而，勒索软件和预勒索软件事件加起来占观察到的威胁的20%以上。如果勒索软件从未执行，并且没有进行加密，那么很难确定什么构成了勒索软件前的攻击，但许多勒索软件前的活动都与著名的勒索软件组织(如Vice Society)有关。

本季度还出现了以前看到的大型加载程序，如Qakbot。在本季度的活动中，Qakbot利用了恶意OneNote文档，这与传播武器化Microsoft Office OneNote附件的各种恶意软件的增加相一致。这表明，在微软于2022年7月开始在其应用程序中默认禁用宏之后，攻击者正在尝试使用不依赖宏的文件类型来传递恶意有效载荷。

在超过45%的攻击中，攻击者利用面向公众的应用程序建立初始访问，比上一季度的15%有了显著增长。在许多此类攻击中，web shell的使用导致攻击者试图攻击暴露在互联网上的基于web的服务器。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230503/1683063192167891.png "1683063192167891.png")

医疗保健和公共卫生是本季度受攻击最多的行业，紧随其后的是零售和贸易、房地产和食品服务/住宿行业，包括酒店业。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230503/1683063208935370.png "1683063208935370.png")

**Web shell使用激增，FIN13的活动**

Talos IR观察到，自2023年1月以来，web shell的使用量从上个季度占所有威胁的6%增加到现在占所有威胁的近25%。Web shell是一种恶意脚本，它使攻击者能够攻击暴露在互联网上的基于Web的服务器。本季度，Talos观察到攻击者使用公开可用的或修改过的web shell，这些shell用各种语言编码，包括PHP, ASP.NET 和 Perl。在利用web shell建立立足点并获得对系统的持久访问后，攻击者远程执行任意代码或命令，在网络内横向移动，或传播额外的恶意有效负载。在许多类似web shell事件中，攻击者严重依赖于来自公开可用的GitHub存储库的web shell代码。这一发现也符合2022年7月至9月(2022年第三季度)Talos IR观察到的趋势，攻击者使用GitHub存储库上托管的各种开源工具和脚本来支持跨攻击生命周期多个阶段的操作。

在一个Web shell活动集群中，Talos观察到目标模式和策略、技术和程序(TTPs)可能与FIN13攻击者相关，这是Talos IR的一个重要发现。具有已知FIN13 TTP的web shell具有不同级别的功能，包括允许对Microsoft SQL（MS-SQL）实例进行查询，创建与外部IP地址的反向shell连接，以及执行可以用作连接到其他服务的代理的PHP脚本。与FIN13的公开报告一致，Talos IR观察到一个基于php的web shell(“404.php”)获取IP或DNS条目和端口并试图创建代理连接。

第二个web shell(“ms3.aspx”)是基于windows的，允许SQL连接到内部服务器，如果成功，结果将在浏览器中呈现。第三个是另一个基于php的web shell(“re.php”)，它执行端口扫描并创建一个出站套接字来响应/泄漏数据给攻击者。这个特定的web shell包含一个硬编码的IP地址，解析到云服务提供商DigitalOcean。

最后的web shell(“txt .asp”)是一个基于windows的web shell，它使用“wscript.shell”和exec()来运行通过HTML文档呈现在屏幕上的命令。虽然每个web shell本身都具有基本功能，但通过将它们链接在一起，攻击者创建了一个灵活的工具包，这样可以在整个网络中传播它们的访问权限，同时提供一个代理来盗窃敏感数据。

虽然本季度web shell出现的确切原因尚不清楚，但它们最近越来越受欢迎很可能与从开源存储库获取代码的便利性有关。开放源代码web shell代码的可用性和易于访问性，加上可能公开暴露的系统或管理不善的补丁，使得使用web shell成为一个有利可图的选择。

**勒索软件**

勒索软件在本季度的威胁中所占的比例要小得多，从20%降至10%。展望未来，最近勒索软件业务激增，我们预计下个季度将再次趋于平稳。综合来看，勒索软件和预勒索软件事件加起来占观察到的攻击的20%以上。

Talos IR自2020年以来一直在应对Phobos勒索软件攻击，最初的访问可能涉及远程桌面协议(RDP)。攻击者部署了一个名为名为“mimidrv.sys”的文件。这是一个签名的Windows内核模式软件驱动程序，旨在与Mimikatz可执行文件一起使用。Talos IR还识别出了7个启动项目，其中包括下载勒索软件可执行文件“Fast.exe”。这是一种常见的持久性技术，在攻击者对客户的Amazon Relational Database Service (RDS)服务器上的注册表进行修改的活动之后使用。加密后，攻击者对文件进行了加密，并在文件中添加了“.fust”扩展名，并在目标设备上发送了一封勒索信。

本季度研究人员还发现了Daixin勒索软件，这是一个新的勒索软件即服务（RaaS）家族，Talos IR以前从未看到过。据美国网络安全和基础设施安全局（CISA）称，2022年6月首次出现的Daixin通常通过附属公司的虚拟专用网络（VPN）服务器或利用未修补的漏洞访问受害者系统。在Daixin发起的一次攻击中，攻击者通过附属公司修改了注册表值，映射了网络共享，并将随机命名的BAT文件作为系统上的服务运行。Talos IR还识别了Impacket工具集，一个用于处理不同网络协议的Python类集合，以及一个加载Cobalt Strike有效载荷的PowerShell脚本，该脚本随后在4444端口上启动了Cobalt Strike shellcode侦听。

研究人员分析，新的恶意软件家族的出现可能与最近执法部门打击勒索软件攻击者的行动有关，旧组织的消亡将为新组织的出现创造空间，这个现象之前就发生过。2023年1月，美国司法部宣布对Hive勒索软件组织进行为期数月的行动。美国联邦调查局与外国执法合作伙伴一起，进入Hive网络并获取解密其软件的密钥后，缴获了其服务器，有效地破坏了Hive。自2022年8月以来，研究人员没有在Talos IR活动中观察到Hive勒索软件，这可能表明Hive操作已经停止，而前成员可能已经加入其他组织或以新名称重新另起炉灶。

**恶意OneNote文档在本季度继续被利用**

从2022年底到2023年初，Qakbot加载程序在本季度的所有活动中都利用了包含恶意OneNote文档的ZIP文件，这与终端遥测和关于网络钓鱼电子邮件中利用OneNote文档的威胁的公开报告一致。在一次Qakbot活动中，一个ZIP文件(“Inv\_02\_02\_#3.zip”)被检测为Qakbot，其中包含一个恶意的OneNote文档，该文档试图引诱用户点击“打开”，其中包含一个恶意的嵌入式URL。

虽然Talos IR本季度没有对任何Emotet事件做出回应，但Emotet在中断数月后，于2023年3月重新出现，恢复了其发送的垃圾邮件业务。在相对较短的时间内，Emotet多次修改其感染链，以最大限度地提高成功感染受害者的可能性。到3月中旬，Emotet已开始传播恶意OneNote文档，这表明攻击者将继续用更新的传播方法来感染受害者。

**初始攻击载体**

本季度有45%的攻击者利用面向公众的应用程序建立初始访问权限，比上一季度的15%有显著增长。在许多此类攻击中，web shell的使用导致攻击者试图攻击暴露在互联网上的基于web的服务器。有效帐户或具有弱密码或单因素身份验证的帐户也有助于在攻击者利用受感染凭据的情况下进行初始访问。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230503/1683063226819834.png "1683063226819834.png")

一些已知的漏洞导致对手通过利用面向公众的应用程序获得初始访问权限。在一次攻击活动中，Talos IR在AccessPress插件和主题中发现了与WordPress漏洞利用相一致的活动，经确定为CVE-221-24867。目前，Talos IR发现了大约20个不同的web shell，可能来自多个攻击者识别和利用这个旧漏洞。

在另一个web shell攻击中，Talos IR发现了一个易受攻击的Magento (Adobe Commerce) 2.4.2版本，该版本在被利用时正在Kubernetes部署中运行。Talos IR总共发现了该版本软件的九个已知漏洞，不包括扩展。Talos IR建议将Magento的所有实例升级到最新的可用版本，并定期检查需要修补或完全删除的易受攻击的过时扩展版本，以减少可用的攻击面。

**安全漏洞**

缺乏多因素身份验证(MFA)仍然是企业安全的最大障碍之一。近30%的组织要么没有MFA，要么只在少数账户和关键服务上启用了MFA。Talos IR经常观察到勒索软件和网络钓鱼事件，如果在关键服务，如终端检测响应(EDR)解决方案或vpn上正确启用MFA，其实这些事件本可以避免。为最大限度缓解初始访问载体，Talos IR建议禁用所有未使用MFA的帐户的VPN访问。

web shell攻击的增加凸显了在帮助防止web shell方面提高警惕的必要性。缓解措施如下所示：

定期更新和修补所有软件和操作系统，以识别和修复web应用程序和web服务器中的漏洞或错误配置；

除了修复漏洞之外，还要执行一般的系统强化，包括删除不必要的服务或协议，并注意所有直接暴露在互联网上的系统；

禁用“php.ini”中不必要的php函数，例如eval()， exec()， peopen()， proc\_open()和passthru()；

经常审计和审查来自web服务器的异常活动日志；

**观察到的MITRE ATT和CK技术最多**

下表显示了本季度Talos IR观察到的MITRE ATT和CK技术。考虑到一些技术可以属于多种策略，我们将它们分组在最相关的策略中。

MITRE ATT&CK框架的主要发现包括：

利用面向公众的应用程序是观察到的最常见的初始访问技术，而增加的web shell活动可能有助于这一重大观察。

攻击者经常使用PowerShell来支持多种威胁，研究人员已经观察到PowerShell的高使用率，此外还有许多其他脚本语言，包括Python、Unix shell和Windows命令shell，它们支持web shell执行。

开源安全工具包Mimikatz在本季度被用于支持近60%的勒索软件和预勒索软件。Mimikatz是一种广泛使用的漏洞利用后工具，用于从受攻击的Windows系统中窃取登录ID、密码和身份验证令牌。

1.Initial Access (TA0001) ，T1190 Exploit Public-Facing Application，Reconnaissance (TA0043) ，攻击者成功地利用了一个公开暴露在互联网上的易受攻击的应用程序；

2.T1592 Gather Victim Host Information，Persistence (TA0003) ，文本文件包含主机的详细信息；

3,T1505.003 Server Software Component: Web Shell，攻击者对基于web的服务器部署web shell；

4.Execution (TA0002)，T1059.001 Command and Scripting Interpreter: PowerShell，执行PowerShell代码来检索有关客户端Active Directory环境的信息；

5.Discovery (TA0007) ，T1046 Network Service Scanning，使用网络或端口扫描工具；

6.Credential Access (TA0006) ，T1003 OS Credential Dumping，部署Mimikatz和公开可用的密码查找实用程序；

7.Privilege Escalation (TA0004)，1484 Domain Policy Modification，修改GPO以执行恶意文件；

8.Lateral Movement (TA0008)，T1021.001 Remote Desktop Protocol，攻击者试图使用Windows远程桌面进行横向移动；

9.Defense Evasion (TA0005) ，T1027 Obfuscated Files or Information，使用base64编码的PowerShell脚本；

10.Command and Control (TA0011) ，T1105 Ingress Tool Transfer，攻击者从外部系统传输/下载工具；

11.Impact (TA0040)，T1486 Data Encrypted for Impact，部署Hive勒索软件并加密关键系统；

12.Exfiltration (TA0010) ，T1567 Exfiltration Over Web Service，使用合法的外部web服务来获取系统信息；

13.Collection (TA0009)，T1560.001 Archive Collected Data ，攻击者利用Windows上的xcopy复制文件；

14.Software/Tool，S0002 Mimikatz，使用Mimikatz获取帐户登录名和密码；

本文翻译自：https://blog.talosintelligence.com/quarterly-report-incident-response-trends-in-q1-2023/...