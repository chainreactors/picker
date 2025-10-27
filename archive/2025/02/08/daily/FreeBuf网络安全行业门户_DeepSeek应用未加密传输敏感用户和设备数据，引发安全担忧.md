---
title: DeepSeek应用未加密传输敏感用户和设备数据，引发安全担忧
url: https://www.freebuf.com/news/421239.html
source: FreeBuf网络安全行业门户
date: 2025-02-08
fetch_date: 2025-10-06T20:37:33.162824
---

# DeepSeek应用未加密传输敏感用户和设备数据，引发安全担忧

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

DeepSeek应用未加密传输敏感用户和设备数据，引发安全担忧

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)
* [数据安全](https://www.freebuf.com/articles/database)

DeepSeek应用未加密传输敏感用户和设备数据，引发安全担忧

2025-02-07 20:28:00

所属地 上海

![image](https://image.3001.net/images/20250208/1738951375879868_8dda2f98ec9e41dc88d41b1050212f16.png!small)

近日，针对DeepSeek在苹果iOS操作系统上的移动应用进行的一项新审计发现了严重的安全问题，其中最突出的是该应用在未加密的情况下通过互联网传输敏感数据，使其容易受到拦截和篡改攻击。

## 未加密传输与数据收集问题

此次评估由NowSecure进行，该公司还发现该应用未能遵循最佳安全实践，并收集了大量用户和设备数据。NowSecure表示：“DeepSeek iOS应用通过互联网传输部分移动应用注册和设备数据时未进行加密，这使得互联网流量中的任何数据都容易受到被动和主动攻击。”

此外，审计还揭示了在用户数据加密方面的几个实施弱点，包括使用不安全的对称加密算法（3DES）、硬编码的加密密钥以及初始化向量的重复使用。

## 数据流向与安全防护缺失

这些数据被发送到由字节跳动（ByteDance）旗下的云计算和存储平台“火山引擎”管理的服务器。字节跳动也是TikTok的母公司。NowSecure指出：“DeepSeek iOS应用全局禁用了应用传输安全（ATS），这是iOS平台的一项保护措施，旨在防止敏感数据通过未加密的通道传输。由于此保护被禁用，该应用可以通过互联网发送未加密的数据。”

这些发现进一步加剧了人们对这款人工智能（AI）聊天机器人服务的担忧。尽管DeepSeek在全球多个市场的Android和iOS应用商店排行榜上迅速攀升，但其安全问题却引发了广泛关注。

![image](https://image.3001.net/images/20250208/1738951378535886_601536be93a348dcac155a2aa9b1988a.png!small)

## 威胁行为者利用AI技术

网络安全公司Check Point表示，已观察到威胁行为者利用DeepSeek、阿里巴巴的Qwen以及OpenAI的ChatGPT等AI引擎开发信息窃取工具、生成未经审查或不受限制的内容，并优化大规模垃圾邮件分发的脚本。该公司强调：“随着威胁行为者利用越狱等先进技术绕过保护措施并开发信息窃取工具、金融盗窃和垃圾邮件分发，组织迫切需要实施主动防御，以应对这些不断演变的威胁，确保对AI技术潜在滥用的强大防御。”

## 国际禁令与恶意攻击

本周早些时候，美联社透露，DeepSeek的网站配置为将用户登录信息发送给中国移动，这家国有电信公司已被禁止在美国运营。与TikTok类似，DeepSeek的中国背景促使美国立法者推动在全国范围内禁止政府设备使用该应用。

包括澳大利亚、意大利、荷兰、韩国在内的多个国家，以及印度和美国的部分政府机构（如国会、NASA、海军、五角大楼和德克萨斯州）已禁止在政府设备上使用DeepSeek。

## 恶意攻击与仿冒页面

DeepSeek的迅速流行也使其成为恶意攻击的目标。中国网络安全公司XLab告诉《环球时报》，该服务在上个月底遭受了来自Mirai僵尸网络hailBot和RapperBot的持续分布式拒绝服务（DDoS）攻击。与此同时，网络犯罪分子正利用DeepSeek的热潮，迅速建立仿冒页面，传播恶意软件、虚假投资骗局和欺诈性加密货币计划。

**参考来源：**

> <https://thehackernews.com/2025/02/deepseek-app-transmits-sensitive-user.html>

# 数据安全 # 移动安全

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

未加密传输与数据收集问题

数据流向与安全防护缺失

威胁行为者利用AI技术

国际禁令与恶意攻击

恶意攻击与仿冒页面

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