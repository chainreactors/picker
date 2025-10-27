---
title: 眼见不为实｜假 Zoom 会议钓鱼分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500726&idx=1&sn=6910bca0976da7f6078662bd95f0bc68&chksm=fddebd31caa93427a623e9effebecf40cb27caa8a441b3cbf75b4ed2547444062904609098ef&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-12-27
fetch_date: 2025-10-06T19:37:40.194837
---

# 眼见不为实｜假 Zoom 会议钓鱼分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osguW85Ym9lP2I9NhktwGicPN8ffdmHo0vmEw8okFVjkt97Nb3p9FyibibGw/0?wx_fmt=jpeg)

# 眼见不为实｜假 Zoom 会议钓鱼分析

原创

慢雾安全团队

慢雾科技

**背景**

近期，X 上多位用户报告了一种伪装成 Zoom 会议链接的钓鱼攻击手法，其中一受害者在点击恶意 Zoom 会议链接后安装了恶意软件，导致加密资产被盗，损失规模达百万美元。在此背景下，慢雾安全团队对这类钓鱼事件和攻击手法展开分析，并追踪黑客的资金流向。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgD8mOGV6VlDGiawIyHlF7nibet41fs65F7Z3vjK5W0bpe3BIr76Ziawk4A/640?wx_fmt=png&from=appmsg)

(https://x.com/lsp8940/status/1871350801270296709)

##

## **钓鱼链接分析**

黑客使用形如“app[.]us4zoom[.]us”的域名伪装成正常 Zoom 会议链接，页面与真 Zoom 会议高度相似，当用户点击“启动会议”按钮，便会触发下载恶意安装包，而非启动本地 Zoom 客户端。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgcicRdq7OlsoPxlPOEdIPNvDdR0shfqKBOEF3xEbSicX3A5njzBsxg7vw/640?wx_fmt=png&from=appmsg)

通过对上述域名探测，我们发现了黑客的监控日志地址 (https[:]//app[.]us4zoom[.]us/error\_log)。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgMTqpluMOASfiaw5MkfR6E437decb6pHnpqSIaIHVFObb6UgN4eAGz8A/640?wx_fmt=png&from=appmsg)

解密发现，这是脚本尝试通过 Telegram API 发送消息时的日志条目，使用的语言为俄语。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgeeomK7hQmWhQ3ER7p2aD38CqOicSTrknjYAMKV2YuibxD1ApZ5mv5v6Q/640?wx_fmt=png&from=appmsg)

该站点 27 天前已部署上线，黑客可能是俄罗斯人，并且从 11 月 14 号便开始寻找目标投马，然后通过 Telegram API 监控是否有目标点击钓鱼页面的下载按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osg66D3LCwVBMyAFXjTmnDcGFQ1aoPHcO7DtSt0aCycoLJCjk8icquxPKQ/640?wx_fmt=png&from=appmsg)

##

## **恶意软件分析**

该恶意安装包文件名为“ZoomApp\_v.3.14.dmg”，以下是该 Zoom 钓鱼软件打开的界面，诱导用户在 Terminal 中执行 ZoomApp.file 恶意脚本，并且执行过程中还会诱导用户输入本机密码。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgTick1J35qNIX2asGgmVW70mEIEMMOhJVrmApsmLrNdYBJn8iccrmyBYw/640?wx_fmt=png&from=appmsg)

下面是该恶意文件的执行内容：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgWnNic4Gncodh0gIYoH71I4Sm79p10TqiblRqRPQrnFKjBGUONIbCia7sA/640?wx_fmt=png&from=appmsg)

对上述内容解码后发现这是一个恶意的 osascript 脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgo2TB3PFJ2bpmoH4goEfwLyVqsHDhV4tAU30RjvakF7nKWptDKredSw/640?wx_fmt=png&from=appmsg)

继续分析发现，该脚本查找一个名为“.ZoomApp”的隐藏的可执行文件并在本地运行。我们对原始安装包“ZoomApp\_v.3.14.dmg”进行磁盘分析，发现安装包确实隐藏了一个名为“.ZoomApp”的可执行文件。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgae1j52cy5ngZhnF6rQnflGHPIWd6JLpRp8Ixaop2rHSYN50yTYHfmg/640?wx_fmt=png&from=appmsg)

##

