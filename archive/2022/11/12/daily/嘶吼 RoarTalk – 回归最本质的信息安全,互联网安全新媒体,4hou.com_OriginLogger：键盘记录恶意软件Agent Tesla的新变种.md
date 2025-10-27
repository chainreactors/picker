---
title: OriginLogger：键盘记录恶意软件Agent Tesla的新变种
url: https://www.4hou.com/posts/BE7x
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-12
fetch_date: 2025-10-03T22:28:56.870303
---

# OriginLogger：键盘记录恶意软件Agent Tesla的新变种

OriginLogger：键盘记录恶意软件Agent Tesla的新变种 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# OriginLogger：键盘记录恶意软件Agent Tesla的新变种

lucywang
[技术](https://www.4hou.com/category/technology)
2022-11-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144365

收藏

导语：我将在本文介绍 OriginLogger 键盘记录器恶意软件，看看它如何处理配置变量的字符串混淆，以及我在查看提取的配置时发现的内容。

2019 年 3 月 4 日，键盘记录恶意软件Agent Tesla被发现。最近，研究人员发现了OriginLogger，这是一个基于Agent Tesla的恶意软件。

我将在本文介绍 OriginLogger 键盘记录器恶意软件，看看它如何处理配置变量的字符串混淆，以及我在查看提取的配置时发现的内容。

Palo Alto Networks 客户通过 Cortex XDR 和具有云交付安全服务（包括 WildFire 和高级威胁预防）的下一代防火墙获得 OriginLogger 及其前身恶意软件 Agent Tesla 的保护。

**OriginLogger的发现过程**

在搜索过程中，我偶然发现了一个销售“完全无法检测”（FUD）工具的人在 2018 年发布的 YouTube 视频。此人展示了带有链接的 OriginLogger 工具，该链接可以从一个已知的网站购买该工具，该网站会传播恶意软件、漏洞利用等。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556436438642.png "1663556436438642.png")

OriginLogger的部分功能

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556446951330.png "1663556446951330.png")

OriginLogger的全部功能

此外，他们还展示了 Web 面板和恶意软件生成器。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556455174966.png "1663556455174966.png")

OriginLogger Web 面板

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556464156606.png "1663556464156606.png")

OriginLogger 生成器

上图显示的生成器图像对我来说特别有趣，因为它提供了一个默认字符串：facebook、twitter、gmail、instagram、movie、skype、porn、hack、whatsapp、discord，这可能是这个应用程序独有的。果然，在 VirusTotal 上的内容搜索显示了 2022 年 5 月 17 日上传的一个匹配文件（SHA256：595a7ea981a3948c4f387a5a6af54a70a41dd604685c72cbd2a55880c2b702ed）。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556474146268.png "1663556474146268.png")

VirusTotal 搜索字符串

由于缺少依赖项，下载并尝试运行此文件会导致错误。但是，知道生成器的文件名 OriginLogger.exe，允许我扩展搜索并找到一个包含运行OriginLogger所需的所有文件的Zip归档文件 (SHA256: b22a0dd33d957f6da3f1cd9687b9b00d0ff2bdf02d28356c1462f3dbfb8708dd)。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556483102423.png "1663556483102423.png")

Zip 压缩文件中的捆绑文件

settings.ini 文件包含生成器将使用的配置，在下图中我们可以看到 SmartWords 下列出的先前搜索字符串。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556493581567.png "1663556493581567.png")

OriginLogger Builder settings.ini 文件

文件 profile.origin 包含客户在购买 OriginLogger 时注册的嵌入式用户名/密码。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556502193046.png "1663556502193046.png")

OriginLogger 生成器登录屏幕

有趣的是，如果你逆向配置文件中的值，就会显示明文密码。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556511172832.png "1663556511172832.png")

profile.origin 文件的内容

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556519139061.png "1663556519139061.png")

OriginLogger 生成器登录屏幕，以明文形式显示密码

当用户登录时，生成器会尝试向 OriginLogger 服务器进行身份验证以验证订阅服务。

此时，我有了两个版本的构建器。第一个(b22a0d\*)包含在Zip文件中，编译于2020年9月6日。另一个包含SmartWords字符串(595a7e\*)的版本是在2022年6月29日编译的，大约在第一个版本的两年之后。

更高版本通过 TCP/3345 向 IP 23.106.223[.]46 发出身份验证请求。自 2022 年 3 月 3 日起，此 IP 已解析到域 originpro[.]me。此域已解析为以下 IP 地址：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556529600770.png "1663556529600770.png")

第二个 IP，204.16.247[.]26，由于解析了这些其他 OriginLogger 相关域而脱颖而出：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556541152066.png "1663556541152066.png")

这个尝试连接到一个不同的IP地址进行身份验证。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556551239370.png "1663556551239370.png")

PCAP 显示远程 IP 地址

