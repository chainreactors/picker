---
title: PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw
url: https://thehackernews.com/2026/10/php-issues-second-windows-security.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:43.549796
---

# PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw](https://thehackernews.com/2026/10/php-issues-second-windows-security.html)

**Swati Khandelwal**Oct 26, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWGYEqFaRxRywsWzBt-2T2G_Jpdp4zy3iV7qI1alNGRaBf_8TMdzRQQb335GhASkVoXD3q9mGkiLjAog4ez9d7DHhl88lkNVvuhI74KiKZP0zZpb2O8yyqyDw12WoYTiGaq1AVfG9TfGcdNhP-DmRwuKJ4Pj4mr9rEo-TVLYxYSpmUogJUSFZFL_VaduQ/s1700-nu-rw-lo-l85-e365/php-windows.jpg)

PHP has rebuilt its official Windows packages for PHP 8.2 through 8.5 to fix **[CVE-2026-111497](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html)**, a flaw in the Brotli compression library that the packages include. The flaw can let an attacker corrupt memory and potentially run code.

[PHP says](https://www.php.net/archive/2026.php#2026-10-26-1) the flaw can be reached through the cURL extension when the extension decompresses HTTP responses automatically. cURL leaves that off by default, but applications and HTTP client libraries can turn it on.

The rebuilt packages, numbered `8.5.12-1`, `8.4.27-1`, `8.3.36-1` and `8.2.35-1`, come five days after the October 21 releases that fixed the two [PHP2Shell remote code execution flaws](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html). They use the same PHP source, so those fixes stay in place, and they now include [Brotli 1.2.1](https://github.com/google/brotli/releases/tag/v1.2.1), the fixed version.

PHP publishes a [software bill of materials](https://downloads.php.net/~windows/releases/archives/php-8.5.12-nts-Win32-vs17-x64.zip.spdx.json), a list of the components inside, with each package. For last week's x64 Non Thread Safe builds of all four versions, those lists show Brotli 1.2.0, one of the affected versions.

PHP [advises Windows users](https://discourse.thephp.foundation/t/announce-updated-php-windows-builds-for-brotli-security-fix/6324) to install the new builds from its [downloads page](https://www.php.net/downloads.php?os=windows). Because the PHP version itself is unchanged, `php -v` shows the same number before and after. The `-1` in the file name, as in `php-8.5.12-1-nts-Win32-vs17-x64.zip`, and the SHA-256 hash listed on the downloads page identify the new build.

Automatic decompression means cURL asks the server for a compressed response and unpacks it. In PHP code, the [`CURLOPT_ENCODING` option](https://curl.se/libcurl/c/CURLOPT_ACCEPT_ENCODING.html) turns it on, and an empty value accepts every format cURL supports.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Guzzle, a PHP HTTP client library, sets that empty value by default for requests it sends through cURL, according to the code in its [7.16.1 release](https://raw.githubusercontent.com/guzzle/guzzle/7.16.1/src/Handler/CurlFactory.php) and in 8.3.1. Based on that code and PHP's own description, an application that keeps Guzzle's default settings meets the condition for reaching the flaw on last week's Windows builds. The Hacker News has not tested this on a Windows system.

An attack would come as a crafted compressed response from a server that the PHP application contacts.

Google rates the flaw 9.2 out of 10, or Critical, on the CVSS 4.0 scale. [Red Hat rates it 8.1](https://access.redhat.com/security/cve/CVE-2026-111497), or Important, on the CVSS 3.1 scale.

[Imperva researchers ran code](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html) through the flaw on one official Node.js build, and it took them several attempts. PHP's notice does not mention any attacks. CISA's assessment of October 23 recorded no exploitation, and the flaw was not in its [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) as of that day's update.

Researchers at OpenAI found the flaw. Google fixed it in Brotli 1.2.1, 1.1.1 and 1.0.10 when it was [first disclosed on October 21](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html). Node.js, Bun and other software that ships its own copy of Brotli have also released fixes.

PHP's notice offers no workaround for systems that cannot be updated yet. [OpenAI advises](https://patchtheplanet.org/brotli) turning off automatic Brotli decompression in HTTP clients until the update is installed, and warns that removing br, Brotli's name in the Accept-Encoding header, "alone does not stop a server from sending it."

In PHP code, following that advice means not setting `CURLOPT_ENCODING`, because cURL does not decompress responses without it. In Guzzle, it means setting the [`decode_content` request option](https://docs.guzzlephp.org/en/stable/request-options.html) to `false`, which stops all automatic decoding, so gzip responses also arrive compressed.

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

[Software Security](https://thehackernews.com/search/label/Software%20Security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [Vulnerability](https://thehackernews....