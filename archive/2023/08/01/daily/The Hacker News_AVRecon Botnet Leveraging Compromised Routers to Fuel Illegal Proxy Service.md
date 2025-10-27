---
title: AVRecon Botnet Leveraging Compromised Routers to Fuel Illegal Proxy Service
url: https://thehackernews.com/2023/07/avrecon-botnet-leveraging-compromised.html
source: The Hacker News
date: 2023-08-01
fetch_date: 2025-10-06T17:04:44.434527
---

# AVRecon Botnet Leveraging Compromised Routers to Fuel Illegal Proxy Service

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

# [AVRecon Botnet Leveraging Compromised Routers to Fuel Illegal Proxy Service](https://thehackernews.com/2023/07/avrecon-botnet-leveraging-compromised.html)

**Jul 31, 2023**Ravie LakshmananNetwork Security / Botnet

[![AVRecon Botnet](data:image/png;base64... "AVRecon Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzVGDjf5VeWkng-8Kx7vbCb4mJwZk-gSfrZ1LeuwM-dOgmFvk3H1WdQo4-4ITibc-3lTKG2RkrYp5VHNRi2HCoCnaU_3eDxOtNAOy6pJtA8CidEDzI7LYP_I20f7oxr1p9cnFPgJErdHlXjsDmfTRCmICAkzkyDngwvdd2jBdwt7GDWS7AGVsUfbalx6Hg/s790-rw-e365/proxy.jpg)

More details have emerged about a botnet called **AVRecon**, which has been observed making use of compromised small office/home office (SOHO) routers as part of a multi-year campaign active since at least May 2021.

AVRecon was [first disclosed](https://thehackernews.com/2023/07/new-soho-router-botnet-avrecon-spreads.html) by Lumen Black Lotus Labs earlier this month as malware capable of executing additional commands and stealing victim's bandwidth for what appears to be an illegal proxy service made available for other actors. It has also surpassed QakBot in terms of scale, having infiltrated over 41,000 nodes located across 20 countries worldwide.

"The malware has been used to create residential proxy services to shroud malicious activity such as password spraying, web-traffic proxying, and ad fraud," the researchers said in the report.

This has been corroborated by new findings from KrebsOnSecurity and Spur.us, which last week [revealed](https://krebsonsecurity.com/2023/07/who-and-what-is-behind-the-malware-proxy-service-socksescort/) that "AVrecon is the malware engine behind a 12-year-old service called SocksEscort, which rents hacked residential and small business devices to cybercriminals looking to hide their true location online."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The basis for the connection stems from direct correlations between SocksEscort and AVRecon's command-and-control (C2) servers. SocksEscort is also said to share overlaps with a Moldovan company named Server Management LLC that offers a mobile VPN solution on the Apple Store called [HideIPVPN](https://apps.apple.com/us/app/hideipvpn-vpn-smart-dns/id964479810).

Black Lotus Labs told The Hacker News that the new infrastructure it identified in connection with the malware exhibited the same characteristics as the old AVrecon C2s.

|  |
| --- |
| [![AVRecon Botnet](data:image/png;base64... "AVRecon Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoNCrSGLc6tYPXw5XRmxEZRfRanfVApP46OG1eguylrUPuhfRjciU4Aa0fKTLw3rjUM3BsdtJ2_uZwlpy3Nzxtpjq9iw7b8zd3XzHOEnWZkvL8I1pLNw1K37xFyBvIDcuOPOme-APPA1WL7YCvzeNii1ctUTW3eUITQDWKXmDMJWl3PRw3WUN3G1LHTpAL/s790-rw-e365/graph.jpg) |
| The new SocksEscort nodes, which shifted during the second week of July (Source: Lumen Black Lotus Labs) |

"We assess that the threat actors were reacting to our publication and null-routing their infrastructure, and attempting to maintain control over the botnet," the company said. "This suggests the actors wish to further monetize the botnet by maintaining some access and continue enrolling users in the SocksEscort 'proxy as a service.'"

Routers and other edge appliances have become [lucrative attack vectors](https://thehackernews.com/2023/07/chinese-apt41-hackers-target-mobile.html) in recent years owing to the fact that such devices are infrequently patched against security issues, may not support endpoint detection and response (EDR) solutions, and are designed to handle higher bandwidths.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

AVRecon also poses a heightened threat for its ability to spawn a shell on a compromised machine, potentially enabling threat actors to obfuscate their own malicious traffic or retrieve further malware for post-exploitation.

"While these bots are primarily being added to the SocksEscort proxy service, there was embedded functionality within the file to spawn a remote shell," the researchers said.

"This could allow the threat actor the ability to deploy additional modules, so we suggest that managed security providers attempt to investigate these devices in their networks, while home users should power-cycle their devices."

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

[Black Lotus Labs](https://thehackernews.com/search/label/Black%20Lotus%20Labs)[botnet](https://thehackernews.com/search/label/botnet)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Proxy Service](https://thehackernews.com/search/label/Proxy%20Service)[SOHO routers](https://thehackernews.com/search/label/SOHO%20routers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Ente...