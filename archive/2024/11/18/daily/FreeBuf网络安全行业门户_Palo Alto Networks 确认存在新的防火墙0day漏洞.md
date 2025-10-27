---
title: Palo Alto Networks 确认存在新的防火墙0day漏洞
url: https://www.freebuf.com/news/415441.html
source: FreeBuf网络安全行业门户
date: 2024-11-18
fetch_date: 2025-10-06T19:14:20.062068
---

# Palo Alto Networks 确认存在新的防火墙0day漏洞

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

Palo Alto Networks 确认存在新的防火墙0day漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Palo Alto Networks 确认存在新的防火墙0day漏洞

2024-11-17 11:59:49

所属地 上海

在告知客户正在调查有关新的防火墙远程代码执行漏洞后，Palo Alto Networks 于周五证实，一种新的0day漏洞正被用于攻击。![](https://image.3001.net/images/20241117/1731815982_67396a2edd5ce8c1d399b.jpg!small)

Palo Alto Networks于 11 月 8 日发布了一份公告([https://security.paloaltonetworks.com/PAN-SA-2024-0015)](https://security.paloaltonetworks.com/PAN-SA-2024-0015%29)，针对有关远程代码执行漏洞的说法，敦促客户确保对 PAN-OS 管理界面的访问是安全的。

Palo Alto Networks 最初表示，尚未发现任何0day漏洞被利用的迹象，但在周五，该公司更新了公告，称“已观察到利用未经身份验证的远程命令执行漏洞针对有限数量暴露在互联网上的防火墙管理接口的威胁活动”。

目前还不清楚该漏洞是如何暴露的、谁利用了它、以及攻击的目标是谁。

该漏洞尚未分配 CVE 标识符，但其 CVSS 评分为 9.3，属于“严重级别”。

Palo Alto 告诉客户，它正在开发补丁和威胁预防签名，希望很快发布。Palo Alto 建议客户确保只能从受信任的 IP 地址访问防火墙管理界面，而不能从互联网访问。

Palo Alto Networks 表示：“绝大多数防火墙已经遵循 Palo Alto Networks 和行业最佳实践。”

该安全公司指出，“如果管理界面访问仅限于 IP，则利用的风险将大大限制，因为任何潜在攻击都首先需要对这些 IP 的特权访问。”

该公司认为 Prisma Access 和 Cloud NGFW 产品不受影响。

这并不是最近几天曝光的唯一一个 Palo Alto 产品漏洞。美国网络安全机构 CISA 表示，它已经发现有三个影响 Palo Alto Networks Expedition 的漏洞已被利用。

**新闻链接：**

<https://www.securityweek.com/palo-alto-networks-confirms-new-firewall-zero-day-exploitation/>

# 漏洞 # 安全漏洞

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