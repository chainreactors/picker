---
title: 可获root权限，思科NX-OS 零日漏洞修复已发布
url: https://www.freebuf.com/news/404980.html
source: FreeBuf网络安全行业门户
date: 2024-07-03
fetch_date: 2025-10-06T17:43:03.447087
---

# 可获root权限，思科NX-OS 零日漏洞修复已发布

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

可获root权限，思科NX-OS 零日漏洞修复已发布

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

可获root权限，思科NX-OS 零日漏洞修复已发布

2024-07-02 13:16:25

所属地 上海

> **思科修补了 4 月份曝出的 NX-OS 零日漏洞，威胁攻击者可以利用该漏洞在受影响的交换机上以 root 身份，安装未知恶意软件。**

![1719905418_6683ac8ad8da8f70949ff.png!small](https://image.3001.net/images/20240702/1719905418_6683ac8ad8da8f70949ff.png!small)

网络安全公司 Sygnia 发现并向思科方面报告了安全漏洞事件，威胁攻击者利用安全漏洞进入受害者内部系统后，收集了大量的管理员级的凭据，一边可以随时访问思科 Nexus 交换机，部署了一个此前未出现过的定制化恶意软件。

此后，威胁攻击者利用这一”渠道“，便可以轻松的远程连接到受害者的设备，上传额外文件并执行恶意代码。

接到漏洞通知后，思科方面立刻做出回应，指出具有管理员权限的本地威胁攻击者可以利用安全漏洞（跟踪为 CVE-2024-20399），在易受攻击设备的底层操作系统上以 root 权限执行任意命令。

此外，思科相关负责人还指出，CVE-2024-20399 安全漏洞是对传递给特定配置 CLI 命令的参数验证不足造成的，使威胁攻击者能够通过将精心制作的输入作为受影响的配置 CLI 命令的参数，从而利用这一安全漏洞。

**一旦威胁攻击者成功利用该安全漏洞后，就可以以 root 权限在底层操作系统上执行任意命令。**![](https://image.3001.net/images/20240702/1719905858_6683ae425e2a96047b571.jpg!small)受影响设备的列表包括多个运行易受攻击的 NX-OS 软件的交换机：

> MDS 9000 系列多层交换机；
> Nexus 3000 系列交换机；
> Nexus 5500 平台交换机；
> Nexus 5600 平台交换机；
> Nexus 6000 系列交换机；
> Nexus 7000 系列交换机；
> 独立 NX-OS 模式下的 Nexus 9000 系列交换机。

威胁攻击者还可以利用 CVE-2024-20399 安全漏洞，在不触发系统 syslog 消息的情况下执行命令，从而使其能够在被攻击的 NX-OS 设备上隐藏入侵迹象。

因此，思科方面强烈建议客户应当定期监控和更改 network-admin 和 vdc-admin 管理用户的凭证。

今年 4 月，思科曾警告称，自 2023 年 11 月以来，一个由国家支持的黑客组织（被追踪为 UAT4356 和 STORM-1849）一直在利用 Adaptive Security Appliance (ASA) 和 Firepower Threat Defense (FTD) 防火墙中的多个零日漏洞（CVE-2024-20353 和 CVE-2024-20359），针对全球政府网络开展名为 ArcaneDoor 的活动。

当时，斯克公司多次强调，安全研究人员还发现有证据表明，威胁攻击者至少从 2023 年 7 月起就针对这些零日安全漏洞测试和开发了漏洞利用程序。之后，威胁攻击者利用这些安全漏洞安装了未知的恶意软件，使其能够在被入侵的 ASA 和 FTD 设备上留下“后门”。

值得一提的是，思科指出尚未确定威胁攻击者用来入侵受害者网络的初始攻击载体。

上个月，Sygnia 称 Velvet Ant 在一次网络间谍活动中利用定制恶意软件攻击了 F5 BIG-IP 设备，在这次攻击活动中，威胁攻击者利用对受害者网络的持续访问，在长达三年的时间里“偷偷”窃取了大量的敏感客户和财务信息。

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