---
title: Hackers Hijack Unsecured Jupyter Notebooks to Stream Illegal Sports Broadcasts
url: https://thehackernews.com/2024/11/hackers-hijack-unsecured-jupyter.html
source: The Hacker News
date: 2024-11-20
fetch_date: 2025-10-06T19:23:38.550205
---

# Hackers Hijack Unsecured Jupyter Notebooks to Stream Illegal Sports Broadcasts

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

# [Hackers Hijack Unsecured Jupyter Notebooks to Stream Illegal Sports Broadcasts](https://thehackernews.com/2024/11/hackers-hijack-unsecured-jupyter.html)

**Nov 19, 2024**Ravie LakshmananCloud Security / Piracy

[![Illegal Sports Broadcasts](data:image/png;base64... "Illegal Sports Broadcasts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEing-tuErIMAsMsios_6cAX77xjGExiBaeSAs3YnNSyedA6pkyVyikWiYA6pcSLI2yLlnfItzk7A9RGSQWtNIBcDnHjbHv1_kjR9keBsDpC1xlvhyphenhyphen02loFPWdd2zY66eWySJVi7dBbiRLEtBiMkvt3m_nN793Ddz2u4LNhHfxfVkbBw6TrgIq_j9CP1OdjB/s790-rw-e365/streaming.png)

Malicious actors are exploiting misconfigured JupyterLab and Jupyter Notebooks to conduct stream ripping and enable sports piracy using live streaming capture tools.

The attacks involve the hijack of unauthenticated Jupyter Notebooks to establish initial access, and perform a series of actions designed to facilitate illegal live streaming of sports events, Aqua said in a [report](https://www.aquasec.com/blog/threat-actors-hijack-misconfigured-servers-for-live-sports-streaming/) shared with The Hacker News.

The covert piracy campaign within interactive environments widely used for data science applications was discovered by the cloud security firm following an attack against its honeypots.

"First, the attacker updated the server, then downloaded the tool [FFmpeg](https://ffmpeg.org)," said Assaf Morag, director of threat intelligence at cloud security firm Aqua. "This action alone is not a strong enough indicator for security tools to flag malicious activity."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Next, the attacker executed FFmpeg to capture live streams of sports events and redirected them to their server."

In a nutshell, the end goal of the campaign is to download FFmpeg from MediaFire and use it to record live sports events feeds from the Qatari beIN Sports network and duplicate the broadcast on their illegal server via ustream[.]tv.

[![Illegal Sports Broadcasts](data:image/png;base64... "Illegal Sports Broadcasts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPvnKqtOSWe14Z3PIDZQLi8ICDn9MMfvVEl7Y4PBqW6gVg4667thyLswGV_LkYfkLRQo_hbJwYm1-zCwCIFsPAIYgKuWRqV0R-aIZM6nKuvmSmAPh_HDgmEqkYteXyPWX9O-2t3nsC_w8rpLIummOMl_nj9yrm_RCcCYijqIe-3GuCzNZ0sZ0CaHNewh6y/s790-rw-e365/attack.png)

This not only facilitates the abuse of compromised Jupyter Notebook server and its resources by serving as an intermediary, but also enables threat actors to make a profit through advertising revenue by illicitly broadcasting the live streams.

It's not clear who is behind the campaign, although there are indications that they could be of Arab-speaking origin owing to one of the IP addresses used (41.200.191[.]23).

"However, it's crucial to remember that the attackers gained access to a server intended for data analysis, which could have serious consequences for any organization's operations," Morag said.

"Potential risks include denial-of-service, data manipulation, data theft, corruption of AI and ML processes, lateral movement to more critical environments, and, in the worst-case scenario, substantial financial and reputational damage."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data science](https://thehackernews.com/search/label/data%20science)[FFmpeg](https://thehackernews.com/search/label/FFmpeg)[Jupyter Notebooks](https://thehackernews.com/search/label/Jupyter%20Notebooks)[JupyterLab](https://thehackernews.com/search/label/JupyterLab)[MediaFire](https://thehackernews.com/search/label/MediaFire)[Sports Piracy](https://thehackernews.com/search/label/Sports%20Piracy)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI ...