---
title: 诈骗碟中谍，Water Labbu利用其他攻击者的恶意DApp窃取加密货币
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552901&idx=2&sn=7e055b0d1f4ab4b74efe6d0abadebb1a&chksm=e915dfbfde6256a9d22d771c6e0f0bb112e2a0ec21ad8d8a31e2f1c851001ac70e84d0db96d8&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-29
fetch_date: 2025-10-03T21:14:41.495605
---

# 诈骗碟中谍，Water Labbu利用其他攻击者的恶意DApp窃取加密货币

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibicpicuV7GMIcbz8ZGSibQnA3Oiaibu8KaTgQw9TyYVpbPubcXSHaTQfU2XA/0?wx_fmt=jpeg)

# 诈骗碟中谍，Water Labbu利用其他攻击者的恶意DApp窃取加密货币

gejigeji

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Dapp (去中心化应用程序)是一种在网络上公开运行的软件应用程序，他们与普通的应用程序没有什么区别，都拥有一样的功能，但不同的是Dapp是在P2P网络上运行。这意味着，Dapp是一种全新的去中心化方式，它还同时整合了加密货币。

DAPP与APP区别主要有：一是APP在安卓或苹果系统上安装并运行；DAPP在区块链公链上开发并结合智能合约；二是APP信息存储在数据服务平台，可以运营方直接修改；DAPP数据加密后存储在区块链，难以篡改。

趋势科技的研究人员最近发现了一个名为Water Labbu的攻击组织，其攻击目标是加密货币诈骗网站。通常，加密货币诈骗者使用社会工程技术，与受害者互动以获得他们的信任，然后操纵他们提供转让加密货币资产所需的权限。虽然Water Labbu也是通过类似的方法从受害者钱包中获得访问许可权限来窃取加密货币，但与其他类似活动不同，他们没有使用任何类型的社会工程，至少没有直接使用。取而代之的是，Water Labbu是借用其他诈骗者的社会工程活动，进而骗取毫无戒心的受害者。

通过这种寄生的方式，攻击者潜入了其他伪装成DApp的诈骗者的网站，并向其注入恶意JavaScript代码。

当攻击者发现一个受害者的钱包中存储了大量加密货币，且该钱包连接到其中一个欺诈网站时，注入的JavaScript负载将发送一个权限请求。该请求被伪装成从一个受攻击的网站发送，并请求允许从目标的钱包转移几乎无限数量的USD Tether (USDT，这是一种与美元挂钩，价值为1:1的稳定币)。

Water Labbu的目标相信该请求最初是由DApp发出的，这可能会导致他们忽视对许可证细节的彻底审查。然而，授予的权限不属于原诈骗者的加密地址，而是属于Water Labbu控制的另一个地址。然后，攻击者可以使用获得的许可从受害者钱包中取出所有USDT资金。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib1jSibKrpsRn4BN5zEZYPqkb7XRRUamwQaB67kNiatg9BHH9AtePlPT4A/640?wx_fmt=jpeg)Water Labbu攻击流程

截至发文之时，研究人员已经发现45个与加密货币相关的DApp网站已被Water Labbu破解。这些网站的风格和主题与无损挖矿（lossless mining）项目诈骗中使用的网站相似。

在检查以太坊区块链上攻击者地址的交易记录后，研究人员发现他们已成功从至少九名不同的受害者那里盗取资金，总金额至少为316728USDT。

接下来，我们将介绍攻击者如何使用注入的JavaScript代码从欺诈性DApp网站劫持加密货币。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicibsgqd2ZVKrMG6U3Xj20SSNR0peZbjqLxD8ib87FsRp710J5fEwdhzmLA/640?wx_fmt=png)

被泄露的欺诈DApp网站截图

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)分析加密货币盗窃程序

如上所述，Water Labbu的方法包括攻击诈骗DApp网站并将其JavaScript负载注入其中。DApp网站似乎是通过某种形式的自定义模板设计的，在这种模板中，通过向给定URL发送HTTP请求，以JSON格式接收公告框中显示的消息。请求的内容显示了一个JSON对象，该对象具有一个包含几个嵌入项的“helper”项。第一项显然是注入的，它包含base64编码脚本的求值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibL7jciaWAnN4fLKjnCh0IoTFO6tLFueNxhSb6TqcCiaXl5O9ibvfwiadqlw/640?wx_fmt=png)

诈骗DApp网站公告框的可视化示例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibTcLvUCdcU6WicTebDL1TKsI6hwlfUWFIBW6POKroicIiaibYertO4A3Kag/640?wx_fmt=png)

以JSON格式显示接收的数据

在研究人员分析的其中一个示例中，Water Labbu注入了一个IMG标签，使用“onerror”事件加载Base64编码的JavaScript负载，这就是所谓的XSS规避技术，以绕过跨站点脚本（XSS）过滤器。然后，注入的有效负载创建另一个脚本元素，该元素从发送服务器tmpmeta[.]com加载另一脚本。然后，发送服务器根据IP地址和浏览器User-Agent标头（用于帮助确定受害者的环境）过滤受害者并发送不同的内容。

研究人员注意到以下行为：

1.如果受害者从使用Android或iOS的移动设备加载脚本，则会返回具有加密货币盗窃功能的第一阶段脚本。

2.如果受害者从运行Windows的桌面加载脚本，则会返回另一个脚本，该脚本显示一条虚假的Flash更新消息，要求受害者下载恶意的可执行文件。

值得一提的是，发送服务器实现了一种机制，以避免在短时间内从同一IP地址多次加载脚本。如果在过去几小时内访问了传递服务器的IP地址或受害者使用的设备类型不符合其他必要条件，它将返回一个简单的窃取脚本，该脚本将收集cookie和LocalStorage数据并将它们发送回传递服务器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibpQIe3b92smbiaIBcApXT6jxyghB8v4Pq7GpibiausEI4mN5gf2iaoromrQ/640?wx_fmt=png)

