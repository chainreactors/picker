---
title: DomCat: A Domain Categorization Tool
url: https://www.blackhillsinfosec.com/domcat-a-domain-categorization-tool/
source: Black Hills Information Security, Inc.
date: 2025-09-25
fetch_date: 2025-10-02T20:38:41.393241
---

# DomCat: A Domain Categorization Tool

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

24
Sep
2025

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/), [Phishing](https://www.blackhillsinfosec.com/category/red-team/phishing/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Domain Categorization](https://www.blackhillsinfosec.com/tag/domain-categorization/), [DomCat](https://www.blackhillsinfosec.com/tag/domcat/), [Expired Domains](https://www.blackhillsinfosec.com/tag/expired-domains/), [William Oldert](https://www.blackhillsinfosec.com/tag/william-oldert/)

# [DomCat: A Domain Categorization Tool](https://www.blackhillsinfosec.com/domcat-a-domain-categorization-tool/)

by [William Oldert](https://www.blackhillsinfosec.com/team/william-oldert/) | BHIS Intern

*As in intern at Black Hills Information Security, William is tasked with researching and developing different tools, making them into a reality.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/domcat_header.png)![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/1-DomCat-ascii-screnshot.png)

Have you ever struggled to find expired domains with the specific categorization you need? Are you frustrated by sites that list expired domains but provide no categorization data? And when you finally find a promising domain, you still have to research its categorization on your own, often discovering it’s not categorized at all — wasting your time (and likely your money).

While there were once tools that helped with this process, many have become outdated and fallen into disrepair. We decided this was unacceptable, so I created DomCat.

## What is DomCat?

DomCat is a command-line tool written in Golang that helps the user find expired domains with desirable categorizations. This tool is currently in its infancy and very bare bones. It is written in such a way as to be upgraded with time.

### **Why is DomCat?**

Some readers may be wondering why you would want to find categorized expired domains. When developing DomCat, I primarily had penetration testers in mind. Pentesters can leverage domains with “safe” categorizations to sneak past certain web filters. Another valuable application I later realized is for SEO, where these domains can be acquired to attach to our existing domain in order to gather more traffic.

### **Making DomCat**

When starting this project, I received a list of tools that had fallen out of development, such as DomainHunter, DomainGain-Dep, and CatMyPhish. All useful… but very outdated. I was tasked with either hunting down a new tool that provided the same functionality, or making one. Finding no leads, I began development on DomCat.

Initially, I attempted to fix and combine these existing tools but soon discovered *why* they became broken: they were scraping websites for lists of expired domains. While this was a more acceptable practice five years ago, today many sites have instated policies that prohibit scraping or bots of any kind. This meant attempting to update existing tools would involve complete re-coding, so I instead redirected my efforts into building my own.

## DomCat Walkthrough

Enough of the boring stuff: let’s see DomCat in action.

DomCat has been tested on both Windows and Linux (Ubuntu), and *should* function on any system that supports Go (but that is not a guarantee). Before we can run the tool, our first step is setup, which shouldn’t take too long. An installation script is currently in development; in the future, I hope to have this process automized.

### Step 1: Install Go

You’ll need Go installed to run DomCat. This varies depending on your operating system (OS) — I will only be demonstrating installation on Windows and Linux (Ubuntu). Regardless of OS, you will need to download the appropriate binary from [here](https://go.dev/dl/).

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/2-golang-downloads.png)

#### Ubuntu

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/3-golang-downloads-linux.png)

Download the file for Linux OS. Once finished, pop into a terminal and extract the files and install Go using the following command. This command will only work in the directory that holds the downloaded file. Modify download file path as needed.

```
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
```

After installation, we will set up the Go environment variables. For Ubuntu, we need to edit .bashrc. Don’t mess with things in here unles...