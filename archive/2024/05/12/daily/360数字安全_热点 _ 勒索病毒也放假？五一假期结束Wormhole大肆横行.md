---
title: 热点 | 勒索病毒也放假？五一假期结束Wormhole大肆横行
url: https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247571332&idx=2&sn=0ed78acc13db081acd821508c7563129&chksm=9f8d478ca8face9ab0ca1cc07f37e9879ab8ae98a0d96879c5a725f26b2aceb0c775aab22a1d&scene=58&subscene=0#rd
source: 360数字安全
date: 2024-05-12
fetch_date: 2025-10-06T17:17:19.332934
---

# 热点 | 勒索病毒也放假？五一假期结束Wormhole大肆横行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVn7DGj3mFMz7l0XRaYOejTqeWGxJLXKicaVetXPWluVEgsiaDbGz9XUOA/0?wx_fmt=jpeg)

# 热点 | 勒索病毒也放假？五一假期结束Wormhole大肆横行

360数字安全

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

自4月中旬以来，360数字安全集团监测到国内一个新兴勒索家族——Wormhole勒索软件开始崛起。在4月下旬，其攻击量开始达到峰值，最高峰时单日拦截该勒索软件攻击可达数百次。

在随后的五一假期期间，Wormhole勒索软件的传播却出乎意料地停滞下来。然而假期一结束，Wormhole又死灰复燃，恢复了其活跃的攻击态势。据推测，该勒索病毒的传播有可能是国内的攻击团伙所为。

360经过分析发现，Wormhole勒索软件利用了瑞\*\*翼软件中的SQL注入漏洞作为其主要传播手段。此漏洞允许攻击者在没有进行适当身份验证的情况下，向数据库注入恶意SQL代码，从而获取对当前系统的非法访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVmoUR3hiacnm3KibHnbm6mxLRjrTlM7g6wAuraibibJTeZD8NChYMX3vl3w/640?wx_fmt=png&from=appmsg)

*360监测到的入侵攻击现场命令行快照*

目前，360已经监测到Wormhole勒索软件有两个主要版本，这两个版本的勒索软件仅在加密文件后的勒索策略上存在细微差异。

**01**

其中一个版本会在被加密的文件后添加“.locked”后缀。在该版本的勒索提示信息中虽明确提出了0.04个比特币（BTC）的赎金要求，但受害者仍可以通过电子邮件与攻击者进行谈判，并有可能通过这一谈判来压低最终实际成交的赎金金额。

**02**

而另一个版本则会在被加密的文件后添加“.Wormhole”的后缀。与前一个版本不同，该版本的勒索提示信息并没有给出明确的勒索金额。受害者只能通过攻击者提供的TOX ID（一个用于点对点通信的标识符）与其进行联系和谈判。这种缺乏明确赎金金额信息的做法可能会使受害者在谈判过程中处于更为劣势的地位。

“.Wormhole”后缀版本的勒索软件在执行后，首先会搜寻并尝试结束其内置进程列表中所指定的进程，以此来解除数据文件占用，方便其后续对于数据文件的加密操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVkVfpRJR8JFFRjD3eUD6C5WpgIMjweV2Y04oQ7t8bTDGNibKNsUKLqTA/640?wx_fmt=png&from=appmsg)

*勒索软件内置的待结束进程列表（部分）*

其一旦发现当前系统中存在内置列表中的对应进程，便会调用系统API尝试结束进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVRibdtoXG30RMloiaOCIcSNywmPps2vJhu97elx94KjkicOMt3hjnZMyLw/640?wx_fmt=png&from=appmsg)

*勒索软件调用系统API尝试结束进程*

完成上述的“铺垫”之后，勒索软件会采用AES256算法对文件内容进行加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVmibhEdvb9GYwT0FvIUvVkiaTOqojRvGT2akoKLWfibMgDibC9ObH0gSCfw/640?wx_fmt=png&from=appmsg)

*勒索软件采用AES256算法对文件内容进行加密*

勒索软件在上述加密文件过程中所使用的AES256由于是一种对称加密算法，所以其用到的密钥（本地生成）则需要被再次加密以防止被直接用来进行文件解密操作，而被用来进行这一对密钥字符串进行二次加密操作的，则是内置在软件内部的RSA公钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVawt9ORJfXC3fiaFfzgBya034ibywemiaXnVW1yGLJbibRVQTtWr7IC6pXg/640?wx_fmt=png&from=appmsg)

*勒索软件内置的RSA公钥字符串*

