---
title: Apache HTTP Server多个安全漏洞
url: http://blog.nsfocus.net/apache-http-server/
source: 绿盟科技技术博客
date: 2023-03-14
fetch_date: 2025-10-04T09:30:46.049389
---

# Apache HTTP Server多个安全漏洞

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

# Apache HTTP Server多个安全漏洞

### Apache HTTP Server多个安全漏洞

[2023-03-13](https://blog.nsfocus.net/apache-http-server/ "Apache HTTP Server多个安全漏洞")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 2,012

## ****一、漏洞概述****

近日，绿盟科技CERT监测到Apache官方发布安全通告，修复多个Apache HTTP Server漏洞，请受影响的用户尽快采取措施进行防护。

****Apache HTTP Server请求走私漏洞（CVE-2023-25690）：****

当mod\_proxy与某种形式的RewriteRule或ProxyPassMatch一同启用时，会出现非特定模式匹配用户部分请求目标（URL）的情况，远程攻击者可通过构造恶意HTTP请求包绕过代理服务器中的访问控制，将非预期的URL代理到现有源服务器，从而导致缓存中毒。

****Apache HTTP Server********响应********走私漏洞（CVE-202********3********-27522）：****

由于mod\_proxy\_uwsgi中存在错误配置，远程攻击可利用此漏洞者注入任意HTTP标头并导致服务器返回拆分响应，攻击者进一步利用该漏洞，最终可能导致Web缓存中毒或跨站脚本攻击，并获取敏感信息。

Apache HTTP Server（简称Apache）是Apache软件基金会的一个开放源码的网页服务器，可以在大多数计算机操作系统中运行，由于其跨平台和安全性被广泛使用，是最流行的Web服务器端软件之一。

参考链接：

https://httpd.apache.org/security/vulnerabilities\_24.html

## ****二、影响范围****

**受影响范围**

CVE-2023-25690：

* 4.0 <= Apache HTTP Server <= 2.4.55

CVE-2023-27522：

* 4.30 <= Apache HTTP Server <= 2.4.55

****不受影响********范围****

CVE-2023-25690：

* Apache HTTP Server >= 2.4.56

CVE-2023-27522：

* Apache HTTP Server >= 2.4.56

## ****三、漏洞检测****

* **版本检测**

相关用户可通过版本检测的方法判断当前应用是否存在风险。

使用如下命令可查看当前使用的Apache HTTP Server版本：

|  |
| --- |
| httpd -v |

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片1-1-300x57.png)

若当前版本在受影响范围内，则可能存在安全风险。

## ****四、漏洞防护****

* **官方升级**

目前官方已发布安全版本修复此漏洞，建议受影响的用户及时升级防护：

https://httpd.apache.org/download.cgi#apache24

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/microsoft-word-cve-2023-21716/)

[Next](https://blog.nsfocus.net/apache-dubbocve-2023-23638/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)