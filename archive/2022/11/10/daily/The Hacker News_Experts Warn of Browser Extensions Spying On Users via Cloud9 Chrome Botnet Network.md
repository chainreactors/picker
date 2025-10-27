---
title: Experts Warn of Browser Extensions Spying On Users via Cloud9 Chrome Botnet Network
url: https://thehackernews.com/2022/11/experts-warn-of-browser-extensions.html
source: The Hacker News
date: 2022-11-10
fetch_date: 2025-10-03T22:19:18.471685
---

# Experts Warn of Browser Extensions Spying On Users via Cloud9 Chrome Botnet Network

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

# [Experts Warn of Browser Extensions Spying On Users via Cloud9 Chrome Botnet Network](https://thehackernews.com/2022/11/experts-warn-of-browser-extensions.html)

**Nov 09, 2022**Ravie Lakshmanan

[![Chromium-based web browsers](data:image/png;base64... "Chromium-based web browsers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvbCjNnYeHS8MYJmhXmgowPqu5E1oCuuaQ0-QyEIu_rel2SqB_27pFL25wtriF0AlRCGAOBej0gCj4qNRrbQrUbMznuqzil0Q7HALOhEk1vylD4Bbw-8c7IwVWl3t0b2UVGUsEBzdHebRmv_AOVpNXEbSYrvTvfewUWpAX6ZQOd9bpoPEpnSt6hde3/s790-rw-e365/flash.jpg)

The Keksec threat actor has been linked to a previously undocumented malware strain, which has been observed in the wild masquerading as an extension for Chromium-based web browsers to enslave compromised machines into a botnet.

Called **Cloud9** by security firm Zimperium, the malicious browser add-on comes with a wide range of features that enables it to siphon cookies, log keystrokes, inject arbitrary JavaScript code, mine crypto, and even enlist the host to carry out DDoS attacks.

The extension "not only steals the information available during the browser session but can also install malware on a user's device and subsequently assume control of the entire device," Zimperium researcher Nipun Gupta [said](https://www.zimperium.com/blog/the-case-of-cloud9-chrome-botnet/) in a new report.

The JavaScript botnet isn't distributed via Chrome Web Store or Microsoft Edge Add-ons, but rather through fake executables and rogue websites disguised as Adobe Flash Player updates.

Once installed, the extension is designed to inject a JavaScript file called "campaign.js" on all pages, meaning the malware could also operate as a standalone piece of code on any website, legitimate or otherwise, potentially leading to watering hole attacks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The JavaScript code takes responsibility for cryptojacking operations, abusing the victim's computing resources to illicitly mine cryptocurrencies, as well as inject a second script named "cthulhu.js."

This attack chain, in turn, exploits flaws in web browsers such as Mozilla Firefox ([CVE-2019-11708](https://nvd.nist.gov/vuln/detail/CVE-2019-11708), [CVE-2019-9810](https://nvd.nist.gov/vuln/detail/cve-2019-9810)), Internet Explorer ([CVE-2014-6332](https://nvd.nist.gov/vuln/detail/CVE-2014-6332), [CVE-2016-0189](https://nvd.nist.gov/vuln/detail/CVE-2016-0189)), and Edge ([CVE-2016-7200](https://nvd.nist.gov/vuln/detail/CVE-2016-7200)) to escape the browser sandbox and deploy malware on the system.

The script further acts as a keylogger and a conduit for launching additional commands received from a remote server, allowing it to steal clipboard data, browser cookies, and mount [layer 7 DDoS attacks](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/) against any domain.

Zimperium attributed the malware to a threat actor tracked as [Keksec](https://thehackernews.com/2022/04/new-enemybot-ddos-botnet-borrows.html) (aka Kek Security, Necro, and FreakOut), which has a history of developing a wide range of botnet malware, including [EnemyBot](https://thehackernews.com/2022/05/enemybot-linux-botnet-now-exploits-web.html), for crypto mining and DDoS operations.

The connection to Keksec comes from overlaps in the domains that were previously identified as used by the malware group.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The fact that Cloud9 is JavaScript-based and is offered either for free or a small fee on hacker forums makes it possible for less-skilled cybercriminals to get easy access to low-cost options for launching attacks targeting different browsers and operating systems.

The disclosure comes over three months after Zimperium discovered a malicious browser add-on dubbed [ABCsoup](https://thehackernews.com/2022/07/experts-uncover-350-browser-extension.html) that posed as a Google Translate tool to strike Russian users of Google Chrome, Opera, and Mozilla Firefox browsers.

"Users should be trained on the risks associated with browser extensions outside of official repositories, and enterprises should consider what security controls they have in place for such risks," Gupta said.

***Update:*** Following the publication of the story, a Google spokesperson shared the below statement with The Hacker News -

"We always recommend users update to the latest version of Google Chrome to ensure they have the most up-to-date security protections. Users can also stay better protected from malicious executables and websites by enabling [Enhanced Protection](https://support.google.com/chrome/answer/9890866?hl=en) in the privacy and security settings in Chrome. Enhanced Protection automatically warns you about potentially risky sites and downloads and inspects the safety of your downloads and warns you when a file may be dangerous."

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

[Browser Extension](https://thehackernews.com/search/label/Browser%20Extension)[Chromium](https://thehackernews.com/search/label/Chromium)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Zimperium](https...