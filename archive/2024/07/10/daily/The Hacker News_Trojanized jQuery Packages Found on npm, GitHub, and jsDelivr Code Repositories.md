---
title: Trojanized jQuery Packages Found on npm, GitHub, and jsDelivr Code Repositories
url: https://thehackernews.com/2024/07/trojanized-jquery-packages-found-on-npm.html
source: The Hacker News
date: 2024-07-10
fetch_date: 2025-10-06T17:48:30.056083
---

# Trojanized jQuery Packages Found on npm, GitHub, and jsDelivr Code Repositories

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

# [Trojanized jQuery Packages Found on npm, GitHub, and jsDelivr Code Repositories](https://thehackernews.com/2024/07/trojanized-jquery-packages-found-on-npm.html)

**Jul 09, 2024**Ravie LakshmananSupply Chain Attack / Web Security

[![Trojanized jQuery Packages](data:image/png;base64... "Trojanized jQuery Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF12l_elDCARlGbY0WSBN6nOXtl0q3arjVsa43aMTtADcN5x5fIVai4nIX8mSloKW139sJ_Rf4cxBd115Vc5gOMzgo21HJmTbBU4ZE9D1ru5hvavh2MPtuqCDed6kBaVlbX3kLraoM7Ow2eOt2JUBy-KBe64gX1it5aUpMkEieboSi0BVgIBgfq0sMjmja/s790-rw-e365/jquery.png)

Unknown threat actors have been found propagating trojanized versions of [jQuery](https://en.wikipedia.org/wiki/JQuery) on npm, GitHub, and jsDelivr in what appears to be an instance of a "complex and persistent" supply chain attack.

"This attack stands out due to the high variability across packages," Phylum [said](https://blog.phylum.io/persistent-npm-campaign-shipping-trojanized-jquery/) in an analysis published last week.

"The attacker has cleverly hidden the malware in the seldom-used '[end](https://api.jquery.com/end/)' function of jQuery, which is internally called by the more popular '[fadeTo](https://api.jquery.com/fadeTo/)' function from its animation utilities."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As many as 68 packages have been linked to the campaign. They were published to the npm registry starting from May 26 to June 23, 2024, using names such as cdnjquery, footersicons, jquertyi, jqueryxxx, logoo, and sytlesheets, among others.

There is evidence to suggest that each of the bogus packages were manually assembled and published due to the sheer number of packages published from various accounts, the differences in naming conventions, the inclusion of personal files, and the long time period over which they were uploaded.

This is unlike other commonly observed methods in which attackers tend to follow a predefined pattern that underscores an element of automation involved in creating and publishing the packages.

The malicious changes, per Phylum, have been introduced in a function named "end," allowing the threat actor to exfiltrate website form data to a remote URL.

Further investigation has found the trojanized jQuery file to be hosted on a GitHub repository associated with an account called "[indexsc](https://github.com/indexsc)." Also present in the same repository are JavaScript files containing a script pointing to the modified version of the library.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"It's worth noting that jsDelivr constructs these GitHub URLs automatically without needing to upload anything to the CDN explicitly," Phylum said.

"This is likely an attempt by the attacker to make the source look more legitimate or to sneak through firewalls by using jsDelivr instead of loading the code directly from GitHub itself."

The development comes as Datadog [identified](https://securitylabs.datadoghq.com/articles/malicious-pypi-package-targeting-highly-specific-macos-machines/) a series of packages on the Python Package Index (PyPI) repository with capabilities to download a second-stage binary from an attacker-controlled server depending on the CPU architecture.

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

[Code Repository](https://thehackernews.com/search/label/Code%20Repository)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub](https://thehackernews.com/search/label/GitHub)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Web Development](https://thehackernews.com/search/label/Web%20Development)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet A...