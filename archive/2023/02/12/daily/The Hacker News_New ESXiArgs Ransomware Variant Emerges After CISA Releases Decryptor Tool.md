---
title: New ESXiArgs Ransomware Variant Emerges After CISA Releases Decryptor Tool
url: https://thehackernews.com/2023/02/new-esxiargs-ransomware-variant-emerges.html
source: The Hacker News
date: 2023-02-12
fetch_date: 2025-10-04T06:26:45.490111
---

# New ESXiArgs Ransomware Variant Emerges After CISA Releases Decryptor Tool

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

# [New ESXiArgs Ransomware Variant Emerges After CISA Releases Decryptor Tool](https://thehackernews.com/2023/02/new-esxiargs-ransomware-variant-emerges.html)

**Feb 11, 2023**Ravie LakshmananRansomware / Endpoint Security

[![ESXiArgs Ransomware](data:image/png;base64... "ESXiArgs Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhejfrp7SpFo_7VBW2I5O3VjlKgxpuGU9Hym-wUz4IODh2ss9FyjTRedT6EYBuky5ILRmSO3hN0CsBBwUrHkC6b7mM2K9iShgY5kw-VSMsuClcwkD0XSvdL21gR4uj3BQwiu8IbKgnUo1Whx7-FaeXJ244-twr0CmfjUrVtwA4r7-Uz_rnrKk1UPLU3/s790-rw-e365/ransomware.png)

After the U.S. Cybersecurity and Infrastructure Security Agency (CISA) released a decryptor for affected victims to recover from [ESXiArgs ransomware attacks](https://thehackernews.com/2023/02/new-wave-of-ransomware-attacks.html), the threat actors have bounced back with an updated version that encrypts more data.

The emergence of the new variant was [reported](https://www.bleepingcomputer.com/forums/t/782193/esxi-ransomware-help-and-support-topic-esxiargs-args-extension/page-31#entry5473353) by a system administrator on an online forum, where another participant stated that files larger than 128MB will have 50% of their data encrypted, making the recovery process more challenging.

Another notable change is the removal of the Bitcoin address from the ransom note, with the attackers now urging victims to contact them on Tox to obtain the wallet information.

The threat actors "realized that researchers were tracking their payments, and they may have even known before they released the ransomware that the encryption process in the original variant was relatively easy to circumvent," Censys [said](https://censys.io/esxwhy-a-look-at-esxiargs-ransomware/) in a write-up.

"In other words: they are watching."

Statistics shared by the crowdsourced platform Ransomwhere [reveal](https://twitter.com/ransomwhere_/status/1623673914822914051) that as many as 1,252 servers have been infected by the new version of ESXiArgs as of February 9, 2023, of which 1,168 are reinfections.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Since the start of the ransomware outbreak in early February, over 3,800 unique hosts have been compromised. A [majority](https://www.reuters.com/world/us/ransomware-outbreak-hits-florida-supreme-court-us-european-universities-2023-02-07/) of the infections are located in France, the U.S., Germany, Canada, the U.K., the Netherlands, Finland, Turkey, Poland, and Taiwan.

ESXiArgs, like [Cheerscrypt](https://thehackernews.com/2022/10/researchers-link-cheerscrypt-linux.html) and [PrideLocker](https://www.synacktiv.com/en/publications/pridelocker-a-new-fork-of-babuk-esx-encryptor.html), is based on the Babuk locker, which had its [source code leaked](https://heimdalsecurity.com/blog/the-full-source-code-for-the-babuk-ransomware-published-on-a-russian-hacker-forum/) in [September 2021](https://blog.morphisec.com/babuk-ransomware-variant-major-attack). But a crucial aspect that differentiates it from other ransomware families is the absence of a data leak site, indicating that it's not running on a [ransomware-as-a-service](https://www.trendmicro.com/vinfo/us/security/definition/ransomware-as-a-service-raas) ([RaaS](https://www.cloudflare.com/learning/security/ransomware/ransomware-as-a-service/)) model.

[![ESXiArgs ransomware](data:image/png;base64... "ESXiArgs ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu0Q0yFTwpSVFSYLadXR0M33VjvktMBMXUkMViJzCEqVNxJpEAw2oc7lm255lxWzIrKDUPdTFm0rCSlqSjvrWqHakEsDRDSNbmYz5f4UMznQPnkxxvpEV_1Gsv6DIv19Y8gzS4n2ZxuNhldjpgP67TzqC5e9i3KW6XivzlSUBkf3b6R0ETU3fgGIJJ/s790-rw-e365/ransomware.png)

"Ransoms are set at just over two bitcoins (US $47,000), and victims are given three days to pay," cybersecurity company Intel471 [said](https://intel471.com/blog/an-analysis-of-the-vmware-esxi-ransomware-blitz).

While it was initially suspected that the intrusions involved the abuse of a two-year-old, now-patched OpenSLP bug in VMware ESXi (CVE-2021-21974), compromises have been reported in devices that have had the network discovery protocol disabled.

VMware has since [said](https://thehackernews.com/2023/02/vmware-finds-no-evidence-of-0-day-flaw.html) that it has found no evidence to suggest that a zero-day vulnerability in its software is being used to propagate the ransomware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This indicates that the threat actors behind the activity may be leveraging [several known vulnerabilities](https://www.greynoise.io/blog/exploit-vector-analysis-of-emerging-esxiargs-ransomware) in ESXi to their advantage, making it imperative that users move quickly to update to the latest version. The attacks have yet to be attributed to a known threat actor or group.

[![ESXiArgs ransomware](data:image/png;base64... "ESXiArgs ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1PSW59JDUuhHt5tgaajAgA7zu_olzFdJk9dUmf6O5ApU-czoAOzFTCC-_P6L_9reMfJcGPN_x3V2uTitwWjCPDeek87h-ZY-g6jXbymo2rk9JbF2ixlE1g_-3N6gyBQMB2vajdBikLqTZSuSN8NGjx94FKKX3PkJvPFQiypddw3d5DffaqI7N42uQ/s790-rw-e365/HACKING.png)

"Based on the ransom note, the campaign is linked to a sole threat actor or group," Arctic Wolf [pointed out](https://arcticwolf.com/resources/blog-uk/active-esxiargs-ransomware-campaign-targeting-esxi-servers/). "More established ransomware groups typically conduct OSINT on potential victims before conducting an intrusion and set the ransom payment based on perceived value."

Cybersecurity company Rapid7 [said](https://www.rapid7.com/blog/post/2023/02/09/nearly-19-000-esxi-servers-still-vulnerable-to-cve-2021-21974/) it found 18,581 internet-facing ESXi servers that are vulnerable to CVE-2021-21974, adding it further observed [RansomExx2](https://thehackernews.com/2022/11/new-ransomexx-ransomware-variant.html) actors opportunistically targeting susceptible ESXi servers.

"While the dollar impa...