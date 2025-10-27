---
title: One Year Since Log4Shell: Lessons Learned for the next ‘code red’
url: https://blog.fox-it.com/2022/12/12/one-year-since-log4shell-lessons-learned-for-the-next-code-red/
source: Fox-IT International blog
date: 2022-12-13
fetch_date: 2025-10-04T01:17:40.911850
---

# One Year Since Log4Shell: Lessons Learned for the next ‘code red’

[Skip to content](#content)

[![Fox-IT International blog](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/06/Fox-logo-for-wordpress-blog-2.png?fit=180%2C49&ssl=1)](https://blog.fox-it.com/)

[Fox-IT International blog](https://blog.fox-it.com/)

News and opinions from Fox-IT

Menu

* [Home](http://blog.fox-it.com/)
* [Archive](https://blog.fox-it.com/archive/)
* [Back to Fox-IT](http://www.fox-it.com)

# One Year Since Log4Shell: Lessons Learned for the next ‘code red’

[Fox-SRT](https://blog.fox-it.com/author/foxsrt/ "Posts by Fox-SRT")

[Uncategorized](https://blog.fox-it.com/category/uncategorized/)

December 12, 2022
14 Minutes

**Authored by** Edwin van Vliet and Max Groot

One year ago, Fox-IT and NCC Group released their blogpost detailing findings on detecting & responding to exploitation of CVE-2021-44228, better known as ‘Log4Shell’. Log4Shell was a textbook example of a code red scenario: exploitation was trivial, the software was widely used in all sorts of applications accessible from the internet, patches were not yet available and successful exploitation would result in remote code execution. To make matters worse, advisories heavily differed in the early hours of the incident, resulting in conflicting information about which products were affected.

Due to the high-profile nature of Log4Shell, the vulnerability quickly drew the attention of both attackers and defenders. This wasn’t the first time such a ‘perfect storm’ has taken place, and it will definitely not be the last one. This 1-year anniversary seems like an appropriate time to look back and reflect on what we did right and what we could do better next time.

Reflection firstly requires us to critically look at ourselves. Thus, in the first part of this blog we will look back at how our own Security Operations Center (SOC) tackled the problem in the initial days of the ‘code red’. What challenges did we face, what solutions worked, and what lessons will we apply for the next code red scenario?

The second part of this blog discusses the remainder of the year. Our CIRT has since been contacted by several organizations that were exploited using Log4Shell. Such cases ranged from mere coinminers to domain-wide ransomware, but there were several denominators between those cases that provide insight in how even a high-profile vulnerability such as Log4Shell can go by unnoticed and result in a compromise further down the line.

## SOC perspective: From quick wins to long term solutions

Within our SOC we are tasked with detecting attacks and informing monitored customers with actionable information in a timely manner. We do not want to call them for generic internet noise, and they expect us to only call when a response on their end is necessary. We have a role that is restricted to monitoring: we do not segment, we do not block, and we do not patch. During the Log4Shell incident, our primary objective was to keep our customers secure by identifying compromised systems quickly and effectively.

The table below summarizes the most important actions we undertook in response to the emergency of the Log4Shell vulnerability. We will reflect further on these events to discuss why we took certain decisions, as well as consider what we could have done differently and what we did right.

|  |  |
| --- | --- |
| **Estimated Time (UTC)** | **Event** |
| 2021-12-09 22:00 (+0H) | Proof-of-Concept for Log4Shell exploitation was published on Github |
| 2021-12-10 08:00 (+10H) | Push experimental Suricata rule to detect exploitation attempts |
| 2021-12-10 12:30 (+14,5H) | Finish tool that harvests IOC’s out of detected exploitation attempts, start hunting across all platforms |
| 2021-12-10 15:00 (+17H) | Behavior-based detection picks up first successful hack using Log4Shell |
| 2021-12-10 21:00 (+23H) | Transition from improvised IOC hunting to emergency hunting shifts |
| 2021-12-11 10:00 (+36H) | Report first incidents based on hunting to customers |
| 2021-12-12 16:00 (+42H) | Send advisory, status update and IOCs to SOC customers |
| 2021-12-12 17:00 (+43H) | Add Suricata rule to testing that can distinguish between failed and successful exploitation in real-time |
| 2021-12-13 08:00 (+58H) | Determine that real-time detection works, move to production |
| 2021-12-13 08:10 (+58H) | Decide to publish all detection & IOC’s as soon as possible |
| 2021-12-13 14:00 (+62H) | Refactor IOC harvesting tool to keep up with exploitation volume |
| 2021-12-13 14:30 (+62,5H) | Another successful hack found using hunting procedure |
| 2021-12-13 19:30 (+67,5H) | Publish all detection and IOC’s in Log4Shell blog |
| 2021-12-13 21:00 (+69h) | End emergency hunting procedure |
| 2021-12-14 06:30 (+80,5H) | Successful hack detected using Suricata rule |

Overview of most important event and actions for the Fox-IT SOC when responding to the emergence of Log4Shell

### **Friday (2021-12-10): Get visibility and grab the quick wins**

On Thursday evening, a proof-of-concept was published on GitHub that made it trivial for attackers to exploit Log4Shell. As we became aware of this on Friday morning, our first point of attention was getting visibility. As we monitor networks with significant exposure to the internet, we anticipated that exploitation attempts would be coming quickly and in vast volumes. One of the first things we did was add detection for exploitation attempts. While we knew that we cannot manually investigate every exploitation attempt, detecting them in the first place would allow us to have a starting point for a threat hunt, add context to other alerts, and give us an idea how this vulnerability is being exploited in the wild. Of course, methods of gaining visibility differ for every SOC and even per threat scenario, but **if you can deploy measures to increase visibility, these will often help you out for the remainder of your response process.**

While we would have preferred to have full detection coverage immediately, that is often not realistic. We hoped that by detecting exploitation attempts, we would be pointed in the right direction for finding additional detection opportunities.

For the Log4Shell vulnerability, there was an additional benefit. Exploitation of Log4Shell is a multi-step process, where upon successful exploitation of the vulnerability the vulnerable Log4J package will reach out to an attacker-controlled server to retrieve the second-stage payload. This multi-step exploitation process is to the advantage of defenders: initial exploitation attempts will contain the location of the attacker-controlled server that hosts the second-stage payload. This made it possible to automatically retrieve and process the exploitation attempts that were detected. This could then be used to generate a list of high-confidence Indicators of Compromise (IOCs). After all, a connection to a server hosting a second-stage payload could be a strong indicator that a successful exploitation had occurred.

We started regularly mining these IOCs and using them as input for emergency threat hunting. Initially this hunting process was a bit freeform, but we quickly realized we would be doing multiple of such emergency threat hunts for the coming days. We initiated a procedure to perform emergency hunting shifts leveraging our SOC analysts on-duty to perform IOC checks and hunting the networks of customers where these IOCs were found.

We were aware that this ‘emergency threat hunting’ approach was not failproof, for a multitude of reasons:

* We had to detect the exploitation attempt correctly to mine the corresponding IOC.
* Hunting for these IOCs still requires manual investigation and threat hunting and is thus prone to human errors.
* Lastly, searching for connections to IOC’s is a form of retroactive investigation: it does not allow defenders to identify a compromise in real-time.

It was clear that this approach wouldn’t last us all weekend. However, this procedure allowed us the much...