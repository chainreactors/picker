---
title: Meta的Llama框架漏洞使AI系统面临远程代码执行风险
url: https://www.freebuf.com/vuls/420864.html
source: FreeBuf网络安全行业门户
date: 2025-01-27
fetch_date: 2025-10-06T20:08:25.825785
---

# Meta的Llama框架漏洞使AI系统面临远程代码执行风险

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

Meta的Llama框架漏洞使AI系统面临远程代码执行风险

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

Meta的Llama框架漏洞使AI系统面临远程代码执行风险

2025-01-26 15:45:00

所属地 上海

![image](https://image.3001.net/images/20250126/1737892856569821_eea71412e63049c0abf2ff8e2f83e73f.png!small)

Meta的Llama大型语言模型（LLM）框架中发现了一个高危安全漏洞，若被成功利用，攻击者可以在Llama堆栈推理服务器上执行任意代码。

该漏洞被标记为CVE-2024-50050，CVSS评分为6.3（满分10.0）。然而，供应链安全公司Snyk将其评为9.3分，属于严重级别。Oligo Security研究员Avi Lumelsky在本周的分析中指出：“受影响的meta-llama版本存在反序列化不可信数据的漏洞，这意味着攻击者可以通过发送恶意数据进行反序列化来执行任意代码。”

## Llama Stack组件中的远程代码执行漏洞

根据云安全公司的分析，该漏洞存在于Llama Stack组件中，该组件为人工智能（AI）应用开发定义了一组API接口，包括使用Meta自家的Llama模型。具体来说，漏洞与Python推理API实现中的远程代码执行缺陷有关，该实现被发现会自动使用pickle反序列化Python对象。pickle格式被认为存在风险，因为在使用该库加载不可信或恶意数据时，可能导致任意代码执行。

Lumelsky表示：“在ZeroMQ套接字暴露在网络中的情况下，攻击者可以通过向套接字发送精心构造的恶意对象来利用此漏洞。由于recv\_pyobj会反序列化这些对象，攻击者可以在主机上实现任意代码执行（RCE）。”

## Meta的修复措施与类似漏洞的警示

在2024年9月24日负责任披露后，Meta于10月10日在0.0.41版本中修复了该问题。此外，Python库pyzmq也进行了修复，该库提供了对ZeroMQ消息库的访问。Meta在一份公告中表示，通过将序列化格式从pickle切换为JSON，修复了与套接字通信相关的远程代码执行风险。

这并非AI框架中首次发现此类反序列化漏洞。2024年8月，Oligo详细介绍了TensorFlow的Keras框架中的一个“影子漏洞”，即CVE-2024-3660（CVSS评分：9.8）的绕过漏洞，该漏洞由于使用不安全的marshal模块可能导致任意代码执行。

## OpenAI ChatGPT爬虫的高危漏洞

与此同时，安全研究员Benjamin Flesch披露了OpenAI的ChatGPT爬虫中的一个高危漏洞，该漏洞可能被武器化，用于对任意网站发起分布式拒绝服务（DDoS）攻击。该问题源于对“chatgpt[.]com/backend-api/attributions”API的HTTP POST请求处理不当。该API设计用于接受URL列表作为输入，但既未检查列表中是否多次出现相同URL，也未对可传递的超链接数量进行限制。

![image](https://image.3001.net/images/20250126/1737892858159953_2217b08eb8a245c5a674c192d1f56154.png!small)

这为恶意行为者提供了一个场景：他们可以在单个HTTP请求中传输数千个超链接，导致OpenAI向目标站点发送所有请求，而不会尝试限制连接数量或防止重复请求。根据传输给OpenAI的超链接数量，这为潜在的DDoS攻击提供了显著的放大效应，有效耗尽目标站点的资源。OpenAI随后修复了该问题。

Flesch表示：“ChatGPT爬虫可以通过向不相关的ChatGPT API发送HTTP请求来触发对受害者网站的DDoS攻击。OpenAI软件中的这一缺陷将导致对毫无戒备的受害者网站发起DDoS攻击，利用ChatGPT爬虫运行的多个Microsoft Azure IP地址范围。”

## AI辅助编程工具的安全隐患

此外，Truffle Security的报告指出，流行的AI辅助编程工具“建议”硬编码API密钥和密码，这种危险的建议可能会误导缺乏经验的程序员，导致项目中引入安全漏洞。安全研究员Joe Leon表示：“LLM正在帮助延续这种不安全编码实践，可能是因为它们是在所有不安全编码实践的基础上训练的。”

## LLM框架漏洞的潜在威胁

LLM框架漏洞的消息紧随研究之后，这些研究表明模型可能被滥用以增强网络攻击生命周期，包括安装最终阶段的窃取载荷和命令控制。Deep Instinct研究员Mark Vaitzman表示：“LLM带来的网络威胁并非革命性的，而是进化性的。LLM只是使网络威胁更好、更快、更准确，规模更大。在经验丰富的攻击者指导下，LLM可以成功集成到攻击生命周期的每个阶段。随着底层技术的进步，这些能力可能会在自主性方面增长。”

## ShadowGenes：识别模型谱系的新方法

最近的研究还展示了一种名为ShadowGenes的新方法，该方法可用于通过利用其计算图识别模型谱系，包括其架构、类型和家族。该方法基于之前披露的名为ShadowLogic的攻击技术。AI安全公司HiddenLayer在一份声明中表示：“用于检测计算图中恶意攻击的签名可以适应跟踪和识别重复模式，称为重复子图，从而确定模型的架构谱系。了解组织中使用的模型家族可以提高对AI基础设施的整体认识，从而实现更好的安全态势管理。”

**参考来源：**

> [Meta's Llama Framework Flaw Exposes AI Systems to Remote Code Execution Risks](https://thehackernews.com/2025/01/metas-llama-framework-flaw-exposes-ai.html)

# 网络安全 # web安全

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