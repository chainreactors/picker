---
title: RubyGems, PyPI Hit by Malicious Packages Stealing Credentials, Crypto, Forcing Security Changes
url: https://thehackernews.com/2025/08/rubygems-pypi-hit-by-malicious-packages.html
source: The Hacker News
date: 2025-08-09
fetch_date: 2025-10-07T00:49:53.928097
---

# RubyGems, PyPI Hit by Malicious Packages Stealing Credentials, Crypto, Forcing Security Changes

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

# [RubyGems, PyPI Hit by Malicious Packages Stealing Credentials, Crypto, Forcing Security Changes](https://thehackernews.com/2025/08/rubygems-pypi-hit-by-malicious-packages.html)

**Aug 08, 2025**Ravie LakshmananMalware / Supply Chain Security

[![RubyGems, PyPI Hit by Malicious Packages](data:image/png;base64... "RubyGems, PyPI Hit by Malicious Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3OfHsx30NYjkocvceLlixtRi0p10MyEw8gYN8Vzzpxv5n6GBECHE0B7SpzwHN6w2Mc4ObLebfX-irJLYuutHNVomQdjxVs8SSGQJ1H1JRWFyRKBUiCCT3zsISxiir-0PGzFQ3l81PCsq8GTyXVXRFqZcm3icMt_H_pgWl4wDS9ncf0XRSoAm3j57XBv_o/s790-rw-e365/malware-code.jpg)

A fresh set of 60 malicious packages has been uncovered targeting the RubyGems ecosystem by posing as seemingly innocuous automation tools for social media, blogging, or messaging services to steal credentials from unsuspecting users and likely resell them on dark web forums like Russian Market.

The activity is assessed to be active since at least March 2023, according to the software supply chain security company Socket. Cumulatively, the gems have been downloaded more than 275,000 times.

That said, it bears noting that the figure may not accurately represent the actual number of compromised systems, as not every download results in execution, and it's possible several of these gems have been downloaded to a single machine.

"Since at least March 2023, a threat actor using the aliases zon, nowon, kwonsoonje, and soonje has published 60 malicious gems posing as automation tools for Instagram, Twitter/X, TikTok, WordPress, Telegram, Kakao, and Naver," security researcher Kirill Boychenko [said](https://socket.dev/blog/60-malicious-ruby-gems-used-in-targeted-credential-theft-campaign).

While the identified gems offered the promised functionality, such as bulk posting or engagement, they also harbored covert functionality to exfiltrate usernames and passwords to an external server under the threat actor's control by displaying a simple graphical user interface to enter users' credentials.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the gems, such as njongto\_duo and jongmogtolon, are notable for focusing on financial discussion platforms, with the libraries marketed as tools to flood investment-related forums with ticker mentions, stock narratives, and synthetic engagement to amplify visibility and manipulate public perception.

The servers that are used to receive the captured information include programzon[.]com, appspace[.]kr, and marketingduo[.]co[.]kr. These domains have been found to advertise bulk messaging, phone number scraping, and automated social media tools.

Victims of the campaign are likely to be grey-hat marketers who rely on such tools to run spam, search engine optimization (SEO), and engagement campaigns that artificially boost engagement.

"Each gem functions as a Windows-targeting infostealer, primarily (but not exclusively) aimed at South Korean users, as evidenced by Korean-language UIs and exfiltration to .kr domains," Socket said. "The campaign evolved across multiple aliases and infrastructure waves, suggesting a mature and persistent operation."

"By embedding credential theft functionality within gems marketed to automation-focused grey-hat users, the threat actor covertly captures sensitive data while blending into activity that appears legitimate."

The development comes as GitLab detected multiple typosquatting packages on the Python Package Index (PyPI) that are designed to steal cryptocurrency from Bittensor wallets by hijacking the [legitimate staking functions](https://docs.learnbittensor.org/staking-and-delegation/delegation/). The names of the Python libraries, which mimic bittensor and bittensor-cli, are below -

* bitensor (versions 9.9.4 and 9.9.5)
* bittenso-cli (version 9.9.4)
* qbittensor (version 9.9.4)
* bittenso (version 9.9.5)

"The attackers appear to have specifically targeted staking operations for calculated reasons," GitLab's Vulnerability Research team [said](https://about.gitlab.com/blog/gitlab-uncovers-bittensor-theft-campaign-via-pypi/). "By hiding malicious code within legitimate-looking staking functionality, the attackers exploited both the technical requirements and user psychology of routine blockchain operations."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure also follows new restrictions imposed by PyPI maintainers to secure Python package installers and inspectors from confusion attacks arising from ZIP parser implementations.

Put differently, PyPI said it will reject Python packages "wheels" (which are nothing but ZIP archives) that attempt to exploit ZIP confusion attacks and smuggle malicious payloads past manual reviews and automated detection tools.

"This has been done in response to the discovery that the popular installer uv has a different extraction behavior to many Python-based installers that use the ZIP parser implementation provided by the zipfile standard library module," the Python Software Foundation's (PSF) Seth Michael Larson [said](https://blog.pypi.org/posts/2025-08-07-wheel-archive-confusion-attacks/#wheels-are-zips-and-zips-are-complicated).

PyPI credited Caleb Brown from the Google Open Source Security Team and Tim Hatch from Netflix for reporting the issue. It also said it will warn users when they publish wheels whose ZIP contents don't match the included RECORD metadata file.

"After 6 months of warnings, on February 1st, 2026, PyPI will begin rejecting newly uploaded wheels whose ZIP contents don't match the included RECORD metadata file," Larsen said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_s...