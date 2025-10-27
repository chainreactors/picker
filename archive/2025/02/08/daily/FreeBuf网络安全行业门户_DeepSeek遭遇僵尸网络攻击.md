---
title: DeepSeek遭遇僵尸网络攻击
url: https://www.freebuf.com/news/421199.html
source: FreeBuf网络安全行业门户
date: 2025-02-08
fetch_date: 2025-10-06T20:37:38.042550
---

# DeepSeek遭遇僵尸网络攻击

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

DeepSeek遭遇僵尸网络攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

DeepSeek遭遇僵尸网络攻击

2025-02-07 10:45:00

所属地 上海

![](https://image.3001.net/images/20250207/1738901361_67a58771190909ca57ce2.jpg!small)

2025年1月20日，DeepSeek发布了首款人工智能模型DeepSeek-R1，火爆全球，但随后DeepSeek遭遇了严重的网络攻击，导致运营中断，新用户注册也被延迟。

此次攻击涉及HailBot和RapperBot僵尸网络，引发了科技行业对网络威胁日益复杂化的警觉。

## DeepSeek的迅速崛起

DeepSeek成立于2023年底，凭借DeepSeek-R1模型迅速在全球范围内受到关注。该模型的性能与OpenAI的ChatGPT相当，但成本不到600万美元。通过使用相对落后的芯片，DeepSeek将运营成本降低了近50倍。

此外，将AI模型开源的决定，也进一步扩大了DeepSeek的影响力和用户基础，发布后几天内就有数百万次应用下载。然而，这种快速的崛起也使其成为了网络犯罪分子的目标。

## 网络攻击的时间线

对深思的攻击始于1月初，并在1月底显著升级。以下是详细的时间线：

* **1月27日：**DeepSeek宣布由于“规模庞大的恶意攻击”暂停新用户注册。
* **1月28日：**网络安全公司Wiz.io报告称，与DeepSeek相关的ClickHouse数据库被泄露。该数据库包含用户敏感信息，包括聊天记录和API密钥。然而，此次泄露被认为与正在进行的攻击无关。
* **1月29日：**《环球时报》披露，自1月初以来，DeepSeek一直遭受定期的分布式拒绝服务（DDoS）攻击。这些攻击利用了反射放大技术，并伴随着来自美国IP地址的HTTP代理攻击和暴力破解尝试。
* **1月30日：**XLab的报告揭示，HailBot和RapperBot这两种Mirai僵尸网络变体是最新一波攻击的幕后黑手。这些僵尸网络利用16个命令与控制（C2）服务器和超过100个C2端口发动了协同攻击。

## 攻击背后的僵尸网络

根据ANY.RUN的报告，扰乱DeepSeek运营的两个僵尸网络，是Mirai僵尸网络的高级变种。

* **HailBot：**HailBot专注于DDoS攻击，并利用华为设备中的CVE-2017-17215等漏洞。通过入侵大量设备，HailBot能够发动大规模拒绝服务攻击。
* **RapperBot：**RapperBot通过SSH暴力破解攻击传播，其标识为“SSH-2.0-HELLOWORLD”。一旦入侵设备，它会通过替换SSH密钥并创建名为“suhelper”的超级用户账户来确保持续访问。此外，RapperBot还具备通过XMRig门罗币矿工进行加密货币挖掘的能力，能够在受感染的设备上挖矿。

## 带来的警示和启发

对DeepSeek的网络攻击揭示了依赖数字基础设施的公司所面临的风险。随着像HailBot和RapperBot这样的僵尸网络作为服务被提供，即使是技术能力有限的攻击者也能发动毁灭性的攻击。对于像DeepSeek这样的AI驱动型企业来说，此类干扰可能导致服务中断、数据泄露以及客户信任的流失。

DeepSeek的遭遇展示了技术快速进步的潜力与风险。创新的人工智能模型颠覆了行业格局，也吸引了复杂的网络威胁来破坏取得的进步。随着网络安全专家进一步分析这些事件，全球各地的组织必须保持警惕，以应对不断演变的威胁。

**参考链接：**

> [https://cybersecuritynews.com/hail-and-rapper-botnet-is-the-mastermind-behind-the-deepseek-cyberattack/﻿](https://cybersecuritynews.com/hail-and-rapper-botnet-is-the-mastermind-behind-the-deepseek-cyberattack/)

# 数据安全

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

DeepSeek的迅速崛起

网络攻击的时间线

攻击背后的僵尸网络

带来的警示和启发

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