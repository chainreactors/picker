---
title: 注意！新的QBot银行木马通过电子邮件传播恶意软件
url: https://www.freebuf.com/news/363877.html
source: FreeBuf网络安全行业门户
date: 2023-04-19
fetch_date: 2025-10-04T11:35:28.471149
---

# 注意！新的QBot银行木马通过电子邮件传播恶意软件

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

注意！新的QBot银行木马通过电子邮件传播恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

注意！新的QBot银行木马通过电子邮件传播恶意软件

2023-04-18 11:34:44

所属地 上海

![](https://image.3001.net/images/20230418/1681785330_643e01f2167368ba77d60.png!small)

近日，卡巴斯基的最新发现显示，一个新的QBot恶意软件正在利用被劫持的商业电子邮件，分发恶意软件。

最开始发现该恶意活动是在2023年4月4日，主要针对德国、阿根廷、意大利、阿尔及利亚、西班牙、美国、俄罗斯、法国、英国和摩洛哥的用户。

QBot（又名Qakbot或Pinkslipbot）是一个银行木马，从2007年开始活跃。除了从网络浏览器中窃取密码和cookies，它还作为后门注入有效载荷，如Cobalt Strike或勒索软件。

该恶意软件通过网络钓鱼活动传播，并不断更新，通过加入反虚拟机、反调试和反沙盒技术以逃避检测。正因为这样，它也成为2023年3月最流行的恶意软件。

卡巴斯基研究人员解释，早期，QBot的传播方式是通过受感染的网站和盗版软件传播的。现在则是通过银行木马已经驻留在其计算机上的恶意软件，社交工程和垃圾邮件传递给潜在的受害者。

电子邮件网络钓鱼攻击并不新鲜。其目的是诱使受害者打开恶意链接或恶意附件，一般情况下，这些文件被伪装成一个微软Office 365或微软Azure警报的封闭式PDF文件。

打开该文件后，就会从一个受感染的网站上检索到一个存档文件，该文件又包含了一个混淆的Windows脚本文件（.WSF）。该脚本包含一个PowerShell脚本，从远程服务器下载恶意的DLL。下载的DLL就是QBot恶意软件。

调查结果发布之际，Elastic Security Labs还发现了一个多阶段的社会工程活动，该活动使用武器化的Microsoft Word文档通过自定义方式分发Agent Tesla和XWorm。基于 NET 的加载程序。

> 参考链接：https://thehackernews.com/2023/04/new-qbot-banking-trojan-campaign.html

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