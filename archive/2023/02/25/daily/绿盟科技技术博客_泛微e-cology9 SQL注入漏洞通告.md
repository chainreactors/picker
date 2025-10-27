---
title: 泛微e-cology9 SQL注入漏洞通告
url: http://blog.nsfocus.net/e-cology9-sql/
source: 绿盟科技技术博客
date: 2023-02-25
fetch_date: 2025-10-04T08:04:33.369607
---

# 泛微e-cology9 SQL注入漏洞通告

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

# 泛微e-cology9 SQL注入漏洞通告

### 泛微e-cology9 SQL注入漏洞通告

[2023-02-24](https://blog.nsfocus.net/e-cology9-sql/ "泛微e-cology9 SQL注入漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 1,003

## ****一、漏洞概述****

近日，绿盟科技CERT监测发现泛微官方发布安全补丁，修复了一个SQL注入漏洞。由于泛微e-cology9中对用户输入的数据验证存在缺陷，未经身份验证的攻击者通过构造特制数据包，最终可获取数据库中的敏感信息，请受影响的用户尽快采取措施进行防护。

泛微协同管理应用平台（e-cology）是一套兼具企业信息门户、知识文档管理、工作流程

管理、人力资源管理、客户关系管理、项目管理、财务管理、资产管理、供应链管理、数据中心功能的企业大型协同管理平台，并可形成一系列的通用解决方案和行业解决方案。

## ****二、影响范围****

**受影响****范围**

* 泛微e-cology9<=10.55

**不受影响****范围**

* 泛微e-cology9> 10.55

## ****三、漏洞防护****

* **官方升级**

目前官方已发布安全补丁修复了该漏洞，请受影响的用户尽快升级版本进行防护，官方下载链接如下：

https://www.weaver.com.cn/cs/securityDownload.asp#

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/vmware-carbon-black-app-controlcve-2023-20858/)

[Next](https://blog.nsfocus.net/ukrainecyberconflict/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)