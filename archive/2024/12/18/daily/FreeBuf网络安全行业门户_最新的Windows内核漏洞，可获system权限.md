---
title: 最新的Windows内核漏洞，可获system权限
url: https://www.freebuf.com/news/417893.html
source: FreeBuf网络安全行业门户
date: 2024-12-18
fetch_date: 2025-10-06T19:42:06.528580
---

# 最新的Windows内核漏洞，可获system权限

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

最新的Windows内核漏洞，可获system权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

最新的Windows内核漏洞，可获system权限

2024-12-17 13:40:55

所属地 上海

网络安全和基础设施安全局（CISA）已将两个新的漏洞添加到其已知被利用漏洞目录中，其中一个是涉及 Windows 内核的漏洞，目前正被用于攻击。

该漏洞编号为CVE-2024-35250，具体是在 Windows 的 ks.sys 驱动中存在的 "不受信任的指针解引用" 。这个漏洞可以通过利用未受信任的指针，来进行任意内存读写，最终实现权限提升。这种问题可能导致系统崩溃或使攻击者能够执行任意代码，对安全专业人员来说是一个重要关注点。

![](https://image.3001.net/images/20241217/1734414008_67610eb8010ecf0ba2b64.png!small)

微软已在最近的12月星期二补丁中修复了该漏洞 ，并表示“成功利用这一漏洞的攻击者可能获得 system权限。”该公司在6月发布的安全公告中仅提供了有限的细节，不过发现该漏洞的 DEVCORE 研究团队通过趋势科技的零日计划（Zero Day Initiative）将其报告给微软，并确定受影响的系统组件为 Microsoft Kernel Streaming Service (MSKSSRV.SYS)。

**影响版本：**

* Windows 10 20H2 Build 19042
* Windows 11 22H2 Build 22621
* VMWare Workstation 17 Pro 环境下也可被利用

**漏洞细节：**

攻击者可以通过发送特制的 IOCTL 请求触发 ks.sys 驱动中的漏洞，利用不可信指针的解引用，最终对系统内存进行任意读写操作。

**限制条件：**

* 实测该漏洞无法在 Hyper-V 环境中成功利用；
* 攻击者需要拥有中等权限（Medium Integrity Level，通常为普通用户权限），才能触发漏洞进行提权。

当前大部分 XDR（扩展检测和响应）解决方案能够检测并阻止该漏洞的利用行为。

另外一个漏洞编号是CVE-2024-20767：此漏洞影响 Adobe ColdFusion，涉及不当的访问控制。攻击者可以利用此类漏洞来获取敏感信息或系统的未经授权访问，对网络安全构成重大威胁。对此，CISA 的操作指令（BOD）22-01，题为“减少已知被利用漏洞的重大风险”，要求联邦政府行政部门（FCEB）机构在指定的截止日期前修补这些漏洞，并表示“此类漏洞是一种常见的攻击途径，对联邦企业构成重大风险。”

虽然 BOD 22-01 明确针对 FCEB 机构，但CISA 依旧强烈建议所有组织采取积极措施，以减少其网络攻击的暴露面。

参考来源：<https://cybersecuritynews.com/windows-kernal-vulnerability-actively-exploits-in-attacks/>

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