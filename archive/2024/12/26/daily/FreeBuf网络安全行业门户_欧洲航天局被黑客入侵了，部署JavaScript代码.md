---
title: 欧洲航天局被黑客入侵了，部署JavaScript代码
url: https://www.freebuf.com/news/418474.html
source: FreeBuf网络安全行业门户
date: 2024-12-26
fetch_date: 2025-10-06T19:38:38.993297
---

# 欧洲航天局被黑客入侵了，部署JavaScript代码

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

欧洲航天局被黑客入侵了，部署JavaScript代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

欧洲航天局被黑客入侵了，部署JavaScript代码

2024-12-25 11:06:38

所属地 上海

欧洲航天局（ESA）的官方网络商店遭遇黑客入侵，加载用于生成虚假Stripe支付页面的JavaScript代码。

欧洲航天局每年的预算超过100亿欧元，其主要任务是通过培训宇航员以及建造火箭和卫星来探索宇宙奥秘，进而拓展太空活动的边界。目前，获准销售的ESA商品网络商店已无法使用，页面显示的信息是“暂时失去轨道”。

就在昨天，这段恶意脚本出现在欧洲航天局的网站上，并开始收集客户信息，其中包含在购买流程最后阶段提供的支付卡数据。电子商务安全公司Sansec于昨日察觉到这段恶意脚本，并发出警告称，这家商店看起来是与ESA系统集成的，这可能会给该机构的员工带来风险。

![](https://image.3001.net/images/20241225/1735095918_676b766edf9890ae7236f.png!small)

Sansec警告ESA商店已被入侵

Sansec发现，用于提取信息的域名与销售ESA商品的合法商店所使用的名称相同，只是顶级域（TLD）有所不同。欧洲机构的官方商店使用的是.com的顶级域名“esaspaceshop”，而黑客使用相同名称但不同顶级域（TLD）的.pics（即esaspaceshop[.]pics），这一点在ESA商店的源代码中能够看到：

![](https://image.3001.net/images/20241225/1735095936_676b768054ff15b08a018.png!small)

ESA网络商店中注入的恶意JavaScript

该脚本包含来自Stripe SDK的混淆HTML代码，当客户试图完成购买操作时，就会加载一个虚假的Stripe支付页面。值得注意的是，这个虚假的Stripe页面看上去并不可疑，特别是当该页面由ESA的官方网络商店提供。

![](https://image.3001.net/images/20241225/1735095970_676b76a205d0cc2b37c64.png!small)

ESA的网络商店加载虚假的Stripe支付页面

网络应用程序安全公司Source Defense Research证实了Sansec的发现，并捕获到了在ESA官方网络商店中加载的虚假Stripe支付页面。目前ESA官网网络商店已经解决该问题，不再出现虚假的Stripe支付页面，但在网站的源代码中仍然能够看到恶意脚本。

ESA表示，这家商店并非托管在其基础设施上，也不管理其上的数据，所以不用担心会影响ESA相关工作。通过简单的WHOIS查询可确认，这家商店的域名注册信息与ESA的官方域名（esa.int）分离，且注册人的联系方式被隐私保护掩盖。

ESA在线商店的攻击事件是一个典型案例，反映出品牌授权模式在网络安全管理中的潜在风险。特别是当授权的外部平台未能执行严格的安全审查时，品牌自身的声誉和用户的安全都会受到威胁。

参考来源：<https://www.bleepingcomputer.com/news/security/european-space-agencys-official-store-hacked-to-steal-payment-cards/>

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