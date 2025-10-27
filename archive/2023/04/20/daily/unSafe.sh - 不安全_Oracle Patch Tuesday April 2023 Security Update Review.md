---
title: Oracle Patch Tuesday April 2023 Security Update Review
url: https://buaq.net/go-159471.html
source: unSafe.sh - 不安全
date: 2023-04-20
fetch_date: 2025-10-04T11:32:45.778364
---

# Oracle Patch Tuesday April 2023 Security Update Review

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

Oracle Patch Tuesday April 2023 Security Update Review

Oracle has released the second quarterly edition of Critical Patch Update, which contains a gro
*2023-4-19 19:47:21
Author: [blog.qualys.com(查看原文)](/jump-159471.htm)
阅读量:32
收藏*

---

Oracle has released the second quarterly edition of Critical Patch Update, which contains a group of patches for **433** security vulnerabilities. Some of the vulnerabilities addressed this month impact various products. These patches address vulnerabilities in Oracle code and third-party components included in Oracle products.

During Q2 2023 Oracle Critical Patch Update, the Oracle Communications product suite recorded the highest number of patches at 77, constituting 17% of the total patches released. The Oracle Financial Services Applications and Oracle Fusion Middleware product lines followed, with 76 and 49 patches, respectively. Also, Oracle MySQL receives 34 new security updates.

341 of the 433, i.e.,79% of security patches, are for non-Oracle CVEs, which are security fixes for issues in third-party products such as open-source components included and exploitable in the context of their Oracle product distributions.

In this security updates, Oracle has covered product families, including Oracle Database Server, Oracle Blockchain Platform, Oracle Essbase, Oracle GoldenGate, Oracle Graph Server and Client, Oracle NoSQL Database, Oracle REST Data Services, Oracle SQL Developer, Oracle Commerce, Oracle Communications Applications, Oracle Communications, Oracle Construction and Engineering, Oracle E-Business Suite, Oracle Enterprise Manager, Oracle Financial Services Applications, Oracle Fusion Middleware, Oracle Analytics, Oracle Health Sciences Applications, Oracle HealthCare Applications, Oracle Hospitality Applications, Oracle Hyperion, Oracle iLearning, Oracle Insurance Applications, Oracle Java SE, Oracle JD Edwards, Oracle MySQL, Oracle PeopleSoft, Oracle Retail Applications, Oracle Siebel CRM, Oracle Supply Chain, Oracle Systems, Oracle Utilities Applications, and Oracle Virtualization.

## Qualys QID Coverage

Qualys has released 8 QIDs mentioned in the table below:

|  |  |
| --- | --- |
| **QIDs** | **Title** |
| 87542 | Oracle WebLogic Server Multiple Vulnerabilities (CPUAPR2023) |
| 296097 | Oracle Solaris 11.4 Support Repository Update (SRU) 55.138.3 Missing (CPUAPR2023) |
| 296096 | Oracle Solaris 11.4 Support Repository Update (SRU) 56.138.2 Missing (CPUAPR2023) |
| 296095 | Oracle Solaris 11.4 Support Repository Update (SRU) 54.138.1 Missing (CPUAPR2023) |
| 296094 | Oracle Solaris 11.3 Support Repository Update (SRU) 36.31.0 Missing (CPUAPR2023) |
| 378425 | Oracle Java Standard Edition (SE) Critical Patch Update – April 2023 (CPUAPR2023) |
| 20343 | Oracle Database 19c Critical OJVM Patch Update – April 2023 |
| 20342 | Oracle Database 21c Critical Patch Update – April 2023 |

**Note:** The table will be updated with the additional QIDs once released.

## Notable Oracle Vulnerabilities Patched

### Oracle Communications

The Critical Patch Update for Oracle Communications contains **77** new security patches for Oracle Communications. Out of which 65 vulnerabilities may be remotely exploitable without authentication.

The CVE-2022-43401 and CVE-2022-43402 are the vulnerabilities in Oracle Communications Cloud Native Core Automated Test Suite of Oracle Communications that has the highest CVSS v3.1 Base Score of 9.9 in this group.

These are sandbox bypass vulnerabilities that affect several Jenkins plugins. An authenticated attacker may execute arbitrary code within the Jenkins JVM controller by exploiting the vulnerabilities.

