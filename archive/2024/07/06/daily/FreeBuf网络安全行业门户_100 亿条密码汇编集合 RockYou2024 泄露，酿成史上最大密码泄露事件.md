---
title: 100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件
url: https://www.freebuf.com/news/405256.html
source: FreeBuf网络安全行业门户
date: 2024-07-06
fetch_date: 2025-10-06T17:43:32.754689
---

# 100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件

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

100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件

2024-07-05 10:07:57

所属地 上海

![1720145294_6687558e0aedb10076249.png!small](https://image.3001.net/images/20240705/1720145294_6687558e0aedb10076249.png!small)

近日，Cybernews 的研究人员发现了一个包含 9948575739 个明文密码的名为rockyou2024.txt 的数据文档被泄露。根据推测，这可能是有史以来最大的密码汇编集合泄露事件。

虽然上传该文档的用户是在 2024 年 5 月底注册的，但他此前曾分享过西蒙斯律师事务所的员工数据库、在线赌场 AskGamblers 的线索以及伯灵顿郡罗文学院的学生申请表。

研究小组将 RockYou2024 泄露事件中包含的密码与 Cybernews 的泄露密码检查器中的数据进行了交叉比对，发现这些密码均来自此前发生的数据泄露事件。

RockYou2024密码汇编集合里包含世界各地个人使用的真实密码。研究人员认为，黑客将数量如此庞大的密码泄露出去，大大增加了凭证填充攻击的风险。

凭据填充攻击会对用户和企业造成严重损害。例如，最近针对桑坦德银行、Ticketmaster、Advance Auto Parts、QuoteWizard 等公司的攻击事件就是针对受害者的云服务提供商 Snowflake 的凭据填充攻击的直接结果。

此外，黑客还可以利用 RockYou2024 密码汇编进行暴力破解攻击，并在未经授权的情况下访问使用数据集中所含密码的个人所使用的各种在线账户。

![RockYou2024 post](https://image.3001.net/images/20200701/1593550745.png!small)

黑客论坛上宣布泄密的帖子，图片来源：Cybernews

## RockYou密码汇编集合数据并非首次泄露

2021年，Cybernews 就曾发表过一篇关于 RockYou2021 密码汇编的报道。

当时有用户在某黑客论坛上发布了一个100GB 的txt文件遭遇泄露，这也是当时最大的密码汇编集合，共包含 84 亿个纯文本密码。

据帖子作者称，泄露的所有密码长度都是6-20个字符，非ascii字符和空格都被删除。该作者还声称文件中包含820亿条密码。然而，在Cybernes测试后发现，实际的数字仅为宣称的十分之一——84亿条。

根据该团队对 RockYou2024 的分析，攻击者通过在互联网上搜索数据泄露信息来开发该数据集，从 2021 年到 2024 年又增加了 15 亿个密码，数据集增加了 15%。

RockYou2021 汇编是 2009 年数据泄露事件的延伸事件，其中包括数千万个社交媒体账户的用户密码。然而，从那时起，汇编的内容急剧增加。最新的 RockYou 版本包含了二十多年来从 4000 多个数据库中收集的信息。

Cybernews 团队认为，攻击者可以利用高达 100 亿的 RockYou2024 数据库来攻击任何未受暴力破解攻击保护的系统，包括从在线和离线服务到面向互联网的摄像头、工业硬件等等。

此外，RockYou2024 与黑客论坛和市场上的其他泄露数据库，例如，包含用户电子邮件地址和其他凭证的数据库相结合，可能导致一连串的数据泄露、金融欺诈和身份盗窃事件发生。

![RockYou2024 leak](https://image.3001.net/images/20200701/1593550745.png!small)

攻击者的用户资料，图片来源：Cybernews

## 应对措施

虽然目前并没有很好的方法来保护密码泄露的用户，但Cybernews 研究团队建议受影响的个人和组织应采取缓解策略：

Cybernews 将把来自 RockYou2024 的数据纳入泄露密码检查器，用户可通过最新的创纪录泄露密码汇编检查自己的凭证是否被泄露。

此次RockYou2024泄露事件是2024 年第二个破纪录的密码汇编泄露事件。

今年早些时候，Cybernews 发现 MOAB泄露了 12 TB 的信息，包括约 260 亿条记录。

> 参考来源：[RockYou2024: 10 billion passwords leaked in the largest compilation of all time | Cybernews](https://cybernews.com/security/rockyou2024-largest-password-compilation-leak/)

# 数据泄露 # 密码泄露

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

RockYou密码汇编集合数据并非首次泄露

应对措施

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