## **恶意行为分析**

##

## **静态分析**

我们将该二进制文件上传到威胁情报平台分析，发现该文件已经被标记为恶意文件。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgSIpiaZ9uoVgoE5WmP7SR9lBgPr3hxYkWTEfxdYnoP6t5PGxUN6eCJibQ/640?wx_fmt=png&from=appmsg)

(https://www.virustotal.com/gui/file/e4b6285e183dd5e1c4e9eaf30cec886fd15293205e706855a48b30c890cbf5f2)

通过静态反汇编分析，下图为该二进制文件的入口代码，用于数据解密和脚本执行。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgc2BjbJVU88aZAbs3dZfzAflWj123WuibLXaHXnUm09RicZsXsib6GRdaA/640?wx_fmt=png&from=appmsg)

下图是数据部分，可以发现大部分信息都经过了加密和编码。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgomibKSsic2BoKL2wwCAKzjPraqdcx5xUeyqeUgWwACm9eM7BHa79gibkQ/640?wx_fmt=png&from=appmsg)

通过对数据解密后发现该二进制文件最终同样执行恶意的 osascript 脚本（完整解密代码已分享到：https://pastebin.com/qRYQ44xa），该脚本会收集用户设备上的信息并发送到后台。

下图是枚举不同插件 ID 路径信息的部分代码。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgqV2lr4o74nG5n1cGQMCT28C4gACG4fc9o3wFaLOjZ0UD87GqS5Uicrg/640?wx_fmt=png&from=appmsg)

下图是读取电脑 KeyChain 信息的部分代码。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osg2WJeYjS5aiba3Bkibrsm8outlficOsmwPDTqFicAAOsfSDogV0sDATeoAA/640?wx_fmt=png&from=appmsg)

恶意代码采集完系统信息、浏览器数据、加密钱包数据、Telegram 数据、Notes 笔记数据和 Cookie 数据等信息后，会将它们压缩并发送至黑客控制的服务器 (141.98.9.20)。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgZgwIygEAEFiabr0ibQyUIKOFnbicsjBB9vkosBRcmia3VKqCD356A67icYg/640?wx_fmt=png&from=appmsg)

由于恶意程序在运行时就诱导用户输入密码，并且后续的恶意脚本也会采集电脑中 KeyChain 数据（可能包含用户保存在电脑上的各种密码），黑客收集后就会尝试解密数据，获得用户的钱包助记词、私钥等敏感信息，从而盗取用户的资产。

据分析，黑客服务器的 IP 地址位于荷兰，目前已被威胁情报平台标记为恶意。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgxyZxU4GQV847qkGcKkY0DdzCNTcDF9MylDQhYEZHN1ro8V7gY5mYuQ/640?wx_fmt=png&from=appmsg)

(https://www.virustotal.com/gui/ip-address/141.98.9.20)

##

## **动态分析**

在虚拟环境下动态执行该恶意程序并分析进程，下图为恶意程序采集本机数据进程和发送数据到后台的进程监控信息。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgyuJWaHx4vbn8PFT8zA7JGcen79iaTZDoicTNkiaNEpkuuJPATjRqsLzPw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgcN76ayeQSicrSKJ93jx9WW0YMZ8n41FvoWKCFNKYMuwvjtg68iaRghuQ/640?wx_fmt=png&from=appmsg)

## **MistTrack 分析**

我们使用链上追踪工具 MistTrack 分析受害者提供的黑客地址 0x9fd15727f43ebffd0af6fecf6e01a810348ee6ac：黑客地址获利超 100 万美金，包括 USD0++、MORPHO 和 ETH；其中，USD0++ 和 MORPHO 被兑换为 296 ETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgeHvaSibuKk8khX4f8TKjakTSmdQ2y2VgzTQ7nrIAmozbcPtMCG9Ty0g/640?wx_fmt=png&from=appmsg)

据 MistTrack 显示，黑客地址曾收到来自地址 0xb01caea8c6c47bbf4f4b4c5080ca642043359c2e 转入的小额 ETH，疑似为黑客地址提供手续费。该地址（0xb01c）的收入来源只有一个地址，却转出小额 ETH 到近 8,800 个地址，似乎是一个“专门提供手续费的平台”。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgAUw7kW6XRRnTRnmQ046YjBufnzSiaKUwKgvWlp48HdlD3amoUhrFibGQ/640?wx_fmt=png&from=appmsg)

