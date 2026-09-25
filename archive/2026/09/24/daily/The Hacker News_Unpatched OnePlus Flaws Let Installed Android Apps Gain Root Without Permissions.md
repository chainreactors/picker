---
title: Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions
url: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:33.487911
---

# Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions

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

# [Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions](https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html)

**Swati Khandelwal**Sep 24, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiGu2guziH88Cs_LnFsPkCJ4zuxqgSX7q3SRrBXdSAEeJPhmYnpNp-c0WCNCqoOoyCv6NcnmCKm20rhqSb2rjw7KZ6Kh6UssR2fZG5SZX9Pjhb_fjONdBfgpxqpWNABPDvSmD9Hp913nErgH4PQm1ehlyspJt5RXASYckP6jHE3G0V2ou5fwkG7JOZyBY/s1700-nu-rw-lo-l85-e365/oneplus.jpg)

A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats, [chained two flaws in OnePlus's own software](https://blog.nns.ee/2026/09/24/oneplus-root/) to gain root access, the highest level of control over an Android phone.

OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not said which.

OnePlus confirmed both flaws in May. In the same reply, the company told Moorats that it alone decides when to make a flaw public and warned that publishing without its permission could result in legal liability. He published on September 24 anyway, when OnePlus had released no fix.

OnePlus set out its position in the reply, [which Moorats published in full](https://blog.nns.ee/raw/2026-09-24-oneplus-root/2026-05-20-oneplus-email.txt). It said a fix was scheduled, but claimed "the exclusive final right of vulnerability disclosure," and told him that even after a fix ships, researchers may not publish full technical details on their own.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The company argued that European cybersecurity rules require makers to accept and fix reports but do not allow researchers to disclose them without the maker's consent. It warned that if he published without permission, OnePlus would "pursue relevant legal liabilities in accordance with applicable laws."

### How the Attack Works

Moorats found the first flaw in a OnePlus service called **AtlasService**, which gathers debugging data, runs as root, and accepts calls from any app without checking who is calling.

A crafted call reaches a OnePlus debugging tool that takes the app's text and drops it, unchecked, into a system command. That hands the app root, but only within a restricted system zone called dumpstate, which cannot do everything root normally can.

The second flaw finishes the job. OnePlus ships another service, a hardware helper called olc2, with a command that executes any shell instruction it receives. Its only guard is that the caller must already be root, which the first flaw provides.

This time, the command runs in a zone that grants all low-level Linux privileges, including the ability to load kernel code, giving the app control of the device at the system level.

### Who Is Affected, and What You Can Do

The attack is local. A malicious app has to be installed and running on the phone first, so it cannot be launched over the internet. But once it is there, the app needs no permissions and shows the user no prompt, and it worked on a stock phone Moorats had not modified.

There is no evidence that anyone has used the flaws in a real attack.

Moorats also confirmed the attack on an older OnePlus 12 Pro, and he expects the same problem across OxygenOS 16 in general. OnePlus and OPPO build their phones on shared software, which is why OnePlus's warning covered both.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

As of Moorats's disclosure, OnePlus had assigned no CVE and released no fix, and no OnePlus advisory naming the flaws could be found. Until a fix ships, the one practical defense is the thing the attack needs to get started: install apps only from sources you trust, because it cannot run without a malicious app on the phone.

By Moorats's account, the disclosure ran over about five months:

* **April 18, 2026:** reported both flaws to OnePlus.
* **May 20:** OnePlus confirmed them, claimed sole control over disclosure, and warned of legal liability if he published.
* **June 22:** OnePlus gave an update on its fix and asked him to hold off, and he agreed not to publish before September 17.
* **July 20 and September 11:** he asked for updates and received no reply.
* **September 24:** he published.

Separately, this is not the only recent case of an installed app reaching root on flagship Android phones.

In August, Lukas Maar, a researcher at the security firm Calif, [showed a different technique](https://calif.io/research/oempocalypse) that took a no-permission app to root locked phones running the latest firmware from Samsung, Xiaomi, OPPO, OnePlus, and Realme by attacking code the makers add to Android.

OnePlus has also been slow to answer researchers before. In 2025, [Rapid7 reported](https://www.rapid7.com/blog/post/cve-2025-10184-oneplus-oxygenos-telephony-provider-permission-bypass-not-fixed/) a separate OxygenOS flaw that let any app read a user's texts, and said OnePlus did not respond until the research was public.

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messeng...