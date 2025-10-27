---
title: Kazakh Organizations Targeted by 'Bloody Wolf' Cyber Attacks
url: https://thehackernews.com/2024/08/kazakh-organizations-targeted-by-bloody.html
source: The Hacker News
date: 2024-08-06
fetch_date: 2025-10-06T18:06:18.132616
---

# Kazakh Organizations Targeted by 'Bloody Wolf' Cyber Attacks

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

# [Kazakh Organizations Targeted by 'Bloody Wolf' Cyber Attacks](https://thehackernews.com/2024/08/kazakh-organizations-targeted-by-bloody.html)

**Aug 05, 2024**Ravie LakshmananNetwork Security / Threat Intelligence

[![Cyber Attacks](data:image/png;base64... "Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUArKFGqz0fnu0Yi29T2v8clRM79HzFDfT4G8DyOr2x9mnVnPETT4wK3Xdi3oah27YPuXAs97oYhnkAy5eybIyf1LNd6LlSQTjk5k5YE9JiA20InmUkMBueEByTdEI2m8TXKtOcTgkVWF6sVcCj8DH-nAxj3P9tXQJKwxoNi6nt0_M7RAL7FY3nm5GaJ8V/s790-rw-e365/cyberattack.png)

Organizations in Kazakhstan are the target of a threat activity cluster dubbed **Bloody Wolf** that delivers a commodity malware called [STRRAT](https://thehackernews.com/2024/03/alert-cybercriminals-deploying-vcurms.html) (aka Strigoi Master).

"The program selling for as little as $80 on underground resources allows the adversaries to take control of corporate computers and hijack restricted data," cybersecurity vendor BI.ZONE [said](https://bi.zone/eng/expertise/blog/bloody-wolf-primenyaet-kommercheskoe-vpo-strrat-protiv-organizatsiy-v-kazakhstane/) in a new analysis.

The cyber attacks employ phishing emails as an initial access vector, impersonating the Ministry of Finance of the Republic of Kazakhstan and other agencies to trick recipients into opening PDF attachments.

The file purports to be a non-compliance notice and contains links to a malicious Java archive (JAR) file as well as an installation guide for the Java interpreter necessary for the malware to function.

In an attempt to lend legitimacy to the attack, the second link points to a web page associated with the country's government website that urges visitors to install Java in order to ensure that the portal is operational.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The STRRAT malware, hosted on a website that mimics the website of the Kazakhstan government ("egov-kz[.]online"), sets up persistence on the Windows host by means of a Registry modification and runs the JAR file every 30 minutes.

What's more, a copy of the JAR file is copied to the Windows startup folder to ensure that it automatically launches after a system reboot.

Subsequently, it establishes connections with a Pastebin server to exfiltrate sensitive information from the compromised machine, including details about operating system version and antivirus software installed, and account data from Google Chrome, Mozilla Firefox, Internet Explorer, Foxmail, Outlook, and Thunderbird.

It's also designed to receive additional commands from the server to download and execute more payloads, log keystrokes, run commands using cmd.exe or PowerShell, restart or shut down the system, install a proxy, and remove itself.

"Using less common file types such as JAR enables the attackers to bypass defenses," BI.ZONE said. "Employing legitimate web services such as Pastebin to communicate with the compromised system makes it possible to evade network security solutions."

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

[Corporate security](https://thehackernews.com/search/label/Corporate%20security)[Cyber Defense](https://thehackernews.com/search/label/Cyber%20Defense)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

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

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Pal...