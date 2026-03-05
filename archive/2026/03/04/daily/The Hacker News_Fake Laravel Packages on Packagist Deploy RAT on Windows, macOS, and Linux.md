---
title: Fake Laravel Packages on Packagist Deploy RAT on Windows, macOS, and Linux
url: https://thehackernews.com/2026/03/fake-laravel-packages-on-packagist.html
source: The Hacker News
date: 2026-03-04
fetch_date: 2026-03-05T04:07:47.703136
---

# Fake Laravel Packages on Packagist Deploy RAT on Windows, macOS, and Linux

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Fake Laravel Packages on Packagist Deploy RAT on Windows, macOS, and Linux](https://thehackernews.com/2026/03/fake-laravel-packages-on-packagist.html)

**Ravie Lakshmanan**Mar 04, 2026Threat Intelligence / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDAkhOUNeGmbnO6-Wf7OTYmb_GbxBRyWPlLwHY_xWh2a3fWN3wqYQcNDK2z-ck6dCpYStrieeh79uwREaRnu7vXx3_1SqPqi0KYqdyMtPq45fbRFKtBdc_Vnbkh9mgOXSPu4GOPlkqQxfCX-mQ-62Jw5jsA8CybEImOOvdliNEOcPjnGQDEjKrunI4kOyG/s1700-e365/php.jpg)

Cybersecurity researchers have [flagged](https://socket.dev/blog/malicious-packagist-packages-disguised-as-laravel-utilities) malicious Packagist PHP packages masquerading as Laravel utilities that act as a conduit for a cross-platform remote access trojan (RAT) that's functional on Windows, macOS, and Linux systems.

The names of the [packages](https://packagist.org/users/nhattuanbl/) are listed below -

* nhattuanbl/lara-helper (37 Downloads)
* nhattuanbl/simple-queue (29 Downloads)
* nhattuanbl/lara-swagger (49 Downloads)

According to Socket, the package "nhattuanbl/lara-swagger" does not directly embed malicious code, lists "nhattuanbl/lara-helper" as a [Composer dependency](https://getcomposer.org/doc/00-intro.md), causing it to install the RAT. The packages are still available for download from the PHP package registry.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Both lara-helper and simple-queue have been found to contain a PHP file named "src/helper.php," which employs a number of tricks to complicate static analysis by making use of techniques like control flow obfuscation, encoding domain names, command names, and file paths, and randomized identifiers for variable and function names.

"Once loaded, the payload connects to a C2 server at helper.leuleu[.]net:2096, sends system reconnaissance data, and waits for commands -- giving the operator full remote access to the host," security researcher Kush Pandya said.

This includes sending system information and parsing commands received from the C2 server for subsequent execution on the compromised host. The communication occurs over TCP using PHP's [stream\_socket\_client()](https://www.php.net/manual/en/function.stream-socket-client.php). The list of supported commands is below -

* **ping**, to send a heartbeat automatically every 60 seconds
* **info**, to send system reconnaissance data to the C2 server
* **cmd**, to run a shell command
* **powershell**, to run a PowerShell command
* **run**, to run a shell command in the background
* **screenshot**, to capture the screen using imagegrabscreen()
* **download**, to read a file from disk
* **upload**, to a file on disk and grant it read, write, and execute permissions to all users
* **stop**, to the socket, and exit

"For shell execution, the RAT probes disable\_functions and picks the first available method from: popen, proc\_open, exec, shell\_exec, system, passthru," Pandya said. 'This makes it resilient to common PHP hardening configurations."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

While the C2 server is currently non-responsive, the RAT is configured such that it retries the connection every 15 seconds in a persistent loop, making it a security risk. Users who have installed the packages are advised to assume compromise, remove them, rotate all secrets accessible from the application environment, and audit outbound traffic to the C2 server.

Besides the aforementioned three packages, the threat actor behind the operation has published three other libraries ("nhattuanbl/lara-media," "nhattuanbl/snooze," and "nhattuanbl/syslog") that are clean, likely in an effort to build credibility and trick users into installing the malicious ones.

"Any Laravel application that installed lara-helper or simple-queue is running a persistent RAT. The threat actor has full remote shell access, can read and write arbitrary files, and receives an ongoing system profile for each connected host," Socket said.

"Because activation happens at application boot (via service provider) or class autoloads (via simple-queue), the RAT runs in the same process as the web application with the same filesystem permissions and environment variables, including database credentials, API keys, and .env contents."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Laravel](https://thehackernews.com/search/label/Laravel), [Malware](https://thehackernews.com/search/label/Malware), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Packagist](https://thehackernews.com/search/label/Packagist), [PHP](https://thehackernews.com/search/label/PHP), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

T...