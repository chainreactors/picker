---
title: 慎用，知名压缩工具7-Zip存在严重漏洞
url: https://www.freebuf.com/news/416144.html
source: FreeBuf网络安全行业门户
date: 2024-11-27
fetch_date: 2025-10-06T19:17:57.714322
---

# 慎用，知名压缩工具7-Zip存在严重漏洞

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

慎用，知名压缩工具7-Zip存在严重漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

慎用，知名压缩工具7-Zip存在严重漏洞

2024-11-26 10:25:54

所属地 上海

近日，主流文件压缩工具7-Zip被曝存在一个严重的安全漏洞，允许远程攻击者通过精心制作的存档执行恶意代码。该漏洞编号为CVE-2024-11477，CVSS评分7.8分，表明受影响版本的用户面临重大安全风险。![](https://image.3001.net/images/20241126/1732588597_6745343557b2f6e01eab1.jpg!small)

漏洞存在于 Zstandard 解压缩的实现中。此问题是由于未正确验证用户提供的数据而导致的，这可能导致在写入内存之前出现整数下溢。攻击者可以利用此漏洞在当前进程的上下文中执行代码，但要利用此漏洞，需要与此库交互，但攻击媒介可能因实施而异。

根据趋势科技安全研究部的Nicholas Zubrisky的说法，攻击者可以通过说服用户打开精心准备的存档来利用此漏洞，这些存档可以通过电子邮件附件或共享文件分发。

Zstandard格式在Linux环境中尤为普遍，通常用于各种文件系统，包括Btrfs、SquashFS和OpenZFS。

### 漏洞影响

* 在受影响的系统上执行任意代码
* 获得与登录用户相同的访问权限
* 可能实现完全的系统绕过

### 缓解措施和修复

7-Zip已在24.07版本中解决了此安全问题。由于该软件缺乏集成的更新机制，用户必须手动下载并安装最新版本以保护其系统，官网地址：<https://www.7-zip.org/>

在企业环境中使用7-Zip的IT管理员和软件开发者应立即将其安装更新为已修补的版本。需要注意的是，由于7-Zip钓鱼邮件和带病毒的假冒产品非常多，在搜索引擎中搜索下载时请注意甄别。

该漏洞最初于

2024年6月，安全研究人员向7-Zip报告了该漏洞，并于11月20日公开披露。尽管目前没有已知的恶意软件针对此漏洞。，但安全专家强烈建议用户及时修补，因为利用该漏洞所需的技术专业知识最少，

这一事件突显了应用程序安全中输入验证的关键重要性，特别是在处理可能不受信任的数据时，使用7-Zip或包含其功能的产品组织和个体应优先更新到最新版本以维护系统安全。

参考来源：<https://cybersecuritynews.com/7-zip-vulnerability-arbitrary-code/>

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