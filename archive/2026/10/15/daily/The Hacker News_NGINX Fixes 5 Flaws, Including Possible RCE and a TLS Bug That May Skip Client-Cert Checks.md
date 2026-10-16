---
title: NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert Checks
url: https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:54.978664
---

# NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert Checks

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

# [NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert Checks](https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html)

**Swati Khandelwal**Oct 15, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEionuV8CAd7SP0bgEbHyb-0hp7JWNkWpPjYtkNH9p86nRQrxDN1T97D1cragnVVzAwCEFCuqrwuysgwzxJLfvTXrYhMSGj5rbBzrpjW-VPvAmrc2-9EAR_hBmPigJUOjynvkm0ArpyasyzCOAWUWFYdCqzsbCJVOsxC09LnYwH2dcV4j4Vm9S9VDelXUlc/s1700-nu-rw-lo-l85-e365/tls.jpg)

NGINX released versions 1.30.6 and 1.31.7 on October 14 to fix five vulnerabilities, one of them present in every release since May 2005.

There are three memory bugs that F5, the company behind NGINX, says could crash a worker process or possibly let an attacker run code, and each requires a specific configuration to exploit.

A fourth lets an attacker forge a TLS session that could get past client-certificate checks, though F5 calls the forgery non-deterministic and beyond the attacker's control. The fifth lets an HTTP/3 client slip extra bytes into a request that NGINX passes on to a backend.

None of the five was in CISA's Known Exploited Vulnerabilities catalog as of October 15, and neither NGINX nor F5 reports attacks. [NGINX rates all five medium](https://nginx.org/en/security_advisories.html). F5 scores the three memory bugs 9.2, Critical, on CVSS v4.0, the TLS flaw 8.3, and the HTTP/3 flaw 6.9.

### Which Configurations Are Exposed

Every one of the five needs a directive you added: an alias with a rewrite, a regex map, AIO with SSI, a shared TLS session cache, or HTTP/3. NGINX's own documentation recommends the shared session cache and request buffering; the other condition for the HTTP/3 flaw is on by default.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The TLS flaw sits in the automatic rotation of session ticket keys. Session tickets let a client resume a TLS session without a full handshake, and since version 1.23.2, from October 2022, a [shared session cache](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_cache) makes NGINX generate and rotate the ticket keys itself unless you load keys from a file.

Each worker process keeps a copy of three key slots. Rotation copied only two, so the third slot held whatever was in memory before, and a ticket naming that slot could be verified and decrypted with that uninitialized key material, "allowing a forged session," [the fix commit](https://github.com/nginx/nginx/commit/1916f26e6ca49296568633d309777e36527e5bb2) says.

F5 says the forgery works "in a non-deterministic manner that is beyond the attacker's control," and that an attacker could use it to bypass verification of client certificates. The exposed setting, ssl\_session\_cache shared:SSL:10m, is the one NGINX's documentation uses in its example configuration. NGINX fixed a session-reuse flaw with the same consequence, CVE-2025-23419, in February 2025.

The conditions and workarounds below are NGINX's and F5's. The version ranges are from NGINX's advisories page.

| Flaw | What it allows | Configuration that exposes you | Affected versions | If you cannot upgrade (F5) |
| --- | --- | --- | --- | --- |
| [CVE-2026-15176](https://my.f5.com/manage/s/article/K000162416) | Heap overflow in a worker process: crash, possibly code execution | A location with `alias`, a `rewrite` that changes the URI, and anything that reads `$request_filename` (`return`, `set`, `if`, `add_header` or the access-log format) | 0.1.29 to 1.31.6 | Do not use `alias` in that location. Do not use `$request_filename`. |
| [CVE-2026-93479](https://my.f5.com/manage/s/article/K000162607) | Heap overflow in a worker process: crash, possibly code execution | A regex `map` whose captures are referenced by `root` or `log_format` before the map's output variable | 1.30.0 to 1.30.5 and 1.31.2 to 1.31.6 | Use named captures, and use them only inside the block with the regex match. |
| [CVE-2026-97205](https://my.f5.com/manage/s/article/K000162608) | Use-after-free in a worker process: crash, memory corruption, possibly code execution | `aio` enabled and an SSI page with `include virtual` commands, in some configurations | 0.8.11 to 1.31.6 | Turn `aio` off, or do not serve SSI pages. |
| [CVE-2026-95101](https://my.f5.com/manage/s/article/K000162613) | Extra bytes injected into a proxied request, or a body past `client_max_body_size` | HTTP/3 with [`proxy_request_buffering on`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_request_buffering) , the default | 1.25.0 to 1.31.6 | Set `proxy_request_buffering off`. |
| [CVE-2026-97629](https://my.f5.com/manage/s/article/K000162606) | A forged TLS session that could bypass client-certificate verification (non-deterministic and beyond the attacker's control, F5 says) | `ssl_session_cache shared:...` without [`ssl_session_ticket_key`](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_ticket_key) , which turns on automatic key rotation | 1.23.2 to 1.31.6 | Remove the shared cache directive, or load keys from a file with `ssl_session_ticket_key`. Servers with `ssl_session_tickets off` are not affected. |

### One Flaw Traces to July's Fix

The map flaw, CVE-2026-93479, is in the string-handling code that NGINX patched on July 15 for [CVE-2026-42533](https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html), a heap overflow F5 scored 9.2 that is reached through a regex map's captures.

The new overflow became possible after a change in that July release, according to [the fix commit](https://github.com/nginx/nginx/commit/6aa4b3fdd4fdc156153f2981eb4070690624447c). A July patch added protection against overrunning a buffer, but data could still spill into a reserved area, and [a second July patch](https://github.com/nginx/nginx/commit/a8289aa69c74f7e664ad63b91c17aa2a554f190f) then sized the...