---
title: Linux io_uring PoC Rootkit Bypasses System Call-Based Threat Detection Tools
url: https://thehackernews.com/2025/04/linux-iouring-poc-rootkit-bypasses.html
source: The Hacker News
date: 2025-04-25
fetch_date: 2025-10-06T22:07:32.617198
---

# Linux io_uring PoC Rootkit Bypasses System Call-Based Threat Detection Tools

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

# [Linux io\_uring PoC Rootkit Bypasses System Call-Based Threat Detection Tools](https://thehackernews.com/2025/04/linux-iouring-poc-rootkit-bypasses.html)

**Apr 24, 2025**Ravie LakshmananEndpoint Security / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn0nAl5S-7wXqFII4llSXtsFiOF7BfaJirhAk_DP0T7pf2a9DcN1mV70N6d9PuS1xHuVafV6y44h1AAClU9egfqgFHyqaIgvzw5NV6w1C9gLSkirGstB_p1QuN3UcvBmYFHO8nVaSRSuAEwrI9jpO8BCL5z9Zx5uJtz9LOM5fXMbI-dbmJM8xNqKLCHr-R/s790-rw-e365/linux-tools.jpg)

Cybersecurity researchers have demonstrated a proof-of-concept (PoC) rootkit dubbed [Curing](https://github.com/armosec/curing) that leverages a Linux asynchronous I/O mechanism called [io\_uring](https://man7.org/linux/man-pages/man7/io_uring.7.html) to bypass traditional system call monitoring.

This causes a "major blind spot in Linux runtime security tools," ARMO said.

"This mechanism allows a user application to perform various actions without using system calls," the company [said](https://www.armosec.io/blog/io_uring-rootkit-bypasses-linux-security/) in a report shared with The Hacker News. "As a result, security tools relying on system call monitoring are blind' to rootkits working solely on io\_uring."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

io\_uring, first [introduced](https://blogs.oracle.com/linux/post/an-introduction-to-the-io-uring-asynchronous-io-framework) in Linux kernel version 5.1 in March 2019, is a Linux kernel system call interface that [employs](https://developers.redhat.com/articles/2023/04/12/why-you-should-use-iouring-network-io) two circular buffers called a submission queue (SQ) and a completion queue (CQ) between the kernel and an application (i.e., user space) to track the submission and completion of I/O requests in an asynchronous manner.

The rootkit devised by ARMO facilitates communication between a command-and-control (C2) server and an infected host to fetch commands and execute them without making any system calls relevant to its operations, instead making use of io\_uring to achieve the same goals.

ARMO's analysis of currently available Linux runtime security tools has revealed that both [Falco](https://github.com/falcosecurity/falco) and [Tetragon](https://github.com/cilium/tetragon) are blind to io\_uring-based operations owing to the fact that they are heavily reliant on system call hooking.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The security risks posed by io\_uring have been known for some time. In June 2023, Google [revealed](https://security.googleblog.com/2023/06/learnings-from-kctf-vrps-42-linux.html) that it decided to limit the use of the Linux kernel interface across Android, ChromeOS, and its production servers as it "provides strong exploitation primitives."

"On the one hand, you need visibility into system calls; on the other, you need access to kernel structures and sufficient context to detect threats effectively," Amit Schendel, Head of Security Research at ARMO, said.

"Many vendors take the most straightforward path: hooking directly into system calls. While this approach offers quick visibility, it comes with limitations. Most notably, system calls aren't always guaranteed to be invoked. io\_uring, which can bypass them entirely, is a positive and great example."

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

[Android](https://thehackernews.com/search/label/Android)[CrowdStrike](https://thehackernews.com/search/label/CrowdStrike)[Google](https://thehackernews.com/search/label/Google)[kernel exploit](https://thehackernews.com/search/label/kernel%20exploit)[linux](https://thehackernews.com/search/label/linux)[Microsoft Defender](https://thehackernews.com/search/label/Microsoft%20Defender)[rootkit](https://thehackernews.com/search/label/rootkit)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Co...