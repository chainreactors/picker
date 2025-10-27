---
title: Cyber Espionage Alert: LilacSquid Targets IT, Energy, and Pharma Sectors
url: https://thehackernews.com/2024/05/cyber-espionage-alert-lilacsquid.html
source: The Hacker News
date: 2024-05-31
fetch_date: 2025-10-06T16:54:04.689840
---

# Cyber Espionage Alert: LilacSquid Targets IT, Energy, and Pharma Sectors

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

# [Cyber Espionage Alert: LilacSquid Targets IT, Energy, and Pharma Sectors](https://thehackernews.com/2024/05/cyber-espionage-alert-lilacsquid.html)

**May 30, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP-0tPvdVxLiudeZNkhmcVrIIDHzugII2J9cwrkd9Jgv1cJ4moSVi1w2Dz8eiMiPNZRkRS82-Vnx1tRkM9eI_NyyFn_onTi9ucCeGXr2pswPjtTyTDnF080T5zM7g5ArztT7Lc1w6Ipo5ywQNCtCJVZtg2tgOgYczSgxRjUb_FHhB6UHil0uKaAf0qVrFo/s790-rw-e365/ciscoc.png)

A previously undocumented cyber espionage-focused threat actor named **LilacSquid** has been linked to targeted attacks spanning various sectors in the United States (U.S.), Europe, and Asia as part of a data theft campaign since at least 2021.

"The campaign is geared toward establishing long-term access to compromised victim organizations to enable LilacSquid to siphon data of interest to attacker-controlled servers," Cisco Talos researcher Asheer Malhotra [said](https://blog.talosintelligence.com/lilacsquid/) in a new technical report published today.

Targets include information technology organizations building software for the research and industrial sectors in the U.S, energy companies in Europe, and the pharmaceutical sector in Asia, indicating a broad victimology footprint.

Attack chains are known to exploit either publicly known vulnerabilities to breach internet-facing application servers or make use of compromised remote desktop protocol (RDP) credentials to deliver a mix of open-source tools and custom malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The campaign's most distinctive feature is the use of an open-source remote management tool called MeshAgent, which serves as a conduit to deliver a bespoke version of [Quasar RAT](https://www.cisa.gov/news-events/analysis-reports/ar18-352a) codenamed PurpleInk.

Alternate infection procedures leveraging compromised RDP credentials exhibit a slightly different modus operandi, wherein the threat actors choose to either deploy MeshAgent or drop a .NET-based loader dubbed InkLoader to drop PurpleInk.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnrslJutILn5-rFJ-yIIPk9iOOEelPYn72r0zy6kHGher83YB8IUVPFizPhBufy-NCKldpqSPlufgh27Ml8L5hh_Mh29cVp8yW0PikALmxR9ZpK-lhfeW8wcrPOzho3bUXAJaCCQ7TGo_-OZMbeyo80AKlwnPzUa4LmLuED2l_Ie_cGQyZnU_w_xddC4pF/s790-rw-e365/cisco.png)

"A successful login via RDP leads to the download of InkLoader and PurpleInk, copying these artifacts into desired directories on disk and the subsequent registration of InkLoader as a service that is then started to deploy InkLoader and, in turn, PurpleInk," Malhotra said.

PurpleInk, actively maintained by LilacSquid since 2021, is both heavily obfuscated and versatile, allowing it to run new applications, perform file operations, get system information, enumerate directories and processes, launch a remote shell, and connect to a specific remote address provided by a command-and-control (C2) server.

Recent variants of the trojan discovered in 2023 and 2024 are a lot more rudimentary, the malware authors whittling the features down to creating a reverse shell and communicating with a proxy for data transfer. This is presumably an attempt to remove redundant functionality and sidestep detection.

Talos said it identified another custom tool called InkBox that's said to have been used by the adversary to deploy PurpleInk prior to its switch to InkLoader.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The incorporation of MeshAgent as part of their post-compromise playbooks is noteworthy in part due to the fact that it's a tactic [previously adopted](https://thehackernews.com/2024/03/new-deepgosu-malware-campaign-targets.html) by a North Korean threat actor named [Andariel](https://asec.ahnlab.com/en/63192/), a sub-cluster within the infamous Lazarus Group, in attacks targeting South Korean companies.

Another overlap concerns the use of tunneling tools to maintain secondary access, with LilacSquid deploying Secure Socket Funneling ([SSF](https://github.com/securesocketfunneling/ssf)) to create a communication channel to its infrastructure.

"Multiple tactics, techniques, tools, and procedures (TTPs) utilized in this campaign bear some overlap with North Korean APT groups, such as Andariel and its parent umbrella group, Lazarus," Malhotra said.

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Information security](https://thehackernews.com/search/label/Information%20security)[Malware](https://thehackernews.com/search/label/Malware)[national security](https://thehackernews.com/search/label/national%20security)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Inc...