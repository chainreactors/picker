---
title: 黑客利用 Facebook 漏洞，发起网络钓鱼攻击
url: https://www.freebuf.com/news/373761.html
source: FreeBuf网络安全行业门户
date: 2023-08-04
fetch_date: 2025-10-04T12:03:13.073240
---

# 黑客利用 Facebook 漏洞，发起网络钓鱼攻击

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

黑客利用 Facebook 漏洞，发起网络钓鱼攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客利用 Facebook 漏洞，发起网络钓鱼攻击

2023-08-03 14:50:34

所属地 上海

Bleeping Computer 网站披露，网络攻击者利用 Salesforce 电子邮件服务和 SMTP 服务器中的漏洞，针对一些特定的 Facebook 账户发起复杂的网络钓鱼活动。![1691045468_64cb4e5cde3c17ed0b116.png!small](https://image.3001.net/images/20230803/1691045468_64cb4e5cde3c17ed0b116.png!small)

据悉，网络攻击者利用 Salesforce 等具有良好信誉的电子邮件网关分发网络钓鱼电子邮件，此举有利于其规避安全电子邮件网关和过滤规则，确保恶意电子邮件能够到达目标收件箱。

前段时间，Guardio Labs 的分析师 Oleg Zaytsev 和 Nati Tal 发现漏洞问题，随后向 Salesforce 报告并帮助进行了漏洞修复，然而 Facebook 游戏平台上的漏洞问题仍悬而未决，Meta 的工程师们仍在努力寻找现有缓解措施不能有效阻止攻击的原因。

## ****PhishForce**** ****漏洞********在攻击********被滥用****

Salesforce CRM 允许客户使用自定义域名作为自己的“品牌”发送电子邮件，但必须通过平台验证这些域名，这样就可以阻止客户通过 Salesforce 发送其无权冒充的其它品牌的电子邮件。然而不幸的是，Guardio Labs 称网络攻击者找到一种利用 Salesforce "Email-to-Case "功能的方法。

具体来说就是攻击者设置一个新的 “Email-to-Case ”流程，以获得对 Salesforce 生成的电子邮件地址的控制权，之后在 “salesforce.com ”域上创建一个新的入站电子邮件地址。![1691045506_64cb4e82d52dbd8cf82e8.png!small?1691045508020](https://image.3001.net/images/20230803/1691045506_64cb4e82d52dbd8cf82e8.png!small?1691045508020)

生成的 Salesforce 地址（Guardio Labs）

接下来，网络攻击者将该地址设置为 “组织范围内的电子邮件地址”，Salesforce 的 Mass Mailer Gateway将其用于出站电子邮件，并最终通过验证过程来确认该域的所有权。![1691045527_64cb4e979f89b517f5c98.png!small?1691045528997](https://image.3001.net/images/20230803/1691045527_64cb4e979f89b517f5c98.png!small?1691045528997)

点击验证链接确认所有权（Guardio Labs）

整个过程允许网络攻击者使用自有的 Salesforce 电子邮件地址向任何人发送信息，从而绕过 Salesforce 的验证保护以及任何其它电子邮件过滤器和反钓鱼系统。

事实上，这就是近期 Guardio Labs 在野外观察到的情况，据称来自 “Meta Platforms ”的网络钓鱼电子邮件使用了 “case.salesforce.com ”域名。![1691045546_64cb4eaab3ae2b63f0db3.png!small?1691045547936](https://image.3001.net/images/20230803/1691045546_64cb4eaab3ae2b63f0db3.png!small?1691045547936)

从真实攻击中提取的网络钓鱼电子邮件样本（Guardio Labs）

一旦受害者点击了嵌入式按钮后，便会进入一个作为 Facebook 游戏平台（"apps.facebook.com"）一部分托管和显示的网络钓鱼页面，这为攻击增加了更多合法性和说服力，使电子邮件收件人更难意识到欺诈行为。![1691045560_64cb4eb8dcae46d1ec977.png!small?1691045562521](https://image.3001.net/images/20230803/1691045560_64cb4eb8dcae46d1ec977.png!small?1691045562521)

托管在 Facebook 游戏平台上的网络钓鱼页面（Guardio Labs）

Guardio 指出此次网络攻击活动中使用的网络钓鱼工具包的目的是窃取 Facebook 帐户凭据，甚至还具有绕过双因素身份验证机制的特点。![1691045638_64cb4f068eb2362f4501f.png!small?1691045640089](https://image.3001.net/images/20230803/1691045638_64cb4f068eb2362f4501f.png!small?1691045640089)

观察到的攻击链（Guardio Labs）

## Meta 正在积极调查网络攻击事件

2023 年 6 月 28 日，Guardio Labs 发现漏洞问题并报告给 Facebook ，一个月后，Guardio Labs 重现了该漏洞并解决了问题。对于“apps.facebook.com”的滥用，Guardio Labs 指出攻击者应该不可能创建用作登录页的游戏拉票。接到 Guardio Labs 的报告后，Meta 删除了违规页面，其工程师仍在调查现有保护措施未能阻止攻击的原因。

随着网络钓鱼行为者不断探索合法服务提供商的每一个潜在滥用机会，新的安全漏洞不断威胁着用户，使其面临严重风险。因此用户不能仅仅依赖电子邮件保护解决方案，还必须仔细检查收件箱中的每封邮件，查找不一致之处，并反复检查邮件中的所有声明。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/hackers-exploited-salesforce-zero-day-in-facebook-phishing-attack/#google\_vignette

# 漏洞分析

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

PhishForce 漏洞在攻击被滥用

Meta 正在积极调查网络攻击事件

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