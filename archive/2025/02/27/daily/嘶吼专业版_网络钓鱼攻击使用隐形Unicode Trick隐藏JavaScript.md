---
title: 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581314&idx=1&sn=a5a3c12cb012cc1e49b0baab230a1473&chksm=e9146eb8de63e7ae138b7556bea2d9fb5ecbbc3221cb295419229bafd8079f4cd61dd502bbe1&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-27
fetch_date: 2025-10-06T20:36:51.006332
---

# 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4NwQTxibG0ehFZ6GaI9za0BurgLHbU2MuOxt6icJO7h8hwb063hA6S8pG2Q/0?wx_fmt=jpeg)

# 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种新的JavaScript混淆方法利用不可见的Unicode字符来表示二进制值，在针对美国政治行动委员会（PAC）附属机构的网络钓鱼攻击中被滥用。

发现此次攻击的网络威胁实验室报告称，该攻击发生在2025年1月初，并带有复杂的迹象，例如使用了：

**·**针对受害者提供个性化的非公开信息；

**·**调试器断点和定时检查以逃避检测；

**·**递归包装邮戳跟踪链接到模糊的最终网络钓鱼目的地。

JavaScript开发人员在2024年10月首次披露了这种混淆技术，它在实际攻击中的迅速采用凸显了新研究被武器化的速度。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4NwqU7QpHjuAYp9RIIEljNvnK9PbPibq7gu1eicmbZRAPLIgIQ9RcVia9ibCw/640?wx_fmt=png&from=appmsg)使JS有效负载“不可见”

新的混淆技术利用不可见的Unicode字符，特别是韩文半宽（U+FFA0）和韩文全宽（U+3164）。

JavaScript负载中的每个ASCII字符被转换为8位二进制表示，其中的二进制值（1和0）被不可见的韩文字符替换。

混淆后的代码作为属性存储在JavaScript对象中，由于韩文填充字符呈现为空白，因此脚本中的有效负载看起来为空，如下图末尾的空白所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4Nw1wu2uqyUXbsm5LNXjmVWHib8I5leF3lxibqpylN798RuXovuwe5GSY7A/640?wx_fmt=png&from=appmsg)

隐藏恶意代码的空白

一个简短的引导脚本使用JavaScript代理的“get（）陷阱”检索隐藏的有效负载。当访问hidden属性时，Proxy将不可见的韩文填充字符转换回二进制并重建原始JavaScript代码。

Juniper分析师报告称，攻击者除了上述步骤之外，还使用了额外的隐藏步骤，比如用base64编码脚本，并使用反调试检查来逃避分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4NwezhIcxGwBUeDqtIHvoSKVZ7HfliaiaI0mOFrrdRAH0e6b4hkySrDpvcg/640?wx_fmt=jpeg&from=appmsg)

韩文填充字符序列的Base64编码

Juniper解释说：“攻击是高度个性化的，包括非公开信息，最初的JavaScript会在被分析时试图调用调试器断点，检测到延迟，然后通过重定向到一个正常的网站来中止攻击。”

这种攻击很难检测，因为空白减少了安全扫描仪将其标记为恶意的可能性。

由于有效负载只是对象中的一个属性，因此可以将其注入合法脚本而不会引起怀疑；另外，整个编码过程很容易实现，不需要高级知识。

Juniper表示，此次活动中使用的两个域名先前与Tycoon 2FA网络钓鱼工具包有关。如果是这样，我们很可能会看到这种不可见的混淆方法在未来被更广泛的攻击者采用。

参考及来源：https://www.bleepingcomputer.com/news/security/phishing-attack-hides-javascript-using-invisible-unicode-trick/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4NwoEMGlQvxbT1d9ClicorDia4rmbVRL72VVumYTDGMO2KOJnBvf2XUNdlg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibmo9SxePSpGHZGtWvSD4NwktodAR3ibXpN7oOSvaaC1eDA4DhWHTjOHTc8csz6I8lPaRzttibN9usA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过