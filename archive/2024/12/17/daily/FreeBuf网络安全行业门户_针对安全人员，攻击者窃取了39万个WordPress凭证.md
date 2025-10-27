---
title: 针对安全人员，攻击者窃取了39万个WordPress凭证
url: https://www.freebuf.com/news/417776.html
source: FreeBuf网络安全行业门户
date: 2024-12-17
fetch_date: 2025-10-06T19:39:52.176407
---

# 针对安全人员，攻击者窃取了39万个WordPress凭证

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

针对安全人员，攻击者窃取了39万个WordPress凭证

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

针对安全人员，攻击者窃取了39万个WordPress凭证

2024-12-16 10:56:25

所属地 上海

据BleepingComputer消息，一个被标记为 MUT-1244 的攻击者利用植入木马的 WordPress 凭证检查器进行了一次规模庞大、长达一年的攻击活动，盗取了超过 39 万个 WordPress 凭证。

![](https://image.3001.net/images/20241216/1734318146_675f98421f30ed8fdb131.png!small)

Datadog Security Labs 的研究人员发现了这些攻击，并表示被感染系统中有数百名受害者的 SSH 私钥和 AWS 访问密钥也被盗取，这些受害者很可能包括红队成员、渗透测试员、安全研究人员甚至其他一些黑客。

被感染者通过相同的第二阶段恶意载荷进行感染，该恶意载荷通过数十个植入了木马的 GitHub 代码库传播，这些代码库提供了针对已知安全漏洞的恶意的概念验证（PoC）漏洞利用代码以及一项钓鱼活动，引导目标安装伪装成 CPU 微码升级的虚假内核升级。

虽然钓鱼电子邮件诱使受害者执行命令安装恶意软件，但虚假代码库则欺骗了寻求特定漏洞利用代码的安全专业人员和其他一些黑客。在此之前，攻击者曾利用虚假的概念验证漏洞来攻击研究人员，希望窃取有价值的研究成果或者获得对网络安全公司网络的访问权限。

研究人员表示，由于它们的命名方式，其中几个代码库会自动包含在 Feedly Threat Intelligence 或Vulnmon 等合法来源中，作为这些漏洞的概念验证代码库，这增加了它们的合法性和被运行的可能性。

这些恶意载荷通过 GitHub 代码库使用多种方法进行传播，包括带有后门的配置编译文件、恶意 PDF 文件、 Python 样本传播程序以及包含在项目依赖项中的恶意 npm 包。

正如 Datadog Security Labs 发现的那样，这次攻击与Checkmarkx 在 11 月发布的一份报告中提到的一次为期一年的供应链攻击有重叠之处，这次攻击通过在"hpc20235/yawp" GitHub 项目中使用"0xengine/xmlrpc" npm 包中的恶意代码来窃取数据和挖掘 Monero 加密货币。

攻击中部署的恶意软件包括一个加密货币挖矿程序和一个后门，帮助 MUT-1244 收集和窃取私有 SSH 密钥、 AWS 凭证、环境变量以及密钥目录内容，比如"~/.aws"。

第二阶段的恶意载荷托管在一个独立的平台上，使攻击者能够将数据导出到像 Dropbox 和file.io 这样的文件共享服务中，调查人员在恶意载荷中找到了这些平台的硬编码凭证，使攻击者能够轻松访问被窃取的信息。

![](https://image.3001.net/images/20241216/1734317868_675f972c0da01d2855683.png!small)攻击流程

Datadog Security Labs 的研究人员表示，MUT-1244 成功获取了超过 39 万个WordPress凭证，并高度确信这些凭证在被导出到 Dropbox 之前就已经落入了攻击者手中。

攻击者成功利用了网络安全界的互信关系，通过目标在无意中执行攻击者的恶意软件而侵入了数十台白帽和黑帽黑客的机器，导致包括 SSH 密钥、 AWS 访问令牌和命令历史在内的数据被窃取。

Datadog Security Labs 估计，数百台系统仍然会受到攻击，而其他系统仍在遭受这次持续攻击带来的感染。

**参考来源：**

> [390,000 WordPress accounts stolen from hackers in supply chain attack](https://www.bleepingcomputer.com/news/security/390-000-wordpress-accounts-stolen-from-hackers-in-supply-chain-attack/)

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