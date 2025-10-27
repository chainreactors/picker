---
title: Black Basta 勒索软件组织通过QAKBOT，Brute Ratel和Cobalt Strike渗透网络
url: https://www.4hou.com/posts/ykyw
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-25
fetch_date: 2025-10-03T20:44:40.850609
---

# Black Basta 勒索软件组织通过QAKBOT，Brute Ratel和Cobalt Strike渗透网络

Black Basta 勒索软件组织通过QAKBOT，Brute Ratel和Cobalt Strike渗透网络 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Black Basta 勒索软件组织通过QAKBOT，Brute Ratel和Cobalt Strike渗透网络

luochicun
[技术](https://www.4hou.com/category/technology)
2022-10-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)123058

收藏

导语：趋势科技的研究人员最近分析了一个与QAKBOT相关的示例，该示例导致了Brute Ratel C4和Cobalt Strike有效负载，这可以归因于Black Basta 勒索软件组织。

趋势科技的研究人员最近分析了一个与QAKBOT相关的示例，该示例导致了Brute Ratel C4和Cobalt Strike有效负载，这可以归因于Black Basta 勒索软件组织。

QAKBOT的恶意软件在短暂中断后于2022年9月8日恢复传播，当时研究人员在这一天发现了几个传播机制。观察到的传播方法包括SmokeLoader(使用' snow0x '传播器ID)， Emotet(使用' azd '传播器ID)，以及使用' BB '和' Obama20x ' ID的恶意垃圾邮件。

最近一个涉及 QAKBOT ‘BB’ 传播器的示例导致部署了Brute Ratel(被趋势科技检测为Backdoor.Win64.BRUTEL)，这是一个类似于Cobalt Strike的框架，作为第二阶段有效负载。这是一个值得注意的进展，因为这是我们第一次通过QAKBOT感染观察到Brute Ratel作为第二阶段有效负载。这次攻击还包括使用Cobalt Strike进行横向移动。研究人员认为这些活动是Black Basta 勒索软件组织所为。

**攻击的时间表**

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626798170882.png "1665626798170882.png")

Brute Ratel和其他C&C框架的兴起

与CobaltStrike一样,BruteRatel是一种攻击模拟工具，是商业C&C框架领域的相对新的工具，它在该领域与更成熟的竞争者如Cobalt Strike竞争。

像Brute Ratel和Cobalt Strike这样的攻击模拟框架经常会被渗透测试专业人员使用，用于合法的渗透测试活动，在这些活动中组织寻求提高他们检测和响应真实网络攻击的能力。这些框架用于从远程位置提供实际的键盘访问，以模拟攻击者在网络攻击中使用的战术、技术和过程(TTP)。

除了Cobalt Strike的合法使用示例外，它还因非法使用而臭名昭著，在过去几年里，它几乎经常出现在勒索软件攻击中。它用作僵尸网络的常见第二阶段有效载荷，例如QAKBOT (TrojanSpy.Win64.QAKBOT)，IcedID (TrojanSpy.Win64.ICEDID)，Emotet (TrojanSpy.Win64.EMOTET) 和Bumblebee (Trojan.Win64.BUMBLELOADER) 等。不幸的是，在过去的几年中，Cobalt Strike的几个版本已被泄露，从而加速了攻击者的恶意使用。

与Brute Ratel相比，由于其受欢迎程度高，其检测覆盖率比后者更大。这使得Brute Ratel和其他不太成熟的C&C框架对恶意攻击者来说越来越有吸引力，他们的活动可能在很长一段时间内都不会被发现。

Brute Ratel最近在黑市非常受欢迎，该框架的版本在地下组织中交易非常活跃，并发布了破解版本。Brute Ratel的开发人员在最近的Twitter帖子中承认了这一漏洞。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626807124774.png "1665626807124774.png")

QAKBOT 'BB' 到Brute Ratel

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626815130109.png "1665626815130109.png")

攻击活动概况

该活动通过垃圾邮件开始，其中包含发送给潜在受害者的恶意新URL。URL登录页面向收件人显示ZIP文件的密码。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626824322520.png "1665626824322520.png")

已下载ZIP文件以及文件密码的通知

**绕过沙盒和安全检测**

在此阶段使用受密码保护的ZIP文件可能是为了逃避安全解决方案的分析。

**绕过安全检测的标志**

ZIP文件包含一个. iso文件。使用ISO文件是为了破坏“Mark of the Web (MOTW)” ，该标记将文件标记为从互联网下载。它使这些文件受到Windows和终端安全解决方案的其他安全措施的影响。ISO文件包含一个使用“Explorer”图标的可见LNK文件和两个隐藏的子目录，每个子目录包含各种文件和目录。默认情况下，Windows操作系统不向用户显示隐藏文件。下图说明了启用“显示隐藏文件”设置时用户看到的内容。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626832163869.png "1665626832163869.png")

启用“显示隐藏文件”设置时，用户看到的添加隐藏子目录

目录结构如下：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626840459223.png "1665626840459223.png")

目录结构

**命令行界面的执行顺序**

QAKBOT在两个脚本文件之间使用模糊处理，一个JavaScript (.js)文件和一个批处理脚本(.cmd)文件，很可能是为了隐藏看起来可疑的命令行。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626849139179.png "1665626849139179.png")

命令行接口的执行顺序

**初始QAKBOT C&C服务器通信**

