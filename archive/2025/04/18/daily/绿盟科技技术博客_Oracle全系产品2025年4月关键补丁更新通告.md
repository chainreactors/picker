---
title: Oracle全系产品2025年4月关键补丁更新通告
url: https://blog.nsfocus.net/oracle-2/
source: 绿盟科技技术博客
date: 2025-04-18
fetch_date: 2025-10-06T22:05:28.234776
---

# Oracle全系产品2025年4月关键补丁更新通告

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

# Oracle全系产品2025年4月关键补丁更新通告

### Oracle全系产品2025年4月关键补丁更新通告

[2025-04-17](https://blog.nsfocus.net/oracle-2/ "Oracle全系产品2025年4月关键补丁更新通告")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 2,091

****一、概述****

2025年4月16日，绿盟科技CERT监测到Oracle官方发布了4月重要补丁更新公告CPU（Critical Patch Update），此次共修复了390个不同程度的漏洞，本次安全更新涉及Oracle MySQL Connectors、Oracle MySQL Server、Oracle Java SE、Oracle Fusion Middleware、Oracle Financial Services Applications、Oracle Communications Applications等多个常用产品。Oracle强烈建议客户尽快应用关键补丁更新修复程序，对漏洞进行修复。

参考链接：

https://www.oracle.com/security-alerts/cpuapr2025.html

****二、重点漏洞概述****

根据产品流行度和漏洞重要性筛选出此次更新中包含影响较大的漏洞，请相关用户重点进行关注：

****Oracle********MySQL Connectors内存破坏漏洞********（********CVE-2025-30706********）：****

Oracle MySQL Connectors中存在内存破坏漏洞。具有普通用户权限的攻击者可通过多种协议进行网络访问，从而接管MySQL Connectors。CVSS评分为7.5。

****Oracle VM VirtualBox身份验证********绕过********漏洞********（CVE-2025-30712）：****

Oracle VM VirtualBox中存在身份验证绕过漏洞。未经身份验证的攻击者可登录Oracle VM VirtualBox的基础设施，从而增删改查所有Oracle VM VirtualBox可访问的数据及导致部分拒绝服务。CVSS评分为8.1。

****Oracle Common Applications身份验证********绕过********漏洞********（****[****CVE-2025-30716****](https://www.cvedetails.com/cve/CVE-2025-30716/)****）：****

Oracle Common Applications中存在身份验证绕过漏洞。未经身份验证的攻击者可通过构造HTTP请求绕过Oracle Common Applications验证，从而查询所有Oracle Common Applications可访问的数据。CVSS评分为7.5。

Oracle官方4月关键补丁更新漏洞总结如下：

|  |  |  |  |
| --- | --- | --- | --- |
| ****产品**** | ****漏洞个数**** | ****未授权远程利用的个数**** | ****最高CVSS评分**** |
| Oracle Database Products Risk Matrices | 7 | 3 | 7.4 |
| Oracle Database Server | 7 | 3 | 7.4 |
| Oracle Application Express | 1 | 1 | 7.5 |
| Oracle Autonomous Health Framework | 1 | 1 | 7.5 |
| Oracle Essbase | 1 | 0 | 4.1 |
| Oracle GoldenGate | 4 | 2 | 7.5 |
| Oracle Graph Server and Client | 1 | 1 | 5.3 |
| Oracle NoSQL Database | 1 | 0 | 6.7 |
| Oracle REST Data Services | 1 | 0 | 6.7 |
| Oracle Secure Backup | 1 | 0 | 6.7 |
| Oracle SQL Developer | 2 | 2 | 7.5 |
| Oracle TimesTen In-Memory Database | 2 | 2 | 7.5 |
| Oracle Commerce | 6 | 5 | 9.8 |
| Oracle Communications Applications | 42 | 35 | 9.8 |
| Oracle Communications | 103 | 82 | 9.8 |
| Oracle Construction and Engineering | 7 | 6 | 7.5 |
| Oracle E-Business Suite | 16 | 11 | 9.8 |
| Oracle Enterprise Manager | 4 | 4 | 9.8 |
| Oracle Financial Services Applications | 34 | 22 | 9.8 |
| Oracle Food and Beverage Applications | 3 | 2 | 7.6 |
| Oracle Fusion Middleware | 31 | 26 | 9.8 |
| Oracle Analytics | 15 | 11 | 9.8 |
| Oracle Hospitality Applications | 3 | 2 | 9.8 |
| Oracle Hyperion | 3 | 2 | 9.1 |
| Oracle Insurance Applications | 1 | 1 | 7.5 |
| Oracle Java SE | 6 | 5 | 7.7 |
| Oracle JD Edwards | 8 | 5 | 9.8 |
| Oracle MySQL | 43 | 2 | 9.1 |
| Oracle PeopleSoft | 4 | 1 | 8.1 |
| Oracle Policy Automation | 3 | 3 | 7.5 |
| Oracle Retail Applications | 11 | 11 | 9.8 |
| Oracle Siebel CRM | 4 | 2 | 7.5 |

****三、漏洞防护****

* + **补丁更新**

请用户参考本文附录“受影响产品及补丁信息”及时下载受影响产品更新补丁，并参照补丁安装包中的readme文件进行安装更新，以保证长期有效的防护。

注：Oracle官方补丁需要用户持有正版软件的许可账号，使用该账号登陆https://support.oracle.com后，可以下载最新补丁。

* **Weblogic临时防护措施**

* **限制T3协议访问**

若相关用户暂时无法安装补丁或不通过T3协议进行JVM通信，可使用下列措施阻断针对利用T3协议漏洞的攻击：

WebLogic Server提供了名为 weblogic.security.net.ConnectionFilterImpl 的默认连接筛选器，此连接筛选器接受所有传入连接，可通过此连接筛选器配置规则，对T3及T3s协议进行访问控制，详细操作步骤如下：

1. 进入Weblogic控制台，在base\_domain的配置页面中，进入“安全”选项卡页面，点击“筛选器”，进入连接筛选器配置。

![](https://blog.nsfocus.net/wp-content/uploads/2025/04/图片19-1-300x170.png)

2. 在连接筛选器中输入：security.net.ConnectionFilterImpl，参考以下写法，在连接筛选器规则中配置符合企业实际情况的规则：

|  |
| --- |
| 127.0.0.1 \* \* allow t3 t3s 本机IP \* \* allow t3 t3s  允许访问的IP  \* \* allow t3 t3s  \* \* \* deny t3 t3s |

![](https://blog.nsfocus.net/wp-content/uploads/2025/04/图片20-1-300x146.png)

|  |
| --- |
| 连接筛选器规则格式如下：target localAddress localPort action protocols，其中： l target 指定一个或多个要筛选的服务器。  l localAddress 可定义服务器的主机地址。(如果指定为一个星号 (\*)，则返回的匹配结果将是所有本地 IP 地址。)  l localPort 定义服务器正在监听的端口。(如果指定了星号，则匹配返回的结果将是服务器上所有可用的端口)。  l action 指定要执行的操作。(值必须为“allow”或“deny”。)  protocols 是要进行匹配的协议名列表。(必须指定下列其中一个协议：http、https、t3、t3s、giop、giops、dcom 或 ftp。) 如果未定义协议，则所有协议都将与一个规则匹配。 |

3. 保存后若规则未生效，建议重新启动Weblogic服务（重启Weblogic服务会导致业务中断，建议相关人员评估风险后，再进行操作）。以Windows环境为例，重启服务的步骤如下：

* 进入域所在目录下的bin目录，在Windows系统中运行cmd文件终止weblogic服务，Linux系统中则运行stopWebLogic.sh文件。

![](https://blog.nsfocus.net/wp-content/uploads/2025/04/图片21-1-300x252.png)

* 待终止脚本执行完成后，再运行cmd或startWebLogic.sh文件启动Weblogic，即可完成Weblogic服务重启。

参考链接：https://docs.oracle.com/cd/E24329\_01/web.1211/e24485/con\_filtr.htm#SCPRG377

* **禁用I****IOP****协议**

用户可通过关闭IIOP协议阻断针对利用IIOP协议漏洞的攻击，操作如下：

在Weblogic控制台中，选择“服务”->”AdminServer”->”协议”，取消“启用IIOP”的勾选。并重启Weblogic项目，使配置生效。

![](https://blog.nsfocus.net/wp-content/uploads/2025/04/图片22-1-300x183.png)

****附录 受影响产品及补丁信息****

|  |  |
| --- | --- |
| ****受影响产品及版本号**** | ****可用补丁**** |
| Autonomous Health Framework, versions 23.8.0-23.11.0, 24.1.0-24.11.0, 25.1.0, 25.2.0 | https://support.oracle.com/rs?type=doc&id=3070732.1 |
| GoldenGate Stream Analytics, versions 19.1.0.0.0-19.1.0.0.10 | https://support.oracle.com/rs?type=doc&id=3070732.1 |
| JD Edwards EnterpriseOne Tools, versions 9.2.0.0-9.2.9.2 | https://support.oracle.com/rs?type=doc&id=3078792.1 |
| Management Cloud Engine, version 24.3.0 | https://support.oracle.com/rs?type=doc&id=3079189.1 |
| MySQL Client, versions 8.0.0-8.0.41, 8.4.0-8.4.4, 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Cluster, versions 7.6.0-7.6.33, 8.0.0-8.0.41, 8.4.0-8.4.4, 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Connectors, versions 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Enterprise Backup, versions 8.0.0-8.0.41, 8.4.0-8.4.4, 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Server, versions 8.0.0-8.0.41, 8.4.0-8.4.4, 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Shell, versions 8.0.32-8.0.41, 8.4.0-8.4.4, 9.0.0-9.2.0 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| MySQL Workbench, versions 8.0.0-8.0.41 | https://support.oracle.com/rs?type=doc&id=3078827.1 |
| Oracle Access Manager, version 12.2.1.4.0 | https://support.oracle.com/rs?type=doc&id=3078819.2 |
| Oracle Agile Engineering Data Management, version 6.2.1 | https://support.oracle.com/rs?type=doc&id=3078833.1 |
| Oracle Application Express, versions 23.2.15, 23.2.16, 24.1.9, 24.1.10, 24.2.3, 24.2.4 | https://support.oracle.com/rs?type=doc&id=3070732.1 |
| Oracle Application Testing Suite, version 13.3.0.1 | https://support.oracle.com/rs?type=doc&id=3070733.1 |
| Oracle Banking APIs, versions 21.1.0.0.0, 22.1.0.0.0, 22.2.0.0.0 | https://support.oracle.com |
| Oracle Banking Corporate Lending Process Management, versions 14.5.0.0.0-14.7.0.0.0 | https://support.oracle.com |
| Oracle Banking Digital Experience, versions 21.1.0.0.0, 22.1...