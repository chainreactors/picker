---
title: New Phishing Kit Xiū gǒu Targets Users Across Five Countries With 2,000 Fake Sites
url: https://thehackernews.com/2024/11/new-phishing-kit-xiu-gou-targets-users.html
source: The Hacker News
date: 2024-11-02
fetch_date: 2025-10-06T19:21:07.121981
---

# New Phishing Kit Xiū gǒu Targets Users Across Five Countries With 2,000 Fake Sites

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

# [New Phishing Kit Xiū gǒu Targets Users Across Five Countries With 2,000 Fake Sites](https://thehackernews.com/2024/11/new-phishing-kit-xiu-gou-targets-users.html)

**Nov 01, 2024**Ravie LakshmananThreat Intelligence / Malware

[![New Phishing Kit Xiū gǒu](data:image/png;base64... "New Phishing Kit Xiū gǒu")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4VIeiIy8Ex1PemCc5a6Ky_29rRUkyHF_PYhQ8RmzgoHNqdLjPxQ5AEe8cy0TVxt6xaBV58moUz41dQO_tEn-sXxsGnXuuEsPX-aR8ZVanhyJR45hAJfmRuncpcVhu5pGN6YSD9XjXuu4k426Ot3w3AARibnKvGV60XIgGCeBU3bUrAwrzRB5wj7UY6SQg/s790-rw-e365/phishing.png)

Cybersecurity researchers have disclosed a new phishing kit that has been put to use in campaigns targeting Australia, Japan, Spain, the U.K., and the U.S. since at least September 2024.

Netcraft said more than 2,000 phishing websites have been identified the kit, known as Xiū gǒu, with the offering used in attacks aimed at a variety of verticals, such as public sectors, postal, digital services, and banking services.

"Threat actors using the kit to deploy phishing websites often rely on Cloudflare's anti-bot and hosting obfuscation capabilities to prevent detection," Netcraft [said](https://www.netcraft.com/blog/doggo-threat-actor-analysis/) in a report published Thursday.

Some aspects of the phishing kit were documented by security researchers [Will Thomas](https://gist.github.com/BushidoUK/3cb208dc4401815d500cfe022631c343) (@ BushidoToken) and [Fox\_threatintel](https://x.com/banthisguy9349/status/1837130065760440420) (@banthisguy9349) in September 2024.

Phishing kits like Xiū gǒu [pose a risk](https://thehackernews.com/2024/10/microsoft-detects-growing-use-of-file.html) because they could lower the barrier of entry for less skilled hackers, potentially leading to an increase in malicious campaigns that could lead to theft of sensitive information.

Xiū gǒu, which is the creation of a Chinese-speaking threat actor, provides users with an admin panel and is developed using technologies like Golang and Vue.js. The kit is also designed to exfiltrate credentials and other information from the fake phishing pages hosted on the ".top" top-level domain via Telegram.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The phishing attacks are propagated via Rich Communications Services (RCS) messages rather than SMS, warning recipients of purported parking penalties and failed package deliveries. The messages also instruct them to click on a link that's shortened using a URL shortener service to pay the fine or update the delivery address.

"The scams typically manipulate victims into providing their personal details and making payments, for example, to release a parcel or fulfill a fine," Netcraft said.

RCS, which is primarily available via Apple Messages (starting with [iOS 18](https://support.apple.com/en-us/104972)) and [Google Messages](https://support.google.com/messages/answer/9487020?hl=en#zippy=%2Crcs-chats-with-iphone-users-dont-have-end-to-end-encryption) for Android, offers users an upgraded messaging experience with support for file-sharing, typing indicators, and [optional support](https://support.google.com/messages/answer/10252671?hl=en) for end-to-end encryption (E2EE).

In a blog post late last month, the search giant [detailed](https://security.googleblog.com/2024/10/5-new-protections-on-google-messages.html) the new protections it's incorporating into the Messages app to combat phishing scams, including rolling out enhanced scam detection using on-device machine learning models to specifically filter out fraudulent messages related to package deliveries and job opportunities.

Google also said it's piloting security warnings when users in India, Thailand, Malaysia, and Singapore receive text messages from unknown senders with potentially dangerous links. The new protections, which are expected to be expanded globally later this year, also block messages with links from suspicious senders.

Lastly, the search major is adding the option to "automatically hide messages from international senders who are not existing contacts" by moving them to the "Spam & blocked" folder. The feature is scheduled to be first enabled as a pilot in Singapore before the end of 2024.

[![New Phishing Kit Xiū gǒu](data:image/png;base64... "New Phishing Kit Xiū gǒu")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiidklGd5Fn2g-xmh7oJwvro87_ychd0nSKxmsk3h6_Y9TWdX1_Dl80VYPIBLcb2GJfmWAb9awAMilaWnCzhvplgrVwSu0wMdVuyz15WtMMwB8rLK8iPRBFqYxzD9iNawW1emmI_4HZZ-OY15nR3ukYpDjBygGLDGwiGOFILRcxh7EkWpaLK8KqxrM0VFme/s790-rw-e365/malware.jpeg)

The disclosure comes as Cisco Talos revealed that Facebook business and advertising account users in Taiwan are being targeted by an unknown threat actor as part of a phishing campaign designed to deliver stealer malware such as Lumma or Rhadamanthys.

The lure messages come embedded with a link that, when clicked, takes the victim to a Dropbox or Google Appspot domain, triggering the download of a RAR archive packing a fake PDF executable, which serves as a conduit to drop the stealer malware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The decoy email and fake PDF filenames are designed to impersonate a company's legal department, attempting to lure the victim into downloading and executing malware," Talos researcher Joey Chen [said](https://blog.talosintelligence.com/threat-actors-use-copyright-infringement-phishing-lure-to-deploy-infostealers/), adding the activity has been ongoing since July 2024.

"The emails demand the removal of the infringing content within 24 hours, cessation of further use without written permission, and warn of potential legal action and compensation claims for non-compliance."

Phishing campaigns have also been observed impersonating OpenAI targeting businesses worldwide, instructing them to immediately update their payment information by clicking on an obfuscated hyperlink.

"This attack was s...