---
title: Malicious npm Packages Found Using Image Files to Hide Backdoor Code
url: https://thehackernews.com/2024/07/malicious-npm-packages-found-using.html
source: The Hacker News
date: 2024-07-17
fetch_date: 2025-10-06T17:46:52.496302
---

# Malicious npm Packages Found Using Image Files to Hide Backdoor Code

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

# [Malicious npm Packages Found Using Image Files to Hide Backdoor Code](https://thehackernews.com/2024/07/malicious-npm-packages-found-using.html)

**Jul 16, 2024**Ravie LakshmananOpen Source / Software Supply Chain

[![Malicious npm](data:image/png;base64... "Malicious npm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg913tMY0qhkLlenwXT_Mnu5o-F5fu946nEcS7iNHZA7GPAWCKeIzXBQLEsJ4XwjvAzdhIYr94rLOGMSdtU_zZoJMh7F4wCfbRyCheELaSIsA9FxEVN3borIh0dWWJqoPfPphIlvy7R1uQSAmCA9ieJnemCRi5k_LC6aAloFNmU4vIlldLOJqUeqvjm23uP/s790-rw-e365/code.png)

Cybersecurity researchers have identified two malicious packages on the npm package registry that concealed backdoor code to execute malicious commands sent from a remote server.

The packages in question – img-aws-s3-object-multipart-copy and legacyaws-s3-object-multipart-copy – have been downloaded [190](https://npm-stat.com/charts.html?package=img-aws-s3-object-multipart-copy) and [48 times](https://npm-stat.com/charts.html?package=legacyaws-s3-object-multipart-copy) each. As of writing, they have been taken down by the npm security team.

"They contained sophisticated command and control functionality hidden in image files that would be executed during package installation," software supply chain security firm Phylum [said](https://blog.phylum.io/fake-aws-packages-ship-command-and-control-malware-in-jpeg-files/) in an analysis.

The packages are designed to impersonate a legitimate npm library called [aws-s3-object-multipart-copy](https://github.com/little-core-labs/aws-s3-object-multipart-copy), but come with an altered version of the "index.js" file to execute a JavaScript file ("loadformat.js").

For its part, the JavaScript file is designed to process three images -- that feature the corporate logos for Intel, Microsoft, and AMD -- with the image corresponding to Microsoft's logo used to extract and execute the malicious content.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The code works by registering the new client with a command-and-control (C2) server by sending the hostname and operating system details. It then attempts to execute attacker-issued commands periodically every five seconds.

In the final stage, the output of the commands' execution is exfiltrated back to the attacker via a specific endpoint.

"In the last few years, we've seen a dramatic rise in the sophistication and volume of malicious packages published to open source ecosystems," Phylum said.

"Make no mistake, these attacks are successful. It is absolutely imperative that developers and security organizations alike are keenly aware of this fact and are deeply vigilant with regard to open source libraries they consume."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Code Injection](https://thehackernews.com/search/label/Code%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[npm Registry](https://thehackernews.com/search/label/npm%20Registry)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Package Management](https://thehackernews.com/search/label/Package%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software development](https://thehackernews.com/search/label/software%20development)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

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

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](https://thehackerne...