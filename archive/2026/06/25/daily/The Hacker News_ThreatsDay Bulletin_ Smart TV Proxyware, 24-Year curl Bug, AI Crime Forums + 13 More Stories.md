---
title: ThreatsDay Bulletin: Smart TV Proxyware, 24-Year curl Bug, AI Crime Forums + 13 More Stories
url: https://thehackernews.com/2026/06/threatsday-bulletin-smart-tv-proxyware.html
source: The Hacker News
date: 2026-06-25
fetch_date: 2026-06-26T06:09:43.683899
---

# ThreatsDay Bulletin: Smart TV Proxyware, 24-Year curl Bug, AI Crime Forums + 13 More Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [ThreatsDay Bulletin: Smart TV Proxyware, 24-Year curl Bug, AI Crime Forums + 13 More Stories](https://thehackernews.com/2026/06/threatsday-bulletin-smart-tv-proxyware.html)

**Ravie Lakshmanan**Jun 25, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO1f6pZmhVaPQd2FjrrAG-IbL0vMk7zHVZ6BqjzkzJS8qd7HlAtIJ-7chRUbqR7tZHPNqdZFbm0QL9O03mkW7YsOh0pVwW1_ogikaoxNX8dFd5-ZB4SwB7-tfpWmp9Hr22DJL6tzZgTdeFnCU4VwaZXSY_htGs2_xlaB8n0EOedrfe7wHuI30GXTF6Pofc/s1700-e365/threatsday-june.jpg)

It’s dumb out there again.

This week has the usual smell of prod on fire and nobody wanting to admit who left the door open — old creds still working, trusted apps doing sketchy crap, browser tricks jumping the fence, and “normal” workflows turning into phishing pipes because apparently email was not enough hell already.

The worst part is how cheap some of it feels. Not elite. Not cinematic. Just stale secrets, fake updates, lazy trust, and random boxes quietly becoming someone else’s infrastructure. Same internet, fresh headache. Let’s get into it.

1. Privacy-first bot defense

   [Cloudflare Partners With Browser Makers for PACT](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx)

   Cloudflare has teamed up with Google Chrome, Microsoft Edge, and Mozilla Firefox to create a privacy-preserving protocol that websites can use to separate desirable web traffic from undesirable network requests. This involves the use of Private Access Control Tokens (PACT), which allow websites to issue anonymous tokens that assert a given browsing session is being run by a human. "A user's browser can then provide these tokens to other sites to prove that a human is in the loop, reducing the need for annoying and clunky captchas or invasive tracking," Cloudflare [said](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx). "PACT is designed so that sites cannot leverage it to track or identify users or their browsing history."
2. Six curl CVEs

   [Multiple Flaws in curl](https://aisle.com/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported)

   AISLE said it [discovered](https://aisle.com/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported) six vulnerabilities in curl, which range from "classic memory-lifetime issues to logic bugs in how libcurl decides whether a connection, credential, or host identity is still valid." One of the notable vulnerabilities is [CVE-2026-8932](https://curl.se/docs/CVE-2026-8932.html), which allows the library to "reuse a previously created connection even when some mTLS config-related option had been changed that should have prohibited reuse." AISLE described it as the oldest curl vulnerability reported so far, adding that it has been shipped in releases since curl [version 7.7](https://curl.se/ch/7.7.html), which was released on March 22, 2001. The identified flaws have been addressed in [version 8.21.0](https://curl.se/mail/lib-2026-06/0026.html).
3. Unauthenticated takeover

   [Maximum-Severity Bug in Hoppscotch](https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-j542-4rch-8hwf)

   A critical security flaw has been disclosed in self-hosted versions of Hoppscotch(CVE-2026-50160, CVSS score: 10.0), an open source API platform, that can result in complete compromise. Offgrid Security's autonomous AI security agent, Kiro, has been [credited](https://www.offgridsec.com/blog-hoppscotch-cve-2026-50160.html) with discovering the bug. "The POST /v1/onboarding/config endpoint allows an unauthenticated attacker to inject arbitrary InfraConfig keys -- including JWT\_SECRET and SESSION\_SECRET -- into the database via mass assignment," the project maintainers [said](https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-j542-4rch-8hwf). "These keys are not declared in the SaveOnboardingConfigRequest DTO, but because the NestJS ValidationPipe does not strip extra properties, they pass through to the service layer, where Object.entries(dto) iterates all keys without restriction." A successful exploitation leads to full server compromise and persistent access that survives password resets. OffGrid Security told The Hacker News that four independent weaknesses are combined to allow an unauthenticated attacker to overwrite the JWT signing key in a single HTTP request, and the exploit requires no credentials. The issue has been fixed in hoppscotch-backend version 2026.5.0.
4. Proxyware in smart TVs

   [Residential Proxy SDKs Hidden in LG and Samsung Smart TV Apps](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks)

   A new report from Spur Intelligence has [revealed](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks) that more than one-third of LG and Samsung smart TV apps it reviewed [contain proxyware](https://thehackernews.com/2026/06/weekly-recap-browser-bugs-edr-killers.html#:~:text=Israeli%20Company%20Linked%20to%20Popa%20Android%20TV%20Box%20Botnet) that can relay third-party traffic through the TV owner's internet connection with users' consent. The company said it scanned 6,038 apps across LG webOS and Samsung Tizen and found 2,058 that contain residential proxy software. This includes clocks, screensavers, games, fish tanks, and other low-utility apps. On LG webOS, 42.5% of apps carried such code. On Samsung Tizen, the rate was 26.9%. Across both platforms, it reached 34.1%. Bright Data, Massive, and Oxylabs take up the top three SDK providers for webOS and Tizen. "Smart TVs are almost ideal proxy hosts. They sit on the same home network as everything else, but they do not feel like computers, so people rarely audit them like computers," Spur said. "There is no battery drain to notice, no cellular bill to spike, no app s...