与 originpro[.]me 关联的 IP 地址不同，74.118.138[.]76 不直接解析为任何 OriginLogger 域，而是解析为 0xfd3[.]com。在此域上逆向显示它包含mail.originlogger[.]com的DNS MX和TXT记录。

从 2022 年 3 月 7 日左右开始，相关域开始解析为 IP 23.106.223[.]47，它在最后一个八位字节中比用于 originpro[.]me 的 IP（使用 46）高一个值。

这两个 IP 地址共享了多个 SSL 证书：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556559170718.png "1663556559170718.png")

共享 SSL 证书

以IP 23.106.223开头的两个服务器的RDP登录屏幕。X显示有多个帐户的Windows Server 2012 R2服务器。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556569134955.png "1663556569134955.png")

RDP登录界面为23.106.223[.]

在进一步搜索该域时，我发现了用户 0xfd3 的 GitHub 配置文件，其中包含下图中所示的两个存储库。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556578887259.png "1663556578887259.png")

用户 0xfd GitHub

**滴管**

由于 Agent Tesla 和 OriginLogger 都是商业化的键盘记录器，因此初始 dropper在不同的活动中会有很大的差异，不应被视为两者都是独一无二的。我将以下内容作为攻击释放 OriginLogger 的真实示例来展示，并表明它们可能非常复杂和模糊。

初始诱饵文档是一个Microsoft Word文件(SHA256: ccc8d5aa5d1a682c20b0806948bf06d1b5d11961887df70c8902d2146c6d1481)。打开时，该文件显示一张德国公民的护照照片以及一张信用卡。我不太确定这对普通用户有多大的吸引力，但无论如何，你都会注意到图像下方包含许多 Excel 工作表，如下图所示。

![17.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556589942675.jpeg "1663556589942675.jpeg")

诱饵文件

这些工作表中的每一个都包含在单独的嵌入式 Excel 工作簿中，并且完全相同：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556600166409.png "1663556600166409.png")

在每个工作簿中都有一个单一的宏，它只是保存要在以下位置执行的命令：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556610277917.png "1663556610277917.png")

运行后，它将通过 MSHTA 下载并执行 hxxp://www.asianexportglass[.]shop/p/25.html 上的文件内容。该网站的屏幕截图如下图所示。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556620912825.png "1663556620912825.png")

网站看起来合法

该文件在文档中间包含一个嵌入的混淆脚本作为注释。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556631193343.png "1663556631193343.png")

网站隐藏评论

取消转换脚本会显示下图中所示的代码，该代码从 BitBucket 片段下载下一个有效负载 (hxxps://bitbucket[.]org/!api/2.0/snippets/12sds/pEEggp/8cb4e7aef7a46445b9885381da074c86ad0d01d6/files/snippet.txt)并使用名为 calsaasdendersw 的计划任务建立持久性，该任务每 83 分钟运行一次，并再次使用 MSHTA 执行 hxxp://www.coalminners[.]shop/p/25.html 中包含的脚本。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556642101829.png "1663556642101829.png")

未转换的脚本

BitBucket 网站上托管的代码段包含进一步混淆的 PowerShell 代码和两个编码和压缩的二进制文件。

这两个文件中的第一个（SHA256: 23fcaad34d06f748452d04b003b78eb701c1ab9bf2dd5503cf75ac0387f4e4f8）是使用 CSharp-RunPE 的 C# 反射加载器。该工具用于挖空一个进程并在其中注入另一个可执行文件，在本例中，键盘记录器有效负载将放置在 aspnet\_compiler.exe 进程中。

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663556652823888.png "1663556652823888.png")

执行dotNet程序集中包含的方法的PowerShell命令

请注意调用 Execute 方法的 projFUD.PA 类。 Morphisec 在 2021 年发布了一个名为“揭示 Snip3 Crypter，一种高度规避的 RAT 加载器”的博客，他们在其中分析了一个加密器即服务，并使用该工件对加密器的开发者进行指纹识别。

两个文件中的第二个（SHA256：cddca3371378d545e5e4c032951db0e000e2dfc901b5a5e390679adc524e7d9c）是 OriginLogger 有效负载。

**OriginLogger 配置**

如前所述，此分析的初衷是自动化并从键盘记录器中提取与配置相关的详细信息。为了实现这一点，我首先查看了如何使用与配置相关的字符串。

我不会深入研究恶意软件的任何实际功能，因为它是相当标准的，并且反映了对原有Agent Tesla 变体的分析。为了开始提取与配置相关的细节，我需要弄清楚用户提供的数据是如何存储在恶意软件中的。结果很简单，生成器将获取动态字符串值并将它们连接成一个巨大的文本块，然后将其编码并存储在一个字节数组中，以便在运行时进行解码。一旦恶意软件运行并命中需要字符串的特定函数...