---
title: Muddled Libra精准高效的攻击组合力让人防不胜防
url: https://www.4hou.com/posts/1pVq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-30
fetch_date: 2025-10-04T11:44:35.164023
---

# Muddled Libra精准高效的攻击组合力让人防不胜防

Muddled Libra精准高效的攻击组合力让人防不胜防 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Muddled Libra精准高效的攻击组合力让人防不胜防

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-06-29 11:20:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128665

收藏

导语：2022年底，随着0ktapus网络钓鱼工具包的发布，Muddled Libra正式出现在公众视野。

2022年底，随着0ktapus网络钓鱼工具包的发布，Muddled Libra正式出现在公众视野，该工具包提供了预构建的托管框架和捆绑模板，利用大量用虚假身份验证的真实门户进行有针对性的攻击，攻击者能够快速收集凭据和多因素身份验证MFA代码。如今0ktapus框架已被商品化，即使是攻击新手也能获得很高的成功率。0ktapus框架功能包括预构建的模板和通过Telegram内置的C2频道，成本只需几百美元。

这个工具包所攻击的目标的数量之多，以至于给攻击归属造成了很多困惑。Group IB、CrowdStrike和Okta之前的报告已经记录并将其中许多攻击映射到以下组织：0ktapus、Scattered Spider和Scatterd Swine。以上三个名字很可能是一个组织，也很可能是使用同一个工具包的三个组织。Muddled Libra就是其中的一个组织。

Unit 42发现Muddled Libra攻击时具有以下特点：

**·**使用0ktapus网络钓鱼工具包；

**·**持续攻击；

**·**非破坏性存在；

**·**持续瞄准业务流程外包（BPO）行业；

**·**数据被盗；

**·** 在下游攻击中使用受攻击的基础设施；

调查表明Muddled Libra使用了一个异常庞大的攻击工具包，包括社会工程、渗透测试和取证工具，其功能要强于强大的网络防御能力。

在Unit 42调查的事件中，Muddled Libra在攻击目标选择上非常有针对性，进攻策略也非常灵活。当一个攻击方法被阻断时，他们要么迅速转向另一个方法，要么转化攻击环境重新开始攻击。

Muddled Libra也对现代事件响应（IR）框架有着深刻理解，这使他们能够不断修改攻击策略从而实现攻击目的。

Muddled Libra更倾向于使用被盗数据来对受害者发起攻击，如果允许，他们会反复刷新被盗数据集。使用这些被盗数据，即使在最初的事件响应之后，攻击者也有能力回到以前的受害者那里。这证明了攻击者即使在被发现后仍具有持续攻击能力。

此外，Muddled Libra似乎对他们的攻击行为有明确的预期和路径设计，而不仅仅是投机取巧那么简单。他们在发动攻击时，会迅速寻找并窃取了下游客户端环境中的信息，然后利用这些信息进入到攻击环境中。他们对高价值客户以及对后续攻击最有用的信息有着1前瞻性判断。

**攻击链**

虽然每一起事件都是独一无二的，但Unit 42的研究人员已经确定了战术、技术和程序（TTP）方面的很过共性，可以将多起事件归因于Muddled Libra。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688005534178112.png "1687929052651863.png")

攻击链

**侦察阶段**

Muddled Libra对目标组织有着非常细致的了解，包括员工名单、职务和手机号码。在某些情况下，这些数据可能是在早期针对上游目标的攻击行为中获得的。

攻击者还经常从非法数据代理那里获取信息包，例如现已倒闭的Genesis和Russian Markets。这些数据通常是从受感染的设备上收集的，包括企业和个人设备，使用的是像RedLine stealer这样的恶意软件。

随着自带设备（BYOD）政策的早期出现，以及混合工作解决方案的流行，公司数据和凭据被频繁使用并缓存在个人设备上。分散IT资产的管理和保护为信息窃取恶意软件创造了一个有利可图的攻击机会。

**资源开发**

使用相似域名发起攻击是Muddled Libra的经典标志。这种策略是有效的，因为移动设备经常截断SMS消息中的链接。

归因于0ktapus活动的早期攻击组织一直使用通过Porkbun或Namecheap注册并托管在Digital Ocean（一家成立于2012年的总部设置在纽约的云主机商家，采用KVM虚拟）基础设施上的域名，这些域往往是短暂的，只在最初的访问阶段使用，然后很快被删除。

