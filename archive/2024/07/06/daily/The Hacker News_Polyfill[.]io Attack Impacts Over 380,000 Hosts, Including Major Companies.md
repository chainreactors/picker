---
title: Polyfill[.]io Attack Impacts Over 380,000 Hosts, Including Major Companies
url: https://thehackernews.com/2024/07/polyfillio-attack-impacts-over-380000.html
source: The Hacker News
date: 2024-07-06
fetch_date: 2025-10-06T17:45:33.727584
---

# Polyfill[.]io Attack Impacts Over 380,000 Hosts, Including Major Companies

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

# [Polyfill[.]io Attack Impacts Over 380,000 Hosts, Including Major Companies](https://thehackernews.com/2024/07/polyfillio-attack-impacts-over-380000.html)

**Jul 05, 2024**Ravie LakshmananSupply Chain Attack / Malware

[![Polyfill Attack](data:image/png;base64... "Polyfill Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4pLyZRjUlwwDS7wu0RqPqlzJi1UA8JDMf4RM6i-So-sGjvIMDe5rGC15ZdBUUmKX-2_scZUf5Ye3vhNP0QO2MXgfHlTMTbaC4FSSivforoLh_zXAiONEXfQvQZTj0NTk1QyXhjlopQ-Jt9eAZlO0ZAivaJho-m654hIwZs0hjfxG0rfDv5xNqSkZlw6ys/s790-rw-e365/code.png)

The supply chain attack targeting the widely-used Polyfill[.]io JavaScript library is broader in scope than previously thought, with [new findings](https://censys.com/july-2-polyfill-io-supply-chain-attack-digging-into-the-web-of-compromised-domains/) from Censys showing that over 380,000 hosts are embedding a polyfill script linking to the malicious domain as of July 2, 2024.

This includes references to "https://cdn.polyfill[.]io" or "https://cdn.polyfill[.]com" in their HTTP responses, the attack surface management firm said.

"Approximately 237,700, are located within the Hetzner network (AS24940), primarily in Germany," it noted. "This is not surprising – Hetzner is a popular web hosting service, and many website developers leverage it."

Further analysis of the affected hosts has revealed domains tied to prominent companies like WarnerBros, Hulu, Mercedes-Benz, and Pearson that reference the malicious endpoint in question.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Details of the attack emerged in late June 2024 when Sansec [alerted](https://thehackernews.com/2024/06/over-110000-websites-affected-by.html) that code hosted on the Polyfill domain had been modified to redirect users to adult- and gambling-themed websites. The code changes were made such that the redirections only took place at certain times of the day and only against visitors who met certain criteria.

The nefarious behavior is said to have been introduced after the domain and its associated GitHub repository were sold to a Chinese company named Funnull in February 2024.

The development has since prompted domain registrar Namecheap to suspend the domain, content delivery networks such as Cloudflare to automatically replace Polyfill links with domains leading to alternative safe mirror sites, and Google to block ads for sites embedding the domain.

[![Polyfill Attack](data:image/png;base64... "Polyfill Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdf4eeQ3xReqTouf1cP_bDJpE4waU9o9JaDj2CJoKHfOZvWWUZpeTgn74F4EOpxupba_F_QF-_nvNujCCpTfQSrUCkFj6IAmwJyX4jogjgz1S2xB37CcRZ7AJhkq0H55N1GJLXewQuWnlpdQkfDAOLGtddEb31wKdosLQK93CFh3zJkXOU6jfcOPk__xOX/s790-rw-e365/data.png)

While the operators attempted to relaunch the service under a different domain named polyfill[.]com, it was also [taken down](https://x.com/Namecheap/status/1806423413151457685) by Namecheap as of June 28, 2024. Of the [two other domains](https://x.com/Polyfill_Global/status/1807717516095172956) registered by them since the start of July – polyfill[.]site and polyfillcache[.]com – the latter remains up and running.

On top of that, a more [extensive network](https://sansec.io/research/polyfill-supply-chain-attack) of potentially related domains, including bootcdn[.]net, bootcss[.]com, staticfile[.]net, staticfile[.]org, unionadjs[.]com, xhsbpza[.]com, union.macoms[.]la, newcrbpc[.]com, has been uncovered as tied to the maintainers of Polyfill, indicating that the incident might be part of a broader malicious campaign.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"One of these domains, bootcss[.]com, has been observed engaging in malicious activities that are very similar to the polyfill[.]io attack, with evidence dating back to June 2023," Censys noted, adding it discovered 1.6 million public-facing hosts that link to these suspicious domains.

"It wouldn't be entirely unreasonable to consider the possibility that the same malicious actor responsible for the polyfill.io attack might exploit these other domains for similar activities in the future."

The development comes as WordPress security company Patchstack [warned](https://patchstack.com/articles/polyfill-vulnerability-effect-on-the-wordpress-ecosystem/) of cascading risks posed by the Polyfill supply chain attack on sites running the content management system (CMS) through dozens of legitimate plugins that link to the rogue domain.

Software supply chain security firm Phylum, in a [similar advisory](https://blog.phylum.io/a-note-about-polyfill/), said that it found over 1,250 packages on PyPI and npm that reference the domain polyfill[.]io, urging users relying on the libraries to "check these references and understand the conditions under which they are invoked."

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

[CloudFlare](https://thehackernews.com/search/label/CloudFlare)[Content Delivery Network](https://thehackernews.com/search/label/Content%20Delivery%20Network)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JavaScript](https://thehackernews.com/searc...