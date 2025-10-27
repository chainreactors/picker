---
title: UEFI固件使用OpenSSL暴露了软件材料清单（SBOM）的弱点，戴尔、惠普和联想中招
url: https://www.4hou.com/posts/VZMo
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:04.501892
---

# UEFI固件使用OpenSSL暴露了软件材料清单（SBOM）的弱点，戴尔、惠普和联想中招

UEFI固件使用OpenSSL暴露了软件材料清单（SBOM）的弱点，戴尔、惠普和联想中招 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# UEFI固件使用OpenSSL暴露了软件材料清单（SBOM）的弱点，戴尔、惠普和联想中招

布加迪
[新闻](https://www.4hou.com/category/news)
2022-12-11 19:28:14

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)158193

收藏

导语：Binarly REsearch团队近日深入研究了最近的OpenSSL安全更新给UEFI固件供应链生态系统带来怎样的影响以及OpenSSL版本在固件环境中是如何广泛使用的。

Binarly REsearch团队近日深入研究了最近的OpenSSL安全更新给UEFI固件供应链生态系统带来怎样的影响以及OpenSSL版本在固件环境中是如何广泛使用的。研究结果不容乐观。

科技行业正在积极讨论使用“软件材料清单”（SBOM）来化解供应链安全风险。为了确保供应链安全实践落地，必须加强软件依赖项方面的透明度。以前，任何一款软件作为黑盒子来发布，并不提供与软件依赖项和第三方组件相关的任何信息。固件在很大程度上也是如此。Binarly团队在之前的一篇博文中讨论了UEFI固件生态系统的多重复杂性和供应链分类，有兴趣的读者可以参阅：https://binarly.io/posts/The\_Firmware\_Supply\_Chain\_Security\_is\_broken\_Can\_we\_fix\_it。

SBOM是否有助于加强专有固件软件包的透明度？答案很复杂。SBOM有助于人们更好地了解依赖项，但在许多情况下，诸厂商将SBOM信息与固件软件包或映像文件分开来分发。当SBOM不相关或可能含有误导性信息时，这就产生了与之前关于供应链问题的讨论相同的问题。现在我们的供应链与SBOM密切相关，在许多情况下，SBOM是厂商提供的信息的静态快照。

当固件不含有相应的源代码时，如果没有全面的代码分析基础设施，很难基于编译后的二进制模块来验证SBOM信息。

本月早些时候，CISA发布了一份与OpenSSL最近的高危安全问题（CVE-2022-3602和CVE-2022-3786）相关的安全公告。CVE-2022-3602和CVE-2022-3786这两个安全漏洞都与x.509证书验证失败有关，证书验证失败可能导致基于堆栈的缓冲区溢出。事实上，较旧的版本不受影响，比如OpenSSL 1.0.2和1.1.1。早期版本也不受影响，因为易受攻击的代码是在OpenSSL 3.0.0中首次引入的。

Binarly REsearch团队决定深入研究这种紧急更新给UEFI固件供应链生态系统带来了怎样的影响以及OpenSSL版本在固件环境中是如何广泛使用的。

**深入核心**

核心框架之一EDKII作为任何UEFI固件的一部分来使用，它在CryptoPkg组件中有自己的子模块和OpenSSL包装器库（OpensslLib）。Github上的主要EDKII存储库经常更新，开发者社区经常关注安全问题。但其中一个主要问题是，这些更新给终端设备的供应链又带来了怎样的影响。

在许多情况下，固件是供应链所有层和终端客户设备之间的单一故障点。

我们以前强调过，即使在设备厂商知道漏洞之后，在端点设备上部署这些补丁时，仍会一再出现失败。但是说到第三方相关的代码，就会带来围绕补丁部署的更复杂问题。

微软最近在《2022年数字防御报告》中强调：分析的固件映像中32%含有至少10个已知的严重漏洞。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221126/1669421350119509.png "1669421271796918.png")

图1

我们在自己的遥测数据中也看到了这一趋势，证实这股势头在上升。据Binarly Platform在调查企业级厂商后得到的数据显示，大约20%的固件更新含有至少两到三个已知的漏洞（以前披露过）。

与利用新的漏洞（0-day）相比，部署使用1/N-day漏洞的固件攻击的成本大幅降低。

不妨进一步了解联想Thinkpad企业设备，以及在一个固件映像中使用了多少个不同版本的OpenSSL。

| OpenSSL版本 | 模块 |
| --- | --- |
| 1.0.2j | DxeCore,   Tcg2Dxe, TcgDxe, VariableSmm, SecurityStubDxe, IpSecDxe, IScsiDxe, Setup,   PlatformMilestoneHookDxe, PlatformMilestoneHookSmm, LenovoTpmConfigDxe,   PlatformInit, PeimBoardInit, PeimBoardInit, PeimBoardInit, Tcg2Pei, TcgPei,   PlatformInitPreMem, LenovoPcdInit, LenovoVerifiedBootPei |
| 1.0.0a | FlashUtilitySmm,   LenovoCryptService, LenovoCryptServiceSmm, LenovoSvpManagerSmm,   LenovoSetupAutomationSmm, LenovoSetupUnderOsSmm, LenovoSecureKeySmm,   LenovoDriveEraseSmm |
| 0.9.8zb | InfineonTpmUpdateDxe |

