---
title: My First Critical Bug: Exposing 3.5 Lakh+ PII! ️
url: https://infosecwriteups.com/my-first-critical-bug-exposing-3-5-lakh-pii-%EF%B8%8F-fbad616ddbea?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-15
fetch_date: 2025-10-06T19:37:24.506422
---

# My First Critical Bug: Exposing 3.5 Lakh+ PII! ️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffbad616ddbea&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-critical-bug-exposing-3-5-lakh-pii-%25EF%25B8%258F-fbad616ddbea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-critical-bug-exposing-3-5-lakh-pii-%25EF%25B8%258F-fbad616ddbea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fbad616ddbea---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fbad616ddbea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 💥 My First Critical Bug: Exposing 350K+ PII! 🛡️

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--fbad616ddbea---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--fbad616ddbea---------------------------------------)

3 min read

·

Dec 14, 2024

--

6

Listen

Share

**Hello Hackers, Today in this write-up I am going to tell you how accidently I discovered my very first critical bug which is disclosing 350k+ peoples PII details, database credentials, api\_keys, secret keys, router information etc. Let’s go**

Press enter or click to view image in full size

![]()

**credit: DALL-E**

**During my penetration testing journey, I have assigned a task to submit at least 10 bugs through openbugbounty platform. So I quickly message my best friend and mentor**

[**AbhirupKonwar**](https://medium.com/u/9e41d1b8a839?source=post_page---user_mention--fbad616ddbea---------------------------------------)

 **bhaiya because he already reported 1000+ bugs to this platform and he suggest me to use automation and I got sparked nuclei tool. If you don’t know research about this tool it is amazing.**

**I quickly run this tool using very basic command:**

```
nuclei -target https://example.com
```

Press enter or click to view image in full size

![]()

**backup-file found 🤑**

**Nuclei give me backup-files which is basically zip file which contains full source code of the website including database files and lots of things.**

**After looking each and every file I found following juicy information:**

![]()

**found some keys with their secrets**

![]()

**ap\_key, api\_secret 🤩**

![]()

**database credentials 😛🤩**

![]()

**Full router information 😲**

**After seeing this all information I am going to report this bug but there are so many more information so I think let’s look at some more database files and when I found file filename.sql which contains all sql queries which are used in the website and also contains all the user data which are inserted into the database and when I look this data around I found 350k+ users data including their user\_id, full name, phone no, city, zip code, address, street\_name, last\_updated logs, and so many things.**

**Here in below photo I only show user\_id:**

Press enter or click to view image in full size

![]()

**get full PII of 350k+ users 🥳**

**Then I quickly make a full report and submitted the company through openbugbounty platform. Now let’s see how company will handle the report 🤞.**

**Thank you for taking the time to read my journey into discovering this critical bug! I truly appreciate your support and enthusiasm for cybersecurity.**

**If you found this write-up insightful, don’t forget to give it some claps and follow me for more exciting content on bug hunting, vulnerabilities, and cybersecurity insights. Let’s stay connected and continue exploring the world of security together!**

**Stay curious, stay safe! 😊**

**My other write-ups you might find helpful:**

[## Methods to bypass 403 & 401

### Hello Hackers, today in this write-up I am going to give you all things you need to know to bypass 403 & 401 error…

infosecwriteups.com](/methods-to-bypass-403-401-38df4cec069e?source=post_page-----fbad616ddbea---------------------------------------)

[## Cracking ATO via Email HTML Injection

### Hello hackers, today in this write-up I am going to share how I find HTML injection in email in one of the self hosted…

infosecwriteups.com](/cracking-ato-via-email-html-injection-edd19c8e1b8f?source=post_page-----fbad616ddbea---------------------------------------)

[## How I Found 3 Bugs in a Single Day

### In this write-up, I will share my journey of discovering my first high-severity bug and making it to the Hall of Fame…

infosecwriteups.com](/how-i-found-3-bugs-in-a-single-day-a690e2abd4fb?source=post_page-----fbad616ddbea---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----fbad616ddbea---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----fbad616ddbea---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----fbad616ddbea---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----fbad616ddbea---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----fbad616ddbea---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fbad616ddbea---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fbad616ddbea---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fbad616ddbea---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fbad616ddbea---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--fbad616ddbea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:96:96/1*WB_W42RWlz5rAUWNCT...