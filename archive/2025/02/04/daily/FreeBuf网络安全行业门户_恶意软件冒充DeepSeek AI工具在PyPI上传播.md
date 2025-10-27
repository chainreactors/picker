---
title: 恶意软件冒充DeepSeek AI工具在PyPI上传播
url: https://www.freebuf.com/articles/421046.html
source: FreeBuf网络安全行业门户
date: 2025-02-04
fetch_date: 2025-10-06T20:38:52.403805
---

# 恶意软件冒充DeepSeek AI工具在PyPI上传播

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

恶意软件冒充DeepSeek AI工具在PyPI上传播

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

恶意软件冒充DeepSeek AI工具在PyPI上传播

2025-02-03 11:33:23

所属地 上海

![恶意人工智能](https://image.3001.net/images/20250204/1738602160656403_1d072c59d74a413fb417f3918dd9d9c0.jpg!small)

威胁行为者正利用DeepSeek日益增长的知名度，在Python包索引（PyPI）上推广两个恶意信息窃取软件包，这些软件包冒充了该AI平台的开发者工具。

这两个软件包分别命名为“deepseeek”和“deepseekai”，模仿了中国人工智能初创公司DeepSeek的名称。该公司开发的R1大型语言模型近期迅速走红。

有趣的是，这些软件包是由一个创建于2023年6月的“老”账户上传的，该账户此前没有任何活动记录。

## 恶意软件包窃取开发者数据

根据发现此次攻击并向PyPI报告的Positive Technologies研究人员，这些冒充DeepSeek AI Python客户端的软件包实际上是信息窃取工具，旨在从使用它们的开发者那里窃取数据。

一旦在开发者的机器上执行，恶意负载就会窃取用户和系统数据，以及环境变量，如API密钥、数据库凭证和基础设施访问令牌。

接下来，窃取的信息通过合法的自动化平台Pipedream，被传输到命令与控制（C2）服务器\_eoyyiyqubj7mquj.m.pipedream[.]net\_。

![恶意负载](https://image.3001.net/images/20250204/1738602161823668_babea4969421419e939871dc22937d9f.jpg!small)**两个软件包中的恶意负载**来源：Positive Technologies

威胁行为者可以利用这些窃取的信息访问开发者使用的云服务、数据库和其他受保护资源。

Positive Technologies的报告指出：“这些软件包中的功能旨在收集用户和计算机数据，并窃取环境变量。”

“当用户在命令行界面中运行deepseeek或deepseekai命令（取决于软件包）时，恶意负载就会被执行。”

“环境变量通常包含应用程序运行所需的敏感数据，例如S3存储服务的API密钥、数据库凭证以及访问其他基础设施资源的权限。”

## 多名开发者受害

恶意软件包deepseeek 0.0.8和deepseekai 0.0.8于2025年1月29日上传到PyPI，两者之间仅相隔20分钟。

![deepseeek 0.0.8 PyPI列表](https://image.3001.net/images/20250204/1738602162597008_639b3d4383b64d58809d7dd60228bd40.jpg!small)**deepseeek 0.0.8 PyPI列表**来源：Positive Technologies

Positive Technologies迅速发现并向PyPI报告了这些软件包，PyPI随后隔离并阻止了这些软件包的下载，最终将其从平台上彻底删除。

尽管检测和响应迅速，仍有222名开发者下载了这两个软件包，其中大部分来自美国（117人），其次是中国（36人）、俄罗斯、德国、香港和加拿大。

使用这些软件包的开发者应立即轮换其API密钥、身份验证令牌和密码，因为它们可能已被泄露。

此外，还应检查任何凭证被盗的云服务，以确认它们是否也受到了影响。

**参考来源：**

> [DeepSeek AI tools impersonated by infostealer malware on PyPI](https://www.bleepingcomputer.com/news/security/deepseek-ai-tools-impersonated-by-infostealer-malware-on-pypi/)

# 系统安全 # 数据安全

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

恶意软件包窃取开发者数据

多名开发者受害

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