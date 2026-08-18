---
title: Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
url: https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
source: The Hacker News
date: 2026-08-17
fetch_date: 2026-08-18T02:54:01.998852
---

# Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

**Ravie Lakshmanan**Aug 17, 2026Vulnerability / Website Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Jfag1_E06odK7mkATjCOSPdD_fHy2kcYYHfi9fDNTsk0CRkV2yJD0Uz4MV82XjbMR5QNyK3Akw5Ysf0N7fDQ3DwApNb5Tf9R4axktScKF3UZlMVtrY3ulTzrYjFviMA8HmIUCBZhxmR59TtnJ7xf-B_iJtl3SWiBZAFbOfhUoldNdZX0sOStx6ULNMSZ/s1700-e365/wordpress-flaw.jpg)

A critical security flaw has been disclosed in Forminator Forms, a WordPress plugin with more than 600,000 active installations, that could be exploited to achieve arbitrary code execution on susceptible sites.

The vulnerability, tracked as **CVE-2026-15748**, is rated 9.8 out of 10.0 on the CVSS scoring system. It was discovered and reported by a security researcher who goes by the online alias "daroo."

"This vulnerability makes it possible for unauthenticated attackers to upload arbitrary files, including executable PHP files, to a vulnerable site, which can lead to remote code execution and complete site compromise," Wordfence [said](https://www.wordfence.com/blog/2026/08/600000-wordpress-sites-affected-by-arbitrary-file-upload-vulnerability-in-forminator-forms-wordpress-plugin/) in a report published today.

That said, a key prerequisite for successful exploitation is that the sites must have a form containing both a File Upload field and a Select field. The vulnerability impacts all versions of the plugin before and including 1.56.1. It has been addressed in version 1.56.2 released on July 31, 2026.

Per the WordPress security company, the flaw is a case of arbitrary file upload that resides in the "handle\_file\_upload()" function, stemming from a lack of sufficient file type validation in user-supplied input.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

As a result, an unauthenticated attacker can exploit the loophole to upload any file, including a specially crafted PHP file, to a vulnerable site by submitting a form and achieving remote code execution. Armed with this capability, the attacker can seize control of the site.

"This is due to insufficient file type validation in handle\_file\_upload, where the dangerous-extension blocklist performs exact-key matching that is bypassed by pipe-alternative MIME type keys, combined with a public submission handler that trusts attacker-controlled upload field configuration injected via a forged Select field value," Wordfence said.

Another aspect worth noting here is that, in the default configuration, files are uploaded to a directory protected by an .htaccess file that prevents PHP execution. But if a site administrator has configured a Custom File Upload Storage root, it may not have the same safeguard as the file is created "only when it is first needed, during a frontend request where the WordPress helper responsible for writing the .htaccess file is not loaded."

As a result, requesting the uploaded file is enough to cause the web server to execute the attacker-controlled PHP code.

### Auth Bypass Flaw in User Profile Builder Plugin

The disclosure comes days after Wordfence also highlighted another critical authentication bypass bug in User Profile Builder, which has more than 40,000 active WordPress installations, that could allow unauthenticated attackers to log in as the user with ID 1 (typically the site administrator) and take over the site.

The vulnerability, tracked as **CVE-2026-15826** (CVSS score: 9.8), was patched on July 16, 2026, with the release of version 3.16.5. All prior versions are affected by the issue, but it is only exploitable on sites where the plugin's Automatically Log In setting is enabled.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"This is due to the wppb\_log\_in\_user() function calling absint() on the return value of wp\_insert\_user() before performing an is\_wp\_error() check — when a registration is submitted with a 61–70 character username, WordPress core rejects it with a WP\_Error object, but absint() coerces that object to the integer 1 before the error check can short-circuit execution, causing the plugin to bind and return a transient-backed autologin nonce tied to user ID 1," Wordfence [said](https://www.wordfence.com/blog/2026/08/40000-wordpress-sites-affected-by-authentication-bypass-vulnerability-in-user-profile-builder-wordpress-plugin/).

"This makes it possible for unauthenticated attackers to log in as the site's Administrator account (user ID 1), resulting in full administrative takeover of the site."

Site owners who have either of the two plugins are advised to apply the updates as soon as possible and ensure their installations are up-to-date.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehacker...