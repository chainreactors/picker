---
title: Smash-and-Grab Extortion
url: https://thehackernews.com/2024/07/smash-and-grab-extortion.html
source: The Hacker News
date: 2024-07-11
fetch_date: 2025-10-06T17:47:30.195644
---

# Smash-and-Grab Extortion

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

# [Smash-and-Grab Extortion](https://thehackernews.com/2024/07/smash-and-grab-extortion.html)

**Jul 10, 2024**The Hacker NewsIoT Security / Firmware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS1TaKtahwUsHEaubtAF8fUdsFtthbkCPizSN5tbkRscJy8VEmRJpbfXajV9blIkLQGReEIJZfHGgb4HlHpkwbR64VNYOy47-dXxqiORGG2idD9nbMmjm9Q00mmzFYDgAlzh1GJtTbhhTGzsPA9i-S-jeoTdpSF5LqETg4VawByTebwgDQjHQ4KOe4OpwO/s790-rw-e365/chip.png)

## **The Problem**

The "2024 Attack Intelligence Report" from the staff at Rapid7 [1] is a well-researched, well-written report that is worthy of careful study. Some key takeaways are:

1. 53% of the over 30 new vulnerabilities that were widely exploited in 2023 and at the start of 2024 were *zero-days*.
2. More mass compromise events arose from zero-day vulnerabilities than from n-day vulnerabilities.
3. Nearly a quarter of widespread attacks were zero-day attacks where a single adversary compromised dozens to hundreds of organizations simultaneously.
4. Attackers are moving from initial access to exploitation in minutes or hours rather than days or weeks.

So the conventional patch and put strategy is as effective as a firetruck showing up after a building has burned to the ground! Of course, patch and put could prevent future attacks, but taking into account that patch development takes from days to weeks [2] and that the average time to apply critical patches is 16 days [3], devices are vulnerable for a long time after the zero-day has become public knowledge. This allows smaller actors to get their share of the meat, much like the vultures they are. In view of Rapid7's report, something different must be done to protect IoT and other vulnerable devices.

## **How Firmware Comes To Be**

"Software Bills of Materials for IoT and OT devices" by IoTSF is another excellent read. I was surprised to learn that "Modern software is rarely created from scratch but rather it integrates a relatively small amount of new code with tens, hundreds, or even thousands of pre-existing components …". In the old days (circa 2015) we wrote our own firmware, but not anymore. Now, according to the authors, IoT firmware is assembled from mostly open source components that are riddled with vulnerabilities. This is not a step forward for device security!

According to the IoTSF authors, components bring in more components, each with more vulnerabilities. Also according to them, creating accurate SBOMs is difficult, and identifying all of the vulnerabilities in an SBOM is even more difficult. So security teams are faced with inadequate SBOMs and the task of deciding which vulnerabilities are exploitable, then fixing those vulnerabilities. According to other reports, the number of vulnerabilities and the complexity of IoT firmware are growing rapidly year by year. Keeping up with patches seems to be a hopeless treadmill. No wonder security teams are getting burned out.

## **Chilling Exploits**

Zero-days are especially concerning because many state actors have inventories of them that are ready to be used as weapons [4]. We tend to think of exploits as data exfiltrations or ransomware attacks. However, these are not the whole story. In 2007 at Idaho National Laboratory it was decided to test if malware could damage a full-size electricity generator [5]. The malware controlled a relay that connected or disconnected the generator from the power grid. By exercising a sequence of connects and disconnects, the malware was able to cause the generator to destroy itself.

The result was not repairable damage, but rather scrap metal that could only be melted down to manufacture a new generator. The generator was destroyed in under a minute. Thus malware running on a tiny MCU was able to destroy a large machine. What if a bad actor could destroy 10% of the electricity generators in the U.S.? How long would it take to manufacture and install replacement generators? What would happen in the meantime?

## **We Need a Better Solution**

We must recognize that patching and putting is not sufficient to deal with emerging new threats and the weaponized threats detailed above.

Isolating vulnerable firmware is the better solution. This is amply demonstrated by Green Hills's Integrity for aerospace, BlackBerry's QNX for automotive, and several "separation kernels" by other companies. However, the problem with these solutions is that they require power-hungry processors, and isolation is at the process level using memory management units (MMUs). IoT devices generally require low-power microcontrollers (MCUs), their firmware is normally comprised of but a single process and they are limited to memory protection units (MPUs). What is needed is more granular isolation (i.e. at the task level) that works for MCUs.

## **We Have Such a Solution**

We have demonstrated that isolated partitioning is practical for Cortex-M based MCUs (which comprise about 80% of all MCUs in production). In addition, the *pmode barrier* provided by this architecture provides additional protection for mission-critical and other trusted code. Such code needs only minimal modification for partitioning. The following figure illustrates the basics of Cortex-M partitioning and how it fits into the overall security picture:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgowOutV6bdycO2VCl1sz4aXU3ogQ8MK6LD7Iu_WxNw7ESF2dAnzqkxtQk69JWkecnlpRUawfn1qYPJgrZyN3cZMYeXafuwV7DAy6QRvw1o3QNnBTOvpISo-vRllgi9F8xSIZNF-5PnafduGV22xtGlneZn5JEBXvrVOckVFedaQgDm7KGpzJ-WDNeFYUk/s790-rw-e365/ms.png)

As shown, mission-critical firmware, security firmware, and handler mode (hmode) firmware are protected by the pmode barrier and run in privileged mode (pmode) or hmode. Vulnerable application firmware, SOUP, and middleware are above the pmode barrier and run in unprivileged mode (umode). Firmware in umode can access pmode or hmode only via exceptions caused by faults or via the SVC exception, which is used for system service...