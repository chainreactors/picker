---
title: 浅谈云原生安全之CASB
url: http://blog.nsfocus.net/casb/
source: 绿盟科技技术博客
date: 2022-10-19
fetch_date: 2025-10-03T20:16:06.571405
---

# 浅谈云原生安全之CASB

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 浅谈云原生安全之CASB

### 浅谈云原生安全之CASB

[2022-10-18](https://blog.nsfocus.net/casb/ "浅谈云原生安全之CASB")[肖毅](https://blog.nsfocus.net/author/xiaoyi/ "View all posts by 肖毅")[云安全](https://blog.nsfocus.net/tag/%E4%BA%91%E5%AE%89%E5%85%A8/)

阅读： 2,197

## **一、******前言****

随着云计算给信息基础设施带来的变革，加上5G、物联网和产业互联网的发展，云原生正在成为企业IT的标配。如果说云原生是在开发项目时就和云环境进行绑定，那么云原生安全，就是在云创建之初就考虑云上应用的安全问题，以达到安全前置的效果。

Gartner就云原生安全提出三大云原生安全解决方案，分别是CWPP（Cloud Workload Protection Platforms）、CSPM（Cloud Security Posture Management）和CASB（Cloud Access Security Broker）。其中CWPP是对云工作负载进行保护，是对数据面的安全防护。CSPM是聚焦控制面的安全属性，包括配置策略和管理工作负载、合规评估、运营监控、DevOps集成、保障调用云运营商API完整性等等。CASB是专注于SaaS安全，为企业提供对SaaS使用情况的可视性和安全控制。以上三者对于保障云应用的实际运行，密不可分。三者配合的目的，都是为了云计算业务的正常开展和租户敏感数据得到妥善保护。

笔者将就CASB解决方案进行了整理和分析，期望与大家共同学习和成长。

## **二、******云访问安全代理（C********ASB********）介绍****

* ****云访问安全代理（CASB）的诞生****

CASB最早是由Gartner于2012年提出来的概念，最初是为了解决影子IT（Shadow IT）和BYOD（Bring your own device）的问题。

随着越来越多的公司将自己的业务迁移至云上，数据也从本地机房转移到云上存储，这也意味着企业已经失去了其对自身业务及数据的安全控制权，同时企业的业务也可能分布于不同的公有云上，因此CASB作为一种解决方案也逐渐承担起了帮助企业安全地接入不同的云应用，使其能清晰地看到云服务的使用情况，实现异构云服务的治理，并对云中的数据进行有效的保护的责任。

* ****云访问安全代理（CASB）的能力模型****

Gartner 将云访问安全代理（CASB）市场定义为云服务所必备的产品和服务，用来解决组织使用云服务时的安全漏洞，弥补组织使用云服务时存在的安全缺陷。

![](https://blog.nsfocus.net/wp-content/uploads/2022/10/图片2-300x171.png)

Gartner CASB基础能力架构【1】

由上图可以看出，云访问安全代理（CASB）是位于云服务消费者和云服务提供商之间的本地或基于云的安全策略实施点，用于在访问基于云的资源时合并和插入企业安全策略。

在此基础上，CASB主要有五个核心功能：

1、****可见性****（Visibility）：这个功能是用来解决影子IT（使用超出/未经批准的企业IT部门安全管理范围外的软件/云服务）的问题。CASB的解决方案通过监控和分类员工对云应用程序的访问和使用来确保业务运营的安全，并通过集中化的视图进行展示。比如说每个应用程序的风险分数，用户访问应用程序的次数，应用程序的类别等，进而通过利用这种深度可见性为后端数据分析模块和安全策略模块提供数据来源和策略执行依据，最终为其用户提供威胁保护。

2、****合规性****（Compliance）：即行为符合某些适用标准。也就是说CASB需要遵照地方性的法律法规或行业性的规定，从而为企业规避法律或政策风险。合规性本身不指向任何的具体功能，而是由CASB自身的其他功能（加密，DLP，威胁检测等等）来满足合规性。

3、****数据安全****（Data Security）：数据安全是CASB系统的核心组件，CASB解决方案需要保护企业在云内存储的所有数据，既保护数据的移动，也保护数据本身。由此可见，CASB解决方案需要集成访问控制和数据防泄漏(DLP)两个功能。确保数据安全的第一步是访问控制，企业用此项功能将访问边界定在CASB上，用于限制非合法用户获得企业数据；并通过结合用户和角色的管理，实现不同权限的合法用户访问对应敏感级的数据。但是仅通过访问控制是不够的，访问控制只是做到数据获取权限和范围的控制，不能管控非法人员使用合法账号操作数据，所以需要数据防泄漏的功能，对流经CASB的数据进行内容审计，甚至是整容（加密、截断、掩盖、替换）从而防止非法人员非法获取、恶意破坏和篡改数据。

4、****威胁防护****（Threat Protection）：目前很多的CASB解决方案都集成UEBA，以用户和实体为对象，结合规则以及机器学习模型，对用户行为进行分析和异常检测，尽可能快速地感知内部用户的可疑非法行为和恶意软件，从而达到威胁防护的效果。

5、****企业集成****（Enterprise Integration）： CASB解决方案整合了多种类型的安全策略，包括身份验证、单点登录、授权、凭据映射、设备分析、加密、标记化、日志记录、警报、恶意软件检测/预防等，当然CASB解决方案也可以与带有这些功能的企业安全设备联动，进行整体的集成。

* ****云访问安全代理（CASB）的功能特点****

与其他基于云环境的安全解决方案相比，CASB的功能非常独特。它不同于WAF和传统防火墙，CASB可以提供：

* 云上的风险评估和治理
* 数据防泄密
* 云上安全控制和协作
* 基于用户和实体行为分析（UEBA）对威胁的风险预防
* 配置审核
* 恶意软件检测
* 数据加密
* SSO和IAM集成
* 密钥管理
* 上下文访问控制

同时CASB解决方案可以支持多种部署方式：反向代理、正向代理和API控制。具体取决于企业提供的服务类型和所需的安全覆盖范围。

## **三、******总结****

Gartner将CASB列为到2021年要实施的十大安全项目之一，如果企业使用云服务并且企业员工用自有设备通过Internet连接访问公司网络，那么使用 CASB 弥合安全漏洞就变得至关重要。

CASB基于在云中数据是自己的，但是承载数据的基础设施不是自己的理念来进行解决方案的设计，适用于保护SaaS应用的场景。它允许企业采取灵活的安全策略实施方法，为企业提供量身定制的选项，并在访问与数据安全之间取得平衡，同时随着上云趋势越来越快，CASB也必将成为现代企业中重要的安全解决方案。

## **四、******参考文献****

[1]：2016年云访问安全代理市场指南（Market Guide for Cloud Access Security Brokers）

https://www.gartner.com/en/documents/3488119

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport42/)

[Next](https://blog.nsfocus.net/curl/)

### Meet The Author

肖毅

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)