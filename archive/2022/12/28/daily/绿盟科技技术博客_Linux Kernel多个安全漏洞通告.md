---
title: Linux Kernel多个安全漏洞通告
url: http://blog.nsfocus.net/linux-kernel-2/
source: 绿盟科技技术博客
date: 2022-12-28
fetch_date: 2025-10-04T02:36:26.583021
---

# Linux Kernel多个安全漏洞通告

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

# Linux Kernel多个安全漏洞通告

### Linux Kernel多个安全漏洞通告

[2022-12-27](https://blog.nsfocus.net/linux-kernel-2/ "Linux Kernel多个安全漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 1,012

## ****一、漏洞概述****

2022年12月26日，绿盟科技CERT监测到网上发布了Linux Kernel中的多个安全漏洞，请相关用户尽快采取措施进行防护。

Linux Kernel远程代码执行漏洞（CVE-2022-47939）：

Linux Kernel SMB2\_TREE\_DISCONNECT命令处理中存在远程代码执行漏洞。由于在对对象执行操作前缺乏对对象存在性的验证，当系统启用ksmbd时，未经身份验证的远程攻击者可实现在目标系统上任意执行代码，CVSS评分为10。

Linux Kernel信息泄露漏洞(CVE-2022-47940)：

Linux Kernel的SMB2\_TREE\_DISCONNECT命令处理中存在越界读信息泄露漏洞。由于缺乏对用户提供的数据的适当验证，当系统启用ksmbd时，经过身份验证的攻击者能够读取超过已分配缓冲区的信息，与其他漏洞结合最终能够在内核上下文中执行任意代码。CVSS评分为9.6。

Linux Kernel远程代码执行漏洞(CVE-2022-47942)：

Linux Kernel的文件属性的处理中存在一个远程代码执行漏洞，由于Linux Kernel在将用户提供的数据复制到基于堆的缓冲区之前，未对其长度进行适当的验证。当系统启用ksmbd时，经过身份验证的攻击者可以利用此漏洞在内核上下文中执行代码。CVSS评分为8.5。

KSMBD是由Namjae Jeon为Linux Kernel开发的开源In-kernel CIFS/SMB3服务器。它是SMB/CIFS协议在内核空间的实现，用于通过网络共享文件和IPC服务。

参考链接：

https://www.openwall.com/lists/oss-security/2022/12/23/10

## ****二、影响范围****

**受影响版本**

**CVE-2022-47939：**

* 15 <=Linux Kernel < 5.19.2

**CVE-2022-47940：**

* 15 <=Linux Kernel < 5.18.18

**CVE-2022-47942：**

* 15 <=Linux Kernel < 5.19.2

**不受影响版本**

**CVE-2022-47939:**

* Linux Kernel >= 5.19.2

**CVE-2022-47940：**

* Linux Kernel >= 5.18.18

**CVE-2022-47942：**

* Linux Kernel >= 5.19.2

## ****三、漏洞检测****

* **版本检测**

Linux系统用户可以通过查看版本来判断当前系统是否在受影响范围内，查看操作系统版本信息命令如下：

|  |
| --- |
| cat /proc/version |

若版本在受影响范围内，且系统启用ksmbd时，可能存在安全风险。

## ****四、漏洞防护****

* **官方升级**

1、目前官方已在新版本中修复了该漏洞，请受影响的用户尽快升级版本进行防护，官方下载链接：https://www.kernel.org

2、目前官方已发布补丁包修复此漏洞，建议受影响的用户及时安装防护：

CVE-2022-47939：

https://github.com/torvalds/linux/commit/cf6531d98190fa2cf92a6d8bbc8af0a4740a223c

CVE-2022-47940：

https://github.com/torvalds/linux/commit/158a66b245739e15858de42c0ba60fcf3de9b8e6

CVE-2022-47942：

https://github.com/torvalds/linux/commit/8f0541186e9ad1b62accc9519cc2b7a7240272a7

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport52/)

[Next](https://blog.nsfocus.net/blackhat2022%EF%BC%9A4g-5/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)