C & C基础设施在地理上分布在主要位于住宅Internet服务提供商 (ISP) 宽带网络中的受损主机上。

这些“第1层”C&C服务器被QAKBOT运营商认为是一次性的，并且几乎每次有新的恶意软件传播时经常被更换，尽管有些服务器在多个QAKBOT恶意软件配置中仍然存在。

**自动化侦察命令**

在最初的C&C通信之后仅6分钟，并且QAKBOT恶意软件现在在注入的进程(wermgr.exe)中运行，通过执行多个内置命令行工具在受感染的环境中执行自动侦察。这些命令行的执行顺序如下：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626858438437.png "1665626858438437.png")

内置命令行的执行顺序

该活动在趋势科技Vision One™中可见，它可以检测到这些内置Windows命令的可疑使用。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626867188964.png "1665626867188964.png")

显示与wermgr.exe相关的活动

**QAKBOT释放Brute Ratel**

自动侦察活动完成五分钟后，注入QAKBOT的wermgr.exe进程释放Brute Ratel DLL，并通过带有“main”导出函数的rundll32.exe子进程调用它。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626920543737.png "1665626920543737.png")

Brute Ratel被wermgr.exe通过rundll32.exe进程调用

该后门是一个HTTPS，它在symantecuptimehost[.]com执行拥有Brute Ratel服务器的签入：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626929143662.png "1665626929143662.png")

Brute Ratel签入

在环境中执行进一步的侦察，以识别特权用户。首先，使用内置的net.exe和nltest.exe。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626938153767.png "1665626938153767.png")

识别特权用户的侦察过程

其次，SharpHound实用程序通过Brute Ratel在注入的svchost.exe进程中运行，以输出JSON文件，这些文件被输入到BloodHound，并被标记为Active Directory组织单元、组策略、域、用户组、计算机和用户。然后将这些文件打包到一个ZIP文件中，以便为信息窃取做准备。整个过程都是脚本化的，只需不到两秒钟就可以完成。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626947144383.png "1665626947144383.png")

通过svchost.exe输出JSON文件

**Brute Ratel释放Cobalt Strike**

有趣的是，攻击者选择利用Cobalt Strike进行横向移动。将几个信标文件中的第一个文件放到运行Brute Ratel C4的受感染终端上，第一个文件为：C:\Users\Public\Name-123456.xls。

使用以下命令在运行Brute Ratel C4的同一主机上执行此信标文件：rundll32 C:\users\public\Name-123456.xls,DllRegisterServer。

接下来，攻击者释放其他信标文件，并将这些文件复制到网络上其他主机上的管理共享，再次使用带有XLS附件的文件名。

C:\Users\Public\abcabc.xls

C:\Users\Public\abc-1234.xls

C:\Users\Public\Orders\_12\_34\_56.xls

C:\Users\Public\MkDir.xls

用于复制文件的命令如下：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626957124772.png "1665626957124772.png")

以下列表是信标C & C服务器：

hxxps://fewifasoc[.]com | 45.153.242[.]251

hxxps://hadujaza[.]com | 45.153.241[.]88

hxxps://himiketiv[.]com | 45.153.241[.]64

在采取任何最终行动之前，攻击者会被从环境中驱逐出去。

**到Brute Ratel的QAKBOT ‘Obama’**

在另一个事件中，趋势科技发现QAKBOT使用‘Obama’传播者ID前缀(即 “Obama208”)也将Brutel Ratel C4作为第二级有效负载。

在此示例中，恶意软件以受密码保护的ZIP文件的形式通过HTML走私传递，这允许攻击者“走私”编码的恶意脚本到HTML附件或网页。一旦用户在浏览器中打开HTML页面，就会解码脚本并组装有效负载。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665626967933805.png "1665626967933805.png")

QAKBOT传播者使用密码保护来抵御网络和沙箱安全扫描

一旦使用HTML附件中提供的密码解密了ZIP文件，用户就会看到一个ISO文件。恶意文件包含在ISO文件中，被用作Web绕过的标记。在内部，ISO文件包含以下目录结构：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665627253500548.png "1665627253500548.png")

ISO文件目录结构

自从QAKBOT回归以来，研究人员观察到执行链中的多种形式，从脚本语言到文件扩展名，再到导出函数名和序号的使用。对于这种感染，使用的是以下变体：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665627068164016.png "1665627068164016.png")

感染过程与上述攻击中描述的TTP(战术、技术和程序)相同。但是，在C2配置中观察到一个显着差异，与更传统的HTTPS C2通道相比该配置使用HTTPS (DoH) 上的DNS。观察到的C & C服务器使用了带有let's-Encrypt的HTTPS。

通过使用DoH，攻击者可以隐藏C2域的DNS查询。如果没有使用中间人 (MitM) 技术检查SSL/TLS流量，则对C2服务器的DNS查询将不会被注意到。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665627054182990.png "1665627054182990.png")

通过HTTPS (DoH)上的DNS执行C & C通信的Brute Ratel进程。在采取任何最终行动之前，攻击已经得到缓解

**与Black Basta的关系**

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665627039161457.png "1665627039161457.png")

QakBot到Black Basta攻击中使用的Brute Ratel和Cobalt Strike基础结构

根据调查，研究人员可以确定 QAKBOT-to-Brute Ratel-to-Cobalt Strike攻击链与Black Basta组织有关。这是基于在Blac...