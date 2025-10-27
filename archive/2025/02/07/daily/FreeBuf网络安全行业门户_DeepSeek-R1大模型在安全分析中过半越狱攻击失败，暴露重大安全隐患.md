---
title: DeepSeek-R1大模型在安全分析中过半越狱攻击失败，暴露重大安全隐患
url: https://www.freebuf.com/news/421179.html
source: FreeBuf网络安全行业门户
date: 2025-02-07
fetch_date: 2025-10-06T20:36:57.865414
---

# DeepSeek-R1大模型在安全分析中过半越狱攻击失败，暴露重大安全隐患

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

DeepSeek-R1大模型在安全分析中过半越狱攻击失败，暴露重大安全隐患

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

DeepSeek-R1大模型在安全分析中过半越狱攻击失败，暴露重大安全隐患

2025-02-06 16:16:29

所属地 上海

![image](https://image.3001.net/images/20250207/1738861469513670_7f38a68621b24c6cb1ce2a7c4198134a.png!small)

近日，基于云的网络安全、合规性和漏洞管理解决方案提供商Qualys对**DeepSeek AI**的蒸馏版DeepSeek-R1 LLaMA 8B变体进行了安全分析，揭示了其关键的安全和合规性问题。研究人员表示，该模型在使用Qualys TotalAI（一个专为AI安全评估设计的平台）进行的安全测试中，表现不佳，未能通过大部分测试。

## 测试范围与结果

Qualys TotalAI的知识库分析涉及对大语言模型（LLM）在16个类别中的响应进行评估，包括争议话题、过度代理、事实不一致、骚扰、仇恨言论、非法活动、法律信息、错位、过度依赖、隐私攻击、亵渎、自残、敏感信息泄露、色情内容、不道德行为以及暴力/不安全行为等。根据Qualys与Hackread.com分享的**研究**，该模型在多个领域表现出弱点，尤其在错位测试中表现较差。

越狱攻击是指通过技术手段绕过LLM的安全机制，可能导致有害输出。Qualys TotalAI测试了18种不同的越狱攻击类型，包括AntiGPT、基于分析的攻击（ABJ）、DevMode2、PersonGPT、始终越狱提示（AJP）、邪恶知己、伪装与重建（DRA）以及Fire等。总共进行了885次越狱测试和891次知识库评估，测试规模相当全面。结果显示，该模型在61%的知识库测试和58%的越狱攻击中失败。

## 不同攻击类型的脆弱性

Qualys的详细数据显示，该模型对不同越狱技术的抵抗能力存在显著差异。例如，尽管整体越狱失败率为58%（513次失败测试），但该模型对某些攻击（如Titanius、AJP、Caloz、JonesAI、Fire）的抵抗力较弱，而对其他攻击（如Ucar、Theta、AntiGPT、Clyde）则相对较强。然而，其高失败率表明该模型极易受到对抗性操纵，有时会生成有害活动的指令、制造仇恨言论内容、宣扬阴谋论并提供错误的医疗信息。

## 合规性与隐私问题

研究人员还发现，该模型存在显著的合规性挑战。其隐私政策指出，用户数据存储在中国的服务器上，这引发了关于政府数据访问、与国际数据保护法规（如GDPR和CCPA）的潜在冲突以及数据治理实践模糊性的担忧。这可能对受严格数据保护法律约束的组织产生影响。

值得注意的是，在DeepSeek AI发布后不久，Hackread.com**报道**称，Wiz Research发现DeepSeek AI暴露了超过100万条聊天记录，包括敏感的用户交互和认证密钥，凸显了其数据保护措施的不足。

## 企业应用的风险与建议

鉴于DeepSeek-R1在知识库攻击和越狱操作中的高失败率，现阶段企业采用该模型存在较大风险。因此，制定全面的安全策略，包括漏洞管理和遵守数据保护法规，对于确保无风险、负责任的AI应用至关重要。

Qualys研究人员在与Hackread.com分享的博客文章中表示：“保护AI环境需要进行结构化的风险和漏洞评估——不仅针对托管这些AI管道的基础设施，还包括引入新安全挑战的新兴编排框架和推理引擎。”

---

通过以上分析可以看出，DeepSeek-R1大模型在安全性和合规性方面存在显著问题，企业需谨慎评估其应用风险，并采取相应的安全措施。

**参考来源：**

> [DeepSeek-R1 LLM Fails Over Half of Jailbreak Attacks in Security Analysis](https://hackread.com/deepseek-r1-llm-fail-jailbreak-attack-security-analysis/)

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

测试范围与结果

不同攻击类型的脆弱性

合规性与隐私问题

企业应用的风险与建议

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