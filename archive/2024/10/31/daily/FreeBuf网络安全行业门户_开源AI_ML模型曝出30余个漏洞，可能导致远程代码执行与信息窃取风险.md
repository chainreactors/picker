---
title: 开源AI/ML模型曝出30余个漏洞，可能导致远程代码执行与信息窃取风险
url: https://www.freebuf.com/news/414008.html
source: FreeBuf网络安全行业门户
date: 2024-10-31
fetch_date: 2025-10-06T18:54:06.301658
---

# 开源AI/ML模型曝出30余个漏洞，可能导致远程代码执行与信息窃取风险

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

开源AI/ML模型曝出30余个漏洞，可能导致远程代码执行与信息窃取风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

开源AI/ML模型曝出30余个漏洞，可能导致远程代码执行与信息窃取风险

2024-10-30 10:11:45

所属地 上海

![1730256236_67219d6ccbeecfef603a0.png!small](https://image.3001.net/images/20241030/1730256236_67219d6ccbeecfef603a0.png!small)

根据最新消息，开源人工智能（AI）和机器学习（ML）模型中已披露了三十几个安全漏洞，其中一些漏洞可能导致远程代码执行和信息窃取。

在 ChuanhuChatGPT、Lunary 和 LocalAI 等工具中发现的这些漏洞已作为 Protect AI 的 Huntr 漏洞悬赏平台的一部分进行了报告。

其中最严重的漏洞是影响大型语言模型（LLM）生产工具包 Lunary 的两个漏洞：CVE-2024-7474 (CVE-2024-7474) 和 CVE-2024-7474（CVE-2024-7474）。

* **CVE-2024-7474（CVSS 得分：9.1）：**一个不安全的直接对象引用 (IDOR) 漏洞，可允许已通过身份验证的用户查看或删除外部用户，导致未经授权的数据访问和潜在的数据丢失
* **CVE-2024-7475 （CVSS 得分：9.1）：**访问控制不当漏洞，允许攻击者更新 SAML 配置，从而有可能以未经授权的用户身份登录并访问敏感信息。

在 Lunary 中还发现了另一个 IDOR 漏洞（CVE-2024-7473，CVSS 得分：7.5），该漏洞允许恶意行为者通过操纵用户控制参数来更新其他用户的提示。

Protect AI 在一份公告中解释道 ：攻击者以用户 A 的身份登录并拦截更新提示符的请求，通过将请求中的'id'参数修改为属于用户 B 的提示符的'id'，攻击者可以在未经授权的情况下更新用户 B 的提示符。

第三个严重漏洞涉及 ChuanhuChatGPT 用户上传功能中的路径遍历漏洞（CVE-2024-5982，CVSS 得分：9.1），该漏洞可能导致任意代码执行、目录创建和敏感数据暴露。

LocalAI是一个开源项目，允许用户运行自托管的LLM，该项目还发现了两个安全漏洞，可能允许恶意行为者通过上传恶意配置文件执行任意代码（CVE-2024-6983，CVSS评分：8.8），以及通过分析服务器的响应时间猜测有效的API密钥（CVE-2024-7010，CVSS评分：7.5）。

Protect AI 表示，该漏洞允许攻击者执行定时攻击，这是一种侧信道攻击，通过测量处理不同 API 密钥请求所需的时间，攻击者可以逐个字符推断出正确的 API 密钥。

此外，还有一个影响 Deep Java Library（DJL）的远程代码执行漏洞，该漏洞源于软件包的 untar 函数中的任意文件覆盖漏洞（CVE-2024-8396，CVSS 得分：7.8）。

该漏洞可能会导致代码执行和数据篡改。英伟达在发布补丁修复其NeMo生成式人工智能框架中的路径遍历漏洞（CVE-2024-0129，CVSS评分：6.3）的同时，也披露了这一漏洞。建议用户将其安装更新到最新版本，以确保其 AI/ML 供应链的安全并防范潜在攻击。

漏洞披露之前，Protect AI 还发布了开源 Python 静态代码分析器 Vulnhuntr，该分析器可利用 LLM 在 Python 代码库中查找零日漏洞。

Vulnhuntr 的工作原理是在不影响 LLM 上下文窗口（LLM 在单个聊天请求中可解析的信息量）的情况下，将代码分解成小块，从而标记出潜在的安全问题。

Dan McInerney 和 Marcello Salvati 说：它会自动在项目文件中搜索可能最先处理用户输入的文件。然后，它会摄取整个文件，并回复所有潜在漏洞。

利用这份潜在漏洞清单，它将继续完成从用户输入到服务器输出的整个函数调用链，对整个项目中的每个潜在漏洞逐个函数/类进行分析，直到它对整个调用链感到满意，才能进行最终分析。

撇开人工智能框架的安全漏洞不谈，Mozilla 的 0Day 调查网络（0Din）发布的一项新越狱技术发现，以十六进制格式和表情符号编码的恶意提示可用于绕过 OpenAI ChatGPT 的防护措施，并对已知的安全漏洞精心设计漏洞利用。

安全研究员马尔科-菲格罗亚（Marco Figueroa）说：越狱策略利用了语言漏洞，指示模型处理一项看似无害的任务：十六进制转换。由于该模型经过优化，可以遵循自然语言的指令，包括执行编码或解码任务，因此它本质上并没有意识到转换十六进制值可能会产生有害输出。

出现这一漏洞的原因是，语言模型被设计为按部就班地执行指令，但缺乏深入的上下文意识，无法在其最终目标的大背景下评估每个单独步骤的安全性。

> 参考来源：[Researchers Uncover Vulnerabilities in Open-Source AI and ML Models](https://thehackernews.com/2024/10/researchers-uncover-vulnerabilities-in.html)

# 安全漏洞 # 开源 # AI安全

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