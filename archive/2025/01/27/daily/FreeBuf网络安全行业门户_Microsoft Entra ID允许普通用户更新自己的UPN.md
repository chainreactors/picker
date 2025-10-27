---
title: Microsoft Entra ID允许普通用户更新自己的UPN
url: https://www.freebuf.com/news/420832.html
source: FreeBuf网络安全行业门户
date: 2025-01-27
fetch_date: 2025-10-06T20:08:27.150486
---

# Microsoft Entra ID允许普通用户更新自己的UPN

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

Microsoft Entra ID允许普通用户更新自己的UPN

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Microsoft Entra ID允许普通用户更新自己的UPN

2025-01-26 10:30:00

所属地 上海

![](https://image.3001.net/images/20250126/1737860330_6795a4ea3784099fbdbcd.jpg!small)

微软允许非特权用户在Entra ID中更新自己的用户主体名称 (UPN) ，这引发了对安全和管理监督的担忧。

测试证实，普通用户可以通过Entra管理中心进入账户属性页面，直接编辑自己的UPN。也可以通过Microsoft Graph PowerShell SDK进行类似的更新，这两种接口都依赖于Microsoft Graph Users API。

![](https://image.3001.net/images/20250126/1737860411_6795a53b11d12f4498050.jpg!small)Eric Hammond Entra帐户的属性

![](https://image.3001.net/images/20250126/1737860598_6795a5f65fb389b3c98fe.jpg!small)使用Microsoft Graph PowerShell SDK更新用户主体名称

作为访问微软服务的关键标识符，此前，UPN的更新通常仅限于管理员，但现在任何用户都可以修改自己的UPN。很难理解为何会有组织会故意允许用户修改如此重要的属性。

## 安全风险与应对措施

允许用户修改UPN带来了诸多安全风险。由于Entra ID与Exchange Online之间的双写同步，更改UPN会自动更新Exchange Online中的主SMTP地址。旧的主SMTP地址将保留为代理地址，以确保电子邮件传递的连续性。

![](https://image.3001.net/images/20250126/1737860650_6795a62ac7963e6f43097.jpg!small)更新用户主体名称和照片后的帐户属性

用户可以暂时更改UPN以冒充他人（如CEO@domain.com），获取该邮箱地址的访问权限，然后再恢复为原来的UPN。如果管理员没有积极监控审核日志，这种更改可能会被忽视。

此外，撤销UPN更改并不会自动删除在此过程中创建的额外邮件代理地址，如果管理员未明确处理，这可能会导致进一步的复杂情况或滥用。

对此功能感到担忧的组织可以采取措施限制用户访问：

* **限制对 Entra 管理中心的访问：**管理员可以配置设置以阻止非管理用户访问 Entra 管理中心。虽然这并不能完全防止具有低级角色（例如报告阅读者）的用户进行更改，但可以减少随意访问。
* **保护 Microsoft Graph PowerShell SDK：**默认情况下，任何用户都可以使用 Connect-MgGraph cmdlet 连接到 Microsoft Graph PowerShell SDK 。管理员可以通过限制相关企业应用程序的设置来保护此功能。如果没有适当的权限，尝试连接的用户将遇到 AADSTS50105 错误。

微软启用这一功能的原因尚不清楚。虽然微软通常会基于特定用例实施更改，但尚未提供允许无特权用户修改其UPN等基本属性的明确理由。这让IT管理员感到困惑，并担心潜在的滥用行为。

## 微软的行动与回应

截至2025年1月24日14:00 UTC，微软已采取措施阻止用户更新自己UPN。当用户尝试进行此类操作时，Entra管理中心现在会显示一条通知，限制此功能。

在微软对此变更的更多信息公布之前，建议组织实施控制措施以降低风险。阻止用户访问 Entra 管理中心和 Microsoft Graph PowerShell SDK 是维护安全的明智之举。

**参考链接：**

> <https://cybersecuritynews.com/microsoft-accidently-allow-unprivileged-users-to-change-their-user-principal-names-in-entra-id/>

# 资讯

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

安全风险与应对措施

微软的行动与回应

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