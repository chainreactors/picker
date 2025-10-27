---
title: Ivanti曝新的MobileIron零日漏洞，正在被恶意利用
url: https://www.freebuf.com/news/375839.html
source: FreeBuf网络安全行业门户
date: 2023-08-24
fetch_date: 2025-10-04T12:01:37.044649
---

# Ivanti曝新的MobileIron零日漏洞，正在被恶意利用

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

Ivanti曝新的MobileIron零日漏洞，正在被恶意利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Ivanti曝新的MobileIron零日漏洞，正在被恶意利用

2023-08-23 10:22:16

所属地 上海

![](https://image.3001.net/images/20230823/1692757291_64e56d2b404f08acb4e5b.png!small)

美国 IT 软件公司 Ivanti 今天提醒客户，一个关键的 Sentry API 身份验证绕过漏洞正在被恶意利用。

Ivanti Sentry（前身为 MobileIron Sentry）在 MobileIron 部署中充当 Microsoft Exchange Server 等企业 ActiveSync 服务器或 Sharepoint 服务器等后端资源的守门员，它还可以充当 Kerberos 密钥分发中心代理（KKDCP）服务器。

网络安全公司 mnemonic 的研究人员发现并报告了这个关键漏洞（CVE-2023-38035），未经身份验证的攻击者可以通过 MobileIron 配置服务（MICS）使用的 8443 端口访问敏感的管理门户配置 API。

攻击者利用限制性不足的 Apache HTTPD 配置绕过身份验证控制后，就可以实现这一点。

成功利用后，他们就可以在运行 Ivanti Sentry 9.18 及以前版本的系统上更改配置、运行系统命令或写入文件。

Ivanti 建议管理员不要将 MICS 暴露在互联网上，并限制对内部管理网络的访问。

Ivanti 表示："截至目前，我们仅发现少数客户受到 CVE-2023-38035 的影响。该漏洞不会影响其他 Ivanti 产品或解决方案，如 Ivanti EPMM、MobileIron Cloud 或 Ivanti Neurons for MDM"。

随后，该公司补充说："在得知该漏洞后，我们立即调动资源修复该问题，并为所有支持版本提供了RPM脚本。我们建议客户首先升级到支持的版本，然后应用专门为其版本设计的 RPM 脚本"。

## 四月份以来被攻击利用的其他 Ivanti 漏洞

自 4 月份以来，国家支持的黑客已经利用了 Ivanti 的 Endpoint Manager Mobile (EPMM)（以前称为 MobileIron Core）中的另外两个安全漏洞。

其中一个（被追踪为 CVE-2023-35078）是一个重要的身份验证绕过漏洞，该漏洞作为零日漏洞被滥用，入侵了挪威多个政府实体的网络。

该漏洞还可与一个目录遍历漏洞（CVE-2023-35081）结合，使具有管理权限的威胁行为者能够在被入侵系统上部署网络外壳。

CISA在8月初发布的一份公告中说：高级持续威胁（APT）组织至少在2023年4月至2023年7月期间利用CVE-2023-35078作为零日漏洞，从多个挪威组织收集信息，并访问和入侵了一个挪威政府机构的网络。

在CISA与挪威国家网络安全中心（NCSC-NO）发布联合公告之前，本月早些时候曾发布命令，要求美国联邦机构在8月15日和8月21日前修补这两个被主动利用的漏洞。

一周前，Ivant 还修复了其企业移动管理（EMM）解决方案 Avalanche 软件中的两个关键的基于堆栈的缓冲区溢出，被追踪为 CVE-2023-32560，利用后可能导致崩溃和任意代码执行。

> 参考链接：https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-actively-exploited-mobileiron-zero-day-bug/

# 资讯 # 漏洞

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

四月份以来被攻击利用的其他 Ivanti 漏洞

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