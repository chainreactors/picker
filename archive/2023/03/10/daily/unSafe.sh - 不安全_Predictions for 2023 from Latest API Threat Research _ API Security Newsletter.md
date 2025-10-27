---
title: Predictions for 2023 from Latest API Threat Research | API Security Newsletter
url: https://buaq.net/go-152769.html
source: unSafe.sh - 不安全
date: 2023-03-10
fetch_date: 2025-10-04T09:05:29.285411
---

# Predictions for 2023 from Latest API Threat Research | API Security Newsletter

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/35472825c6576b3b33b7603bf13974c4.jpg)

Predictions for 2023 from Latest API Threat Research | API Security Newsletter

March has arrived and is roaring like a very confused lion, at least in the northern hemisphe
*2023-3-9 21:10:48
Author: [lab.wallarm.com(查看原文)](/jump-152769.htm)
阅读量:40
收藏*

---

March has arrived and is roaring like a very confused lion, at least in the northern hemisphere. And much like in the wild, brood production is increasing. We’ve already seen some fruits of that labor, such as the Q4-2022 and 2022 Year-End ThreatStats™ Report, and some very tasty product upgrades. Read on for this month’s bit o’ honey.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Note-from-Ivan.png?resize=260%2C90&ssl=1)

Greetings everyone!

We’ve been keeping an eye on the API threat landscape, and some notable API vulnerabilities that you should be aware of. But don’t worry, we’re here to help with our latest threat research and product updates.

