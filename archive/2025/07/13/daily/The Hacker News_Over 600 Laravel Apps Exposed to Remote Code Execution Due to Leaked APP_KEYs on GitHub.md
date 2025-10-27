---
title: Over 600 Laravel Apps Exposed to Remote Code Execution Due to Leaked APP_KEYs on GitHub
url: https://thehackernews.com/2025/07/over-600-laravel-apps-exposed-to-remote.html
source: The Hacker News
date: 2025-07-13
fetch_date: 2025-10-06T23:39:33.595163
---

# Over 600 Laravel Apps Exposed to Remote Code Execution Due to Leaked APP_KEYs on GitHub

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

# [Over 600 Laravel Apps Exposed to Remote Code Execution Due to Leaked APP\_KEYs on GitHub](https://thehackernews.com/2025/07/over-600-laravel-apps-exposed-to-remote.html)

**Jul 12, 2025**Ravie LakshmananApplication Security / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfdA6QsvuPxcwfuhho78-AdWIi2mTQlw20yMyWMCaOJPXEkdKCKRm_cD_WLkKXW94HavjzeTGeGyHQdciWtqFdeXO4wT-MrqFvPM_7XGHZdatVITkbZ01zfRSycL8Ch4L30-45niDTNYbpZNeFtcPuamQDLFNxwW6n102EF9dO2bysoCk_nVmT9LrBVjN6/s790-rw-e365/lara.jpg)

Cybersecurity researchers have discovered a serious security issue that allows leaked Laravel APP\_KEYs to be weaponized to gain remote code execution capabilities on hundreds of applications.

"Laravel's APP\_KEY, essential for encrypting sensitive data, is often leaked publicly (e.g., on GitHub)," GitGuardian [said](https://blog.gitguardian.com/exploiting-public-app_key-leaks/). "If attackers get access to this key, they can exploit a deserialization flaw to execute arbitrary code on the server – putting data and infrastructure at risk."

The company, in [collaboration](https://www.synacktiv.com/en/publications/laravel-appkey-leakage-analysis) with Synacktiv, said it was able to extract more than 260,000 APP\_KEYs from GitHub from 2018 to May 30, 2025, identifying over 600 vulnerable Laravel applications in the process. GitGuardian said it observed over 10,000 unique APP\_KEYs across GitHub, of which 400 APP\_KEYs were validated as functional.

[APP\_KEY](https://laravel.com/docs/12.x/encryption) is a random 32-byte encryption key that's generated during the installation of Laravel. Stored in the .env file of the application, it's used to encrypt and decrypt data, generate secure, random strings, sign and verify data, and create unique authentication tokens, making a crucial security component.

GitGuardian noted that Laravel's current implementation of decrypt() function introduces a security issue wherein it automatically deserializes decrypted data, thereby opening the door for possible remote code execution.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Specifically in Laravel applications, if attackers obtain the APP\_KEY and can invoke the decrypt() function with a maliciously crafted payload, they can achieve remote code execution on the Laravel web server," security researcher Guillaume Valadon said.

"This vulnerability was first documented with [CVE-2018-15133](https://nvd.nist.gov/vuln/detail/cve-2018-15133), which affected Laravel versions prior to 5.6.30. However, this attack vector persists in newer Laravel versions when developers explicitly configure session serialization in cookies using the SESSION\_DRIVER=cookie setting, as demonstrated by [CVE-2024-55556](https://nvd.nist.gov/vuln/detail/CVE-2024-55556)."

It's worth noting that CVE-2018-15133 has been [exploited](https://thehackernews.com/2024/11/androxgh0st-malware-integrates-mozi.html) in the wild by threat actors associated with the AndroxGh0st malware, after scanning the internet for Laravel applications with misconfigured .env files.

Further analysis has found that 63% of APP\_KEY exposures originate from .env files (or their variants) that typically contain other valuable secrets, such as cloud storage tokens, database credentials, and secrets associated with e-commerce platforms, customer support tools, and artificial intelligence (AI) services.

More importantly, approximately 28,000 APP\_KEY and APP\_URL pairs have been concurrently exposed on GitHub. Of these, approximately 10% have been found to be valid, rendering 120 applications vulnerable to trivial remote code execution attacks.

Given that the APP\_URL configuration specifies the application's base URL, exposing both APP\_URL and APP\_KEY creates a potent attack vector that threat actors can leverage to directly access the app, retrieve session cookies, and attempt to decrypt them using the exposed key.

Simply scrubbing secrets from repositories isn't enough, especially when they've already been cloned or cached by third-party tools. What developers need is a clear rotation path, backed by monitoring that flags every future reappearance of sensitive strings across CI logs, image builds, and container layers.

"Developers should never simply delete exposed APP\_KEYs from repositories without proper rotation," GitGuardian said. "The proper response involves: immediately rotating the compromised APP\_KEY, updating all production systems with the new key, and implementing continuous secret monitoring to prevent future exposures."

These types of incidents also align with a broader class of PHP deserialization vulnerabilities, where tools like phpggc help attackers craft gadget chains that trigger unintended behaviors during object loading. When used in Laravel environments with leaked keys, such gadgets can achieve full RCE without needing to breach the app's logic or routes.

The disclosure comes after GitGuardian [revealed](https://blog.gitguardian.com/fresh-from-the-docks-uncovering-100-000-valid-secrets-in-dockerhub/) that it discovered a "staggering 100,000 valid secrets" in Docker images publicly accessible on the DockerHub registry. This includes secrets associated with Amazon Web Services (AWS), Google Cloud, and GitHub tokens.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A new Binarly analysis of over 80,000 unique Docker images spanning 54 organizations and 3,539 repositories has likewise uncovered 644 unique secrets that encompassed generic credentials, JSON Web Tokens, HTTP Basic Authorization header, Google Cloud API key, AWS access tokens, and CircleCI API tokens, among others.

"Secrets appear in a wide variety of file types, including source code, configuration files, and even large binary files, areas where many existing scanners fall short," the company [said](https://www.binarly.io/blog/stop-the-leak-scanning-containers-for-exposed-secrets)...