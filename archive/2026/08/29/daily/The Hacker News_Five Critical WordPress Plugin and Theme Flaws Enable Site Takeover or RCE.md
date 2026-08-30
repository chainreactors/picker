---
title: Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE
url: https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html
source: The Hacker News
date: 2026-08-29
fetch_date: 2026-08-30T07:42:32.783845
---

# Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE](https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html)

**Ravie Lakshmanan**Aug 29, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiROOqCRPV4u9cWfJL8nvCYKi4Ake-ki3_uh8Qn8RJ0P20h3Mz_qxVfF856pJ9DQZMHy922CeLwOHDc37Gpb4p1UCTMx6cMT5HeeAP_w4RitCuQficYcGDDkqpDVfW_nA3M7qWT-WyM6A5Adk3J2e8kMWSG1GSUOatrcVBmc7fmb2-ovadVS3fOdkd1ubFx/s1700-nu-rw-lo-l85-e365/wordpress-themes.jpg)

Multiple critical security flaws have been disclosed in WordPress plugins and themes, including WPMU DEV Dashboard, Avada, TranslatePress, Pods, and GiveWP, that could lead to authentication bypass, account takeover, and arbitrary code execution.

The vulnerabilities, according to Wordfence and Patchstack, are listed below -

* **[CVE-2026-76581](https://www.wordfence.com/blog/2026/08/wordfence-argus-finds-critical-authentication-bypass-in-wpmu-dev-dashboard-plugin/)** (CVSS score: 9.8) - An authentication bypass flaw in the WPMU DEV Dashboard plugin that could allow an unauthenticated attacker, on sites connected to WPMU DEV with Hub Single-Sign On (SSO) enabled and mapped to an administrator, to obtain administrator access and achieve site takeover. (Affects all versions up to, and including, 5.0.1)
* **[CVE-2026-18431](https://www.wordfence.com/blog/2026/08/wordfence-argus-finds-complex-6-step-critical-rce-in-avada-theme-with-1-million-sales/)** (CVSS score: 9.8) - An arbitrary file write flaw in the Avada theme for WordPress that makes it possible for an unauthenticated attacker to write attacker-controlled files to the server, which, in turn, can be exploited to create and execute arbitrary PHP files, resulting in remote code execution and complete site compromise. (Affects all versions up to, and including, 7.16, when the Fusion Builder plugin is installed and active in versions up to, and including, 3.16)
* **[CVE-2026-19632](https://www.wordfence.com/blog/2026/08/400000-wordpress-sites-affected-by-account-takeover-vulnerability-in-translatepress-wordpress-plugin/)** (CVSS score: 9.8) - A sensitive information exposure flaw in the "TranslatePress – Translate Multilingual sites with AI Translation" plugin that could allow an unauthenticated attacker to extract the raw administrator password-reset URL, including the plaintext reset key and login parameters, and enable full administrator account takeover. (Affects all versions up to, and including, 3.3.1 only when automatic string saving is enabled and the target administrator's profile locale is set to a published secondary language)
* **[CVE-2026-19598](https://www.wordfence.com/blog/2026/08/100000-wordpress-sites-affected-by-privilege-escalation-vulnerability-in-pods-wordpress-plugin/)** (CVSS score: 9.8) - A privilege escalation flaw in the "Pods – Custom Content Types and Fields" plugin that allows an unauthenticated attacker to escalate their privileges to Administrator or overwrite the password of any user account, including the site owner's, resulting in complete site takeover. (Affects all versions up to, and including, 3.3.9)
* **[CVE-2026-82222](https://patchstack.com/articles/unauthenticated-php-object-injection-to-remote-code-execution-on-givewp/)** (CVSS score: 10.0) - A vulnerability in the GiveWP plugin that allows an attacker to execute arbitrary commands on the server of a GiveWP site that has one published donation form and one active payment gateway. (Affects all versions up to, and including, 4.16.7.1)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"The flaw chains a broken 'safe unserialize' helper, a donation flow that feeds that helper attacker-controlled data, and a gadget chain in code that GiveWP ships," Patchstack said about CVE-2026-82222. "This case shows how PHP object injection turns into remote code execution when three ingredients line up: a place to store an attacker-controlled serialized object, code that later unserializes it, and a gadget chain in loaded classes."

"The root causes are common: trusting a serialization sanitizer that does not actually strip objects, unserializing data read back from the database as if it were trusted, and shipping development-only libraries into production where they provide ready-made gadget chains."

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

[Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [WordPress](https://thehackernews.com/search/label/WordPress)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account](https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More](https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html)

[![The Hacker News](data:image/svg+xml;base64...)

Actively Exploited Oracle WebLogic Flaw L...