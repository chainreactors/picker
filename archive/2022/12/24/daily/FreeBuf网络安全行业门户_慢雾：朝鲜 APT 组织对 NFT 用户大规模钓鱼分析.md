---
title: 慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析
url: https://www.freebuf.com/articles/blockchain-articles/353456.html
source: FreeBuf网络安全行业门户
date: 2022-12-24
fetch_date: 2025-10-04T02:25:48.269558
---

# 慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析

2022-12-23 20:38:53

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# **背景**

9 月 2 日，慢雾安全团队发现疑似 APT 团伙针对加密生态的 NFT 用户进行大规模钓鱼活动，并发布了《[“零元购” NFT 钓鱼分析》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496261&idx=1&sn=9c657f56128df327e27c49fc49d4cc02&chksm=fdde8cc2caa905d4a9cd709c44888b54ccf4071301056052f0bc800b6d5d487873d3bafd124a&scene=21#wechat_redirect)。

9 月 4 日，推特用户 Phantom X 发推称朝鲜 APT 组织针对数十个 ETH 和 SOL 项目进行大规模的网络钓鱼活动。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799133_63a5a15d64ad08d7d9beb.jpg!small)

（<https://twitter.com/PhantomXSec/status/1566219671057371136>）

该推特用户给出了 196 个钓鱼域名信息，分析后关联到朝鲜黑客相关信息，具体的域名列表如下：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799134_63a5a15e29e89a8b8d2e8.jpg!small)

（<https://pastebin.com/UV9pJN2M>）

慢雾安全团队注意到该事件并第一时间跟进深入分析：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799134_63a5a15ecd5c641be0d6d.jpg!small)

（<https://twitter.com/IM_23pds/status/1566258373284093952>）

由于朝鲜黑客针对加密货币行业的攻击模型多样化，我们披露的也只是冰山一角，因为一些保密的要求，本篇文章也仅针对其中一部分钓鱼素材包括相关钓鱼钱包地址进行分析。这里将重点针对 NFT 钓鱼进行分析。

# **钓鱼网站分析**

经过深入分析，发现此次钓鱼的其中一种方式是发布虚假 NFT 相关的、带有恶意 Mint 的诱饵网站，这些 NFT 在 OpenSea、X2Y2 和 Rarible 等平台上都有出售。此次 APT 组织针对 Crypto 和 NFT 用户的钓鱼涉及将近 500 多个域名。

查询这些域名的注册相关信息，发现注册日期最早可追溯到 7 个月前：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799135_63a5a15f6ed8315c96d39.jpg!small)

同时我们也发现朝鲜黑客常使用的一些独有的钓鱼特征：

**特征一：钓鱼网站都会记录访客数据并保存到外部站点。**黑客通过 HTTP GET 请求将站点访问者信息记录到外部域，发送请求的域名虽不同但是请求的 API  接口都为 “/postAddr.php”。一般格式为 “<https://nserva.live/postAddr.php?mmAddr=...>[Metamask]...&accessTime=xxx&url=evil.site”，其中参数 mmAddr 记录访客的钱包地址，accessTime 记录访客的访问时间，url 记录访客当前所访问的钓鱼网站链接。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799136_63a5a1602482304452dc0.jpg!small)

**特征二：钓鱼网站会请求一个 NFT 项目价目表**，通常 HTTP 的请求路径为 “getPriceData.php”：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799137_63a5a1617dcd962a71bd9.jpg!small)

**特征三：存在一个链接图像到目标项目的文件 “imgSrc.js”**，包含目标站点列表和在其相应网络钓鱼站点上使用的图像文件的托管位置，这个文件可能是钓鱼网站模板的一部分。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799138_63a5a1624f7c4ccf06d06.jpg!small)

进一步分析发现 APT 用于监控用户请求的主要域名为 “thedoodles.site”，此域名在 APT 活动早期主要用来记录用户数据：

查询该域名的 HTTPS 证书启用时间是在 7 个月之前，黑客组织已经开始实施对 NFT 用户对攻击。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799138_63a5a162e6ee001bddd6e.jpg!small)

最后来看下黑客到底运行和部署了多少个钓鱼站点：

比如最新的站点伪装成世界杯主题：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799140_63a5a164287b0a921ad9f.jpg!small)

继续根据相关的 HTTPS 证书搜索得到相关的网站主机信息：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799141_63a5a1652f5f400c04123.jpg!small)

在一些主机地址中发现了黑客使用的各种攻击脚本和统计受害者信息的 txt 文件。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799141_63a5a165eef3d201262c6.jpg!small)

这些文件记录了受害者访问记录、授权情况、使用插件钱包的情况：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799143_63a5a16750f8326c53147.jpg!small)

可以发现这些信息跟钓鱼站点采集的访客数据相吻合。

其中还包括受害者 approve 记录：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799145_63a5a16959b2dece845ac.jpg!small)

