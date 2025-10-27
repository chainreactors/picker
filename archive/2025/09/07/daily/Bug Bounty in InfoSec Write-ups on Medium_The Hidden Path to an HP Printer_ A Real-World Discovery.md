---
title: The Hidden Path to an HP Printer: A Real-World Discovery
url: https://infosecwriteups.com/the-hidden-path-to-an-hp-printer-a-real-world-discovery-4b05187a8271?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-07
fetch_date: 2025-10-02T19:47:27.576318
---

# The Hidden Path to an HP Printer: A Real-World Discovery

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4b05187a8271&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-path-to-an-hp-printer-a-real-world-discovery-4b05187a8271&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-path-to-an-hp-printer-a-real-world-discovery-4b05187a8271&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4b05187a8271---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4b05187a8271---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The Hidden Path to an HP Printer: A Real-World Discovery 🔍

[![Manav](https://miro.medium.com/v2/resize:fill:64:64/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---byline--4b05187a8271---------------------------------------)

[Manav](https://medium.com/%40manav_24?source=post_page---byline--4b05187a8271---------------------------------------)

3 min read

·

Sep 5, 2025

--

Listen

Share

**Alright, so here’s a weird story from my adventures while doing Bug Bounty…**
Hey guys, I hope you’re doing well! I’m back again with another interesting Story. Today, I want to share how I discovered HP printer’s admin page by Doing basic directory brute-forcing. It Looks like someone decided the printer should be Open for all to access.

Grab your coffee, and let’s get started! 😉

![]()

## ***The Discovery***

It all started on a regular afternoon. I was watching YouTube, just passing the time, when an email from [CyberBay](https://cyberbay.tech/) showed up in my inbox. It mentioned that some new programs had been launched, so I thought, why not take a look? I started with some basic recon, used WaybackURLs to find some old archived paths, then ran Nuclei to check for any quick wins. Nothing came up. So, I fired up Dirsearch and started brute-forcing directories, hoping to find something interesting. That’s when things took an unexpected turn one hidden path caught my eye, and it wasn’t just any path.
*I found myself staring at the unlocked admin page of an HP Printer.*

![]()

## **Digging Deeper: Access and Control**

This is the URL that earned me a critical bug within minutes:
<http://n119236249203.example.com/SSI/index.htm>

When I first opened it, I wasn’t expecting much. It looked like a basic, and boring link nothing that much important. But as soon as the page loaded, I realized I was looking at something way more serious , the full admin panel of an HP printer.

No login, no warning, just open access to everything.

Press enter or click to view image in full size

![]()

*I just start exploring the admin panel and was able to find that:*

* I was able to modify network settings, like DNS and IP configurations, to redirect traffic through a malicious network they control.

Press enter or click to view image in full size

![]()

* I was able to change the printer’s phone book, like adding some extra contact names in their list.

Press enter or click to view image in full size

![]()

* An attacker could also disable all network connections, cutting the printer off completely and rendering it unusable.

Press enter or click to view image in full size

![]()

### **Disclosure & Reward**

I reported the issue to the platform, and the very next morning, I got an email saying the report was accepted and I was rewarded ***$700*** for this finding.

Press enter or click to view image in full size

![]()

Plus an extra ***$175*** for retesting the issue. That’s when I realized even printers can pay you that much.

Press enter or click to view image in full size

![]()

Thanks for reading the story till the end.
This discovery just shows that even the most unexpected places can hold some serious surprises.

Keep exploring, stay curious, and who knows what you’ll find next!
Catch you in the next writeup!

Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/manav2829/)

**Happy Hunting!!** 🐞

![]()

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4b05187a8271---------------------------------------)

[Web Applications](https://medium.com/tag/web-applications?source=post_page-----4b05187a8271---------------------------------------)

[Offensive Security](https://medium.com/tag/offensive-security?source=post_page-----4b05187a8271---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4b05187a8271---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4b05187a8271---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4b05187a8271---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4b05187a8271---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4b05187a8271---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Manav](https://miro.medium.com/v2/resize:fill:96:96/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---post_author_info--4b05187a8271---------------------------------------)

[![Manav](https://miro.medium.com/v2/resize:fill:128:128/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---post_author_info--4b05187a8271---------------------------------------)

[## Written by Manav](https://medium.com/%40manav_24?source=post_page---post_author_info--4b05187a8271---------------------------------------)

[45 followers](https://medium.com/%40manav_24/followers?source=post_page---post_author_info--4b05187a8271---------------------------------------)

·[8 following](https://medium.com/%40manav_24/following?source=post_page---post_author_info--4b05187a8271---------------------------------------)

Cyber security Researcher || Bug Bounty Hunter || Red Teamer || Pentester ...