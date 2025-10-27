---
title: A Developer's Perspective on Time-Based Estimates
url: https://buaq.net/go-269461.html
source: unSafe.sh - 不安全
date: 2024-10-27
fetch_date: 2025-10-06T18:46:13.980246
---

# A Developer's Perspective on Time-Based Estimates

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

![]()

A Developer's Perspective on Time-Based Estimates

Before diving in, I want to clarify that I’m not a project or product manager. As a senior engineer,
*2024-10-26 23:0:21
Author: [hackernoon.com(查看原文)](/jump-269461.htm)
阅读量:10
收藏*

---

Before diving in, I want to clarify that I’m not a project or product manager. As a senior engineer, I do engage in planning and prioritization, but I’m not a SCRUM master or a certified PMP. My insights are drawn purely from my experiences as a developer, not formal training in project management.

Over the past 15 years, I’ve worked with various teams and managers, but one consistent truth stands out: time is our most valuable asset. To maintain a proper work-life balance, managing and protecting that time effectively is essential. While project management has long sought to move away from time-based estimates, I believe that, as an engineer, these estimates are crucial for shielding me from the burden of long hours.

The real issues we need to address are feature creep and poor estimation practices. Let’s explore why the industry is moving away from time-based estimates, and then I’ll explain why I think they can be effective when used correctly.

### Why Not Time-Based Estimates?

Developers and project managers often have reservations about time-based estimates for several reasons:

1. **Uncertainty**: Software development is unpredictable. Changing requirements, technical challenges, and team dynamics can all impact task durations.
2. **Pressure**: Time estimates can create pressure to meet deadlines, potentially leading to rushed work and compromised quality.
3. **Miscommunication**: Estimates may be misunderstood or misrepresented, resulting in unrealistic expectations from stakeholders.
4. **Focus on Speed**: Time estimates can shift the emphasis from quality and creativity to merely getting the job done.
5. **Variability**: Team members work at different paces and have varying levels of experience, complicating the creation of consistent estimates.
6. **Retrospective Accountability**: Consistently inaccurate estimates can lead to blame games, hindering learning and improvement.
7. **Overemphasis on Metrics**: A strong focus on time estimates can cultivate a culture more concerned with metrics than with outcomes and customer satisfaction.

### Pro-Time-Based Arguments

Upon examining these concerns, I find flaws in many of them. It seems that the common objections to time-based estimates stem from poor estimation practices or poorly planned deadlines. Issues like uncertainty, pressure, and retrospective accountability often arise from inadequate processes.

Miscommunication is a separate issue altogether, and variability and an overemphasis on metrics relate more to planning and culture than the estimation process itself. The real challenge appears to be that many development managers or teams lack the skills or maturity for effective time-based estimation, rather than time-based estimates being inherently flawed.

### Why Are Time-Based Estimates Important?

Time is a precious resource. We have twenty-four hours in a day, typically allocating around eight for sleep and another eight for work. This leaves us with limited time for commuting, family, and personal interests. Many of us find that maintaining a work-life balance requires strict adherence to an eight-hour workday.

However, employers often have their own agendas and expect a consistent flow of completed tasks that can often force employees beyond their expected eight hours. So, how do we demonstrate productivity while protecting our time? For me, time-based estimation is the answer.

At Wayfair, we refined our sprint process into something remarkable. Every sprint was well-sized, our team was engaged and productive, and we rarely had to work extra hours to meet deadlines. Our project manager established an efficient and informed approach that allowed us to function smoothly, grounded in time-based estimation. Here’s how we did it:

Technically, we used “Story Points” based on “days,” allowing for splitting into two-hour increments (0.25 pts). Days were assigned Fibonacci numbers (1, 2, 3, 5), and anything beyond five needed to be broken into smaller tickets.

The estimation process included a weekly meeting (or biweekly if necessary) where an engineer familiar with a ticket presented it to the team. We discussed potential solutions, identified unknowns, and noted any external influences impacting our estimates. After the discussion, we would vote on how many “days” the ticket should take, considering developers’ varying levels of experience.

If estimates differed, we opted for the largest or most common estimate based on the spread. If we couldn’t reach a consensus, we would discuss until the team reached a satisfactory conclusion. Crucially, everyone had a voice in sizing the tickets, fostering a collaborative atmosphere.

The next step involved assessing developer capacity and ensuring our sprints aligned with that capacity. With our tickets focused on expected completion times, we established capacity as follows:

* Junior Dev: 7 days of work per sprint
* Mid/Senior Dev: 8 days of work per sprint
* Leads: 6 days of work per sprint

These figures are adjusted for workload and vacations. Once we determined each developer's capacity, we held a grooming session to refine the upcoming sprint. By this point, all tickets were estimated, and developer capacity was clear.

As an example, suppose we had 27 tickets totaling 56 points, and our team of six developers (two junior, three senior, one lead) had 47 points available. This discrepancy meant we needed to remove nine days of work. Our project manager would then prioritize which less critical tickets to drop, ensuring that developers championed any tickets relevant to their work to prevent important tasks from being sidelined. By the end of this session, we could confidently move forward with a manageable sprint.

### Conclusion

Time is paramount. As a developer who values a healthy work-life balance, I aim to complete my tasks within a 40-hour week, and I need my manager to recognize my efforts. Moving away from time-based estimates can create a situation where developers are expected to work extra hours to complete their tasks, as there’s no reliable method to size the workload effectively.

By committing to a robust process that amplifies every developer’s voice and incorporates time as a core element, we can ensure that everyone’s time is respected while still delivering results. This approach helps avoid issues like sprints bleeding into one another or failing to meet deadlines, ensuring work is completed on schedule.

Of course, no system is perfect. There will inevitably be tickets that need to carry over, and adjustments may be necessary over time. Nevertheless, this approach provided me with the best working environment and estimation/planning process I have ever experienced.

文章来源: https://hackernoon.com/a-developers-perspective-on-time-based-estimates?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)