---
title: Data Analysis: The Unsung Hero of Cybersecurity Expertise &#x5b;Guest Diary&#x5d;, (Wed, Dec 4th)
url: https://isc.sans.edu/diary/rss/31494
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-05
fetch_date: 2025-10-06T19:41:39.038602
---

# Data Analysis: The Unsung Hero of Cybersecurity Expertise &#x5b;Guest Diary&#x5d;, (Wed, Dec 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31488)
* [next](/diary/31502)

# [Data Analysis: The Unsung Hero of Cybersecurity Expertise [Guest Diary]](/forums/diary/Data%2BAnalysis%2BThe%2BUnsung%2BHero%2Bof%2BCybersecurity%2BExpertise%2BGuest%2BDiary/31494/)

**Published**: 2024-12-04. **Last Updated**: 2024-12-04 01:37:56 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Data%2BAnalysis%2BThe%2BUnsung%2BHero%2Bof%2BCybersecurity%2BExpertise%2BGuest%2BDiary/31494/#comments)

[This is a Guest Diary by Robert Cao, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

As a cybersecurity professional, I've always prided myself on my technical skills—understanding protocols, setting up secure systems, and knowing the ins and outs of firewalls and authentication mechanisms. But a recent deep dive into firewall and SSH logs taught me a lesson I wasn’t expecting: being technically savvy is only part of the equation. True success in cybersecurity also hinges on being an effective data analyst.

When I began examining the logs, I expected to find the usual culprits—brute force attempts, unusual traffic patterns, and the occasional misconfiguration. What I didn’t expect was how the data itself would tell a story far more valuable than any single technical fix. For instance, a repetitive pattern in the SSH logs from IP 137.184.185.209 showcased over 30 login attempts using common credentials like rootpaired with passwords such as Qaz@123456. At first glance, it seemed like just another brute force attempt. However, when I correlated this with firewall data, the same IP surfaced as repeatedly probing port **2222**, a non-standard SSH port. Suddenly, it became clear: the actor wasn’t just relying on brute force; they were systematically targeting configurations presumed to be "secure by obscurity."

This realization made me question my own assumptions. In the past, I might have simply blocked the IP and moved on, feeling satisfied that I had applied a technical fix. But digging deeper into the data revealed patterns that informed broader strategies. Why was port **2222** being targeted? Could it be part of a larger campaign? These questions led to a more proactive approach: not just reacting to the attack, but trying to anticipate the next one.

Another revelation came from looking at overlapping datasets. By comparing SSH logs with firewall activity, I found four IPs—including 47.236.168.148 and 54.218.26.129—engaged in both brute force attempts and network probes. These actors were persistent, attempting to exploit systems over a short but intense window of time. Without correlating these datasets, I might have missed the coordinated nature of the attack entirely. This experience drove home the importance of cross-referencing data sources to uncover insights that no single log file could reveal.

Perhaps the most humbling realization was understanding that even advanced technical setups are only as good as the decisions behind them. Configurations that allowed root logins or didn’t enforce rate-limiting created vulnerabilities actors could exploit. As I analyzed the logs, I saw not just the actors' actions but also the blind spots in my own system's defenses. Technical knowledge helped me secure the systems, but it was the data analysis that highlighted the gaps.

This experience shifted my mindset. Cybersecurity isn't just about firewalls, encryption, and protocols—it's about understanding the data these systems generate. Data analysis is what transforms raw logs into actionable intelligence. It’s what turns a technically skilled professional into a strategist capable of predicting, preventing, and responding to threats effectively.

If there’s one thing I’ve learned, it’s that cybersecurity professionals must wear at least two hats: the technical expert and the data analyst. Technical skills build the foundation, but it’s the analysis of data that sharpens defenses and enables proactive security. As threats evolve and actors become more sophisticated, so too must our approach. Data is the key, and learning to harness its power is just as important as mastering the latest technical tools.

[1] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords:

[0 comment(s)](/diary/Data%2BAnalysis%2BThe%2BUnsung%2BHero%2Bof%2BCybersecurity%2BExpertise%2BGuest%2BDiary/31494/#comments)

* [previous](/diary/31488)
* [next](/diary/31502)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)