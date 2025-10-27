---
title: Exploring the LockBit Panel Breach – What Logs and Chats Reveal About Ransomware-as-a-Service
url: https://labs.yarix.com/2025/05/exploring-the-lockbit-panel-breach-what-logs-and-chats-reveal-about-ransomware-as-a-service/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-30
fetch_date: 2025-10-06T22:27:34.416634
---

# Exploring the LockBit Panel Breach – What Logs and Chats Reveal About Ransomware-as-a-Service

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Exploring the LockBit Panel Breach – What Logs and Chats Reveal About Ransomware-as-a-Service

* [Home](https://labs.yarix.com "Go to Home Page")
* Exploring the LockBit Panel Breach – What Logs and Chats Reveal About Ransomware-as-a-Service

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2025/05/logo5.jpg)

29May29/05/2025

## Exploring the LockBit Panel Breach – What Logs and Chats Reveal About Ransomware-as-a-Service

[cti](https://labs.yarix.com/author/cti/ "Posts by cti")2025-06-04T17:53:29+02:00

By
[cti](https://labs.yarix.com/author/cti/ "Posts by cti")

Reading Time:   12 minutes

On May 7, 2025, a number of domains associated with the LockBit ransomware group were subjected to a web defacement attack by an unknown individual. Visitors to the compromised domains encountered the following message, replacing the original website content:

***Don’t do crime. CRIME IS BAD. xoxo from Prague***

On the same page, a file named “paneldb\_dump.zip” was available for download. This archive contained the MySQL database from the panel used by LockBit affiliates to manage operations such as attack histories and negotiations with victims. The Yarix Cyber Threat Intelligence Team (YCTI) retrieved the file and presents below the analysis of relevant information identified within the archive.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x27.jpg)

*Screenshot from the Compromised Domain – Source: YCTI Team*

## A Pattern of Defacement?

For those closely following ransomware group activities, the message “Don’t do crime. CRIME IS BAD. xoxo from Prague” recalls a similar event in April[[1]](#_ftn1) involving the *.onion* domain of the Everest ransomware group’s Data Leak Site.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x25.jpg)

*Everest DLS Defacement – Source: Bleeping Computer*

The message is identical to that found on the compromised LockBit domains. However, in Everest’s case, no files were shared. Subsequently, the compromised .onion URL of Everest’s DLS was restored and is currently online and accessible. LockBit represents the second instance in a short period where a ransomware group’s .*onion* site has been exploited. Although the identity of the mysterious “pentester” remains unknown, these actions may indicate a trend of exploiting Data Leak Site domains or ransomware panel login pages to identify potential vulnerabilities. The motivations in these two specific cases remain a mystery, and it remains unclear whether this is the work of a zealous “lone wolf” acting for the glory of pentesting or a direct competitor of the ransomware groups.

## Inside the Dump: Structure, Tables and Source

The file retrieved from LockBit’s compromised domains is an SQL dump weighing approximately 26 megabytes, comprising 114,055 rows. The identified tables within include:

*“api\_history”, “btc\_addresses”, “builds”, “builds\_configurations”, “chats”, “clients”, “events”, “events seen”, “”faq”, “files”, “invites”, “jobs”, “migrations”, “news”, “pkeys”, “socket\_messages”, “system\_invalid\_requests”, “testfiles”, “users”, “visits”.*

By examining the dates related to the conversation messages in the “chats” table and the SQL dump’s creation date, the information was placed within a timeframe between December 18, 2024, and April 29, 2025. This allowed YCTI analysts to link the December date with LockBit’s announcement regarding the release of version 4.0 of its malware. The event was announced on LockBit’s DLS with the following post published on December 19, 2024:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x37.jpg)

*Source: LockBit Data Leak Site*

Visiting the domains mentioned in the post currently displays a message suggesting maintenance is underway, thereby concealing the original domain content.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x43.jpg)

*Source: LockBit Data Leak Site*

Nonetheless, the content of one of the domains was available through ANY.RUN’s archive [[2]](#_ftn2):

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x56.jpg)

*Source: ANY.RUN*

The domains appear to relate to LockBit’s login panels, consistent with the Ransomware-as-a-Service model offered by the criminal group. This is further supported by posts from users who announced the defacement incident on X[[3]](#_ftn3):

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x79.jpg)

*Source: Rey account on x.com*

According to the same source, LockBit confirmed that the compromise affected the panel dedicated to affiliates for registration and account activation procedures. The exfiltrated information by the unknown user included user conversations and Bitcoin addresses, excluding the theft of source code or the Locker builder.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x25.jpg)

*Original LockBit Conversation Posted by User Rey – Source: Rey account on x.com*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x25.jpg)

*LockBit Conversation Translated into English by User Rey – Source: Rey account on x.com*

## User Accounts – Affiliate Roles and Attack Volume

The YCTI Team’s analysis of specific tables led to the identification of aliases and rankings associated with affiliates registered on LockBit’s panel. Some accounts are linked to contact IDs via Tox and Session, useful for potential correlations with other “handles.” It remains unclear whether the identified users represent the entirety of LockBit’s affiliates or only those registered on the exploited panel. In other words, it is uncertain if separate panels exist for affiliates to access LockBit’s tools.

Within the “users” table, 75 users were identified. Among these, the users named “admin” and “matrix777,” despite lacking any rank, appear to be administrative accounts for LockBit, as their creation timestamps are identical. Sixty-two users hold the “newbie” rank; five are “verified”; four are “pentester”; one is “ru target”; and one is categorized as “scammer.”

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x83.jpg)

*List of Users – LockBit Panel Dump*

Comparing the list of aliases released during Operation Cronos (194 accounts), no matches were found between the usernames shared by law enforcement and those in the analyzed dump, except for the “admin” account. Below are the alias lists from Operation Cronos[[4]](#_ftn4) and those from the May 2025 dump collected by the the YCTI Team:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x46.jpg)

*Operation Cronos – LockBit User List – Source: Trend Micro*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x57.jpg)*Users Identified in the May 2025 Dump –  May 2025 Dump – Source: YCTI Analysis*

Comparing the “admin” account creation timestamps from the aliases shared post-Operation Cronos with those in the May 2025 dump reveals an exact match in date and time, further confirming the hypothesis that these are aliases related to LockBit’s administrative accounts:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x11.jpg)

*“Admin” User – Operation Cronos – 2024*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x17.jpg)

*“Admin” Accounts – May 2025 Dump – Source: YCTI Analysis*

The YCTI Team also noted a similarity between the alias “matrix777” and a username in the BlackBasta chat leak[[5]](#_ftn5) named “@usernam...