筛选该地址（0xb01c）转出对象中被标记为恶意的地址，关联到两个钓鱼地址，其中一个被标记为 Pink Drainer，扩展分析这两个钓鱼地址，资金基本转移到 ChangeNOW 和 MEXC。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgmPAicfWrUIELrdbAW4H7lOOZsxOXspLZiaGOYaG4akreHLRJOZN2ekuw/640?wx_fmt=png&from=appmsg)

接着分析被盗资金的转出情况，共有 296.45 ETH 被转移到新地址 0xdfe7c22a382600dcffdde2c51aaa73d788ebae95。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgupphrkricVKJAFPce22s0p3ibVwicI8t8BxiaderV6IOyy84CG7ftYbWeQ/640?wx_fmt=png&from=appmsg)

新地址（0xdfe7）的首笔交易时间为 2023 年 7 月，涉及多条链，目前余额为 32.81 ETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osg9RKvibetZWXpRhxJVNics8DGLh8BYnde8QuqC6hQq4RSZ0jaXZibRuofw/640?wx_fmt=png&from=appmsg)

新地址（0xdfe7）主要的 ETH 转出路径如下：

200.79 ETH -> 0x19e0…5c98f

63.03 ETH -> 0x41a2…9c0b

8.44 ETH -> 兑换为 15,720 USDT

14.39 ETH -> Gate.io

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgWvGKxxqicTVBoFdibZL9jV8PQBiblpfSV5RwEM4k6orfmymcnuq9k2sQw/640?wx_fmt=png&from=appmsg)

以上扩展地址后续的转出与多个平台如 Bybit, Cryptomus.com, Swapspace, Gate.io, MEXC 关联，且与被 MistTrack 标记为 Angel Drainer 和 Theft 的多个地址相关。除此之外，目前有 99.96 ETH 停留在地址 0x3624169dfeeead9f3234c0ccd38c3b97cecafd01。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgSIcNj4jJ0gPo05okTgZEUwHUyEoZGxasMDIBgkGcaHdnlw2Cq4tgtw/640?wx_fmt=png&from=appmsg)

新地址（0xdfe7）的 USDT 交易痕迹也非常多，被转出到 Binance, MEXC, FixedFloat 等平台。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbibA73Bibj1l4N6q7qJP5osgzz1OsT7t93BGFJHgpfswqhcEtSicTeyNTGKzJ2ZGlSxw30qBxibUjBkQ/640?wx_fmt=png&from=appmsg)

## **总结**

本次分享的钓鱼途径是黑客通过伪装成正常 Zoom 会议链接，诱导用户下载并执行恶意软件。恶意软件通常具备收集系统信息、窃取浏览器数据和获取加密货币钱包信息等多重危害功能，并将数据传输至黑客控制的服务器。这类攻击通常结合了社会工程学攻击和木马攻击技术，用户稍有不慎便会中招。慢雾安全团队建议用户在点击会议链接前谨慎验证，避免执行来源不明的软件和命令，安装杀毒软件并定期更新。更多的安全知识建议阅读慢雾安全团队出品的《区块链黑暗森林自救手册》：https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README\_CN.md。

作者 | Reborn, Lisa

编辑 | Liz

**往期回顾**

[慢雾科技通过厦门市 2024 年专精特新中小企业认定](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500689&idx=1&sn=4edcb09fb8b3f3c92edad1d7a6edcb05&scene=21#wechat_redirect)

[Keyblock Solutions 宣布与 MistTrack 达成战略合作](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500674&idx=1&sn=ae109f56fa8b688eebce6f48366d1a3f&scene=21#wechat_redirect)

[每月动态 | Web3 安全事件总损失约 8,624 万美元](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500662&idx=1&sn=7ae9f27e00bd9f6751cdc900e42566c9&scene=21#wechat_redirect)

[Doo Group 与 MistTrack 达成合作伙伴关系，共促加密交易的安全与合规](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500641&idx=1&sn=623e19b75de821ef7791699d8017f04f&scene=21#wechat_redirect)

[活动回顾｜慢雾(SlowMist) 荣获 Invest HK Fintech "Must-know" 2024](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500629&idx=1&sn...