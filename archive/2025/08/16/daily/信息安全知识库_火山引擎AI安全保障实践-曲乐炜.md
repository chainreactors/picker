---
title: 火山引擎AI安全保障实践-曲乐炜
url: https://vipread.com/library/topic/4010
source: 信息安全知识库
date: 2025-08-16
fetch_date: 2025-10-07T00:12:41.321752
---

# 火山引擎AI安全保障实践-曲乐炜

[![logo](/static/logo_light.png)
![logo-dark](/static/logo_light.png)](/)

[VIPREAD 导航](/)

* [主页](/index)
* [书架](/library/category)
* [议题](/library/datas)
* [附件](/library/attachment)
* [成员](/library/authors)
* [搜索](/library/search)
* [**打赏**](/donate)
* [我要分享](/share/submit)

* [登录](/auth/login)
* [Dark](/setmode/black)

##### [主页](/) / [第16期“安全范儿”技术沙龙「LLM安全漏洞挖掘」专场](/library/cid/456) / 火山引擎AI安全保障实践-曲乐炜

![](https://archive1.vipread.com/covers/2025/08/topic/2_1755226259_351cbc4a.jpg)

* 标题

  [火山引擎AI安全保障实践-曲乐炜](/library/topic/4010)
* 作者

  曲乐炜@火山引擎
* 标签

  [AI安全](/library/tags/AI%E5%AE%89%E5%85%A8)
  [智能体](/library/tags/%E6%99%BA%E8%83%BD%E4%BD%93)
  [安全运营](/library/tags/%E5%AE%89%E5%85%A8%E8%BF%90%E8%90%A5)
  [安全保障](/library/tags/%E5%AE%89%E5%85%A8%E4%BF%9D%E9%9A%9C)
  [大模型](/library/tags/%E5%A4%A7%E6%A8%A1%E5%9E%8B)
* 简介

  这份文档详细介绍了火山引擎在AI领域的安全保障实践。首先，文档概述了火山引擎的AI业务架构，该架构涵盖了从底层AI基础设施（AI Infra）、大模型服务平台（MaaS）到智能体开发运维（Agent DevOps）和最终的AI智能体（AI Agent）应用的全方位服务。

  文档的核心部分阐述了火山引擎的AI安全保障方案，强调“安全是一切Agent的基础”。该方案构建了一个多层次的纵深防御体系，包括针对大语言模型（LLM）本身的提示词攻击防护、模型平台安全；针对Agent和工具的协议安全、沙箱防护；以及覆盖底层基础设施和平台治理的全面安全措施。

  文档重点分析了AI智能体场景中MCP（Model-as-a-Service Connector Protocol）面临的七大核心安全风险，例如传统的Web服务漏洞、工具描述投毒、间接提示词注入、恶意“地毯式骗局”（Rug Pull）以及企业数据安全风险等。

  为应对这些挑战，火山引擎设计了MCP安全架构。该架构包含三大核心策略：

  + 第一，严格的安全准入控制，确保所有接入MCP市场的服务都经过安全扫描和漏洞修复；
  + 第二，原生安全设计，针对多租户体验场景和单租户私有化部署场景，分别采用临时凭证隔离和VPC内部署等不同安全机制；
  + 第三，运行时安全防护，通过“大模型防火墙”和“AgentArmor”等工具，实时检测并拦截恶意输入和非预期行为，保障模型和智能体在运行过程中的安全。
* 援引

  https://mp.weixin.qq.com/s/u8vIFU\_TXIrXJ1EZOPBB4g
* 提示

  本站仅做资料的整理和索引,转载引用请注明出处

###### 相关推荐

* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1gcmtud0e9dj31080m5wlg.jpg)](/library/topic/2633)

  [大型互联网企业的数据安全攻](/library/topic/2633)

  2019-11-01 07:03:00
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1fyel641bvxj314t0nytg5.jpg)](/library/topic/2043)

  [人工智能的安全问题](/library/topic/2043)

  2018-11-24 11:05:00
* [![](https://archive1.vipread.com/covers/2021/12/topic/migration_3657_1638512009_05d625c0.jpg)](/library/topic/3657)

  [企业自建SOC安全运营的探](/library/topic/3657)

  2021-12-03 14:13:29.157617
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1gcmu5t0f4lj30v70lmjui.jpg)](/library/topic/2739)

  [论安全运营在医疗信息安全建](/library/topic/2739)

  2020-01-17 03:45:55

[![](https://archive1.vipread.com/images/ad/flag_3.gif)](https://www.flagify.com/?ref=https://vipread.com)

###### 附件下载

* ![](/static/images/icons/file-pdf.svg)

  ###### 火山引擎AI安全保障实践-曲乐炜-img.pdf

  时间:  2025-08-15T02:44:12Z

  大小:
  4.58 M

  下载:  22

  [登录下载](/auth/login)

##### 附件下载

![validate_code](#)

输入验证码
刷新验证码？

提交

错误信息

###### R2直链下载:

点击下载

###### 百度网盘:提取码(svip)

正在同步,稍等片刻

###### 蓝奏云盘:

正在同步,稍等片刻

关闭

错误信息

**分享文档请发送到 [[email protected]](/cdn-cgi/l/email-protection) ,感谢支持**

© 2014-2024 [信息安全知识库](//vipread.com)
[吉ICP备15005112号-2](https://beian.miit.gov.cn/)

* [**打赏支持**](/donate)
* [友情链接](/friends)
* [服务条款](/terms)
* [RSS](/rss)
* QQ交流群: 825629062