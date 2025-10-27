---
title: 全球多地Zimbra电子邮件账户遭到钓鱼邮件攻击
url: https://www.freebuf.com/news/375349.html
source: FreeBuf网络安全行业门户
date: 2023-08-19
fetch_date: 2025-10-04T12:00:26.010908
---

# 全球多地Zimbra电子邮件账户遭到钓鱼邮件攻击

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

全球多地Zimbra电子邮件账户遭到钓鱼邮件攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

全球多地Zimbra电子邮件账户遭到钓鱼邮件攻击

2023-08-18 10:13:32

所属地 上海

根据 ESET 的一份报告，至少从 2023 年 4 月起，网络钓鱼活动就一直在试图窃取全球多地的 Zimbra Collaboration 电子邮件凭证。

![](https://image.3001.net/images/20230818/1692324847_64ded3ef6a8d72eb48130.png!small)

根据 ESET 研究人员的说法，攻击始于一封假装来自组织管理员的网络钓鱼电子邮件，通知用户即将进行电子邮件服务器更新，会导致帐户暂时停用，要求用户打开附加的 HTML 文件，以了解有关服务器升级的更多信息，并查看有关避免停用帐户的说明。

![](https://image.3001.net/images/20230818/1692324895_64ded41fc06014ed31ee5.png!small)钓鱼邮件内容示例

打开 HTML 附件时，将显示一个虚假的 Zimbra 登录页面，为了更加真实，该页面复刻了包含目标公司的徽标和品牌。一旦在钓鱼表单中输入了帐户密码，就会通过 HTTPS POST 请求发送到攻击者的服务器。

![](https://image.3001.net/images/20230818/1692324936_64ded4485671b29f9b5b0.png!small)Zimbra 钓鱼登录页面

![](https://image.3001.net/images/20230818/1692324991_64ded47fa36b7ae76699e.png!small)窃取用户输入的密码

ESET 报告称，在某些情况下，攻击者会使用窃取到的管理员帐户创建新邮箱向企业组织的其他成员发送网络钓鱼电子邮件。分析师强调，尽管该活动缺乏复杂性，但其传播范围很广，Zimbra Collaboration 的用户需要意识到这一威胁。

由于此次网络钓鱼电子邮件被发送到世界各地的企业组织，而不是特定针对某些组织或部门，其背后的攻击者身份仍然未知。

通常，攻击者会针对 Zimbra Collaboration 电子邮件服务器进行网络间谍活动，以收集内部通信或将其用作传播到目标组织网络的初始突破点。

今年年初，Proofpoint 透露，俄罗斯“ Winter Vivern ”黑客组织利用 Zimbra Collaboration 缺陷 (CVE-2022-27926) 访问了北约组织、政府、外交官和军事人员的网络邮件门户；去年，Volexity 报告称，名为“ TEMP\_Heretic ”的攻击者利用 Zimbra Collaboration 产品中的零日漏洞 (CVE-2022-23682) 访问邮箱并执行了横向网络钓鱼攻击。

ESET 总结称，Zimbra Collaboration 在IT 预算较低的企业组织中广受欢迎，这也导致它对攻击者而言是一个颇具吸引力的目标。

> 参考来源：[Phishing campaign steals accounts for Zimbra email servers worlwide](https://www.bleepingcomputer.com/news/security/phishing-campaign-steals-accounts-for-zimbra-email-servers-worlwide/)

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