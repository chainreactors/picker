---
title: 警惕，Foxit PDF 阅读器存在设计”缺陷“
url: https://www.freebuf.com/news/401073.html
source: FreeBuf网络安全行业门户
date: 2024-05-17
fetch_date: 2025-10-06T17:15:59.596387
---

# 警惕，Foxit PDF 阅读器存在设计”缺陷“

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

警惕，Foxit PDF 阅读器存在设计”缺陷“

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕，Foxit PDF 阅读器存在设计”缺陷“

2024-05-16 10:47:56

所属地 上海

目前，PDF 已然成为了数字通信中不可或缺的一部分，在 PDF 阅读器领域，Adobe Acrobat Reader 占据了最大的市场份额，但近些年后起之秀 Foxit PDF Reader 的市场占有率开始突飞猛进，在 200 多个国家拥有超过 7 亿用户。![1715827770_6645743a6ad3ded78a358.png!small](https://image.3001.net/images/20240516/1715827770_6645743a6ad3ded78a358.png!small)

然而，Check Point Research 近日发现了一种针对 Foxit Reader 用户的 PDF 安全漏洞利用的异常操作模式，该安全漏洞会触发安全警告，诱使毫无戒心的用户执行”有害“命令。目前，该安全漏洞的变体在野外正被积极利用

## ****Foxit PDF Reader 设计中存在安全缺陷****

研究人员表示，安全漏洞是由 Foxit Reader 中警告消息中某个设计缺陷引发。据悉，警告消息中提供了一个”有害“的默认选项，一旦有粗心的用户使用默认选项，安全漏洞就会自动触发，从远程服务器下载并执行恶意有效负载。![1715827841_6645748117d196900ffb1.png!small?1715827842101](https://image.3001.net/images/20240516/1715827841_6645748117d196900ffb1.png!small?1715827842101)

触发恶意命令的默认选项

安全研究人员已经证实安全漏洞已经被多个威胁攻击者用于电子犯罪和间谍活动。其中，名为 APT-C-35 / DoNot Team 威胁组织发起的某一间谍组织最为”著名“。威胁攻击者通过部署特定恶意软件、获得受害者的数据信息。此外，威胁攻击者能够开展针对 Windows 和 Android 设备的混合攻击活动，从而绕过双因素身份验证 （2FA） 。

VenomRAT、Agent-Tesla、Remcos、NjRAT、NanoCore RAT、Pony、Xworm、AsyncRAT、DCRat 等在内的各种网络犯罪攻击者都在利用该安全漏洞，以分发、部署恶意软件。Check Point Research 跟踪了一起可能是通过 Facebook 分发恶意软件的活动，发现了一条攻击链。![1715827836_6645747c8acfaf420df21.png!small?1715827839089](https://image.3001.net/images/20240516/1715827836_6645747c8acfaf420df21.png!small?1715827839089)

攻击链

在另一场攻击活动中，Check Point Research 确认了威胁攻击者为@silentkillertv，主要利用两个链接的PDF 文件执行活动，其中一个文件托管在合法网站 trello.com 上。威胁攻击者还销售恶意工具，并于 4 月 27 日宣传了这一漏洞。
![1715827877_664574a5902faff843dfd.png!small?1715827878698](https://image.3001.net/images/20240516/1715827877_664574a5902faff843dfd.png!small?1715827878698)

研究过程中，Check Point 获得了多个攻击者拥有的构建器，这些构建器利用此漏洞创建恶意 PDF 文件，大多数收集的 PDF 正在执行 PowerShell 命令，该命令从远程服务器下载有效负载，然后立刻执行。![1715827906_664574c29f19b61d560ca.png!small?1715827908419](https://image.3001.net/images/20240516/1715827906_664574c29f19b61d560ca.png!small?1715827908419)

PDF 命令执行分析。

最后，安全人员指出，随着社会工程策略的日益复杂，用户必须时刻保持警惕，随时了解自身网络安全状况，谨慎行事，并实施包括多因素身份验证和安全意识培训等在内的安全措施，以最大程度上降低成为此类攻击受害者的风险。

参考文章：

> https://blog.checkpoint.com/research/foxit-pdf-reader-flawed-design-hidden-dangers-lurking-in-common-tools/

# 安全漏洞

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

Foxit PDF Reader 设计中存在安全缺陷

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