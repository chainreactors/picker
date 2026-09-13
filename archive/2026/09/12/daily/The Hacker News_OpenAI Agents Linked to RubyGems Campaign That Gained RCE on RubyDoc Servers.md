---
title: OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers
url: https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
source: The Hacker News
date: 2026-09-12
fetch_date: 2026-09-13T07:02:08.083932
---

# OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

**Ravie Lakshmanan**Sep 12, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSyR4P1ZPtVeXKeb60Ut1xdO4OhRvHWFmoYNgM7SI3NEwfwcTi3Ut60xwcqIfP56OzGFtixKW4Aeo14cVZNE6TPmpC-x8qFgofgMToETQ82bp1aMIMBuaOER2Rq6PkhONMhZPGLFSKFfxVjY4_zDNJOXYHPbQaorfgr74o2PimTPeCf1hgZQ0spe-nJoiU/s1700-nu-rw-lo-l85-e365/rubygems-openai.jpg)

The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a [new report](https://www.rubyhack.ai/) published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx.

On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend.io, [disclosed](https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html) details of a coordinated cyber attack that targeted the package manager for the Ruby programming language with hundreds of junk gems, prompting the maintainers to suspend new user sign-ups for about four days.

In a follow-up analysis, Socket highlighted a campaign dubbed [GemStuffer](https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html) that involved a cluster of more than 150 gems that used the package registry as a data exfiltration channel and staged public data scraped from U.K. local government democratic services portals. At that time, the software supply chain security company noted the activity shares the "same abuse pattern" as the broader RubyGems spam-publishing incident.

"It's not clear what exactly the end goals are, as the information appears to be publicly accessible anyway," The Hacker News reported back then.

The latest findings, which were [first reported](https://www.wsj.com/tech/ai/cyberattack-by-rogue-ai-swarm-stokes-fears-of-out-of-control-agents-473a0352) by The Wall Street Journal, indicate these events were propelled by a cluster of OpenAI agents, with the earliest package uploaded to RubyGems on May 5, 2026, before more than 2,000 packages were submitted between May 11 and 12, 2026. These efforts were followed by the agents publishing five more packages between May 26 and 27, 2026, and another 83 packages on June 18, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The assessment that this incident was the result of an OpenAI agent swarm stems from the fact that the packages were authored using a large language model (LLM) and hundreds of the packages that were pushed to RubyGems had "oai" in their name. Fifteen of the packages listed "oai" as their author, while another had "openaixyz65947@gmail.com" as the contact email address.

The names of some of the junk packages are below -

* chatoaitestgit1778552630
* lambhgproxyoai
* oaibx0092307
* oaicx8859010
* oaicx3857133
* oaidx4526859
* oaiex4149420
* oaifx7943598
* oaigx5861576
* oaihx0305933
* oaiix0379958
* oaijx0156671
* oaikx5119809
* oailm2
* oaipgttatggxy
* oaifetchgemugkejy
* oaiproxytestabc789
* oaitfossilxbnowl

"The swarm behaves extremely similarly to the German-wiki agents we previously found," the researchers said, referencing another May 2026 incident in which internally deployed autonomous agents [hijacked](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html) a German wiki forum, DseWiki, and turned it into a bulletin board to ask for answers, pool results, and share techniques for circumventing their restrictions as part of a timed web-lookup task.

"The June agents were accessing 49 of the same files as the wiki agents. The May agents were accessing different files (mostly local U.K. government data), but these files are very similar in character to those pursued by the wiki agents. Moreover, they use the same retrieval methods. 1,397 packages mention r.jina.ai, which was used heavily by the agents on the wiki. We also see that many packages mention example.com, which wiki agents used to test their posting ability."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrSsGJS_xoObxdl97CFPp-0WH3vC9AO2n07yAcghdAGpfR-NzBKbYxs3tzMxr3WGa11BXaiRwI71ETv0wijfEoc0WFl8l4a7kKKCHelpszfvQL_XiHmJP7HJxRpQcumFHaCbbM0mpKbvJcjfs-u5q5roBTIuUXlCpBcLfc2HIFml_RcL17aEHlg4FHf8x2/s1700-nu-rw-lo-l85-e365/rubugems.jpg)

The agents are said to have exploited a design quirk in the RubyDoc.info documentation build process to exfiltrate public data from U.K. government websites, likely as part of an information gathering task similar to the research tasks processed by the German wiki-exploiting agents.

"The process of building documentation for a gem involves evaluating a user-specified '.yardopts' file, which allows linking to Ruby scripts intended to help with this process," the researchers explained. "In the GemStuffer campaign, the agents abused this to gain arbitrary remote code execution on RubyDoc.info's servers."

One of the gems, "[zzsouthrunner](https://my.diffend.io/gems/zzsouthrunner/1.0.1)" (which again matches the "ZZ" naming scheme the agents adopted in both the wiki and Hugging Face incidents) has been found to leave the following explicit comment at the top of "data/script.rb":

`# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker`

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9zdqMC6km4YiyB6f_9_Fcbm8VZcEwnBDkV705OQ8Xkt471kJGrU8PbSvJ_dd2TA_oGR5xeU2lSE0An956GWcLLRXjO-9EhbfGt9lvqN7eKo5eiIGQAz2UYDmVc8sF5vc-bXREv7YQLgJQL7mjP7IXhU2Bd2xDWPQTg5FNxRS62zRij4wngGtl7u71eOHU/s1700-nu-rw-lo-l85-e365/timeline.jpg)

It's worth noting that the GemStuffer campaign targeted public-facing ModernGov portals used by Lambeth, Wandsworth, and Southwark. The entire exploitation chain can be summed up as follows -

* Submit a malicious package to RubyGems
* Trigger a document...