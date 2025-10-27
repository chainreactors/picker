---
title: Warning: Over 2,000 Palo Alto Networks Devices Hacked in Ongoing Attack Campaign
url: https://thehackernews.com/2024/11/warning-over-2000-palo-alto-networks.html
source: The Hacker News
date: 2024-11-22
fetch_date: 2025-10-06T19:20:09.732843
---

# Warning: Over 2,000 Palo Alto Networks Devices Hacked in Ongoing Attack Campaign

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

# [Warning: Over 2,000 Palo Alto Networks Devices Hacked in Ongoing Attack Campaign](https://thehackernews.com/2024/11/warning-over-2000-palo-alto-networks.html)

**Nov 21, 2024**Ravie LakshmananVulnerability / Cyber Attack

[![Palo Alto Networks Devices](data:image/png;base64... "Palo Alto Networks Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXv44zhmUswskZlIcFC1E_N0ADtP3J5s__qk_PqPsCmAR4a8X0WNBXIU9u0XAxxOylPEY8wH_ohVBWzz4KlgbDVI21W6P_Y0juTzOYE5pX4XNWrhR-6P13ceozwxfo9Vrytlks8JMm76jV9JVqaiP5uxCiKPvFEJm8QAoPpABD6gNayh5HGjUWXdsZnVKs/s790-rw-e365/firewall.png)

As many as 2,000 Palo Alto Networks devices are [estimated](https://infosec.exchange/%40shadowserver/113520322017264871) to have been compromised as part of a campaign abusing the newly disclosed security flaws that have come under active exploitation in the wild.

According to [statistics](https://dashboard.shadowserver.org/statistics/combined/map/?map_type=std&day=2024-11-20&source=compromised_website&source=compromised_website6&tag=panos-compromised%2B&geo=all&data_set=count&scale=log) shared by the Shadowserver Foundation, a majority of the infections have been reported in the U.S. (554) and India (461), followed by Thailand (80), Mexico (48), Indonesia (43), Turkey (41), the U.K. (39), Peru (36), and South Africa (35).

Earlier this week, Censys [revealed](https://thehackernews.com/2024/11/pan-os-firewall-vulnerability-under.html) that it had identified 13,324 publicly exposed next-generation firewall (NGFW) management interfaces, with 34% of these exposures located in the U.S. However, it's important to note that not all of these exposed hosts are necessarily vulnerable.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The [flaws in question](https://thehackernews.com/2024/11/pan-os-firewall-vulnerability-under.html), CVE-2024-0012 (CVSS score: 9.3) and CVE-2024-9474 (CVSS score: 6.9), are a combination of authentication bypass and privilege escalation that could allow a bad actor to perform malicious actions, including modifying configurations and executing arbitrary code.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4nYQrXE1KKK8C3CTwvXZj6KPhGzMqEJgN8cecAtury80mo4erxIAde2f2FsIKuzezh8teog70qNoz2T3slh2d5X8fCtNqouaR59wSIJdZJ9YNl_7YGumgv8rbjklxxtkJN_Pnfo4yZfaTuMum7h5VKoXDz084wYg0JJkC8graw937PJwAfTDEVJpe1I0I/s790-rw-e365/exploits.png)

Palo Alto Networks, which is tracking the initial zero-day exploitation of the flaws under the name Operation Lunar Peek, said they are being weaponized to achieve command execution and drop malware, such as PHP-based web shells, on hacked firewalls.

The network security vendor has also warned that cyber attacks targeting the security flaws are likely to escalate following the availability of an exploit combining them.

To that end, it [said](https://unit42.paloaltonetworks.com/cve-2024-0012-cve-2024-9474/) it "assesses with moderate to high confidence that a functional exploit chaining CVE-2024-0012 and CVE-2024-9474 is publicly available, which will enable broader threat activity."

It further noted that it has observed both manual and automated scanning activity, necessitating that users apply the latest fixes as soon as possible and secure access to the management interface as per recommended best practice deployment guidelines.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This particularly includes restricting access to only trusted internal IP addresses to prevent external access from the internet.

### Update

Palo Alto Networks told The Hacker News that the actual number of infected devices is smaller than what has been reported by the Shadowserver Foundation owing to the fact that the latter only shows firewalls that have management interfaces exposed to the internet.

In addition to working with affected customers, it also said a majority of its customers already follow industry best practices and secure their management interfaces, and only less than 0.5% of its firewalls have an internet-exposed interface.

### PAN Flaws Used to Drop Sliver and Crypto Miners

Cloud security firm Wiz has [revealed](https://www.wiz.io/blog/cve-2024-0012-pan-os-vulnerability-exploited-in-the-wild) that exploitation attempts in the wild have "dramatically increased" following the [release](https://github.com/rapid7/metasploit-framework/pull/19663) of a valid proof-of-concept (PoC) exploit on November 19, 2024, and that it has observed threat actors weaponizing the flaws to drop web shells, Sliver implants, and crypto miners.

*(The story was updated after publication to include a response from Palo Alto Networks and details of exploitation activity.)*

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall Security](https://thehackernews.com/search/label/Firewall%20Security)[Malware](https://thehackernews.com/search/label/Malware)[Palo Alto Networks](https://thehackernews.com/search/label/Palo%20Alto%20Networks)[Shadowserver](https://thehackernews...