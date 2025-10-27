---
title: New Honeypots
url: https://www.hackerfactor.com/blog/index.php?%2Farchives%2F983-New-Honeypots.html=
source: Instapaper: Unread
date: 2023-02-25
fetch_date: 2025-10-04T08:07:10.988601
---

# New Honeypots

![Hacker Factor Logo](/images/hf-lock-banner.png)

[The Hacker Factor Blog](/blog/)

**Science-based transgender diversity for vulnerable evidence-based fetus entitlement**

[Home](/)
[Blog](/blog/)
[Swag](https://www.zazzle.com/hackerfactor/?rf=238307745558769988)

### About

[Dr. Neal Krawetz](/about.php) writes The Hacker Factor Blog. Follow him on [Mastodon](https://noc.social/%40hackerfactor).

### Tools

• [FotoForensics](https://fotoforensics.com/): Test your own photos.

### Links

**Security**

### Calendar

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [«](https://hackerfactor.com/blog/index.php?/archives/2025/09.html "View posts for previous month") | October '25 | | | | |  |
| S | M | T | W | T | F | S |
|  |  |  | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

### Archives

* [October 2025](/blog/index.php?/archives/2025/10.html "October 2025")
* [September 2025](/blog/index.php?/archives/2025/09.html "September 2025")
* [August 2025](/blog/index.php?/archives/2025/08.html "August 2025")
* [Recent...](/blog/index.php?frontpage)
* [Older...](https://hackerfactor.com/blog/index.php?/archive)

### Feeds

* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss1)
  [RSS 1.0 feed](/blog/index.php?/feeds/index.rss1)
* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss2)
  [RSS 2.0 feed](/blog/index.php?/feeds/index.rss2)

### Categories

* [Conferences](/blog/index.php?/categories/7-Conferences "Been there, done that, took notes")
* [Copyright](/blog/index.php?/categories/16-Copyright "Copyrights, Patents, and Concerns")
* [Financial](/blog/index.php?/categories/8-Financial "Money Matters")
* [Forensics](/blog/index.php?/categories/14-Forensics "Computer and Digital Forensics")
* [Authentication](/blog/index.php?/categories/23-Authentication)
* [FotoForensics](/blog/index.php?/categories/17-FotoForensics "http://fotoforensics.com/")
* [Image Analysis](/blog/index.php?/categories/1-Image-Analysis "A Picture's Worth")
* [IoT](/blog/index.php?/categories/22-IoT "Internet of Things")
* [Mass Media](/blog/index.php?/categories/6-Mass-Media "Volume Does Not Imply Brightness")
* [Music](/blog/index.php?/categories/24-Music)
* [Network](/blog/index.php?/categories/3-Network "A Series of Tubes")
* [Honeypot](/blog/index.php?/categories/21-Honeypot "This is my other computer")
* [Tor](/blog/index.php?/categories/19-Tor "The Onion Router")
* [Phones](/blog/index.php?/categories/18-Phones "Telemarketers, Cold Calls, and Scams")
* [Politics](/blog/index.php?/categories/13-Politics "Fear, Uncertaity, Doubt, and that bad aftertaste")
* [Privacy](/blog/index.php?/categories/9-Privacy "You Have The Right")
* [Programming](/blog/index.php?/categories/5-Programming "Code Monkey's Unite!")
* [AI](/blog/index.php?/categories/20-AI "AI and Machine Learning")
* [Security](/blog/index.php?/categories/4-Security "Attack and Defend")
* [Terrorists](/blog/index.php?/categories/2-Terrorists "Terrorism Research")
* [Travel](/blog/index.php?/categories/15-Travel "Enjoy life! Eat out more often!")
* [Unfiction](/blog/index.php?/categories/12-Unfiction "I can't make this up...")
* [[Other]](/blog/index.php?/categories/11-Other "Catch-all category")

[All categories](/blog/index.php?frontpage "All categories")

# [New Honeypots](/blog/index.php?/archives/983-New-Honeypots.html)

## Thursday, 23 February 2023

As a network security researcher, I run a [bunch](/blog/index.php?/archives/841-Building-a-Basic-Honeypot.html) [of](/blog/index.php?/archives/776-A-little-honey-goes-a-long-way.html) [honeypots](/blog/index.php?/archives/837-From-Harmless-to-Annoyance-to-Attack.html) and related [honeytraps](/blog/index.php?/archives/864-Its-All-Fun-and-Games.html). I typically do this to generate a baseline for "what is normal" attack volume. I mean, I know my servers (and your servers, and every server on the internet) is constantly under attack, but is the attack volume and the targeted services "typical"? Or is there something hitting my servers that should make me concerned?

When I had to [change hosting locations](/blog/index.php?/archives/969-Be-Right-Back.html) last year, I ended up losing a bunch of my honeypot systems. I've spent the last few months relying on my previously collected baseline data. (Fortunately, that's been good enough for now.) I've also been redesigning some new honeypot and monitoring systems. This month, I began rolling out a couple of new honeypot systems and redoing some benchmark experiments. At a high level, these are the same types of data collection that I've previously done, but I'm using new tools that collect much more information about the attackers.

### Attack Scope

The SANS Internet Storm Center (ISC) has this long-running research project called the [Survival Time](https://isc.sans.edu/survivaltime.html). Often, new systems are deployed and then configured later. For example, you turn on your new Windows computer, connect to the internet, and then download patches. The time between going online and installing the first patches is critical because you are vulnerable to attack.

The ISC's Survival Time addresses a simple question: If you deploy a brand new system on the internet, how long will it take for an attacker to scan and/or attack your system?

[Back in 2003](https://www.gothamtg.com/blog/whats-your-internet-survival-time), the survival time averaged about 40 minutes. That is, you had *on average* about 40 minutes to download and install patches before someone would find your system and potentially compromise you. (Given network speeds back then, this was a tough task.)

A year later, it dropped to 16 minutes.

Today, 20 years later, it's gone from less than 40 **minutes** to less than 40 **seconds**. The volume of scans and attacks is crazy high. If you deploy a new system on the internet, just assume it will be attacked before you can install patches.

I configured my new honeypot with a bunch of passive detectors. I started with an out-of-the-box Linux system that only had Secure Shell (SSH) enabled for remote logins. (A typical default server install.) I added in some of my custom monitoring tools and then turned it on. My plan included adding in a web server and mail server after getting the system up and running.

My honeypot booted up for the first time and received its first scan after 7 seconds. An attacker found the SSH daemon after 21 seconds and attempted a cipher-related attack after 45 seconds. (All times are relative to when the networking interface was first brought up.) This is right in line with the ISC's current findings.

Keep in mind, the scans and attack happened *fast*. It happened before I had a chance to install and configure my web and mail servers. So consider this: Let's assume you are a very proficient sysadmin and very familiar with installing and configuring a mail server. Do you think you can install and securely configure it in under 45 seconds? Personally, I know what I'm doing. I scripted most of the installation process and just needed to cut-and-paste the configuration settings. It still took longer than a minute. Fortunately, the mail server defaulted to local delivery only, so remote attackers had nothing to attack until after I had it configured, hardened, and locally tested.

My web server install wasn't as lucky. When it first installs, it's live to the internet. The bots found it and retrieved the homepage (Apache default page) before the few seconds it took to replace the default information with my new (honeypot) web service. The same attacker came back a few minutes later and retrieved the new web site before I could configure TLS. He came back a third time after I had HTTPS up and running. I don't know if this was just an aggressive scanning bot or if I triggered some automated rules for frequently checking ...