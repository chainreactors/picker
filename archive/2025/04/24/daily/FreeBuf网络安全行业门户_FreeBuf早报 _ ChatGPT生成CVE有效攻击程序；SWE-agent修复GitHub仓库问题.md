---
title: FreeBuf早报 | ChatGPT生成CVE有效攻击程序；SWE-agent修复GitHub仓库问题
url: https://www.freebuf.com/news/428451.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:55.432936
---

# FreeBuf早报 | ChatGPT生成CVE有效攻击程序；SWE-agent修复GitHub仓库问题

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

FreeBuf早报 | ChatGPT生成CVE有效攻击程序；SWE-agent修复GitHub仓库问题

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBuf早报 | ChatGPT生成CVE有效攻击程序；SWE-agent修复GitHub仓库问题

2025-04-23 16:20:00

## 全球网安事件速递

### 1. ChatGPT在公开漏洞利用代码发布前成功生成CVE有效攻击程序

AI成功生成高危漏洞攻击程序，改写网络安全格局。GPT-4仅凭CVE描述即完成代码分析、漏洞定位、攻击编写及调试全过程，大幅缩短漏洞利用开发时间。这一突破既提升研究效率，也加剧安全风险，迫使组织加速补丁部署。【[外刊-阅读原文](https://cybersecuritynews.com/chatgpt-creates-working-exploit-for-cves/)】

### 2. SWE-agent：开源工具利用大语言模型修复GitHub仓库问题

SWE-agent开源工具连接GPT-4o等语言模型与实用工具，可自主修复GitHub错误、解决网络安全问题。其EnIGMA模式专攻攻防任务，整合调试器等工具提升效率。设计简洁灵活，适配性强，已在GitHub免费提供。【[外刊-阅读原文](https://www.helpnetsecurity.com/2025/04/23/swe-agent-llm-fix-issues-github-repositories/)】

### 3. 三星One UI安全漏洞：剪贴板数据明文存储且永不过期

三星One UI系统存在重大安全漏洞，剪贴板数据以明文永久存储，包括密码等敏感信息，且无自动删除机制。攻击者可轻易获取数据，建议手动清除或使用自动填充功能。该问题多年未解决，引发用户强烈担忧。【[外刊-阅读原文](https://cybersecuritynews.com/samsung-one-ui-security-flaw/)】

### 4. "Cookie-Bite"攻击手法可绕过多重验证并维持持久访问权限

网络安全研究人员发现"Cookie-Bite"攻击技术，通过窃取浏览器cookie绕过MFA保护，持久访问云环境。攻击者利用中间人攻击、恶意扩展等手段窃取会话令牌，无需凭证即可冒充用户。建议企业监控异常行为、限制浏览器扩展并部署令牌保护机制应对威胁。【[外刊-阅读原文](https://cybersecuritynews.com/cookie-bite-attack/)】

### 5. 伪装成Alpine Quest的恶意地图应用被曝监控俄军动向

伪造Alpine Quest应用植入间谍软件，窃取俄军定位数据、通讯录及文件。通过Telegram传播，伪装为"专业版"，可远程扩展功能。建议避免非官方渠道下载，警惕模块化恶意软件。幕后组织尚未确认。【[外刊-阅读原文](https://hackread.com/fake-alpine-quest-mapping-app-spying-russian-military/)】

### 6. GCP Cloud Composer漏洞允许攻击者通过恶意PyPI包提升权限

Google云平台修复高危漏洞ConfusedComposer，攻击者可利用Cloud Composer编辑权限提升至Cloud Build账户，窃取数据或部署后门。Azure和AWS近期也曝出漏洞，均已被修复。云服务间交互权限问题需持续关注。【[外刊-阅读原文](https://thehackernews.com/2025/04/gcp-cloud-composer-bug-let-attackers.html)】

### 7. 网络钓鱼者利用Google Sites和DKIM重放攻击发送签名邮件窃取凭证

黑客利用谷歌Sites和DKIM重放攻击发送伪造签名邮件，诱导受害者点击钓鱼链接窃取凭证。攻击通过谷歌OAuth应用触发真实安全警报邮件，保留DKIM签名后转发，完美绕过验证。谷歌已修复漏洞，建议用户启用双重认证防范。【[外刊-阅读原文](https://thehackernews.com/2025/04/phishers-exploit-google-sites-and-dkim.html)】

### 8. 黑客滥用Cloudflare隧道基础设施传播多种远程访问木马

黑客利用Cloudflare隧道分发多种RAT，通过钓鱼邮件伪装发票文件感染系统，采用复杂多阶段技术绕过检测，最终建立持久远程访问。安全厂商警告其持续演变威胁全球组织。【[外刊-阅读原文](https://cybersecuritynews.com/hackers-abuse-cloudflare-tunnel-infrastructure/)】

### 9. YouTube的阴暗面：恶意链接、钓鱼攻击与深度伪造——网络安全视角

YouTube诈骗手段多样，包括恶意链接、钓鱼邮件、深度伪造名人推广虚假加密货币等，针对创作者和普通用户。AI技术加剧了诈骗复杂性，平台面临法律与审核挑战。用户需警惕可疑链接、启用双重认证、核实合作方身份并及时举报诈骗。【[外刊-阅读原文](https://www.helpnetsecurity.com/2025/04/23/most-common-youtube-scams/)】

### 10. 谷歌云Composer漏洞允许攻击者提升权限

谷歌云平台(GCP)的Cloud Composer服务存在"ConfusedComposer"权限提升漏洞，攻击者可通过注入恶意PyPI包获取高权限服务账户控制权。谷歌已修复该漏洞，改用更安全的服务账户执行安装操作，并更新相关文档。【[外刊-阅读原文](https://cybersecuritynews.com/google-cloud-composer-vulnerability/)】

## 优质文章推荐

### 1. APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞

APISandbox靶场包含多个API漏洞场景，如平行越权、缓存投毒、GraphQL漏洞等，演示OWASP API Top 10漏洞。通过Docker部署环境，涵盖注入、越权、数据泄露等攻击手法，提供实战演练。免责声明强调仅限合法学习，禁止恶意利用。【[阅读原文](https://www.freebuf.com/articles/428164.html)】

### 2. Twitter最新接口浅析(非爬虫)

本文分析Twitter的GraphQL接口实现，探讨搜索参数、分页游标机制及高级搜索技巧，提供金融业务监测案例，强调合法合规使用技术。【[阅读原文](https://www.freebuf.com/articles/421784.html)】

### 3. CTF学习：PWN基础之栈溢出（BUUCTF）

文章总结了PWN（BUUCTF）中的栈溢出、格式化字符串漏洞等核心技巧，包括利用libc、retlibc、mprotect函数等方法，以及32位和64位基础脚本的构造。重点介绍了如何通过覆盖、修改值、利用后门函数等手段实现攻击，并提供了具体代码示例和解题思路。【[阅读原文](https://www.freebuf.com/articles/428076.html)】

## 漏洞情报精华

**1.金盘移动图书馆系统 tabShow 信息泄露漏洞**
**<https://xvi.vulbox.com/detail/1914877335904063488>**

**2.有人物联 USR-TCP232-304 弱口令漏洞**
**<https://xvi.vulbox.com/detail/1914868477957640192>**

**3.红帆HFOffice GetSelEmpID SQL注入漏洞**
**[https://xvi.vulbox.com/detail/1914930385951789056﻿](https://xvi.vulbox.com/detail/1914930385951789056)**

**\*本文内容收集自全球范围内的媒体与刊物，制作者对其完整性负责，但不对其真实性和有效性负责。**

**\*标明为【外刊】的内容主要来源为英语国家的媒体与刊物，部分内容需要注册原链接平台账号后方可阅读。**

# 资讯 # FreeBuf早报

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

全球网安事件速递

* 1. ChatGPT在公开漏洞利用代码发布前成功生成CVE有效攻击程序
* 2. SWE-agent：开源工具利用大语言模型修复GitHub仓库问题
* 3. 三星One UI安全漏洞：剪贴板数据明文存储且永不过期
* 4. "Cookie-Bite"攻击手法可绕过多重验证并维持持久访问权限
* 5. 伪装成Alpine Quest的恶意地图应用被曝监控俄军动向
* 6. GCP Cloud Composer漏洞允许攻击者通过恶意PyPI包提升权限
* 7. 网络钓鱼者利用Google Sites和DKIM重放攻击发送签名邮件窃取凭证
* 8. 黑客滥用Cloudflare隧道基础设施传播多种远程访问木马
* 9. YouTube的阴暗面：恶意链接、钓鱼攻击与深度伪造——网络安全视角
* 10. 谷歌云Composer漏洞允许攻击者提升权限

优质文章推荐

* 1. APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞
* 2. Twitter最新接口浅析(非爬虫)
* 3. CTF学习：PWN基础之栈溢出（BUUCTF）

漏洞情报精华

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