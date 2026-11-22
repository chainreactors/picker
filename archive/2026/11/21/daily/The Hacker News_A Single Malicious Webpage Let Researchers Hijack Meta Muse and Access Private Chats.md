---
title: A Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats
url: https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html
source: The Hacker News
date: 2026-11-21
fetch_date: 2026-11-22T09:02:52.400253
---

# A Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [A Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats](https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html)

**Swati Khandelwal**Nov 21, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYiVrbfn3FWfI_uNyjj8q9SZ38d2mHKu2ehdtYYKPwyg-05yKJBYUAPEaVxJq5KDGwU11X2tmEKNUKPIHQY9s67e1K9w_8NRdEOxVCDJqqMbQ6F27kfOj3GKjcQ3-0WHFNg7uYT6QeIU90qX1YW_Zvyn7WhZwpV41i5Pj6watQsF7Ti8NN1GIQLxw-jPc/s1700-nu-rw-lo-l85-e365/muse-ai.jpg)

A malicious webpage could extract a **Meta Muse** user's private conversations and stored memories from the assistant without triggering any approval prompt, researchers have shown.

The same attack could be extended to reach the credentials Muse stores for the user's connected accounts.

The work was a laboratory demonstration, not an attack on real users, and it stayed inside the individual user's cloud machine. **NebuSec**, the security firm that published it yesterday, says Muse's team has since fixed every weakness it describes.

Muse is Meta's personal AI agent, launched on September 8, that works through the online accounts a user connects to it and can make purchases on their behalf. Each person's agent runs on its own cloud computer.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

There, a monitoring layer called **Sentinel** is meant to be the single gate for anything the agent sends out, and the passwords and tokens for connected accounts are supposed to stay beyond the agent's reach.

Muse's team described the aim at launch: "So we designed the system to assume the agent may be under attack and limit the potential damage."

In the demonstration, a malicious page the agent opened could pull a user's conversation history and stored memories to an external server and alter them, with no prompt shown to the user, according to the firm's [research write-up](https://nebusec.ai/research/meta-muse-credential-exposure/).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZnPU8k823yly65d9kRWaMSl4Xtd7GdxXzDOdTDqIuEUorZA-UeG27ybMfR8snN6UbzL_xHsaE_B99SQq4FPYzDD4b0aIS6dGY6GwfTUSSwNxrX_e4GQhwdSAsBzY0DbdeugAYR7i5RIPOv_jRYnjQsDzp_1_zPRN22mL22nf9P0FNh9Qvc4Xfuf69EFM/s1700-nu-rw-lo-l85-e365/MUSE.jpg)

From there, the researchers chained a flaw in Muse's built-in browser, which the assistant uses for tasks such as creating PDFs, to a Linux kernel flaw, thereby taking full control of the user's cloud machine. They set out that chain in a [technical breakdown](https://nebusec.ai/research/inside-meta-muse/).

That full control reached the credential store, the saved files, and Sentinel itself, the parts Muse's [security design](https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) keeps walled off from the agent.

The compromise went no further than that one machine. The researchers did not break out to the shared server beneath it or into other users' machines.

Muse was built to assume its own agent could be turned against the user and to box in any break-in. Each of those controls worked as designed, the firm said, yet the attack still ran the whole way through.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The firm says it reported the findings to Muse's team and that the exploits were all fixed before publication. Meta has not publicly confirmed the fixes or commented on the work, and the write-up does not say whether any user data was accessed before the patches went in.

The firm's Muse research broke into the cloud system behind the assistant, unlike an [earlier Muse flaw](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html) found in September, which only let malware already on a user's Mac hijack the assistant on the device.

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

[AI Agents](https://thehackernews.com/search/label/AI%20Agents), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Meta](https://thehackernews.com/search/label/Meta), [Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs...