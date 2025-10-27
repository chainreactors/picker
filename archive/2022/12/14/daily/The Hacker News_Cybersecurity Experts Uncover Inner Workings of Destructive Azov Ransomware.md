---
title: Cybersecurity Experts Uncover Inner Workings of Destructive Azov Ransomware
url: https://thehackernews.com/2022/12/cybersecurity-experts-uncover-inner.html
source: The Hacker News
date: 2022-12-14
fetch_date: 2025-10-04T01:28:55.986274
---

# Cybersecurity Experts Uncover Inner Workings of Destructive Azov Ransomware

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

# [Cybersecurity Experts Uncover Inner Workings of Destructive Azov Ransomware](https://thehackernews.com/2022/12/cybersecurity-experts-uncover-inner.html)

**Dec 13, 2022**Ravie LakshmananData Security / Endpoint Security

[![Destructive Azov Ransomware](data:image/png;base64... "Destructive Azov Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi136glY86wsW1K5SryAUmWZYxzFdhtmy2nZ2EsXhFgUv7I3QZEYWBB_bes7vYRnclkj2-dL16HaC7earebSCtyDqJ2VUDvRbrrL_wbfsNMo9wwU7FiHR0Woao27ftda03J9YMa0ZShPyXSTTQEVxb-x02zL5_iyFBXGegebpE02b9do4HVj9gCkVdM/s790-rw-e365/wiper.png)

Cybersecurity researchers have published the inner workings of a new wiper called **Azov Ransomware** that's deliberately designed to corrupt data and "inflict impeccable damage" to compromised systems.

Distributed through another malware loader known as [SmokeLoader](https://thehackernews.com/2022/07/smokeloader-infecting-targeted-systems.html), the malware has been [described](https://research.checkpoint.com/2022/pulling-the-curtains-on-azov-ransomware-not-a-skidsware-but-polymorphic-wiper/) as an "effective, fast, and unfortunately unrecoverable data wiper," by Israeli cybersecurity company Check Point. Its origins have yet to be determined.

The wiper routine is set to overwrite a file's contents in alternating 666-byte chunks with random noise, a technique referred to as [intermittent encryption](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/) that's being increasingly leveraged by ransomware operators to evade detection and encrypt victims' files faster.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"One thing that sets Azov apart from your garden-variety ransomware is its modification of certain 64-bit executables to execute its own code," threat researcher Jiří Vinopal said. "The modification of executables is done using polymorphic code, so as not to be potentially foiled by static signatures."

Azov Ransomware also incorporates a logic bomb – a set of conditions that should be met before activating a malicious action – to detonate the execution of the wiping and backdooring functions at a predetermined time.

[![Destructive Azov Ransomware](data:image/png;base64... "Destructive Azov Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6q_Ap4aJ8545NdCNhiGDa-0O147_8sbRju1pl36Wms33--7gs5rvzRflQiWJPSp7f9AL7LLXd5Qvrlsgz9e0eO5pvMFcx7Puqed4K47_VXQCXbpfjGRxddtbIz4SXBZhIoIfpIkku3EZkqrVGquUVpet3_t60LLvycAiAzjqW2rzamw0F0OVzZ_4L/s790-rw-e365/wiper-malware.png)

"Although the Azov sample was considered skidsware when first encountered [...], when probed further one finds very advanced techniques — manually crafted assembly, injecting payloads into executables in order to backdoor them, and several anti-analysis tricks usually reserved for security textbooks or high-profile brand-name cybercrime tools," Vinopal added.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes amid a profusion of destructive wiper attacks since the start of the year. This includes [WhisperGate](https://thehackernews.com/2022/01/a-new-destructive-malware-targeting.html), [HermeticWiper](https://thehackernews.com/2022/02/new-wiper-malware-targeting-ukraine.html), [AcidRain](https://thehackernews.com/2022/04/russian-wiper-malware-responsible-for.html), [IsaacWiper](https://thehackernews.com/2022/03/second-new-isaacwiper-data-wiper.html), [CaddyWiper](https://thehackernews.com/2022/03/caddywiper-yet-another-data-wiping.html), [Industroyer2](https://thehackernews.com/2022/04/russian-hackers-tried-attacking.html), [DoubleZero](https://thehackernews.com/2022/03/us-government-warns-companies-of.html), [RURansom](https://thehackernews.com/2022/03/caddywiper-yet-another-data-wiping.html), and [CryWiper](https://thehackernews.com/2022/12/russian-courts-targeted-by-new-crywiper.html).

Last week, security firm ESET disclosed another previously unseen wiper called [Fantasy](https://thehackernews.com/2022/12/iranian-hackers-strike-diamond-industry.html) that's spread using a supply chain attack targeting an Israeli software company to target customers in the diamond industry. The malware has been linked to a threat actor called Agrius.

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

[encryption](https://thehackernews.com/search/label/encryption)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)[SmokeLoader](https://thehackernews.com/search/label/SmokeLoader)[wiper malware](https://thehackernews.com/search/label/wiper%20malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-ho...