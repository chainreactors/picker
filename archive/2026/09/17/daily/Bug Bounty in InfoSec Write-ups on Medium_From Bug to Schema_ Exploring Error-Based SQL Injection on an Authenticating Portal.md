---
title: From Bug to Schema: Exploring Error-Based SQL Injection on an Authenticating Portal
url: https://infosecwriteups.com/from-bug-to-schema-exploring-error-based-sql-injection-on-an-authenticating-portal-be905548ada2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-09-17
fetch_date: 2026-09-18T06:52:20.857290
---

# From Bug to Schema: Exploring Error-Based SQL Injection on an Authenticating Portal

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-bug-to-schema-exploring-error-based-sql-injection-on-an-authenticating-portal-be905548ada2&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-bug-to-schema-exploring-error-based-sql-injection-on-an-authenticating-portal-be905548ada2&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-be905548ada2-----------------------------------------)

·

1. [Step 1: Starting from Dorking (The Entry Point)](/?source=post_page-----be905548ada2-----------------------------------------#7f22 "Step 1: Starting from Dorking (The Entry Point)")
2. [Step 2: Breaking the Query Logic with a Single Quote](/?source=post_page-----be905548ada2-----------------------------------------#6b95 "Step 2: Breaking the Query Logic with a Single Quote")
3. [Step 3: Repairing the Syntax Structure](/?source=post_page-----be905548ada2-----------------------------------------#12c2 "Step 3: Repairing the Syntax Structure")
4. [Step 4: Triggering Context Discovered via Data Conversions](/?source=post_page-----be905548ada2-----------------------------------------#23d4 "Step 4: Triggering Context Discovered via Data Conversions")
5. [Step 5: Proving Data Extraction Legally (Schema Mapping)](/?source=post_page-----be905548ada2-----------------------------------------#9e36 "Step 5: Proving Data Extraction Legally (Schema Mapping)")
6. [Conclusion & Responsible Reporting](/?source=post_page-----be905548ada2-----------------------------------------#2676 "Conclusion & Responsible Reporting")
7. [Key Takeaway for Readers](/?source=post_page-----be905548ada2-----------------------------------------#45bf "Key Takeaway for Readers")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-be905548ada2-----------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Sql Injection](https://medium.com/tag/sql-injection?source=post_page---header_tags--be905548ada2-----------------------------------------)

[Vulnerability Disclosure](https://medium.com/tag/vulnerability-disclosure?source=post_page---header_tags--be905548ada2-----------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--be905548ada2-----------------------------------------)

[Web Security](https://medium.com/tag/web-security?source=post_page---header_tags--be905548ada2-----------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page---header_tags--be905548ada2-----------------------------------------)

# From Bug to Schema: Exploring Error-Based SQL Injection on an Authenticating Portal

[![0x7ipher](https://miro.medium.com/v2/resize:fill:64:64/1*T5L7CHMwnN7mkoBrzZvMHw.png)](https://0x7ipher.medium.com/?source=post_page---byline--be905548ada2-----------------------------------------)

[0x7ipher](https://0x7ipher.medium.com/?source=post_page---byline--be905548ada2-----------------------------------------)

5 min read

·

Sep 1, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbe905548ada2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-bug-to-schema-exploring-error-based-sql-injection-on-an-authenticating-portal-be905548ada2&source=---header_actions--be905548ada2---------------------post_audio_button--------------------)

Share

> Case Study Analysis of how I identified an Error-Based SQL Injection vulnerability in a production environment via (VDP).

Press enter or click to view image in full size

![]()

> **Disclaimer:** This paper is only intended for informative and educational use. The vulnerability described here in has been identified by a Vulnerability Disclosure Program (VDP) during a designated testing period. All sensitive information that includes identifiers, domain names, and any other organization-related information has been properly anonymized or substituted with generic terms to comply with non-disclosure requirements and target privacy. No data modification has occurred in the course of anonymizing the test data.

### **Step 1: S**tarting from Dorking (The Entry Point)

When performing a vulnerability assessment through a Vulnerability Disclosure Program (VDP), my first task was to map the attack surface of the target. To discover the unknown or unreported assets, I resorted to passive reconnaissance with the help of search engine optimization filters, famously called “**Google Dorking**”.

Press enter or click to view image in full size

![]()

By using a simple wildcard domain query, I filtered out the main website to look purely for exposed subdomains: site:\*.example.com

Press enter or click to view image in full size

![]()

Among the indexed results, a specific subdomain stood out. It was hosting an online **Management Information System (MIS) Portal**. Navigating to the page revealed a standard login form requiring a valid username and password to proceed.

### Step 2: Breaking the Query Logic with a Single Quote

SQL injection lifecycle always starts by identifying the spaces where inputs will interface directly with the database interpreter. In the process of normal mapping, I attacked the well-known input parameter space (**Username field**).

> To test how the backend handled unexpected inputs, I entered a single quotation mark (`'`):

Press enter or click to view image in full size

![]()

The backend server was quick to reply with the details of the crash in the database:

> The error showed that the application had used dynamic query generation by simply using strings (e.g., `SELECT * FROM users WHERE user = 'INPUT'`). Through entering an odd number of quotation marks, the interpreter would crash, giving an instant response that no input escaping whatsoever was implemented.

### Step 3: Repairing the Syntax Structure

Before any extraction of information, the researcher must demonstrate his/her mastery of the query stream logic by correcting the faulty syntax logic.

This was done by commenting out the remainder of the developer’s code using the SQL inline comment syntax ( - - ) as shown below:

Press enter or click to view image in full size

![]()

Rather than crashing the database engine, the application cleanly threw an authentication error message that said, “Invalid Username/Password. Please try again.”

> This verified the execution alignment. With the help of a close-quote along with a backend comment string, I was able to manage the state of operation of the web application database s...