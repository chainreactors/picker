---
title: FunkSec Ransomware Decryptor Released Free to Public After Group Goes Dormant
url: https://thehackernews.com/2025/07/funksec-ransomware-decryptor-released.html
source: The Hacker News
date: 2025-07-31
fetch_date: 2025-10-06T23:55:40.886780
---

# FunkSec Ransomware Decryptor Released Free to Public After Group Goes Dormant

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

# [FunkSec Ransomware Decryptor Released Free to Public After Group Goes Dormant](https://thehackernews.com/2025/07/funksec-ransomware-decryptor-released.html)

**Jul 30, 2025**Ravie LakshmananEncryption / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7PmGsgllMAOwglnKzxlkwwg_pjF0l5IDIeFKjdhC9_2lSS6a9TFqT1JFST8hwaNaq32tikFQJtI-pmGx-gwU0KxFqdDmUMjhSKRIRfqwZrdBnxMC3eJlZIfu0pWCva_HdexQ9H6vuocpNQ8FuIsJb4kcnlehBno5ch56BSjzUSEhV5mnQkyjipyQjsg93/s790-rw-e365/ransomware-remove.jpg)

Cybersecurity experts have released a decryptor for a ransomware strain called FunkSec, allowing victims to recover access to their files for free.

"Because the ransomware is now considered dead, we released the decryptor for public download," Gen Digital researcher Ladislav Zezula [said](https://www.gendigital.com/blog/insights/research/funksec-ai).

[FunkSec](https://www.ransomlook.io/groups#Funksec), which emerged towards the end of 2024, has [claimed 172 victims](https://www.ransomware.live/group/funksec), according to data from Ransomware.live. The vast majority of targeted entities are located in the U.S., India, and Brazil, with technology, government, and education being the top three sectors attacked by the group.

An analysis of FunkSec by Check Point earlier this January [found](https://thehackernews.com/2025/01/ai-driven-ransomware-funksec-targets-85.html) signs that the encryptor was developed with assistance from artificial intelligence (AI) tools. The group has not added any new victims to its data leak site since March 18, 2025, suggesting that the group may no longer be active.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's also believed that the group consisted of inexperienced hackers seeking visibility and recognition by uploading leaked datasets associated with previous hacktivism campaigns.

FunkSec was built using Rust, a fast and efficient programming language that's now popular among newer ransomware groups. Other families, like BlackCat and Agenda, also use Rust to help their attacks run quickly and avoid detection. FunkSec relies on the orion-rs library (version 0.17.7) for encryption, using the Chacha20 and Poly1305 algorithms to lock files during its routine.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWfhEcp6NJbA5thQV7twd-8-tinZu9o9jzyPizuPY6JNDVROh03OIIBtQ62OHgXTqYgrjOaH8iPoohlmZRlb0EJIwgfUmksYnqK360QOstQSk3uX5j5Q-vccO11S-6vh-im7gZ7b6O7NeZm6WKNXT2RewgUORa8xc10iKDkPVoZB4JGK9H4h05hapvsKA6/s790-rw-e365/funksec-ransomware.jpg)

"This hash-based method ensures integrity of encryption parameters: the encryption key, n-once, block lengths, and encrypted data itself," Zezula noted. "Files are encrypted per-blocks of 128 bytes, adding 48 bytes of extra metadata to each block, which means that encrypted files are about 37% bigger than the originals."

Gen Digital did not disclose how it was able to develop a decryptor and if it entailed the exploitation of a cryptographic weakness that makes it possible to reverse the encryption process. The decryptor can be [accessed](https://www.nomoreransom.org/en/decryption-tools.html#FunkSec) via the No More Ransom project.

Victims looking to recover their data should first confirm that encrypted files match FunkSec's signature, typically identified by the .funksec extension or unique metadata padding. The No More Ransom portal provides basic usage steps, but administrators are advised to back up affected files before attempting decryption in case of partial recovery or file corruption.

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

[Check Point](https://thehackernews.com/search/label/Check%20Point)[cryptography](https://thehackernews.com/search/label/cryptography)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[encryption](https://thehackernews.com/search/label/encryption)[Malware](https://thehackernews.com/search/label/Malware)[No More Ransom](https://thehackernews.com/search/label/No%20More%20Ransom)[ransomware](https://thehackernews.com/search/label/ransomware)[ransomware decryptor](https://thehackernews.com/search/label/ransomware%20decryptor)[Rust Programming](https://thehackernews.com/search/label/Rust%20Programming)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Steal...