---
title: Microsoft Details Cookie-Controlled PHP Web Shells Persisting via Cron on Linux Servers
url: https://thehackernews.com/2026/04/microsoft-details-cookie-controlled-php.html
source: The Hacker News
date: 2026-04-03
fetch_date: 2026-04-04T04:17:50.142663
---

# Microsoft Details Cookie-Controlled PHP Web Shells Persisting via Cron on Linux Servers

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Microsoft Details Cookie-Controlled PHP Web Shells Persisting via Cron on Linux Servers](https://thehackernews.com/2026/04/microsoft-details-cookie-controlled-php.html)

**Ravie Lakshmanan**Apr 03, 2026Linux / Server Hardening

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_2zEf8l08MTElI1sGlJPVVWtscud2RAXdsivOvcby3pO4NUWMBioT3FNaFL7Bw0GeEqnX_WqY10FVqXhVNBTOrl0UMPoyun7AvshwpvfJIdfdJ0yJ1V2mz7ZHQDE9motXuuW6urvTJYu0kLGvpZf10Qx1hNeobD4YV25tJY9nvNoW9Sqd8nSsWK7NWQP0/s1700-e365/php-linux.jpg)

Threat actors are increasingly using HTTP cookies as a control channel for PHP-based web shells on Linux servers and to achieve remote code execution, according to findings from the Microsoft Defender Security Research Team.

"Instead of exposing command execution through URL parameters or request bodies, these web shells rely on threat actor-supplied cookie values to gate execution, pass instructions, and activate malicious functionality," the tech giant [said](https://www.microsoft.com/en-us/security/blog/2026/04/02/cookie-controlled-php-webshells-tradecraft-linux-hosting-environments/).

The approach offers added stealth as it allows malicious code to stay dormant during normal application execution and activate the web shell logic only when specific cookie values are present. This behavior, Microsoft noted, extends to web requests, scheduled tasks, and trusted background workers.

The malicious activity takes advantage of the fact that cookie values are available at runtime through the [$\_COOKIE superglobal](https://www.php.net/manual/en/reserved.variables.cookies.php) variable, allowing attacker-supplied inputs to be consumed without additional parsing. What's more, the technique is unlikely to raise any red flags as cookies blend into normal web traffic and reduce visibility.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The cookie-controlled execution model comes in different implementations -

* A PHP loader that uses multiple layers of obfuscation and runtime checks before parsing structured cookie input to execute an encoded secondary payload.
* A PHP script that segments structured cookie data to reconstruct operational components such as file handling and decoding functions, and conditionally writes a secondary payload to disk and executes it.
* A PHP script that uses a single cookie value as a marker to trigger threat actor-controlled actions, including execution of supplied input and file upload.

In at least one case, threat actors have been found to obtain initial access to a victim's hosted Linux environment through valid credentials or the exploitation of a known security vulnerability to set up a cron job that invokes a shell routine periodically to execute an obfuscated PHP loader.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_dnkqNRqaQpLxOU5zufB7nhgbrggi35J3Umk4F10AbHlHsthwjU_JsBrtLRw5Jr1PyugGvlbNMXVSJSPShLAxDXihKHtisOfPgfqqlAnH9bdyYcV7Qm2t6uEQ5nHsBVBaBG7vfCsKx7FEJ_8F5JIaTqFVWMvm9RxKa76BORPZkMaSd6tgeINAbCm5QgjI/s1700-e365/cookie.jpg)

This "self-healing" architecture allows the PHP loader to be repeatedly recreated by the scheduled task even if it was removed as part of cleanup and remediation efforts, thereby creating a reliable and persistent remote code execution channel. Once the PHP loader is deployed, it remains inactive during normal traffic and springs into action upon receiving HTTP requests with specific cookie values.

"By shifting execution control into cookies, the web shell can remain hidden in normal traffic, activating only during deliberate interactions," Microsoft added. "By separating persistence through cron-based re-creation from execution control through cookie-gated activation, the threat actor reduced operational noise and limited observable indicators in routine application logs."

A common aspect that ties together all the aforementioned implementations is the use of obfuscation to conceal sensitive functionality and cookie-based gating to initiate the malicious action, while leaving a minimal interactive footprint.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

To counter the threat, Microsoft recommends enforcing multi-factor authentication for hosting control panels, SSH access, and administrative interfaces; monitoring for unusual login activity; restricting the execution of shell interpreters; auditing cron jobs and scheduled tasks across web servers; checking for suspicious file creation in web directories; and limiting hosting control panels' shell capabilities.

"The consistent use of cookies as a control mechanism suggests reuse of established web shell tradecraft," Microsoft said. "By shifting control logic into cookies, threat actors enable persistent post-compromise access that can evade many traditional inspection and logging controls."

"Rather than relying on complex exploit chains, the threat actor leveraged legitimate execution paths already present in the environment, including web server processes, control panel components, and cron infrastructure, to stage and preserve malicious code."

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
[![Facebook Messenger](data:image/png;...