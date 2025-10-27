---
title: Palo Alto Networks确认0Day漏洞正在被黑客利用
url: https://www.freebuf.com/news/415484.html
source: FreeBuf网络安全行业门户
date: 2024-11-19
fetch_date: 2025-10-06T19:18:21.411216
---

# Palo Alto Networks确认0Day漏洞正在被黑客利用

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

Palo Alto Networks确认0Day漏洞正在被黑客利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Palo Alto Networks确认0Day漏洞正在被黑客利用

2024-11-18 11:35:35

所属地 上海

近日，全球网络巨头Palo Alto Networks确认旗下0Day漏洞正在被黑客利用。11月8日，Palo Alto Networks发布了一份安全通告([https://security.paloaltonetworks.com/PAN-SA-2024-0015)](https://security.paloaltonetworks.com/PAN-SA-2024-0015%29)，警告客户PAN-OS管理界面中存在一个远程代码执行漏洞，并建议客户确保PAN-OS管理界面访问的安全性。![](https://image.3001.net/images/20241118/1731901242_673ab73a68324e09d69e4.jpg!small)

但随着该漏洞的曝光，Palo Alto Networks在11月15日发现已经有黑客/威胁组织正在利用该漏洞，对用户发起网络攻击，主要目标用户是那些暴露在互联网上防火墙管理界面。

目前还不清楚该漏洞如何暴露，以及受影响的企业范围。该漏洞也还没有分配CVE标识符，CVSS评分9.3分。Palo Alto Networks表示，他们认为Prisma Access和Cloud NGFW产品不受此漏洞影响。

### **安全措施和建议**

目前，Palo Alto Networks正在开发补丁和威胁预防签名，建议客户确保只有来自可信IP地址的访问才能访问防火墙管理界面，而不是从互联网访问。公司指出，大多数防火墙已经遵循了这一Palo Alto Networks和行业的安全最佳实践。

其他受影响的产品：除了上述漏洞，美国网络安全机构CISA还表示，他们知道有三个影响Palo Alto Networks Expedition的漏洞在野外被利用。CISA警告，至少有两个影响Palo Alto Networks Expedition软件的漏洞正在被积极利用，并已将这些漏洞添加到其已知被利用漏洞(KEV)目录中，要求联邦文职行政部门机构在2024年12月5日之前应用必要的更新。

### 屡屡出现0Day漏洞

值得一提的是，在2024年3月，Palo Alto Networks防火墙产品也曾被曝存在严重安全漏洞，编号 CVE-2024-3400 ，CVSS 评分达10分，具体涉及PAN-OS 10.2、PAN-OS 11.0 和 PAN-OS 11.1 防火墙版本软件中的两个缺陷。

在第一个缺陷中，GlobalProtect 服务在存储会话 ID 格式之前没有对其进行充分验证。Palo Alto Networks 产品安全高级总监 Chandan B. N. 表示，这使得攻击者能够用选择的文件名存储一个空文件。第二个缺陷被认为是系统生成的文件将文件名作为了命令的一部分。

值得注意的是，虽然这两个缺陷本身都不够严重，但当它们组合在一起时，就可能导致未经验证的远程 shell 命令执行。

Palo Alto Network表示，利用该漏洞实施零日攻击的攻击者实施了两阶段攻击，以便在易受影响的设备上执行命令。该活动被命名为Operation MidnightEclipse，涉及发送包含要执行命令的特制请求，然后通过名为 UPSTYLE 的后门运行。

在攻击的第一阶段，攻击者向 GlobalProtect 发送精心制作的 shell 命令而非有效的会话 ID，导致在系统上创建一个空文件，文件名由攻击者命名为嵌入式命令；在第二阶段，定时运行系统作业会在命令中使用攻击者提供的文件名，进而让攻击者提供的命令能以更高的权限执行。利用这种方式，攻击者就能将该漏洞武器化，且不需要在设备上启用遥测功能就能对其进行渗透。

参考来源：<https://www.securityweek.com/palo-alto-networks-confirms-new-firewall-zero-day-exploitation/>

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