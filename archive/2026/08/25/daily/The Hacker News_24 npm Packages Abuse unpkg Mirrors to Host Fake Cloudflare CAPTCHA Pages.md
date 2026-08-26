---
title: 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages
url: https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html
source: The Hacker News
date: 2026-08-25
fetch_date: 2026-08-26T03:07:02.665865
---

# 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html)

**Ravie Lakshmanan**Aug 25, 2026Phishing / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6XLRNvnqL3SBGR1Hrv9eIrUlQ8Tr6RhA2dwxYZYKiNoh7qZwgA8aGATBHsDqQCD6ilgXGlLdMIs54WZ5jEW4G_TjJiFyQ6u5acpyUE5vdHa-0E-SZwIliX9sTQqcOw6pNG0TlGm-lUQrvdEEKdSOnB-Mep1U7GVVW-qOQiD1PEDItN-lDv3mOjexfo29x/s1700-e365/cf-phishing.jpg)

Cybersecurity researchers have disclosed details of a new campaign that uses a cluster of 24 npm packages as free phishing infrastructure for redirecting to ClickFix-style fake CAPTCHA pages.

"While the malware is simply a single HTML page inside the npm package, and while downloading it wouldn't do harm, the threat actor’s use of npm isn't to infect developers who install it, but to use the registry and its mirrors as a safe, validated storage for the malware," OX Security researchers Moshe Siman Tov Bustan and Vitalii Chepurko [said](https://www.ox.security/blog/research-clickfix-phishing-npm-packages/).

The list of npm packages, some of which are still available for download, is below -

* bgzxcuite2
* prezdentkxheiw
* egair0810
* mnteckets
* airdzticket
* egypt0811
* passport811
* vxhjkseuiaqkb
* ndmushdkeqe
* ndmxchdjxn2
* ndmfguyhoxc3
* mjsdqwocvn
* m2fcsfyjkuxb
* m3fdfocdoewn
* @worrisome/reutil
* testdgdbcsd
* tesgfvbncsdbcv
* mndsxcusiwlk1
* mn2adskhweox
* mn3sadkoiewu
* mn4xcouzvhus
* mbxcnsuwgs1
* skxcmwuncbg2
* mobiwaefhxc3

The campaign specifically targets mirrors like unpkg. Once mirrored on these services, the HTML file (e.g., "unpkg[.]com/ndmxchdjxn2@1.0.0/index.html") becomes a live, fully-rendered fake Cloudflare CAPTCHA page that's hosted on a trusted domain but redirects to ClickFix phishing infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

As a result, anyone who opens a link that's hosted on the npm mirror will be tricked into carrying out unintended actions that can lead to the deployment of malware. This involves displaying a fake Cloudflare verification page, which then sends the target to an external website controlled by the attacker.

The HTML page embeds the logic to serve the bogus CAPTCHA verification prompt, as well as JavaScript necessary to send a request to a remote server. Initial iterations of the malware were found to send the request to a typosquat domain that impersonates the Microsoft login page ("login[.]microsofte[.]live").

But after the domain was added to Google Chrome's Safe Browsing blocklist, the threat actor behind the campaign is said to have responded by switching to [KeyVal](https://keyval.org/) ("api.keyval[.]org"), a free, public key-value store that allows developers to set a key-value pair or retrieve a value given a key using a REST API.

In doing so, it turns the legitimate service into a dead drop resolver ([DDR](https://www.cc.gatech.edu/news/hiding-plain-sight-disrupting-malwares-secret-web-dead-drops)) and uses it to extract and decode the URL to which the victim is redirected to.

"Currently the remote logic transfers the user to the legitimate ChatGPT website, but it could be weaponized to deliver ClickFix or any other phishing domains when configured to by the attacker," the researchers said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

This is not the first time this approach has been abused by bad actors. In October 2025, Socket [detailed](https://thehackernews.com/2025/10/175-malicious-npm-packages-with-26000.html) a set of 175 npm packages that used unpkg.com's content delivery network (CDN) to host redirect scripts that routed victims to credential harvesting pages as part of a campaign codenamed Beamglea.

"Threat actors keep finding and using new and novel techniques not just to deliver malware, but to use legitimate infrastructure to store their payloads and data," OX Security said.

"When we think of malware as families of code that steal data directly from the machine they are running on, we can miss other ideas such as infrastructure abuse, using npm and its mirrors as free storage, and persistence – since npm packages can live forever in mirrors even after they are removed from the official stores."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [Malware](https://thehackernews.com/search/label/Malware), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Phishing](https://thehackernews.com/search/label/Phishing), [Social Engineering](https://thehackernews.com/search/label/Social%20Engineering), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stor...