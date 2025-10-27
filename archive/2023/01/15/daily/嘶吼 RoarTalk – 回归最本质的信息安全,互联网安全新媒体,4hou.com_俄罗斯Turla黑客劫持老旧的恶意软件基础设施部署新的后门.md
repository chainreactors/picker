---
title: 俄罗斯Turla黑客劫持老旧的恶意软件基础设施部署新的后门
url: https://www.4hou.com/posts/DE4K
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-15
fetch_date: 2025-10-04T03:55:46.532072
---

# 俄罗斯Turla黑客劫持老旧的恶意软件基础设施部署新的后门

俄罗斯Turla黑客劫持老旧的恶意软件基础设施部署新的后门 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 俄罗斯Turla黑客劫持老旧的恶意软件基础设施部署新的后门

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)157562

收藏

导语：一个名为Turla的俄罗斯网络间谍组织利用一个10年前的恶意软件所使用的攻击基础设施，向乌克兰的攻击目标投放自己的侦察和后门工具。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673591373195844.jpeg "1673227598146450.jpeg")

据观察，一个名为Turla的俄罗斯网络间谍组织利用一个10年前的恶意软件所使用的攻击基础设施，向乌克兰的攻击目标投放自己的侦察和后门工具。

谷歌旗下的Mandiant将这个网络间谍组织编号为未加分类的UNC4210，声称被劫持的服务器对应于2013年上传到VirusTotal的一种名为ANDROMEDA（安德洛美达，又名Gamarue）的商用恶意软件的变体。

Mandiant的研究人员在上周发表的一份分析报告中称：“UNC4210在2022年9月重新注册了至少三个过期的ANDROMEDA指挥和控制（2）域名，开始对受害者进行分析，以便有所选择地部署KOPILUWAK和QUIETCANARY。”

Turla又叫Iron Hunter（钢铁猎手）、Krypton（氪）、Uroburos、Venomous Bearr（恶毒熊）和Waterbug（水蝽），这是一个手段高超的政府撑腰的组织，使用一大批的定制恶意软件，主要攻击敌国政府、外交和军事组织。

自2022年2月俄罗斯军事入侵乌克兰以来，这个敌对组织就与一系列针对乌克兰组织的凭据网络钓鱼和侦察行动有关。

2022年7月，谷歌的威胁分析小组（TAG）透露，Turla创建了一个恶意的安卓应用程序，据称是为了帮助亲乌克兰的黑客活动分子对俄罗斯网站发起分布式拒绝服务（DDoS）攻击。

Mandiant的最新发现表明，Turla一直在偷偷地利用旧的感染方法作为恶意软件分发机制，更不用说利用ANDROMEDA通过受感染的U盘来传播这个事实大做文章了。

这家威胁情报公司声称，通过USB传播恶意软件仍然是一条有用的途径，可以获得对组织的初始访问权。

在Mandiant分析的事件中，据称一只受感染的U盘于2021年12月被插入到了一家未具名的乌克兰组织的系统中，最终导致了一旦启动一个伪装成U盘内文件夹的恶意链接（. LNK）文件，就在主机上部署一个老式的ANDROMEDA恶意载荷。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673591374569798.png "1673227609107233.png")

图1. ANDROMEDA变成Turla团队入侵的时间表

然后，威胁分子对其中一个休眠的域名（这些域名是ANDROMEDA已废弃的C2基础设施的一部分）改头换面，他们在2022年1月重新注册了该域名，通过投放第一个阶段的KOPILUWAK 释放器（一种基于JavaScript的网络侦察实用工具），对受害者进行分析。

两天后即2022年9月8日，攻击进入到了最后阶段，执行了一个基于.NET的名为QUIETCANARY（又名Tunnus）的植入程序，导致2021年1月1日之后创建的文件被泄露。

Turla所使用的谍报技术与此前报道的有关该组织在俄乌战争期间广泛分析受害者的活动相一致，这可能有助于该组织调整后续利用漏洞的行动，以获取俄罗斯感兴趣的信息。

这也是一个罕见的例子，表明黑客团伙针对一起不同的恶意软件活动的受害者以实现自己的战略目标，同时竭力掩饰自己的行踪。

研究人员表示，随着旧的ANDROMEDA恶意软件继续从受攻击的USB设备传播，这些重新注册的域名带来了风险，因为新的威胁分子可以获得控制权，并向受害者发送新的恶意软件。

这种新颖的技术利用被广泛分布、以牟利为动机的恶意软件使用的过期域名，可以在随后攻击一大批实体。此外，防御者在分类鉴别各种各样的警报时更有可能忽略老旧的恶意软件和基础设施。

**COLDRIVER攻击美国核研究实验室**

发布上述研究结果的同时，路透社报道称，另一个由俄罗斯政府撑腰的代号为COLDRIVER（冷河，又名Callisto或SEABORGIUM）的威胁组织于2022年初攻击了美国的三家核研究实验室。

为此，数字攻击包括针对布鲁克海文国家实验室、阿尔贡国家实验室和劳伦斯利弗莫尔国家实验室创建了虚假的登录页面，企图欺骗核科学家们透露他们的密码。

这种策略与已知的COLDRIVER活动相一致，最近发现COLDRIVER活动欺骗了英国和美国的多家国防和情报咨询公司以及非政府组织、智库及高等教育组织的登录页面。

**攻陷指标**

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673591374119128.png "1673227662180293.png")

图2

**YARA规则**

KOPILUWAK

rule M\_APT\_Kopiluwak\_Recon\_1

