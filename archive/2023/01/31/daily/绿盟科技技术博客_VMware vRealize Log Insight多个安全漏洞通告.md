---
title: VMware vRealize Log Insight多个安全漏洞通告
url: http://blog.nsfocus.net/vmware-vrealize-log-insigh/
source: 绿盟科技技术博客
date: 2023-01-31
fetch_date: 2025-10-04T05:14:09.571634
---

# VMware vRealize Log Insight多个安全漏洞通告

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

# VMware vRealize Log Insight多个安全漏洞通告

### VMware vRealize Log Insight多个安全漏洞通告

[2023-01-30](https://blog.nsfocus.net/vmware-vrealize-log-insigh/ "VMware vRealize Log Insight多个安全漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[周报](https://blog.nsfocus.net/tag/%E5%91%A8%E6%8A%A5/), [威胁防护](https://blog.nsfocus.net/tag/%E5%A8%81%E8%83%81%E9%98%B2%E6%8A%A4/)

阅读： 776

## ****一、漏洞概述****

近日，绿盟科技CERT监测发现VMware官方修复了多个VMware vRealize Log Insight的安全漏洞。在默认配置条件下，未经身份验证的攻击者通过组合利用以下重点漏洞，最终实现在在目标系统上以ROOT权限任意执行代码。国外安全团队表示已成功验证这些漏洞，请受影响的用户尽快采取措施进行防护。

重点漏洞如下：

****VMware vRealize Log Insight********远程代码执行漏洞（CVE-2022-31704）：****

由于vRealize Log Insight中存在访问控制缺陷，未经身份验证的远程攻击者通过将恶意文件注入受影响设备的操作系统，最终导致在目标系统上任意执行代码，CVSS评分为9.8。

****VMware vRealize Log Insight目录********遍历********漏洞********（CVE-2022-31706）：****

由于vRealize Log Insight中存在目录遍历漏洞，未经身份验证的远程攻击者通过将文件注入受影响设备的操作系统，最终导致在目标系统上任意执行代码，CVSS评分为9.8。

****VMware vRealize Log Insight********信息泄露漏洞（CVE-2022-31711）：****

由于vRealize Log Insight中存在信息泄露漏洞，未经身份验证的远程攻击者可利用该漏洞收集敏感会话和应用程序信息，CVSS评分为5.3。

参考链接：

https://www.vmware.com/security/advisories/VMSA-2023-0001.html

## ****二、影响范围****

**受影响版本**

* VMware vRealize Log Insight 8.x < 8.10.2
* VMware Cloud Foundation (VMware vRealize Log Insight) 4.x
* VMware Cloud Foundation (VMware vRealize Log Insight) 3.x

**不****受影响版本**

* VMware vRealize Log Insight 8.x >= 8.10.2

## ****三、漏洞防护****

* **官方升级**

目前官方已针对漏洞发布了补丁，请受影响的用户尽快下载补丁进行防护，对应产品版本的修复补丁及文档如下：

|  |  |  |
| --- | --- | --- |
| **产品版本** | **下载链接** | **操作文档** |
| VMware vRealize Log Insight 8.x | https://customerconnect.vmware.com/downloads/details?downloadGroup=VRLI-8102&productId=1351 | https://docs.vmware.com/en/vRealize-Log-Insight/8.10.2/rn/vrealize-log-insight-8102-release-notes/index.html |
| VMware Cloud Foundation (VMware vRealize Log Insight) 4.x | https://kb.vmware.com/s/article/90668 | |
| VMware Cloud Foundation (VMware vRealize Log Insight) 3.x |

* **临时防护措施**

若相关用户暂时无法进行升级操作，也可参考官方给出的措施进行临时缓解：

https://kb.vmware.com/s/article/90635

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport4/)

[Next](https://blog.nsfocus.net/apache-shirocve-2023-22602/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)