---
title: Oracle全系产品2023年1月关键补丁更新通告
url: http://blog.nsfocus.net/oracle20231/
source: 绿盟科技技术博客
date: 2023-02-01
fetch_date: 2025-10-04T05:20:58.627537
---

# Oracle全系产品2023年1月关键补丁更新通告

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

# Oracle全系产品2023年1月关键补丁更新通告

### Oracle全系产品2023年1月关键补丁更新通告

[2023-01-31](https://blog.nsfocus.net/oracle20231/ "Oracle全系产品2023年1月关键补丁更新通告")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")

阅读： 1,845

## ****一、概述****

2023年1月19日，绿盟科技CERT监测发现Oracle官方发布了1月重要补丁更新公告CPU（Critical Patch Update），此次共修复了327个不同程度的漏洞，此次安全更新涉及Oracle WebLogic Server、Oracle Fusion Middleware、Oracle MySQL、Oracle Java SE、Oracle Retail Applications、Oracle Database Server等多个常用产品。Oracle强烈建议客户尽快应用关键补丁更新修复程序，对漏洞进行修复。

参考链接：

https://www.oracle.com/security-alerts/cpujan2023.html

## ****二、重点漏洞概述****

根据产品流行度和漏洞重要性筛选出此次更新中包含影响较大的漏洞，请相关用户重点进行关注：

****Oracle WebLogic Server 远程代码执行漏洞********（CVE-2023-21839）：****

由于Weblogic IIOP/T3协议存在缺陷，未经身份验证的攻击者通过IIOP/T3协议向受影响的服务器发送恶意的请求，最终导致在目标服务器上访问敏感信息并执行任意代码，目前该漏洞技术细节已公开。

****Oracle WebLogic Server 远程代码执行漏洞（CVE-2022-42920）：****

由于Oracle WebLogic Server中引用了第三方软件“Apache Commons BCEL”，且其中有许多通常只允许更改特定类特征的 API，由于存在越界写入缺陷，未经身份验证的攻击者可利用多个API发送恶意数据进行攻击，最终可造成拒绝服务或任意代码执行。

****Oracle Fusion Middleware********多个漏洞：****

此次安全更新针对Oracle MySQL发布了50个安全补丁, 其中的39个漏洞在未经用户身份验证的情况下即可远程进行利用，即无需用户凭据即可通过网络利用。严重漏洞编号如下：

CVE-2022-45047

CVE-2022-42889

CVE-2022-23305

CVE-2022-25236

CVE-2022-31813

CVE-2022-2274

CVE-2022-27404

**Oracle MySQL多个漏洞：**

此次安全更新针对Oracle MySQL发布了37个安全补丁, 其中的8个漏洞在未经用户身份验证的情况下即可远程进行利用，即无需用户凭据即可通过网络利用。高危漏洞编号如下：

CVE-2022-31692

CVE-2022-32221

CVE-2022-37434

CVE-2020-36242

CVE-2022-24407

**Oracle Financial Services Applications多个漏洞：**

此次安全更新针对Oracle Financial Services Applications发布了16个安全补丁。其中的12个漏洞在未经用户身份验证的情况下即可远程进行利用。高危漏洞编号如下：

CVE-2022-33980

****Oracle Communications Applications多个漏洞：****

此次安全更新针对Oracle Communications发布了39个安全补丁，其中的31个漏洞在未经用户身份验证的情况下即可远程进行利用。高危漏洞编号如下：

CVE-2022-42889

CVE-2022-33980

CVE-2022-22978

CVE-2022-37454

CVE-2022-31692

**Oracle E-Business Suite多个漏洞：**

此次安全更新针对Oracle E-Business Suite发布了12个安全补丁，其中的10个漏洞在未经用户身份验证的情况下即可远程进行利用。攻击者可以通过HTTP访问网络，从而破坏套件中的产品，从而对关键数据的未授权访问或对所有套件中产品可访问数据的完全访问。高危漏洞编号如下：

CVE-2023-21849

CVE-2023-21858

CVE-2023-21857

CVE-2023-21856

CVE-2023-21852

CVE-2023-21851

CVE-2023-21853

CVE-2023-21855

CVE-2023-21854

Oracle官方1月关键补丁更新漏洞总结如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **产品** | **漏洞个数** | **未授权远程利用个数** | **最高CVSS评分** |
| Oracle Communications | 79 | 63 | 9.9 |
| Oracle Big Data Graph | 2 | 1 | 9.8 |
| Oracle Essbase | 2 | 1 | 9.8 |
| Oracle Commerce | 2 | 2 | 9.8 |
| Oracle Communications Applications | 39 | 31 | 9.8 |
| Oracle Construction and Engineering | 7 | 4 | 9.8 |
| Oracle Enterprise Manager | 3 | 2 | 9.8 |
| Oracle Financial Services Applications | 16 | 12 | 9.8 |
| Oracle Fusion Middleware | 50 | 39 | 9.8 |
| Oracle Health Sciences Applications | 2 | 2 | 9.8 |
| Oracle HealthCare Applications | 4 | 2 | 9.8 |
| Oracle Hyperion | 2 | 2 | 9.8 |
| Oracle JD Edwards | 2 | 1 | 9.8 |
| Oracle MySQL | 37 | 8 | 9.8 |
| Oracle PeopleSoft | 12 | 10 | 9.8 |
| Oracle Siebel CRM | 2 | 1 | 9.8 |
| Oracle Support Tools | 6 | 6 | 9.8 |
| Oracle Systems | 2 | 1 | 9.8 |
| Oracle Utilities Applications | 7 | 7 | 9.8 |
| Oracle Hospitality Applications | 1 | 0 | 8.8 |
| Oracle Food and Beverage Applications | 7 | 2 | 8.3 |
| Oracle Java SE | 4 | 4 | 8.1 |
| Oracle Virtualization | 6 | 1 | 8.1 |
| Oracle Supply Chain | 8 | 5 | 7.8 |
| Oracle Database Products Risk Matrices | 9 | 1 | 7.5 |
| Oracle Database Server | 9 | 1 | 7.5 |
| Oracle E-Business Suite | 12 | 10 | 7.5 |
| Oracle Retail Applications | 1 | 1 | 7.5 |
| Oracle Global Lifecycle Management | 3 | 0 | 6.5 |
| Oracle GoldenGate | 3 | 0 | 6.5 |
| Oracle Graph Server and Client | 1 | 0 | 6.5 |
| Oracle Spatial Studio | 1 | 0 | 6.5 |
| Oracle TimesTen In-Memory Database | 1 | 0 | 6.5 |
| Oracle Insurance Applications | 1 | 1 | 6.5 |

## ****三、漏洞防护****

* **补丁更新**

请用户参考本文附录“受影响产品及补丁信息”及时下载受影响产品更新补丁，并参照补丁安装包中的readme文件进行安装更新，以保证长期有效的防护。

注：Oracle官方补丁需要用户持有正版软件的许可账号，使用该账号登陆https://support.oracle.com后，可以下载最新补丁。

* **W****eblogic临时防护措施**

**3****.2.1 限制T3协议访问**

若相关用户暂时无法安装补丁或不通过T3协议进行JVM通信，可使用下列措施阻断针对利用T3协议漏洞的攻击：

WebLogic Server提供了名为 weblogic.security.net.ConnectionFilterImpl 的默认连接筛选器，此连接筛选器接受所有传入连接，可通过此连接筛选器配置规则，对T3及T3s协议进行访问控制，详细操作步骤如下：

1. 进入WebLogic控制台，在base\_domain的配置页面中，进入“安全”选项卡页面，点击“筛选器”，进入连接筛选器配置。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_2-2-300x170.png)

