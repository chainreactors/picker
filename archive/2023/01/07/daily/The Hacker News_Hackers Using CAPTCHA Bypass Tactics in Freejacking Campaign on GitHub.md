---
title: Hackers Using CAPTCHA Bypass Tactics in Freejacking Campaign on GitHub
url: https://thehackernews.com/2023/01/hackers-using-captcha-bypass-tactics-in.html
source: The Hacker News
date: 2023-01-07
fetch_date: 2025-10-04T03:17:46.729644
---

# Hackers Using CAPTCHA Bypass Tactics in Freejacking Campaign on GitHub

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

# [Hackers Using CAPTCHA Bypass Tactics in Freejacking Campaign on GitHub](https://thehackernews.com/2023/01/hackers-using-captcha-bypass-tactics-in.html)

**Jan 06, 2023**Ravie LakshmananCryptocurrency / GitHub

[![Freejacking Campaign](data:image/png;base64... "Freejacking Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbMpcB6011zvS07BeTgRd_Wz7rnTGnQBlCme-j3L4aBmDDNjbD-XQmd6JzgOHjkMZeMTso220Ef1FI4WeY7ftly24pZrjToDt6cZndt7NTNCO50OEWIriLm31AmdWJ83uwOFoBudANig2m9LCxPnjf-hOhrJqjmXS3dNjUuQhwUwBNDbiWxcBF3ywh/s790-rw-e365/captcha.png)

A South Africa-based threat actor known as Automated Libra has been observed employing CAPTCHA bypass techniques to create GitHub accounts in a programmatic fashion as part of a freejacking campaign dubbed PURPLEURCHIN.

The group "primarily targets cloud platforms offering limited-time trials of cloud resources in order to perform their crypto mining operations," Palo Alto Networks Unit 42 researchers William Gamazo and Nathaniel Quist [said](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/).

PURPLEURCHIN first came to light in October 2022 when Sysdig [disclosed](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html) that the adversary created as many as 30 GitHub accounts, 2,000 Heroku accounts, and 900 Buddy accounts to scale its operation.

Now according to Unit 42, the cloud threat actor group created three to five GitHub accounts every minute at the height of its activity in November 2022, totally setting up over 130,000 bogus accounts across Heroku, Togglebox, and GitHub.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

More than 22,000 GitHub accounts are estimated to have been created between September and November 2022: three in September, 1,652 in October, and 20,725 in November. A total of 100,723 unique Heroku accounts have also been identified.

The cybersecurity company also termed the abuse of cloud resources as a "play and run" tactic designed to avoid paying the platform vendor's bill by making use of falsified or stolen credit cards to create premium accounts.

Its analysis of 250GB of data puts the earliest sign of the crypto campaign at least nearly 3.5 years ago in August 2019, in addition to uncovering the use of more than 40 wallets and seven different cryptocurrencies.

[![Freejacking Campaign](data:image/png;base64... "Freejacking Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Uq9y0IMrPZAsY0owUOWekC1Qa2BHbEaj0VmvUP87M_7Nm2sGcdZ2x-lbsqp7gcYr7yKzufg3bviFwijjOHIVgVirpUYQKktMZTLE9iDTMZnMpnTY36KkZZy1xCd4XyJ2lbKAsYMZpd-sP2XsgwNCwTRb1IC1Y3lR44RcqdN0OLJXqSuv7bOQSV4I/s790-rw-e365/captcha.png)

The core idea that undergirds PURPLEURCHIN is the exploitation of computational resources allocated to free and premium accounts on cloud services in order to reap monetary profits on a massive scale before losing access for non-payment of dues.

Besides automating the account creation process by leveraging legitimate tools like [xdotool](https://www.semicomplete.com/projects/xdotool/) and [ImageMagick](https://imagemagick.org/), the threat actor has also been found to take advantage of weakness within the CAPTCHA check on GitHub to further its illicit objectives.

[![Freejacking Campaign](data:image/png;base64... "Freejacking Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYZIlP3QAG_s86Zy1pBuyvjDP2Eie5T4xu1_3y5AJkBnUrXSEpNx7TMyj0LImE30LDz4y4_hiZlqn9OgbwgrwjOilTw_1Dnpy48YUx5p41OMmo5u9cDqrcs5ptPD3ex3ARuuonPreV6vG4iWivGChDZY2diLwarulYW2sve1QGczCgKiSTnvPGE46d/s790-rw-e365/github.png)

This is accomplished by using ImageMagick's [convert command](https://imagemagick.org/script/convert.php) to transform the CAPTCHA images to their RGB complements, followed by using the [identify command](https://imagemagick.org/script/identify.php) to extract the skewness of the [red channel](https://en.wikipedia.org/wiki/Channel_%28digital_image%29#RGB_images) and selecting the smallest value.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Once the account creation is successful, Automated Libra proceeds to create a GitHub repository and [deploys workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) that make it possible to launch external Bash scripts and containers for initiating the crypto mining functions.

The findings illustrate how the freejacking campaign can be weaponized to maximize returns by increasing the number of accounts that can be created per minute on these platforms.

"It is important to note that Automated Libra designs their infrastructure to make the most use out of CD/CI tools," the researchers concluded.

"This is getting easier to achieve over time, as the traditional VSPs are diversifying their service portfolios to include cloud-related services. The availability of these cloud-related services makes it easier for threat actors, because they don't have to maintain infrastructure to deploy their applications."

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

[CAPTCHA bypass](https://thehackernews.com/search/label/CAPTCHA%20bypass)[Freejacking](https://theh...