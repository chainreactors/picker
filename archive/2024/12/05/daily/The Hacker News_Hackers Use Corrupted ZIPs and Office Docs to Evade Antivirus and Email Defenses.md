---
title: Hackers Use Corrupted ZIPs and Office Docs to Evade Antivirus and Email Defenses
url: https://thehackernews.com/2024/12/hackers-use-corrupted-zips-and-office.html
source: The Hacker News
date: 2024-12-05
fetch_date: 2025-10-06T19:42:27.419010
---

# Hackers Use Corrupted ZIPs and Office Docs to Evade Antivirus and Email Defenses

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

# [Hackers Use Corrupted ZIPs and Office Docs to Evade Antivirus and Email Defenses](https://thehackernews.com/2024/12/hackers-use-corrupted-zips-and-office.html)

**Dec 04, 2024**Ravie LakshmananEmail Security / Malware

[![Evade Antivirus and Email Defenses](data:image/png;base64... "Evade Antivirus and Email Defenses")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlznOookZQSNVcdC6gHOJeuRkmrd0QeSnd-6aQIVKXWZ2I4CFrjnnvjWhBTm4jHkLu9P__JA1LDW9qZaghVN11OUfvozDMv_1RvGi9SxkVrw1vcoMhLfoHndOLf9wWcYP4hwGi1UkQCEMCwRIRPFfnBiTlO9yX4kRrywvx6J9sWC0N8o6gffJd7LdNGsm_/s790-rw-e365/zip-word.png)

Cybersecurity researchers have called attention to a novel phishing campaign that leverages corrupted Microsoft Office documents and ZIP archives as a way to bypass email defenses.

"The ongoing attack evades #antivirus software, prevents uploads to sandboxes, and bypasses Outlook's spam filters, allowing the malicious emails to reach your inbox," ANY.RUN [said](https://x.com/anyrun_app/status/1861024182210900357) in a series of posts on X.

The malicious activity entails sending emails containing ZIP archives or Office attachments that are intentionally corrupted in such a way that they cannot be scanned by security tools. These messages aim to trick users into opening the attachments with false promises of employee benefits and bonuses.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In other words, the corrupted state of the files means that they are not flagged as suspicious or malicious by email filters and antivirus software.

However, the attack still works because it takes advantage of the built-in recovery mechanisms of programs like Word, Outlook, and WinRAR to relaunch such damaged files in recovery mode.

[![Evade Antivirus and Email Defenses](data:image/png;base64... "Evade Antivirus and Email Defenses")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFJ0M7D-5hD4NmjEBT7C3b2xkmLBz0OYqDK8JiZCvVNNita1CF2SKaMCItzetkOgleH3psXbpTC8KroYnSRX7TjFwC3wqtYZDZWyVPPwo6FfnxtxbVrnVYz9-FnI-JBciMSbUCcHcDiMHsOshwqx19ohsPNqnpBkId-fD11WzN-6sA98ROKKx53k2uHdBx/s790-rw-e365/GdOvhTYXIAAebhk.jpg)

ANY.RUN has revealed that the attack technique has been employed by threat actors at least since August 2024, describing it as a potential zero-day that is being exploited to evade detection.

The end goal of these attacks is to deceive users into opening booby-trapped documents, which embed QR codes that, when scanned, redirect victims to fraudulent websites for malware deployment or fake login pages for credential theft.

The findings once again illustrate how bad actors are constantly on the lookout for previously unseen techniques to get around email security software and ensure their phishing emails land in targets' inboxes.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Although these files operate successfully within the OS, they remain undetected by most security solutions due to the failure to apply proper procedures for their file types," ANY.RUN said.

"The file remains undetectable by security tools, yet user applications handle it seamlessly due to built-in recovery mechanisms exploited by attackers."

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

[Antivirus](https://thehackernews.com/search/label/Antivirus)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[Malware](https://thehackernews.com/search/label/Malware)[Microsoft office](https://thehackernews.com/search/label/Microsoft%20office)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.co...