---
title: Hackers Use CAPTCHA Trick on Webflow CDN PDFs to Bypass Security Scanners
url: https://thehackernews.com/2025/02/hackers-use-captcha-trick-on-webflow.html
source: The Hacker News
date: 2025-02-14
fetch_date: 2025-10-06T20:39:37.222795
---

# Hackers Use CAPTCHA Trick on Webflow CDN PDFs to Bypass Security Scanners

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

# [Hackers Use CAPTCHA Trick on Webflow CDN PDFs to Bypass Security Scanners](https://thehackernews.com/2025/02/hackers-use-captcha-trick-on-webflow.html)

**Feb 13, 2025**Ravie LakshmananWeb Security / Cloud Security

[![CAPTCHA Trick on Webflow](data:image/png;base64... "CAPTCHA Trick on Webflow")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE8fSEcKLmb_PCMSPO4kchN7GAhh2sBQE6GhXgNTAQY-Ncpk738Ztw6YJqwgK_gZW3LU4JJDq_lZ51xSUjO_nBdL7KGVmsUqiqNLRogXPDXy7tM5qbGG98TIt53psA34_6o6X06rN6_bf9ap4OZNvvlAgUCsWdtdzEsUuIqpPvlEqV7W4GE416_Jo2bstp/s790-rw-e365/pdfs.png)

A widespread phishing campaign has been observed leveraging bogus PDF documents hosted on the [Webflow](https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html) content delivery network (CDN) with an aim to steal credit card information and commit financial fraud.

"The attacker targets victims searching for documents on search engines, resulting in access to malicious PDF that contains a CAPTCHA image embedded with a phishing link, leading them to provide sensitive information," Netskope Threat Labs researcher Jan Michael Alcantara [said](https://www.netskope.com/blog/new-phishing-campaign-abuses-webflow-seo-and-fake-captchas).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The activity, ongoing since the second half of 2024, entails users looking for book titles, documents, and charts on search engines like Google to redirect users to PDF files hosted on Webflow CDN.

These PDF files come embedded with an image that mimics a CAPTCHA challenge, causing users who click on it to be taken to a phishing page that, this time, hosts a real Cloudflare Turnstile CAPTCHA.

In doing so, the attackers aim to lend the process a veneer of legitimacy, fooling victims into thinking that they had interacted with a security check, while also evading detection by static scanners.

Users who complete the genuine CAPTCHA challenge are subsequently redirected to a page that includes a "download" button to access the supposed document. However, when the victims attempt to complete the step, they are served a pop-up message asking them to enter their personal and credit card details.

[![CAPTCHA Trick on Webflow](data:image/png;base64... "CAPTCHA Trick on Webflow")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2DSHtO0F4CBsLkLQfgwhkR36Uw9W4KZewAgcfktckqx5EHGzRVS3J34weCkCV0e_j7LMM5UmFrdoFSti8hu1maxvEVvPwwdiwHKJZp0EzdyPZHWAlZhgBx6hXzfltp5y0_V5zBpy1ZjllaEbWKp3VnC2lRZBIDNp5P5QcHUpk5jllLDohyphenhyphenGEp0YC9vxeQ/s790-rw-e365/captcha.png)

"Upon entering credit card details, the attacker will send an error message to indicate that it was not accepted," Michael Alcantara said. "If the victim submits their credit card details two or three more times, they will be redirected to an HTTP 500 error page."

The development comes as SlashNext detailed a new phishing kit named Astaroth (not to be confused with a [banking malware](https://thehackernews.com/2024/10/astaroth-banking-malware-resurfaces-in.html) of the same name) that's advertised on Telegram and cybercrime marketplaces for $2,000 in exchange for six-months of updates and bypass techniques.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Like other phishing-as-a-service ([PhaaS](https://thehackernews.com/2025/01/new-sneaky-2fa-phishing-kit-targets.html)) offerings, it allows cyber crooks the ability to harvest credentials and two-factor authentication (2FA) codes via bogus login pages that mimic popular online services.

"Astaroth utilizes an [Evilginx](https://thehackernews.com/2023/09/w3ll-store-how-secret-phishing.html)-style reverse proxy to intercept and manipulate traffic between victims and legitimate authentication services like Gmail, Yahoo, and Microsoft," security researcher Daniel Kelley [said](https://slashnext.com/blog/astaroth-a-new-2fa-phishing-kit-targeting-gmail-yahoo-aol-o365-and-3rd-party-logins/). "Acting as a man-in-the-middle, it captures login credentials, tokens, and session cookies in real time, effectively bypassing 2FA."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[digital forensics](https://thehackernews.com/search/label/digital%20forensics)[Malware](https://thehackernews.com/search/label/Malware)[online fraud](https://thehackernews.com/search/label/online%20fraud)[Phishing](https://thehackernews.com/search/label/Phishing)[social engineering](https://thehackernews.com/search/label/social%20engineering)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[web security](https://thehackernews.com/search/label/web%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Res...