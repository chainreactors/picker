---
title: Foxit PDF Reader与Editor多个远程代码执行漏洞
url: http://blog.nsfocus.net/foxit-pdf-readereditor/
source: 绿盟科技技术博客
date: 2023-03-17
fetch_date: 2025-10-04T09:51:25.610133
---

# Foxit PDF Reader与Editor多个远程代码执行漏洞

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

# Foxit PDF Reader与Editor多个远程代码执行漏洞

### Foxit PDF Reader与Editor多个远程代码执行漏洞

[2023-03-16](https://blog.nsfocus.net/foxit-pdf-readereditor/ "Foxit PDF Reader与Editor多个远程代码执行漏洞")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 735

## ****一、漏洞概述****

近日，绿盟科技CERT监测到Foxit官方修复了多个Foxit PDF Reader与Editor远程代码执行漏洞（CVE-2023-27329、CVE-2023-27330、CVE-2023-27331）。由于对Annotation objects（注释对象）的处理存在缺陷，Foxit PDF Reader与Editor在对对象执行操作之前未验证对象是否存在，未经身份验证的攻击者通过诱导用户打开特制文件或访问恶意页面，最终可实现在目标系统上任意执行代码。CVSS评分为7.8，请受影响的用户尽快采取措施进行防护。

福昕阅读器（Foxit PDF Reader，也称为Foxit Reader）是一款多语言PDF编辑查看工具，可以用于创建、查看、编辑、数字签名和打印PDF文件。

参考链接：

https://www.foxit.com/support/security-bulletins.html

## ****二、影响范围****

**受影响版本**

* Foxit PDF Editor 12.x <= 12.1.0.15250
* Foxit PDF Editor 11.x <= 11.2.4.53774
* Foxit PDF Editor <= 10.1.10.37854
* Foxit PDF Reader <= 12.1.0.15250

**不受影响版本**

* Foxit PDF Editor = 12.1.1
* Foxit PDF Editor = 11.2.5
* Foxit PDF Reader = 12.1.1

## ****三、漏洞防护****

* **官方升级**

目前官方已发布安全版本修复此漏洞，建议受影响的用户及时升级防护：

https://www.foxit.com/downloads/

* **手动升级**

在福昕PDF编辑器中，单击“帮助”>“关于福昕PDF编辑器”>“检查更新”以更新到最新版本。

注意：对于版本10及之前版本，请单击“帮助”>“检查更新”。

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/apache-dubbocve-2023-23638-2/)

[Next](https://blog.nsfocus.net/nacos/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)