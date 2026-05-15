---
title: 18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated RCE
url: https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:28.584629
---

# 18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated RCE

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated RCE](https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html)

**Ravie Lakshmanan**May 14, 2026Vulnerability / Web Server

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhCvxtNv7UYYMCITB2HLsBgkN83LdRXcw0wmP9gMAfXeNpmJoOJKNIaQb55b-GLDeQHx-dUBkASGDYgstnvYAE5eFuwyzMSxY804fn56OaTsGlESOab9y-kFHJ-iV5iUlWrc5j27WLduUDhW6nRSjkv5tFMKZjDbbmDdk7_NMZ3y7sipHKy7t4XuMQ9YfG/s1700-e365/nn.gif)

Cybersecurity researchers have disclosed multiple security vulnerabilities impacting NGINX Plus and NGINX Open, including a critical flaw that remained undetected for 18 years.

The vulnerability, [discovered](https://depthfirst.com/nginx-rift) by [depthfirst](https://depthfirst.com/), is a heap buffer overflow issue impacting ngx\_http\_rewrite\_module (CVE-2026-42945, CVSS v4 score: 9.2) that could allow an attacker to achieve remote code execution or cause a denial-of-service (DoS) with crafted requests. It has been codenamed **NGINX Rift**.

"NGINX Plus and NGINX Open Source have a vulnerability in the ngx\_http\_rewrite\_module module," F5 [said](https://my.f5.com/manage/s/article/K000161019) in an advisory released Wednesday. "This vulnerability exists when the rewrite directive is followed by a rewrite, if, or set directive and an unnamed Perl-Compatible Regular Expression (PCRE) capture (for example, $1, $2) with a replacement string that includes a question mark (?)."

"An unauthenticated attacker, along with conditions beyond its control, can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process, leading to a restart. Additionally, for systems with Address Space Layout Randomization (ASLR ) disabled, code execution is possible."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The issue has been addressed in the following versions after responsible disclosure on April 21, 2026 -

* NGINX Plus R32 - R36 (Fixes introduced in R32 P6 and R36 P4)
* NGINX Open Source 1.0.0 - 1.30.0 (Fixes introduced in 1.30.1 and 1.31.0)
* NGINX Open Source 0.6.27 - 0.9.7 (No fixes planned)
* NGINX Instance Manager 2.16.0 - 2.21.1
* F5 WAF for NGINX 5.9.0 - 5.12.1
* NGINX App Protect WAF 4.9.0 - 4.16.0
* NGINX App Protect WAF 5.1.0 - 5.8.0
* F5 DoS for NGINX 4.8.0
* NGINX App Protect DoS 4.3.0 - 4.7.0
* NGINX Gateway Fabric 1.3.0 - 1.6.2
* NGINX Gateway Fabric 2.0.0 - 2.5.1
* NGINX Ingress Controller 3.5.0 - 3.7.2
* NGINX Ingress Controller 4.0.0 - 4.0.1
* NGINX Ingress Controller 5.0.0 - 5.4.1

In its own advisory, depthfirst said the vulnerability could allow a remote, unauthenticated attacker to corrupt the heap of an NGINX worker process by sending a crafted URI. What makes the vulnerability severe is that it's reachable without authentication, can be reliably used to trigger the heap overflow, and can lead to remote code execution in the NGINX worker process.

"An attacker who can reach a vulnerable NGINX server over HTTP can send a single request that overflows the heap in the worker process and achieves remote code execution," depthfirst said. "There is no authentication step, no prior access requirement, and no need for an existing session."

"The bytes written past the allocation are derived from the attacker’s URI, so the corruption is shaped by the attacker rather than random. Repeated requests can also be used to keep workers in a crash loop and degrade availability for every site served by the instance."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Also patched in NGINX Plus and NGINX Open Source are three other flaws -

* **[CVE-2026-42946](https://my.f5.com/manage/s/article/K000161027)** (CVSS v4 score: 8.3) - An excessive memory allocation vulnerability in the ngx\_http\_scgi\_module and ngx\_http\_uwsgi\_module modules that could allow a remote, unauthenticated attacker with adversary-in-the-middle (AitM) capabilities to control responses from an upstream server to read the memory of the NGINX worker process or restart it when scgi\_pass or uwsgi\_pass is configured.
* **[CVE-2026-40701](https://my.f5.com/manage/s/article/K000161021)** (CVSS v4 score: 6.3) - A use-after-free vulnerability in the ngx\_http\_ssl\_module module that could allow a remote, unauthenticated attacker to have limited control of modification of data or restart the NGINX worker process when the ssl\_verify\_client directive is set to "on" or "optional," and the ssl\_ocsp directive is set to "on."
* **[CVE-2026-42934](https://my.f5.com/manage/s/article/K000161028)** (CVSS v4 score: 6.3) - An out-of-bounds read vulnerability in the ngx\_http\_charset\_module module that could allow a remote, unauthenticated attacker to disclose memory contents or restart the NGINX worker process when charset, source\_charset, and charset\_map, and proxy\_pass with disabled buffering ("off") directives are configured.

Users are advised to apply the latest versions for optimal protection. If immediate patching is not an option for CVE-2026-42945, users are advised to change the rewrite configuration by replacing unnamed captures with named captures in every affected rewrite directive.

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
[**Share on WhatsApp](#link...