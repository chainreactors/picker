---
title: Iranian OilRig Hackers Using New Backdoor to Exfiltrate Data from Govt. Organizations
url: https://thehackernews.com/2023/02/iranian-oilrig-hackers-using-new.html
source: The Hacker News
date: 2023-02-04
fetch_date: 2025-10-04T05:43:39.210700
---

# Iranian OilRig Hackers Using New Backdoor to Exfiltrate Data from Govt. Organizations

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

# [Iranian OilRig Hackers Using New Backdoor to Exfiltrate Data from Govt. Organizations](https://thehackernews.com/2023/02/iranian-oilrig-hackers-using-new.html)

**Feb 03, 2023**Ravie LakshmananCyber Espionage / Cyber Threat

[![Exfiltrate Data](data:image/png;base64... "Exfiltrate Data")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjU4fSPWr0_RVAoioww9V9nua8FUsVRc8n0g08ghWV2XehR_z2Bo9muxUzWrV6eTppK0Z8STgpLanqNW2axU-xkGwd5tRrrxYnsedkq6mnrsa5GCFA9XVSiOIuA_ysX4IXQovE5lSKfYP9Jd512-9H3SJRMXCETEX3zLRXmYwkOSIL_PdYc6By1g_5i/s790-rw-e365/email.png)

The Iranian nation-state hacking group known as **OilRig** has continued to target government organizations in the Middle East as part of a cyber espionage campaign that leverages a new backdoor to exfiltrate data.

"The campaign abuses legitimate but compromised email accounts to send stolen data to external mail accounts controlled by the attackers," Trend Micro researchers Mohamed Fahmy, Sherif Magdy, and Mahmoud Zohdy [said](https://www.trendmicro.com/en_us/research/23/b/new-apt34-malware-targets-the-middle-east.html).

While the technique in itself is not unheard of, the development marks the first time OilRig has adopted it in its playbook, indicating the continued evolution of its methods to bypass security protections.

The advanced persistent threat (APT) group, also referred to as APT34, Cobalt Gypsy, Europium, and Helix Kitten, has been [documented](https://cyware.com/blog/apt34-the-helix-kitten-cybercriminal-group-loves-to-meow-middle-eastern-and-international-organizations-48ae) for its targeted phishing attacks in the Middle East since at least 2014.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Linked to Iran's Ministry of Intelligence and Security (MOIS), the group is known to use a diverse toolset in its operations, with recent attacks in 2021 and 2022 employing backdoors such as [Karkoff](https://thehackernews.com/2019/04/karkoff-dnspionage-malware.html), [Shark, Marlin](https://thehackernews.com/2022/02/iranian-hackers-using-new-marlin.html), and [Saitama](https://thehackernews.com/2022/05/new-saitama-backdoor-targeted-official.html) for information theft.

The starting point of the latest activity is a .NET-based dropper that's tasked with delivering four different files, including the main implant ("DevicesSrv.exe") responsible for exfiltrating specific files of interest.

Also put to use in the second stage is a dynamic-link library ([DLL](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-libraries)) file that's capable of harvesting credentials from domain users and local accounts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuQEIjMo45wZ8D-zu4ezYdt6Z8HQMLbWyp80M3Btw2XfKo00dqEZdCSO5Rd9nAj7FLgieeqb5nflJrEZW8oHAFg7O_ukqW9H5alXffUFHtuqQCdgVxTS_ElSuJ-r9tBk1lTUaHwFrxPHtriYe4LqqVhfmYFaKa4TY2o-zpb1EHetZlOjoxfwWESuuW/s790-rw-e365/malware-1.png)

The most notable aspect of the .NET backdoor is its exfiltration routine, which involves using the stolen credentials to send electronic missives to actor-controlled email Gmail and Proton Mail addresses.

"The threat actors relay these emails via government Exchange Servers using vaild accounts with stolen passwords," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The campaign's connections to APT34 stems from similarities in between the first-stage dropper and Saitama, the victimology patterns, and the use of internet-facing exchange servers as a communication method, as observed in the case of [Karkoff](https://thehackernews.com/2021/04/researchers-uncover-new-iranian-malware.html).

If anything, the growing number of malicious tools associated with OilRig indicates the threat actor's "flexibility" to come up with new malware based on the targeted environments and the privileges possessed at a given stage of the attack.

"Despite the routine's simplicity, the novelty of the second and last stages also indicate that this entire routine can just be a small part of a bigger campaign targeting governments," the researchers said.

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Iranian Hacker](https://thehackernews.com/search/label/Iranian%20Hacker)[Malware](https://thehackernews.com/search/label/Malware)[OilRig](https://thehackernews.com/search/label/OilRig)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Imperson...