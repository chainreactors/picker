---
title: FreeBuf周报 | AWS密钥泄露即可被利用；新型钓鱼工具包能让“菜鸟”轻松发动攻击
url: https://www.freebuf.com/news/417080.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:26.244095
---

# FreeBuf周报 | AWS密钥泄露即可被利用；新型钓鱼工具包能让“菜鸟”轻松发动攻击

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

FreeBuf周报 | AWS密钥泄露即可被利用；新型钓鱼工具包能让“菜鸟”轻松发动攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBuf周报 | AWS密钥泄露即可被利用；新型钓鱼工具包能让“菜鸟”轻松发动攻击

2024-12-06 15:44:07

所属地 上海

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、安全事件、一周好文和省心工具，保证大家不错过本周的每一个重点！![](https://image.3001.net/images/20220923/1663923572_632d7574ead5a97f52086.jpg!small)

## 热点资讯

### 1. 因涉嫌实施侵入性的监控行为，苹果公司在加州被员工起诉

一名现任苹果员工于美国当地时间12月1日向加利福尼亚州法院提起诉讼，指控苹果侵入性的监控行为干预了员工的个人生活。

### 2. 只需几分钟，AWS密钥泄露即可被利用

Clutch Security的研究人员进行了一项测试，结果显示，攻击者倾向于在几分钟内发现并利用在GitHub和DockerHub上泄露的AWS访问密钥，而在PyPI、Pastebin和Postman社区上暴露的密钥则在几小时内被利用。

### 3. 新型恶意软件能利用LogoFAIL漏洞感染Linux系统

韩国Best of the Best （BoB） 培训计划的网络安全学生利用 LogoFAIL 漏洞创建了新型恶意软件Bootkitty，能够攻击Linux系统设备。

### 4. 印度电信安全新规引发大量吐槽

印度电信监管机构推出了旨在保护国家关键基础设施网络免受网络威胁的规则，但专家表示，这些新指南对用户的基本隐私权保护不足。

### 5. 新型钓鱼工具包能让“菜鸟”轻松发动攻击

研究人员近日发出警告，称一种恶意电子邮件活动正利用名为 Rockstar 2FA 的网络钓鱼即服务（PhaaS）工具包窃取 Microsoft 365 用户帐户凭证。

## 安全事件

### 1. 因软件更新，丹麦第一电信运营商宕机超过24小时

近日，丹麦发生了一起大规模手机故障事件。丹麦电信运营商 TDC Net 遭遇大规模电信服务中断，导致所有用户无法使用移动电话、短信和网络接入服务，持续时间长达至少一天。

### 2. 损坏的Word钓鱼文件可以绕过微软安全防护

一种新型的网络钓鱼攻击利用了微软Word文件恢复功能，通过发送损坏的Word文档作为电子邮件附件，使它们能够因为损坏状态而绕过安全软件，但仍然可以被应用程序恢复。

### 3. 知名开源监控系统Zabbix存在SQL 注入漏洞

Zabbix 存在 SQL 注入漏洞（CVE-2024-42327），该漏洞是由于在 Zabbix前端的CUser类中的addRelatedObjects函数未对输入数据进行充分验证和转义，导致具有API访问权限的恶意用户可以通过user.get API传递特制输入触发SQL注入攻击，进而利用该漏洞实现权限提升或访问敏感数据。

### 4. 思科安全设备ASA十年老漏洞正在被利用

近期，思科系统公司（Cisco Systems）更新了关于CVE-2014-2120的安全公告，警告客户该漏洞已在野外被利用。CVE-2014-2120是一个影响思科自适应安全设备（ASA）软件的WebVPN登录页面的跨站脚本（XSS）漏洞。该漏洞最初于2014年披露，它允许未经身份验证的远程攻击者对WebVPN用户执行XSS攻击。

### 5. 立即修复，微软驱动程序关键漏洞已被APT组织利用

近日，微软被曝Windows AFD.sys漏洞（编号：CVE-2024-38193）正在被黑客组织利用。该漏洞被归类为自带易受攻击驱动程序（BYOVD）漏洞，可影响Windows套接字的注册I/O（RIO）扩展，并允许攻击者远程接管整个系统。

## 一周好文共读

### 1. AI 安全案例分享：我是如何控制劫持AI助手的

本文将详细分享作者是如何发现并利用这一漏洞的过程，以及这一漏洞可能带来的严重影响。希望通过作者的经历，能够帮助大家更好地理解AI安全的重要性，并采取有效的防护措施。 【[阅读全文](https://www.freebuf.com/articles/web/415632.html)】

![1719383456_667bb5a05000ee7693c04.png](https://image.3001.net/images/20241206/1733471081_6752ab693f4fb40f4db64.png!small)

### 2. 企业安全 | 邮件安全建设实践

本文章将看看企业内邮件系统可能面临的安全风险以及如何保障企业内部邮件安全。  【[阅读全文](https://www.freebuf.com/articles/es/406387.html)】

![1](https://image.3001.net/images/20241206/1733471151_6752abaf41ac77ce74b39.jpg!small)

### 3. 信息系统全生命周期——总体方案

本文概述了软件或系统的生命周期贯穿从需求产生到最终报废的完整过程。 【[阅读全文](https://www.freebuf.com/consult/416109.html)】

![1719198198_6678e1f6016c872e387dd.png!small?1719198198682](https://image.3001.net/images/20241206/1733471234_6752ac027aa9572dca02f.jpg!small)

## 省心工具

### 1. MORF：一款轻量级移动端网络安全侦查框架

MORF是一款功能强大、轻量级且独立于平台的移动端网络安全工具，旨在帮助广大安全研究人员轻松识别和处理移动应用程序中的敏感信息。 【[阅读全文](https://www.freebuf.com/sectool/416461.html)】

![](https://image.3001.net/images/20241128/1732804244_67487e9432a399da8fd7f.png!small)

### 2. ExecutePeFromPngViaLNK：一款PE文件嵌入隐写工具

ExecutePeFromPngViaLNK是一款针对PE文件和LNK文件的安全测试工具，该工具旨在使用LNK 文件提取并执行嵌入在 PNG 文件中的 PE。 【[阅读全文](https://www.freebuf.com/sectool/416466.html)】

![](https://image.3001.net/images/20241128/1732808070_67488d865eba52b9a578c.png!small)

### 3. Grove：一款软件即服务型安全日志收集框架

Grove是一款软件即服务型（SaaS）安全日志收集框架，旨在帮助广大安全分析人员从不支持日志流的服务中收集安全日志等数据。 【[阅读全文](https://www.freebuf.com/sectool/416531.html)】

![](https://image.3001.net/images/20241129/1732861135_67495ccf68243ed1e7b76.png!small)

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

热点资讯

* 1. 因涉嫌实施侵入性的监控行为，苹果公司在加州被员工起诉
* 2. 只需几分钟，AWS密钥泄露即可被利用
* 3. 新型恶意软件能利用LogoFAIL漏洞感染Linux系统
* 4. 印度电信安全新规引发大量吐槽
* 5. 新型钓鱼工具包能让“菜鸟”轻松发动攻击

安全事件

* 1. 因软件更新，丹麦第一电信运营商宕机超过24小时
* 2. 损坏的Word钓鱼文件可以绕过微软安全防护
* 3. 知名开源监控系统Zabbix存在SQL 注入漏洞
* 4. 思科安全设备ASA十年老漏洞正在被利用
* 5. 立即修复，微软驱动程序关键漏洞已被APT组织利用

一周好文共读

* 1. AI 安全案例分享：我是如何控制劫持AI助手的
* 2. 企业安全 | 邮件安全建设实践
* 3. 信息系统全生命周期——总体方案

省心工具

* 1. MORF：一款轻量级移动端网络安全侦查框架
* 2. ExecutePeFromPngViaLNK：一款PE文件嵌入隐写工具
* 3. Grove：一款软件即服务型安全日志收集框架

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