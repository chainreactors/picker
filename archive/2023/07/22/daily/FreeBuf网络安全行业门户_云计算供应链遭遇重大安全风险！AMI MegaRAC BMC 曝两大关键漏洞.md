---
title: 云计算供应链遭遇重大安全风险！AMI MegaRAC BMC 曝两大关键漏洞
url: https://www.freebuf.com/news/372790.html
source: FreeBuf网络安全行业门户
date: 2023-07-22
fetch_date: 2025-10-04T11:54:54.494410
---

# 云计算供应链遭遇重大安全风险！AMI MegaRAC BMC 曝两大关键漏洞

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

云计算供应链遭遇重大安全风险！AMI MegaRAC BMC 曝两大关键漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

云计算供应链遭遇重大安全风险！AMI MegaRAC BMC 曝两大关键漏洞

2023-07-21 17:43:39

所属地 上海

![1689932612_64ba534408075fe4d81e5.png!small](https://image.3001.net/images/20230721/1689932612_64ba534408075fe4d81e5.png!small)近日，AMI MegaRAC Baseboard Management Controller (BMC)软件中披露了两个安全漏洞，这些漏洞一旦被攻击者成功利用，将可远程控制服务器并直接部署恶意软件。

Eclypsium 研究人员 Vlad Babkin 和 Scott Scheferman 在与 The Hacker News 分享的一份报告中说：这些新漏洞的严重程度从低到高不等，包括未经验证的远程代码执行和具有超级用户权限的未经授权设备访问。

能够访问 Redfish 远程管理界面的远程攻击者，或者从受损的主机操作系统，都可以利用这些漏洞。

更糟糕的是，这些缺陷也可能被“武器化”，使持久固件植入物不受操作系统重新安装和硬盘驱动器更换、砖砌主板组件的影响，通过过电压攻击造成物理损坏，并引发无限期的重新启动循环。

研究人员指出：随着攻击者将重点从面向用户的操作系统转移到硬件和计算信任所依赖的底层嵌入式代码，入侵行为变得更难检测，补救措施也更加复杂。

此次Eclypsium的发现基于RansomExx组织在2021年8月针对硬件制造商技嘉的勒索软件攻击中泄露的AMI固件的分析。此次的新漏洞被命名为BMC&C，其中一些漏洞是固件安全公司在2022年12月（CVE-2022-40259、CVE-2022-40242和CVE-2022-2827）和2023年1月（CVE-2022-26872和CVE-2022-40258）披露的。

新漏洞列表如下：

* CVE-2023-34329 (CVSS 得分：9.1) - 通过 HTTP 报头欺骗进行身份验证绕过
* CVE-2023-34330（CVSS 得分：8.2）--通过动态 Redfish 扩展接口注入代码

当这两个漏洞 一并出现的时候，其严重程度评分达到 10.0，将允许对手绕过 Redfish 身份验证，并以最高权限在 BMC 芯片上远程执行任意代码。此外，上述漏洞还可与 CVE-2022-40258 串联起来，以用来破解 BMC 芯片上管理员账户的密码。

值得注意的是，在这个过程中，可能还涉及到恶意软件被非法安装的相关问题。这些恶意软件可以在安全软件的监视下不仅可以进行长期的网络间谍活动，甚至还可以通过电源管理篡改技术（如 PMFault）直接破坏 CPU 。

虽然没有证据表明这些漏洞已被广泛利用，但 MegaRAC BMC（主要供应商出货的数百万台设备中的关键供应链组件）确实已经成为了威胁行为者的重要目标。

研究人员表示，这些漏洞给那些以云计算为基础的技术供应链带来了巨大风险。简单来说，就是一个组件供应商的漏洞可能会影响到许多其他的硬件供应商，而这些硬件供应商的漏洞又会传递给许多云计算服务。

这些漏洞可能会对企业的服务器、硬件以及支持其使用的云服务的硬件构成风险。

> 参考来源：[Critical Flaws in AMI MegaRAC BMC Software Expose Servers to Remote Attacks](https://thehackernews.com/2023/07/critical-flaws-in-ami-megarac-bmc.html)

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