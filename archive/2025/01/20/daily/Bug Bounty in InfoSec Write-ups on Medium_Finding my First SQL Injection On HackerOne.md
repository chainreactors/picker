---
title: Finding my First SQL Injection On HackerOne
url: https://infosecwriteups.com/finding-my-first-sql-injection-on-hackerone-6a031ab5aa1c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-20
fetch_date: 2025-10-06T20:09:02.843671
---

# Finding my First SQL Injection On HackerOne

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6a031ab5aa1c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-my-first-sql-injection-on-hackerone-6a031ab5aa1c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-my-first-sql-injection-on-hackerone-6a031ab5aa1c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6a031ab5aa1c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6a031ab5aa1c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Finding my First SQL Injection On HackerOne

[![Aleksa Zatezalo](https://miro.medium.com/v2/resize:fill:64:64/1*NC7SQUXrhwE3X0RCiS66BA.jpeg)](https://aleksazatezalo.medium.com/?source=post_page---byline--6a031ab5aa1c---------------------------------------)

[Aleksa Zatezalo](https://aleksazatezalo.medium.com/?source=post_page---byline--6a031ab5aa1c---------------------------------------)

5 min read

·

Jan 19, 2025

--

5

Listen

Share

![]()

Source: <https://www.linkedin.com/pulse/sql-injection-meera-ramanujam/>

SQL injections have been a persistent aspect of web application security, maintaining their position on OWASP’s top 10 vulnerabilities year after year. Like an old adversary that refuses to be defeated, they continue to emerge in modern applications despite decades of awareness and documentation. Whether they lead to a full system compromise or yield limited information disclosure, discovering a SQL injection vulnerability never fails to get a security researcher’s heart racing. This excitement recently became personal when I stumbled upon my first bug bounty SQL injection on a platform dedicated to hosting cultural content. In this post, I’ll walk you through the discovery process and discuss key takeaways from this experience.

The vulnerability I discovered centers on a critical parameter injection in Itaú Cultural’s agenda system. When users interact with [www.itaucultural.org.br/agenda-cultural](http://www.itaucultural.org.br/agenda-cultural), the application makes backend requests to [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org) for certain operations. During my testing, I identified that the ‘tag’ parameter in requests to the backend server was vulnerable to time-based SQL injection. This allowed me to execute SQL commands on the underlying MySQL database hosted on prod-conteudo-portal-ic-2022.i-nove.org. While time-based SQL injections can be more challenging to exploit compared to their error-based or union-based counterparts, they still present significant security concerns. Despite multiple attempts to expand the exploitation scope, I was limited to time-based techniques and couldn’t achieve broader access to the database. In the following sections, I’ll walk through the exact steps to reproduce this vulnerability and explain the technical details of the injection point.

**Note:** *The vulnerability has been resolved as of this publication. It was part of a vulnerability disclosure program and did not pay out any bounties.*

## Steps to identification

I started by accessing [www.itaucultural.org.br](http://www.itaucultural.org.br/) and proxying data through Burpsuite Pro. After accessing [www.itaucultural.org.br/agenda-cultural](http://www.itaucultural.org.br/agenda-cultural), I noticed numerous search requests made to [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org/) with search terms ‘site’ and ‘tag’ included as URL parameters. The HTTP history involving [www.itaucultural.org.br/agenda-cultural](http://www.itaucultural.org.br/agenda-cultural) and [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org/) is seen on the highlighted lines below (299 and 345).

Press enter or click to view image in full size

![]()

API calls originaitng from itaucultural

Sending a request to Burp’s repeater that queries [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org/) for podcast content returns a large response containting data in a JSON format indicating that the request might be retrieving data from a database.

Press enter or click to view image in full size

![]()

JSON Response containing Data

Adding a single quote (‘) to the end of the tag parameter returns Status Code 500 as seen below, indicating that the parameter tag is passed directly to an SQL query without parameterization.

Press enter or click to view image in full size

![]()

SQL injection confirmed

Adding a URL-encoded, time-based SQLi (*“‘ and (select\*from(select(sleep(20)))a) — “*) to the tag parameter, delays the response in proportion to the time included in the query indicating an SQLi. As seen in the screenshot below, the Referer for [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org/) is <https://www.itaucultural.org.br/> indicating that [www.prod-conteudo-portal-ic-2022.i-nove.org](http://www.prod-conteudo-portal-ic-2022.i-nove.org/) represents a back-end data retrieval service for [www.itaucultural.org.br](http://www.itaucultural.org.br/).

Press enter or click to view image in full size

![]()

SQL injection impact demonstrated

## Impact

The identified time-based SQL injection vulnerability allows an attacker to interact directly with the backend database by injecting arbitrary SQL queries into the vulnerable parameter. This can lead to the following potential security risks described below.

**Database Enumeration:** Attackers can infer sensitive information about the database structure, such as table names, column names, and other metadata, by exploiting time delays in the response.

**Privilege Escalation:** If exploited further, the vulnerability may reveal critical information about user roles and privileges, potentially allowing attackers to identify superuser accounts or administrative credentials.

**Data Extraction:** By chaining this vulnerability with advanced techniques, attackers can exfiltrate sensitive data such as usernames, passwords, or personally identifiable information (PII) from the database without triggering alarms.

**Denial of Service (DoS):** An attacker can abuse database queries to introduce significant delays in database responses, impacting the application’s performance and potentially leading to a denial of service for legitimate users.

**Reputation and Compliance Risks:** Exposing sensitive data or impa...