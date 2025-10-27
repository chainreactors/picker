---
title: 重大供应链威胁！这个 Java 开源框架存在严重漏洞
url: https://www.freebuf.com/news/359129.html
source: FreeBuf网络安全行业门户
date: 2023-03-03
fetch_date: 2025-10-04T08:32:20.766727
---

# 重大供应链威胁！这个 Java 开源框架存在严重漏洞

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

重大供应链威胁！这个 Java 开源框架存在严重漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

重大供应链威胁！这个 Java 开源框架存在严重漏洞

2023-03-02 15:01:36

所属地 上海

![](https://image.3001.net/images/20230302/1677740715_64004aab158529f5ab612.jpg!small)

美国网络安全和基础设施安全局（CISA）和安全研究人员报告称，一个受广泛使用的开源Java框架中存在严重漏洞并被攻击者利用，他们正利用该漏洞向未打补丁的服务器部署后门。专家表示，这种情况可能会对未打补丁的软件构成重大供应链威胁。

CISA已将CVE-2022-36537添加到其已知已开发漏洞（KEV）目录中，该漏洞影响ZK Java Web框架9.6.1、9.6.0.1、9.5.1.3、9.0.1.2和8.6.4.1版本。

根据KEV列表，在ZK框架AuUploader servlets中发现的这个漏洞，可能允许攻击者 "检索位于Web上下文中的文件内容"，从而窃取敏感信息。CISA表示：该漏洞可以影响多个产品，包括但不限于ConnectWise R1Soft Server Backup Manager。

事实上，该漏洞在2022年10月首次出现便引起广泛关注，当时ConnectWise对其产品中漏洞的存在发出了警报，特别是ConnectWise Recover和R1Soft服务器备份管理器技术。Huntress的高级安全研究人员John Hammond和Caleb Stewart随后发表了一篇关于如何利用该漏洞的博文。

CISA和Huntress都是根据Fox-IT 2月22日发表的研究报告发出警告的，该报告发现有证据表明攻击者使用易受攻击版本的ConnectWise R1Soft Server Backup Manager软件 作为初始访问点和控制通过R1Soft Backup Agent连接的下游系统的平台，研究人员在一篇博客文章中写道。

研究人员在博文中还写道：这个代理被安装在系统上，以支持被R1Soft服务器软件备份，通常以高权限运行。这意味着，在对手最初通过R1Soft服务器软件获得访问权后，它能够在连接到该R1Soft服务器的所有运行代理的系统上执行命令。

## 漏洞的历史

ConnectWise方面在10月迅速采取行动为产品打补丁，向ConnectWise服务器备份管理器（SBM）的云端和客户端实例推送了自动更新，并敦促R1Soft服务器备份管理器的客户立即升级到新的SBM v6.16.4。

总部位于德国的安全厂商Code White GmbH的一名研究人员率先发现了CVE-2022-36537，并在2022年5月向ZK Java Web框架的维护者报告。他们在该框架的9.6.2版本中修复了这个问题。

根据Huntress的博文，ConnectWise意识到其产品的漏洞，当时同一公司的另一位研究人员发现ConnectWise的R1Soft SBM技术正在使用有漏洞的ZK库版本，并向公司报告了这个问题。

当该公司在90天内没有回应时，研究人员在Twitter上公布了一些关于如何利用该漏洞的细节，Huntress的研究人员利用这些细节复制了该漏洞并完善了一个概念验证（PoC）漏洞。

Huntress的研究人员最终证明他们可以利用该漏洞泄露服务器私钥、软件许可信息和系统配置文件，并最终在系统超级用户的背景下获得远程代码执行。

当时，研究人员通过Shodan发现了 多达5000个暴露的服务器管理器备份实例，所有这些都有可能被威胁者利用，同时还有他们的注册主机。他们推测，该漏洞有可能影响到比这更多的机器。

## 供应链面临风险

当Huntress对该漏洞进行分析时，没有证据表明存在主动利用的情况。现在，随着这种情况的改变，不仅在ConnectWise，在其他产品中也存在任何未打补丁的ZK Java Web框架版本。这对攻击者来说无疑是利好的，同时这可能给供应链带来重大风险。

Fox-IT的研究表明，全世界对ConnectWise的R1Soft服务器软件的利用大约始于11月底，也就是Huntress发布其PoC之后不久。

研究人员写道：在指纹识别的帮助下，我们已经在全球范围内确定了多个被攻击的主机供应商。

Fox-IT研究人员在1月9日说，他们已经确定了 总共有286台运行R1Soft服务器软件的服务器带有特定后门。

根据KEV列表，CISA敦促任何仍在使用受影响ConnectWise产品的未修补版本的组织“根据供应商说明”更新其产品。虽然到目前为止，该漏洞的存在仅在ConnectWise产品中被发现，但使用未修补版本的框架的其他软件也容易受到攻击。

> 参考链接：https://www.darkreading.com/risk/cisa-zk-java-framework-rce-flaw-under-active-exploit

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

漏洞的历史

供应链面临风险

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