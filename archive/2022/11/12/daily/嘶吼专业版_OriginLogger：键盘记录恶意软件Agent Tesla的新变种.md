---
title: OriginLogger：键盘记录恶意软件Agent Tesla的新变种
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553649&idx=2&sn=73b22c7f744c8c200321cb25b92bf5b6&chksm=e915c24bde624b5ddd63e2a501987f14c0085937c582769bc47a59a11a25fcbed94a00552bce&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-12
fetch_date: 2025-10-03T22:32:50.400632
---

# OriginLogger：键盘记录恶意软件Agent Tesla的新变种

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2wMcicKibjysYGIm3AhYibBSetOpJIR0lKbjBHD4x9cmQibgCTIUd0FZicMw/0?wx_fmt=jpeg)

# OriginLogger：键盘记录恶意软件Agent Tesla的新变种

lucywang

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

2019 年 3 月 4 日，键盘记录恶意软件Agent Tesla被发现。最近，研究人员发现了OriginLogger，这是一个基于Agent Tesla的恶意软件。

我将在本文介绍 OriginLogger 键盘记录器恶意软件，看看它如何处理配置变量的字符串混淆，以及我在查看提取的配置时发现的内容。

Palo Alto Networks 客户通过 Cortex XDR 和具有云交付安全服务（包括 WildFire 和高级威胁预防）的下一代防火墙获得 OriginLogger 及其前身恶意软件 Agent Tesla 的保护。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2kIvhpPibmH5UTMmtsGOz0mK1HMW6g0kLhrJnn3iacYkNA02PzAD5R7pA/640?wx_fmt=png)OriginLogger的发现过程

在搜索过程中，我偶然发现了一个销售“完全无法检测”（FUD）工具的人在 2018 年发布的 YouTube 视频。此人展示了带有链接的 OriginLogger 工具，该链接可以从一个已知的网站购买该工具，该网站会传播恶意软件、漏洞利用等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2NsCG5bVltDu8W7ibM6SVLDPyicmUTgUk46UDrE1cicAtKthzPfI5Von9w/640?wx_fmt=png)

OriginLogger的部分功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2fQ8YYxMNWOE55SZfcEbVapzaeKN7V78MhUpwQwxLBO6jGVB05WDNWw/640?wx_fmt=png)

OriginLogger的全部功能

此外，他们还展示了 Web 面板和恶意软件生成器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2dCVpObmibk49svXuy5XI6dKuqOO4ibKibcjsiaMicxUkyLsVQRQYPzepmww/640?wx_fmt=png)

OriginLogger Web 面板

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2uD0pmSOXrLqOffib6UaFagwqfbhmYSy6MTHQFib19Ur7D5rr3oAwPBeA/640?wx_fmt=png)

OriginLogger 生成器

上图显示的生成器图像对我来说特别有趣，因为它提供了一个默认字符串：facebook、twitter、gmail、instagram、movie、skype、porn、hack、whatsapp、discord，这可能是这个应用程序独有的。果然，在 VirusTotal 上的内容搜索显示了 2022 年 5 月 17 日上传的一个匹配文件（SHA256：595a7ea981a3948c4f387a5a6af54a70a41dd604685c72cbd2a55880c2b702ed）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD23NmrYKVT1ajFqFY47npj1dGebxd0jEwA37ooPW9lWRyxh8V2S4Z39w/640?wx_fmt=png)

VirusTotal 搜索字符串

由于缺少依赖项，下载并尝试运行此文件会导致错误。但是，知道生成器的文件名 OriginLogger.exe，允许我扩展搜索并找到一个包含运行OriginLogger所需的所有文件的Zip归档文件 (SHA256: b22a0dd33d957f6da3f1cd9687b9b00d0ff2bdf02d28356c1462f3dbfb8708dd)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2NCLSwQNRRJ8DbxmYPLNsxapy17ckouUeWibYNXVkhPjia9Z3GnmqDmicQ/640?wx_fmt=png)

Zip 压缩文件中的捆绑文件

settings.ini 文件包含生成器将使用的配置，在下图中我们可以看到 SmartWords 下列出的先前搜索字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2CSrszctFtDshibGg7l7oYuTCojsFjRE4CY2GdwRwH6EpF8jmxsq4RgQ/640?wx_fmt=png)

OriginLogger Builder settings.ini 文件

