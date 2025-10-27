---
title: 微软：警惕利用VMware ESXi进行身份验证绕过攻击
url: https://www.freebuf.com/news/407317.html
source: FreeBuf网络安全行业门户
date: 2024-07-31
fetch_date: 2025-10-06T17:43:49.535009
---

# 微软：警惕利用VMware ESXi进行身份验证绕过攻击

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

微软：警惕利用VMware ESXi进行身份验证绕过攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软：警惕利用VMware ESXi进行身份验证绕过攻击

2024-07-30 11:12:00

所属地 上海

微软于7月29日发布警告，称勒索软件团伙正在积极利用 VMware ESXi 身份验证绕过漏洞进行攻击。

![](https://image.3001.net/images/20240730/1722309575_66a85bc7dc9a89f73fb43.png!small)

该漏洞被追踪为 CVE-2024-37085，由微软安全研究人员 Edan Zwick、Danielle Kuznets Nohi 和 Meitar Pinto 发现，并在 6 月 25 日发布的 ESXi 8.0 U3 更新中进行了修复。

研究称，该漏洞能让攻击者将新用户添加到由他们创建的“ESX 管理员”组中，并自动获得对 ESXi 虚拟机监控程序的完全管理权限。

虽然成功实施攻击需要对目标设备和用户交互具有高权限，但微软表示，已有几个勒索软件团伙利用漏洞完全掌控了管理员权限，窃取存储在托管虚拟机上的敏感数据，在受害者的网络中横向移动，并加密 ESXi 虚拟机管理程序的文件系统。

微软已确定至少三种可用于利用 CVE-2024-37085 漏洞的策略，包括：

* 将“ESX Admins”组添加到域并添加用户。
* 将域中的任何组重命名为“ESX Admins”，并将用户添加到组或使用现有组成员。
* ESXi 虚拟机管理程序特权刷新（为其他组分配管理员权限不会将其从“ESX 管理员”组中移除）。

到目前为止，该漏洞已被被追踪为 Storm-0506、Storm-1175、Octo Tempest 和 Manatee Tempest 的勒索软件运营商在野外利用，并在攻击中部署了Akira和Black Basta勒索软件。例如，Storm-0506 在利用 CVE-2024-37085 漏洞提升权限后，在一家北美工程公司的 ESXi 虚拟机管理程序上部署了 Black Basta 勒索软件。

![](https://image.3001.net/images/20240730/1722309483_66a85b6b92073da8e2772.png!small)以Storm-0506为例的ESXi 攻击链

由于 ESXi 虚拟机 （VM） 具有高效的资源处理能力，目前已有许多企业开始使用该产品来托管关键应用程序和存储，这也导致针对企业组织的 ESXi 虚拟机管理程序的攻击趋势越来越明显。微软警告称，在过去三年中，针对 ESXi 虚拟机管理程序并对其造成影响的微软事件响应（Microsoft IR）事件数量增加了一倍多。

攻击者一旦攻破虚拟机，不仅可以对企业正常业务开展造成巨大破环，还能将存储在虚拟机管理程序上的文件和备份进行加密，从而严重限制企业恢复数据的能力。

**参考来源：**

> [Microsoft: Ransomware gangs exploit VMware ESXi auth bypass in attacks](https://www.bleepingcomputer.com/news/microsoft/microsoft-ransomware-gangs-exploit-vmware-esxi-auth-bypass-in-attacks/)

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