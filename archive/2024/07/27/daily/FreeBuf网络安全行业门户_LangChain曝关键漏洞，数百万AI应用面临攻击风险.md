---
title: LangChain曝关键漏洞，数百万AI应用面临攻击风险
url: https://www.freebuf.com/news/407063.html
source: FreeBuf网络安全行业门户
date: 2024-07-27
fetch_date: 2025-10-06T17:42:54.125275
---

# LangChain曝关键漏洞，数百万AI应用面临攻击风险

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

LangChain曝关键漏洞，数百万AI应用面临攻击风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

LangChain曝关键漏洞，数百万AI应用面临攻击风险

2024-07-26 11:14:18

所属地 上海

LangChain是一个流行的开源生成式人工智能框架，其官网介绍，有超过一百万名开发者使用LangChain框架来开发大型语言模型（LLM）应用程序。LangChain的合作伙伴包括云计算、人工智能、数据库和其他技术开发领域的许多知名企业。

![面向初学者的 5 个最佳 Langchain 教程：学习 Langchain 的综合指南](https://image.3001.net/images/20240726/1721963807_66a3151f95795e3c2ee58.jpg!small)

近日，来自Palo Alto Networks的研究人员详细描述了LangChain中的两个重大安全漏洞。

这些漏洞被识别为CVE-2023-46229和CVE-2023-44467，它们有可能允许攻击者执行任意代码和访问敏感数据。鉴于有一百多万名开发者依赖LangChain，这一发现给众多AI驱动的应用程序带来了重大安全风险。

## CVE-2023-46229：服务器端请求伪造（SSRF）

在LangChain 0.0.317之前的版本中，存在一个通过精心设计的站点地图实现的SSRF漏洞。利用该漏洞，攻击者可以从内网获取敏感信息，并可能绕过访问控制。Palo Alto Networks在2023年10月13日发现了这一问题，并立即通知了LangChain团队。该漏洞已在版本0.0.317中通过拉取请求langchain#11925得到修复。

![](https://image.3001.net/images/20240726/1721976574_66a346fe93f8f154d6008.png!small)

## CVE-2023-44467：LangChain实验版中的严重提示注入漏洞

CVE-2023-44467是一个严重提示注入漏洞，影响0.0.306之前的LangChain实验版本。LangChain实验版是一个专为研究和试验而设计的Python库，包含可能被恶意提示利用的集成。这个漏洞影响了PALChain功能，这是一个通过程序辅助语言模型（PAL）增强语言模型生成代码解决方案的能力的功能。

该漏洞允许攻击者利用PALChain的处理能力进行提示注入，使他们能够执行有害的命令或代码。这种利用可能导致未经授权的访问或操纵，带来重大的安全风险。Palo Alto Networks在2023年9月1日识别出这一问题，并及时通知了LangChain开发团队，后者在第二天在LangChain实验PyPI页面上发布了警告。

随着对大型语言模型（LLM）应用需求的增加，LangChain的受欢迎程度在最近几个月急剧上升。其丰富的预构建组件和集成库使其成为开发者的首选工具。然而，这种广泛的应用也意味着这些漏洞的潜在影响被放大。

Palo Alto Networks的研究人员强烈建议使用LangChain的开发者和组织将LangChain更新到最新的修补版本，以确保应用安全。

参考来源：https://securityonline.info/critical-flaws-in-langchain-expose-millions-of-ai-apps-to-attack/

# SSRF # 人工智能 # SSRF漏洞

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

CVE-2023-46229：服务器端请求伪造（SSRF）

CVE-2023-44467：LangChain实验版中的严重提示注入漏洞

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