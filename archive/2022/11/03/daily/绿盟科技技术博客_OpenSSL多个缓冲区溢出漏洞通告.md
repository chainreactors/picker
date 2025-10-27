---
title: OpenSSL多个缓冲区溢出漏洞通告
url: http://blog.nsfocus.net/openssl/
source: 绿盟科技技术博客
date: 2022-11-03
fetch_date: 2025-10-03T21:39:56.650274
---

# OpenSSL多个缓冲区溢出漏洞通告

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

# OpenSSL多个缓冲区溢出漏洞通告

### OpenSSL多个缓冲区溢出漏洞通告

[2022-11-02](https://blog.nsfocus.net/openssl/ "OpenSSL多个缓冲区溢出漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 956

## ****一、漏洞概述****

2022年11月2日，绿盟科技CERT监测到openssl官方发布安全公告，修复了OpenSSL存在多个缓冲区溢出漏洞。OpenSSL 是一个开放源代码的软件库包。应用程序可以使用这个包来进行安全通信、避免窃听，同时确认另一端连接者的身份，广泛被应用在互联网的网页服务器上。请相关用户尽快采取措施进行防护。

****OpenSSL 缓冲区溢出漏洞（CVE-2022-3602）：****

OpenSSL的X.509证书验证过程中可触发缓冲区溢出漏洞。在经过证书链签名验证，且CA 签署恶意证书或应用程序继续进行证书验证后，攻击者可通过制作恶意电子邮件地址，使堆栈上四个被控制的字节溢出，最终导致拒绝服务或在特定平台上执行任意代码。在 TLS 客户端中，连接到恶意服务器可以触发该漏洞。在TLS服务器中，若服务器请求客户端身份验证并且恶意客户端连接，即可触发该漏洞。

****OpenSSL 缓冲区溢出漏洞（CVE-2022-3786）：****

OpenSSL的X.509证书验证过程中可触发缓冲区溢出漏洞。在经过证书链签名验证，且CA 签署恶意证书或应用程序继续进行证书验证后，攻击者可通过在证书中制作恶意电子邮件地址，实现包含“.”字符(十进制46)的任意字节数溢出，最终导致拒绝服务攻击。在TLS客户端中，连接到恶意服务器可以触发此操作。在TLS服务器中，若服务器请求客户端身份验证并且恶意客户端连接，即可触发此漏洞。

参考链接：

https://www.openssl.org/news/secadv/20221101.txt

## ****二、影响范围****

**受影响版本**

* 0.0 <= OpenSSL <= 3.0.6

**安全版本**

* OpenSSL >= 3.0.7

注：OpenSSL 3.0以下版本不受该漏洞影响

## ****三、漏洞检测****

* **人工检测**

相关用户可通过运行下列命令进行版本检测判断当前系统是否存在风险：

|  |
| --- |
| openssl version |

若当前使用的OpenSSL版本在受影响范围内，则可能存在安全风险。

## ****四、漏洞防护****

* **官方升级**

目前官方已针对受支持的版本修复了该漏洞，请受影响的用户尽快更新版本进行防护，官方下载链接：https://github.com/openssl/openssl/tags

补丁链接：https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=c42165b5706e42f67ef8ef4c351a9a4c5d21639a

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/google-chromecve-2022-3723/)

[Next](https://blog.nsfocus.net/idapython/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)