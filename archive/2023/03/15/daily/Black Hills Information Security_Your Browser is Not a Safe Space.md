---
title: Your Browser is Not a Safe Space
url: https://www.blackhillsinfosec.com/your-browser-is-not-a-safe-space/
source: Black Hills Information Security
date: 2023-03-15
fetch_date: 2025-10-04T09:36:13.160605
---

# Your Browser is Not a Safe Space

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

14
Mar
2023

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Corey Ham](https://www.blackhillsinfosec.com/category/author/corey-ham/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)
[Browser Security](https://www.blackhillsinfosec.com/tag/browser-security/), [Data Breaches](https://www.blackhillsinfosec.com/tag/data-breaches/), [Malware](https://www.blackhillsinfosec.com/tag/malware/), [Password Managers](https://www.blackhillsinfosec.com/tag/password-managers/), [Stealer Logs](https://www.blackhillsinfosec.com/tag/stealer-logs/)

# [Your Browser is Not a Safe Space](https://www.blackhillsinfosec.com/your-browser-is-not-a-safe-space/)

[Corey Ham](https://www.blackhillsinfosec.com/team/corey-ham/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/BLOG_chalkboard_00620-1024x576.png)

## **Tl;dr**

*Use a password manager instead of browser storage for passwords, credit card numbers, and other autofill items.*

***Personal security:*** *Do not save anything sensitive in your browser, especially credentials. This data will probably be spread further than you realize, and it can be accessed by malware. Consider deleting all credentials and autofills from your browser of choice.*

***Enterprise security:*** *Prevent users from both saving credentials in browser credential stores and consider preventing users from logging into their browsers on enterprise-managed hosts. Enforce access controls that prevent users from signing into browsers on non-managed hosts, if possible. Monitor for credential abuse.*

## **The Story**

I do red team engagements for BHIS. These engagements are designed to cover the widest attack surface possible for a target entity. We operate with broad scoping — meaning we can attack any user, computer, application, or fax machine we identify as owned by the target, unless explicitly provided as out-of-scope ahead of time.

During a recent red team engagement, I gained access to employee credentials, browser cookies, screenshots of a user’s desktop, and some interesting files **on the first day of testing**. Now, you might be thinking this sounds like a brag about my god-tier hacker skills or that the target had terrible security if I managed to get that far on day one. The truth is, I probably didn’t even have command-and-control infrastructure set up yet, and the target had excellent security. So how did this happen? I found all this data in some Stealer Logs.

### **Stealer Logs?**

I first became aware of stealer logs at WWHF Deadwood 2022, where I had a great conversation with Mishaal Khan after his talk where he demonstrated using them for OSINT. I’m something of an OSINT fan myself, and the main data breach wrangler at BHIS, so I resolved to get my hands on some of this data and check it out for myself. I eventually managed to get heaps and heaps of it, totaling over 10TB of data. I then worked to process as much of the data as possible to make it searchable. I’ll spare you the boring details of this, but suffice it to say that black hat hackers are absolutely TERRIBLE at organizing files. Let me know if you’d like to see a separate blog post or webcast detailing how I processed the data and made it searchable in our private breach database.

For a quick overview of what the logs themselves look like, check out this excellent blog from IntelTechniques (<https://inteltechniques.com/blog/2022/07/06/new-breach-data-lesson-ii-stealer-logs/>).

A brief overview:

* Stealer malware is distributed in a variety of ways, including being packaged with cracked/pirated software, in phishing campaigns, and in malvertising.
* Stealers are commodity malware that are cheap ($100), and there are quite a few variants, including [Redline](https://cyberint.com/blog/research/redline-stealer/), [Raccoon](https://raccoon.ic3.gov/home), [Vidar](https://blog.cyble.com/2021/10/26/vidar-stealer-under-the-lens-a-deep-dive-analysis/), and more. Stealers commonly grab the following information from the victim:
  + System information (running processes, installed software, screenshots)
  + Browser data (credentials, history, cookies, autofills, etc.)
  + Browser credential data is generally reported with four fields:
    - Host/URL
    - Username
    - Password
    - Browser version (i.e. Chrome 104)
  + Interesting-looking files
  + Specific extractors are built for high-value software, such as cryptocurrency wallets, video games, discord authentication tokens, etc.
  + Webcam captures, depending on variant

The malware doesn’t stick around for long, but grabs what it can and sends it off to a central server for processing. ...