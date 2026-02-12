---
title: First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials
url: https://thehackernews.com/2026/02/first-malicious-outlook-add-in-found.html
source: The Hacker News
date: 2026-02-11
fetch_date: 2026-02-12T04:23:18.173878
---

# First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials](https://thehackernews.com/2026/02/first-malicious-outlook-add-in-found.html)

**Ravie Lakshmanan**Feb 11, 2026Cloud Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGH5OFCdEH8WLDQvMuU6qAbaI73kVMtx4uASqujZ12UAb3Q-yJX3ZsFCpc1uJuUE4ah_z24WgRv_1JhOem_ISHdoYtPzZPy6o5HwRuoBGjThyru3WAtrcOqyA9hDvSNgSKIgaYUTdIOUJHL7HCRUEZgt9Z8fP6F8oINDt4LkeziTnTW6cx_Qw_DJ2FLMmo/s1700-e365/outlook.jpg)

Cybersecurity researchers have discovered what they said is the first known malicious Microsoft Outlook add-in detected in the wild.

In this unusual supply chain attack [detailed](https://www.koi.ai/blog/agreetosteal-the-first-malicious-outlook-add-in-leads-to-4-000-stolen-credentials) by Koi Security, an unknown attacker claimed the domain associated with a now-abandoned legitimate add-in to serve a fake Microsoft login page, stealing over 4,000 credentials in the process. The activity has been codenamed **AgreeToSteal** by the cybersecurity company.

The Outlook add-in in question is [AgreeTo](https://marketplace.microsoft.com/en-us/product/WA200004949), which is advertised by its developer as a way for users to connect different calendars in a single place and share their availability through email. The add-in was last updated in December 2022.

Idan Dardikman, co-founder and CTO of Koi, told The Hacker News that the incident represents a broadening of supply chain attack vectors.

"This is the same class of attack we've seen in browser extensions, npm packages, and IDE plugins: a trusted distribution channel where the content can change after approval," Dardikman said. "What makes Office add-ins particularly concerning is the combination of factors: they run inside Outlook, where users handle their most sensitive communications, they can request permissions to read and modify emails, and they're distributed through [Microsoft's own store](https://support.microsoft.com/en-us/office/use-add-ins-in-outlook-1ee261f9-49bf-4ba6-b3e2-2ba7bcab64c8), which carries implicit trust."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"The AgreeTo case adds another dimension: the original developer did nothing wrong. They built a legitimate product and moved on. The attack exploited the gap between when a developer abandons a project and when the platform notices. Every marketplace that hosts remote dynamic dependencies is susceptible to this."

At its core, the attack exploits how Office add-ins work and the lack of periodic content monitoring of add-ins published to the Marketplace. According to Microsoft's documentation, add-in developers are [required](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/submit-to-appsource-via-partner-center) to create an account and submit their solution to the Partner Center, following which it is subjected to an approval process.

What's more, Office add-ins make use of a manifest file that declares a URL, the contents of which are fetched and served in real-time from the developer's server every time it's opened within an iframe element inside the application. However, there is nothing stopping a bad actor from taking control of an expired domain.

In the case of AgreeTo, the manifest file pointed to a URL hosted on Vercel ("outlook-one.vercel[.]app"), which became claimable after the developer's Vercel deployment was deleted due to it essentially becoming abandonware sometime around 2023. The infrastructure is still live as of writing.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiW7COSto5yIlW-_idS-0u8sEczFHtj0uPM2Y6cYI01ikwmkfBRmiKRzZ5F1QXZ7YDhKObF_P6b4XZdZQH8PUsA36g2aXVh-GzPMPP6SWuPBO50nb7Nr9RKri3nvQICTjKBJVdrdi-Pevqd6l8sMVXf75az5ClCoTeziXsZ1e3e93ZwWk5dp2RG2qRD2gpz/s1700-e365/outlook.png)

The attacker took advantage of this behavior to stage a phishing kit on that URL that displayed a fake Microsoft sign-in page, capturing entered passwords, exfiltrating the details via the Telegram Bot API, and eventually redirecting the victim to the actual Microsoft login page.

But Koi warns that the incident could have been worse. Given that the add-in is configured with "[ReadWriteItem](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/understanding-outlook-add-in-permissions)" permissions – which allows it to read and modify the user's emails – a threat actor could have abused this blind spot to deploy JavaScript that can covertly siphon a victim's mailbox contents.

The findings once again bring to fore the need for rescanning packaged and tools uploaded to marketplaces and repositories to flag malicious/suspicious activity.

Dardikman said while Microsoft reviews the manifest during the initial submission phase, there is no control over the actual content that is retrieved live from the developer's server every time the add-in is opened, once it's signed and approved. As a result, the absence of continued monitoring of what the URL serves opens the door to unintended security risks.

"Office add-ins are fundamentally different from traditional software," Dardikman added. "They don't ship a static code bundle. The manifest simply declares a URL, and whatever that URL serves at any given moment is what runs inside Outlook. In AgreeTo's case, Microsoft signed the manifest in December 2022, pointing to outlook-one.vercel.app. That same URL is now serving a phishing kit, and the add-in is still listed in the store."

To counter the security issues posed by the threat, Koi recommends a number of steps that Microsoft can take -

* Trigger a re-review when an add-in's URL starts returning different content from what it was during review.
* Verify ownership of the domain to ensure that it's managed by the add-in developer, and flag add-ins where the domain infrastructure has changed hands.
* Implement a mechanism for delisting or flagging add-ins that have not been updated beyond a ce...