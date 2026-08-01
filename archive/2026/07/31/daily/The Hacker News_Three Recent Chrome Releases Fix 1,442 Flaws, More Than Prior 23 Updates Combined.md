---
title: Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined
url: https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:35.108435
---

# Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined

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

![cybersecurity](data:image/svg+xml;base64...)

# [Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined](https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html)

**Ravie Lakshmanan**Jul 31, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqUoKsOzzL1DJubfk79p5F7EfcWUNP-tPwTMNDt329zqRohKeX2tE3qxMCciII-FZEHofHM72OihyAfF_7Eqs48MRmxxVOcGZyKML5LHynh5Akf1fWeNSsDlY2D-EaGLx2T9wy6y2jNfOGx-5xmKNhf0koUmkpIGcuShRA47RVW_207PVhnxdlPijMUmkx/s1700-e365/chrome.jpg)

Google on Thursday [announced](https://blog.google/security/chrome-stronger-with-every-update/) that it fixed a whopping 1,072 security bugs in Chrome versions 149 and 150, surpassing the total number of flaws the company fixed across the prior 23 milestones combined.

Both versions were released last month. In its latest patch for Chrome 151, released Wednesday, the tech giant [resolved 370 flaws](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html#seven-critical-chrome-flaws-fixed), out of which 349 were reported by Google itself. Seven of the vulnerabilities have been marked critical in severity.

The development comes amid an exponential surge in vulnerability discovery, mainly fueled by the advent of large language models (LLMs) that have accelerated the process, leading to an unprecedented spike in new bug reports, so much so that issues are being [flagged at a faster rate](https://www.propublica.org/article/anthropic-mythos-microsoft-software-vulnerabilities) than companies can fix them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

According to [statistics](https://nvd.nist.gov/vuln/search#/nvd/home?resultType=statistics) shared by the U.S. National Vulnerabilities Database (NVD), 46,872 flaws have been recorded so far in 2026, nearing the 49,920 vulnerabilities reported for the entirety of 2025.

One such vulnerability discovered in the Chrome codebase is a [critical sandbox escape](https://issues.chromium.org/issues/487383169) in the Navigation component ([CVE-2026-3545](https://nvd.nist.gov/vuln/detail/CVE-2026-3545), CVSS score: 9.6) that could be exploited to trick the browser into reading local files from the user's system. It was [patched](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop.html) by Google earlier this March.

The shortcoming, per Google, was discovered via an agent harness leveraging its Gemini models and remained undetected in its source code for more than 13 years.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKZkKrgLwdlwgLsWR6ehru-X1-zm4IStPeYG9JU5r25MV1K8fadUUGWtLj85tmeG1hyphenhyphen8pdSlowXdxLxNqfxSBk9h3QgxKcDUZ3nj3vabbrXvB0hQVWCc6_fIXF8IpJBHeH5PnEJccI0DC-RXBv6wad57cvp7qknybnZ7xZw7oY-Q9eDcj3s6YsdBMWcycN/s1700-e365/bugs.png)

The tech giant, which is in the process of transitioning to a two-week release cadence for major Chrome milestones, alongside weekly security updates, said it's piloting a shift to two security releases per week in the face of "fast-moving, AI-powered attacks."

"Even with this pace, proper public disclosure remains paramount," Google said in a post. "Every security bug that reaches Chrome Stable, regardless of whether it was discovered internally or reported externally, is documented and disclosed publicly as a standard best practice."

Google said it's working on automating efforts to generate release notes and CVE descriptions from security bug fixes to mitigate manual bottlenecks and further shorten the window between vulnerability discovery and public disclosure.

Separately, the internet behemoth noted it's exploring ways to dynamically apply the patches without the need for restarting Chrome and ensure a seamless session restore in situations where a restart is required for the changes to take effect, thus eliminating delays and shifting the burden away from the end users.

"By leveraging Chrome's multi-process architecture, dynamic patching sequentially replaces background child processes (like the Renderer and GPU) with updated binaries on the fly," Google said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"For example, in Chrome 150, we rolled out a change to take advantage of the unique application state on macOS where applications typically continue running in the background even after all windows are closed. Now, if Chrome detects a pending update while in this windowless state, it automatically restarts."

Additionally, Google is taking steps to eliminate entire classes of security issues from Chrome, such as use-after-frees, out-of-bounds weaknesses, and [memory safety flaws](https://thehackernews.com/2026/04/google-adds-rust-based-dns-parser-into.html), by hardening the runtime environment to combat legacy C++ flaws, transitioning to memory-safe languages like Rust, and implementing the browser's top-level user interface using HTML, CSS, and TypeScript to further reduce dependencies on traditional C++ frameworks.

That's not all. In an attempt to improve browser security, the company said it's moving all Chrome third-party dependencies onto automated update pipelines to ensure they are up-to-date.

"Every bug found and fixed is one less foothold for an attacker," Google's Chrome Security Team said. "But discovering and fixing a bug is only half the battle - we must also ship the fix and apply the update for users faster than adversaries can exploit the bug, and invest in projects that mitigate or eliminate classes of bugs through accelerated release cadences, dynamic patching, and opportune restarts, we are driving toward a browser that is continuously protected without disrupting the user."

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
[**Share on Twitter...