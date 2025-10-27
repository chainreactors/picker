---
title: On the Cyber Safety Review Board
url: https://www.schneier.com/blog/archives/2024/08/a-better-investigatory-board-for-cyber-incidents.html
source: Schneier on Security
date: 2024-08-07
fetch_date: 2025-10-06T18:06:02.010587
---

# On the Cyber Safety Review Board

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## On the Cyber Safety Review Board

When an airplane crashes, impartial investigatory bodies leap into action, empowered by law to unearth what happened and why. But there is no such empowered and impartial body to investigate CrowdStrike’s [faulty update](https://www.nytimes.com/2024/07/19/business/microsoft-outage-cause-azure-crowdstrike.html) that recently unfolded, ensnarling banks, airlines, and emergency services to the tune of billions of dollars. We need one. To be sure, there is the White House’s [Cyber Safety Review Board](https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb). On March 20, the CSRB [released](https://www.cisa.gov/sites/default/files/2024-04/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf) a report into last summer’s intrusion by a Chinese hacking group into Microsoft’s cloud environment, where it compromised the U.S. Department of Commerce, State Department, congressional offices, and several associated companies. But the board’s report—well-researched and containing some good and actionable recommendations—shows how it suffers from its lack of subpoena power and its political unwillingness to generalize from specific incidents to the broader industry.

Some background: The [CSRB](https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb) was established in 2021, by executive order, to provide an independent analysis and assessment of significant cyberattacks against the United States. The goal was to pierce the corporate confidentiality that often surrounds such attacks and to provide the entire security community with lessons and recommendations. The more we all know about what happened, the better we can all do next time. It’s the same thinking that led to the formation of the National Transportation Safety Board, but for cyberattacks and not plane crashes.

But the board immediately failed to live up to its mission. It was founded in response to the Russian cyberattack on the U.S. known as [SolarWinds](https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise). Although it was [specifically tasked](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) with investigating that incident, it [did not](https://www.propublica.org/article/cyber-safety-board-never-investigated-solarwinds-breach-microsoft)—for reasons that remain unclear.

So far, the board has published three reports. They offered only [simplistic recommendations](https://federalnewsnetwork.com/cybersecurity/2024/01/is-the-cyber-safety-review-board-working-lawmakers-consider-tweaks-to-csrb/). In the [first investigation](https://www.dhs.gov/news/2022/07/14/cyber-safety-review-board-releases-report-its-review-log4j-vulnerabilities-and), on Log4J, the CSRB exhorted companies to patch their systems faster and more often. In the [second](https://www.dhs.gov/news/2023/08/10/cyber-safety-review-board-releases-report-activities-global-extortion-focused), on Lapsus$, the CSRB told organizations not to use SMS-based two-factor authentication (it’s vulnerable to SIM-swapping attacks). These two recommendations are basic cybersecurity hygiene, and not something we need an investigation to tell us.

The most recent [report](https://www.dhs.gov/news/2024/04/02/cyber-safety-review-board-releases-report-microsoft-online-exchange-incident-summer)—on China’s penetration of Microsoft—is much better. This time, the CSRB gave us an extensive analysis of Microsoft’s security failures and placed blame for the attack’s success squarely on their shoulders. Its recommendations were also more specific and extensive, addressing Microsoft’s board and leaders specifically and the industry more generally. The report describes how Microsoft stopped rotating cryptographic keys in early 2021, reducing the security of the systems affected in the hack. The report suggests that if the company had set up an automated or manual key rotation system, or a way to alert teams about the age of their keys, it could have prevented the attack on its systems. The report also looked at how Microsoft’s competitors—think Google, Oracle, and Amazon Web Services—handle this issue, offering insights on how similar companies avoid mistakes.

Yet there are still problems, with the report itself and with the environment in which it was produced.

First, the public report cites a large number of anonymous sources. While the report lays blame for the breach on Microsoft’s lax security culture, it is actually quite deferential to Microsoft; it makes special mention of the company’s cooperation. If the board needed to make trades to get information that would only be provided if people were given anonymity, this should be laid out more explicitly for the sake of transparency. More importantly, the board seems to have conflict-of-interest issues arising from the fact that the investigators are corporate executives and heads of government agencies who have full-time jobs.

Second: Unlike the NTSB, the CSRB lacks subpoena power. This is, at least in part, out of fear that the conflicted tech executives and government employees would use the power in an anticompetitive fashion. As a result, the board must rely on wheedling and cooperation for its fact-finding. While the DHS press release [said](https://www.dhs.gov/news/2024/04/02/cyber-safety-review-board-releases-report-microsoft-online-exchange-incident-summer), “Microsoft fully cooperated with the Board’s review,” the next company may not be nearly as cooperative, and we do not know what was not shared with the CSRB.

One of us, Tarah, recently [testified](https://www.youtube.com/watch?v=a7GV8rKFHQ4) on this topic before the U.S. Senate’s Homeland Security and Governmental Affairs Committee, and the senators asking questions seemed genuinely interested in how to fix the CSRB’s extreme slowness and lack of transparency in the two reports they’d issued so far.

It’s a hard task. The CSRB’s charter comes from [Executive Order 14208](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/), which is why—unlike the NTSB—it doesn’t have subpoena power. Congress needs to codify the CSRB in law and give it the subpoena power it so desperately needs.

Additionally, the CSRB’s reports don’t provide useful guidance going forward. For example, is the Microsoft report provides no mapping of the company’s security problems to any government standards that could have prevented them. In this case, the problem is that there are no standards overseen by NIST—the organization in charge of cybersecurity standards—for key rotation. It would have been better for the report to have said that explicitly. The cybersecurity industry needs NIST standards to give us a compliance floor below which any organ...