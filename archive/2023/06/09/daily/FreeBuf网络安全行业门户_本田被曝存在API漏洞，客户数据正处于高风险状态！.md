---
title: 本田被曝存在API漏洞，客户数据正处于高风险状态！
url: https://www.freebuf.com/news/368853.html
source: FreeBuf网络安全行业门户
date: 2023-06-09
fetch_date: 2025-10-04T11:47:40.967186
---

# 本田被曝存在API漏洞，客户数据正处于高风险状态！

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

本田被曝存在API漏洞，客户数据正处于高风险状态！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

本田被曝存在API漏洞，客户数据正处于高风险状态！

2023-06-08 11:01:50

所属地 上海

![1686193861_648146c5d8073c3cbc018.png!small?1686193863655](https://image.3001.net/images/20230608/1686193861_648146c5d8073c3cbc018.png!small?1686193863655)

近日，本田被曝存在API漏洞，客户数据正处于高风险状态。由于利用API漏洞可以重置任何帐户的密码，所以本田的电力设备、船舶、草坪和花园电子商务平台等都极易遭到外部人员的入侵。

几个月前，一位化名Eaton Works的安全研究人员发现了本田系统的安全漏洞，他利用该漏洞入侵了本田的供应商门户网站。

Eaton Works利用了一个密码重置API重置了那些本田内部有价值的账户的密码，然后在公司的网络上进行了不受限制的管理级数据访问。

研究人员称：访问控制的破坏或缺失使得访问平台上的所有数据成为可能，即使是以测试帐户登录也是如此。

以下这些信息不仅暴露给了安全研究人员，还极可能暴露给了那些利用相同漏洞入侵的威胁行为者：

* 从2016年8月到2023年3月，所有经销商的21393个客户订单，其中包括客户姓名、地址、电话号码和订购的商品
* 1570个经销商网站(其中1091个是活跃的)，所有站点均可被修改
* 3588个经销商用户/账户(包括姓名、电子邮件地址)，任意用户密码均可被修改
* 1090封经销商电子邮件(包括姓名)
* 11034封客户邮件(包括名字和姓氏)
* Stripe、PayPal和Authorize.net提供的私钥。
* 内部财务报告

![1686193366_648144d66fc9736f4c37d.png!small](https://image.3001.net/images/20230608/1686193366_648144d66fc9736f4c37d.png!small)

曝光的客户邮件(eaton-works.com)

上述数据可能被用于发起网络钓鱼活动、社会工程攻击，或直接被人在黑客论坛和暗网市场上出售。此外，通过访问经销商网站，攻击者还可以植入信用卡刷卡程序或其他恶意JavaScript代码片段。

![1686193346_648144c28984e3f75417c.png!small](https://image.3001.net/images/20230608/1686193346_648144c28984e3f75417c.png!small)

能够编辑页面内容(eaton-works.com)

## 访问管理面板

EatonWorks解释说，API漏洞存在于本田的电子商务平台，该平台将“powerdealer.honda.com”子域名分配给注册经销商/经销商。

研究人员发现，本田有一个网站的电力设备技术快车(PETE)密码重置API在处理重置请求时不需要令牌或之前的密码，只需要有效的电子邮件即可。

虽然在电子商务子域登录门户上不存在此漏洞，但通过PETE站点切换的凭据仍然可以对它们起作用，因此任何人都可以通过这种简单的攻击访问内部经销商数据。

![1686193755_6481465bc3d273202ec52.png!small?1686193757148](https://image.3001.net/images/20230608/1686193755_6481465bc3d273202ec52.png!small?1686193757148)

密码重置API请求发送到PETE (eaton-works.com)

唯一缺失的部分是拥有一个属于经销商的有效电子邮件地址，研究人员从YouTube视频中获取了该电子邮件地址，该视频展示了使用测试帐户的经销商面板。

![1686193917_648146fdd7edd233092b2.png!small?1686193919713](https://image.3001.net/images/20230608/1686193917_648146fdd7edd233092b2.png!small?1686193919713)

YouTube视频曝光测试账号邮箱

除了测试账户，下一步就是从真正的交易商那里获取信息。但最好是在不中断操作的情况进行，这样就不必重新设置数百个帐户的密码。

研究人员发现的解决方案是利用第二个漏洞，即平台中用户id的顺序分配和缺乏访问保护。

这使得任意访问所有本田经销商的数据面板成为可能，具体方法就是将用户ID增加1，直到没有任何其他结果。

研究人员称：只要增加ID就可以访问每个经销商的数据。底层JavaScript代码接受该ID，并在API调用中使用它来获取数据并在页面上显示。而值得庆幸的是，这个操作能让重新设置密码变得没什么实际效用。

![1686194153_648147e9ee3d932ecf813.png!small?1686194155496](https://image.3001.net/images/20230608/1686194153_648147e9ee3d932ecf813.png!small?1686194155496)

增加用户ID号码以访问所有经销商面板(eaton-works.com)

值得注意的是，本田的注册经销商可能会利用上述漏洞访问其他经销商的面板，进而访问他们的订单、客户详细信息等。最后一步就是访问本田的管理面板，因为这是该公司电子商务平台的中央控制点。

研究人员通过修改HTTP响应假扮管理员访问该面板，从而实现无限制地访问本田经销商网站平台。

![1686194314_6481488ae537576bdeb33.png!small?1686194316017](https://image.3001.net/images/20230608/1686194314_6481488ae537576bdeb33.png!small?1686194316017)

本田经销商网站管理面板(eaton-works.com)

有关上述这个漏洞的相关问题是在今年3月16日报告给了本田，到今年4月3日，所有问题都已得到妥善解决。

> 参考来源：[Honda API flaws exposed customer data, dealer panels, internal docs](https://www.bleepingcomputer.com/news/security/honda-api-flaws-exposed-customer-data-dealer-panels-internal-docs/)

# 数据泄露 # 漏洞利用 # 系统漏洞

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

访问管理面板

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