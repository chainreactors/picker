---
title: 因办公应用程序导致大规模数据泄露！涉及戴尔、AT&T、大通银行等900家公司
url: https://www.freebuf.com/news/407784.html
source: FreeBuf网络安全行业门户
date: 2024-08-06
fetch_date: 2025-10-06T18:04:40.573071
---

# 因办公应用程序导致大规模数据泄露！涉及戴尔、AT&T、大通银行等900家公司

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

因办公应用程序导致大规模数据泄露！涉及戴尔、AT&T、大通银行等900家公司

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

因办公应用程序导致大规模数据泄露！涉及戴尔、AT&T、大通银行等900家公司

2024-08-05 10:05:50

所属地 上海

![1722823423_66b032ffbce25298fee14.png!small](https://image.3001.net/images/20240805/1722823423_66b032ffbce25298fee14.png!small)

近日，有研究人员发现了一次大规模的数据泄漏事件，共涉及到大约 900 家公司和组织，其中包括戴尔、Verizon、AT&T、能源部、康卡斯特和大通银行等。

今年 3 月 25 日，Cybernews 研究小组发现了一个可公开访问的网络目录，该目录属于马里兰州的 Simpli 公司（前身为 Charm City Concierge）。

该公司的应用程序允许租用办公空间的公司的员工查看位于同一栋大楼内的商店。它列出了可用的便利设施、工作场所福利和折扣，并使用户能够订购各种服务和产品。

这个开放的网络目录存储了 2024 年 1 月对公司网站和 Simpli 应用程序数据库的备份数据。据悉，此次泄露的应用程序的备份暴露了 10000 名员工的电子邮件地址和来自大约 900 家公司的哈希密码。

![1722823451_66b0331be7ed9be3b8a48.png!small](https://image.3001.net/images/20240805/1722823451_66b0331be7ed9be3b8a48.png!small)

包含网站和数据库备份的网络目录被曝光

受影响的公司包括：

* Capital One
* 海军分析中心
* 美国律师协会
* 微策略
* 剑桥联营公司
* 戴尔
* 威瑞森
* 康卡斯特
* 西部交通
* WeWork
* 信托银行
* 美国电话电报公司
* 国家残疾人委员会
* 能源部
* 大通银行

![1722823479_66b033373fe965a046c8c.png!small](https://image.3001.net/images/20240805/1722823479_66b033373fe965a046c8c.png!small)

带备注的订单信息

由于大多数员工都使用公司电子邮件地址注册了 Simpli 服务，因此这构成了重大风险。威胁攻击者有可能通过使用凭据填充攻击，将目标锁定在员工可以访问的更敏感的公司系统上。

Cybernews 的信息安全研究员 Aras Nazarovas 说：虽然员工凭证是以相对安全的格式存储的，但密码仍有可能被破解，尤其是弱密码。

如果员工在多个账户中使用相同的密码，被破解的密码就可以用来登录其他更敏感、与工作相关的终端。

![1722823500_66b0334ca24dba032f3fe.png!small](https://image.3001.net/images/20240805/1722823500_66b0334ca24dba032f3fe.png!small)

建筑物及其租户清单

此次泄露的数据库还曝光了通过该应用程序发出的指令，其中一些指令包含可能涉及敏感业务信息的备注。这些笔记包括来自不同公司的个人之间的会议细节和会议目的。

在开放目录中发现的文件表明，这些信息可能是在该公司将其系统从 Drupal 7 迁移到 Drupal 9 时泄露的。目前 Simpli 公司暂未对此做出回应。

![1722823523_66b0336352b8a005ebd89.png!small](https://image.3001.net/images/20240805/1722823523_66b0336352b8a005ebd89.png!small)

用户凭证

## 供应链攻击风险

此类泄密事件凸显了使用第三方服务的固有风险，这些服务可能会带来供应链攻击的风险。在这种网络攻击中，威胁者往往会寻找供应网络中的薄弱环节，而不是直接针对一家公司。

攻击者攻破一个供应商，就有可能影响到使用该供应商产品或服务的公司。从第三方供应商处提取的凭据对于已经瞄准一家公司的恶意行为者来说可能非常有用。

零售商 Target 就曾遭受过此类攻击。2013 年，恶意行为者入侵了 Target 的制冷、供暖和空调分包商 Fazio Mechanical，并将恶意软件传播到 Target 的大部分销售点设备。据报道，恶意软件当时共收集到了大约 4000 万张借记卡和信用卡的财务信息。

因此，提供第三方服务的公司和组织应该对网络安全问题格外保持警惕，因为这些公司极有可能会成为攻击者的目标。

> 参考来源：[Employees at Dell, AT&T, Verizon, Capital One, and other companies exposed via popular office app | Cybernews](https://cybernews.com/security/simpli-app-data-leak/)

# 数据泄露

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

供应链攻击风险

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