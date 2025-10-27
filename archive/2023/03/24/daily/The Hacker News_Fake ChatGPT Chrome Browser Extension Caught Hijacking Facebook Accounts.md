---
title: Fake ChatGPT Chrome Browser Extension Caught Hijacking Facebook Accounts
url: https://thehackernews.com/2023/03/fake-chatgpt-chrome-browser-extension.html
source: The Hacker News
date: 2023-03-24
fetch_date: 2025-10-04T10:32:46.878384
---

# Fake ChatGPT Chrome Browser Extension Caught Hijacking Facebook Accounts

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Fake ChatGPT Chrome Browser Extension Caught Hijacking Facebook Accounts](https://thehackernews.com/2023/03/fake-chatgpt-chrome-browser-extension.html)

**Mar 23, 2023**Ravie LakshmananBrowser Security / Artificial Intelligence

[![ChatGPT Chrome Browser Extension](data:image/png;base64... "ChatGPT Chrome Browser Extension")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_vl3iveKduJHDN_hYWW1wM2rvsY3U6jWelLB9a2WX-NZ87m1DbXoRwHBwVFOP0twNOzF-s0r68n8kF1tWbIirxEw_JKXOwlKHCQbdjtgERTzFXxt7YqC4EUuFX2oLlFnn1Zzy_fPyjoA9EPblYb8HjvEvqYLxH2lBNL5DqMrKdsKRUZRczrK2D6PE/s790-rw-e365/chatgpt.png)

Google has stepped in to remove a bogus Chrome browser extension from the official Web Store that masqueraded as OpenAI's ChatGPT service to harvest Facebook session cookies and hijack the accounts.

The "ChatGPT For Google" extension, a trojanized version of a [legitimate open source browser add-on](https://github.com/wong2/chatgpt-google-extension), attracted over 9,000 installations since March 14, 2023, prior to its removal. It was originally uploaded to the Chrome Web Store on February 14, 2023.

According to [Guardio Labs](https://labs.guard.io/fakegpt-2-open-source-turned-malicious-in-another-variant-of-the-facebook-account-stealer-d00ef9883d61) researcher Nati Tal, the extension was propagated through [malicious](https://thehackernews.com/2023/03/lookalike-telegram-and-whatsapp.html) [sponsored Google search results](https://thehackernews.com/2023/03/new-dotrunpex-malware-delivers-multiple.html) that were designed to redirect unsuspecting users searching for "Chat GPT-4" to fraudulent landing pages that point to the fake add-on.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Installing the extension adds the promised functionality – i.e., enhancing search engines with ChatGPT – but it also stealthily activates the ability to capture Facebook-related cookies and exfiltrate it to a remote server in an encrypted manner.

Once in possession of the victim's cookies, the threat actor moves to seize control of the Facebook account, change the password, alter the profile name and picture, and even use it to disseminate extremist propaganda.

[![ChatGPT Chrome Browser](data:image/png;base64... "ChatGPT Chrome Browser")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIlQEMB6xiJtX3FTsvGxlBnvH7tE5ONp1IFGRoSLFWwSrapDH27npvu51zoP-3l_nk4So7r19Btk-4eJmqAefixqpMKsNbQU8WMwjtla33XIToezLL45pkN-Czfz1Um5GbQiAnsFN39r7uixPr2K099mcYmqL3eD-rp2JJMbC0C-iLzUEMJR_uKn8k/s790-rw-e365/chatgpt.png)

The development makes it the second fake ChatGPT Chrome browser extension to be discovered in the wild. The [other extension](https://thehackernews.com/2023/03/fake-chatgpt-chrome-extension-hijacking.html), which also functioned as a Facebook account stealer, was distributed via sponsored posts on the social media platform.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

If anything, the findings are yet another proof that cybercriminals are capable of swiftly adapting their campaigns to cash in on the popularity of ChatGPT to distribute malware and stage opportunistic attacks.

"For threat actors, the possibilities are endless — using your profile as a bot for comments, likes, and other promotional activities, or creating pages and advertisement accounts using your reputation and identity while promoting services that are both legitimate and probably mostly not," Tal said.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Browser Extension](https://thehackernews.com/search/label/Browser%20Extension)[ChatGPT](https://thehackernews.com/search/label/ChatGPT)[chrome browser](https://thehackernews.com/search/label/chrome%20browser)[OpenAI](https://thehackernews.com/search/label/OpenAI)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Network...