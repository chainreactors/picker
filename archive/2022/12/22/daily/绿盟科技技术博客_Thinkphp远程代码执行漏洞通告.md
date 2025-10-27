---
title: Thinkphp远程代码执行漏洞通告
url: http://blog.nsfocus.net/thinkphp/
source: 绿盟科技技术博客
date: 2022-12-22
fetch_date: 2025-10-04T02:13:43.405737
---

# Thinkphp远程代码执行漏洞通告

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

# Thinkphp远程代码执行漏洞通告

### Thinkphp远程代码执行漏洞通告

[2022-12-21](https://blog.nsfocus.net/thinkphp/ "Thinkphp远程代码执行漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")

阅读： 1,515

近日，绿盟科技CERT监测到网上公开披露了Thinkphp远程代码执行漏洞的利用细节。由于Thinkphp 程序中存在传入参数检查缺陷，当Thinkphp开启了多语言功能，未经身份验证的攻击者可以通过 get、header、cookie 等位置传入参数，实现目录穿越及文件包含，最终通过 pearcmd 文件包含trick实现远程代码执行。漏洞细节已公开，请相关用户尽快采取措施进行防护。

ThinkPHP 是一个免费开源的，快速、简单的面向对象的轻量级PHP开发框架 。

绿盟科技CERT已成功复现此漏洞：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_2-2-300x119.png)

参考链接：

https://blog.thinkphp.cn/3078655

## ****二、影响范围****

**受影响版本**

* 0.0 <= ThinkPHP <= v6.0.13
* 1.0 <= ThinkPHP <=v5.1.41
* 0.0 <= ThinkPHP <= v5.0.24

**不受影响版本**

* ThinkPHP >= v6.0.14
* ThinkPHP = v5.1.42

## ****三、漏洞排查****

步骤1、执行以下命令，查看ThinkPHP的版本信息：

|  |
| --- |
| php think version |

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_3-1-300x44.png)

若在影响范围内，则产品可能受该漏洞影响。

步骤2、查看ThinkPHP是否开启多语言功能

①Thinkphp6：

查看app/middleware.php中以下内容是否有注释，若无注释，则ThinkPHP开启了多语言功能，产品受此漏洞影响

|  |
| --- |
| \think\middleware\LoadLangPack::class |

②Thinkphp5：

查看app/middleware.php，若存在以下内容，则ThinkPHP开启了多语言功能，产品受此漏洞影响

|  |
| --- |
| ‘lang\_switch\_on’=> true |

## ****四、漏洞防护****

* **官方升级**

目前官方已发布安全版本修复此漏洞，建议受影响的用户及时升级防护：

https://github.com/top-think/framework/releases

* **临时防护措施**

若无法进行升级，用户可以通过以下方式进行规避防护。

1、Thinkphp6：

查看app/middleware.php，将以下内容进行注释

|  |
| --- |
| \think\middleware\LoadLangPack::class |

2、Thinkphp5：

查看app/middleware.php，将’lang\_switch\_on’=> true改为以下内容

|  |
| --- |
| ‘lang\_switch\_on’=>false |

3、重启Thinkphp

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/kaiyuanloudong/)

[Next](https://blog.nsfocus.net/fortinet-fortios-sslvpndcve-2022-42475/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)