---
title: Adobe ColdFusion多个安全漏洞通告
url: http://blog.nsfocus.net/adobe-coldfusion/
source: 绿盟科技技术博客
date: 2023-03-21
fetch_date: 2025-10-04T10:09:03.584768
---

# Adobe ColdFusion多个安全漏洞通告

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

# Adobe ColdFusion多个安全漏洞通告

### Adobe ColdFusion多个安全漏洞通告

[2023-03-20](https://blog.nsfocus.net/adobe-coldfusion/ "Adobe ColdFusion多个安全漏洞通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")[安全漏洞](https://blog.nsfocus.net/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/), [漏洞防护](https://blog.nsfocus.net/tag/%E6%BC%8F%E6%B4%9E%E9%98%B2%E6%8A%A4/)

阅读： 793

## ****一、漏洞概述****

近日，绿盟科技CERT监测到Adobe官方发布安全通告，修复了多个Adobe ColdFusion漏洞，请受影响的用户尽快采取措施进行防护。重点漏洞如下：

****Adobe ColdFusion反序列化漏洞（CVE-2023-26359）********：****

由于Adobe ColdFusion对反序列化安全检查存在缺陷，未经身份验证的远程攻击者通过构造恶意数据包进行反序列化攻击，最终可实现在目标系统上执行任意代码，CVSS评分为9.8。

****Adobe ColdFusion访问控制不当漏洞（CVE-2023-26360）：****

由于Adobe ColdFusion存在对资源访问控制不当的缺陷，未经身份验证的攻击者可利用该漏洞在目标系统上实现任意代码执行，且无需用户交互。目前已监测到该漏洞存在在野利用，CVSS评分8.6。

Adobe ColdFusion是一种用于构建动态Web应用程序的服务器端编程语言和开发平台。它由Adobe Systems开发和维护，并使用Java虚拟机（JVM）作为其运行环境。ColdFusion支持多种编程语言，包括CFML（ColdFusion标记语言）、JavaScript、Java、.NET和其他Web技术，如HTML、CSS和SQL。

参考链接：

https://helpx.adobe.com/security/products/coldfusion/apsb23-25.html

## ****二、影响范围****

**受影响****范围**

外部版本：

* Adobe ColdFusion 2021 <= 2021Update 5
* Adobe ColdFusion 2018 <= 2018 Update 15

内部版本：

* Adobe ColdFusion 2021 < 2021.0.06.330132
* Adobe ColdFusion 2018 < 2018.0.16,330130

**不受影响****范围**

外部版本：

* Adobe ColdFusion 2021 Update 6
* Adobe ColdFusion 2018 Update 16

内部版本：

* Adobe ColdFusion 2021 >= 2021.0.06.330132
* Adobe ColdFusion 2018 >= 2018.0.16.330130

## ****三、漏洞检测****

* **版本检测**

相关用户可通过版本检测的方法判断当前应用是否存在风险。

方法一：登陆系统后访问/CFIDE/administrator/index.cfm，查看system inforamtion中的版本

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/WeChat0c6b024b303ff5dec2a3745152bee632-300x145.png)

方法二：在Adobe ColdFusion安装目录的bin下执行cfinfo -version(info)命令查看版本

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/WeChat9da9b45f78646115c69948c54958f683-300x194.png)

若当前版本在受影响范围内，则可能存在安全风险。

## ****四、漏洞防护****

* **官方升级**

目前官方已在最新版本中修复了该漏洞，请受影响的用户尽快升级版本进行防护，参考链接如下：

Adobe ColdFusion 2021：

https://helpx.adobe.com/coldfusion/kb/coldfusion-2021-update-6.html

Adobe ColdFusion 2018：

https://helpx.adobe.com/coldfusion/kb/coldfusion-2018-update-16.html

* **手动****升级**

****对于********Adobe ColdFusion 2018：****

****步骤一：****访问以下链接下载补丁

https://cfdownload.adobe.com/pub/adobe/coldfusion/2018/updates/hotfix-016-330130.jar

****步骤二：****根据下载的补丁文件执行以下相应命令（必须具有启动或停止ColdFusion服务以及对ColdFusion根目录有完全访问权限。）

Windows下执行：

|  |
| --- |
| <cf\_root>/jre/bin/java.exe -jar <jar-file-dir>/hotfix-\*.jar |

Linux下执行：

|  |
| --- |
| <cf\_root>/jre/bin/java -jar <jar-file-dir>/hotfix-\*.jar |

确保与ColdFusion捆绑在一起的JRE用于执行下载的JAR。对于独立的ColdFusion，必须位于<cf\_root>/jre/bin。

更多信息请参考官方教程：

https://helpx.adobe.com/coldfusion/configuring-administering/using-the-coldfusion-administrator.html#serverupdate

****对于Adobe ColdFusion 2021：****

****步骤一：****访问以下链接下载补丁：

https://cfdownload.adobe.com/pub/adobe/coldfusion/2021/updates/hotfix-006-330132.jar

****步骤二：****访问以下链接下载存储库，并解压到所有ColdFusion服务器实例都可以访问的位置：

https://cfdownload.adobe.com/pub/adobe/coldfusion/2021/packages/hotfix-packages-cf2021-006-330132.zip

****步骤三：****更新cfusion及其所有子实例的 cfusion/lib/neo\_updates.xml 中的“packagesurl”，以指向下载文件夹中的<InstallerReposityUnzippedPath>/bundles/bundlesdependency.json

注：若核心服务器修补程序安装成功，但包存在问题，则可以从包管理器客户端对包进行安装或更新(cfusion\bin\cfpm.bat|cfpm.sh)

****步骤四：****参考Adobe ColdFusion 2018升级中的步骤二

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/win10-u/)

[Next](https://blog.nsfocus.net/microsoft-outlookcve-2023-23397/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)