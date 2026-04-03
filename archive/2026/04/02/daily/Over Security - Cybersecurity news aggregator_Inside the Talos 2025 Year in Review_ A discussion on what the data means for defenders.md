---
title: Inside the Talos 2025 Year in Review: A discussion on what the data means for defenders
url: https://blog.talosintelligence.com/inside-the-talos-2025-year-in-review-a-discussion-on-what-the-data-means-for-defenders/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:10.318951
---

# Inside the Talos 2025 Year in Review: A discussion on what the data means for defenders

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2026/03/2025YiR-report_cover.jpg)

# Inside the Talos 2025 Year in Review: A discussion on what the data means for defenders

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, April 2, 2026 06:00

[2025YiR](/category/2025yir/)
[Year In Review](/category/year-in-review/)

Every year, the [Cisco Talos Year in Review](https://www.blog.talosintelligence.com/2025yearinreview) captures the patterns shaping the threat landscape. The 2025 report paints a clear picture: Attackers are moving faster than ever, while using identity-related attacks as the primary battleground.

To unpack the biggest takeaways and what they mean for security teams, we brought together Christopher Marshall, VP of Cisco Talos, and Peter Bailey, SVP and GM of Cisco Security.

Here’s their conversation.

## Old vulnerabilities, new speed

**Marshall:**  One of the clearest trends in this year’s data is the contrast in how vulnerabilities are being exploited. We saw React2Shell disclosed in December and within weeks it became the most targeted vulnerability we tracked.

At the same time, a 12-year-old vulnerability still appeared in the top 10 most exploited list. So we’re seeing very rapid weaponization (likely fuelled by AI given the compressed timeline from initial proof of concept to large-scale exploitation, across multiple languages and platforms) alongside continued success with legacy flaws.

**Bailey:**  There’s always a lot of focus on the latest zero-day, and rightly so. The industrialization of vulnerability exploitation is extremely concerning. But at the same time, many attacks are still leveraging vulnerabilities that have been around for years.

Organizations are dealing with complexity. Large environments. Long device lifecycles. Change management processes that take time. But attackers don’t care about those constraints. They actually count on them.

This is where we need to repeat that the fundamentals still matter. Patch management, asset visibility, lifecycle discipline... We still have work to do there as an industry.

**Marshall:**  And then you have 40% of the top 100 exploited vulnerabilities being effective because organizations were running end-of-life devices. That’s a measurable problem. When infrastructure is no longer supported, attackers know it. They scan for it, and then they target it. Technical debt becomes operational risk.

**Bailey:**  Absolutely. In most cases, it’s not that customers don’t want to patch. It’s that their critical networking infrastructure has been stable for years, and taking it offline can disrupt the business.

As an industry, we need to reduce that friction. Cisco is a big part of that, with built-in protections in our networking equipment that can be applied without downtime, and options to shield systems when patching can'thappen immediately.

## Identity as the primary target

**Marshall:**  If there’s one area where attackers are consistently investing their time and energy, it’s identity. In 2025, identity-based attack techniques were central to major phases of operations, like lateral movement, privilege escalation, and persistence. Controlling identity effectively means controlling access across the environment.

One of the most striking data points in the report is that fraudulent device registration increased 178 percent year over year. In many cases, attackers convinced administrators to register devices on their behalf through vishing (or voice phishing). They targeted administrator-managed registration flows at three times the rate of user-driven ones. There’s a clear preference for high-value victims.

**Bailey:**  And unfortunately these stolen credentials are widely available. Logging in is often easier than breaking in. Once attackers obtain legitimate access, they can blend in.

For defenders, identity controls need to go beyond authentication. You need continuous monitoring. You need risk-based adjustments to access. You need to detect abnormal behavior quickly.

**Marshall:**  We’re also seeing a rise in internal phishing. More than a third of phishing incidents we observed involved attackers sending messages from already compromised accounts.

Once inside, they create mailbox rules to hide replies and suppress visibility. They explore shared drives and collaboration platforms. They look for sensitive information that can help them expand access. This all means defenders need strong visibility into normal user behavior. If accounts suddenly start sending far more messages than usual or accessing data they never touched before, that should stand out.

**Bailey:**  Identity is no longer just an authentication problem. It’s a monitoring and governance problem, as well.

## State-sponsored activity and the blurring of motives

**Marshall:**  We observed continued evolution in state-sponsored activity throughout the year. Talos investigations into China-nexus campaigns increased nearly 75 percent in 2025. These actors are exploiting both zero-day and n-day vulnerabilities while also engaging in financially motivated activity to support their broader goals.

Russian-linked activity continues to correlate closely with geopolitical developments. We consistently see these actors exploiting unpatched networking equipment to establish long-term access.

North Korean affiliated actors refined their “Contagious Interview” campaigns. They compromised developers through fake job opportunities and expanded IT worker schemes using AI-generated personas.

Iranian-linked actors increased hacktivist-style operations by roughly 60 percent last year, and we’ve seen that type of activity rise again during the ongoing conflict in the Middle East. At the same time, actors such as ShroudedSnooper are deploying highly evasive and stealthy backdoors to maintain long-term acc...