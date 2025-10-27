---
title: WooCommerce Users Targeted by Fake Patch Phishing Campaign Deploying Site Backdoors
url: https://thehackernews.com/2025/04/woocommerce-users-targeted-by-fake.html
source: The Hacker News
date: 2025-04-29
fetch_date: 2025-10-06T22:08:58.558988
---

# WooCommerce Users Targeted by Fake Patch Phishing Campaign Deploying Site Backdoors

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

# [WooCommerce Users Targeted by Fake Patch Phishing Campaign Deploying Site Backdoors](https://thehackernews.com/2025/04/woocommerce-users-targeted-by-fake.html)

**Apr 28, 2025**Ravie LakshmananWebsite Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm3BCDBtoijyuhiobLlc-kjzrqQmLcRtfwMgLi4liR8Af85SB-fQidNC8KhL6yoYns8PRkXs9XSQOby752lb2CUEJLlChJhDxkrarPc4KeLHnv29FBTtIQlxd6dzMUwhkOl2RbAIvHDvoTgaBqNSofeKFmTXI-IDrahS4aC6oQr9oL3rUHrXrK4oNoArLg/s790-rw-e365/wooo.jpg)

Cybersecurity researchers are warning about a large-scale phishing campaign targeting WooCommerce users with a fake security alert urging them to download a "critical patch" but deploy a backdoor instead.

WordPress security company Patchstack described the activity as sophisticated and a variant of another campaign [observed](https://patchstack.com/articles/fake-cve-phishing-campaign-tricks-wordpress-users-to-install-malware/) in December 2023 that employed a fake CVE ploy to breach sites running the popular content management system (CMS).

Given the similarities in the phishing email lures, the bogus web pages, and the identical methods employed to conceal the malware, it's believed the latest attack wave is either the work of the same threat actor or it's a new cluster closely mimicking the earlier one.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"They claim the targeted websites are impacted by a (non-existent) 'Unauthenticated Administrative Access' vulnerability, and they urge you to visit their phishing website, which uses an [IDN homograph attack](https://thehackernews.com/2020/08/magecart-homograph-phishing.html) to disguise itself as the official WooCommerce website," security researcher Chazz Wolcott [said](https://patchstack.com/articles/fake-security-vulnerability-phishing-campaign-targets-woocommerce-users/).

Recipients of the phishing email are urged to click on a "Download Patch" link in order to download and install the supposed security fix. However, doing so redirects them to a spoofed WooCommerce Marketplace page hosted on the domain "woocommėrce[.]com" (note the use of "ė" in place of "e") from where a ZIP archive ("authbypass-update-31297-id.zip") can be downloaded.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizDy5bplogFcIdpTF2iJvl4G0MJf5BzU0ULGfUCtrtHELImBSrajhZ7BunZKRkVAkktxOXZSWjHLsYJ0oVpcm9sIN7yW0tVFqQMVnKHLDGGS3iHxE5rGmFx6Po19ToTKVMAj08ctdCkhheEonvDm3oRYbd82hWhFX4A_vcXJas5hyAQPfFI0VdCOi0Aga7/s790-rw-e365/woo.png)

Victims are then prompted to install the patch as they would install any regular WordPress plugin, effectively unleashing the following series of malicious actions -

* Create a new administrator-level user with an obfuscated username and a randomized password after setting up a randomly named cron job that runs every minute
* Send an HTTP GET request to an external server ("woocommerce-services[.]com/wpapi") with information about the username and password, along with the infected website's URL
* Send an HTTP GET request to download a next-stage obfuscated payload from a second server ("woocommerce-help[.]com/activate" or "woocommerce-api[.]com/activate")
* Decode the payload to extract multiple web shells like P.A.S.-Fork, p0wny, and WSO
* Hide the malicious plugin from the list of plugin and conceal the created administrator account

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A net result of the campaign is that it allows the attackers remote control over the websites, allowing them to inject spam or sketchy ads, redirect site visitors to fraudulent sites, enlist the breached server into a botnet for carrying out DDoS attacks, and even encrypt the server resources as part of an extortion scheme.

Users are advised to scan their instances for suspicious plugins or administrator accounts, and ensure that the software is up-to-date.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Phishing](https://thehackernews.com/search/label/Phishing)[Web Shell](https://thehackernews.com/search/label/Web%20Shell)[website security](https://thehackernews.com/search/label/website%20security)[WooCommerce](https://thehackernews.com/search/label/WooCommerce)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secur...