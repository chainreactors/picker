---
title: Smartbi商业智能软件任意文件读取漏洞通告
url: http://blog.nsfocus.net/smartbi/
source: 绿盟科技技术博客
date: 2023-03-25
fetch_date: 2025-10-04T10:37:53.906590
---

# Smartbi商业智能软件任意文件读取漏洞通告

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

# Smartbi商业智能软件任意文件读取漏洞通告

### Smartbi商业智能软件任意文件读取漏洞通告

[2023-03-24](https://blog.nsfocus.net/smartbi/ "Smartbi商业智能软件任意文件读取漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 713

## ****一、漏洞概述****

近日，绿盟科技CERT监测到Smartbi官方修复了一个MYSQL JDBC任意文件读取漏洞，由于 Smartbi对敏感系统文件的安全限制存在缺陷，未经身份验证的远程攻击者通过此漏洞可获取到系统中的敏感信息，最终造成敏感信息泄露。

Smartbi是广州思迈特软件有限公司旗下的商业智能BI和数据分析品牌。 Smartbi致力于为企业客户提供一站式商业智能解决方案 。

参考链接：

https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=107741875

## ****二、影响范围****

**受影响****范围**

* V7 <= Smartbi <= V10.5.12

## ****三、漏洞防护****

* **官方升级**

目前官方已发布补丁包修复此漏洞，建议受影响的用户及时安装防护，参考链接：

https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=107741875

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/spring-frameworkcve-2023-20860/)

[Next](https://blog.nsfocus.net/miniocve-2023-28432/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)