我们可以看到，同一个固件二进制包中至少使用了三个不同版本的OpenSSL：1.0.0a（2014）、1.0.2j（2018）和0.9.8zb（2014）。最新的OpenSSL版本是在2018年发布的，因此已过时四年。

许多与安全相关的固件模块含有明显过时的OpenSSL版本。其中一些模块（比如InfineonTpmUpdateDxe）含有已知过时至少八年的易受攻击的代码。InfineonTpmUpdateDxe模块负责更新英飞凌芯片上可信任平台模块（TPM）的固件。这清楚地表明了第三方依赖项存在的供应链问题，这些依赖项看起来从未收到更新，哪怕针对严重的安全问题。

在联想企业设备上使用的OpenSSL的最新版本可以追溯到2021年夏天。下图显示了Binarly Platform检测到的所有OpenSSL版本（用于最新的固件更新）和Linux供应商固件服务（LVFS）公共数据内容：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221126/1669421353547640.png "1669421292107661.png")

图2

这些表清楚地反映了总体情况和同一设备固件代码中使用不同OpenSSL版本的多样化程度。为了更好地了解OpenSSL数据，不妨看看不同版本与各大企业厂商的设备上的发布日期有怎样的联系。

| 设备厂商 | OpenSSL版本 | 发布日期 |
| --- | --- | --- |
| 联想和戴尔 | 0.9.8l | 05-Nov-2009 |
| 联想、戴尔和惠普 | 0.9.8w | 24-Apr-2012 |
| 联想和惠普 | 0.9.8zb | 06-Aug-2014 |
| 联想 | 0.9.8zd | 08-Jan-2015 |
| 联想 | 0.9.8ze | 15-Jan-2015 |
| 联想 | 0.9.8zf | 19-Mar-2015 |
| 联想 | 1.0.0a | 01-Jun-2010 |
| 联想 | 1.0.2d | 09-Jul-2015 |
| 联想 | 1.0.2f | 28-Jan-2016 |
| 联想和戴尔 | 1.0.2g | 01-Mar-2016 |
| 联想 | 1.0.2h | 03-May-2016 |
| 联想、戴尔和惠普 | 1.0.2j | 26-Sep-2016 |
| 联想和戴尔 | 1.0.2k | 26-Jan-2017 |
| 联想、戴尔和惠普 | 1.0.2u | 20-Dec-2019 |
| 联想 | 1.1.0b | 26-Sep-2016 |
| 联想 | 1.1.0g | 02-Nov-2017 |
| 联想和戴尔 | 1.1.0h | 27-Mar-2018 |
| 联想和戴尔 | 1.1.0j | 20-Nov-2018 |
| 联想 | 1.1.1d | 10-Sep-2019 |
| 联想和戴尔 | 1.1.1l | 24-Aug-2021 |
| 戴尔 | 1.1.0e | 16-Feb-2017 |
| 戴尔 | 1.1.1n | 15-Mar-2022 |

我们从Binarly OpenSSL的研究数据中可以看出，固件常常使用多个版本的OpenSSL。其背后的原因是，第三方代码的供应链依赖它们各自的代码库，而设备固件开发人员常常无法获得这些代码库。这就增加了供应链的复杂性。大多数OpenSSL依赖项作为库静态链接到特定的固件模块，这些模块创建编译时依赖项，如果没有深入分析代码的功能，就很难识别这些依赖项。在过去，第三方代码依赖项的问题不是在编译代码层面就能轻松解决的问题。

行业目前采取的做法是为单独的模块生成散列，与特定的版本版本号相关联，以便连接SBOM层面的依赖项列表。这种做法适用于开源项目（比如用于验证的Sigstore项目），但面对闭源生态系统，它总是以失败告终。虽然散列提供了完整性信息，但无法为闭源项目保证SBOM内容和完整性。从这个意义上说，涉及到在二进制层面进行验证的编译代码时，我们迫切需要一个额外的SBOM验证层，即与厂商提供的实际SBOM相匹配的第三方依赖项信息列表。

完整性提供不了代码级别的可见性，根据二进制模块的散列确定依赖项的范围很困难。当依赖项是间接的，隐藏在代码抽象层中时，尤其困难重重。

遗憾的是，说到二进制代码分析，没有简单的解决办法，业界在如何思考基于SBOM的供应链安全解决方案方面需要改变观念。说到封装的第三方代码，依赖项列表总是不尽如人意。“信任但验证”的方法是处理SBOM失败和降低供应链风险的最佳方法。

本文翻译自：https://www.binarly.io/posts/OpenSSL\_Usage\_in\_UEFI\_Firmware\_Exposes\_Weakness\_in\_SBOMs/index.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?jQX8sEMK)

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
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/si...