Our recent API vulnerability, exploit and attack data analysis has yielded both [Q4-focused results](https://lab.wallarm.com/q4-2022-api-threatstats-report/) and a [2022 year-end review](https://lab.wallarm.com/2022-year-end-api-threatstats-report/), with predictions for 2023 including continued rise in API vulnerabilities, growth in API attacks, and worsening time-to-exploit window.

As you’ll also learn from the report, OWASP API Security Top-10 does not perfectly cover real API exploits; therefore, we’re hoping the new one will be much better. To learn more about the recently released first draft and what to expect of OWASP API Top-10 2023, join us on March 16th for what promises to be [a lively webinar](https://www.wallarm.com/webinars/new-2023-owasp-api-security).

On the product front, we’re continuing to release improvements to ensure users are getting the best end-to-end security for their APIs. We’ve recently dropped enhancements in API Discovery (which is really all about security posture), and SSRF protection. Find the details below.

As a spoiler, this month you will also find my API security predictions for 2023 in an upcoming Forbes article. I’m expecting that API token leaks will be part of kill-chains which will result in different types of attacks in 2023. I also expect to see an increase in API abuse attacks due to authentication and authorization issues, as well as a rise in data decoding attacks targeting APIs. My thoughts are based on vulnerability, exploit & attack data analyzed in our [2022 Year-End ThreatStats™ Report](https://www.wallarm.com/resources/2022-year-end-api-threatstats-full-report), and the many data breaches which happened last year.

 – Ivan, CEO & Co-Founder, Wallarm

PS – Stay up-to-the-minute on all the latest news about [#apisecurity](https://www.linkedin.com/feed/hashtag/?keywords=apisecurity&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A6999039478417825792) exploits and updates by following our new [**API ThreatStats LinkedIn page**](https://www.linkedin.com/company/threatstats/).

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Wallarm-News-header.png?resize=768%2C116&ssl=1)

**Wallarm news**

The 2022 API vulnerability, exploit and attack data have been crunched and the latest **API ThreatStats™ Report** season is complete. The team provided both Q4-focused results and, perhaps more importantly, a 2022 year-end review. Lots to explore, including:

* Q4-2022 [blog post](https://lab.wallarm.com/q4-2022-api-threatstats-report/) and [infographic](https://hubspot.wallarm.com/hubfs/Q4%20API%20ThreatStats%28TM%29%20infographic.pdf)
* YE-2022 [blog post](https://lab.wallarm.com/2022-year-end-api-threatstats-report/), [report](https://www.wallarm.com/resources/2022-year-end-api-threatstats-full-report) and [on-demand webinar](https://www.wallarm.com/webinars/api-threatstats-2022-and-q4)

Too much to recap here, but be sure to read check out our predictions for 2023, including:

* Continued rise in API vulnerabilities, in numbers and severity.
* Unceasing growth in API attacks, which will lead to even more breaches.
* Worsening time-to-exploit window, which will put even more pressure on security and DevOps teams.

![](https://lh5.googleusercontent.com/GCSq7XayB8A-s41hDf-6XbJ1OY-jdYm0YGt6nsozzGB2pzwIar9ga6v4AKT3ppFyPjJ9HdQcWFgoyX89SfMuAaUHX0dOzMh_poqHnuU-mDBNjTYhOGMxvB9CJXNgTTT8B2R0aGbV3-lMI7nYgfCgj_A)

Read the 2022 year-end collection to know what to prepare for, and look at the Q4-2022 collection to learn how we got here. Dig In!

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Product-News-header.png?resize=768%2C116&ssl=1)

The hive has served up some sweet ambrosia for Wallarm users in the past month.

![](https://lh4.googleusercontent.com/0pZnqkSuEmML5zjJDqrJNd6JFRDpG16vI3DDzZO_eWRCKqmRnHaESaJxoxyH8SJj9z_MNKaNZOAczysuxR92Vgg5vsOZDbzMZ27thiNGtlKyXhJFWzJJjv8uRV4NzV5cjpMEoNOQadqN455HqdijhZk)

**API Discovery Dashboard Upgrades**

With this update, you can now more easily monitor sensitive data (to maintain compliance), track API changes (to monitor drift), identify risky endpoints (to reduce your API attack surface), and more. Read more in [this changelog entry](https://changelog.wallarm.com/introducing-the-wallarm-api-discovery-dashboard-12HrJ6).

**SSRF Attack Mitigation**

Server-Side Request Forgery (SSRF) attacks can allow malicious actors to read server configurations, connect to internal services, perform unintended post requests, or circumvent input validation. With this update, which requires Node v 4.4.3, you can now more easily protect against this attack vector. Read more in [this changelog entry](https://changelog.wallarm.com/ssrf-mitigation-for-mission-critical-apis-with-wallarm-last-update-NTPws).

**Did You Know?** You can subscribe to our [**update announcements**](https://changelog.wallarm.com/) to keep up-to-date with the latest product news.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Events-header.png?resize=768%2C116&ssl=1)

**Upcoming:**

***Webinar*** [*Mar 16, 2023*] — [A CISOs Guide To The New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/new-2023-owasp-api-security)

Join our upcoming webinar as we explore the new Top-10 API risks Release Candidate (RC) for 2023, and the implications of these updates to your API security posture.

[![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/text-1.png?resize=256%2C45&ssl=1)](https://www.wallarm.com/webinars/new-2023-owasp-api-security)

**Past:**

***Webinar*** [*on-demand*] — [API ThreatStats™ Report: 2022 Year-in-Review & Q4 Results](https://www.wallarm.com/webinars/api-threatstats-2022-and-q4)

The Wallarm Research team looked through all published API vulnerabilities and exploits for 2022 and aggregated these into our year-end report. Watch our recording of our recap of the highlights and trends we saw in 2022, and hear our predictions for what’s to come in 2023.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Notable-vulns-header.png?resize=768%2C116&ssl=1)

[**VMware NSX Manager Vulnerabilities Being Actively Exploited in the Wild**](https://lab.wallarm.com/vmware-nsx-manager-vulnerabilities-being-actively-exploited-in-the-wild/)

Read this write-up from the Wallarm Detect team regarding exploit attempts in the wild of [CVE-2022-31678](https://nvd.nist.gov/vuln/detail/CVE-2022-31678) (CVSS score: 9.1) and [CVE-2021-39144](https://nvd.nist.gov/vuln/detail/CVE-2021-39144) (CVSS score: 8.5) impacting [VMware NSX Manager](https://www.vmware.com/products/nsx.html). If successfully exploited, the imp...