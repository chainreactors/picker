---
title: 起亚经销商网站曝出严重漏洞！黑客可在30秒内远程操控数百万辆汽车
url: https://www.freebuf.com/news/411878.html
source: FreeBuf网络安全行业门户
date: 2024-09-28
fetch_date: 2025-10-06T18:27:09.747753
---

# 起亚经销商网站曝出严重漏洞！黑客可在30秒内远程操控数百万辆汽车

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

起亚经销商网站曝出严重漏洞！黑客可在30秒内远程操控数百万辆汽车

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

起亚经销商网站曝出严重漏洞！黑客可在30秒内远程操控数百万辆汽车

2024-09-27 10:06:28

所属地 上海

![1727402638_66f6128e48cf71f12b038.png!small](https://image.3001.net/images/20240927/1727402638_66f6128e48cf71f12b038.png!small)

近日，有安全研究人员发现起亚汽车经销商门户网站存在一个关键漏洞，黑客只需使用目标车辆的车牌，就能定位并窃取数百万辆 2013 年后生产的起亚汽车。

大约在2022 年，安全研究员和漏洞赏金猎人萨姆-库里等人发现了影响十多家汽车公司的其他关键漏洞，这些漏洞可以让犯罪分子远程定位、禁用启动器、解锁和启动法拉利、宝马、劳斯莱斯、保时捷和其他汽车制造商生产的 1500 多万辆汽车。

今天，库里透露称起亚门户网站漏洞最早是在今年6月被发现的，黑客利用该漏洞能在 30 秒内控制任何配备远程硬件的起亚汽车，无论其是否有激活的起亚互联订阅。

这些漏洞还暴露了车主的敏感个人信息，包括姓名、电话号码、电子邮件地址和实际地址，并可能使攻击者在车主不知情的情况下将自己添加为目标车辆的第二用户。

为了进一步证明这一问题，研究小组制作了一个工具，展示攻击者如何输入汽车牌照，并在 30 秒内远程锁定或解锁汽车、启动或停止汽车、按喇叭或定位车辆。

研究人员在起亚的 kiaconnect.kdealer.com 经销商门户网站上注册了一个经销商账户，以获取这些信息。

通过身份验证后，他们生成了一个有效的访问令牌，该令牌允许他们访问后端经销商 API，从而获得车主的重要详细信息和对汽车遥控器的完全访问权限。

他们发现，攻击者可以利用后台经销商 API完成以下操作，包括：

* 生成经销商令牌并从 HTTP 响应中获取该令牌
* 访问受害者的电子邮件地址和电话号码
* 使用泄露的信息修改车主的访问权限
* 将攻击者控制的电子邮件添加到受害者的车辆上，从而实现远程命令

HTTP 响应包含车主的姓名、电话号码和电子邮件地址。库里表示：我们能够使用正常的应用程序凭证和修改后的通道头验证进入经销商门户。

从那里，攻击者可以通过 API 输入车辆的 VIN（车辆识别码），并在车主不知情的情况下远程跟踪、解锁、启动或鸣笛。

起亚门户网站的漏洞允许在未经授权的情况下隐秘地访问车辆，因为正如库里解释的那样，从受害者的角度来看，他们的车辆被访问后没有任何通知，他们的访问权限也没有被修改。

库里补充道：这些漏洞后来都得到了修复，这个工具也从未发布过，起亚团队已经证实这从未被恶意利用过。

> 参考来源：[Kia dealer portal flaw could let attackers hack millions of cars (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/kia-dealer-portal-flaw-could-let-attackers-hack-millions-of-cars/)

# 黑客攻击 # 汽车安全 # 网站漏洞

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