Unit 42注意到攻击者使用ktapus网络钓鱼工具包来获取凭证。Group-IB详细记录了这种多用途的工具，在地下组织中广泛使用。它几乎不需要什么技能就可以安装和配置，这使它成为高度针对性的欺骗攻击的理想工具。

**初始访问**

在Unit 42可以确定初始访问方法的所有事件中，都涉及诈骗或社会工程。在大多数事件中，攻击者直接向目标员工的手机发送引诱信息，声称他们需要更新账户信息或重新验证公司应用程序。消息中包含一个指向伪造公司域的链接，该域旨在模仿熟悉的登录页面。

**持久性**

Muddled Libra特别专注于维护对目标环境的访问。虽然攻击者在攻击期间使用免费或演示版的远程监控和管理（RMM）工具是很常见的，但Muddled Libra通常安装了六个或更多这样的实用程序。他们这样做是为了确保即使有一个被发现，他们也能保留一个进入环境的后门。

使用商业RMM工具尤其需要注意，因为这些工具是Muddled Libra正在滥用的合法程序。他们可以合法地出现在组织内，防御者应该权衡是完全阻止还是仔细监控他们。观察到的工具包括Zoho Assist、AnyDesk、Splashtop、TeamViewer、ITarian、FleetDeck、ASG Remote Desktop、RustDesk和ManageEngine RMM。

这些工具本身都不是恶意的，并且经常用于许多企业网络的日常管理。Unit 42建议组织通过签名者阻止任何不允许在企业内使用的RMM工具。

**防御规避**

Muddled Libra对各种安全控制及其熟悉，完美地避开了常见的防御。

具体行为包括：

**·**禁用防病毒和基于主机的防火墙；

**·**试图删除防火墙配置文件；

**·**绕过防御者；

**·**停用或卸载EDR和其他监控产品；

攻击者还重新启用并使用了现有的Active Directory帐户，以避免触发公共安全信息和事件管理（SIEM）监控规则。他们还被观察到在终端检测和响应（EDR）管理控制台内操作以清除警报。

Muddled Libra在攻击活动中很谨慎，一直使用商业虚拟专用网络（VPN）服务来隐藏其地理位置，并试图融入合法流量。在Unit 42研究人员调查的大多数事件中，Mullvad VPN是首选，但也观察到许多其他供应商，如ExpressVPN、NordVPN、Ultrasurf、Easy VPN和ZenMate。

Unit 42的研究人员还观察到了轮流使用住宅代理服务的情况。正如Brian Krebs在2021年报道的那样，住宅代理服务通常将其代码隐藏在浏览器扩展中，允许运营商将住宅连接出租给合法和恶意攻击者。

**凭据访问**

一旦捕获了用于初始访问的凭据，攻击者就会选择其中一条路径。在第一种情况下，他们继续从他们控制的计算机进行身份验证，并立即请求多因素身份验证（MFA）代码。在另一种情况下，他们随后生成了一系列MFA提示，直到用户接受其中一个，这种方法也称为MFA轰炸。

在MFA轰炸失败的情况下，攻击者就会联系该组织的求助台，声称自己是受害者。然后谎称他们的手机无法操作或放错地方，并要求注册一个新的、由攻击者控制的MFA身份验证设备。

Muddled Libra在社会工程方面的成功是值得注意的。在许多示例中，该组织通过电话与服务台和其他员工交流，实施攻击活动。

在建立了立足点后，Muddled Libra迅速采取行动，提升访问权限。本阶段使用的标准凭证窃取工具包括Mimikatz、ProcDump、DCSync、Raccoon Stealer和LAPSToolkit。当该组织无法快速确定提升的凭据时，他们就会使用Impacket、MIT Kerberos Ticket Manager和NTLM编码器/解码器。

在一些事件中，Muddled Libra采取了不同寻常的步骤，使用专门的工具，使用MAGNET RAM Capture和Volatility直接搜索内存内容以查找凭据。由于这些都是Muddled Libra正在滥用的合法取证工具，防御者应该仔细考虑阻止它们的不利因素，包括安全团队活动产生误报警报的可能性。

