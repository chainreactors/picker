---
title: Apache Solr远程代码执行漏洞（CNVD-2023-27598）通告
url: http://blog.nsfocus.net/apache-solrcnvd-2023-27598/
source: 绿盟科技技术博客
date: 2023-04-20
fetch_date: 2025-10-04T11:34:30.816207
---

# Apache Solr远程代码执行漏洞（CNVD-2023-27598）通告

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

# Apache Solr远程代码执行漏洞（CNVD-2023-27598）通告

### Apache Solr远程代码执行漏洞（CNVD-2023-27598）通告

[2023-04-19](https://blog.nsfocus.net/apache-solrcnvd-2023-27598/ "Apache Solr远程代码执行漏洞（CNVD-2023-27598）通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 968

## ****一、漏洞概述****

近日，绿盟科技CERT监测发现网上公开披露了Apache Solr远程代码执行漏洞的分析文章。当Solr以cloud模式启动且可出网时，未经身份验证的远程攻击者通过发送多个特制的数据包，最终可实现在目标系统上执行任意代码。请受影响的用户尽快采取措施进行防护。

Apache Solr是Apache Lucene 项目的开源企业搜索平台，由 Java 开发，运行于 Servlet 容器（如Apache Tomcat或Jetty）的一个独立的全文搜索服务器，主要功能包括全文检索、命中标示、分面搜索、动态聚类、数据库集成，以及富文本的处理。

## ****二、影响范围****

**受影响范围**

* 10.0 <= Apache Solr < 9.2.0

**不受影响范围**

* Apache Solr >= 9.2.0
* Apache Solr < 8.10.0

## ****三、漏洞防护****

* **官方升级**

目前官方已发布安全版本修复该漏洞，建议受影响的用户尽快升级版本进行防护：

https://github.com/apache/solr/releases/tag/releases%2Fsolr%2F9.2.0

* **临时防护措施**

* 在对业务无影响的条件下，通过设置白名单的方式来限制不受信任IP的访问。
* 以SolrCloud方式部署的机器不出网。
* SolrCloud模式下，需将“json”上传至ZooKeeper。
* 在Solr启动时加上用户身份校验。

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/google-chrome-v8cve-2023-2033/)

[Next](https://blog.nsfocus.net/%E4%BA%91%E5%AE%89%E5%85%A8%E6%8A%80%E6%9C%AF%E5%8F%82%E8%80%83%E6%9E%B6%E6%9E%84%EF%BC%88%E7%AC%AC%E4%BA%8C%E7%89%88%EF%BC%89%EF%BC%88%E4%B8%8B%EF%BC%89/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)