---
title: Google Chrome多个安全漏洞通告
url: http://blog.nsfocus.net/google-chrome/
source: 绿盟科技技术博客
date: 2023-02-28
fetch_date: 2025-10-04T08:15:11.038973
---

# Google Chrome多个安全漏洞通告

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

# Google Chrome多个安全漏洞通告

### Google Chrome多个安全漏洞通告

[2023-02-27](https://blog.nsfocus.net/google-chrome/ "Google Chrome多个安全漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 735

## **一、漏洞概述**

近日，绿盟科技CERT监测到Google Chrome官方发布安全公告，修复了多个安全漏洞。重点漏洞如下所示：

Google Chrome释放后重用漏洞（CVE-2023-0927）：

由于Google Chrome中的Web Payments API存在释放后使用缺陷，能够破坏渲染器进程的远程攻击者通过诱导用户访问恶意的HTML页面来利用堆损坏漏洞，最终可实现在目标系统上执行任意代码。

Google Chrome释放后重用漏洞（CVE-2023-0941）：

由于Google Chrome中的Prompts存在释放后使用缺陷，远程攻击者通过诱导用户访问恶意的HTML页面来利用堆损坏漏洞，最终可实现在目标系统上执行任意代码。

Google Chrome释放后重用漏洞（CVE-2023-0928）：

由于Google Chrome中的 SwiftShader存在释放后使用缺陷，远程攻击者通过诱导用户访问恶意的HTML页面来利用堆损坏漏洞，最终可实现在目标系统上执行任意代码。

Google Chrome释放后重用漏洞（CVE-2023-0929）：

由于Google Chrome中的Vulkan存在释放后使用缺陷，远程攻击者通过诱导用户访问恶意的HTML页面来利用堆损坏漏洞，最终可实现在目标系统上执行任意代码。

Google Chrome缓冲区溢出漏洞（CVE-2023-0930）：

由于Google Chrome中的Video存在缓冲区溢出缺陷，远程攻击者通过诱导用户访问恶意的HTML页面来利用堆损坏漏洞，最终可实现在目标系统上执行任意代码。

参考链接：

[https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update\_22.html](https://link.zhihu.com/?target=https%3A//chromereleases.googleblog.com/2023/02/stable-channel-desktop-update_22.html)

## **二、** **影响范围**

**受影响版本**

Google Chrome for Mac/Linux < 110.0.5481.177

Google Chrome for Windows < 110.0.5481.177

**不受影响版本**

Google Chrome for Mac/Linux >= 110.0.5481.177

Google Chrome for Windows >= 110.0.5481.177/.178

## **三、** **漏洞防护**

3.1 **官方升级**

目前官方已发布安全版本修复此漏洞，建议受影响的用户及时升级防护：[https://www.google.com/chrome/](https://link.zhihu.com/?target=https%3A//www.google.com/chrome/)

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/node-jscve-2023-23918/)

[Next](https://blog.nsfocus.net/flightradar/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)