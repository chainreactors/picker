---
title: GitHub, Telegram Bots, and QR Codes Abused in New Wave of Phishing Attacks
url: https://thehackernews.com/2024/10/github-telegram-bots-and-qr-codes.html
source: The Hacker News
date: 2024-10-12
fetch_date: 2025-10-06T18:56:23.397268
---

# GitHub, Telegram Bots, and QR Codes Abused in New Wave of Phishing Attacks

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

# [GitHub, Telegram Bots, and ASCII QR Codes Abused in New Wave of Phishing Attacks](https://thehackernews.com/2024/10/github-telegram-bots-and-qr-codes.html)

**Oct 11, 2024**Ravie LakshmananMalware / Financial Security

[![Phishing Attacks](data:image/png;base64... "Phishing Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqGAFhKOnkwzltNIgfGrMZZnuSNZOXOM6x1N5y6ZGHCCRyVF52VKe3tqOZT3luAmpoqTggBjmOkBUvgJ7mCpip44rDs_YiW9OvqLGfv-eVgDiOEiNtsCgjP-N8UJw12C48QoDSseF3-PZlp8iNniJXycG08s2UV8B6ke47FnEsMjCFhbe6dqVSzfLuiMtj/s790-rw-e365/phishing.png)

A new tax-themed malware campaign targeting insurance and finance sectors has been observed leveraging GitHub links in phishing email messages as a way to bypass security measures and deliver Remcos RAT, indicating that the method is gaining traction among threat actors.

"In this campaign, legitimate repositories such as the open-source tax filing software, UsTaxes, HMRC, and InlandRevenue were used instead of unknown, low-star repositories," Cofense researcher Jacob Malimban [said](https://cofense.com/blog/tax-extension-malware-campaign).

"Using trusted repositories to deliver malware is relatively new compared to threat actors creating their own malicious GitHub repositories. These malicious GitHub links can be associated with any repository that allows comments."

Central to the attack chain is the abuse of GitHub infrastructure for staging the malicious payloads. One variation of the technique, [first disclosed](https://thehackernews.com/2024/03/new-python-based-snake-info-stealer.html) by OALABS Research in March 2024, involves threat actors opening a GitHub issue on well-known repositories and uploading to it a malicious payload, and then closing the issue without saving it.

In doing so, it has been found that the uploaded malware persists even though the issue is never saved, a vector that has become ripe for abuse as it allows attackers to upload any file of their choice and not leave any trace except for the link to the file itself.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The approach has been weaponized to trick users into downloading a Lua-based malware loader that is capable of establishing persistence on infected systems and delivering additional payloads, as [detailed](https://thehackernews.com/2024/10/gamers-tricked-into-downloading-lua.html) by Morphisec this week.

The phishing campaign detected by Cofense employs a similar tactic, the only difference being that it utilizes [GitHub comments](https://docs.github.com/en/rest/guides/working-with-comments) to attach a file (i.e., the malware), after which the comment is deleted. Like in the aforementioned case, the link remains active and is propagated via phishing emails.

[![Phishing Attacks](data:image/png;base64... "Phishing Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLHPQ_p5zj7QrUvTI014bz8qtqyLGP3G8HqsfEGzSjMWY0Z1gdJcff9we_8OmxCagLS3EAEpyF5yYCjbGy-alwudPgxVSykbd64577y7Z_QY-csFZ2AWphLWLs0h3Gd3K8hFkxL_CMnhiDtfdHyXebOd2ri7IU2GSvlwS3PgBw5l1l7Ug3wNglGeB3usBP/s790-rw-e365/phishng.PNG)

"Emails with links to GitHub are effective at bypassing SEG security because GitHub is typically a trusted domain," Malimban said. "GitHub links allow threat actors to directly link to the malware archive in the email without having to use Google redirects, QR codes, or other SEG bypass techniques."

The development comes as Barracuda Networks revealed novel methods adopted by phishers, including [ASCII- and Unicode-based QR codes](https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html) and [blob URLs](https://en.wikipedia.org/wiki/Blob_URI_scheme) as a way to make it harder to block malicious content and evade detection.

"A blob URI (also known as a blob URL or an object URL) is used by browsers to represent binary data or file-like objects (called blobs) that are temporarily held in the browser's memory," security researcher Ashitosh Deshnur [said](https://blog.barracuda.com/2024/10/09/novel-phishing-techniques-ascii-based-qr-codes-blob-uri).

"Blob URIs allow web developers to work with binary data like images, videos, or files directly within the browser, without having to send or retrieve it from an external server."

It also follows new research from ESET that the threat actors behind the [Telekopye](https://thehackernews.com/2023/11/cybercriminals-using-telekopye-telegram.html) Telegram toolkit have expanded their focus beyond online marketplace scams to target accommodation booking platforms such as Booking.com and Airbnb, with a sharp uptick detected in July 2024.

[![Phishing Attacks](data:image/png;base64... "Phishing Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiftOnOsAQ8XRGNPMdFPRaYk6edzBU_n3pVkMFJ_24ZJ59XNm7ASBFZKkSC7dZkoTAtTPO7J28oXIKdg6VgzivtWP05A6Q01PquQmAdM1XAxwHmTbl7Kk-AQSemQv6e8bR22LBtJKy5tt5lOHB_LcN2sdrzqcl7CAgxUERtHeqmCi3-caSxS6iPF5u7Q6Rq/s790-rw-e365/ask.png)

The attacks are characterized by the use of compromised accounts of legitimate hotels and accommodation providers to contact potential targets, claiming purported issues with the booking payment and tricking them into clicking on a bogus link that prompts them to enter their financial information.

"Using their access to these accounts, scammers single out users who recently booked a stay and haven't paid yet – or paid very recently – and contact them via in-platform chat," researchers Jakub Souček and Radek Jizba [said](https://www.welivesecurity.com/en/eset-research/telekopye-hits-new-hunting-ground-hotel-booking-scams/). "Depending on the platform and the Mammoth's settings, this leads to the Mammoth receiving an email or SMS from the booking platform."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This makes the scam much harder to spot, as the information provided is personally relevant to the victims, arrives via the expected communication channel, and the linked...