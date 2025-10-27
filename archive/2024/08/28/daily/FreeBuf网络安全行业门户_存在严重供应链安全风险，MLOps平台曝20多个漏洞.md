---
title: 存在严重供应链安全风险，MLOps平台曝20多个漏洞
url: https://www.freebuf.com/news/409541.html
source: FreeBuf网络安全行业门户
date: 2024-08-28
fetch_date: 2025-10-06T18:04:07.522958
---

# 存在严重供应链安全风险，MLOps平台曝20多个漏洞

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

存在严重供应链安全风险，MLOps平台曝20多个漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

存在严重供应链安全风险，MLOps平台曝20多个漏洞

2024-08-27 13:20:03

所属地 上海

网络安全研究人员警告称，在发现20多个漏洞后，机器学习（ML）软件供应链存在安全风险，这些漏洞可能被利用来针对MLOps平台。这些漏洞被描述为固有和实现方面的缺陷，可能会产生严重后果，从任意代码执行到加载恶意数据集。![](https://image.3001.net/images/20240827/1724735968_66cd61e0eab7f538061e1.png!small)

MLOps平台提供了设计和执行ML模型管道的能力，模型注册表作为存储和版本训练ML模型的存储库。然后可以将这些模型嵌入到应用程序中，或允许其他客户端使用API（即模型即服务）查询它们。

JFrog研究人员在一份详细报告中表示：“固有漏洞是由技术中所使用的底层格式和过程引起的。”固有漏洞的一些例子包括利用ML模型运行攻击者选择的代码，这是通过利用模型在加载时支持自动代码执行的事实（例如Pickle模型文件）。

这种行为也扩展到某些数据集格式和库，它们允许自动代码执行，从而在仅加载公开可用的数据集时就可能为恶意软件攻击敞开大门。另一个固有漏洞涉及JupyterLab（前身为Jupyter Notebook），这是一个基于Web的交互式计算环境，使用户能够执行代码块（或单元格）并查看相应的结果。

简单来说，攻击者可以输出恶意JavaScript代码，使其在当前JupyterLab笔记本中添加一个新单元格，将Python代码注入其中并执行它。特别是在利用跨站脚本（XSS）漏洞的情况下，这一点尤其明显。JFrog表示，它发现了一个MLFlow的XSS漏洞（CVE-2024-27132，CVSS评分：7.5），可导致在JupyterLab中执行客户端代码。

研究人员说：“我们从这项研究中的一个主要收获是，我们需要将ML库中的所有XSS漏洞视为潜在的任意代码执行，因为用户可能会将这些ML库与Jupyter Notebook一起使用。”

第二类漏洞涉及实现弱点，例如MLOps平台中缺乏身份验证，可能会允许具有网络访问权限的威胁行为者通过滥用ML管道功能获得代码执行能力。这些威胁并非理论上的，以经济利益为动机的对手可能滥用这些漏洞，如在未打补丁的Anyscale Ray（CVE-2023-48022，CVSS评分：9.8）的情况下，部署加密货币矿工。

第二种实现漏洞是针对Seldon Core的容器逃逸，使攻击者能够超越代码执行，在云环境中横向移动并访问其他用户的模型和数据集，方法是将恶意模型上传到推理服务器。它们不仅可以被武器化，在组织内部渗透、传播，还可以威胁服务器。

Palo Alto Networks Unit 42详细说明了开源LangChain生成式AI框架中的两个现已修复的漏洞（CVE-2023-46229和CVE-2023-44467），这两个漏洞可能允许攻击者执行任意代码和访问敏感数据。

上个月，Trail of Bits还揭示了Ask Astro中的四个问题，这是一个检索增强生成（RAG）开源聊天机器人应用程序，可能导致聊天机器人输出中毒、文档摄取不准确和潜在的拒绝服务（DoS）。

正如安全问题在人工智能驱动的应用程序中被暴露出来一样，人们也在设计技术来用最终目标欺骗大型语言模型（LLMs）产生易受攻击的代码来毒害训练数据集。

康涅狄格大学的一位学者表示：“与最近将恶意负载嵌入代码的可检测或不相关部分的攻击不同，CodeBreaker利用LLMs（例如GPT-4）进行复杂的负载转换（不影响功能），确保微调的毒害数据和生成的代码都可以规避强大的漏洞检测。”

参考来源：<https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html>

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