---
title: 黑客背刺同行，向对方发送信息窃取软件
url: https://www.freebuf.com/news/410373.html
source: FreeBuf网络安全行业门户
date: 2024-09-07
fetch_date: 2025-10-06T18:28:07.998532
---

# 黑客背刺同行，向对方发送信息窃取软件

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

黑客背刺同行，向对方发送信息窃取软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客背刺同行，向对方发送信息窃取软件

2024-09-06 10:58:19

所属地 上海

据BleepingComputer消息，有黑客使用一种假冒的 OnlyFans 工具瞄准其他黑客，声称可以用来帮助窃取用户帐户，但实际上却是用 Lumma信息窃取器对这些黑客发动入侵。

这项由 Veriti Research 发现的现象反映了网络犯罪分子之间并非是统一的”猎食者“身份，彼此之间的背刺时有发生。

这次黑客所利用的OnlyFans 是一个非常受欢迎、基于用户订阅的内容创作平台，创作者可以与订阅者分享视频、图像、消息和直播流，而订阅者则需要支付经常性费用或一次性付款以获得独家内容。鉴于它的受欢迎程度，OnlyFans 帐户经常成为攻击者的目标，试图劫持账户、勒索账户所有者支付赎金，或者干脆泄露私人照片。

![](https://image.3001.net/images/20240906/1725591592_66da702820545ae51fdf3.png!small)黑客论坛上的OnlyFans恶意工具广告

因此，黑客开发了一种能快速验证账户的工具，检查登录信息是否与任何 OnlyFans 账户匹配，以及是否仍然有效，否则，黑客就必须手动测试成千上万个凭证，其过程既不现实又繁琐，导致该计划无法实施。

然而，正是由于该工具由黑客创建并在其他黑客中传播，处于竞争关系的黑客必然在其中留了一手，对其他黑客窃取信息以将自身利益最大化。

Veriti发现的假冒OnlyFans 工具内含有Lumma信息窃取器，有效载荷名为 "brtjgjsefd.exe"，是从 GitHub 存储库中获取并加载到受害者计算机中。Lumma 自 2022 年以来一直以每月 250-1000 美元的价格出租给网络犯罪分子，并通过各种方式传播，包括恶意广告、YouTube 评论、种子文件以及最近的 GitHub 评论。

Lumma 具有创新的规避机制和恢复过期谷歌会话令牌的能力。 它主要用于窃取双因素身份验证代码、加密货币钱包，以及存储在受害者浏览器和文件系统中的密码、cookie 和信用卡。 Lumma 本身也是一个加载器，能够在被入侵系统中引入额外的有效载荷，并执行 PowerShell 脚本。

Veriti 发现，当 Lumma Stealer 有效载荷启动时，它会连接到一个名为 "UserBesty "的 GitHub 账户，幕后黑客利用该账户托管其他恶意有效载荷。

这并不是黑客第一次针对其他网络犯罪分子进行恶意攻击。 2022 年 3 月，黑客利用伪装成破解 RAT 和恶意软件构建工具的剪贴板窃取程序来窃取加密货币。 同年晚些时候，一名恶意软件开发者在自己的恶意软件中设置了后门，以窃取其他黑客的凭证、加密货币钱包和 VPN 账户数据。

**参考来源：**

> [Hacker trap: Fake OnlyFans tool backstabs cybercriminals, steals passwords](https://www.bleepingcomputer.com/news/security/hacker-trap-fake-onlyfans-tool-backstabs-cybercriminals-steals-passwords/)

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