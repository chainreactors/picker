---
title: Discovery of Blind SQL Injection and OS Command Injection Vulnerabilities in a University Portal
url: https://infosecwriteups.com/discovery-of-blind-sql-injection-and-os-command-injection-vulnerabilities-in-a-university-portal-064929692019?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:29:04.472644
---

# Discovery of Blind SQL Injection and OS Command Injection Vulnerabilities in a University Portal

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F064929692019&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovery-of-blind-sql-injection-and-os-command-injection-vulnerabilities-in-a-university-portal-064929692019&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovery-of-blind-sql-injection-and-os-command-injection-vulnerabilities-in-a-university-portal-064929692019&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-064929692019---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-064929692019---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Discovery of Blind SQL Injection and OS Command Injection Vulnerabilities in a University Portal

[![Avyukt Security](https://miro.medium.com/v2/resize:fill:64:64/1*5jGxXKsgQjjFNintRNHdwg.jpeg)](https://medium.com/%40avyuktsec?source=post_page---byline--064929692019---------------------------------------)

[Avyukt Security](https://medium.com/%40avyuktsec?source=post_page---byline--064929692019---------------------------------------)

9 min read

·

Aug 2, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

By: Vedant Bhalgama (@ActiveXSploit)

One day during reconnaissance on a university website, I was exploring various endpoints and gathering intel that could potentially lead to vulnerabilities. While conducting subdomain enumeration, I came across two subdomains — one appeared to be quite old, while the other seemed relatively new. Interestingly, both were publicly accessible over the Internet.

After some tinkering with both sites, I identified a straightforward yet classic SQL Injection vulnerability present in each. Additionally, the newer subdomain was found to be vulnerable to blind command injection.

In this post, I’ll walk you through the overall process I followed to uncover these vulnerabilities. However, to avoid exposing sensitive information about the target, I’ll only be showcasing one of the subdomains with a limited set of screenshots.

## - 0x01: Summary of the Methodology Used to Discover the Vulnerabilities (TL;DR):

* Performed subdomain enumeration and discovered two exposed subdomains.
* Interacted with both, identifying a university appraisal system for employees login portal built on ASPX, hinting at an MSSQL backend.
* Discovered a working blind-SQL Injection on both subdomains, used it to bypass login on one of the subdomains and later dump the database via Ghauri.
* Noticed the MSSQL backend and attempted command execution using `xp_cmdshell`, which was disabled by default but could be enabled due to high privileges.
* Achieved blind command execution by triggering response delays through `ping` and custom `PowerShell` queries, confirming successful RCE without direct output.
* Tested whether outbound access was allowed by setting up a webhook and attempting to send a request to it. Unfortunately, the server had outbound access disabled.

## - 0x02: Discovering Additional Subdomains via Enumeration :

* For the purpose of this post, we’ll refer to the target website as **target.com** to avoid disclosing any information related to the actual organization.
* As usual, I started with subdomain enumeration to discover additional subdomains associated with target.com and identify any that seemed interesting or worth exploring further.

I used various tools and techniques to discover subdomains, which are :

* Google Dorks (for eg. site:\*.target.com -www)
* [crt.sh](https://crt.sh/)
* [SubFinder](https://github.com/projectdiscovery/subfinder)
* OWASP Amass
* While reviewing the newly discovered subdomains, I came across several, but two stood out — one was a subdomain hosting an application which seemed old enough (from 2019–20) and had been left exposed to the internet, and the other was a relatively recent one (from 2023–24), hosting a an appraisal system for university employees.

Press enter or click to view image in full size

![]()

The two subdomains that were identified were as follows:

* apps.target.com
* `targetname`web.target.com (Where `targetname` is the actual name of the target organization)

## - 0x03: Discovering a Blind-SQLi Vulnerability on the Login Portal:

* I began exploring the relatively newer application from 2023–24, hosted on **apps.target.com**. It appeared to be an appraisal system used by university employees.
* I also noticed that the site was pretty basic and built using ASPX, suggesting that it was running on an IIS web server with a likely MSSQL backend.

Press enter or click to view image in full size

![]()

* After reaching the login portal, the next logical step was to test for SQL Injection by injecting quotes into the input fields. If the application was vulnerable, it would either throw a SQL syntax error or exhibit noticeable changes in its behavior.
* And to my surprise, the application did in fact display a SQL syntax error on the screen — sweet! This confirmed that the application was vulnerable to SQL Injection, and I could proceed to attempt dumping the database.
* However, before attempting to dump the database, I tested a classic SQL Injection-based authentication bypass payload — and it worked. I successfully bypassed the login page and gained access to sensitive appraisal-related information of an employee, along with much more.

```
' or 1=1- -
```

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

* Next, I attempted to manually extract information from the login page by executing various MSSQL injection queries. Since the application was returning SQL syntax errors, I expected it might also return query results. However, that wasn’t the case — every time I executed a valid query, the application simply responded with an “Invalid login” message. Interestingly, if I intentionally introduced an error in the query, the application did display a SQL syntax error. This indicated that the application was vulnerable to a **semi-blind SQL Injection**, where SQL errors are reflected but actual query results are not.
* Next, I used **Ghauri** — a tool similar to SQLMap — to automate the SQL Injection exploitation process and dump the database of the **target.com** site. It streamlined the process and made extracting data significantly easier.

![]()

## - 0x04: Blind Command Execution via xp\_cmdshell:

* Even after successfully retrieving the database information from the target site, I wasn’t quit...