文件 profile.origin 包含客户在购买 OriginLogger 时注册的嵌入式用户名/密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2gSjzQ8ibXXMDicibC3J0T9mqS2dRnrQ63s1a0jKian4FcDYeKjaSZWiayxA/640?wx_fmt=png)

OriginLogger 生成器登录屏幕

有趣的是，如果你逆向配置文件中的值，就会显示明文密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2jSvsFPIeN8a3oq58T8qeHqIyPwccFicbBhujvtIZXXtgXD9QYhib9POg/640?wx_fmt=png)

profile.origin 文件的内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD27hl6EawFQBy7dMypm7lOa0lOUB1rGfnvGJD6XIm5WlHV4RoDRC6Dww/640?wx_fmt=png)

OriginLogger 生成器登录屏幕，以明文形式显示密码

当用户登录时，生成器会尝试向 OriginLogger 服务器进行身份验证以验证订阅服务。

此时，我有了两个版本的构建器。第一个(b22a0d\*)包含在Zip文件中，编译于2020年9月6日。另一个包含SmartWords字符串(595a7e\*)的版本是在2022年6月29日编译的，大约在第一个版本的两年之后。

更高版本通过 TCP/3345 向 IP 23.106.223[.]46 发出身份验证请求。自 2022 年 3 月 3 日起，此 IP 已解析到域 originpro[.]me。此域已解析为以下 IP 地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2Tias2Ov91pZLia8T5gy2g4xlFuntY58Z5LlLcuxia4pvtXkB2r7tlgOqg/640?wx_fmt=png)

第二个 IP，204.16.247[.]26，由于解析了这些其他 OriginLogger 相关域而脱颖而出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2rphZf8ky28j8EcTcpOvpb5zKSaTsyYvSC2MRIZue2qELDWNia7nCE8g/640?wx_fmt=png)

这个尝试连接到一个不同的IP地址进行身份验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2Avoiauj6b6EY4Zico20MnNtticdwz7ha6aeFYBBocQIdSaTZ0z2CRo0oA/640?wx_fmt=png)

PCAP 显示远程 IP 地址

与 originpro[.]me 关联的 IP 地址不同，74.118.138[.]76 不直接解析为任何 OriginLogger 域，而是解析为 0xfd3[.]com。在此域上逆向显示它包含mail.originlogger[.]com的DNS MX和TXT记录。

从 2022 年 3 月 7 日左右开始，相关域开始解析为 IP 23.106.223[.]47，它在最后一个八位字节中比用于 originpro[.]me 的 IP（使用 46）高一个值。

这两个 IP 地址共享了多个 SSL 证书：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2SyDzRicLvqxohcewTL9Rbf7SdqibibUCPo46ibzDhcGCGd1OSmqSczlo8g/640?wx_fmt=png)

共享 SSL 证书

以IP 23.106.223开头的两个服务器的RDP登录屏幕。X显示有多个帐户的Windows Server 2012 R2服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2ZG4BjibbMEZZEWz8sFVMQFH29ib5gBdica7wQ8ia0IJqKxTRl5fPwj492g/640?wx_fmt=png)

RDP登录界面为23.106.223[.]

在进一步搜索该域时，我发现了用户 0xfd3 的 GitHub 配置文件，其中包含下图中所示的两个存储库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD20ZvsQHCrYEz9zNDSJnnLJesarQjjl2fxfamMoAUvETKnuuj85RQ5kQ/640?wx_fmt=png)

用户 0xfd GitHub

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2kIvhpPibmH5UTMmtsGOz0mK1HMW6g0kLhrJnn3iacYkNA02PzAD5R7pA/640?wx_fmt=png)滴管

由于 Agent Tesla 和 OriginLogger 都是商业化的键盘记录器，因此初始 dropper在不同的活动中会有很大的差异，不应被视为两者都是独一无二的。我将以下内容作为攻击释放 OriginLogger 的真实示例来展示，并表明它们可能非常复杂和模糊。

初始诱饵文档是一个Microsoft Word文件(SHA256: ccc8d5aa5d1a682c20b0806948bf06d1b5d11961887df70c8902d2146c6d1481)。打开时，该文件显示一张德国公民的护照照片以及一张信用卡。我不太确定这对普通用户有多大的吸引力，但无论如何，你都会注意到图像下方包含许多 Excel 工作表，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2rMfYDY9ICU8Vf3QWATibk9GiaarMlXhgkdYYQchZNYJYJz5Zv3hZn4dw/640?wx_fmt=jpeg)

