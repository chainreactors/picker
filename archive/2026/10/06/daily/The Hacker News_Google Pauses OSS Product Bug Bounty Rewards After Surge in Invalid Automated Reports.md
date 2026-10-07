---
title: Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports
url: https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.571288
---

# Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports](https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html)

**Swati Khandelwal**Oct 06, 2026Vulnerability / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCWoelMB7H9bFZJdDV7vP5M3a1ByvpHs8ub2SrBGOM1gz6r0Fg9cV1fplW5Q6mNBFtRlW99wDCSC-_6_sZBw0l4HsFvUDP5cCH2zmgcF4NK5wCOInv05K4hH2WMlKCA_G_psX4zB_hUcXid2MWx5fGDjaJvD1YjWBechwUdrhXK51dJYZ3PGsu0JQcT1U/s1700-nu-rw-lo-l85-e365/google-bug-bounty.jpg)

Google has stopped accepting product vulnerability reports through its bug bounty program for its open-source software.

The change, in effect since October 1, means researchers can no longer submit security flaws in the code of projects such as Go, Angular, and Protocol Buffers there for a reward. Reports about supply chain compromises are still accepted, and reports filed before October 1 are not affected.

Google called the stop temporary in a [post on X](https://x.com/GoogleVRP/status/2105689195180179605) on October 1 and said it was due to "a significant rise in automated submissions, the vast majority of which are not valid."

The post gave no figures. It did not say whether the submissions were produced with AI tools.

The [rules of the program](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules#product-vulnerabilities), called the Open Source Software Vulnerability Reward Program (OSS VRP), now carry a notice of the stop. It commits Google to an update in the first quarter of 2027 while it reworks this part of the program.

Neither the post nor the notice gives a date for accepting product vulnerability reports again.

Under the rules, a product vulnerability is a design or implementation flaw in Google's open source software. It must substantially affect the confidentiality or integrity of user data in software built with that code. Examples include memory corruption in file format parsers and path traversal.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The program sorts projects into four tiers based on their sensitivity. Only the top two, called flagship and important, had rewards listed for product vulnerabilities.

The same change that added the notice [removed those listed amounts](https://github.com/google/bughunters/commit/f8bf23ad82928bfa728214f20dc0af4fa13e310f): $500 to $7,500 for flagship projects and $101 to $3,133.7 for important ones. It was published to Google's public GitHub copy of the rules on September 30, a day before the X post.

[Google's list](https://github.com/google/bughunters/blob/main/oss-repository-tier/README.md) of tiered repositories, last updated in mid-September, names 26 flagship repositories and 47 important ones. The flagship tier includes Go, Angular, Flutter, Bazel, and Protocol Buffers.

Supply chain compromises, which are flaws that could let someone tamper with a project's source code or published packages, keep their listed rewards. So do other security issues, such as leaked credentials that give write access.

| Category | Flagship | Important | Standard |
| --- | --- | --- | --- |
| Supply chain compromises | $3,133.7 to $31,337 | $1,337 to $13,337 | $500 to $3,133.7 |
| Product vulnerabilities | None (was $500 to $7,500) | None (was $101 to $3,133.7) | None |
| Other security issues | $1,000 | $500 | None |

The fourth tier, for low-priority projects, has no listed rewards.

### Where Reports Can Go Now

Google's notice names three routes for researchers:

* **Cloud VRP:** Product vulnerability reports may still be accepted for some Google Cloud repositories that affect Google Cloud products, but the notice does not name them. Under the [Cloud VRP rules](https://bughunters.google.com/about/rules/google-friends/cloud-vulnerability-reward-program-rules), a flaw in an open source repository maintained by Google Cloud that affects Cloud products is rated at most IT3b. That is the tier for acquisitions and lower-priority products, and the cap applies unless Google's product list says otherwise.
* **Patch rewards:** The [Patch Rewards Program](https://bughunters.google.com/about/rules/open-source/patch-rewards-program-rules) pays $100 to $15,000 for security patches to the projects it covers, not for vulnerability reports. The project's maintainers must accept a patch and remain in place for one month before it can be submitted. A patch that fixes only a single vulnerability is reviewed on a case-by-case basis.
* **Other reward programs:** Google asks researchers to check whether a flaw affects something covered by one of its other reward programs and to submit it there. The OSS VRP rules also encourage reporting flaws in projects closely tied to Google Cloud or AI products to the Cloud VRP or the AI VRP.

The notice does not say whether Google will still take product vulnerability reports without a reward.

Some project policies point to other channels. Go [takes security reports by email](https://go.dev/doc/security/policy) to its own security team. A [security policy in Google's GitHub organization](https://github.com/google/.github/blob/master/SECURITY.md) sends reporters to Google's vulnerability reporting address, g.co/vulnz.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

[Angular's security policy](https://github.com/angular/angular/blob/main/SECURITY.md), as of October 6, says Angular is part of the OSS VRP, sends vulnerability reports to Google's Bug Hunters site, and names no other channel.

### Earlier Limits on Low-Quality Reports

Google [launched the OSS VRP](https://thehackernews.com/2022/08/google-launches-new-open-source-bug.html) in August 2022. In March 2026, it [began requiring stronger proof](https://bughunters.google.com/blog/ossvrp-rule-updates-2026) for reports in some tiers to filter o...