{

    meta:

        author = "Mandiant"

    strings:

        $rc4\_1 = ".charCodeAt(i %"

        $rc4\_2 = ".length)) % 256"

        $b64\_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        $b64\_3 = ".charAt(parseInt("

        $recon\_1 = "WScript.CreateObject"

        $recon\_2 = ".Run("

        $Arguments = "WScript.Arguments"

    condition:

        ($rc4\_1 and $rc4\_2 and $b64\_1) and ($Arguments or ($b64\_3 and $recon\_1 and $recon\_2))

}

QUIETCANARY

rule M\_HUNTING\_QUIETCANARY\_STRINGS {

  meta:

        author="Mandiant"

  strings:

    $pdb1 = "c:\\Users\\Scott\\source\\repos\\Kapushka.Client\\BrowserTelemetry\\obj\\Release\\CmService.pdb" ascii wide nocase

    $pdb2 = "c:\\Users\\Scott\\source\\repos\\Kapushka.Client\\BrowserTelemetry\\obj\\Release\\BrowserTelemetry.pdb" ascii wide nocase

    $pdb3 = "c:\\Users\\Scott\\source\\repos\\BrowserTelemetry\\BrowserTelemetry\\obj\\Release\\BrowserTelemetry.pdb" ascii wide nocase

    $orb1 = {  68 00 74 00 74 00 70 00 73 00 3A 00 2F 00 2F }

    $orb2 = {  68 00 74 00 74 00 70 00 3A 00 2F 00 2F }

    $command1 = "get\_Command" ascii wide nocase

    $command2 = "set\_Command" ascii wide nocase

    $command3 = "DownloadCommand" ascii wide nocase

    $command4 = "UploadCommand"  ascii wide nocase

    $command5 = "AddCommand" ascii wide nocase

    $command6 = "ExeCommand" ascii wide nocase

    $command7 = "KillCommand" ascii wide nocase

    $command8 = "ClearCommand"  ascii wide nocase

      $rc4 = {21 00 62 00 76 00 7A 00 65 00 26 00 78 00 61 00 62 00 72 00 39 00 7C 00 38 00 5B 00 3F 00 78 00 77 00 7C 00 7C 00 79 00 26 00 7A 00 6C 00 23 00 74 00 70 00

6B 00 7A 00 6A 00 5E 00 62 00 39 00 61 00 38 00 6A 00 5D 00 40 00 6D 00 39 00 6E 00 28 00 67 00 67 00 24 00 40 00 74 00 74 00 65 00 33 00 33 00 6E 00 28 00 32 00 72 00 7A

00 62 00 7A 00 69 00 74 00 75 00 31 00 2A 00 66 00 61 00 00 80 E9 4D 00 6F 00 7A 00 69 00 6C 00 6C 00 61 }

  condition:

    (1 of ($pdb\*)) and (1 of ($orb\*)) and (all of ($command\*)) or ($rc4)

}

**网络规则**

ANDROMEDA

alert tcp any any -> any any ( msg:"503 irc\_bot\_cmd Trojan.Downloader.Andromeda AI callback-trojan block"; content:".php HTTP/1"; nocase; content:"|0a|"; content:"|0a|"; within:4; content:"POST "; content:"Mozilla/4.0|0d 0a|"; content:!"Referer: "; nocase; content:!"Cookie: "; nocase; content:!"Accept-Language: "; nocase; content:!"Accept-Encoding: "; nocase; content:!"pharma"; nocase; content:!"|0d0a|TE:"; nocase; pcre:"/POST (http\:\/\/\S\*\.[a-z0-9]{1,4})?/[a-z]{1,3}\.php HTTP/"; reference:fe\_date,2013-07-11; reference:a\_type,mal.dsh; reference:mal\_hash,bc76bd7b332aa8f6aedbb8e11b7ba9b6; priority:90; sid:89039193; rev:3; )

**MITRE ATT&CK**

|  |  |  |
| --- | --- | --- |
| ATT&CK战术类别 | 技术 | |
| 防御规避 | | |
|  | T1027: | 经过混淆处理的文件或信息 |
|  | T1055: | 进程注入 |
|  | T1070.004: | 文件删除 |
|  | T1112: | 篡改注册表 |
|  | T1564.003: | 隐藏的窗口 |
|  | T1622: | 调试器规避 |
| 持续性 | | |
|  | T1547.001 | 注册表运行键/启动文件夹 |
| 发现 | | |
|  | T1010: | 应用程序窗口发现 |
|  | T1012: | 查询注册表 |
|  | T1033: | 系统所有者/使用者发现 |
|  | T1049: | 系统网络连接发现 |
|  | T1057: | 进程发现 |
|  | T1082: | 系统信息发现 |
|  | T1083: | 文件和目录发现 |
|  | T1518: | 软件发现 |
| 收集 | | |
|  | T1560: | 归档收集的数据 |
|  | T1560.001: | 通过实用工具来归档 |
| 资源开发 | | |
|  | T1584: | 攻陷基础设施 |
|  | T1608.003: | 安装数字证书 |
| 指挥和控制 | | |
|  | T1071.001: | 互联网协议 |
|  | T1573.002: | 非对称加密 |
| 影响 | | |
|  | T1529: | 系统关闭/重启 |

参考及来源：
https://thehackernews.com/2023/01/russian-turla-hackers-hijack-decade-old.html
https://www.mandiant.com/resources/blog/turla-galaxy-opportunity如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BNWJrVAv)

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

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利...