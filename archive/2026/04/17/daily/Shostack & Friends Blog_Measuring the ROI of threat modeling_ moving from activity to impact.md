---
title: Measuring the ROI of threat modeling: moving from activity to impact
url: https://shostack.org/blog/roi-of-threat-modeling/
source: Shostack & Friends Blog
date: 2026-04-17
fetch_date: 2026-04-18T04:32:30.987904
---

# Measuring the ROI of threat modeling: moving from activity to impact

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
  + [Our Partners](/partners/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Measuring the ROI of threat modeling: moving from activity to impact

Shostack + Friends Blog

# Measuring the ROI of threat modeling: moving from activity to impact

Kymberlee Price, Shostack + Associates

Shostack + Associates COO Kymberlee Price shares her experience measuring the impact of secure design engineering practices on security outcomes
![a generated image of a woman standing at a chalkboard reviewing the functions written on it](/images/blog/img/2026/roi-of-tm-796w.png)

When it comes to cybersecurity, one of the most persistent challenges for organizations is *proving the value of preventative work*. Counting the number of threat models (TMs) delivered is a metric of volume, but it doesn't tell us if the money and time we have spent are actually making the organization safer.

While it is easy to measure the cost of Bad Things after they occur, it is extremely difficult to prove that you’ve *prevented* a Bad Thing that may or may not have happened. While Google is producing excellent research into the impact of defensive engineering investments on reducing exploitation, the signal-to-noise ratio remains incredibly small. We are looking at a few hundred 0-days a year compared to millions of lines of code, making direct attribution nearly impossible. When assessing “What Could Go Wrong” so we can prevent negative outcomes from occurring, we have to answer the question:

> Did you successfully prevent harm or was there no actual threat of harm to begin with?

Fortunately there are ways AppSec teams can measure the impact of their threat modeling and secure development programs and not just activity:

* **Near Miss Tracking:** Instead of just counting models, measure how many threats were identified, their severity, and how many were remediated before release. Over time, this data can be analyzed to uncover trends for analysis - are fewer threats being identified per threat model? Is there data that would attribute that to engineering teams improving their security design capabilities (true negative), or a change in the skills or capacity of the people performing the threat models (false negative)?
* **Risk Acceptance Tracking:** How many findings were added to the risk register or formally accepted?
* **Cost Avoidance Analysis:** Based on severity ratings of the issues identified in your threat models, you can estimate the potential cost of the issues found. What would these vulnerabilities have cost the company in developer fix time or bug bounty awards if they had been identified post-release, requiring an incident response operation?
* **Retrospective Analysis:** Look at the 12-18 month window after a feature or product launches, and compare to other features or products across the company. Do components that underwent threat modeling have significantly fewer findings in the bug bounty program than those that didn't?
* **Incident Correlation:** Look at your incident artifacts. If 95% of your critical incidents occur in components that were never threat modeled, while your threat-modeled components rarely reach the critical incident response level, you have a powerful correlation that demonstrates value.

By shifting our focus from how much work we are doing to quantifying identification and reduction in risk and cost savings, we can better communicate the true ROI of a robust threat modeling program.

---

Kymberlee Price has spent years building [effective Secure Development and AppSec programs](https://www.youtube.com/watch?v=oMsBSydxXjA) that balance engineering user experience, scalability, and instrumentation for measuring the impact of security efforts. If this blog post resonated and you’d like more help with your secure design and threat modeling efforts, check out the [Shostack + Associates Accelerator Program](/secure-design-accelerator) – a leadership academy for security professionals that are accountable for an organization's secure-by-design engineering program. This advisory program helps companies actually change how they build secure software.

Image by midjourney: “A woman at a large chalkboard filled with mathematical calculations; precise, ordered, the work of someone thinking rigorously. Marketing photo, high production.”

Originally published by Kymberlee on 17 Apr 2026

Categories:
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)
  [application security](/blog/category/application-security)
  [measurement](/blog/category/measurement)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a generated image of a woman standing at a chalkboard reviewing the functions written on it](/images/blog/img/2026/roi-of-tm-175w.png)](/blog/roi-of-threat-modeling/)

### [Measuring the ROI of threat modeling: moving from activity to impact](/blog/roi-of-threat-modeling/)

17 Apr 2026

Shostack + Associates COO Kymberlee Price shares her experience measuring the impact of secure design engineering practices on security outcomes

[![Conference attendees talk security in a sunny auditorium in San Francisco.](/images/blog/img/2026/Gemini_Generated_Image_SanFrancisco-sunny-conference-175w.png)](/blog/adam-reflections-on-rsac26/)

### [Adam reflects on BSides SF and RSAC](/blog/adam-reflections-on-rsac26/)

14 Apr 2026

Adam finally caught his breath and sat down to reflect on BSides SF and RSAC 2026.

[![Banner for new Threat Modeling AI Systems Course from Shostack + Associates](/images/blog/img/2026/TMAISystems-banner-175w.png)](/blog/early-bird-one-week/)

### [One week left for Threat Modeling AI Systems Early Bird pricing](/blog/early-bird-one-week/)

08 Apr 2026

One week left to take advantage of Early Bird pricing for our new Threat Modeling AI Systems course.

[![The Artemis mission trajectory, so far](/images/blog/img/2026/artemis-trajectory-175w.png)](/blog/artemis-and-cybersecurity/)

### [Artemis and Cybersecurity](/blog/artemis-and-cybersecurity/)

08 Apr 2026

Some thoughts on Ar...