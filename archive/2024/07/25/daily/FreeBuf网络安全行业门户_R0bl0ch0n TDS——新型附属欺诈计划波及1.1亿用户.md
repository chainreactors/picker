---
title: R0bl0ch0n TDS——新型附属欺诈计划波及1.1亿用户
url: https://www.freebuf.com/news/406861.html
source: FreeBuf网络安全行业门户
date: 2024-07-25
fetch_date: 2025-10-06T17:43:24.061155
---

# R0bl0ch0n TDS——新型附属欺诈计划波及1.1亿用户

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

R0bl0ch0n TDS——新型附属欺诈计划波及1.1亿用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

R0bl0ch0n TDS——新型附属欺诈计划波及1.1亿用户

2024-07-24 11:29:41

所属地 上海

近日，世界观察组织的专家团队揭露了一种新型流量分配系统（TDS），该系统与附属营销紧密相关，并在多起欺诈计划中被积极利用。由于其URL重定向中独特的“0/0/0”序列，这一系统被命名为R0bl0ch0n TDS，已经对全球约1.1亿互联网用户造成了影响。

![](https://image.3001.net/images/20240724/1721791731_66a074f341cf1287f5d07.png!small)附属营销本是一种正当的商品与服务推广方式，但在本次事件中，它被用作散播欺诈广告的手段。研究人员发现，有数百个小规模的附属网络专门推广可疑的优惠，这些优惠往往与知名的诈骗计划相关。

R0bl0ch0n TDS是一个包含众多域名和专用服务器的复杂架构，由Cloudflare提供安全保护。尽管操纵者在他们的计划中加入了一些合法功能，例如退订和反馈机制，但他们也采取了重要措施来隐藏这些操作背后的真正组织。

技术分析显示，R0bl0ch0n TDS中嵌入电子邮件的URL遵循固定模式（<domain>/bb/[0-9]{18}），并通过多个自动重定向将用户引导至假冒商店或调查页面。值得注意的是，由于需要用户参与来绕过假CAPTCHA，这些URL无法被自动化系统准确分析。

专家们还发现，托管假冒调查的域名会主动与第三方网站交换用户数据。例如，域名facileparking.sbs向event.trk-adulvion.com传输信息。这个域名网络从2021年夏天开始运营，在亚马逊网络服务（AWS）服务器上拥有300多个专用IP地址。

DomainTools的数据显示，自2021年起，event子域的A型DNS请求总数约为1.1亿。考虑到每个用户由于指纹识别机制只记录一次DNS请求，这个数字准确地反映了这些欺诈计划所针对的总人数。

研究人员识别了通过R0bl0ch0n TDS分发的两类主要欺诈性优惠：

### 1. 抽奖活动

提供诱人的中奖信息，要求用户完成在线调查后支付小额运费。实际上，这会导致用户注册定期支付的订阅服务（每两周20至45欧元）。美国联邦贸易委员会报告称，投诉导致的损失总额超过3亿美元，平均每人损失约900美元。世界观察组织的专家认为，考虑到每天发送的广告量，实际损失可能更高。

### 2.家居改善优惠

推广价格过高的服务，如檐槽过滤器、太阳能电池板、热泵或老年人使用的步入式淋浴。这些计划通常通过电子邮件传播或利用搜索引擎优化（SEO）进行推广。每次用户填写联系表后，附属公司可获得佣金，随后“销售人员”会联系潜在客户。而且，卖家经常故意夸大客户可能有资格获得的政府补贴金额。

R0bl0ch0n TDS的URL通过多种方法进行初始分发：

* 使用带有URL片段数据的随机AWS子域，这些数据可能与附属程序参数相关联。
* 使用匹配特定模式的随机Azure子域，URL片段中的数据同样传递给R0bl0ch0n TDS。
* 使用URL缩短服务。

专家指出，利用AWS或Azure等合法基础设施服务或URL缩短器，附属公司能够轻松地修改和部署新的基础设施，从而绕过谷歌安全浏览或反垃圾邮件过滤器中的检测系统和对策。

参考来源：
https://securityonline.info/r0bl0ch0n-tds-new-affiliate-fraud-scheme-impacts-110-million-users/

# 网络欺诈 # url # 域名欺诈

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