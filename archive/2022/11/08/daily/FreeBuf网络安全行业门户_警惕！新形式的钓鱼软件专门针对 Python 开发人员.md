---
title: 警惕！新形式的钓鱼软件专门针对 Python 开发人员
url: https://www.freebuf.com/articles/349072.html
source: FreeBuf网络安全行业门户
date: 2022-11-08
fetch_date: 2025-10-03T21:56:40.165324
---

# 警惕！新形式的钓鱼软件专门针对 Python 开发人员

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

警惕！新形式的钓鱼软件专门针对 Python 开发人员

* ![]()
* 关注

警惕！新形式的钓鱼软件专门针对 Python 开发人员

2022-11-07 19:18:28

所属地 上海

![](https://image.3001.net/images/20221107/1667819890_6368e9722baa9cc4b1b62.jpg!small)最近，一种新形式的钓鱼软件专门攻击 Python 开发人员。攻击者通过伪造的 Python 包并使用常规的伪装技术，通过 W4SP Stealer 来感染开发人员的系统。W4SP Stealer 是一种用来窃取加密货币信息、泄露敏感数据并从开发人员系统收集凭据的木马工具。

根据软件供应链公司 Phylum 本周发布的一份报告中说：一名攻击者在 Python 包索引 (PyPI) 上创建了 29 个流行软件包的克隆，给它们包装成合法的软件包名称，这种做法被称为仿冒域名。如果开发人员下载并加载了恶意程序包，安装脚本则会通过一些混淆步骤来误导安装 W4SP Stealer 木马。目前，这些软件包的下载量已高达 5,700 次。

Phylum 的联合创始人兼首席技术官 Louis Lang 表示，虽然 W4SP Stealer 的作用是针对加密货币钱包和金融账户，但当前攻击者最重要目的很有可能是开发者的隐私。

这与我们过去经常遇到的电子邮件网络钓鱼活动的形式一样，只是这次攻击者只针对开发人员。“考虑到开发人员经常可以访问最核心的地方，一旦被成功的攻击那么会对组织造成毁灭性的打击。

该组织对 PyPI 的攻击是针对软件供应链的最新威胁。通过存储库服务分发的开源软件组件，例如 PyPI 和节点包管理器 (npm)，是一种流行的攻击媒介，因为导入软件的需求数量急剧增加。攻击者试图利用生态系统将恶意软件传输到粗心的开发人员系统中，例如2020 年对 Ruby Gems 生态系统的攻击和对Docker Hub 映像生态系统的攻击。而在 8 月，Check Point Software Technologies 的安全研究人员发现了 10 个 PyPI 软件包，它们都为窃取信息的恶意软件。

Phylum 研究人员 在他们的分析中表示：在这次最新的攻击活动中，这些软件包是一种更复杂的尝试，将 W4SP Stealer 传递到 Python 开发人员的机器上。并补充说：“由于这是一个持续的攻击，攻击者通过不断的改变策略，导致我们很难发现。同时，我们怀疑在不久的将来会出现更多类似的恶意软件。

### PyPI 攻击是一种“量化游戏”

这种攻击通过伪装通用软件包名称或使用新软件包来迷惑没有充分审查软件来源的开发人员。例如：一个名为“typesutil”的恶意程序包只是流行的 Python 程序包“datetime2”的副本，并进行了一些修改。

最初，任何导入恶意软件的程序都会在 Python 加载依赖项的设置阶段运行命令并下载恶意软件。后来，由于 PyPI 实施了某些检查，攻击者开始使用大量空格将可疑命令推送到大多数代码编辑器的正常可视范围之外。

Phylum 在其分析中说：攻击者稍微改变了策略，不是仅仅将导入文件放在一个明显的位置，而是将它放在屏幕外，利用 Python 很少使用的分号将恶意代码偷偷放到与其他合法代码的行中。

Phylum 的 Lang 表示，虽然域名仿冒是一种低保真攻击，成功率极低，但与潜在的回报相比，这种成本微乎其微。

这是一场量的游戏，攻击者每天都用大量的恶意软件包污染软件包生态系统。然而相对于回报率来说，成本却极低。

### 令人痛心的 W4SP

攻击的最终目标是安装“信息窃取木马 W4SP Stealer”，它入侵受害者的系统，窃取浏览器存储的密码，针对加密货币钱包，并使用关键字搜索感兴趣的文件，例如‘银行’和‘秘密’ 。

Lang说：除了窃取加密货币或银行信息带来的明显金钱回报外，攻击者还可以利用窃取的一些信息通过访问关键基础设施或借用开发人员的身份来进一步攻击。

目前，Phylum 在识别攻击者方面取得了一些进展，并向正在使用其基础设施的公司发送了报告。

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