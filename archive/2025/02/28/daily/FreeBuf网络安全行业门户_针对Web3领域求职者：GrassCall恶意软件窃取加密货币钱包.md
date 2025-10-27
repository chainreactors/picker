---
title: 针对Web3领域求职者：GrassCall恶意软件窃取加密货币钱包
url: https://www.freebuf.com/articles/423069.html
source: FreeBuf网络安全行业门户
date: 2025-02-28
fetch_date: 2025-10-06T20:37:41.965843
---

# 针对Web3领域求职者：GrassCall恶意软件窃取加密货币钱包

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

针对Web3领域求职者：GrassCall恶意软件窃取加密货币钱包

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

针对Web3领域求职者：GrassCall恶意软件窃取加密货币钱包

2025-02-27 17:11:02

所属地 上海

近日，一场针对Web3领域求职者的社交工程攻击通过一款名为“GrassCall”的恶意会议应用程序实施虚假面试，进而安装信息窃取恶意软件，窃取加密货币钱包。数百人已受到此次骗局的影响，部分受害者报告称其钱包中的资产被清空。

一个Telegram群组已成立，旨在讨论此次攻击，并帮助受影响的用户清除Mac和Windows设备上的恶意软件感染。

![黑客窃取加密货币](https://image.3001.net/images/20250227/1740618208769874_e86b98f0adb34475b853f5f0ec92232f.jpg!small)

## GrassCall攻击详情

此次攻击由一个名为“Crazy Evil”的俄语“traffer团队”发起。该团队通过社交工程攻击诱骗用户在Windows和Mac设备上下载恶意软件。这个网络犯罪团伙以瞄准加密货币领域的用户而闻名，通常通过社交媒体推广虚假游戏或工作机会。

用户被诱骗安装软件，这些软件会在设备上部署信息窃取恶意软件，用于窃取密码、身份验证Cookie以及钱包信息。在与受攻击的Web3专业人士Choy的交流中，BleepingComputer了解到，攻击者精心打造了一个在线身份，包括一个网站以及X和领英上的社交媒体资料，伪装成一家名为“ChainSeeker.io”的公司。

攻击者随后在领英、WellFound和CryptoJobsList（一个专注于Web3和区块链职业的热门招聘网站）上发布了高级职位列表。

![CryptoJobsList上推广的ChainSeeker职位](https://image.3001.net/images/20250227/1740618209525116_4a7258e63f0f4c57b1ae6754502f212d.jpg!small)CryptoJobsList上推广的ChainSeeker职位  来源: Choy

申请职位的求职者会收到一封包含面试邀请的电子邮件，他们将在面试中与首席营销官（CMO）会面。目标被要求通过Telegram与CMO联系以协调会议安排。

![虚假ChainSeeker公司的面试邀请](https://image.3001.net/images/20250227/1740618210137601_8f30efa1a0424d4aa2a983d4cc5323e4.jpg!small)虚假ChainSeeker公司的面试邀请  来源: Choy

当用户联系后，虚假的CMO会告知他们需要从指定网站下载一个名为“GrassCall”的视频会议软件，并使用提供的代码。

![与虚假ChainSeeker首席营销官的Telegram对话](https://image.3001.net/images/20250227/1740618210511097_35d0b4fcd45d40c5b75fadca3c638f24.jpg!small)与虚假ChainSeeker首席营销官的Telegram对话  来源: Choy

GrassCall软件从“grasscall[.]net”网站下载，根据访问者的浏览器用户代理提供Windows或Mac客户端。

![](https://image.3001.net/images/20250227/1740646448_67c02830c1aadcf9a101a.png!small)

GrassCall[.]net网站 来源: BleepingComputer

网络安全研究员g0njxa告诉BleepingComputer，GrassCall网站是之前攻击活动中使用的“Gatherum”网站的克隆版本。这些网站被用于由Crazy Evil子团队“kevland”实施的社交工程攻击，Recorded Future的一份报告对此进行了描述。

“Gatherum自称是一款AI增强的虚拟会议软件，主要在社交媒体（@GatherumAI）和AI生成的Medium博客（medium[.]com/@GatherumApp）上推广，”Recorded Future关于Crazy Evil网络犯罪分子的报告中解释道。

“负责Gatherum的traffers会获得一份操作手册。Gatherum由Crazy Evil子团队KEVLAND管理，Insikt Group内部将其追踪为CE-6。”

当访问者尝试下载GrassCall应用程序时，系统会提示他们输入虚假CMO在Telegram对话中分享的代码。输入正确的代码后，网站会提供Windows版的“GrassCall.exe”客户端[VirusTotal]或Mac版的“GrassCall\_v.6.10.dmg”客户端[VirusTotal]。当程序被执行时，两者都会安装信息窃取恶意软件或远程访问木马（RAT）。

虽然尚不清楚Windows客户端安装了哪种信息窃取恶意软件，但Mac版本会安装Atomic（AMOS）窃取程序。恶意软件运行时，会尝试基于关键词窃取文件、加密货币钱包、存储在Apple钥匙串中的密码，以及存储在网页浏览器中的密码和身份验证Cookie。

g0njxa告诉BleepingComputer，窃取的信息会上传到操作服务器，关于所窃取信息的内容会发布到网络犯罪企业使用的Telegram频道。“如果发现钱包，密码会被暴力破解，资产会被清空，并向诱使用户下载虚假软件的人支付报酬，”研究员表示。

研究员称，Crazy Evil成员的支付信息会公开发布到Telegram上，揭示该行动的成员可以从每个成功清空的受害者那里获得数万甚至数十万美元的收入。

![](https://image.3001.net/images/20250227/1740646488_67c0285850318a7e816dd.png!small)

Crazy Evil在Telegram上发布的支付信息 来源: G0njxa

针对此次攻击，CryptoJobsList删除了相关职位列表，并警告申请者这是骗局，建议他们扫描设备以查找恶意软件。

由于此次骗局引起了公众关注，攻击者似乎已终止了此次行动，相关网站已无法访问。然而，对于误装了该软件的用户，必须更改所访问网站的密码、密语和身份验证令牌，以及拥有的加密货币钱包的密码。

同样在追踪这些活动的网络安全研究员MalwareHunterTeam告诉BleepingComputer，Crazy Evil已发起了一场新的攻击，冒充一款名为Mystix的NFT区块链游戏。与此前的攻击类似，该游戏瞄准加密货币领域，并使用类似的恶意软件窃取加密货币钱包。

**参考来源：**

> [GrassCall malware campaign drains crypto wallets via fake job interview](https://www.bleepingcomputer.com/news/security/grasscall-malware-campaign-drains-crypto-wallets-via-fake-job-interviews/)

# 网络安全 # 数据安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

GrassCall攻击详情

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)