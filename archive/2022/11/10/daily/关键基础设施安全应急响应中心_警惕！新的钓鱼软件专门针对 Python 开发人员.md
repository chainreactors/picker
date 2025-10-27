---
title: 警惕！新的钓鱼软件专门针对 Python 开发人员
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247532546&idx=3&sn=2ce4df2c3ee36cc097e66ec07f4643e9&chksm=c1e9cc53f69e454580538219d763f505c010c7eeb29af8f253e978e0027de079c2b45a880e19&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-11-10
fetch_date: 2025-10-03T22:15:25.398650
---

# 警惕！新的钓鱼软件专门针对 Python 开发人员

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguZAWPyRiboDDlfVNOK8EaI4J3bKiceKRPrIBVQXUPltpadUJgnxQg3C2vNNF6jRud2h38lr2HmdLqw/0?wx_fmt=jpeg)

# 警惕！新的钓鱼软件专门针对 Python 开发人员

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguZAWPyRiboDDlfVNOK8EaI4QaHVibkiaU3BibU01OXRKnicFav3dpgCkoAbubDKiadBvIHjtnxEk51T8fg/640?wx_fmt=jpeg)

最近，一种新形式的钓鱼软件专门攻击 Python 开发人员。攻击者通过伪造的 Python 包并使用常规的伪装技术，通过 W4SP Stealer 来感染开发人员的系统。W4SP Stealer 是一种用来窃取加密货币信息、泄露敏感数据并从开发人员系统收集凭据的木马工具。

根据软件供应链公司 Phylum 本周发布的一份报告中说：一名攻击者在 Python 包索引 (PyPI) 上创建了 29 个流行软件包的克隆，给它们包装成合法的软件包名称，这种做法被称为仿冒域名。如果开发人员下载并加载了恶意程序包，安装脚本则会通过一些混淆步骤来误导安装 W4SP Stealer 木马。目前，这些软件包的下载量已高达 5,700 次。

Phylum 的联合创始人兼首席技术官 Louis Lang 表示，虽然 W4SP Stealer 的作用是针对加密货币钱包和金融账户，但当前攻击者最重要目的很有可能是开发者的隐私。

这与我们过去经常遇到的电子邮件网络钓鱼活动的形式一样，只是这次攻击者只针对开发人员。“考虑到开发人员经常可以访问最核心的地方，一旦被成功的攻击那么会对组织造成毁灭性的打击。

该组织对 PyPI 的攻击是针对软件供应链的最新威胁。通过存储库服务分发的开源软件组件，例如 PyPI 和节点包管理器 (npm)，是一种流行的攻击媒介，因为导入软件的需求数量急剧增加。攻击者试图利用生态系统将恶意软件传输到粗心的开发人员系统中，例如2020 年对 Ruby Gems 生态系统的攻击和对Docker Hub 映像生态系统的攻击。而在 8 月，Check Point Software Technologies 的安全研究人员发现了 10 个 PyPI 软件包，它们都为窃取信息的恶意软件。

Phylum 研究人员 在他们的分析中表示：在这次最新的攻击活动中，这些软件包是一种更复杂的尝试，将 W4SP Stealer 传递到 Python 开发人员的机器上。并补充说：“由于这是一个持续的攻击，攻击者通过不断的改变策略，导致我们很难发现。同时，我们怀疑在不久的将来会出现更多类似的恶意软件。

**PyPI 攻击是一种“量化游戏”**

这种攻击通过伪装通用软件包名称或使用新软件包来迷惑没有充分审查软件来源的开发人员。例如：一个名为“typesutil”的恶意程序包只是流行的 Python 程序包“datetime2”的副本，并进行了一些修改。

最初，任何导入恶意软件的程序都会在 Python 加载依赖项的设置阶段运行命令并下载恶意软件。后来，由于 PyPI 实施了某些检查，攻击者开始使用大量空格将可疑命令推送到大多数代码编辑器的正常可视范围之外。

Phylum 在其分析中说：攻击者稍微改变了策略，不是仅仅将导入文件放在一个明显的位置，而是将它放在屏幕外，利用 Python 很少使用的分号将恶意代码偷偷放到与其他合法代码的行中。

Phylum 的 Lang 表示，虽然域名仿冒是一种低保真攻击，成功率极低，但与潜在的回报相比，这种成本微乎其微。

这是一场量的游戏，攻击者每天都用大量的恶意软件包污染软件包生态系统。然而相对于回报率来说，成本却极低。

**令人痛心的 W4SP**

攻击的最终目标是安装“信息窃取木马 W4SP Stealer”，它入侵受害者的系统，窃取浏览器存储的密码，针对加密货币钱包，并使用关键字搜索感兴趣的文件，例如‘银行’和‘秘密’ 。

Lang说：除了窃取加密货币或银行信息带来的明显金钱回报外，攻击者还可以利用窃取的一些信息通过访问关键基础设施或借用开发人员的身份来进一步攻击。

目前，Phylum 在识别攻击者方面取得了一些进展，并向正在使用其基础设施的公司发送了报告。

**参考文章：**

https://www.darkreading.com/threat-intelligence/w4sp-stealer-aims-to-sting-python-developers-in-supply-chain-attack

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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