---
title: CERT-UA Warns of Phishing Attacks Targeting Ukraine’s Defense and Security Force
url: https://thehackernews.com/2024/12/cert-ua-warns-of-phishing-attacks.html
source: The Hacker News
date: 2024-12-11
fetch_date: 2025-10-06T19:42:47.856743
---

# CERT-UA Warns of Phishing Attacks Targeting Ukraine’s Defense and Security Force

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

# [CERT-UA Warns of Phishing Attacks Targeting Ukraine's Defense and Security Force](https://thehackernews.com/2024/12/cert-ua-warns-of-phishing-attacks.html)

**Dec 10, 2024**Ravie LakshmananMalware / Cyber Attack

[![Phishing Attacks](data:image/png;base64... "Phishing Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtJ_5D9bVrLYcxGu6qSkuVn7CEGC99ZZTUQ_kNLWuvzuBXAfOzSi7khtYmp_DCmV-KHR8atwbbJ5dgDmOrRj-khoGTx06C39G5TsWrBJ9Ihd1uN_XClHVte8JOGUfyc3F21p4eSjwqH_vUzv2ofRC23D27NuHDHE5DNX-WGAWZNmqbZJ_igvHLCVXGqvIg/s790-rw-e365/malware.png)

The Computer Emergency Response Team of Ukraine (CERT-UA) has warned of a new set of cyber attacks that it said were aimed at defense companies in the country as well as its security and defense forces.

The phishing attacks have been attributed to a Russia-linked threat actor called **UAC-0185** (aka UNC4221), which has been active since at least 2022.

"The phishing emails mimicked official messages from the Ukrainian League of Industrialists and Entrepreneurs," CERT-UA [said](https://cert.gov.ua/article/6281632). "The emails advertised a conference held on December 5th in Kyiv, aimed at aligning the products of domestic defense industry companies with NATO standards."

The email messages come embedded with a malicious URL that urges the recipients to click on it to view "important information" related to their participation in the conference.

But in reality, doing so results in the download of a Windows shortcut file that, upon opening, is designed to execute an HTML Application, which, in turn, contains JavaScript code responsible for running PowerShell commands that are capable of loading next-stage payloads.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This includes a decoy file and a ZIP archive that contains a batch script, another HTML Application, and an executable file. In the final step, the batch script is launched to run the HTML Application file, which, then, runs the [MeshAgent](https://thehackernews.com/2024/08/ukraine-warns-of-new-phishing-campaign.html) binary on the host, granting the attackers remote control over the compromised system.

CERT-UA said the threat actor is primarily focused on stealing credentials associated with messaging apps like Signal, Telegram, and WhatsApp, and Ukraine's military systems such as DELTA, Teneta, and Kropyva.

"The hackers have also launched a number of cyber attacks to get unauthorized access to the PCs of defence companies' workers and representatives of the security and defence forces," the agency said.

According to Google-owned Mandiant, which exposed UNC4221 at the [SentinelLabs LABScon](https://www.sentinelone.com/blog/labscon-2024-security-research-in-real-time-talks-not-to-miss/) security conference earlier this September, the threat actor is [known](https://www.labscon.io/speakers/dan-black/) for collecting "battlefield-relevant data through the use of Android malware, phishing operations masquerading as Ukrainian military applications, and operations targeting popular messaging platforms like Telegram and WhatsApp."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Defense](https://thehackernews.com/search/label/Defense)[Malware](https://thehackernews.com/search/label/Malware)[Messaging Apps](https://thehackernews.com/search/label/Messaging%20Apps)[NATO](https://thehackernews.com/search/label/NATO)[Phishing](https://thehackernews.com/search/label/Phishing)[powershell](https://thehackernews.com/search/label/powershell)[Threat Actor](https://thehackernews.com/search/label/Threat%20Actor)[Ukraine](https://thehackernews.com/search/label/Ukraine)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump...