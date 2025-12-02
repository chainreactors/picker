---
title: ShadyPanda Turns Popular Browser Extensions with 4.3 Million Installs Into Spyware
url: https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html
source: The Hacker News
date: 2025-12-01
fetch_date: 2025-12-02T03:19:08.190952
---

# ShadyPanda Turns Popular Browser Extensions with 4.3 Million Installs Into Spyware

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [ShadyPanda Turns Popular Browser Extensions with 4.3 Million Installs Into Spyware](https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html)

**Dec 01, 2025**Ravie LakshmananBrowser Security / Spyware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKcr0fKdcaAiLI2df3VuAO4_N-LNwwcm7EwlF6Fc_Nhrdtc3rxujMv18inGk8B_5PwclH_eM7APWwFpdHYkm1RoKFuL9P_nFsR2Evmm80od17LBp3S6-veUG0R0rZwGbJOYfFsEDp7wWkFTR8mM97pkdLX-dphCfPj_vHYEKp4nZUzZ0Ijli_LfmBeyKAu/s790-rw-e365/chrome-spyware.jpg)

A threat actor known as **ShadyPanda** has been linked to a seven-year-long browser extension campaign that has amassed over 4.3 million installations over time.

Five of these extensions started off as legitimate programs before malicious changes were introduced in mid-2024, according to a [report](https://www.koi.ai/blog/4-million-browsers-infected-inside-shadypanda-7-year-malware-campaign) from Koi Security, attracting 300,000 installs. These extensions have since been taken down.

"These extensions now run hourly remote code execution – downloading and executing arbitrary JavaScript with full browser access," security researcher Tuval Admoni said in a report shared with The Hacker News. "They monitor every website visit, exfiltrate encrypted browsing history, and collect complete browser fingerprints."

To make matters worse, one of the extensions, Clean Master, was featured and verified by Google at one point. This trust-building exercise allowed the attackers to expand their user base and silently issue malicious updates years later without attracting any suspicion.

Meanwhile, another set of five add-ons from the same publisher is designed to keep tabs on every URL visited by its users, as well as record search engine queries and mouse clicks, and transmit the information to servers located in China. These extensions have been installed about four million times, with [WeTab](https://microsoftedge.microsoft.com/addons/detail/wetab-%E6%96%B0%E6%A0%87%E7%AD%BE%E9%A1%B5/bpelnogcookhocnaokfpoeinibimbeff) alone accounting for three million installs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

Early signs of malicious activity were said to have been observed in 2023, when 20 extensions on the Chrome Web Store and 125 extensions on Microsoft Edge were published by developers named "nuggetsno15" and "rocket Zhang," respectively. All the identified extensions masqueraded as wallpaper or productivity apps.

These extensions were found to engage in affiliate fraud by stealthily injecting tracking codes when users visited eBay, Booking.com, or Amazon to generate illicit commissions from users' purchases. In early 2024, the attack shifted from seemingly harmless injections to active browser control through search query redirection, search query harvesting, and exfiltration of cookies from specific domains.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs8gV73B6TS2UxKEZPHmGhwjBUO-lS939TvxicWfC9YR8imIPzDnjRAFKA2QvZd9SQoGH3CHqvN5urLpvH8q9hOXV3brodzMCv-rYAa5pZlATVqm48kXMYoOXdxtTH4okA2wy_gtF4tIqHqR-0c8Rmb-y2xxvKC4vy75xYGLNclBV1MuxqEoidOvFGnJLK/s790-rw-e365/clean.png)

"Every web search was redirected through trovi.com – a known browser hijacker," Koi said. "Search queries logged, monetized, and sold. Search results manipulated for profit."

At some point in mid-2024, five extensions, three of which had been operating legitimately for years, were modified to distribute a malicious update that introduced backdoor-like functionality by checking the domain "api.extensionplay[.]com" once every hour to retrieve a JavaScript payload and execute it.

The payload, for its part, is designed to monitor every website visit and send the data in encrypted format to a ShadyPanda server ("api.cleanmasters[.]store"), along with a detailed browser fingerprint. Besides using extensive obfuscation to conceal the functionality, any attempt to access the browser's developer tools causes it to switch to benign behavior.

Furthermore, the extensions can stage adversary-in-the-middle (AitM) attacks to facilitate credential theft, session hijacking, and arbitrary code injection into any website.

The activity moved to the final stage when five other extensions published around 2023 to the Microsoft Edge Addons hub, including WeTab, leveraged its huge install base to enable comprehensive surveillance, including gathering every URL visited, search queries, mouse clicks, cookies, and browser fingerprints.

They also come fitted with capabilities to collect information about how a victim interacts with a web page, such as the time spent viewing it and scrolling behavior. The WeTab extension is still available for download as of writing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-insights-d)

The findings paint the picture of a sustained campaign that transpired over four distinct phases, progressively turning the browser extensions from a legitimate tool into data-gathering spyware. However, it bears noting that it's not clear if the attackers artificially inflated the downloads to lend them an illusion of legitimacy.

Users who installed the extensions are recommended to remove them immediately and rotate their credentials out of an abundance of caution.

"The auto-update mechanism – designed to keep users secure – became the attack vector," Koi said. "Chrome and Edge's trusted update pipeline silently delivered malware to users. No phishing. No social engineering. Just trusted extensions with quiet version bumps that turned productivity tools into surveillance platforms."

"ShadyPanda's success isn't just about technical sophistication. It's about systematically exploiting the same vulnerability for seven years: Marketplaces review extensions at submission. They don't watch what happens after approval."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFky...