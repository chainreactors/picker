---
title: AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs
url: https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
source: The Hacker News
date: 2026-06-06
fetch_date: 2026-06-07T06:16:38.817277
---

# AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs

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

# [AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)

**Swati Khandelwal**Jun 06, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyg1vRQART17ZjJXANnrQ8Vtn7h_tM5IihGJ4LnxbGTDFL1QSvR_lEDmVm7bsO84br04_oM-RM9ZgX-6b5yVQnEOTwKgk3KzImrhPBrI91GIYmQ-n09hq3vjF3tPVnNqVhHbV22BIxXg9zhGg4b2s4kATPjtnqGWldHRw29GexKQbEcX6HxG46vPfvo26l/s1700-e365/chrome-update.jpg)

Two things landed within days of each other this week. A security startup reported 21 previously unknown vulnerabilities in FFmpeg, the media library inside almost everything that touches video, all of them found by an autonomous AI agent.

The same week, Google shipped [Chrome 149](https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop.html) with patches for 429 security bugs, the most ever in a single release.

Only the FFmpeg bugs were found by AI. Chrome's record landed after Google overhauled its bounty program to cope with a flood of AI-generated reports. The mechanisms differ, but the pressure is the same: AI is putting more vulnerabilities in front of the people who have to deal with them, and faster than before.

The FFmpeg findings come from [depthfirst](https://depthfirst.com/research/21-zero-days-in-ffmpeg), whose autonomous security agent scanned the project's roughly 1.5 million lines of C and produced 21 confirmed zero-days, each with a reproducible proof-of-concept input.

The company puts the cost of the run at around $1,000. Several of the bugs had been latent for 15 to 20 years; one stack overflow in the service-description-table code dates to 2003 and sat untouched for 23 years.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Most are heap or stack overflows in parsers and demuxers, spanning components from the TS demuxer to the VP9 decoder. depthfirst says some already carry CVE identifiers; its writeup lists nine, CVE-2026-39210 through CVE-2026-39218, and notes the rest are fixed but not yet numbered. It also [published a PoC](https://github.com/DepthFirstDisclosures/ffmpeg-dfvuln127).

In separate news, Chrome 149 fixes 429 vulnerabilities, a record for a single release. Over 100 are critical or high severity, mostly use-after-free and insufficient input validation.

The worst, CVE-2026-10881 (CVSS 9.6), is an out-of-bounds read and write in the ANGLE graphics engine that lets a crafted page escape the sandbox and run code on the host. Google paid $97,000 for it.

The highest-severity bugs were mostly internal finds: of roughly 90 high-severity bugs, only 10 came from outside researchers, and 19 of the 22 critical ones were Google's own. The AI connection is more about volume than authorship.

Google hasn't tied the 429 to AI; the on-record signal is the [bounty overhaul](https://bughunters.google.com/blog/evolving-the-android-chrome-vrps-for-the-ai-era) it made in April, prompted by a flood of AI-generated submissions and now asking for a concise reproducer over the long writeups AI churns out.

Google's Big Sleep agent reported a run of FFmpeg bugs last year, now visible on the project's [security page](https://ffmpeg.org/security.html) tagged BIGSLEEP, and Anthropic's [Mythos model](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) pulled a 16-year-old H.264 flaw and others out of FFmpeg for about $10,000, three of which shipped in FFmpeg 8.1, per its [own writeup](https://red.anthropic.com/2026/mythos-preview/).

Days ago, another autonomous tool found an authenticated RCE in [Redis](https://thehackernews.com/2026/06/autonomous-ai-tool-finds-2-year-old-rce.html) that had been present since version 7.2.0, unnoticed for over two years. The research points the same way: a February study had an agent reproduce working PoCs for more than half of [100 real Linux kernel N-day bugs](https://arxiv.org/abs/2602.07287), beating fuzzing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

For FFmpeg, pull the fixed upstream build or your distribution's security update as soon as it lands, and prioritize anything that ingests untrusted RTSP or AV1-over-RTP. FFmpeg is widely bundled in media pipelines, Python wheels, container images, and appliances, so do not stop at system packages; those embedded copies need patching too.

For Chrome, update to 149.0.7827.53 on Linux or 149.0.7827.53/54 on Windows and macOS, or confirm auto-update has run.

The response has to match the new pace: shorter patch cycles, auto-update wherever it exists, and dependency bumps that carry CVE fixes treated as security work, not routine maintenance.

The hard part is shifting, though. Finding these bugs has gotten cheap; triaging the reports, shipping the fixes, and getting them installed has not, and much of that work still falls to volunteers and a thin layer of human triagers now expected to keep pace with machines.

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

[AI](https://thehackernews.com/search/label/AI), [Chrome](https://thehackernews.com/search/label/Chrome)...