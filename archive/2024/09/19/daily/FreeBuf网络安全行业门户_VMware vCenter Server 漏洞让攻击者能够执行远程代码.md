---
title: VMware vCenter Server 漏洞让攻击者能够执行远程代码
url: https://www.freebuf.com/news/411162.html
source: FreeBuf网络安全行业门户
date: 2024-09-19
fetch_date: 2025-10-06T18:25:33.378796
---

# VMware vCenter Server 漏洞让攻击者能够执行远程代码

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

VMware vCenter Server 漏洞让攻击者能够执行远程代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

VMware vCenter Server 漏洞让攻击者能够执行远程代码

2024-09-18 11:11:18

所属地 上海

据Cyber Security News消息，VMware 披露了两个影响其 vCenter Server 和 Cloud Foundation 产品的关键安全漏洞，这些漏洞可能允许攻击者执行远程代码并提升权限。该公司敦促客户立即修补受影响的系统。

![](https://image.3001.net/images/20240918/1726630899_66ea4bf3b6252b576a50c.png!small)

其中一个漏洞被追踪为 CVE-2024-38812，是在 vCenter Server 中实施 DCERPC 协议时存在的堆溢出漏洞，CVSS 评分高达 9.8。根据 VMware 的公告，具有网络访问权限的攻击者对易受攻击的 vCenter Server可以通过发送特制网络数据包来触发此漏洞，从而导致远程代码执行。

另一个漏洞被追踪为CVE-2024-38813，属 vCenter Server 中的权限提升缺陷，CVSS 评分7.5，可能允许攻击者通过发送恶意网络数据包将权限升级到 root。

这两个漏洞都会影响 VMware vCenter Server 7.0 和 8.0 版本，以及 VMware Cloud Foundation 4.x 和 5.x 版本。

VMware 已发布修补程序来解决这些缺陷，并强烈建议客户尽快应用这些更新。对于 vCenter Server，用户应尽快升级到8.0 U3b 或 7.0 U3s 版本，Cloud Foundation 客户应应用 KB88287 中引用的异步修补程序。

该公司表示，到目前为止还没有发现任何对这些漏洞的野外利用。但是，鉴于 vCenter Server 在管理虚拟化环境方面的关键性质，这些缺陷可能成为攻击者的诱人目标。

据悉，这两个漏洞由参加中国2024“矩阵杯”网络安全大赛的TZL研究人员发现，并在事后向 VMware 进行了报告。

今年6月，VMware 曾修复了一个类似的 vCenter Server 远程代码执行漏洞 （CVE-2024-37079），该漏洞可通过特制数据包进行攻击。

**参考来源：**

> [VMware vCenter Server Vulnerabilities Let Attackers Execute Remote Code](https://cybersecuritynews.com/vmware-vcenter-server-remote-code/#google_vignette)

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