这给防御者提出了一个挑战，尽管用户帐户可能通过特权访问管理受到保护，但终端通常具有缓存用于系统管理或运行服务的提升凭据。应注意确保特权凭据仅具有执行其预期功能所需的权限，并密切监控其是否偏离正常行为。

**发现过程**

muddle Libra的发现方法在不同的示例中是一致的。在调查中，该组织使用了知名的合法渗透测试工具来绘制环境并确定感兴趣的目标。他们的工具包包括SharpHound, ADRecon, AD Explorer, Angry IP Scanner, Angry Port Scanner和CIMplant。

事实证明，Muddled Libra还精通商业系统管理工具，如用于发现和自动化的ManageEngine、LANDESK和PDQ Inventory，虚拟环境中使用的VMware PowerCLI和RVTools。

防御者应警惕未经批准的网络扫描和对多个系统的异常快速访问或跨逻辑业务部门的访问。

**执行过程**

调查发现，Muddled Libra似乎主要对数据和凭据盗窃感兴趣，我们很少看到远程执行。当需要时，该组织使用Sysinternals PsExec或Impacket完成执行。捕获的凭据或身份验证哈希用于权限提升。

**横向活动**

对于横向活动，Muddled Libra更喜欢使用来自受攻击设备的远程桌面协议（RDP）。这种方法有助于最大限度地减少日志中可发现的外部网络构件，这些构件可以提醒防御者并帮助调查人员进行追踪。

**寻找目标数据**

Muddled Libra似乎非常了解企业数据管理。他们成功地在受害者设备上的各种常见数据存储库中找到敏感数据，包括结构化和非结构化数据存储库，比如：

**·**Confluence；

**·**Git；

**·**Elastic；

**·**Microsoft Office 365 suite (e.g., SharePoint, Outlook)；

**·**Internal messaging platforms；

他们还从Zendesk和Jira等常见服务台应用程序中查找受害者环境中的数据。挖掘的数据包括进一步泄露的凭据，它们直接针对敏感和机密信息。

Unit 42的研究人员还观察到了开源数据挖掘工具Snafler和本地工具在注册中心、本地驱动器和网络共享中搜索\*password\*和securestring等关键词的情况。然后，使用WinRAR或PeaZip对泄露的数据进行分级和存档。

防御者应定期在自己的环境中执行关键字搜索，以识别不正确存储的数据和凭证。

**盗取数据**

在一些情况下，Muddled Libra试图建立反向代理shell或secure shell（SSH）隧道，用于命令和控制或盗取。Muddled Libra还使用了常见的文件传输网站，如put[.]io、transfer[.]sh、wasabi[.]com或gofile[.]io来盗取数据，研究人员还观察到Cyberduck作为文件传输代理。

**缓解措施**

Muddled Libra是一个攻击能力非常强的恶意软件，对软件自动化、业务流程外包、电信和技术行业的组织构成了巨大威胁。他们精通一系列安全规范，能够在相对安全的环境中迅速执行以完成毁灭性的攻击。

Muddled Libra并没有任何技术上的创新，只是把目前已有的技术叠加在一起从而产生了很强的攻击力。

**建议组织：**

1.尽可能实现MFA和单点登录（SSO），最好是快速身份在线（FIDO）。在我们调查的示例中，Muddled Libra最成功的是说服攻击目标帮助他们绕过MFA。当他们无法做到这一点时，他们就会更换其他目标。

2.防御者还应考虑如何在多次MFA故障时最好地实施安全警报和帐户锁定。

3.实施员工安全意识培训。Muddled Libra通过电话和短信大力实施社会工程，包括通过电话和短信帮助台。

4.在发生攻击的情况下，假设这个攻击者知道现代IR战术，考虑建立带外响应机制。

5.确保证书是最新的，只在必要的时候和时间内授予访问权限。

6.监控和管理对关键防御和控制的访问对于防御熟练攻击者至关重要。权利应仅限于每个工作职能所必需的内容。应使用Cortex XDR和Cortex XSIAM等身份威胁检测和响应（ITDR）工具来监测异常行为。

7.防御者应该限制允许连接到网络的匿名服务，最好是在防火墙上通过App-ID。

本文翻译自：https://unit42.paloaltonetworks.com/muddled-libra/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?yooyLABV)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [Armour...