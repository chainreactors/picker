---
title: Nacos身份认证绕过漏洞
url: http://blog.nsfocus.net/nacos/
source: 绿盟科技技术博客
date: 2023-03-17
fetch_date: 2025-10-04T09:51:25.256059
---

# Nacos身份认证绕过漏洞

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

# Nacos身份认证绕过漏洞

### Nacos身份认证绕过漏洞

[2023-03-16](https://blog.nsfocus.net/nacos/ "Nacos身份认证绕过漏洞")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 2,944

## ****一、漏洞概述****

近日，绿盟科技CERT监测发现Nacos官方修复了一个身份认证绕过漏洞。在默认配置下，由于未对密钥进行修改，未经身份验证的攻击者可通过对token.secret.key默认值进行碰撞，从而伪造身份访问后台，可实现对配置文件的读取、修改密码等操作，请受影响的用户尽快采取措施进行防护。

Nacos是构建云原生应用的动态服务发现、配置管理和服务管理平台。

绿盟科技已成功复现此漏洞：

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/WeChate32817e0875893f668b3a43aed1b1cde-300x142.png)

参考链接：

https://nacos.io/zh-cn/blog/announcement-token-secret-key.html

## ****二、影响范围****

**受影响****范围**

* 1.0 <= Nacos <= v2.2.0

**不受影响****范围**

* Nacos >= v2.2.0.1

## ****三、漏洞防护****

* **官方升级**

目前官方已针对该漏洞发布修复版本，建议受影响的用户及时更新升级到最新版本，下载链接：https://github.com/alibaba/nacos/releases/tag/2.2.0.1

* **其他防护措施**

若用户无法对产品进行升级，可通过参考以下链接，修改application.properties中的配置信息，对JWT令牌的密钥进行自定义：

https://nacos.io/zh-cn/docs/v2/guide/user/auth.html

****官方提示：****Nacos定义为一个应用服务发现和配置管理中间件服务，这类应用一般应该部署于内部网络环境，因此不建议用户将Nacos暴露在公网环境。同时应开启鉴权，设置自定义token.secret.key，并修改nacos用户的密码，提高安全性。另外，即使升级到最新版本，开启鉴权并修改了token.secret.key和nacos用户的密码，也请不要暴露在公网环境使用。

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/foxit-pdf-readereditor/)

[Next](https://blog.nsfocus.net/microsoftmarch/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)