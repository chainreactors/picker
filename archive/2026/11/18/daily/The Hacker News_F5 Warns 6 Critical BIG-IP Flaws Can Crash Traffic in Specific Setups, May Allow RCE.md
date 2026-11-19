---
title: F5 Warns 6 Critical BIG-IP Flaws Can Crash Traffic in Specific Setups, May Allow RCE
url: https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:34.036893
---

# F5 Warns 6 Critical BIG-IP Flaws Can Crash Traffic in Specific Setups, May Allow RCE

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

# [F5 Warns 6 Critical BIG-IP Flaws Can Crash Traffic in Specific Setups, May Allow RCE](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)

**Swati Khandelwal**Nov 18, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizE3X3tUSPpxIYnNyM91hyphenhyphenzZOS6jjdHnCLmubn4upOYKZn3MdjUqJQGEjIBGtZ2JHK6yggH6RxSQCANhtF7-zIWJ0EfGqA7iY2KQWM7vtoiCsc-_KeFZeHeDm-TOpM_oL_EVzOvPru_cMVzx3wJL8kaLEgXuzPzxm3iYnTiyu57quhgBgMY1Nb7V_sXG4/s1700-nu-rw-lo-l85-e365/f5.png)

Six critical vulnerabilities in **F5** BIG-IP allow an attacker to crash the Traffic Management Microkernel (TMM) without logging in, disrupting traffic until the TMM restarts.

Each flaw needs a specific setup on a virtual server: an iRule that uses a particular command, or an APM policy that includes two particular kinds of agent.

F5, which makes **BIG-IP**, disclosed the flaws today and says they may also allow remote code execution. The company has released engineering hotfixes and lists no workaround.

The company rates all six 9.8 under CVSS v3.1 and 9.3 under CVSS v4.0. They are stack-based buffer overflows in BIG-IP's data plane, the part that processes almost all of its network traffic. The management side is not exposed, according to the company.

None of the company's advisories says the flaws have been exploited. WatchTowr researcher Sina Kheirkhah reported four, and the company found the other two itself.

Five of the flaws are in iRules, a BIG-IP feature that administrators use to manage traffic, and one is in BIG-IP's APM module. Some also affect BIG-IP Next for Kubernetes and BIG-IP CNF, part of the company's BIG-IP Cloud-Native Edition.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Each flaw needs the setup listed below on a virtual server:

* **CVE-2026-123637**: an APM per-request policy that includes both the Client Information agent and Endpoint Security agents. Affects BIG-IP APM only.
* **CVE-2026-121805**: an iRule that uses PEM::subscriber on client traffic. Affects BIG-IP PEM, BIG-IP Next for Kubernetes and, as of today, BIG-IP CNF.
* **CVE-2026-120292**: an HTTP profile and an iRule that uses MR::message route. Affects BIG-IP (all modules) and BIG-IP Next for Kubernetes.
* **CVE-2026-120285**: an HTTP profile and an iRule that uses PSC::ip\_address. Affects BIG-IP (all modules), BIG-IP Next for Kubernetes and, as of today, BIG-IP CNF.
* **CVE-2026-116953**: an iRule that uses GENERICMESSAGE::route on client traffic. Affects BIG-IP (all modules) and BIG-IP Next for Kubernetes.
* **CVE-2026-120722**: an iRule that uses DNS::scrape on client traffic. Affects BIG-IP DNS and BIG-IP Next for Kubernetes. The company's advisory lists BIG-IP CNF as not vulnerable, but its CVE record, updated today, lists CNF as affected.

F5's [security notification](https://my.f5.com/manage/s/article/K000164058) lists the 22 advisories it published today, including 10 for NGINX.

For the six critical flaws, the only fixes are engineering hotfixes, builds that the company issues between its normal software releases. No scheduled release is listed as a fix, and the advisories provide no workaround until a hotfix is installed.

The company warns that "engineering hotfixes do not undergo the extensive QA assessment of scheduled software releases." Its [hotfix policy](https://my.f5.com/manage/s/article/K4918) adds that they come with no warranty or promise that they will work.

A system on a custom engineering hotfix needs a new one from the company's support team.

BIG-IP Next for Kubernetes is fixed in BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 and BNK-2.2.5-EHF1, for versions 2.4.0 to 2.4.2, 2.3.0 to 2.3.4 and 2.2.0 to 2.2.5. BIG-IP CNF, on the same version ranges, is fixed in CNF-2.4.2-EHF1, CNF-2.3.4-EHF1 and CNF-2.2.5-EHF1 for CVE-2026-121805 and CVE-2026-120285.

The company checks only versions that are still within technical support, so an older release missing from its tables has not been shown to be safe.

Today's flaws differ from **CVE-2026-94127**, an [APM flaw](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html) that F5 disclosed on September 22 and that was later exploited. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added it to its Known Exploited Vulnerabilities catalog the same day.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

That flaw is a heap-based buffer overflow in APM setups that serve as OAuth authorization servers, allowing attackers to run code without logging in. Today's six are stack-based overflows that need different settings.

### Six Other BIG-IP and BIG-IQ Flaws

Today's advisories also cover six lower-rated flaws in BIG-IP and BIG-IQ, each with its own fix. The scores below are CVSS v3.1:

* **CVE-2026-125274** (iControl SOAP, 8.8): A user with network access and at least the Guest role can send an unauthorized management request. The company says this may allow them to run system commands, create or delete files, or disable services. It is fixed in BIG-IP 21.1.0.3, 17.5.1.10 and 17.1.3.6, and in BIG-IQ 8.4.2.3. Until then, the [SOAP advisory](https://my.f5.com/manage/s/article/K000163936) explains how to limit iControl SOAP access to trusted networks and warns that blocking it on self-IP addresses may break high-availability setups.
* **CVE-2026-120718** (iControl REST, 8.1): iControl REST tokens may not expire as expected. An attacker who already holds a token may be able to extend how long it stays valid unless its owner deletes it. It is fixed in BIG-IP 21.1.0.2, 17.5.1.10, and 17.1.3.6. As a workaround, scripts that create tokens can be changed to delete them when they are no longer needed.
* **CVE-2026-125272** (APM, 7.5): When an APM access profile on a virtual server has a per-request policy with a form-based Logon Page, an attacker can crash TMM without logging in. It is fixed in t...