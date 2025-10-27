---
title: Phishing-as-a-Service "Rockstar 2FA" Targets Microsoft 365 Users with AiTM Attacks
url: https://thehackernews.com/2024/11/phishing-as-service-rockstar-2fa.html
source: The Hacker News
date: 2024-11-30
fetch_date: 2025-10-06T19:19:12.069281
---

# Phishing-as-a-Service "Rockstar 2FA" Targets Microsoft 365 Users with AiTM Attacks

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

# [Phishing-as-a-Service "Rockstar 2FA" Targets Microsoft 365 Users with AiTM Attacks](https://thehackernews.com/2024/11/phishing-as-service-rockstar-2fa.html)

**Nov 29, 2024**Ravie LakshmananCybercrime / Cloud Security

[![Phishing-as-a-Service](data:image/png;base64... "Phishing-as-a-Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxzgJ8MxkpuN59qlFiI44tB0LQRet2hTZo9q4vBoyYD7RkE749685kKkQbzCd7hws4YWaP36cyUXF3L1mHKenGH6LqY9hoapzkJ8wX1xqKjozRDddh8tOMGWeBe4OFpt-vg6_N26GHZttGcJYwm3aiglUBraF4tYdaIrSxNavD6RCkgyy0QQBABCmZE8g1/s790-rw-e365/aitm.png)

Cybersecurity researchers are warning about malicious email campaigns leveraging a phishing-as-a-service ([PhaaS](https://thehackernews.com/2024/11/microsoft-meta-and-doj-disrupt-global.html)) toolkit called **Rockstar 2FA** with an aim to steal Microsoft 365 account credentials.

"This campaign employs an AitM [adversary-in-the-middle] attack, allowing attackers to intercept user credentials and session cookies, which means that even users with multi-factor authentication (MFA) enabled can still be vulnerable," Trustwave researchers Diana Solomon and John Kevin Adriano [said](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas/).

Rockstar 2FA is assessed to be an updated version of the [DadSec](https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html) (aka Phoenix) phishing kit. Microsoft is tracking the developers and distributors of the Dadsec PhaaS platform under the moniker [Storm-1575](https://x.com/MsftSecIntel/status/1712936244987019704).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Like its predecessors, the phishing kit is advertised via services like ICQ, Telegram, and Mail.ru under a subscription model for $200 for two weeks (or $350 for a month), allowing cyber criminals with little-to-no technical expertise to mount campaigns at scale.

Some of the promoted features of Rockstar 2FA include two-factor authentication (2FA) bypass, 2FA cookie harvesting, antibot protection, login page themes mimicking popular services, fully undetectable (FUD) links, and Telegram bot integration.

It also claims to have a "modern, user-friendly admin panel" that enables customers to track the status of their phishing campaigns, generate URLs and attachments, and even personalize themes that are applied to the created links.

Email campaigns spotted by Trustwave leverage diverse initial access vectors such as URLs, QR codes, and document attachments, which are embedded within messages sent from compromised accounts or spamming tools. The emails make use of various lure templates ranging from file-sharing notifications to requests for e-signatures.

Besides using [legitimate link redirectors](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/trusted-domain-hidden-danger-deceptive-url-redirections-in-email-phishing-attacks/) (e.g., shortened URLs, open redirects, URL protection services, or URL rewriting services) as a mechanism to bypass antispam detection, the kit incorporates antibot checks using Cloudflare Turnstile in an attempt to deter automated analysis of the AitM phishing pages.

[![Phishing-as-a-Service](data:image/png;base64... "Phishing-as-a-Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWLutWgCqHi_TE6d-gc0znpmwYN5OpT8snXQYLQgiLlcEnymCfWxPtJnTHBf-vsM1d7RUUQMdZ-OVe2QJ3husNte6w5LuOt0anXuni_AYPQqHwZl4_0HTcyQhM9NEV_gS_uD_Soz8__mbvtOPGk5t4yELv3XYpKYtMR0N6dfcyWJ5RUYDPy9TWmgZT3qhC/s790-rw-e365/emails.png)

Trustwave said it [observed](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns/) the platform utilizing legitimate services like Atlassian Confluence, Google Docs Viewer, LiveAgent, and Microsoft OneDrive, OneNote, and Dynamics 365 Customer Voice to host the phishing links, highlighting that threat actors are taking advantage of the trust that comes with such platforms.

"The phishing page design closely resembles the sign-in page of the brand being imitated despite numerous obfuscations applied to the HTML code," the researchers said. "All the data provided by the user on the phishing page is immediately sent to the AiTM server. The exfiltrated credentials are then used to retrieve the session cookie of the target account."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Malwarebytes [detailed](https://www.threatdown.com/blog/beluga-phishing-campaign-targets-onedrive-credentials/) a phishing campaign dubbed Beluga that employs .HTM attachments to dupe email recipients into entering their Microsoft OneDrive credentials on a bogus login form, which are then exfiltrated to a Telegram bot.

Phishing links and deceptive betting game ads on social media have also been found to push adware apps like [MobiDash](https://www.threatdown.com/blog/watch-out-mobidash-android-adware-spread-through-phishing-and-online-links/) as well as fraudulent financial apps that steal personal data and money under the guise of promising quick returns.

"The betting games advertised are presented as legitimate opportunities to win money, but they are carefully designed to trick users into depositing funds, which they may never see again," Group-IB CERT analyst Mahmoud Mosaad [said](https://www.group-ib.com/blog/shady-bets/).

"Through these fraudulent apps and websites, scammers would steal both personal and financial information from users during the registration process. Victims can suffer significant financial losses, with some reporting losses of more than US$10,000."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive cont...