---
title: Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data
url: https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html
source: The Hacker News
date: 2026-09-25
fetch_date: 2026-09-26T06:51:59.239826
---

# Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data](https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html)

**Swati Khandelwal**Sep 25, 2026Cloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJuj6tshfElqbwJCAvJf00nvl1Tng8D3yBW5uZZyVpwOqXJuzBB1df67IlNM1OSkHdGH11R6G8rseykpeXWUBu24sJvyxDL-uiqA7NC2ItwUUN2fMdaTWhqcHR2WYfpI6ihc0EVpEXfep1VFBygmh2-F6cAL1lwin0qQbmSebV5OmhqFmgBs3i0_WtdGI/s1700-nu-rw-lo-l85-e365/cf-escape.jpg)

A flaw in Cloudflare Containers let a paying customer read data that other customers' containers had left behind on the same server, Cloudflare and the researchers who found it said on Thursday.

The data came from disk space that earlier containers had used and given up, not from any live workload, and an attacker could not choose whose data they got, [according to Cloudflare](https://blog.cloudflare.com/containers-cross-tenant-vulnerability/). The company has fixed the flaw across its service and says customers need to do nothing.

Cloudflare Containers runs customers' programs inside containers on servers shared by many accounts, and Cloudflare, not the customer, picks the server. Cloudflare Sandboxes, which runs on Containers and is sold as a safe place to run untrusted code, including code written by AI agents, was affected too.

The flaw was reported on September 4 by Oren Yomtov of the security firm **Accomplish**, through Cloudflare's bug bounty program.

The problem was in how the shared disks were set up. Each container gets a disk built using a Linux feature called thin provisioning, which allocates storage in 64-kilobyte blocks. When a container was deleted, its blocks returned to a pool shared across customer accounts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

That pool was set to [skip wiping a block](https://docs.kernel.org/admin-guide/device-mapper/thin-provisioning.html) before handing it to the next container, and wiping is normally the default. So when a new container wrote only a small amount into a reused block, the rest of the block still held the previous container's data.

To reach it, the researchers wrote a small four-kilobyte block into unused space and then read the whole block back at the raw disk level. The 60 kilobytes they had not written still held bytes from a previous container.

Across production tests, they reported finding leftover material on 18 of 24 tries, each on a server Cloudflare chose, and on 20 of 22 underlying machines across four continents.

The recovered blocks held directory structures, database pages, and structurally complete SQLite databases, Cloudflare said; the researchers' [own write-up](https://accomplish.ai/blog/escaping-the-cloudflare-sandbox/) lists directory listings, SQLite databases, Chromium browser profiles, .env files, and credential files, and describes them as other customers' files.

The researchers reported that their analysis scripts output only counts and format checks, not file contents, and that the material they sent Cloudflare contained no third-party names, identifiers, credentials, or recovered content.

They also confirmed the recovered data was kept private and securely deleted after they submitted it, Cloudflare said. The researchers did not show that the flaw could change another customer's live data or take a workload offline.

Cloudflare fixed the flaw in two steps. It first turned wiping back on for newly handed-out blocks, which stopped the reported method; the researchers confirmed on September 14 that their proof of concept no longer worked.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

But that change did not clean blocks already mapped into running container disks or into each server's cache of prepared image layers, which a new container could inherit and read. So Cloudflare also retired every running container disk and cleared those caches, draining and restarting servers during quiet hours. It finished that cleanup on September 19, and disclosed the flaw five days later.

Cloudflare said it looked for signs that anyone else had used the method. It built detection signatures from the researchers' proof of concept and its own copy of the attack and ran them against the disk-activity records it had kept. It found only the researchers' and its own engineers' authorized testing, and said it saw no evidence that this specific method was used by anyone else.

That finding covers the records Cloudflare retained, though it did not state the time span or when the unsafe setting was first put in place, so how long the exposure lasted is not clear from its account.

The researchers, who separately say the same disk setup affected Cloudflare's Browser Run product, described the flaw as their sixth escape from a code sandbox published since July, after findings in Anthropic's Claude Cowork and Claude Code, Cursor's command-line tool, Docker, and OpenAI's Codex. Cloudflare's post named Containers and Sandboxes as affected and did not mention Browser Run.

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
[**Share on ...