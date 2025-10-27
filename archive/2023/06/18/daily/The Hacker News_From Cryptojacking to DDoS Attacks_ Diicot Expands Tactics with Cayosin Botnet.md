---
title: From Cryptojacking to DDoS Attacks: Diicot Expands Tactics with Cayosin Botnet
url: https://thehackernews.com/2023/06/from-cryptojacking-to-ddos-attacks.html
source: The Hacker News
date: 2023-06-18
fetch_date: 2025-10-04T11:47:22.456873
---

# From Cryptojacking to DDoS Attacks: Diicot Expands Tactics with Cayosin Botnet

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [From Cryptojacking to DDoS Attacks: Diicot Expands Tactics with Cayosin Botnet](https://thehackernews.com/2023/06/from-cryptojacking-to-ddos-attacks.html)

**Jun 17, 2023**Ravie LakshmananCryptojacking / Network Security

[![Cybersecurity](data:image/png;base64... "Cybersecurity")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjO2bLtx-UVg7s_ceoNpJSax6DwS1gQsIBj_bDKSps_s4deT0AFis1wJzEDpaYH-fNQq1sl4i4tnl_2PrkpuYMKYwGM2FjqjaMXIToJj_ryV848koE4EjvRpRFu7MUhhdXjo-n2y6tIp2GTBjdn-9U3pnM8Px6pXXCoXcTw5_-Zhe95iKfoiAO8blMC/s790-rw-e365/hacking-ddos.jpg)

Cybersecurity researchers have discovered previously undocumented payloads associated with a Romanian threat actor named **Diicot**, revealing its potential for launching distributed denial-of-service (DDoS) attacks.

"The Diicot name is significant, as it's also the name of the [Romanian organized crime and anti-terrorism policing unit](https://en.wikipedia.org/wiki/Directorate_for_Investigating_Organized_Crime_and_Terrorism)," Cado Security [said](https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/) in a technical report. "In addition, artifacts from the group's campaigns contain messaging and imagery related to this organization."

Diicot (née Mexals) was [first documented](https://thehackernews.com/2021/07/researchers-warn-of-linux-cryptojacking.html) by Bitdefender in July 2021, uncovering the actor's use of a Go-based SSH brute-forcer tool called Diicot Brute to breach Linux hosts as part of a cryptojacking campaign.

Then earlier this April, Akamai [disclosed](https://thehackernews.com/2023/06/beware-1000-fake-cryptocurrency-sites.html) what it described as a "resurgence" of the 2021 activity that's believed to have started around October 2022, netting the actor about $10,000 in illicit profits.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The attackers use a long chain of payloads before eventually dropping a Monero cryptominer," Akamai researcher Stiv Kupchik [said](https://www.akamai.com/blog/security-research/mexals-cryptojacking-malware-resurgence) at the time. "New capabilities include usage of a Secure Shell Protocol (SSH) worm module, increased reporting, better payload obfuscation, and a new LAN spreader module."

The latest analysis from Cado Security shows that the group is also deploying an off-the-shelf botnet agent referred to as [Cayosin](https://web.archive.org/web/20190414145619/https%3A//perchsecurity.com/perch-news/threat-report-sunday-february-3rd-2019/), a malware family that shares characteristics with [Qbot](https://thehackernews.com/2023/06/evasive-qbot-malware-leverages-short.html) and [Mirai](https://thehackernews.com/2023/06/active-mirai-botnet-variant-exploiting.html).

The development is a sign that the threat actor now possesses the ability to mount DDoS attacks. Other activities carried out by the group include doxxing of rival hacking groups and its reliance on Discord for command-and-control and data exfiltration.

[![Cybersecurity](data:image/png;base64... "Cybersecurity")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgN53xOf06Mkves343KyZeVKnItvaZ3vVuDHW-SgN9z6E9V89ZV059azKog4dZAO9NBro52LerIt6L4Imao3sVWGwevk7qPEYy290ENEZ2KC-3tFFrmBjNJKE1yWIOWUOgTsgBUg9nGlpcTPeoICDQd14BLBYpUi2KMRpwDfL-e72wwOu3iprMw7HH/s790-rw-e365/malware.jpg)

"Deployment of this agent was targeted at routers running the Linux-based embedded devices operating system, OpenWrt," the cybersecurity company said. "The use of Cayosin demonstrates Diicot's willingness to conduct a variety of attacks (not just cryptojacking) depending on the type of targets they encounter."

Diicot's compromise chains have remained largely consistent, leveraging the custom SSH brute-forcing utility to gain a foothold and drop additional malware such as the Mirai variant and the crypto miner.

Some of the other tools used by the actor are as follows -

* **Chrome** - An internet scanner based on Zmap that can write the results of the operation to a text file ("bios.txt").
* **Update** - An executable that fetches and executes the SSH brute-forcer and Chrome if they don't exist in the system.
* **History** - A shell script that's designed to run Update

The SSH brute-forcer tool (aka aliases), for its part, parses the text file output of Chrome to break into each of the identified IP addresses, and if successful, establishes remote connection to the IP address.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is then followed by running a series of commands to profile the infected host and using it to either deploy a cryptominer or make it act as a spreader if the machine's CPU has less than four cores.

To mitigate such attacks, organizations are recommended to implement SSH hardening and firewall rules to limit SSH access to specific IP addresses.

"This campaign specifically targets SSH servers exposed to the internet with password authentication enabled," Cado Security said. "The username/password list they use is relatively limited and includes default and easily-guessed credential pairs."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[botnet](htt...