---
title: Silent Lynx Using PowerShell, Golang, and C++ Loaders in Multi-Stage Cyberattacks
url: https://thehackernews.com/2025/02/silent-lynx-using-powershell-golang-and.html
source: The Hacker News
date: 2025-02-06
fetch_date: 2025-10-06T20:39:57.062871
---

# Silent Lynx Using PowerShell, Golang, and C++ Loaders in Multi-Stage Cyberattacks

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

# [Silent Lynx Using PowerShell, Golang, and C++ Loaders in Multi-Stage Cyberattacks](https://thehackernews.com/2025/02/silent-lynx-using-powershell-golang-and.html)

**Feb 05, 2025**Ravie LakshmananThreat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1fPmPJRLqSkb80PZeZFaS74ZzuOkdMRmMRzBnV1mSf2wv2EVcLhaIzyuewmQTqTINBKrvuzJhP6FFPIWdX0Viwensz5FOmN4bnoqPZitCeTtT6rWL9bKq2LBh5Xu4q1KnD5AlvFbU1Jau_GX8YoTZmJgH_s90AhZS2dc4PgZvOroa4VaSrI5ApeVjMihX/s790-rw-e365/cyber.jpg)

A previously undocumented threat actor known as Silent Lynx has been linked to cyber attacks targeting various entities in Kyrgyzstan and Turkmenistan.

"This threat group has previously targeted entities around Eastern Europe and Central Asian government think tanks involved in economic decision making and banking sector," Seqrite Labs researcher Subhajeet Singha [said](https://www.seqrite.com/blog/silent-lynx-apt-targeting-central-asian-entities/) in a technical report published late last month.

Targets of the hacking group's attacks include embassies, lawyers, government-backed banks, and think tanks. The activity has been attributed to a Kazakhstan-origin threat actor with a medium level of confidence.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The infections commence with a spear-phishing email containing a RAR archive attachment that ultimately acts as a delivery vehicle for malicious payloads responsible for granting remote access to the compromised hosts.

The first of the two campaigns, detected by the cybersecurity company on December 27, 2024, leverages the RAR archive to launch an ISO file that, in turn, includes a malicious C++ binary and a decoy PDF file. The executable subsequently proceeds to run a PowerShell script that uses Telegram bots (named "@south\_korea145\_bot" and "@south\_afr\_angl\_bot") for command execution and data exfiltration.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiqjTGDze5_u41bJDoMUhhINMnnVhCKGNjTk5_exZvJi5z5XhR3-wvxX1WmtxwBY9Sxc-4vcH0ymnLEA42xqC23BB4YA0aoqkRkQdam4eW17UGKdB1osFF86zk8qTBzau6_qs_tPdbhA0seWGNQdw0ihHutbUUphBJccXaGVC5QeLVTs8u0pR715HjII0z/s790-rw-e365/map.png)

Some of the commands executed via the bots include curl commands to download and save additional payloads from a remote server ("pweobmxdlboi[.]com") or Google Drive.

The other campaign, in contrast, employs a malicious RAR archive containing two files: A decoy PDF and a Golang executable, the latter of which is designed to establish a reverse shell to an attacker-controlled server ("185.122.171[.]22:8082").

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Seqrite Labs said it observed some level of tactical overlaps between the threat actor and [YoroTrooper](https://thehackernews.com/2023/10/yorotrooper-researchers-warn-of.html) (aka SturgeonPhisher), which has been linked to attacks targeting the Commonwealth of Independent States (CIS) countries using PowerShell and Golang tools.

"Silent Lynx's campaigns demonstrate a sophisticated multi-stage attack strategy using ISO files, C++ loaders, PowerShell scripts, and Golang implants," Singha said.

"Their reliance on Telegram bots for command and control, combined with decoy documents and regional targeting which also highlights their focus on espionage in Central Asia and SPECA based nations."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Golang](https://thehackernews.com/search/label/Golang)[Malware](https://thehackernews.com/search/label/Malware)[powershell](https://thehackernews.com/search/label/powershell)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One...