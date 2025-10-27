---
title: CISA 警告Palo Alto PAN-OS漏洞正在被积极利用
url: https://www.freebuf.com/news/422206.html
source: FreeBuf网络安全行业门户
date: 2025-02-20
fetch_date: 2025-10-06T20:35:13.749000
---

# CISA 警告Palo Alto PAN-OS漏洞正在被积极利用

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

CISA 警告Palo Alto PAN-OS漏洞正在被积极利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

CISA 警告Palo Alto PAN-OS漏洞正在被积极利用

2025-02-19 13:52:38

所属地 上海

![](https://image.3001.net/images/20250219/1739944401_67b571d1bee74ecc2c946.jpg!small)

近期，美国网络安全与基础设施安全局（CISA）发布了一则紧急警报，矛头直指帕洛阿尔托网络公司（Palo Alto Networks）防火墙设备所搭载的操作系统 PAN-OS。该系统现正遭受黑客攻击，其存在的一个高严重性身份验证绕过漏洞（CVE-2025-0108）已被黑客们积极利用。

据监测，全球范围内已有超过 25 个恶意 IP 地址对未安装补丁的系统发动攻击。联邦当局联合网络安全专家发出警告：攻击者很可能将这一漏洞与其他漏洞串联起来，从而对关键网络基础设施造成严重破坏。

CVE-2025-0108 的通用漏洞评分系统 3.1 版评分为 7.8，这意味着，未经身份验证但能够访问 PAN-OS 管理 Web 界面的攻击者，可以借此绕过身份验证控制，进而执行特定的 PHP 脚本。虽说这一漏洞本身不会直接导致远程代码执行，但攻击者通过未经授权访问敏感功能，已然对系统的完整性和保密性构成了严重威胁。

帕洛阿尔托网络公司确认，若将 CVE-2025-0108 与 CVE-2024-9474（一个在 2024 年 11 月已修复的权限提升漏洞）结合利用，黑客便能完全控制设备。

受此次漏洞影响的版本包括 PAN-OS 10.1（10.1.14-h9 之前的版本）、10.2（10.2.13-h3 之前的版本）、11.1（11.1.6-h1 之前的版本）以及 11.2（11.2.4-h4 之前的版本）。不过，云下一代防火墙（Cloud NGFW）和 Prisma Access 部署目前不受影响。

## 攻击趋势与溯源

GreyNoise 的监测数据显示，攻击态势在短时间内急剧恶化。从 2 月 13 日仅 2 个恶意 IP 地址发起攻击，到 2 月 18 日，这一数字已激增至 25 个。进一步调查发现，这些攻击流量主要源自美国、德国和荷兰。

![](https://image.3001.net/images/20250219/1739944642_67b572c20b46fc9b5cd49.jpg!small)

攻击者利用的是公开的概念验证（PoC）漏洞利用程序，而这些程序的技术细节，大多来源于 Assetnote 研究人员的披露。他们在调查早期 PAN-OS 漏洞时，首次发现了 CVE-2025-0108 这个漏洞。

2 月 19 日，帕洛阿尔托网络公司更新了安全公告，明确指出针对未安装补丁的防火墙，尤其是面向互联网的管理界面的攻击数量正在 “不断增加”。

对此，帕洛阿尔托网络公司发言人史蒂文・泰（Steven Thai）强调：“我们强烈敦促所有客户立即应用更新，并严格限制管理界面的访问权限。”

## 应对措施与建议

CISA 和帕洛阿尔托网络公司共同给出了以下应对建议：

1. **立即应用补丁**：尽快将 PAN-OS 升级到 10.1.14-h9、10.2.13-h3、11.1.6-h1 或 11.2.4-h4 版本，这些版本已修复 CVE-2025-0108 漏洞。
2. **限制管理界面访问**：只允许受信任的内部 IP 地址进行连接，坚决避免管理界面暴露在公共互联网中。
3. **禁用未使用的服务**：若不需要 OpenConfig 插件，应及时将其停用，以防它成为额外的攻击入口。
4. **监测攻击行为**：借助 GreyNoise 等威胁情报平台，实时跟踪与 CVE-2025-0108 相关的恶意 IP 地址。

Assetnote 的舒巴姆・沙阿（Shubham Shah）指出，CVE-2025-0108 的真正威胁在于，它为攻击者提供了初始访问途径。他强调：“攻击者会将这个漏洞与二次漏洞利用程序结合，从而实现命令执行。” 这种攻击策略并非首次出现，与之前利用 CVE-2024-0012 和 CVE-2024-9474 针对 PAN-OS 身份验证机制的攻击活动如出一辙。

对于依赖帕洛阿尔托防火墙的联邦机构和企业而言，当务之急是优先部署补丁，因为未受保护的设备随时都有被攻击的风险。CISA 发布这一警报，与其 “设计安全” 倡议高度契合，旨在敦促供应商和客户从源头上消除关键基础设施中的默认暴露风险。

随着攻击活动的持续升级，各组织务必争分夺秒，尽快缓解 CVE-2025-0108 带来的安全隐患。在帕洛阿尔托网络公司全力遏制威胁的同时，管理员必须严格落实访问控制措施，并假定未安装补丁的设备已被入侵，提前做好应对准备。

**参考链接：**

> <https://cybersecuritynews.com/pan-os-vulnerability-actively-exploited/>

# 资讯

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

攻击趋势与溯源

应对措施与建议

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