### Oracle Financial Services Applications

This Critical Patch Update for Oracle Financial Services Applications contains 76 security patches. 59 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-22978 and CVE-2022-46364 have the highest CVSS v3.1 Base Score of vulnerabilities affecting Oracle Financial Services Applications, 9.8.

CVE-2022-22978 can be exploited by easy misconfiguration to bypass some servlet containers.

CVE-2022-46364 exists in Apache CXF, which may allow an attacker to perform SSRF-style attacks on web services that take at least one parameter of any type.

### Oracle Fusion Middleware

The Critical Patch Update for Oracle Fusion Middleware contains 49 new security patches. 44 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2022-45047, CVE-2022-22965, CVE-2022-37434, CVE-2022-22965, CVE-2022-33980, and CVE-2022-29599 have the highest CVSS v3.1 Base Score of vulnerabilities affecting Oracle Fusion Middleware is 9.8.

The Oracle Fusion Middleware products and versions affected by vulnerabilities are:

* Oracle SOA Suite, version 12.2.1.4.0
* Oracle JDeveloper, version 12.2.1.4.0
* Oracle HTTP Server, version 12.2.1.4.0
* Oracle Data Integrator, version 12.2.1.4.0
* Oracle Access Manager, version 12.2.1.4.0
* Oracle Identity Manager, version 12.2.1.4.0
* Oracle Outside In Technology, version 8.5.6
* Oracle WebCenter Portal, version 12.2.1.4.0
* Oracle Managed File Transfer, version 12.2.1.4.0
* Oracle Coherence, version 12.2.1.4.0 and 14.1.1.0.0
* Oracle Business Process Management Suite, version 12.2.1.4.0
* Oracle Middleware Common Libraries and Tools, version 12.2.1.4.0
* Oracle WebLogic Server, version 12.2.1.3.0, 12.2.1.4.0, and 14.1.1.0.0

### Oracle MySQL

The Critical Patch Update contains 34 new security patches for Oracle MySQL. 11 vulnerabilities may be remotely exploitable without authentication. CVE-2022-37434 has the highest CVSSv3.1 Base Score of 9.8.

The Oracle MySQL products and versions affected by vulnerabilities are:

* MySQL Cluster, version 8.0.32 and prior
* MySQL Connectors, version 8.0.32 and prior
* MySQL Enterprise Monitor, version 8.0.32 and prior
* MySQL Server, version 5.7.41 and prior, 8.0.32 and prior

### Oracle Communications Applications

The Critical Patch Update for Oracle Communications Applications contains 18 new security patches, and 13 of these vulnerabilities may be remotely exploitable without authentication.

CVE-2020-35168, CVE-2022-1471, and CVE-2022-36760 are the vulnerabilities with the CVSS v3.1 Base Score of 9.8.

The Oracle Communications Applications products and versions affected by vulnerabilities are:

* Oracle Communications IP Service Activator, version 7.4.0 and 7.5.0
* Oracle Communications Unified Assurance, version 5.5.0-5.5.10 and 6.0.0-6.0.2
* Oracle Communications Unified Inventory Management, version 7.4.0, 7.4.1, 7.4.2, and 7.5.0
* Oracle Communications Convergent Charging Controller, version 6.0.1.0.0, 12.0.1.0.0-12.0.6.0.0, and 12.0.4-12.0.6
* Oracle Communications Network Charging and Control, version 6.0.1.0.0, 12.0.1.0.0-12.0.6.0.0, and 12.0.4-12.0.6
* Oracle Communications Order and Service Management, version 7.4.1

### Oracle Database Server

The Critical Patch Update for Oracle Database Products contains **five** new security patches. One of these vulnerabilities may be remotely exploitable without authentication.

The Oracle Database Server products and versions affected by vulnerabilities are:

* Java VM, version 19c, 21c
* OML4PY (Python), version 21c
* Oracle Database Recovery Manager, version 19c, 21c
* Oracle Database Spatial and Graph (Apache Commons Fileupload), version 19c, 21c
* Oracle Database Workload Manager (Apache Commons FileUpload), version 21c

### Oracle Essbase

The Critical Patch Update for Oracle Essbase Products contains **four** new security patches. All of these vulnerabilities may be remotely exploitable without authentication...