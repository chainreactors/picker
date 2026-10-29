---
title: Researcher Reveals How Logic Bugs Alone Cracked Microsoft Edge in $175,000 Pwn2Own Win
url: https://thehackernews.com/2026/10/researcher-reveals-how-logic-bugs-alone.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:55.019384
---

# Researcher Reveals How Logic Bugs Alone Cracked Microsoft Edge in $175,000 Pwn2Own Win

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

# [Researcher Reveals How Logic Bugs Alone Cracked Microsoft Edge in $175,000 Pwn2Own Win](https://thehackernews.com/2026/10/researcher-reveals-how-logic-bugs-alone.html)

**Swati Khandelwal**Oct 28, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAGi2cGlEYo6PNV9aaEulhQB9MtbWjCBFhi3MugyJf4kGwtSPjq9F9wxhlptAUKuipSCQ0_NhE5eyEbHzMWnT6hVLsXtqrIQImq0QndxbKoKMz_gzxJonZa2jnvwHGEqjN_J7uyi5BPaqlGmtMn1y9xzJQywFZB_FNgKV-GR7qtBQfVmrLxdoUlyhPTiA/s1700-nu-rw-lo-l85-e365/edge.jpg)

A chain of logic flaws, with no memory corruption, can turn a malicious web page into code running on a Windows computer outside Microsoft Edge's sandbox, a security researcher has shown.

Orange Tsai of DEVCORE published the full method on October 28, five months after the chain won $175,000 at the [Pwn2Own Berlin contest](https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results) in May. Microsoft fixed the Edge bugs the day after the contest, so an up-to-date browser is not at risk.

A browser sandbox is the wall that keeps a web page's code inside the browser and off the rest of the computer. Breaking out of it, and then running a program, is what turns a web bug into full control of the machine.

Browser escapes like this almost always rely on memory corruption. This one used none. In his [write-up](https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/), Tsai describes a chain built solely from logic errors in how Edge and Windows handle ordinary features, and he says the whole exploit is under 100 lines of code.

The result is a universal cross-site scripting (UXSS) primitive: a way to run JavaScript on any website, bypassing the content security policy meant to prevent it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Because the attack starts from the browser's own process, it can reach sites like google.com that an ordinary web bug cannot touch. Tsai calls this a new attack surface rather than a one-off bug.

This was a competition exploit, not an attack seen in the wild. Tsai demonstrated it on stage at Pwn2Own; there is no evidence it has been used against real users, and the public CVE records list exploitation as none. One step in the chain restarts the browser, which Tsai notes is a convenience for the contest and not needed in a real attack.

The chain begins with an Edge feature for business sign-ins called a conditional access navigation throttle. Tsai found that triggering it lets the browser's own process start a new navigation that is not tied to the page that asked for it, so Edge attaches it to whichever tab is open. That mismatch is the first bug, and it produces the UXSS.

Making it run without a click took four more weaknesses. Edge checked that the request came from a trusted Microsoft site, but Tsai bypassed the check by opening the request from a second window. Edge's popup blocker should have stopped that window, but Edge carried a hardcoded list of allowed addresses, and one of them opened the popup.

The attack also required the victim to be already signed in, which the Edge auto-sign-in feature provides on its own when the user visits a Microsoft site. Lastly, the chain reads the victim's email address from a Microsoft site, assets.msn.com, which returned it to any website due to a misconfigured cross-origin setting.

Running JavaScript everywhere is still not in control of the computer. To escape the sandbox, Tsai used Edge's reading mode, Immersive Reader, which runs under a custom read:// address that Microsoft left off the list of pages barred from running scripts.

From there, the chain called an internal Edge function meant to zip up diagnostic logs and abused it to write a file with an attacker-chosen name and content anywhere on disk.

That file write is turned into code execution in two steps. The chain overwrites a configuration file that controls which websites may launch which protocol handlers, then restarts Edge so the file is read. It then launches a telnet:// link; because Windows does not ship a telnet program by default, it searches the system path for one and runs an attacker-planted copy from a folder the low-privileged user can write to.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Microsoft shipped the fix on May 15, the day after the contest, in [Edge Stable version 148.0.3967.70](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security). That release carried three Edge-specific fixes, tracked as CVE-2026-45492, CVE-2026-45494, and CVE-2026-45495. The first is recorded as a security feature bypass, and the second as a spoofing bug, both affecting Edge versions before 148.0.3967.70.

Microsoft's records rate the first two at 5.4 on a 10-point scale, a medium score that reflects a single bug in isolation, not the full chain that strings them into code execution. DEVCORE said the fix came within 24 hours of the disclosure.

Updating Edge closes this chain. Because the fix shipped in May, a browser on automatic updates has long since received it, and no separate action is needed.

Tsai built the chain by hand, over about two months, without any AI help, and frames the work as a point about where human research still matters. "The hard part is finding them, and once you find them all, chaining is the easiest part," he writes of the logic bugs. The research won the 2026 Pwnie Award for Epic Achievement.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_sha...