---
title: North Korean Hackers Moonstone Sleet Push Malicious JS Packages to npm Registry
url: https://thehackernews.com/2024/08/north-korean-hackers-moonstone-sleet.html
source: The Hacker News
date: 2024-08-07
fetch_date: 2025-10-06T18:06:11.613984
---

# North Korean Hackers Moonstone Sleet Push Malicious JS Packages to npm Registry

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

# [North Korean Hackers Moonstone Sleet Push Malicious JS Packages to npm Registry](https://thehackernews.com/2024/08/north-korean-hackers-moonstone-sleet.html)

**Aug 06, 2024**Ravie LakshmananMalware / Windows Security

[![North Korean Hackers](data:image/png;base64... "North Korean Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlz59vQU4Xf_etL3k_9DIQH3sug8cvmLvK38yezMtVd3D321wlGuQJLr_De53d6uu4bOFRKkK-JjVhpTW8EUsnIToBYTOGIvyN4awSe4MkNCk6Tlw4AqihodN4jNrDpF-dvpr4CAy6GNFMJfwx8QK5_MuaWyuUuNskA4o-wyNQOdxfkOCbPYuAJIB_vvQf/s790-rw-e365/c2.png)

The North Korea-linked threat actor known as **Moonstone Sleet** has continued to push malicious npm packages to the JavaScript package registry with the aim of infecting Windows systems, underscoring the persistent nature of their campaigns.

The packages in question, [harthat-api](https://npm-stat.com/charts.html?package=harthat-api) and [harthat-hash](https://npm-stat.com/charts.html?package=harthat-hash), were published on July 7, 2024, according to Datadog Security Labs. Both the libraries did not attract any downloads and were shortly pulled after a brief period of time.

The security arm of the cloud monitoring firm is tracking the threat actor under the name Stressed Pungsan, which exhibits overlaps with a newly discovered North Korean malicious activity cluster dubbed Moonstone Sleet.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"While the name resembles the [Hardhat](https://www.npmjs.com/package/hardhat) npm package (an Ethereum development utility), its content does not indicate any intention to typosquat it," Datadog researchers Sebastian Obregoso and Zack Allen [said](https://securitylabs.datadoghq.com/articles/stressed-pungsan-dprk-aligned-threat-actor-leverages-npm-for-initial-access/). "The malicious package reuses code from a well-known GitHub repository called [node-config](https://github.com/node-config/node-config/) with over 6,000 stars and 500 forks, known in npm as config."

Attack chains orchestrated by the adversarial collective are known to disseminate bogus ZIP archive files via LinkedIn under a fake company name or freelancing websites, enticing prospective targets into executing next-stage payloads that invoke an npm package as part of a supposed technical skills assessment.

"When loaded, the malicious package used curl to connect to an actor-controlled IP and drop additional malicious payloads like SplitLoader," Microsoft [noted](https://thehackernews.com/2024/05/microsoft-uncovers-moonstone-sleet-new.html) in May 2024. "In another incident, Moonstone Sleet delivered a malicious npm loader which led to credential theft from LSASS."

Subsequent findings from Checkmarx [uncovered](https://thehackernews.com/2024/06/north-korean-hackers-target-brazilian.html) that Moonstone Sleet has also been attempting to spread their packages through the npm registry.

The newly discovered packages are designed to run a pre-install script specified in the package.json file, which, in turn, checks if it's running on a Windows system ("Windows\_NT"), after which it contacts an external server ("142.111.77[.]196") to download a DLL file that's sideloaded using the [rundll32.exe binary](https://attack.mitre.org/techniques/T1218/011/).

The rogue DLL, for its part, does not perform any malicious actions, suggesting either a trial run of its payload delivery infrastructure or that it was inadvertently pushed to the registry before embedding malicious code into it.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as South Korea's National Cyber Security Center (NCSC) [warned](https://ncsc.go.kr/main/cop/bbs/selectBoardArticle.do?bbsId=SecurityAdvice_main&nttId=146934&pageIndex=1&searchCnd2) of cyber attacks mounted by North Korean threat groups tracked as [Andariel](https://thehackernews.com/2024/07/us-doj-indicts-north-korean-hacker-for.html) and [Kimsuky](https://thehackernews.com/2024/05/kimsuky-apt-deploying-linux-backdoor.html) to deliver malware families such as Dora RAT and TrollAgent (aka Troll Stealer) as part of intrusion campaigns aimed at construction and machinery sectors in the country.

The Dora RAT attack sequence is noteworthy for the fact that the Andariel hackers exploited vulnerabilities in a domestic VPN software's software update mechanism to propagate the malware.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub](https://thehackernews.com/search/label/GitHub)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[North Korea](https://thehackernews.com/search/label/North%20Korea)[npm Registry](https://thehackernews.com/search/label/npm%20Registry)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "St...