---
title: 依然活跃，30% 的 CVE 漏洞利用事件再次发现 Log4Shell
url: https://www.freebuf.com/news/400990.html
source: FreeBuf网络安全行业门户
date: 2024-05-16
fetch_date: 2025-10-06T17:16:08.809377
---

# 依然活跃，30% 的 CVE 漏洞利用事件再次发现 Log4Shell

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

依然活跃，30% 的 CVE 漏洞利用事件再次发现 Log4Shell

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

依然活跃，30% 的 CVE 漏洞利用事件再次发现 Log4Shell

2024-05-15 10:58:43

所属地 上海

根据 Cato Networks 的一项调查结果显示，许多组织一直在其广泛的访问网络 （WAN） 上运行不安全的协议，使得网络犯罪分子更容易进行跨网络移动（农业、房地产、旅行和旅游业中尤为明显）。
![](https://image.3001.net/images/20240515/1715750757_66444765c6e7ff35644ee.jpg!small)

## 组织过于信任自身的网络防御系统

Cato 在一份报告中深入分析了安全威胁及其识别网络特征，包括所有总流量（无论其来自互联网还是广域网，亦或是其目的地是互联网还是广域网），以及跨站点、远程用户和云资源的所有端点。

Cato Networks 首席安全战略师 Etay Maor 指出，由于威胁攻击者不断推出针对各行各业组织的新威胁工具、技术和应用程序，网络威胁情报仍然”支离破碎“，非常难以形成有效的体系，解决方案很难做出有效应对。

一旦威胁攻击者渗透到受害者网络系统中，就会立刻窥探网络传输中的关键数据。更糟糕的是，研究人员发现，很多入侵过程非常”丝滑“，不会遇到太大阻力。此外，几乎所有企业一直在其 WAN 上运行不安全的协议，其中 62% 的 Web 应用程序流量是 HTTP，54% 的流量是 telnet，46% 的流量是 SMB v1 或 v2，而不是 SMBv3。

## 不同行业的安全性各不相同

在调查过程中，研究人员发现，横向移动（攻击者在网络间自由移动）在农业、房地产和旅游行业中最常见。

2024 年前三个月，企业最常用的人工智能工具是微软 Copilot、OpenAI ChatGPT 和 Emol（一种记录情感并与人工智能机器人对话的应用程序），采用这些工具最多的是旅游和旅游业（79% 的企业采用），采用率最低的是娱乐业（44%）。

媒体、娱乐相关机构中，48% 的组织没有使用 Cato CTRL 确定的 200+ 应用程序之一作为信息安全工具。在服务和酒店业，威胁攻击者使用 T1212 利用凭据访问的频率是其他行业的三倍，甚至更多。

虽然零日安全漏洞在业内备受关注，但研究人员发现，威胁攻击者往往不会使用新漏洞，反而喜欢针对未打补丁的系统（有很多带有漏洞的系统，不进行补丁修复安全漏洞），开展网络攻击行动。研究人员在评估十大入站常见安全漏洞时，针对 PHPUnit 测试框架的安全漏洞 CVE-2017-9841 ”得票率“最高，有 33% 的入站 CVE 攻击中都发现了其踪迹。

值得一提的是，研究人员指出，Log4Shell（CVE-2021-44228）在被发现三年后仍然是最常用的漏洞利用之一，在观察到的 30% 的出站 CVE 漏洞利用中都发现了它的痕迹。

参考文章：

> https://www.helpnetsecurity.com/2024/05/14/log4j-wan-insecure-protocols/

# 漏洞分析

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

组织过于信任自身的网络防御系统

不同行业的安全性各不相同

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