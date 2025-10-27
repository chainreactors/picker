---
title: Fortinet多个产品安全漏洞通告
url: http://blog.nsfocus.net/fortinet/
source: 绿盟科技技术博客
date: 2023-02-22
fetch_date: 2025-10-04T07:43:25.363142
---

# Fortinet多个产品安全漏洞通告

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

# Fortinet多个产品安全漏洞通告

### Fortinet多个产品安全漏洞通告

[2023-02-21](https://blog.nsfocus.net/fortinet/ "Fortinet多个产品安全漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 868

## **一、****漏洞概述**

近日，绿盟科技CERT监测发现Fortinet官方发布安全通告，修复了Fortinet多个产品漏洞，重点漏洞如下所示：

**FortiNAC keyUpload远程代码执行漏洞（CVE-2022-39952）:**

由于ForitNAC的keyUpload脚本存在缺陷，未经身份验证的攻击者可通过发送特制的HTTP请求，最终实现在目标系统上执行任意代码。CVSS评分为9.8。请相关用户尽快采取措施进行防护。

FortiNAC是Fortinet的网络访问控制解决方案，通过对连接到网络的所有内容的可见性、控制和自动响应来增强Fortinet的安全结构。可监督和保护连接到企业网络的所有数字资产，涵盖从IT、IoT、OT/ICS到IoMT的设备，并协调对各种网络事件的自动响应。

参考链接：[https://www.fortiguard.com/psirt/FG-IR-22-300](https://link.zhihu.com/?target=https%3A//www.fortiguard.com/psirt/FG-IR-22-300)

**FortiWeb 远程代码执行漏洞（CVE-2021-42756）：**

由于ForitWeb代理程序存在缺陷，未经身份验证的攻击者通过发送特制HTTP请求触发基于堆栈的缓冲区溢出，最终可实现在目标系统上执行任意代码。CVSS评分为9.3，请相关用户尽快采取措施进行防护。

FortiWeb是Fortinet的Web应用防火墙，可保护关键业务Web应用免受针对已知和未知漏洞的攻击。

参考链接：

[https://www.fortiguard.com/psirt/FG-IR-21-186](https://link.zhihu.com/?target=https%3A//www.fortiguard.com/psirt/FG-IR-21-186)

**FortiADC CLI命令注入漏洞（CVE-2022-27482）：**

由于FortiADC存在缺陷，经过身份验证的攻击者可通过CLI命令以root权限任意执行shell代码。CVSS评分为7.8，请相关用户尽快采取措施进行防护。

FortiADC是一款先进的应用交付控制器，可优化应用的性能和可用性，同时通过自身的原生安全工具和将应用交付集成到Fortinet Security Fabric安全架构中来保障应用的安全。

参考链接：

[https://www.fortiguard.com/psirt/FG-IR-22-046](https://link.zhihu.com/?target=https%3A//www.fortiguard.com/psirt/FG-IR-22-046)

**FortiExtender命令注入漏洞（CVE-2022-27489）：**

由于FortiExtender 网络服务器对用户输入参数的验证存在缺陷，具有高权限的攻击者通过发送特制参数，最终可实现在目标系统上任意命令执行。CVSS评分为7.2，请相关用户尽快采取措施进行防护。

FortiExtender 蜂窝网关助力用户打造超快速LTE和5G无线网络，支持任意WAN边缘的安全连接与扩展。

参考链接：

[https://www.fortiguard.com/psirt/FG-IR-22-048](https://link.zhihu.com/?target=https%3A//www.fortiguard.com/psirt/FG-IR-22-048)

## **二、****影响范围**

**受影响版本**

**CVE-2022-39952:**

l FortiNAC = 9.4.0

l 9.2.0 <= FortiNAC <= 9.2.5

l 9.1.0 <= FortiNAC <= 9.1.7

l 8.8.0 <= FortiNAC <= 8.8.11

l 8.7.0 <= FortiNAC <= 8.7.6

l 8.6.0 <= FortiNAC <= 8.6.5

l 8.5.0 <= FortiNAC <=8.5.4

l FortiNAC = 8.3.7

**CVE-2021-42756：**

l 5.6.0 <= FortiWeb <= 5.9.1

l 6.0.0 <= FortiWeb <= 6.0.7

l 6.1.0 <= FortiWeb <= 6.1.2

l 6.2.0 <= FortiWeb <= 6.2.6

l 6.3.0 <= FortiWeb <= 6.3.16

l 6.4.0 <= FortiWeb <= 6.4.1

**CVE-2022-27482:**

l 7.0.0 <= FortiADC <= 7.0.1

l 6.2.0 <= FortiADC <= 6.2.3

l 6.1.0 <= FortiADC <= 6.1.6

l 6.0.0 <= FortiADC <= 6.0.4

l 5.4.0 <= FortiADC <= 5.4.5

l 5.3.0 <= FortiADC <= 5.3.7

l 5.2.0 <= FortiADC <= 5.2.8

l 5.1.0 <= FortiADC <= 5.1.7

l 5.0.0 <= FortiADC <= 5.0.4

CVE-2022-27489:

l 7.0.0 <= FortiExtender <= 7.0.3

l FortiExtender = 5.3.2

l 4.2.0 <= FortiExtender <= 4.2.4

l 4.1.1 <= FortiExtender <= 4.1.8

l 4.0.0 <= FortiExtender <= 4.0.2

l 3.3.0 <= FortiExtender <= 3.3.2

l 3.2.1 <= FortiExtender <= 3.2.3

l 3.1.0 <= FortiExtender <= 3.1.2

l 3.0.0 <= FortiExtender <= 3.0.2

**不受影响版本**

**CVE-2022-39952:**

l FortiNAC >= 9.4.1

l FortiNAC >= 9.2.6

l FortiNAC >= 9.1.8

l FortiNAC >= 7.2.0

**CVE-2021-42756：**

l FortiWeb >= 7.0.0

l FortiWeb >= 6.3.17

l FortiWeb >= 6.2.7

l FortiWeb >= 6.1.3

l FortiWeb >= 6.0.8

**CVE-2022-27482:**

l FortiADC >= 7.0.2

l FortiADC >= 6.2.4

**CVE-2022-27489:**

l FortiExtender >= 7.2.0

l FortiExtender >= 7.0.4

l FortiExtender >= 4.2.5（即将发布）

l FortiExtender >= 4.1.9 （即将发布）

l FortiExtender >= 4.0.3（即将发布）

l FortiExtender >= 3.3.3

l FortiExtender >= 3.2.4

## **三、****漏洞防护**

3.1 **官方升级**

目前官方已发布新版本修复了上述漏洞，请受影响的用户尽快升级至最新版本进行防护， 官方下载链接：

|  |  |
| --- | --- |
| CVE编号 | 修复版本链接 |
| CVE-2022-39952 | [https://docs.fortinet.com/product/fortinac/9.4](https://link.zhihu.com/?target=https%3A//docs.fortinet.com/product/fortinac/9.4) |
| CVE-2021-42756 | [https://docs.fortinet.com/product/fortiweb/7.2](https://link.zhihu.com/?target=https%3A//docs.fortinet.com/product/fortiweb/7.2) |
| CVE-2022-27482 | [https://docs.fortinet.com/product/FortiADC/7.2](https://link.zhihu.com/?target=https%3A//docs.fortinet.com/product/FortiADC/7.2) |
| CVE-2022-27489 | [https://docs.fortinet.com/product/FortiExtender/7.2](https://link.zhihu.com/?target=https%3A//docs.fortinet.com/product/FortiExtender/7.2) |

其他产品可参考：[https://www.fortiguard.com/psirt?date=02-2023](https://link.zhihu.com/?target=https%3A//www.fortiguard.com/psirt%3Fdate%3D02-2023)

3.2 **其他防护建议**

若相关用户暂时无法进行升级操作，可使用白名单限制对受影响系统端口的访问。

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/cmm/)

[Next](https://blog.nsfocus.net/joomlacve-2023-23752/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)