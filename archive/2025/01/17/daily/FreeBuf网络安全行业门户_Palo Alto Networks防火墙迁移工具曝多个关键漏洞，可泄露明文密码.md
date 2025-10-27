---
title: Palo Alto Networks防火墙迁移工具曝多个关键漏洞，可泄露明文密码
url: https://www.freebuf.com/news/419970.html
source: FreeBuf网络安全行业门户
date: 2025-01-17
fetch_date: 2025-10-06T20:10:19.957347
---

# Palo Alto Networks防火墙迁移工具曝多个关键漏洞，可泄露明文密码

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

Palo Alto Networks防火墙迁移工具曝多个关键漏洞，可泄露明文密码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Palo Alto Networks防火墙迁移工具曝多个关键漏洞，可泄露明文密码

2025-01-16 10:52:58

所属地 上海

据Cyber Security News消息，Palo Alto Networks 在其 Expedition 迁移工具中披露了多个关键安全漏洞，包括一个令人担忧的操作系统命令注入漏洞，该漏洞使攻击者能够执行任意命令并访问敏感的防火墙凭证。

![](https://image.3001.net/images/20250116/1736995967_6788747fcd59b86a585e3.jpg!small)

这一命令注入漏洞被追踪为CVE-2025-0107，允许经过身份验证的攻击者以 www-data 用户身份运行任意 OS 命令，从而可能暴露运行 PAN-OS 软件防火墙的用户名、明文密码、设备配置和 API 密钥。

据悉，Expedition 已于 2024 年 12 月 31 日达到生命周期终点 (EoL)，因此暴露出大量漏洞。已披露的其他漏洞包括 SQL 注入（CVE-2025-0103、CVSS 7.8）、反射型跨站点脚本（CVE-2025-0104、CVSS 4.7）、任意文件删除（CVE-2025-0105、CVSS 2.7）和通配符扩展枚举（CVE-2025-0106、CVSS 2.7）。

Palo Alto Networks 已在 1.2.100 版本（针对 CVE-2025-0103、CVE-2025-0104 和 CVE-2025-0107）和版本 1.2.101（针对 CVE-2025-0105 和 CVE-2025-0106）中解决了这些安全问题。但是，由于该工具已达到 EoL 状态，因此该公司不打算发布任何其他更新或安全修复程序。

安全研究人员指出，虽然目前没有证据表明这些新漏洞被积极利用，但针对类似漏洞的概念验证漏洞的可用性引发了对未来潜在攻击的担忧。

为了降低这些风险，Palo Alto Networks 强烈建议企业组织采取应对措施：

* 升级到 Expedition 1.2.101 或更高版本
* 将网络访问限制为仅授权用户、主机和网络
* 在不频繁使用 Expedition 时完全禁用 Expedition
* 由于已进入 EoL 状态，建议考虑不再使用该工具

Expedition是一款免费实用程序，旨在帮助企业组织从其他供应商过渡到 Palo Alto Networks 的下一代防火墙 （NGFW） 平台。

虽然这些漏洞不会直接影响 Palo Alto Networks 防火墙、Panorama 设备、Prisma Access 部署或云 NGFW，但它们会严重危害运行 Expedition 易受攻击版本的系统的安全性。

**参考来源：**

> [Palo Alto Networks Expedition Tool Vulnerability Exposes Cleartext Firewall Passwords](https://cybersecuritynews.com/palo-alto-networks-expedition-firewall-passwords/#google_vignette)

# 系统安全

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