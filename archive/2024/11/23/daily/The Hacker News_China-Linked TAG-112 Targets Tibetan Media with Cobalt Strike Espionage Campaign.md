---
title: China-Linked TAG-112 Targets Tibetan Media with Cobalt Strike Espionage Campaign
url: https://thehackernews.com/2024/11/china-linked-tag-112-targets-tibetan.html
source: The Hacker News
date: 2024-11-23
fetch_date: 2025-10-06T19:26:05.525984
---

# China-Linked TAG-112 Targets Tibetan Media with Cobalt Strike Espionage Campaign

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

# [China-Linked TAG-112 Targets Tibetan Media with Cobalt Strike Espionage Campaign](https://thehackernews.com/2024/11/china-linked-tag-112-targets-tibetan.html)

**Nov 22, 2024**Ravie LakshmananCyber Espionage / Malware

[![Cobalt Strike Espionage](data:image/png;base64... "Cobalt Strike Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzZ-PsIxqTdOZ1c1qKMjWX2BCMvZU3c9E0AiPJLVxPELZ2RJksrg1LpJiPODAFVw8CFReS34GTiOn6eSwl2qoYIVSdBinbEayEwygmTjXeUbXc59kxbftIjc8A-kf1Uo0_ME5okEWjDWtHDhN9UHY6G7R7xCvgIfZ1bQk9oSi07V7E6n-RFl4S7Phu1Dod/s790-rw-e365/hacked.png)

A China-linked nation-state group called TAG-112 compromised Tibetan media and university websites in a new cyber espionage campaign designed to facilitate the delivery of the Cobalt Strike post-exploitation toolkit for follow-on information collection.

"The attackers embedded malicious JavaScript in these sites, which spoofed a TLS certificate error to trick visitors into downloading a disguised security certificate," Recorded Future's Insikt Group [said](https://www.recordedfuture.com/research/china-nexus-tag-112-compromises-tibetan-websites).

"This malware, often used by threat actors for remote access and post-exploitation, highlights a continued cyber-espionage focus on Tibetan entities."

The compromises have been pinned on a state-sponsored threat group called TAG-112, which has been described as a possible sub-group of another cluster tracked as [Evasive Panda](https://thehackernews.com/2024/10/chinese-hackers-use-cloudscout-toolset.html) (aka Bronze Highland, Daggerfly, StormBamboo, and TAG-102) owing to tactical overlaps and their historical targeting of Tibetan entities.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The two Tibetan community websites that were breached by the adversarial collective in late May 2024 were Tibet Post (tibetpost[.]net) and Gyudmed Tantric University (gyudmedtantricuniversity[.]org).

Specifically, it has been found that the compromised websites were manipulated to prompt visitors to the sites to download a malicious executable disguised as a "security certificate" that loaded a Cobalt Strike payload upon execution.

The JavaScript that made this possible is said to have been uploaded to the sites likely using a security vulnerability in their content management system, Joomla.

"The malicious JavaScript is triggered by the window.onload event," Recorded Future said. "It first checks the user's operating system and web browser type; this is likely to filter out non-Windows operating systems, as this function will terminate the script if Windows isn't detected."

The browser information (i.e., Google Chrome or Microsoft Edge) is then sent to a remote server (update.maskrisks[.]com), which sends back a HTML template that's a modified version of the respective browser's [TLS certificate error page](https://www.hostinger.in/tutorials/net-err_cert_common_name_invalid) that's usually displayed when there is a problem with the host's TLS certificate.

The JavaScript, besides displaying the fake security certificate alert, automatically starts the download of a supposed security certificate for the domain \*.dnspod[.]cn, but, in reality, is a legitimate signed executable that sideloads a Cobalt Strike Beacon payload using DLL side-loading.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's worth pointing out at this stage that the website for Tibet Post was separately infiltrated by the Evasive Panda actor in connection with a watering hole and supply chain attack targeting Tibetan users at least since September 2023. The attacks led to the deployment of backdoors known as MgBot and Nightdoor, ESET [revealed](https://thehackernews.com/2024/03/chinese-state-hackers-target-tibetans.html) earlier this March.

Despite this significant tactical intersection, Recorded Future said it's keeping the two intrusion sets disparate owing to the "difference in maturity" between them.

"The activity observed by TAG-112 lacks the sophistication seen by TAG-102," it said. "For example, TAG-112 does not use JavaScript obfuscation and employs Cobalt Strike, while TAG-102 leverages custom malware. TAG-112 is likely a subgroup of TAG-102, working toward the same or similar intelligence requirements."

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

[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[Cobalt Strike](https://thehackernews.com/search/label/Cobalt%20Strike)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Joomla](https://thehackernews.com/search/label/Joomla)[Malware](https://thehackernews.com/search/label/Malware)[Recorded Future](https://thehackernews.com/search/label/Recorded%20Future)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https:/...