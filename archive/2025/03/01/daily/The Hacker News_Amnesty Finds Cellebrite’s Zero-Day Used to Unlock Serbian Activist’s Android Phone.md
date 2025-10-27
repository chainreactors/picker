---
title: Amnesty Finds Cellebrite’s Zero-Day Used to Unlock Serbian Activist’s Android Phone
url: https://thehackernews.com/2025/02/amnesty-finds-cellebrites-zero-day.html
source: The Hacker News
date: 2025-03-01
fetch_date: 2025-10-06T22:01:45.427560
---

# Amnesty Finds Cellebrite’s Zero-Day Used to Unlock Serbian Activist’s Android Phone

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

# [Amnesty Finds Cellebrite's Zero-Day Used to Unlock Serbian Activist's Android Phone](https://thehackernews.com/2025/02/amnesty-finds-cellebrites-zero-day.html)

**Feb 28, 2025**Ravie LakshmananMobile Security / Zero-Day

[![Cellebrite's Zero-Day Exploit](data:image/png;base64... "Cellebrite's Zero-Day Exploit")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhf4g-SMzauU7AoANXasCQJWZ3ggBAs1-_HL5aXP6Vw8kf_ESVKTjOnWN0am_qLHCNYTOlQajxJmSUwLTiDzi_Cg5w2xu4PUdCd66EJItIYQyNjZQfmx1tfjuz56QUBA3tlGByU-2ab2H6pmZiGq0_eD1FapY58j1YFljL0uTaK8Sh_nfum8n1W7ycMVBaS/s790-rw-e365/phone-hacking.png)

A 23-year-old Serbian youth activist had their Android phone targeted by a zero-day exploit developed by Cellebrite to unlock the device, according to a new report from Amnesty International.

"The Android phone of one student protester was exploited and unlocked by a sophisticated zero-day exploit chain targeting Android USB drivers, developed by Cellebrite," the international non-governmental organization [said](https://securitylab.amnesty.org/latest/2025/02/cellebrite-zero-day-exploit-used-to-target-phone-of-serbian-student-activist/), adding traces of the exploit were discovered in a separate case in mid-2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The vulnerability in question is [CVE-2024-53104](https://thehackernews.com/2025/02/google-patches-47-android-security.html) (CVSS score: 7.8), a case of privilege escalation in a kernel component known as the USB Video Class (UVC) driver. A patch for the flaw was released for the Linux kernel in December 2024. It was subsequently addressed in Android earlier this month.

It's believed that CVE-2024-53104 was combined with two other flaws – CVE-2024-53197 and CVE-2024-50302 – both of which have been resolved in the Linux kernel. They are yet to be included in an Android Security Bulletin.

* **[CVE-2024-53197](https://lore.kernel.org/linux-cve-announce/2024122725-CVE-2024-53197-6aef%40gregkh/)** (CVSS score: N/A) - An out-of-bounds access vulnerability for Extigy and Mbox devices
* **[CVE-2024-50302](https://lore.kernel.org/linux-cve-announce/2024111908-CVE-2024-50302-f677%40gregkh/)** (CVSS score: 5.5) - A use of an uninitialized resource vulnerability that could be used to leak kernel memory

"The exploit, which targeted Linux kernel USB drivers, enabled Cellebrite customers with physical access to a locked Android device to bypass an Android phone's lock screen and gain privileged access on the device," Amnesty said.

"This case highlights how real-world attackers are exploiting Android's USB attack surface, taking advantage of the broad range of legacy USB kernel drivers supported in the Linux kernel."

The activist, who has been given the name "Vedran" to protect their privacy, was taken to a police station and his phone confiscated on December 25, 2024, after he attended a student protest in Belgrade.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Amnesty's analysis found that the exploit was used to unlock his Samsung Galaxy A32 and that the authorities attempted to install an unknown Android application. While the exact nature of the Android app remains unclear, the modus operandi is consistent with that of prior [NoviSpy spyware](https://thehackernews.com/2024/12/novispy-spyware-installed-on.html) infections reported in mid-December 2024.

Earlier this week, Cellebrite [said](https://cellebrite.com/en/cellebrite-statement-about-amnesty-international-report/) its tools are not designed to facilitate any type of offensive cyber activity and that it works actively to curtail the misuse of its technology.

The Israeli company also said it will no longer allow Serbia to use its software, stating "we found it appropriate to stop the use of our products by the relevant customers at this time."

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

[Android](https://thehackernews.com/search/label/Android)[Cellebrite](https://thehackernews.com/search/label/Cellebrite)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[digital forensics](https://thehackernews.com/search/label/digital%20forensics)[Human Rights](https://thehackernews.com/search/label/Human%20Rights)[Linux kernel](https://thehackernews.com/search/label/Linux%20kernel)[mobile security](https://thehackernews.com/search/label/mobile%20security)[surveillance](https://thehackernews.com/search/label/surveillance)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernew...