---
title: 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests
url: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
source: The Hacker News
date: 2026-06-22
fetch_date: 2026-06-23T06:08:25.809480
---

# 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests](https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html)

**Swati Khandelwal**Jun 22, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA4IfKMjQxVhpOYdrcCC4ty0vlGBDg_qCZuuvSTvyVWXYPXQlli7qyCZkPdHHuGJp-HVH1s-HGmf_Zqn97o2Qz5JOHaZ-Mk1mecm4W4yUBiCaejJL5guczISx2Q8ZH7RvS_4fXiNdHemr1aWKwz0CcyBJI_4_jFjQhY5JedBz_-pSiSQ1eQCF_BPYEbRs/s1700-e365/sq.jpg)

A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy.

The bug traces to a [1997 FTP-parsing change](https://github.com/squid-cache/squid/commit/bb97dd37a) and is still live in Squid's default configuration. Researchers at Calif.io [disclosed it in June](https://blog.calif.io/p/squidbleed-cve-2026-47729) and named it **Squidbleed** (**CVE-2026-47729**), after Heartbleed, which leaked memory the same way.

Squid describes this as an attack by a [trusted client](https://seclists.org/oss-sec/2026/q2/896): someone already permitted to use the proxy, not any random host on the internet. That matches Squid's usual home, shared networks like schools, offices, and public Wi-Fi. In those setups, the attacker is just another user of the same proxy.

The leak also only reaches traffic that Squid can read. Normal HTTPS rides an opaque CONNECT tunnel, so Squid never sees inside it; the exposed traffic is cleartext HTTP, plus TLS-terminating setups where Squid decrypts and inspects.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The attacker also needs the proxy to reach an FTP server they control on port 21. Both FTP and that port are on by default.

## How the leak works

The bug sits in Squid's FTP directory-listing parser. To handle old NetWare servers that padded listings with extra spaces, the code skips whitespace with a loop: while (strchr(w\_space, \*copyFrom)) ++copyFrom;.

If the attacker's FTP server sends a listing line that ends right after the timestamp, with no filename, copyFrom lands on the string's null terminator. strchr treats that terminating NUL as part of the string it searches, so it returns a pointer instead of NULL, and the loop never stops. It walks off the end of the buffer, and xstrdup copies whatever follows back to the attacker as a filename.

The leaked bytes are the useful part. Squid reuses freed memory buffers without zeroing them, so a 4KB buffer that recently held a victim's HTTP request still holds most of it. A short FTP line overwrites only the first few bytes; the over-read returns the rest.

Calif's demo pulls an Authorization header from a victim sharing the same proxy, enough to act as that user. [Proof-of-concept code is public](https://github.com/califio/publications/tree/main/MADBugs/squidbleed), and no in-the-wild exploitation has been reported as of writing.

## What to do

If you patch, verify the fix, not just the version. Confirm the guard is in FtpGateway.cc, or check your distribution's backport, since distros ship their own builds (Debian packages Squid 5.7).

The public thread is still inconsistent: maintainer Amos Jeffries first said Squid 7.6 carried the fix, then [corrected that to 7.7](https://seclists.org/oss-sec/2026/q2/930), and on June 22 Debian's Salvatore Bonaccorso [noted the referenced commit](https://seclists.org/oss-sec/2026/q2/995) looks like it is already in 7.6.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The fix is small, a [null-terminator check before the vulnerable strchr calls](https://github.com/squid-cache/squid/commit/865a131c7d557e68c965043d98c2eccae26deef8), merged to the development branch in April and v7 in May. Squid 7.6 does separately patch CVE-2026-50012, an unrelated cache\_digest heap overflow.

The cleaner move is the one the researchers recommend anyway: turn FTP off. Chromium dropped FTP years ago, and most networks carry almost none of it, so disabling it removes this attack surface for free, whatever build you run.

The risk is real but bounded. SUSE rates it moderate, [CVSS 6.5](https://www.suse.com/security/cve/CVE-2026-47729.html), and the vector explains the score: the attacker needs proxy access (low privileges), and the only impact is confidentiality, nothing on integrity or availability.

Calif credits Anthropic's Claude Mythos Preview, the model behind [Project Glasswing](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html), with catching the strchr quirk almost at once, the same kind of buried parser bug [AI agents have been surfacing elsewhere](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html), including in FFmpeg. Calif hints Squid's FTP code may not be the last place it forgot to stop reading.

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

[Ai Research](https://thehackernews.com/search/label/Ai%20Research), [Credential Leak](https://thehackernews.com/search/label/Credential%20Leak), [Proxy Security](https://thehacke...