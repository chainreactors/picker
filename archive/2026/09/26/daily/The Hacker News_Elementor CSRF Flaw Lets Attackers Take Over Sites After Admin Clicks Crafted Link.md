---
title: Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link
url: https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html
source: The Hacker News
date: 2026-09-26
fetch_date: 2026-09-27T07:25:09.619798
---

# Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html)

**Ravie Lakshmanan**Sep 26, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoCsmpn_im_gimeko6yEdebgucFfzjRrTH0Hmvl1triNXT64w_JdoBIqCrFEApRZ9mmKBYfJQ1fqgfubPH3ZRaWW7SJ2HSr18mBsjSdFE6AwVl362SwcdzHp0EtlL2qoVuYARkSKmOqQaORUjjYVAM-PCT9Itvvkgb69lyVLttezAFtAuCw86RpPu3lAo4/s1700-nu-rw-lo-l85-e365/wordpress-ele.jpg)

Details have emerged about a high-severity security flaw in the Elementor Website Builder WordPress plugin that could be exploited by an unauthenticated attacker to create rogue administrator accounts and take control of a site.

The cross-site request forgery (CSRF) vulnerability, which has yet to be assigned a CVE identifier, carries a CVSS score of 8.8 out of 10.0. It only affects versions 4.3.0 and 4.3.1 of the plugin, which is active on over 10 million WordPress sites. Statistics from WordPress.org [show](https://wordpress.org/plugins/elementor/advanced/) that the two impacted versions alone have been installed on more than 2 million sites.

"One link, opened by a logged-in WordPress user, makes that user carry out any REST API action their account is permitted to perform," Patchstack [said](https://patchstack.com/articles/cross-site-request-forgery-in-elementor-plugin-affecting-2-million-sites/). "On a stock installation, an administrator clicking the link creates a second administrator account for the attacker."

The WordPress security company said the attack does not hinge on any prerequisite, such as JavaScript, a submitted form, or a web page under the threat actor's control. The link can even be a plain anchor tag embedded in an email, a chat message, or a comment.

Following responsible disclosure, the issue has been addressed in [version 4.3.2](https://elementor.com/pro/changelog/) released earlier this week. A security researcher going by the alias "Saggre" has been credited with discovering and reporting the bug.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Patchstack said the vulnerability stems from the Editor Events module skipping CSRF protection for cookie-authenticated REST API requests every time the literal string "elementor/v1/events/" appears anywhere in the request URI.

"Because the request URI includes the query string, and the query string is written by whoever composes the link, any REST request can opt itself out of that protection by appending a harmless-looking parameter," it added.

The bypass applies to the entire REST API surface of a site, including WordPress core routes and the routes of every other plugin installed on it. An attacker could exploit this loophole to create an administrator account through "/wp/v2/users" using a request like below -

```
https://example.com/wp-json/wp/v2/users
?_method=POST
&username=csrfadmin
&email=csrfadmin%40example.test
&password=...
&roles%5B%5D=administrator
&x=elementor/v1/events/
```

Because Elementor releases before 4.3.0 do not ship the Editor Events proxy, they are not affected by the flaw. Users of the plugin are advised to apply the latest update as soon as possible to counter any potential threat.

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

Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data](https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html)

[![The Hacker News](data:image/svg+xml;base64...)

Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions](https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories](https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html)

[![The Hacker News](data:image/svg+xml;base64...)

Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content](https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agent Bypassed Australian Medicare Portal Controls to Access Non-Public Files](https://thehackernews.com/2026/09/openai-agent-bypassed-australian.html)

[![The Hacker News](data:image/svg+xml;base64...)

A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You](https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html)

[![The Hacker News](data:image/svg...