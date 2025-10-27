---
title: Atlassian多个高危漏洞通告
url: http://blog.nsfocus.net/atlassian-2/
source: 绿盟科技技术博客
date: 2023-07-22
fetch_date: 2025-10-04T11:54:53.389884
---

# Atlassian多个高危漏洞通告

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

# Atlassian多个高危漏洞通告

### Atlassian多个高危漏洞通告

[2023-07-21](https://blog.nsfocus.net/atlassian-2/ "Atlassian多个高危漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 1,270

## **一、****漏洞概述**

近日，绿盟科技CERT监测到Atlassian官方发布安全公告，修复了Atlassian产品中的多个高危漏洞，请相关用户采取措施进行防护。

**Atlassian Confluence Data Center和Server远程代码执行漏洞（CVE-2023-22508/** **CVE-2023-22505）：**

Atlassian Confluence Data Center和Server中存在远程代码执行漏洞，经过身份验证的远程攻击者利用该漏洞可实现远程代码执行，且无需用户交互。

Atlassian Confluence是Atlassian公司出品的专业wiki程序。它可以作为一个知识管理的工具，通过它能够实现团队成员之间的协作和知识共享。

**Bamboo Data Center和Server远程代码执行漏洞（CVE-2023-22506）：**

Bamboo Data Center和Server中存在远程代码执行漏洞，经过身份验证的远程攻击者利用该漏洞可导致修改系统调用执行操作，最终实现执行任意代码。

Atlassian Bamboo 是一款流行的持续集成和持续交付（CI/CD）工具，它可以自动化软件构建、测试和部署的流程。它被广泛用于开发团队中，特别是敏捷开发环境中的软件项目。

参考链接：

[https://jira.atlassian.com/browse/CONFSERVER-88221](https://link.zhihu.com/?target=https%3A//jira.atlassian.com/browse/CONFSERVER-88221)

[https://jira.atlassian.com/browse/CONFSERVER-88265](https://link.zhihu.com/?target=https%3A//jira.atlassian.com/browse/CONFSERVER-88265)

[https://jira.atlassian.com/browse/BAM-22400](https://link.zhihu.com/?target=https%3A//jira.atlassian.com/browse/BAM-22400)

## **二、****影响范围**

**受影响版本**

**CVE-2023-22508**

7.19.8 <= Confluence Data Center和Server < 8.2.0

**CVE-2023-22505**

8.0.0 <= Confluence Data Center和Server < 8.3.2、8.4.0

**CVE-2023-22506**

8.0.0 <= Bamboo Data Center和Server < 9.2.3、9.3.1

**不受影响版本**

**CVE-2023-22508**

Confluence Data Center和Server >= 8.2.0

**CVE-2023-22505**

Confluence Data Center和Server >= 8.3.2

Confluence Data Center和Server >= 8.4.0

**CVE-2023-22506**

Bamboo Data Center和Server >= 9.2.3

Bamboo Data Center和Server >= 9.3.1

## **三、****漏洞防护**

3.1 **官方升级**

目前官方已在最新版本中修复了该漏洞，请受影响的用户尽快升级版本进行防护，官方下载链接如下：

|  |  |
| --- | --- |
| 受影响产品 | 安全版本链接 |
| Confluence Data Center和Server | [https://www.atlassian.com/software/confluence/download-archives](https://link.zhihu.com/?target=https%3A//www.atlassian.com/software/confluence/download-archives) |
| Bamboo Data Center和Server | [https://www.atlassian.com/software/bamboo/download-archives](https://link.zhihu.com/?target=https%3A//www.atlassian.com/software/bamboo/download-archives) |

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/citrix-adccitrix-gatewaycve-2023-3519/)

[Next](https://blog.nsfocus.net/spring-securitycve-2023-34034/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)