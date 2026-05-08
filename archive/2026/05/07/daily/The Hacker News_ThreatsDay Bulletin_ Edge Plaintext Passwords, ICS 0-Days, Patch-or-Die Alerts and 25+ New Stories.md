---
title: ThreatsDay Bulletin: Edge Plaintext Passwords, ICS 0-Days, Patch-or-Die Alerts and 25+ New Stories
url: https://thehackernews.com/2026/05/threatsday-bulletin-edge-plaintext.html
source: The Hacker News
date: 2026-05-07
fetch_date: 2026-05-08T04:56:58.876744
---

# ThreatsDay Bulletin: Edge Plaintext Passwords, ICS 0-Days, Patch-or-Die Alerts and 25+ New Stories

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [ThreatsDay Bulletin: Edge Plaintext Passwords, ICS 0-Days, Patch-or-Die Alerts and 25+ New Stories](https://thehackernews.com/2026/05/threatsday-bulletin-edge-plaintext.html)

**Ravie Lakshmanan**May 07, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYNaH2vOiD-OgAVnO0nGCSr8j4nnvHD2n7RieJD2mDMlPev_fKoBafjhvob13LV4pOFhgMuZd6ex8zyQnCM1AyVfl6fuRG9Max2F76Ku9rWbieBvF0AtGlQd0nXlIwHDKvq5H4BJn3hGCRfE86fHs5SL05RywOADNDC9J5lG9DF8goavgxWzAh7a7isNMB/s1700-e365/threatsday-1.jpg)

Bad week.

Turns out the easiest way to get hacked in 2026 is still the same old garbage: shady packages, fake apps, forgotten DNS junk, scam ads, and stolen logins getting dumped into Discord channels like it’s normal. Some of these attack chains don’t even feel sophisticated anymore. More like some tired guy with a Telegram account and too much free time. The worst part is how often this stuff still works.

Meanwhile, AI tools are speeding up exploit hunting, browsers are keeping passwords sitting in memory for “performance reasons,” and even ransomware crews are pushing broken builds into the wild. Everybody’s scrambling to patch faster because attackers are automating faster.

Anyway. ThreatsDay’s rough this week. Let’s get into it.

1. Credential theft campaign

   [New MicroStealer Spotted](https://any.run/malware-trends/microstealer/)

   A new stealer called MicroStealer has been observed targeting education and telecom sectors to steal sensitive data. It was first observed in the wild in December 2025. "It specializes in stealing browser credentials, active session data, screenshots, cryptocurrency wallets, and system information," ANY.RUN [said](https://any.run/malware-trends/microstealer/). "It spreads quickly with low detection rates thanks to a sophisticated multi-stage delivery chain and exfiltrates data via Discord webhooks and attacker-controlled servers."
2. Location data crackdown

   [FTC and Kochava Announce Settlement](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data)

   The Federal Trade Commission (FTC) and location data broker Kochava said they [agreed](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data) to a settlement in which the company and its subsidiary Collective Data Solutions would be blocked from selling, sharing, or disclosing sensitive location data without consumers' explicit consent. The company was [found](https://thehackernews.com/2022/08/ftc-sues-data-broker-over-selling.html) to be illegally obtaining and selling consumers' yearly incomes, mobile device IDs, app usage, and nearly real-time geolocation data within 10 meters without their consent or awareness. While the proposed order does not impose a fine on Kochava, the company is required to establish a data retention schedule that will mandate consumers' data be deleted in a predetermined time frame.
3. Quantum-safe email upgrade

   [Proton Adds PQC Support in Proton Mail](https://proton.me/blog/introducing-post-quantum-encryption)

   Proton has added support for post-quantum encryption as an optional feature in Proton Mail. "Once enabled, Proton Mail can generate and use post-quantum-ready keys for new encrypted emails to protect your personal messages and business communications against today's threats and a future where current public-key cryptography may no longer be enough," the Swiss privacy-focused company [said](https://proton.me/blog/introducing-post-quantum-encryption). "Enabling PQC helps protect new encrypted emails going forward. It does not retroactively re-encrypt the emails already in your mailbox, for now."
4. Supply chain hardening

   [pnpm 11 Rolls Out New Security Measures to Tackle Supply Chain Attacks](https://pnpm.io/blog/releases/11.0)

   [pnpm 11](https://pnpm.io/blog/releases/11.0) has been released with new supply chain protections in place, including defaulting the [minimum release age](https://pnpm.io/settings#minimumreleaseage) to 24 hours to reduce the risk of installing compromised packages and blocking exotic sub-dependencies that resolve from non-standard sources, such as Git repositories or direct tarball URLs. "Newly published package versions are not resolved until they are at least one day old. Teams can opt out by setting minimumReleaseAge: 0, but pnpm's default posture now favors a built-in waiting period before fresh package releases enter installs," Socket [said](https://socket.dev/blog/pnpm-11-adds-new-supply-chain-protection-defaults). With most package compromise campaigns relying on automated installs to expand their reach, the new effort aims to reduce the risk of packages getting installed immediately after publication.
5. AI age verification push

   [Meta Plans to Use AI to Strengthen Underage Enforcement](https://about.fb.com/news/2026/05/ai-age-assurance-teens/)

   Meta said it's deploying artificial intelligence (AI) tools to bolster its underage enforcement measures and remove people under 13 from its services like Facebook and Instagram. Acknowledging that "knowing someone’s age online is a complex, industry-wide challenge," the company said it's using AI to analyze profiles for contextual clues, as well as scan photos and videos for physical cues to assess whether a user is under 13 on Instagram and Facebook. "We want to be clear: this is not facial recognition. Our AI looks at general themes and visual cues, for example, height or bone structure, to estimate someone’s general age; it does not identify the specific person in the image," Meta [said](https://about.fb.com/news/2026/05/ai-age-assurance-teens/). "By combining these visual insights with our analysis of text and interactions, we can significantly increase the number of underage accounts we identify and remove."
6. North Korea-linked c...