收集cookie和LocalStorage数据的Stealer脚本

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)加密货币窃取脚本：第一阶段

最初，加载web3.js库。这为第一阶段脚本提供了连接到受害者钱包的能力，尽管只有当受害者的钱包连接到被攻击的DApp网站时，恶意脚本才会与受害者钱包通信。通过访问钱包，Water Labbu可以收集目标的以太坊地址和余额。该脚本还与Tether USD智能合约交互，以接收受害者的USDT余额。如果钱包的ETH数大于0.001或USDT数大于1，它将通过HTTP请求将钱包余额信息和钱包地址发送到信息收集服务器linkstometa[.]com。

以下文本显示了提取钱包余额的请求：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicibia7qz93TZ1mVMrUWAicebpRiaDA0vI54OcWM69iaYcHqWdUKNqkicH1AX5A/640?wx_fmt=png)

用于收集钱包余额和默认钱包地址的脚本(去模糊化)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)加密货币窃取脚本：第二阶段

一旦报告的余额中ETH余额高于0.005 ETH且USDT令牌余额高于22000 USDT，导出请求将返回第二阶段脚本。否则，它将返回一个空有效负载，并将受害者留给其他诈骗者。在第二阶段脚本中，执行第三个余额检查并请求令牌限额批准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibGDic27T0h8B2FicT2ibRCgunGyKdibgJAk3J95oX2faZpMSB0cMibDibV0zw/640?wx_fmt=png)

负责显示令牌允许批准的脚本

令牌批准请求要求受害者授予对给定地址的许可，以完成交易并使用加密货币资产。恶意脚本请求10^32 USDT的批准限制，这远远超过区块链上可用的USDT代币总数。当发出“批准”请求时，加密货币钱包应用程序将要求用户在确认前查看请求的详细信息。如果受害者没有仔细检查请求详细信息并授予Water Labbu地址的权限，那么攻击者将能够从受害者的钱包中转移所有USDT。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicibg4rh6M7ryHUUNibO1ibaPgEy8dm3iakempVqZAIrcltLRY40wY2kic3ajg/640?wx_fmt=png)

加密货币钱包恶意许可请求的审查提示

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)区块链交易分析

在对Water Labbu的运营进行监控期间，研究人员注意到有两个地址被反复用于接收授予的权限和转移受害者的加密货币资产。

地址0xd6ed30a5ecdeaca58f9abf8a0d76e193e1b7818a是第一个从受害者那里接收令牌批准的地址。截至2022年8月，该地址已成功使用“Transfer From”方法7次从不同地址收取USDT，这些可能属于该组织的受害者。然后，资金转移到第二个地址0x3e9f1d6e244d773360dce4ca88ab3c054f502d51。第二个位置有两个事务，将被盗的USDT转移到其他两个地址：0x486d08f635b90196e5793725176d9f7ead155fed和0xfc74d6cfdf6da90ae996c999e12002090bc6d5bf。

地址0xfece995f99549011a88bbb8980bbedd8fada5a35是我们在Water Labbu的脚本中从2022年6月发现的一个更新的地址。这个地址成功地从两个地址中提取了USDT，在Uniswap加密货币交易所交换它们，首先是美元硬币（USDC），然后是ETH。最后将ETH资金发送到TTornado Cash混合器。

截至2022年8月，Water Labbu从9名受害者身上排放的USDT总额达316728 USDT。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibtYww6IyHrAOCRJcJib8Seia82m2CRsRGtpUl1Err4jMyuE2NkNDqibvUQ/640?wx_fmt=png)

显示被盗USDT交易的图表

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)虚假Flash感染链分析

当目标使用Windows桌面访问受攻击的DApp网站时，发送服务器tmpmeta[.]com将返回一个不同的脚本，该脚本将尝试窃取cookie和LocalStorage数据。它还从其他发送服务器（如whg7[.]cc和r8s[.]cc）加载其他脚本。发送服务器r8s[.]cc返回了最新的阶段脚本，在受攻击网站上创建了虚假的Flash安装消息覆盖。该消息用简体中文表示，Flash Player支持已于2020年9月14日终止，需要下载最新版本才能继续浏览页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kiciboib9FH5rhZpq46Mu9ptRlibpDlib99or7NbCrDA9k13X946qGsXKIpzwg/640?wx_fmt=png)

Windows桌面系统上的脚本加载顺序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibTHTnjKyrQTvEGoDBZKiakFDyssbVevFRlGXP5ln3g1Nf1G95z4L9TAw/640?wx_fmt=png)

虚假Flash Player安装信息被覆盖在被攻击的网站上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibCrkuCGLMY0JsBp3nW2BQv4xtSrQJtxW2vzcve7bsyFXZH1yXx4Mtnw/640?wx_fmt=png)

可从GitHub存储库“flashtech9/Flash”下载的文件列表

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)总结

Water Labbu通过将其恶意脚本注入其他诈骗者的欺诈网站，成功窃取加密货币资金，这表明其愿意利用其他恶意攻击者的方法达到自己的目的。

用户应注意来自不受信任方的任何投资邀请。此外，他们不应在任何未知平台上交易加密货币。

参考及来源：https://www.trendmicro.com/en\_us/research/22/j/water-labbu-abuses-malicious-dapps-to-steal-cryptocurrency.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibhuaKy6A3WHLicJOfiaaRPH2vemibJNmia9zCAkqwmpoxOQibk7qZTibpbqDw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibTnS3BkPFicuiafxVd2ud5NdtMbNibicjqaPwuH2YQkRtveM7qKELdVqwpw/640?wx_fmt=png)

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