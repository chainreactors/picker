---
title: Nacos Raft协议反序列化代码执行漏洞
url: http://blog.nsfocus.net/nacos-raft/
source: 绿盟科技技术博客
date: 2023-06-09
fetch_date: 2025-10-04T11:48:08.532001
---

# Nacos Raft协议反序列化代码执行漏洞

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

# Nacos Raft协议反序列化代码执行漏洞

### Nacos Raft协议反序列化代码执行漏洞

[2023-06-08](https://blog.nsfocus.net/nacos-raft/ "Nacos Raft协议反序列化代码执行漏洞")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 1,689

## ****一、漏洞概述****

近日，绿盟科技CERT监测发现到Nacos的Raft协议存在反序列化漏洞。由于Nacos集群对部分Jraft请求进行处理时，未限制使用hessian进行反序列化，从而导致攻击者可以实现代码执行。请受影响的用户尽快采取措施进行防护。

Nacos是一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。它提供了一组简单易用的特性集，实现动态服务发现、服务配置、服务元数据及流量管理。

|  |  |  |  |
| --- | --- | --- | --- |
| ****漏洞细节**** | ****漏洞PoC**** | ****漏洞EXP**** | ****在野利用**** |
| 未公开 | 未公开 | 未公开 | 暂不存在 |

参考链接：

https://github.com/alibaba/nacos/releases

## ****二、影响范围****

**受影响****版本**

* 4.0 <= Nacos < 1.4.6
* 0.0 <= Nacos < 2.2.3

**不受影响****版本**

* Nacos < 1.4.0
* 4.6 <= Nacos < 2.0.0
* Nacos >= 2.2.3

## ****三、漏洞防护****

* **官方升级**

目前官方已发布新版本修复该漏洞，请受影响的用户尽快升级版本进行防护，官方下载链接如下：

https://github.com/alibaba/nacos/releases/tag/1.4.6

https://github.com/alibaba/nacos/releases/tag/2.2.3

* **临时****防护****措施**

默认配置下该漏洞仅影响Nacos集群间Raft协议通信的7848端口，此端口不承载客户端请求，可以通过限制集群外部IP访问7848端口来进行缓解。

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport202323/)

[Next](https://blog.nsfocus.net/trustmap/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)