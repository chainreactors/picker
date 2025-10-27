---
title: 攻击者冒充VPN提供商对员工发起攻击，超130家公司已“中招”
url: https://www.freebuf.com/news/409821.html
source: FreeBuf网络安全行业门户
date: 2024-08-31
fetch_date: 2025-10-06T18:04:31.948556
---

# 攻击者冒充VPN提供商对员工发起攻击，超130家公司已“中招”

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

攻击者冒充VPN提供商对员工发起攻击，超130家公司已“中招”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

攻击者冒充VPN提供商对员工发起攻击，超130家公司已“中招”

2024-08-30 09:51:44

所属地 上海

![](https://image.3001.net/images/20240830/1724984126_66d12b3e9c5bd466f50f2.png!small)

近日，GuidePoint Research和Intelligence Team（GRIT）发现了一个针对英语使用者的持续钓鱼活动，该活动已经针对美国超过130家公司和组织。

研究人员指出，自2024年6月26日以来，这个威胁行为者注册了与目标组织使用的VPN提供商相似的域名。威胁行为者通常会打电话给员工个人，假装来自服务台或IT团队，并声称他们正在解决VPN登录问题。如果这种社工攻击尝试成功，威胁行为者会发送一个短信链接给用户，该链接指向假冒公司VPN的假网站。

该威胁行为者还为每个目标组织设置了自定义的VPN登录页面。与此活动相关的域名如下：

- ciscoweblink.com
- ciscolinkweb.com
- ciscolinkacc.com
- ciscoacclink.com
- linkciscoweb.com
- fortivpnlink.com
- vpnpaloalto.com
- linkwebcisco.com

这些页面与每个组织的合法页面非常相似，包括可用的 VPN 组。但是，在某些情况下，威胁行为者已将“TestVPN”和“RemoteVPN”等 VPN 组添加到虚假登录页面的下拉菜单中，这可能是作为社会工程攻击中的一种策略。

通过这些虚假登录页面，威胁行为者能够收集用户的用户名、密码和令牌，即使存在多因素认证（MFA）也是如此。

如果 MFA 使用推送通知，则威胁行为者会指示用户在社交工程调用期间批准推送通知。在最后一步中，用户被重定向到目标组织的合法 VPN 地址，并可能被要求再次登录，从而加强问题已解决的错觉。

一旦威胁行为者获得对网络的VPN访问权限，他们立即开始扫描网络，以识别横向移动、持久性和进一步权限提升的目标。

GRIT写道：这种钓鱼活动中使用的社会工程类型特别难以检测，因为它通常发生在传统安全工具的可见性之外，例如通过直接拨打用户的手机号和使用短信/文本消息。

除非用户报告收到这些类型的电话或消息，否则安全团队甚至可能察觉不到。威胁行为者还可以通过这种方法针对多个用户，直到他们成功地找到一个容易受到这种攻击的用户。

为了避免安全风险，用户应对过去30天内来自VPN分配IP地址的可疑活动日志进行详细排查。如果发现任何成功的入侵迹象要立即与安全团队沟通，并立刻采取相应措施。

> 参考来源：<https://cybernews.com/news/us-vpn-phishing-attack/>

# 网络钓鱼攻击

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