诱饵文件

这些工作表中的每一个都包含在单独的嵌入式 Excel 工作簿中，并且完全相同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2dv0LsNpibYLUdxvAl9ETlibXrZlYIjo3H4ULibXcRZeltVAbNBHu7eiavg/640?wx_fmt=png)

在每个工作簿中都有一个单一的宏，它只是保存要在以下位置执行的命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2DZuWC5JroFUBVYsv6wNHibcGOIE4Ric50zjGBSdjU1lFI4ks5ibqVL9yQ/640?wx_fmt=png)

运行后，它将通过 MSHTA 下载并执行 hxxp://www.asianexportglass[.]shop/p/25.html 上的文件内容。该网站的屏幕截图如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2GcPz8etUbxY0eeBLU6Ns2ZX3P28qlRZC6x5wEpLicDqBCIWZbD01AtQ/640?wx_fmt=png)

网站看起来合法

该文件在文档中间包含一个嵌入的混淆脚本作为注释。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2jksjA461OMLoOrsfeYsdytp9iarTNmEahibfU9Nr7klWrd4TosFXNG9g/640?wx_fmt=png)

网站隐藏评论

取消转换脚本会显示下图中所示的代码，该代码从 BitBucket 片段下载下一个有效负载 (hxxps://bitbucket[.]org/!api/2.0/snippets/12sds/pEEggp/8cb4e7aef7a46445b9885381da074c86ad0d01d6/files/snippet.txt)并使用名为 calsaasdendersw 的计划任务建立持久性，该任务每 83 分钟运行一次，并再次使用 MSHTA 执行 hxxp://www.coalminners[.]shop/p/25.html 中包含的脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2u1sjgB1VickWiay6DSg8t5cw5TcgzfUWGK3xzKSeS3JRv3Ml9iaCKFEUQ/640?wx_fmt=png)

未转换的脚本

BitBucket 网站上托管的代码段包含进一步混淆的 PowerShell 代码和两个编码和压缩的二进制文件。

这两个文件中的第一个（SHA256: 23fcaad34d06f748452d04b003b78eb701c1ab9bf2dd5503cf75ac0387f4e4f8）是使用 CSharp-RunPE 的 C# 反射加载器。该工具用于挖空一个进程并在其中注入另一个可执行文件，在本例中，键盘记录器有效负载将放置在 aspnet\_compiler.exe 进程中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2r69DiarE85wicKu6DqtZ65XGicHt2h02Lj340ct5lXLeylw1dyIsHudKw/640?wx_fmt=png)

执行dotNet程序集中包含的方法的PowerShell命令

请注意调用 Execute 方法的 projFUD.PA 类。Morphisec 在 2021 年发布了一个名为“揭示 Snip3 Crypter，一种高度规避的 RAT 加载器”的博客，他们在其中分析了一个加密器即服务，并使用该工件对加密器的开发者进行指纹识别。

两个文件中的第二个（SHA256：cddca3371378d545e5e4c032951db0e000e2dfc901b5a5e390679adc524e7d9c）是 OriginLogger 有效负载。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2kIvhpPibmH5UTMmtsGOz0mK1HMW6g0kLhrJnn3iacYkNA02PzAD5R7pA/640?wx_fmt=png)OriginLogger 配置

如前所述，此分析的初衷是自动化并从键盘记录器中提取与配置相关的详细信息。为了实现这一点，我首先查看了如何使用与配置相关的字符串。

我不会深入研究恶意软件的任何实际功能，因为它是相当标准的，并且反映了对原有Agent Tesla 变体的分析。为了开始提取与配置相关的细节，我需要弄清楚用户提供的数据是如何存储在恶意软件中的。结果很简单，生成器将获取动态字符串值并将它们连接成一个巨大的文本块，然后将其编码并存储在一个字节数组中，以便在运行时进行解码。一旦恶意软件运行并命中需要字符串的特定函数，例如将屏幕截图上传到的 HTTP 地址，它会将偏移量和字符串长度传递给函数，然后该函数将在块中的该位置显示出文本。

为了说明这一点，你可以在下面看到用于主要文本块的解码逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfb...