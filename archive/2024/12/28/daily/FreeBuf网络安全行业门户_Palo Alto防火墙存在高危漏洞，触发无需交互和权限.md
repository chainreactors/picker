---
title: Palo Alto防火墙存在高危漏洞，触发无需交互和权限
url: https://www.freebuf.com/news/418628.html
source: FreeBuf网络安全行业门户
date: 2024-12-28
fetch_date: 2025-10-06T19:38:37.628583
---

# Palo Alto防火墙存在高危漏洞，触发无需交互和权限

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

Palo Alto防火墙存在高危漏洞，触发无需交互和权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Palo Alto防火墙存在高危漏洞，触发无需交互和权限

2024-12-27 14:14:56

所属地 上海

Palo Alto Networks近日披露，其下一代防火墙中的PAN-OS软件存在一个高危漏洞，编号为CVE-2024-3393。该漏洞允许未经身份验证的攻击者通过发送精心构造的DNS数据包，利用DNS安全特性触发拒绝服务（DoS）状态。若此漏洞被反复利用，可能导致受影响的防火墙重启并进入维护模式。

![](https://image.3001.net/images/20241227/1735280103_676e45e7b28446a3a5066.png!small)

问题的根源在于PAN-OS的DNS安全特性对异常情况的处理不当。攻击者可通过防火墙的数据平面发送恶意数据包，进而使其崩溃并重启。此漏洞的CVSS评分为8.7（高），意味着其具有较大的破坏潜力。该攻击复杂性低，无需用户交互和权限，且可通过网络远程执行。

该漏洞影响多个版本的PAN-OS：

> PAN-OS 11.2：受影响版本低于11.2.3；
>
> PAN-OS 11.1：受影响版本低于11.1.5；
>
> PAN-OS 10.2：受影响版本低于10.2.8，且在维护版本中提供了额外修复；
>
> PAN-OS 10.1：受影响版本低于10.1.14。

使用受影响PAN-OS版本的Prisma Access客户也存在风险。Palo Alto Networks确认，在生产环境中已出现该漏洞被利用的情况，攻击者成功触发了由此导致的DoS攻击。

尽管该漏洞不影响机密性或完整性，但对可用性影响很大，所以对依赖这些防火墙进行网络安全保护的组织而言，这是一个关键问题。

Palo Alto Networks已发布以下版本的补丁来解决此问题：

> PAN-OS 10.1.14 - h8
>
> PAN-OS 10.2.10 - h12
>
> PAN-OS 11.1.5
>
> PAN-OS 11.2.3

强烈建议客户升级到这些版本或更高版本以降低风险。

对于无法立即应用修复的用户，临时解决方案包括禁用DNS安全日志记录，具体步骤如下：
1. 导航至对象→安全配置文件→反间谍软件→DNS策略；
2. 将所有DNS安全类别的“日志严重性”设置为“无”；
3. 提交更改，并在应用修复后恢复设置。

使用Palo Alto防火墙的组织应当：

* 立即应用补丁以保护系统；
* 若无法打补丁，则实施推荐的临时解决方案；
* 监控防火墙行为，查看是否有意外重启或进入维护模式的情况；
* 定期查看安全通告并保持软件版本更新。

这一漏洞凸显了及时进行修补管理以及实施强大监控实践的重要性，只有这样才能保护网络基础设施免受新出现威胁的攻击。

参考来源：<https://cybersecuritynews.com/#google_vignette>

# 漏洞

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