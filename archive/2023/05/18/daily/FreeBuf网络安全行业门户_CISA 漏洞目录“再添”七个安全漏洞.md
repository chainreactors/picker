---
title: CISA 漏洞目录“再添”七个安全漏洞
url: https://www.freebuf.com/news/366718.html
source: FreeBuf网络安全行业门户
date: 2023-05-18
fetch_date: 2025-10-04T11:40:03.714319
---

# CISA 漏洞目录“再添”七个安全漏洞

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

CISA 漏洞目录“再添”七个安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

CISA 漏洞目录“再添”七个安全漏洞

2023-05-17 10:53:16

所属地 上海

Security Affairs 网站披露，美国网络安全和基础设施安全局（CISA）在其已知被利用的漏洞目录中增加了七个新安全漏洞。![1684291974_64644186629e11db4e92b.png!small](https://image.3001.net/images/20230517/1684291974_64644186629e11db4e92b.png!small)

## **漏洞详情**：

**CVE-2023-25717：**Cybir 的研究人员发现 Ruckus 无线接入点（AP）软件在 web 服务组件中存在一个未知漏洞。一旦用户在 AP 上启用了 web 服务组件，攻击者就可以执行跨站点请求伪造（CSRF）或远程代码执行（RCE）。此漏洞会影响 Ruckus ZoneDirector、SmartZone 和 Solo AP，用户应尽快安装补丁；

**CVE-2021-3560：**Red Hat Polkit 通过绕过 D-Bus 请求的凭据检查，包含一个不正确的授权漏洞，攻击者可以利用该漏洞进行权限升级。polkit 是一个应用层面的工具包，用于定义和处理允许非特权进程与特权进程对话的策略，它被默认安装在几个 Linux 发行版上。

**CVE-2014-0196：**Linux 内核在 n\_tty\_write 函数中包含一个竞争条件漏洞，该漏洞允许本地用户通过长字符串的读写操作造成拒绝服务或获得特权。；

**CVE-2010-3904：**Linux 内核在可靠数据报套接字（RDS）协议实现中包含一个不正确的输入验证漏洞，该漏洞允许本地用户通过精心使用 sendmsg 和 recvmsg 系统调用来获得权限；

**CVE-2015-5317：**Jenkins用户界面（UI）包含一个信息泄露漏洞，该漏洞允许用户在“指纹”页面上查看作业和构建的名称。

**CVE-2016-3427：**Oracle Java SE、Java SE Embedded 和 JRockit 中的 JMX 子组件存在安全漏洞。远程攻击者可利用该漏洞控制组件，影响数据的保密性，完整性及可用性。

攻击者可通过沙盒 Java Web Start 应用程序和沙盒 Java 小程序利用该漏洞，也可以通过向指定组件中的 API 提供数据来利用漏洞。受到影响版本包括 Oracle Java SE 6u113 版本，7u99 版本，8u77 版本，Java SE Embedded 8u77 版本，Jrockit R28.3.9 版本；

**CVE-2016-8735：**Apache Tomcat 中存在一个远程代码执行漏洞，远程攻击者可利用该漏洞执行任意代码。一旦攻击者使用 JmxRemoteLifecycleListener 并且获得访问 Java 管理扩展（JMX）端口的权限，就可以轻松利用该漏洞允，执行远程代码。受影响版本包括 Apache Tomcat 6.0.48 之前的版本，7.0.73 之前的7.x版本，8.0.39 之前的 8.x 版本，8.5.7 之前的 8.5.x 版本，9.0.0.M12 之前的 9.x 版本。

根据约束性操作指令（BOD）22-01的要求，所有联邦民事行政部门机构(FCEB)在被添加到 CISA 的已知利用漏洞(KEV)目录后，必须在到期日前解决已识别的漏洞，保护其系统免受此安全漏洞的影响，降低已知被利用漏洞的重大风险。此外，网络安全专家建议私营组织也应该审查 CISA 目录中的漏洞，并解决其基础设施中存在的漏洞。

最后，CISA 命令联邦机构在 2023 年 6 月 2 日之前修复上述漏洞！

**文章来源：**

> https://securityaffairs.com/146285/hacking/known-exploited-vulnerabilities-catalog-ruckus.html

# 安全漏洞

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

漏洞详情：

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