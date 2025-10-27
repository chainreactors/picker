---
title: New Banshee Stealer Variant Bypasses Antivirus with Apple’s XProtect-Inspired Encryption
url: https://thehackernews.com/2025/01/new-banshee-stealer-variant-bypasses.html
source: The Hacker News
date: 2025-01-10
fetch_date: 2025-10-06T20:12:42.209142
---

# New Banshee Stealer Variant Bypasses Antivirus with Apple’s XProtect-Inspired Encryption

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

# [New Banshee Stealer Variant Bypasses Antivirus with Apple's XProtect-Inspired Encryption](https://thehackernews.com/2025/01/new-banshee-stealer-variant-bypasses.html)

**Jan 09, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWGvqxzCQlUURalzkgvCQTDM_C93hK7vnqs7FO_KTTcXmZ5XgvsROO9PKuxaUP8oy7lh4WlTpsUdZv5YSvTdKGI0-6nGY_3g-Lbbotaxm61u7grQAuB7SvFtwpGFJDxBVo54ggsgMdgMMQ-nwoSDvJOXHoV-9SRPsMSeREDoKLBJcwlBA7rH2xHi-WK5Vn/s790-rw-e365/macos.png)

Cybersecurity researchers have uncovered a new, stealthier version of a macOS-focused information-stealing malware called **Banshee Stealer**.

"Once thought dormant after its source code leak in late 2024, this new iteration introduces advanced string encryption inspired by Apple's XProtect," Check Point Research [said](https://blog.checkpoint.com/research/cracking-the-code-how-banshee-stealer-targets-macos-users/) in a new analysis shared with The Hacker News. "This development allows it to bypass antivirus systems, posing a significant risk to over 100 million macOS users globally."

The cybersecurity company said it detected the new version in late September 2024, with the malware distributed using phishing websites and fake GitHub repositories under the guise of popular software such as Google Chrome, TradingView, Zegent, Parallels, Solara, CryptoNews, MediaKIT, and Telegram.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Banshee Stealer was [first documented](https://thehackernews.com/2024/08/new-banshee-stealer-targets-100-browser.html) in August 2024 by Elastic Security Labs. Offered under a malware-as-a-service (MaaS) model to other cybercriminals for $3,000 a month, it's capable of harvesting data from web browsers, cryptocurrency wallets, and files matching specific extensions.

The malware operation [suffered a setback](https://thehackernews.com/2024/12/hackers-using-fake-video-conferencing.html) in late November 2024 when its source code leaked online, prompting it to shut down their operations. However, Check Point said it has identified multiple campaigns still distributing the malware through phishing websites, although it's currently not known if they are carried out by previous customers.

These campaigns target macOS users with Banshee while simultaneously targeting Windows users with another well-known stealer malware Lumma Stealer, suggesting that the cybercriminals are looking to compromise as many systems as possible.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1mL-m4RyzPeovd7bT8NgqBNkG_SjYD4RPB8QdgrooYQXAa7yQnznDEE8Mc_PKIXvgaMh5aHsZa0Bx-9disF2YUoifsW0mxYOah9IuanAo7aIJucc5NYQ6FYFu7N4AbbDlBKn63cuQjQxmP_lhbUQ-uAtyc_S7OUZvP4VvdLbXzE_ZIKjkveIXfd_SuZVl/s790-rw-e365/cp.png)

The new variant is notable for removing a Russian language check used to prevent infections of Macs that had set Russian as the default system language. Dropping the feature alludes to the possibility that the threat actors are looking to cast a wider net of potential targets.

Another crucial update is the use of a string encryption algorithm from Apple's XProtect antivirus engine to obfuscate the plaintext strings used in the original version of Banshee Stealer. This had the desired effect of lowering detection by antivirus engines for over two months.

"Modern malware campaigns are exploiting common human vulnerabilities, not just platform-specific flaws," Eli Smadja, security research group manager at Check Point Research, said in a statement shared with The Hacker News. "MacOS, like any other OS, is exposed to these evolving threats, especially as cybercriminals employ advanced techniques like social engineering and fake software updates."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as unsolicited messages on Discord are being used to propagate various stealer malware families such as Nova Stealer, Ageo Stealer, and Hexon Stealer under the pretext of testing out a new video game.

"One of the main interests for the stealers seem to be Discord credentials which can be used to expand the network of compromised accounts," Malwarebytes [said](https://www.malwarebytes.com/blog/news/2025/01/can-you-try-a-game-i-made-fake-game-sites-lead-to-information-stealers). "This also helps them because some of the stolen information includes friends accounts of the victims."

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

[Antivirus](https://thehackernews.com/search/label/Antivirus)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[encryption](https://thehackernews.com/search/label/encryption)[MacOS](https://thehackernews.com/search/label/MacOS)[Malware](https://thehackernews.com/search/label/Malware)[Phishing](https://thehackernews.com/search/label/Phishing)[social engineering](https://thehackernews.com/search/label/social%20engineering)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](dat...