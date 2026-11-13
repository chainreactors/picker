---
title: Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data
url: https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:46.070370
---

# Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data](https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html)

**Swati Khandelwal**Nov 12, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhD-9bYYTxb5WmvOmftwsTAe5hDcHyjm12YlQj320OhT6WqICBOe0D6nQf-PPslE-I0c0r8xvZdTAXfyPwGQxHWRiQ5HSIPEZGEiNrE15ygDNZCRzzVvGugdRlIq6IARQf38iJG-MN-uo7MvdXXcA0wXIGDm0-olouPSw_SbBm2-2CYGHb4uHgtREv2ycI/s1700-nu-rw-lo-l85-e365/nodeks.jpg)

A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections.

Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1.

The crash flaw, **CVE-2026-123863**, needs only a default HTTP/2 server that replies before the request body has fully arrived. The Node.js project calls that behavior typical. The crash works over both TLS and cleartext connections.

The memory flaw, CVE-2026-123866, affects all three lines. From 24.22.0 and 26.9.0 onward, a client alone can trigger it. On 22.x and older 24.x and 26.x builds, it can still be triggered when the server itself closes a stream partway through a response, for example after an idle timeout.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

A separate flaw in Node.js HTTPS servers, CVE-2026-123864, can allow an unauthenticated client to read memory from other connections, "including TLS private keys and other users' requests," the project says. It affects all three supported lines.

The flaw needs a handler that calls res.flushHeaders() before the request body has fully arrived and later calls res.end() with data. Reading the leaked memory also needs a route that sends back or stores a request body. Plain HTTP servers built with node:http are not affected.

The release fixes 16 vulnerabilities in Node.js itself, seven of them rated high. The other four high-rated flaws, and the servers they affect, are:

* **CVE-2026-123865**: a client can make any default HTTP/2 server hold memory and file descriptors permanently, on all three lines.
* **CVE-2026-123874**: a client can corrupt server memory on 24.x and 26.x when the server serves files with stream.respondWithFile() or stream.respondWithFD(). On all three lines, canceling such downloads can also crash the server (CVE-2026-123875, rated medium).
* **CVE-2026-126051**: a client can crash a TLS server on 24.x and 26.x if the server uses the SNICallback, OCSPRequest, newSession or resumeSession hooks, or server.addContext().
* **CVE-2026-123872**: on a TLS server with stricter client-certificate rules for some hostnames, a client approved for another hostname can switch to a stricter one during TLS 1.2 renegotiation without meeting its rules. All three lines are affected.

The eight flaws above are all in Node.js's own HTTP/2, HTTPS and TLS server code, so they matter where a Node.js process accepts those connections itself.

Updating to the fixed version for each line is the only fix in the project's [security advisory](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases). It lists no workaround for servers that cannot update yet.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

End-of-life lines, including 20.x and 25.x, get no fix in this release, and the project says such versions are always affected.

The advisory does not report any attacks using the flaws. It also does not say whether servers that met the conditions for the HTTPS flaw should replace their TLS keys or other secrets after updating.

Five of the flaws, including CVE-2026-123863 and CVE-2026-123864, were reported by Chris Rohlf in collaboration with Claude and Anthropic Research, according to the advisory.

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

[network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-avail...