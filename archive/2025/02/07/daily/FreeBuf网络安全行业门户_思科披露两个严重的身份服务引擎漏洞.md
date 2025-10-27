---
title: 思科披露两个严重的身份服务引擎漏洞
url: https://www.freebuf.com/articles/421143.html
source: FreeBuf网络安全行业门户
date: 2025-02-07
fetch_date: 2025-10-06T20:37:00.111529
---

# 思科披露两个严重的身份服务引擎漏洞

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

思科披露两个严重的身份服务引擎漏洞

* ![]()
* 关注

思科披露两个严重的身份服务引擎漏洞

2025-02-06 13:57:05

所属地 上海

![](https://image.3001.net/images/20250206/1738821272_67a44e980da8611a30435.jpg!small)

思科公司披露了其身份服务引擎（ISE）软件中的两个关键漏洞，CVE-2025-20124和CVE-2025-20125，CVSS评分分别为9.9和9.1，严重性评级极高。这两个漏洞可能允许已认证的攻击者执行以下操作：远程任意命令执行、系统权限提升以及配置参数篡改。

截至目前，思科产品安全事件响应团队（PSIRT）尚未发现这些漏洞被公开利用或恶意使用的证据。但这些关键漏洞的发现进一步强调了，在企业环境中保持软件更新以及保护管理权限凭证的重要性。

## 漏洞技术细节

### 1. CVE-2025-20124 反序列化漏洞

* **成因：**API 接口对 Java 字节流反序列化处理不当
* **攻击条件：**攻击者需持有有效只读管理员凭证
* **攻击方式：**通过 API 发送恶意序列化 Java 对象
* **影响：**获得 root 权限执行任意命令，从而可能完全控制整个设备

### 2. CVE-2025-20125 权限绕过漏洞

* **成因：**API 授权机制缺陷 + 用户输入验证不足
* **攻击方式：**向易受攻击的API发送精心构造的HTTP请求
* **攻击效果：**窃取敏感信息、修改系统配置、强制节点重启

两个漏洞都要求攻击者具备有效的只读管理凭证，这也强调了保护此类账户的重要性。

## 受影响的产品以及解决方案

这些漏洞影响思科ISE和思科ISE被动身份连接器（ISE-PIC），无论设备配置如何。具体受影响的软件版本包括3.0、3.1、3.2和3.3，已确认3.4版本不受影响。

* **3.1版本：**在3.1P10版本中修复
* **3.2版本：**在3.2P7版本中修复
* **3.3版本：**在3.3P4版本中修复

思科已经发布了免费的软件更新以解决这些漏洞，由于没有可用的临时解决方案，思科建议所有受影响用户立即升级系统，以降低潜在利用风险。

**参考来源：**

> [https://cybersecuritynews.com/cisco-ise-vulnerabilities-arbitrary-command/﻿](https://cybersecuritynews.com/cisco-ise-vulnerabilities-arbitrary-command/)

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

漏洞技术细节

* 1. CVE-2025-20124 反序列化漏洞
* 2. CVE-2025-20125 权限绕过漏洞

受影响的产品以及解决方案

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