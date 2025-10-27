---
title: Rackspace Confirms Play Ransomware Gang Responsible for Recent Breach
url: https://thehackernews.com/2023/01/rackspace-confirms-play-ransomware-gang.html
source: The Hacker News
date: 2023-01-07
fetch_date: 2025-10-04T03:17:50.417765
---

# Rackspace Confirms Play Ransomware Gang Responsible for Recent Breach

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

# [Rackspace Confirms Play Ransomware Gang Responsible for Recent Breach](https://thehackernews.com/2023/01/rackspace-confirms-play-ransomware-gang.html)

**Jan 06, 2023**Ravie LakshmananCloud Security / Cyber Threat

[![Play Ransomware](data:image/png;base64... "Play Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIkYkTBU5KJGFe1OgGLpYygDiWxeko_-avcEdQlausI60efbG2CTSjXoushTX82kWSNdNGwqru9TyK8Ohoh9Af2DlFFuzSZEDV0NH_rRPaEYUi86D_fRS5OutucQG2fb-8zydnRbryW1mN5kn5PUKySHDQ1UTPRbRWn1T-eB2NPm0Jh80Md9edRKdq/s790-rw-e365/rackspace-breach.png)

Cloud services provider Rackspace on Thursday confirmed that the ransomware gang known as **Play** was responsible for last month's breach.

The security incident, which took place on December 2, 2022, leveraged a previously unknown security exploit to gain initial access to the Rackspace Hosted Exchange email environment.

"This zero-day exploit is associated with [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080)," the Texas-based company [said](https://status.apps.rackspace.com/index/viewincidents?group=2). "Microsoft disclosed CVE-2022-41080 as a privilege escalation vulnerability and did not include notes for [it] being part of a remote code execution chain that was exploitable."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Rackspace's forensic investigation found that the threat actor accessed the Personal Storage Table ([.PST](https://en.wikipedia.org/wiki/Personal_Storage_Table)) of 27 customers out of a total of nearly 30,000 customers on the Hosted Exchange email environment.

However, the company said there is no evidence the adversary viewed, misused, or distributed the customer's emails or data from those personal storage folders. It further said it intends to retire its Hosted Exchange platform as part of a planned migration to Microsoft 365.

It's not currently not known if Rackspace paid a ransom to the cybercriminals, but the disclosure follows a report from CrowdStrike last month that shed light on the new technique, dubbed [OWASSRF](https://thehackernews.com/2022/12/ransomware-hackers-using-new-way-to.html), employed by the Play ransomware actors.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The mechanism targets Exchange servers that are unpatched against the ProxyNotShell vulnerabilities ([CVE-2022-41040](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040) and [CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)) but have in place URL rewrite mitigations for the Autodiscover endpoint.

This involves an exploit chain comprising CVE-2022-41080 and CVE-2022-41082 to achieve remote code execution in a manner that bypasses the blocking rules through Outlook Web Access (OWA). The flaws were addressed by Microsoft in November 2022.

The Windows maker, in a statement shared with The Hacker News, urged customers to prioritize installing its [November 2022 Exchange Server updates](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-november-2022-exchange-server-security-updates/ba-p/3669045) and noted that the reported method targets vulnerable systems that have not applied the latest fixes.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Malware](https://thehackernews.com/search/label/Malware)[Rackspace](https://thehackernews.com/search/label/Rackspace)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](htt...