2. 在连接筛选器中输入：weblogic.security.net.ConnectionFilterImpl，参考以下写法，在连接筛选器规则中配置符合企业实际情况的规则：

|  |
| --- |
| 127.0.0.1 \* \* allow t3 t3s 本机IP \*\* allow t3 t3s  允许访问的IP  \* \* allow t3 t3s  \* \* \* deny t3 t3s |

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_3-2-300x146.png)

|  |
| --- |
| 连接筛选器规则格式如下：target localAddress localPort action protocols，其中： · target 指定一个或多个要筛选的服务器。  · localAddress 可定义服务器的主机地址。(如果指定为一个星号 (\*)，则返回的匹配结果将是所有本地 IP 地址。)  · localPort 定义服务器正在监听的端口。(如果指定了星号，则匹配返回的结果将是服务器上所有可用的端口)。  · action 指定要执行的操作。(值必须为“allow”或“deny”。)  · protocols 是要进行匹配的协议名列表。(必须指定下列其中一个协议：http、https、t3、t3s、giop、giops、dcom 或 ftp。) 如果未定义协议，则所有协议都将与一个规则匹配。 |

3. 保存后若规则未生效，建议重新启动WebLogic服务（重启WebLogic服务会导致业务中断，建议相关人员评估风险后，再进行操作）。以Windows环境为例，重启服务的步骤如下：

进入域所在目录下的bin目录，在Windows系统中运行stopWebLogic.cmd文件终止WebLogic服务，Linux系统中则运行stopWebLogic.sh文件。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_4-2-300x252.png)

待终止脚本执行完成后，再运行startWebLogic.cmd或startWebLogic.sh文件启动WebLogic，即可完成WebLogic服务重启。

**3****.2.****2****关闭IIOP协议**

用户可通过关闭IIOP协议阻断针对利用IIOP协议漏洞的攻击，操作如下：

在WebLogic控制台中，选择“服务”->“AdminServer”->“协议”，取消“启用IIOP”的勾选。并重启WebLogic项目，使配置生效。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_5-2-300x183.png)

****附录 受影响产品及补丁信息****

|  |  |
| --- | --- |
| ****受影响产品及版本号**** | ****可用补丁**** |
| Big Data Spatial and Graph, versions prior to 21.4.3, prior to 23.1.0 | https://support.oracle.com/rs?type=doc&id=2906899.1 |
| Enterprise Manager Base Platform, versions 13.4.0.0, 13.5.0.0 | https://support.oracle.com/rs?type=doc&id=2906900.1 |
| Enterprise Manager Ops Center, version 12.4.0.0 | https://support.oracle.com/rs?type=doc&id=2906900.1 |
| Fujitsu M10-1, M10-4, M10-4S, M12-1, M12-2, M12-2S Servers, versions prior to XCP2411, prior to XCP3111, prior to XCP4011 | https://support.oracle.com/rs?type=doc&id=2920776.1 |
| GoldenGate Stream Analytics, versions prior to 19.1.0.0.8 | https://support.oracle.com/rs?type=doc&id=2906899.1 |
| GoldenGate Veridata, versions prior to 12.2.1.4.220831 | https://support.oracle.com/rs?type=doc&id=2906899.1 |
| JD Edwards EnterpriseOne Orchestrator, versions prior to 9.2.7.2 | https://support.oracle.com/rs?type=doc&id=2915506.1 |
| JD Edwards EnterpriseOne Tools, versions prior to 9.2.7.2 | https://support.oracle.com/rs?type=doc&id=2915506.1 |
| Management Cloud Engine, version 22.1.0.0.0 | https://support.oracle.com/rs?type=doc&id=2919078.1 |
| Management Pack for Oracle GoldenGate, versions prior to 12.2.1.2.221115 | https://supp...