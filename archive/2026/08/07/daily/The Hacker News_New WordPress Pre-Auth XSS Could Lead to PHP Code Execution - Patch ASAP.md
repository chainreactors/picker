---
title: New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP
url: https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:00.870719
---

# New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP

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

![cybersecurity](data:image/svg+xml;base64...)

# [New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP](https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html)

**Swati Khandelwal**Aug 07, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge2pF0kPrHXARehOfrgRZzC4bsZvLQSss2mm4xJwNfV53riYQHKateFgF6HvgO5WoDDzjKhc8JFT_6pD2ggOORpEuUIBbySYIy79R_UTRAB4NpEUEi3dhenfNInEROpfShqpE6cTx_VqNfL1hf6fFJpzXLV7-RiFaJguVGvF-l_Ras_0YomMVjeV4ZdfM/s1700-e365/wordpress-xss.jpg)

WordPress has fixed a pre-authentication reflected cross-site scripting (XSS) flaw in its login screen that affects every version of the content management system. pwn.ai demonstrated how the flaw can be chained into PHP code execution on the server when a logged-in administrator interacts with an attacker-controlled page.

Tracked as **CVE-2026-64638** (CVSS score: 8.9), the high-severity vulnerability requires no attacker privileges. According to **[pwn.ai](https://pwn.ai/blog/xss2shell)**, which discovered the flaw and shared technical details with The Hacker News, the login-page XSS requires no authentication. Once a crafted username reaches the failed-login error page, the resulting JavaScript executes in the visitor's browser with no further interaction required on that page.

The code-execution path requires a victim already logged in as an Administrator and explicit interaction with an attacker-controlled page. In pwn.ai's demonstration, that interaction is one ordinary click.

The researchers told The Hacker News that the attack works against default WordPress installations and does not require unusual hosting or deployment settings. The researchers said they have multiple paths from the XSS to code execution, including variants that install a plugin or upload an arbitrary ZIP.

WordPress's own advisory takes a more cautious view of exploitability, noting that escalation to RCE involves conditions outside the attacker's control and requires successful social engineering plus explicit victim interaction.

The issue was patched on August 6 in [WordPress 7.0.3](https://wordpress.org/news/2026/08/wordpress-7-0-3-release/), with fixes backported through the 4.7 branch. WordPress recommends updating immediately, and sites that support automatic background updates should receive the security release automatically. Versions older than 4.7 remain affected but fall outside the project's current backport range.

The researchers, who call the attack chain **XSS2Shell**, said its autonomous system discovered and reproduced the vulnerability chain after being given **Paulos Yibelo**'s 2022 Same Origin Method Execution (SOME) research as a starting point.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The company said the work took nearly four days using open-source models and a multi-agent workflow. It said the chain was reproduced on July 26 and reported to WordPress the following day.

The flaw starts in the way WordPress handles the username from a failed login. According to the researchers, the value passes through sanitize\_user() and wp\_strip\_all\_tags(), which relies on PHP's strip\_tags(). A tag-like string containing whitespace after the opening < can survive that parser as text. Later, WordPress passes the value through wp\_kses\_post(), whose separate parser interprets the same input as permitted HTML. The result is attacker-controlled live DOM elements on the failed-login page.

Those elements then interact with WordPress's own user-profile.js, a profile-management script that is also loaded on the login page because the page handles password resets.

Some profile elements the script expects are absent there: two missing inputs both resolve to undefined, allowing an equality check to pass, while the otherwise undefined ajaxurl variable can be clobbered with an injected DOM element. That steers WordPress's own JavaScript toward an attacker-selected same-origin REST request.

The researchers use WordPress's REST JSONP support to turn that request into JavaScript executing in the site's origin. For deployments where anonymous REST requests return HTTP 401, the \_envelope=1 parameter can wrap the denial in an outer HTTP 200 response, allowing jQuery to continue processing the response as script.

The researchers also found in their testing that a nonce-based Content Security Policy using strict-dynamic did not block the demonstrated path.

The path from XSS to PHP execution builds on Yibelo's earlier SOME technique, which uses a permitted JSONP property chain to invoke a method in another browser window.

One path demonstrated by pwn.ai uses the WordPress-origin XSS to invoke the native Application Password approval control inside a logged-in Administrator's session. WordPress then creates an API credential and redirects it to an attacker-selected HTTPS success\_url.

[Application Passwords](https://developer.wordpress.org/advanced-administration/security/application-passwords/) are revocable credentials intended for API access, so this path does not need to steal the administrator's primary password. The researchers used the credential for authenticated REST access to publish a WordPress page containing same-origin JavaScript. When the retained administrator session opened that page, its script obtained WordPress's plugin-upload nonce and uploaded an attacker-supplied ZIP. PHP could then be requested directly from the extracted plugin. The plugin did not need to be activated.

The production evidence supplied to The Hacker News stops at the XSS. The researchers separately reproduced the cookie-less login-page XSS against two WordPress 7.0.2 deployments in fresh Chrome profiles with no WordPress cookies or credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

They did not attempt Application Password creation, file upload, persistence, or PHP execution on those systems. The complete PHP-execution chain was demonstrated separately on a clean local WordPress 7.0.2 installation.

The researchers said known WordPress hardening measures should not be treated as a complete mitigation for the underlying XSS and that applying the security update is required.

A successful PHP execution ...