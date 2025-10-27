---
title: Oracle Patch Tuesday, July 2023 Security Update Review
url: https://buaq.net/go-172451.html
source: unSafe.sh - 不安全
date: 2023-07-20
fetch_date: 2025-10-04T11:51:14.062038
---

# Oracle Patch Tuesday, July 2023 Security Update Review

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Oracle Patch Tuesday, July 2023 Security Update Review

Oracle has released its third quarterly edition of Critical Patch Update, which contains a grou
*2023-7-19 23:56:6
Author: [blog.qualys.com(查看原文)](/jump-172451.htm)
阅读量:21
收藏*

---

Oracle has released its third quarterly edition of Critical Patch Update, which contains a group of patches for **508** security vulnerabilities. Some of the vulnerabilities addressed this month impact more than one product. These patches address vulnerabilities in Oracle code and third-party components included in Oracle products.

During Q3 2023 Oracle Critical Patch Update, the Oracle Financial Services Applications received the highest number of 147 patches, constituting 29% of the total patches released. Oracle Communications and Oracle Fusion Middleware followed, with 77 and 60 patches, respectively.

449 of the 508, i.e.,88% of security patches, are for non-Oracle CVEs, which are security fixes for issues in third-party products such as open-source components included and exploitable in the context of their Oracle product distributions.

In these security updates, Oracle has covered product families, including Oracle Database Server, Oracle Application Express, Oracle Essbase, Oracle GoldenGate, Oracle Graph Server and Client, Oracle Spatial Studio, Oracle TimesTen In-Memory Database, Oracle Commerce, Oracle Communications Applications, Oracle Communications, Oracle Construction and Engineering, Oracle E-Business Suite, Oracle Enterprise Manager, Oracle Financial Services Applications, Oracle Food and Beverage Applications, Oracle Fusion Middleware, Oracle Analytics, Oracle Health Sciences Applications, Oracle Hospitality Applications, Oracle Hyperion, Oracle Insurance Applications, Oracle Java SE, Oracle JD Edwards, Oracle MySQL, Oracle PeopleSoft, Oracle Policy Automation, Oracle Retail Applications, Oracle Siebel CRM, Oracle Supply Chain, Oracle Systems, Oracle Utilities Applications, Oracle Virtualization.

## Qualys QID Coverage

Qualys has released 7 QIDs mentioned in the table below:

|  |  |
| --- | --- |
| **QIDs** | **Title** |
| 378680 | Oracle VM VirtualBox Windows Multiple Vulnerabilities (CPUJUL2023) |
| 378679 | Oracle Solaris 11.4 Support Repository Update (SRU) 56.138.2 Missing (CPUAPR2023) |
| 378678 | Oracle MySQL Connector/ODBC Critical Patch Update (CPU) July 2023 (CPUJULY2023) |
| 378677 | Oracle Hypertext Transfer Protocol Server (HTTP Server) Server Multiple Vulnerabilities (CPUJUL2023) |
| 378675 | Oracle Coherence July 2023 Critical Patch Update (CPUJUL2023) |
| 296101 | Oracle Solaris 11.4 Support Repository Update (SRU) 59.138.2 Missing (CPUJUL2023) |
| 20357 | Oracle MySQL July 2023 Critical Patch Update (CPUJULY2023) |

**Note:** The table will be updated with the additional QIDs once released.

## Notable Oracle Vulnerabilities Patched

### Oracle Financial Services Applications

This Critical Patch Update for Oracle Financial Services Applications contains **147** security patches. **115** of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-1471, CVE-2022-46364, CVE-2022-45047, and CVE-2022-31692 in different Oracle Financial Services Applications products have the highest CVSS score of 9.8.

### Oracle Communications

The Critical Patch Update for Oracle Communications contains **77** new security patches for Oracle Communications. Out of which, 57 vulnerabilities may be remotely exploitable without authentication.

CVE-2023-20862, CVE-2022-37434, CVE-2022-1471, CVE-2023-20873, and CVE-2022-36944 in different products of Oracle Communications have the highest CVSS score of 9.8.

### Oracle Fusion Middleware

The Critical Patch Update for Oracle Fusion Middleware contains **60** new security patches. 40 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-42920, CVE-2022-45047, CVE-2023-25690, CVE-2021-42575, CVE-2022-41853, CVE-2021-43113, and CVE-2023-26119 in different products of Oracle Fusion Middleware have the highest CVSS score of 9.8.

### Oracle MySQL

The Critical Patch Update contains **24** new security patches for Oracle MySQL. 11 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2023-20862 has the highest CVSS score of 9.8. The vulnerability affects MySQL Enterprise Monitor version 8.0.34 and prior.

### Oracle Analytics

The Critical Patch Update contains **32** new security patches for Oracle MySQL. 23 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-46364, CVE-2022-29361, CVE-2019-17531, CVE-2019-13990, CVE-2022-1471, and CVE-2022-33980 in BI Publisher and Oracle Business Intelligence Enterprise Edition have the highest CVSS score of 9.8.

### Oracle Communications Applications

The Critical Patch Update for Oracle Communications Applications contains **40** new security patches, and 30 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-1471, CVE-2021-42575, CVE-2022-46364, CVE-2022-31692, CVE-2023-20873, and CVE-2023-20862 in different products of Oracle Communications Applications have the highest CVSS score of 9.8.

### Oracle Database Server

The Critical Patch Update for Oracle Database Products contains **five** new security patches. One of these vulnerabilities may be remotely exploitable without authentication. On the other hand, one of these patches applies to client-only installations, i.e., installations that do not have the Oracle Database Server installed.

The Oracle Database Server products and versions affected by vulnerabilities are:

* Oracle Text (LibExpat), version 21.3 through 21.10
* OML4PY (cryptography), version 21.3 through 21.10
* Java VM, version 19.3 through 19.19 and 21.3 through 21.10

### Oracle Utilities Applications

The Critical Patch Update for Oracle Utilities Applications contains **14** new security patches. 12 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-1471, CVE-2023-20873, and CVE-2023-20862 in Oracle Utilities Testing Accelerator and Oracle Utilities Network Management System have the highest CVSS score of 9.8.

### Oracle Supply Chain

The Critical Patch Update for Oracle Supply Chain contains **13** new security patches. 11 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-37434 and CVE-2022-27404 in Oracle Agile Engineering Data Management and Oracle AutoVue have the highest CVSS score of 9.8.

### Oracle Retail Applications

The Critical Patch Update contains **11** new security patches for Oracle Retail Applications. 8 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-37434 in Oracle Retail Advanced Inventory Planning has the highest CVSS score of 9.8.

### Oracle Commerce

The Critical Patch Update contains **8** new security patches for Oracle Commerce. All of these vulnerabilities may be remotely exploitable without authentication.

The Oracle Commerce products and versions affected by vulnerabilities are:

* Oracle Commerce Guided Search, version 11.3.2
* Oracle Commerce Platform, version 11.3.0, 11.3.1, and 11.3.2

### Oracle E-Business Suite

The Critical Patch Update contains **five** new security patches for Oracle E-Business Suite. Three of these vulnerabilities may be remotely exploitable without authentication.

The highest CVSS Score of vulnerabilities affecting Oracle E-Business Suite is 6.5.

The Oracle E-Business Suite products and versions affected by vulnerabilities are:

* Oracle Scripting versions 12.2.3 through 12.2.12
* Oracle Applications Framework vers...