以及签名数据 sigData 等，由于比较敏感此处不进行展示。

另外，统计发现主机相同 IP 下 NFT 钓鱼站群，单独一个 IP 下就有 372 个 NFT 钓鱼站点：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799146_63a5a16abea5a5792d3c7.jpg!small)

另一个 IP 下也有 320 个 NFT 钓鱼站群：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799147_63a5a16b59f1f777fc90c.jpg!small)

甚至包括朝鲜黑客在经营的一个 DeFi 平台：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799147_63a5a16be380658082c59.jpg!small)

由于篇幅有限，此处不再赘述。

# **钓鱼手法分析**

结合之前《[NFT 零元购钓鱼](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496261&idx=1&sn=9c657f56128df327e27c49fc49d4cc02&chksm=fdde8cc2caa905d4a9cd709c44888b54ccf4071301056052f0bc800b6d5d487873d3bafd124a&scene=21#wechat_redirect)》文章，我们对此次钓鱼事件的核心代码进行了分析。我们发现黑客钓鱼涉及到 WETH、USDC、DAI、UNI 等多个地址协议。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799148_63a5a16c8099017cd650b.jpg!small)

下面代码用于诱导受害者进行授权 NFT、ERC20 等较常见的钓鱼 Approve 操作：

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799149_63a5a16d6db9af46df0c9.jpg!small)

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799150_63a5a16e1e92700d1c2bd.jpg!small)

除此之外，黑客还会诱导受害者进行 Seaport、Permit 等签名。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799151_63a5a16f2ed9878414d84.jpg!small)

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799152_63a5a1703efb4ba2112b6.jpg!small)

下面是这种签名的正常样例，只是在钓鱼网站中不是 “opensea.io” 这个域名。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799152_63a5a170c5868276b87c1.jpg!small)

我们在黑客留下的主机也发现了这些留存的签名数据和 “Seaport” 的签名数据特征一致。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799153_63a5a171724facb575917.jpg!small)

由于这类型的签名请求数据可以“离线存储”，黑客在拿到大量的受害者签名数据后批量化的上链转移资产。

# **MistTrack 分析**

对钓鱼网站及手法分析后，我们选取其中一个钓鱼地址（0xC0fd...e0ca）进行分析。

可以看到这个地址已被 MistTrack 标记为高风险钓鱼地址，交易数也还挺多。钓鱼者共收到 1055 个 NFT，售出后获利近 300 ETH。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799154_63a5a1722653de55ad7ee.jpg!small)

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799155_63a5a1730a1e5212d444c.jpg!small)

往上溯源，该地址的初始资金来源于地址（0x2e0a...DA82）转入的 4.97 ETH。往下溯源，则发现该地址有与其他被 MistTrack 标记为风险的地址有交互，以及有 5.7 ETH 转入了 FixedFloat。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799155_63a5a173a156126320359.jpg!small)

再来分析下初始资金来源地址（0x2e0a...DA82），目前收到约 6.5 ETH。初始资金来源于 Binance 转入的 1.433 ETH。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799156_63a5a17479c9d49be48ed.jpg!small)

同时，该地址也是与多个风险地址进行交互。

![慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](https://image.3001.net/images/20221223/1671799157_63a5a17502e8c84d21404.jpg!small)

# **总结**

由于保密性和隐私性，本文仅针对其中一部分 NFT 钓鱼素材进行分析，并提炼出朝鲜黑客的部分钓鱼特征，当然，这只是冰山一角。慢雾在此建议，用户需加强对安全知识的了解，进一步强化甄别网络钓鱼攻击的能力等，避免遭遇此类攻击。更多的安全知识建议阅读慢雾出品的《区块链黑暗森林自救手册》：<https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README_CN.md>

Ps. 感谢 hip 、ScamSniffer 提供的支持。

相关链接：

<https://www.prevailion.com/what-wicked-webs-we-unweave>

<https://twitter.com/PhantomXSec/status/1566219671057371136>

<https://twitter.com/evilcos/status/1603969894965317632>

其他钓鱼方式，推荐阅读：

[慢雾：空白支票 eth\_sign 钓鱼分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496513&idx=1&sn=63b0f0126ef73da56064f947933178e2&chksm=fdde8dc6caa904d03bae041013a3c58663dca29cebbafec576d1f65cb57bc785e136d1911114&scene=21#wechat_redirect)

[慢雾：警惕 TransferFrom 零转账骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496770&idx=1&sn=f95df1020b2319e3a1c9469829686c13&chksm=fdde8ac5caa903d3f873fed02a107b0be4ba5343256d5882e4540480cbae1adeb8e6759a6f65&scene=21#wechat_redirect)

[慢雾：警惕相同尾号空投骗局](http://mp.weixin.qq.com/s?__biz=MzU4O...