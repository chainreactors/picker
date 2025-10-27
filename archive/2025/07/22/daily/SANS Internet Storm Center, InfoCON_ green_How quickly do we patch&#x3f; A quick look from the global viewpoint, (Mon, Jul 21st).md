---
title: How quickly do we patch&#x3f; A quick look from the global viewpoint, (Mon, Jul 21st)
url: https://isc.sans.edu/diary/rss/32126
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-22
fetch_date: 2025-10-06T23:51:19.953434
---

# How quickly do we patch&#x3f; A quick look from the global viewpoint, (Mon, Jul 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32122)
* [next](/diary/32128)

# [How quickly do we patch? A quick look from the global viewpoint](/forums/diary/How%2Bquickly%2Bdo%2Bwe%2Bpatch%2BA%2Bquick%2Blook%2Bfrom%2Bthe%2Bglobal%2Bviewpoint/32126/)

**Published**: 2025-07-21. **Last Updated**: 2025-07-21 11:03:12 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/How%2Bquickly%2Bdo%2Bwe%2Bpatch%2BA%2Bquick%2Blook%2Bfrom%2Bthe%2Bglobal%2Bviewpoint/32126/#comments)

Since the ongoing “ToolShell” exploitation campaign, in which threat actors attack on-premise Sharpoint servers using a chain of two recently published vulnerabilities[[1](https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/),[2](https://www.cisa.gov/news-events/alerts/2025/07/20/microsoft-releases-guidance-exploitation-sharepoint-vulnerability-cve-2025-53770),[3](https://research.eye.security/sharepoint-under-siege/)], is still on top of the cyber security news[[4](https://www.bleepingcomputer.com/news/microsoft/microsoft-sharepoint-zero-day-exploited-in-rce-attacks-no-patch-available/),[5](https://thehackernews.com/2025/07/critical-microsoft-sharepoint-flaw.html),[6](https://www.securityweek.com/sharepoint-under-attack-microsoft-warns-of-zero-day-exploited-in-the-wild-no-patch-available/),[7](https://www.helpnetsecurity.com/2025/07/20/microsoft-sharepoint-servers-under-attack-via-zero-day-vulnerability-with-no-patch-cve-2025-53770/)], I thought it might be a good time to look at the question of how quickly do we – as a global society – actually patch actively-exploited vulnerabilities when it comes to our internet-facing systems.

![](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2021-31207.png)

While this is admittedly a very complex topic, and in order to arrive at any detailed conclusions, an in-depth, long-term study would be needed, I believe that even a quick look at available data may show us some general (and hopefully interesting) trends.

Since I - on my own - lack the ability to periodically scan the entire internet and identify how many systems are affected and/or patched when it comes to specific vulnerability, I decided to use data gathered from Shodan using my TriOp tool[[8](https://isc.sans.edu/diary/27034)] over the past 30 months. Specifically, I looked at the number of systems that Shodan detected as “vulnerable” to any vulnerability listed in the CISA KEV catalog[[9](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)] each day during that timeframe.

It should be mentioned at this point that Shodan is not capable of detecting all of the KEV vulnerabilities (of the approximately 1380 vulnerabilities currently listed in the KEV, it seems to be able to identify only between 200 and 250) and that even for those vulnerabilities it detects, the mechanisms it uses to identify whether a specific system is vulnerable are passive in nature. Therefore, the resulting numbers are – by necessity – not exact, since there is a significant potential for false-positive (or false-negative) identification. Nevertheless, this data still provides a good starting point.

From all the data, I removed CVEs for which Shodan detected less than 50 vulnerable systems (or – to be more exact – 50 public IP addresses) and then generated time charts for all of the rest.

Based on a quick visual analysis, it appears that (if we gloss over the sharp sudden decreases/increases that Shodan is prone to – see e.g. [[10](https://isc.sans.edu/diary/SSL%2B20%2Bturns%2B30%2Bthis%2BSunday%2BPerhaps%2Bthe%2Btime%2Bhas%2Bcome%2Bto%2Blet%2Bit%2Bdie/31664)] – and omit other Shodan-introduced artifacts, such as sharp increases in detections most likely associated with new detection analytics) for most vulnerabilities, the number of affected systems decreases over time in more or less linear fashion, with a tendency to slowly level out… As you may see below, in some cases, the rate of decrease is slower than in others, which may be due to slower patching or due to Shodan (at least partially) not being able to recognize backported patches.

[![](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2019-0211.png)](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2019-0211.png)

Data for [CVE-2019-0211](https://nvd.nist.gov/vuln/detail/cve-2019-0211)

[![](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2022-0028.png)](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2022-0028.png)

Data for [CVE-2022-0028](https://security.paloaltonetworks.com/CVE-2022-0028)

[![](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2023-20109.png)](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2023-20109.png)

Data for [CVE-2023-20109](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-getvpn-rce-g8qR68sx.html)

Although for some vulnerabilities, there were occasions when a sharper short-term decrease was visible in the number of vulnerable systems, these were always explainable not by increased patching but by removal of systems that reached their “end of life” from production environments.

This effect can be clearly seen in chart for an Exchange vulnerability CVE-2021-31207 (and in charts for two other Exchange vulnerabilities - CVE-2021-34523 and CVE-2021-34473), where we may observe a significant decrease of vulnerable IP addresses detected by Shodan starting at the end of April 2023 and ending in the early May 2023. This decrease is almost certainly related to the fact that Microsoft ended support for Exchange 2013 (which was affected by the vulnerability/vulnerabilities)  on April 11, 2023[[11](https://learn.microsoft.com/en-us/troubleshoot/exchange/administration/exchange-2013-end-of-support)].

[![](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2021-31207.png)](https://isc.sans.edu/diaryimages/images/25-07-21-cve-2021-31207.png)

Data for [CVE-2021-31207](https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-31207)

To sum up, although we need to take the Shodan numbers with a grain of salt, and although vulnerabilities in CISA KEV may not necessarily be the most important ones from everyone’s perspective, from what we’ve shown, it seems that even in July of 2025, the answer to the question of “How quickly do we patch?” is still “Not nearly quickly enough!”.

And while we’ve historically seen cases of vulnerabilities, where patching was relatively fast and the remaining “vulnerable population” was nearly insignificant (such as CVE-2019-19781 AKA “Shitrix”)[[12](https://isc.sans.edu/diary/26900)], these – sadly – still seem to be the exception, rather than the rule…

[1] <https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/>
[2] <https://www.cisa.gov/news-events/alerts/2025/07/20/microsoft-releases-guidance-exploitation-sharepoint-vulnerability-cve-2025-53770>
[3] <https://research.eye.security/sharepoint-under-siege/>
[4] <https://www.bleepingcomputer.com/news/microsoft/microsoft-sharepoint-zero-day-exploited-in-rce-attacks-no-patch-available/>
[5] <https://thehackernews.com/2025/07/critical-microsoft-sharepoint-flaw.html>
[6] <https://www.securityweek.com/sharepoint-under-attack-microsoft-warns-of-zero-day-exploited-in-the-wild-no-patch-available/>
[7] <https://www.helpnetsecurity.com/2025/07/20/microsoft-sharepoint-servers-under-attack-via-zero-day-vulnerability-with-no-patch-cve-2025-53770/>
[8] <https://isc.sans.edu/diary/27034>
[9] <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>
[10] [https://isc.sans.edu/diary/SSL+20+turns+30+this+Sunday+Perhaps+the+time+has+come+to+let+it+die/31664](https://isc.sans.edu/diary/SSL%2B20%2Bturns%2B30%2Bthis%2BSunday%2BPerhaps%2Bthe%2Btime%2Bhas%2Bcome%2Bto%2Blet%2Bit%2Bdie/31664)
[11]...