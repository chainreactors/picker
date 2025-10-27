---
title: Ivanti VPN 零日漏洞正在被黑客利用
url: https://www.freebuf.com/news/419390.html
source: FreeBuf网络安全行业门户
date: 2025-01-10
fetch_date: 2025-10-06T20:08:35.646759
---

# Ivanti VPN 零日漏洞正在被黑客利用

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

Ivanti VPN 零日漏洞正在被黑客利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Ivanti VPN 零日漏洞正在被黑客利用

2025-01-09 14:36:10

所属地 上海

Ivanti 公开披露了影响 Connect Secure (ICS) VPN 设备的两个关键漏洞： CVE-2025-0282 和 CVE-2025-0283。

![](https://image.3001.net/images/20250109/1736404481_677f6e01c041f9c2eda64.jpg!small)

网络安全公司 Mandiant 的报告称，CVE-2025-0282 零日漏洞利用活动开始于 2024 年 12 月中旬。这一漏洞的利用引发了人们对潜在网络漏洞以及受影响组织后续损害的担忧。

比较而言，CVE-2025-0282 是两个漏洞中更为严重的一个，被描述为未经身份验证的基于栈的缓冲区溢出漏洞。

利用该漏洞，攻击者无需身份验证即可实现远程代码执行，从而为他们在受感染的网络中部署恶意软件或进行进一步攻击提供立足点。

CVE-2025-0283 的信息尚未完全披露，但同样被认为是关键漏洞。

Mandiant 的持续调查表明，CVE-2025-0282 正在被利用于针对多个组织的定向攻击活动中。

攻击者在发起攻击前展示了探测 ICS 设备版本的高超技术，特别是针对特定软件版本中的漏洞进行攻击。

Mandiant 观察到威胁行为者利用了一系列恶意软件家族，包括已知的 SPAWN 生态系统（SPAWNANT 安装程序、 SPAWNMOLE 隧道工具和 SPAWNSNAIL SSH 后门）。

在受感染的设备中还识别出了两个新的恶意软件家族：DRYHOOK 和 PHASEJAM。

## **攻击技术和持久化方法**

攻击者在利用 CVE-2025-0282 时典型的攻击步骤包括禁用 SELinux 等安全功能、写入恶意脚本、部署 Web Shell 以及篡改系统日志以隐藏入侵痕迹。

特别令人担忧的是，攻击者植入了在系统升级后仍然能够存活的持久化恶意软件组件，确保即使系统被修补，攻击者仍能保持访问权限。

分析还揭示了攻击者在 ICS 软件组件中部署了 Web Shell，以实现远程访问和代码执行。

例如，PHASEJAM 恶意软件会劫持系统升级过程，利用基于 HTML 的虚假升级进度条，从视觉上让管理员误以为升级正在进行。实际上，恶意行为者会悄悄阻止合法升级，确保系统仍然受到入侵威胁，同时保持攻击不被发现。

另一种恶意软件 SPAWNANT 则通过将自身嵌入系统文件来确保升级过程中的持久性。

在漏洞利用后，还观察到威胁行为者从设备的多个关键区域删除了入侵证据：

* 使用 dmesg 清除内核消息，并从调试日志中删除漏洞利用期间生成的条目
* 删除故障排除信息包（状态转储）以及进程崩溃生成的任何核心转储
* 删除与系统日志故障、内部 ICT 故障、崩溃痕迹和证书处理错误相关的应用程序事件日志条目
* 从 SELinux 审计日志中删除已执行的命令

## **幕后黑手是谁？**

Ivanti 和 Mandiant 认为此次攻击活动带有间谍活动的痕迹。

受感染的 ICS 设备数据库缓存已多次被泄露，这引发了人们对暴露的 VPN 会话数据、 API 密钥、凭证和证书的担忧。

网络安全专家警告称，如果这些漏洞的概念验证利用代码被公开，可能会吸引更多威胁行为者参与，从而导致攻击的范围扩大。

## **Ivanti 对零日漏洞的响应**

Ivanti 正在处理零日漏洞 CVE-2025-0282 和 CVE-2025-0283，这两个漏洞影响了 Ivanti Connect Secure 、Policy Secure 以及 Neurons for ZTA 网关。

修复程序可以通过下载门户获取。

**参考来源：**<https://cybersecuritynews.com/active-exploitation-of-ivanti-vpn-0-day-vulnerability-cve-2025-0282/>

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

攻击技术和持久化方法

幕后黑手是谁？

Ivanti 对零日漏洞的响应

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