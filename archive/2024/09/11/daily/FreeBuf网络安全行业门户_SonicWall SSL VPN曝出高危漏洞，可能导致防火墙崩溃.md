---
title: SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃
url: https://www.freebuf.com/news/410635.html
source: FreeBuf网络安全行业门户
date: 2024-09-11
fetch_date: 2025-10-06T18:28:37.515614
---

# SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

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

SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

2024-09-10 09:06:42

所属地 上海

![SonicWall](https://image.3001.net/images/20240910/1725935583_66dfafdfa436dadf1b3f9.jpeg!small)

近日，有黑客利用 SonicWall SonicOS 防火墙设备中的一个关键安全漏洞入侵受害者的网络。

这个不当访问控制漏洞被追踪为 CVE-2024-40766，影响到第 5 代、第 6 代和第 7 代防火墙。SonicWall于8月22日对其进行了修补，并警告称其只影响防火墙的管理访问界面。

然而，SonicWall上周五（9月6日）透露，该安全漏洞还影响了防火墙的SSLVPN功能，且已被黑客用以网络攻击。该公司提醒客户尽快为受影响的产品打上补丁，但没有透露有关野外利用的详细信息。

Arctic Wolf的安全研究人员认为这些攻击与Akira勒索软件背后的运营者有所关联，他们试图以SonicWall设备为目标，获得对目标网络的初始访问权。

Arctic Wolf高级威胁情报研究员Stefan Hostetler表示：在每个实例中，被攻击的账户都是设备本身的本地账户，而不是与微软活动目录等集中式身份验证解决方案集成在一起。此外，所有被入侵账户的 MFA 都被禁用，受影响设备上的 SonicOS 固件属于已知易受 CVE-2024-40766 影响的版本。

同时，网络安全机构Rapid7也在最近的事件中发现了针对SonicWall SSLVPN账户的勒索软件组织，但其表示将CVE-2024-40766与这些事件联系起来的证据仍然是间接的。

Arctic Wolf 和 Rapid7 复制了 SonicWall 的警告，并敦促管理员尽快升级到最新的 SonicOS 固件版本。

## 联邦机构被勒令在 9 月 30 日前打补丁

本周一（9月9日），CISA将此关键访问控制漏洞添加到其已知漏洞目录中，并命令联邦机构在 9 月 30 日之前的三周内，按照约束性操作指令 (BOD) 22-01 的规定，确保其网络中存在漏洞的 SonicWall 防火墙的安全。

SonicWall 缓解建议将防火墙管理和 SSLVPN 访问限制为可信来源，并尽可能禁止互联网访问。管理员还应为所有使用 TOTP 或基于电子邮件的一次性密码 (OTP) 的 SSLVPN 用户启用多因素身份验证 (MFA)。

在网络间谍和勒索软件攻击中，攻击者经常以 SonicWall 设备和设备为目标。例如，包括HelloKitty和FiveHands在内的多个勒索软件团伙也利用SonicWall的安全漏洞初步访问了受害者的企业网络。

> 参考来源：[Critical SonicWall SSLVPN bug exploited in ransomware attacks (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/critical-sonicwall-sslvpn-bug-exploited-in-ransomware-attacks/)

# 防火墙 # 高危漏洞 # SonicWall

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

联邦机构被勒令在 9 月 30 日前打补丁

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