最终，被加密后的AES256密钥则会被写入到勒索信中的”Your Wormhole ID”处。而完成加密操作后，勒索软件最终会在被加密的文件名添加”.Wormhole”的后缀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVfsopuHKJaBVMEwuTcDjPcsLU7exPVPJDiapmTAibITiblZ2oZYAnIIqqg/640?wx_fmt=png&from=appmsg)

*勒索软件向被加密的文件后添加”.Wormhole”后缀*

在全部的加密过程中，勒索软件会对一些特定的目录、文件名以及文件扩展名进行排除（不加密）。

加密完成后，勒索软件会留下名为”How to recover files encrypted by Wormhole.txt”的勒索信。其内容中还会留下一个TOX ID用于让受害者与攻击者进行联系。

Tox 是一款开源、免费、去中心化、使用端到端加密技术的即时通讯软件，而这些特性恰恰迎合了此类攻击者既希望能与受害者取得联系索取赎金，又对隐匿自身性有着极高要求的特点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVBiaLnWS8Ub12Ohl9g394jpWxqLaJV8wWibGzzCjsfMnQRGoibYg4ia3jXg/640?wx_fmt=png&from=appmsg)

*勒索信内容*

在完成所有上述行为后，勒索软件最终会删除用于系统备份的卷影副本，以防止受害者对被加密的数据进行恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVTp9mJwy213QlUWLOqxHIlmUR0J0Ytxf05EyxRlzLouicFjIoXIulmjw/640?wx_fmt=png&from=appmsg)

*勒索软件删除卷影副本*

针对Wormhole家族这类利用漏洞攻击的勒索方式，我们向广大用户提出以下几点安全建议：

**01**

及时更新软件补丁：请定期使用安全软件中的漏洞修复工具，为操作系统、浏览器以及所有常用软件应用及时打上安全补丁；

**02**

信任安全软件的警报：请相信您的安全软件的判断，避免将被识别为恶意的程序添加到信任列表中，也不要在没有充分理由的情况下关闭安全软件；

**03**

定期进行安全检查：对于已知易受攻击的环境，如Java、通达OA、致远OA等，进行定期的安全排查。这有助于识别和修复可能的安全风险；

**04**

备份重要数据：定期备份您的重要数据，确保在遭受攻击时能够快速恢复，减少潜在的损失。

360基于多年攻防实战经验和能力推出360安全云，云化数据、探针、专家、平台和大模型能力开放给广大客户，并以安全云为核心打造360防勒索解决方案，构建了有效预防、持续监测、高效处置的勒索病毒防御体系。

作为这套方案的重要组成，360终端安全管理系统集成防病毒、漏洞与补丁管理、Win7盾甲、终端管控、桌面优化、软件管理、安全U盘及移动存储管理等功能于一体，可及时完成对各类勒索病毒的查杀与拦截，目前已实现针对该勒索软件的全面截杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2PLxh8VWogLtVkMkcfbwEVv1bUdxVLD0XPAISOwVvb0eaJ2xoWYkdW8wticD2gO9OqysjwHlcSoGg/640?wx_fmt=png&from=appmsg)

**想要了解更多详情**

**欢迎拨打咨询电话：400-0309-360**

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● ISC2023周鸿祎发布战略级产品360安全云，首提安全即服务 | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247563239&idx=1&sn=249e838ae2cf5f2a8570717d7f84a777&chksm=9f8d67efa8faeef96fd676b8680a067989f945fbefa554acf09d141fb17e435573d801ddffd9&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ● 2023年度十大勒索“卡牌”，你被PICK过吗？ | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247568789&idx=1&sn=94edadb44ee862db56090e11469b4c5b&chksm=9f8d5d9da8fad48b50de54e7ab57ff4cb5a7a43043e04ad96e7407436e1d3c756d8abee0e74a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● 防范勒索攻击——360安全云在，数据在！ | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247567618&idx=2&sn=8e682b9766ad1e0d3eda5d4db1527f63&chksm=9f8d590aa8fad01cab27a3c3f29ac8871c69f4a8d9e62a0762a8b97812ef572793eb2cbf9c16&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 勒索风暴：2023年最惊人心弦的十大事件！ | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247568617&idx=1&sn=8466d15b038c66f9f00def23a4d28b3e&chksm=9f8d5ce1a8fad5f7e1e243bd069c3c86f9fd3c7e65cb107a18a8ca44bd44a55155e9c3426077&scene=21#wechat_redirect) | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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