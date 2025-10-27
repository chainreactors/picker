---
title: VMware Finds No Evidence of 0-Day in Ongoing ESXiArgs Ransomware Spree
url: https://thehackernews.com/2023/02/vmware-finds-no-evidence-of-0-day-flaw.html
source: The Hacker News
date: 2023-02-08
fetch_date: 2025-10-04T06:03:20.423719
---

# VMware Finds No Evidence of 0-Day in Ongoing ESXiArgs Ransomware Spree

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

# [VMware Finds No Evidence of 0-Day in Ongoing ESXiArgs Ransomware Spree](https://thehackernews.com/2023/02/vmware-finds-no-evidence-of-0-day-flaw.html)

**Feb 07, 2023**Ravie LakshmananEndpoint Security / Zero-Day

[![VMware Ransomware](data:image/png;base64... "VMware Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9gz1N_Tfcwx3TpyJ6JJCoDrXIa0NxqqiHA41VSkVhw3b5qsw1_gtSmtFuFZhCjpgb7A_UUyaG_wOf7jQVVlQpPESQJCxmV59Ly7LmpUugObqea-N5wN5Tu15U9kGmAN6qxJNj90Qq4bOSgeDu9c3BH8Qo70CzXcycryUVBIUbNF4VW9LLrhWnmB1i/s790-rw-e365/vmware.png)

VMware on Monday said it found no evidence that threat actors are leveraging an unknown security flaw, i.e., a zero-day, in its software as part of an [ongoing ransomware attack spree](https://thehackernews.com/2023/02/new-wave-of-ransomware-attacks.html) worldwide.

"Most reports state that End of General Support (EoGS) and/or significantly out-of-date products are being targeted with known vulnerabilities which were previously addressed and disclosed in VMware Security Advisories (VMSAs)," the virtualization services provider [said](https://blogs.vmware.com/security/2023/02/83330.html).

The company is further recommending users to upgrade to the latest available supported releases of vSphere components to mitigate known issues and [disable the OpenSLP service](https://kb.vmware.com/s/article/76372) in ESXi.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"In 2021, ESXi 7.0 U2c and ESXi 8.0 GA began shipping with the service disabled by default," VMware added.

The announcement comes as unpatched and unsecured VMware ESXi servers around the world have been targeted in a [large-scale](https://www.csa.gov.sg/singcert/Alerts/AL-2023-015) [ransomware campaign](https://cert.at/de/aktuelles/2023/2/massive-vmware-esxi-verschlusselungs-welle) dubbed ESXiArgs by likely exploiting a two-year-old bug VMware patched in February 2021.

The vulnerability, tracked as CVE-2021-21974 (CVSS score: 8.8), is an OpenSLP heap-based buffer overflow vulnerability that an unauthenticated threat actor can exploit to gain remote code execution.

The intrusions appear to single out susceptible ESXi servers that are exposed to the internet on OpenSLP port 427, with the victims instructed to [pay 2.01 Bitcoin](https://darkfeed.io/2023/02/04/a-new-ransomware-attack-is-spreading-like-crazy/) (about $45,990 as of writing) to receive the encryption key needed to recover files. No data exfiltration has been observed to date.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Data from GreyNoise shows that [19 unique IP addresses](https://viz.greynoise.io/tag/vmware-esxi-openslp-rce-attempt?days=30) have been attempting to exploit the ESXi vulnerability since February 4, 2023. 18 of the 19 IP addresses are classified as benign, with one sole malicious exploitation [recorded](https://viz.greynoise.io/query/?gnql=CVE-2021-21974%20classification%3Amalicious) from the Netherlands.

"ESXi customers should ensure their data is backed up and should update their ESXi installations to a fixed version on an emergency basis, without waiting for a regular patch cycle to occur," Rapid7 researcher Caitlin Condon [said](https://www.rapid7.com/blog/post/2023/02/06/ransomware-campaign-compromising-vmware-esxi-servers/). "ESXi instances should not be exposed to the internet if at all possible."

## **Update:**

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday [released](https://github.com/cisagov/ESXiArgs-Recover) a recovery script for organizations that have fallen victim to ESXiArgs ransomware. "The ESXiArgs ransomware encrypts configuration files on vulnerable ESXi servers, potentially rendering virtual machines (VMs) unusable," noted the agency.

CISA has also [released](https://www.cisa.gov/uscert/ncas/alerts/aa23-039a) an advisory, warning that [threat](https://arcticwolf.com/resources/blog-uk/active-esxiargs-ransomware-campaign-targeting-esxi-servers/) [actors](https://www.wiz.io/blog/ransomware-attacks-targeting-vmware-esxi-servers-everything-you-need-to-know) are "exploiting known vulnerabilities in VMware ESXi software to gain access to servers and deploy ESXiArgs ransomware." Over 3,800 servers across the globe have been compromised to date.

The identity of the adversaries behind the campaign is unclear, and it appears that the attacks are taking advantage of several [high-profile OpenSLP vulnerabilities](https://www.greynoise.io/blog/exploit-vector-analysis-of-emerging-esxiargs-ransomware) in ESXi for obtaining initial access.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[ESXi Server](https://thehackernews.com/search/label/ESXi%20Server)[hacking news](https://thehackernews.com/search/label/hacking%20news)[ransomware](https://thehackernews.com/search/label/ransomware)[vmware](https://thehackernews.com/search/label/vmware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWi...