---
title: Unpatched Kaltura mwEmbed Flaws Could Let Remote Attackers Read Files and Run Code
url: https://thehackernews.com/2026/08/unpatched-kaltura-mwembed-flaws-could.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:29.776277
---

# Unpatched Kaltura mwEmbed Flaws Could Let Remote Attackers Read Files and Run Code

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

# [Unpatched Kaltura mwEmbed Flaws Could Let Remote Attackers Read Files and Run Code](https://thehackernews.com/2026/08/unpatched-kaltura-mwembed-flaws-could.html)

**Swati Khandelwal**Aug 26, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4vWsyC0OylljN3m8OwCHpDKLPXe9Sw7VI5ddPEuRswkrrsHlTyfbfkXAKOTX7jemZjktTQh1IlD1hjeWsOJwZm2aSe4OtppGdqTBMUCxgFAPIfI2RY-jAdZD5hfHsj7KpRexnN4SbfUJ8nsLB8w6P_me_L8xM00ZjskYgpyEbMkDBC5hSt5FAuLbFaK0/s1700-e365/kaltura.jpg)

The CERT Coordination Center (CERT/CC) has disclosed two unpatched vulnerabilities in Kaltura's HTML5 video player library that allow a remote, unauthenticated attacker to read arbitrary files from a server and execute code on it.

The flaws, tracked as **CVE-2026-19913** and **CVE-2026-19912**, both stem from the same unsafe deserialization in the `mwEmbedLoader.php` endpoint of the mwEmbed player library, which Kaltura also distributes as html5lib.

Neither requires authentication or a Kaltura session token, and network access to the endpoint is the only precondition CERT/CC states.

No patch is available, and CERT/CC said it was "unable to reach Kaltura to coordinate these vulnerabilities." Administrators are advised to restrict or disable external access to the endpoint and to enforce a strict allow-list for the `ServiceUrl` parameter that permits only legitimate backend API URLs.

No exploitation had been reported at the time of writing, and neither CVE appeared in CISA's Known Exploited Vulnerabilities (KEV) catalog as of August 25, 2026.

CERT/CC describes Kaltura as a video platform providing tools for video management, publishing, playback, and integration with web applications. The vulnerable loader is exposed on customer installations and on Kaltura's own shared production hosts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Because the affected endpoint is also exposed on Kaltura's shared, multi-tenant CDN infrastructure, these vulnerabilities affect not only individual customer installations, but also every tenant served by these shared hosts," CERT/CC said in [the vulnerability note](https://www.kb.cert.org/vuls/id/308749).

The file read issue, **CVE-2026-19913**, starts with the `ServiceUrl` parameter, which `mwEmbedLoader.php` accepts and uses as the target URL for backend API requests. The `KalturaClientBase` PHP client fetches whatever that URL returns and passes it to PHP's `unserialize()` without validating the source, the scheme, or the content.

Supplying a `file://` path causes the server to fetch a local file rather than an API response. The deserialization attempt then fails. The raw bytes of the fetched file are reflected back to the requester inside the resulting error message.

Gerjan Wemekamp, the AndDone researcher credited with reporting both flaws, said in [a technical writeup published Tuesday](https://anddone-git.github.io/2026/one-parameter-two-bugs/) that he escalated the file read by retrieving the Kaltura application configuration at `/opt/kaltura/app/configurations/local.ini`, which holds plaintext database connection strings, admin and console passwords, and internal host references.

The second flaw, **CVE-2026-19912**, turns the same deserialization into code execution by way of the `uiconf_id` request parameter, which is appended to the cache folder path without sanitization when the application writes to disk.

An attacker points `ServiceUrl` at a malicious serialized object carrying executable PHP code. The client fetches and deserializes it. A `uiconf_id` value containing traversal sequences such as `../` then redirects the write outside the intended cache directory and into a web-accessible one. Requesting that file directly executes it as the web-server user.

"The file-drop step depends on the file-based cache backend, which is the Kaltura default. A memcache-only configuration may suppress the write and therefore that specific RCE path. However, that does not make the deployment safe," Wemekamp said.

With no fixed version to install, administrators running the player are advised to perform the following steps -

* **Block or remove the endpoint** at the WAF, reverse proxy, or CDN where legacy mwEmbed players are not being served.
* **Allow-list `ServiceUrl`**, permitting only the deployment's own API host and rejecting non-HTTP(S) schemes.
* **Reject `uiconf_id` values** containing traversal sequences, absolute paths, or directory separators.
* **Deny PHP execution** in cache directories.
* **Restrict outbound network access** from the application server, which the code execution path needs in order to fetch the payload.
* **Rotate everything in `local.ini`** where the endpoint has been exposed, covering database credentials, admin and console passwords, partner secrets, and API keys.

CERT/CC lists the affected releases as html5lib v2.45, v2.103 and earlier, and other v2.x releases that expose the vulnerable endpoint.

Wemekamp scored CVE-2026-19912 at 10.0 and CVE-2026-19913 at 9.1, labeling both in his writeup as reporter-assigned. CERT/CC published no score for either flaw, and there was no NVD record for either identifier as of August 25, 2026.

NIST said in April that it [no longer enriches every CVE](https://thehackernews.com/2026/04/nist-limits-cve-enrichment-after-263.html), prioritizing those in the KEV catalog, software used within the federal government, and software designated critical under Executive Order 14028.

The researcher was explicit about what he did and did not demonstrate.

"To be exact about scope: the end-to-end web shell drop was demonstrated on the Kaltura Server docker image from 2019. What I verified on the current release is that both halves of the chain are present, and that the deserialization half still executes as described," Wemekamp said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The Hacker News ver...