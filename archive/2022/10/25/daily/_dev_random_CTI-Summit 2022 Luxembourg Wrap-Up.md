---
title: CTI-Summit 2022 Luxembourg Wrap-Up
url: https://blog.rootshell.be/2022/10/24/cti-summit-2022-wrap-up/
source: /dev/random
date: 2022-10-25
fetch_date: 2025-10-03T20:49:32.324029
---

# CTI-Summit 2022 Luxembourg Wrap-Up

[Skip to content](#content)

[![/dev/random](https://blog.rootshell.be/wp-content/uploads/2016/05/art-of-war-e1464648394825.jpg)](https://blog.rootshell.be/)

[/dev/random](https://blog.rootshell.be/)

"If the enemy leaves a door open, you must rush in." – Sun Tzu

Search for:

* [About Me](https://blog.rootshell.be/about/)
  + [About Me](https://blog.rootshell.be/about/)
  + [Online Presentations](http://www.slideshare.net/xme)
  + [PGP Public Key](https://blog.rootshell.be/pgp-public-key/)
* [Disclaimer](https://blog.rootshell.be/disclaimer/)
* [Tools](https://blog.rootshell.be/?page_id=3051)
  + [alerts2afterglow](https://github.com/xme/alerts2afterglow)
  + [hoover](https://github.com/xme/hoover)
  + [inotes.py](https://github.com/xme/inotes.py)
  + [known\_hosts\_bruteforcer](https://github.com/xme/known_hosts_bruteforcer)
  + [pastemon](https://github.com/xme/pastemon)
  + [oplb](https://github.com/xme/oplb)
  + [ossec\_dashboard](https://github.com/xme/ossec_dashboard)
  + [ossec2dshield](https://github.com/xme/ossec2dshield)
  + [twittermon](https://github.com/xme/twittermon)
  + [rrhunter](https://github.com/xme/rrhunter)
  + [syslog2loggly](https://github.com/xme/syslog2loggly)

![](https://blog.rootshell.be/wp-content/uploads/2022/10/ctis2022-900x400.jpg)

# CTI-Summit 2022 Luxembourg Wrap-Up

[October 24, 2022](https://blog.rootshell.be/2022/10/24/cti-summit-2022-wrap-up/ "17:58") [CTI](https://blog.rootshell.be/category/security/cti/), [Event](https://blog.rootshell.be/category/event/), [Wrap-Up](https://blog.rootshell.be/category/wrap-up-2/) [Leave a comment](https://blog.rootshell.be/2022/10/24/cti-summit-2022-wrap-up/#respond)

It has been a while since I did not take time to write a security conference wrap-up. With all these COVID restrictions, we were stuck at home for a while. Still today, some events remain postponed and, worse, canceled! The energy crisis in Europe does not help, some venues are already increasing their prize to host events! How will this evolve? No idea, but, fortunately, they are motivated people who are motivated to organize excellent events! Still no hack.lu this year but, people from [CIRCL.lu](https://circl.lu) decided to organize the first edition of the [Cyber Threat Intelligence Summit](https://cti-summit.org) in Luxembourg. Before the pandemic, there was also the [MISP](https://misp-project.org) summit organized close to hack.lu. This event, held last week, was a mix of pure CTI- and MISP-related presentations. Here is a quick wrap-up and some links to interesting content.

The first-day keynote was performed by Patrice Auffret and was about “*Ethical Internet Scanning in 2022*”. [Patrice](https://twitter.com/patriceauffret) is the founder of [Onypthe](https://www.onyphe.io). If you don’t know the service, it’s a very good concurrent to Shodan. They collect data about Internet connected objects and URLs. Today, scanning is accepted by most of network owners. IMHO, if you care about port-scanning, you failed. It’s part of the “background noise”. What about the ethical aspect of this? Questions that won’t be covered: law aspects, is it useful/useless? Patrice made 10 recommendations to follow when scanning the Internet:

* Explain the purpose
* Put an opt-out
* Provide abuse contacts
* Provides lists of scanners IP addresses
* Have good reverse DNS
* Handle abuse requests
* Don’t fuzz, just use standard packets/protocols
* Scan slowly
* Use fixed IP addresses (no trashable ones)
* Remote collected data (upon request – GDPR)

They are many active players (Shodan, Censys, ZoomEye, LeakIX, …). Don’t blame them because they scan you. Buy an account, use their REST API and query the information they know about you and increase your footprint visibility. Don’t forget that bad guys do it all the time, they know your assets better than you. Also “*You can’t’ secure assets you don’t know*”

Robert Nixon presented two talks related to MISP: “*In Curation we trust*” and, later, “*MISP to Power BI*”. He explained the common problem that we are all facing when starting to deal with threat intel. The risks of “noise” and low-level information. If you collect garbage, you’ll enrich garbage and generate more garbage. Think about the classic IOC “8.8.8.8”. He explained the process of curating MISP events to make them more valuable inside an organization. Example of processing:

* Remove potential false positive
* Reduce the lack of contextualization or inconsistencies
* Are IOCs actionable?

Robert stayed on stage for the 2nd part of his presentation: “MISP + Power BI”. The idea is to access the MISP SQL db from [Power BI](https://powerbi.microsoft.com) (of course in a safe way) and create powerful dashboards based on data available in MISP. Be careful with the tables you will open (correlation is not the best one). Robert explained how data can be prepared for better performances (transform some data), convert them, and remove unwanted columns).

The next presentation was called “*What can time-based analysis say in Ransomware cases?*” by Jorina Baron & david Rufenacht. Like many MSPP, they’ve been busy with ransomware for a while. The compiled data from multiple incidents were used to generate some useful statistics. They focused on:

* Initial access
* Lateral movement
* Effect on target

The dataset was based on 31 ransomware attacks. Some facts:

* 14d between initial to lateral
* 40h between lateral to encryption

Interesting approach for ransomware attacks, besides the classic technical details.

Then Sami Mokaddem presented “*Automation with MISP workflows*”. Recently, a new feature was added to MISP: [Workflows](https://www.misp-project.org/2022/08/08/MISP.2.4.160.released.html/). You may roughly compare it to a small XOAR tool inside MISP that helps to trigger actions based on parameters. Example of uses:

* Chat notifications
* Prevent publication with a specific sanity check

After lunch, we had some lightning talks and “*HZ Rat goes China – Following the tail of an unknown backdoor*” by Axel Wauer. The malware was analyzed and some numbers were reported:

* 120 samples analyzed
* 2 delivery techniques
* 3 malware versions identified
* C2 servers are online
* Campaign is ongoing for 2y
* Focus on Asia/China

As usual, [Andras Iklody](https://twitter.com/iglocska) presented some quick updates about MISP. What changed recently, what’s in the pipe. The amount of work is impressive: 16 releases, 3768 commits, and 100+ contributors.

Cyril Bras came on stage to present his view on sharing IOCs with customers and partners.

And we had another interesting tool to expand the MISP capabilities. [Koen Van Impe](https://twitter.com/cudeso) presented his tool “[Web Scraper](https://github.com/cudeso/misp-scraper)“. The idea is to feed a MISP instance with instructed informations or structured (CSV, TXT, …). You definitely need to check it if you are struggling with a lot of documents to ingest in MISP!

Another topic that comes often on the table about MISP: How to use it and the cloud and, more important, how to scale it properly? [Mikesh Nagar](https://cti-summit.org/speakers/#mikesh-nagar-id) came to talk about his experience with high-level MISP instances hosted in the cloud.

The last presentation of the day was not public.

The second started with another keynote presented by Gregory Boddin: “*Internet Leak Exchange Platform*“. [LeakIx](https://leakix.net) could be seen as a competitor of Onyphe but they focus more on searching for vulnerabilities instead of “mapping the Internet”. The idea could be resumed to “*Get there before the threat actors*”. Gregory explained how the platform works, what they are searching for, and how they handle collected data.

Then, Markus Ludwig came with a presentation called “*Communities – the underestimated super power of CTI*“. Not technical at all, the idea was to have a broader view of the huge amount of security researchers. They are more free researchers than paid ones! The ...