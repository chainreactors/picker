---
title: Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs
url: https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
source: The Hacker News
date: 2026-11-06
fetch_date: 2026-11-07T08:02:14.251055
---

# Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs](https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html)

**Swati Khandelwal**Nov 06, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsAMxBevh2cmz1buKWukyP6JgUHrIPcr9zrJjAs1OwDoP1wMjn_s_WKHeUAdSwVzTImUsDE0C3SLGEpciaLk9H8CGvqiYugQWASsflB1a5zA9Wyr4RbroT3Z3JlOeak1AEinAy7Brf9N0BRDuGFWdZC23nCrOq4VuSMQQuDFYBYC6YCEm2ncPhHOv3KXs/s1700-nu-rw-lo-l85-e365/cwp.jpg)

A backdoor has been found hiding in the web server that runs **Control Web Panel** (CWP), a free panel for managing Linux hosting servers, researchers at QiAnXin's XLab said this week.

The backdoored web server executes commands that attackers send via web requests, and those requests never appear in its access logs. Installing it takes root access, so the attackers must already control the server.

The researchers, who named the backdoor **cwpdoor**, captured its installer, a shell script posing as a version update, on June 29. The installer handles only two versions of that web server, cwpsrv 1.15.10 and 1.24.0. The researchers do not yet know how attackers get the root access the installer needs.

On September 30, an archive holding a copy of the backdoor was uploaded to VirusTotal from Brazil. The researchers say this indicates that "real victims already exist in the wild." They give no count of infected servers.

The backdoor is **cwpsrv** itself, rebuilt with extra code, the researchers found in their [technical analysis](https://blog.xlab.qianxin.com/cwpdoor-the-invisible-backdoor-living-inside-control-web-panel/). It behaves like the normal program until a request arrives with a valid timestamp and signature in custom headers whose names begin with X-Ngx-Integrity. It then runs the command carried in the request.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

When the installer replaces the cwpsrv file, it puts the file's dates back to their original values, so checks with ls and stat show it as unchanged. When the researchers checked, the backdoor file had zero detections out of 63 on VirusTotal.

### Checking a Server for the Backdoor

XLab gives three checks:

* **Socket:** run `ss -axp | grep integrity`. A result naming `ngx_http_integrity_helper`, the Unix socket the backdoor uses, is a sign of infection.
* **Process:** run `ps aux | grep cwpsrv` and look for unexpected helper processes started by cwpsrv.
* **File:** run `strings /usr/local/cwpsrv/bin/cwpsrv | grep X-Ngx-Integrity` and look for the backdoor's header names.

In the researchers' example, the socket check found the backdoor on a server where the list of open ports looked normal.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxh6I-CLt7M0pgao5VVUU_dj9ty0db4JOy7PvBajkEMDuwvRni7cQU_epR1b6DQe-xDxYoI5zEXCYkVEen1ze7UGuv-wAVIDl9w0hD29kioc7gX5zKF2fowPwVUoa_u4vUEDxqmF_-v3FxAFxz0B-xDHK2PF0rhszCuPfuy39qQ9UTFsMsRhD5nKjEjkU/s1700-nu-rw-lo-l85-e365/cleam.png)

The researchers published these indicators:

* **MD5:** `e505d4ffa21cf494a5dc2d7c8f4f1236` (installer script, cwpsrv\_update.sh)
* **MD5:** `965aea67fb40de1bab5169ada993349f` (backdoored cwpsrv 1.15.10)
* **MD5:** `d3f4e95113d49ab3991b45e457bda75b` (backdoored cwpsrv 1.24.0)
* **IP:** `136.0.141[.]71` (download server)
* **URL:** `https://136.0.141[.]71/static/cwpsrv_update.sh`
* **URL:** `https://136.0.141[.]71/static/cwpsrv_1.15.10`
* **URL:** `https://136.0.141[.]71/static/cwpsrv_1.24.0`

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

### Cleaning Up an Infected Server

If a server is infected, the researchers recommend three steps:

1. Restore the original cwpsrv from the backup the installer creates in `/usr/local/cwpsrv/bin`, with a name starting `cwpsrv.prev-` and ending in a date and time. The researchers' description of the installer says it deletes "the temporary files and backup" after a successful swap, so this copy may be missing.
2. Upgrade to the latest version, then confirm that `ss -axp | grep integrity` returns nothing.
3. Change all control panel credentials, because the backdoor can run any command. Treat the whole server as compromised and check it for other threats.

The archive uploaded from Brazil also held the [Ebury malware](https://thehackernews.com/2024/05/ebury-botnet-malware-compromises-400000.html), an OpenSSH backdoor and credential stealer active since at least 2009. The researchers do not know whether the two are related, and say different attackers may have planted them on the same server.

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

[linux](https://thehackernews.com/search/label/linux), [Malware](https://thehackernews.com/search/label/Malware), [server security](https://thehackernews.com/search/label/server%20security), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.c...