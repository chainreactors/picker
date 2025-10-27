---
title: WordPress LiteSpeed Cache Plugin Security Flaw Exposes Sites to XSS Attacks
url: https://thehackernews.com/2024/10/wordpress-litespeed-cache-plugin.html
source: The Hacker News
date: 2024-10-05
fetch_date: 2025-10-06T18:59:13.860547
---

# WordPress LiteSpeed Cache Plugin Security Flaw Exposes Sites to XSS Attacks

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

# [WordPress LiteSpeed Cache Plugin Security Flaw Exposes Sites to XSS Attacks](https://thehackernews.com/2024/10/wordpress-litespeed-cache-plugin.html)

**Oct 04, 2024**Ravie LakshmananWebsite Security / Vulnerability

[![WordPress LiteSpeed Cache](data:image/png;base64... "WordPress LiteSpeed Cache")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhApXXlu88uIGKrb9s4u3kebscc93US3xfLMrozvKyHASsUEQGpUzb39ERMLUUWYQcYZnyyRsKqBbZB8B9kPThc3Vq5tnxDBEk0GZCVqr3-oaba43GxKdQ9e1OcN15npiI2C-CtwhRPAkd22ddkWVGu7GuEBeiG1rMMVWfSfE9zNXFwktjGlrJFizU62BwF/s790-rw-e365/wordpress.png)

A new high-severity security flaw has been disclosed in the LiteSpeed Cache plugin for WordPress that could enable malicious actors to execute arbitrary JavaScript code under certain conditions.

The flaw, tracked as **CVE-2024-47374** (CVSS score: 7.2), has been described as a stored cross-site scripting ([XSS](https://owasp.org/www-community/attacks/xss/)) vulnerability impacting all versions of the plugin up to and including 6.5.0.2.

It was addressed in version 6.5.1 on September 25, 2024, following responsible disclosure by Patchstack Alliance researcher TaiYou.

"It could allow any unauthenticated user from stealing sensitive information to, in this case, privilege escalation on the WordPress site by performing a single HTTP request," Patchstack [said](https://patchstack.com/articles/unauthenticated-stored-xss-vulnerability-in-litespeed-cache-plugin-affecting-6-million-sites/) in a report.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The flaw stems from the manner in which the plugin the "X-LSCACHE-VARY-VALUE" HTTP header value is parsed without adequate sanitization and output escaping, thereby allowing for injection of arbitrary web scripts.

That said, it's worth pointing out that the Page Optimization settings "CSS Combine" and "Generate UCSS" are required to enable the exploit to be successful.

Also called persistent XSS attacks, such vulnerabilities make it possible to store an injected script permanently on the target website's servers, such as in a database, in a message forum, in a visitor log, or in a comment.

This causes the malicious code embedded within the script to be executed every time an unsuspecting site visitor lands on the requested resource, for instance, the web page containing the specially crafted comment.

Stored XSS attacks can have serious consequences as they could be weaponized to deliver browser-based exploits, steal sensitive information, or even hijack an authenticated user's session and perform actions on their behalf.

The most damaging scenario is when the hijacked user account is that of a site administrator, thereby allowing a threat actor to completely take control of the website and stage even more powerful attacks.

WordPress plug-ins and themes are a popular avenue for cybercriminals looking to compromise legitimate websites. With LiteSpeed Cache boasting over six million active installations, flaws in the plugin pose a lucrative attack surface for opportunistic attacks.

The latest patch arrives nearly a month after the plugin developers [addressed](https://thehackernews.com/2024/09/critical-security-flaw-found-in.html) another flaw (CVE-2024-44000, CVSS score: 7.5) that could allow unauthenticated users to take control of arbitrary accounts.

It also follows the [disclosure](https://patchstack.com/articles/unpatched-sql-injection-vulnerability-in-ti-woocommerce-wishlist-plugin/) of an unpatched critical SQL injection flaw in the TI WooCommerce Wishlist plugin (CVE-2024-43917, CVSS score: 9.3) that, if successfully exploited, permits any user to execute arbitrary SQL queries in the database of the WordPress site.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Wordfence, which has assigned CVE-2024-43917 a higher CVSS score of 9.8, [said](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/ti-woocommerce-wishlist/ti-woocommerce-wishlist-282-unauthenticated-sql-injection) the problem is due to "insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query." This, it added, enables unauthenticated attackers to append additional SQL queries into already existing queries and extract sensitive information from the database.

Another critical security vulnerability concerns the Jupiter X Core WordPress plugin (CVE-2024-7772, CVSS score: 9.8) that allows unauthenticated attackers to upload arbitrary files on the affected site's server, potentially leading to remote code execution.

It has been fixed in version 4.7.8, along with a high-severity authentication bypass flaw (CVE-2024-7781, CVSS score: 8.1) that "makes it possible for unauthenticated attackers to log in as the first user to have logged in with a social media account, including administrator accounts," Wordfence [said](https://www.wordfence.com/blog/2024/09/90000-wordpress-sites-affected-by-arbitrary-file-upload-and-authentication-bypass-vulnerabilities-in-jupiter-x-core-wordpress-plugin/).

*(The story was updated after publication to include more information about CVE-2024-43917 and highlight the differences in the CVSS score.)*

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
[![Facebook Messenger](data:image/png;base64...