---
title: New Golang-Based Zergeca Botnet Capable of Powerful DDoS Attacks
url: https://thehackernews.com/2024/07/new-golang-based-zergeca-botnet-capable.html
source: The Hacker News
date: 2024-07-06
fetch_date: 2025-10-06T17:45:36.588948
---

# New Golang-Based Zergeca Botnet Capable of Powerful DDoS Attacks

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

# [New Golang-Based Zergeca Botnet Capable of Powerful DDoS Attacks](https://thehackernews.com/2024/07/new-golang-based-zergeca-botnet-capable.html)

**Jul 05, 2024**Ravie LakshmananNetwork Security / Cyber Attack

[![Powerful DDoS Attacks](data:image/png;base64... "Powerful DDoS Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVAOsbCVG11RWVag7PkQYKz7BAzpe9CYvguFuU10P7lGWUrz2Y90zDiQzYVflrXT7cLpMKYAbY6Ot_HOrWmYKJzRMYF8Vds5Q6QKrAhQmC2QHt8bFxobAh27kW0Ly9tHPArgldfXoOmRcNp2Vl0bfMEoBfk2SM9bu9_k-2WTy7FUesfHfaWNQtLBffN2Lh/s790-rw-e365/ddos.png)

Cybersecurity researchers have uncovered a new botnet called Zergeca that's capable of conducting distributed denial-of-service (DDoS) attacks.

Written in Golang, the botnet is so named for its reference to a string named "ootheca" present in the command-and-control (C2) servers ("ootheca[.]pw" and "ootheca[.]top").

"Functionally, Zergeca is not just a typical DDoS botnet; besides supporting six different attack methods, it also has capabilities for proxying, scanning, self-upgrading, persistence, file transfer, reverse shell, and collecting sensitive device information," the QiAnXin XLab team [said](https://blog.xlab.qianxin.com/a-deep-dive-into-the-zergeca-botnet/#background) in a report.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Zergeca is also notable for using DNS-over-HTTPS ([DoH](https://en.wikipedia.org/wiki/DNS_over_HTTPS)) to perform Domain Name System (DNS) resolution of the C2 server and using a lesser-known library known as [Smux](https://github.com/xtaci/smux) for C2 communications.

There is evidence to suggest that the attackers behind the botnet are actively developing and updating the malware to support new commands. What's more, the C2 IP address 84.54.51[.]82 is said to have been previously used to distribute the [Mirai botnet](https://thehackernews.com/2024/05/mirai-botnet-exploits-ivanti-connect.html) around September 2023.

As of April 29, 2025, the same IP address began to be used as a C2 server for the new botnet, raising the possibility that the threat actors "accumulated experience operating the Mirai botnets before creating Zergeca."

Attacks mounted by the botnet, primarily [ACK flood DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-an-ack-flood/), have targeted Canada, Germany, and the U.S. between early and mid-June 2024.

Zergeca's features span four distinct modules – namely persistence, proxy, silivaccine, and zombie – to set up persistence by adding a system service, implementing proxying, removing competing miner and backdoor malware, and gaining exclusive control over devices running the x86-64 CPU architecture, and handle the main botnet functionality.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The zombie module is responsible for reporting sensitive information from the compromised device to the C2 and awaits commands from the server, supporting six types of DDoS attacks, scanning, reverse shell, and other functions.

"The built-in competitor list shows familiarity with common Linux threats," XLab said. "Techniques like modified UPX packing, XOR encryption for sensitive strings, and using DoH to hide C2 resolution demonstrate a strong understanding of evasion tactics."

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

[botnet](https://thehackernews.com/search/label/botnet)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click ...