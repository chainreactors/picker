---
title: Windows存储系统现0day漏洞，攻击者可远程删除目标文件
url: https://www.freebuf.com/articles/system/421642.html
source: FreeBuf网络安全行业门户
date: 2025-02-13
fetch_date: 2025-10-06T20:35:08.106447
---

# Windows存储系统现0day漏洞，攻击者可远程删除目标文件

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

Windows存储系统0day漏洞，攻击者可远程删除目标文件

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

Windows存储系统0day漏洞，攻击者可远程删除目标文件

2025-02-12 08:13:54

所属地 上海

![image](https://image.3001.net/images/20250212/1739372543363895_22d2314075c84a8c8e120c2b8b714894.webp!small)

Windows系统近日被曝出一个重大安全漏洞，攻击者可利用该漏洞远程删除受影响系统上的目标文件。该漏洞编号为CVE-2025-21391，于2025年2月11日披露，属于权限提升漏洞，严重性被评定为"重要"级别。

## **漏洞详情与风险分析**

CVE-2025-21391利用了一个被称为"文件访问前链接解析不当"（CWE-59）的缺陷，使攻击者能够操纵文件访问权限。该漏洞的CVSS评分为7.1，属于中高风险的漏洞。

攻击向量为本地（AV:L），攻击复杂度低（AC:L），所需权限也较低（PR:L），这意味着攻击者无需大量资源或高权限即可利用该漏洞。微软研究人员指出，CVSS评分显示该漏洞不会导致机密性丧失（C:N），但对完整性（I:H）和可用性（A:H）的影响重大。换句话说，虽然无法窃取敏感信息，但攻击者可以删除重要文件，可能导致系统运行中断。

## **影响范围与缓解措施**

该漏洞已在野被利用，状态显示为"已检测到利用"。成功利用该漏洞的攻击者可以删除目标文件，如果关键系统文件受到影响，可能导致服务不可用。受影响的Windows版本包括Windows Server 2016、Windows Server 2019、Windows Server 2022、Windows 10（版本1607、1809、21H2和22H2）以及Windows 11（版本22H2）。x64和ARM64架构的系统均受到影响。

为防范该漏洞，建议用户尽快应用微软2025年2月发布的月度安全更新。用户应优先更新系统，以防潜在攻击，确保数据的完整性和可用性。

**参考来源：**

> [Windows Storage 0-Day Vulnerability Let Attackers Delete The Target Files Remotely](https://cybersecuritynews.com/windows-storage-0-day-vulnerability/)

# 漏洞 # 终端安全

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

漏洞详情与风险分析

影响范围与缓解措施

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