---
title: SentinelOne Uncovers Chinese Espionage Campaign Targeting Its Infrastructure and Clients
url: https://thehackernews.com/2025/04/sentinelone-uncovers-chinese-espionage.html
source: The Hacker News
date: 2025-04-30
fetch_date: 2025-10-06T22:07:28.443321
---

# SentinelOne Uncovers Chinese Espionage Campaign Targeting Its Infrastructure and Clients

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [SentinelOne Uncovers Chinese Espionage Campaign Targeting Its Infrastructure and Clients](https://thehackernews.com/2025/04/sentinelone-uncovers-chinese-espionage.html)

**Apr 29, 2025**Ravie LakshmananThreat Intelligence / Cyber Espionage

[![Chinese Espionage Campaign](data:image/png;base64... "Chinese Espionage Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijVGiZgZi0eGu8dnstLxH3dcuzIc99pgvP53ux8n4NBL7bRrEba9ccsomDGaU6ZvBnIUCFwVJhpUToX0SQ2jVcddYTgY2HcDA7ON0iRWsjyDejMryhkWwYZNrtcTnZ5tXhyphenhyphenAUEIBLTS8nxiTy5UhSH7lVKW1z8qYyxABrGB8QrkVIJftxB8e9nqKko6zCD/s790-rw-e365/chinese-hackers.jpg)

Cybersecurity company SentinelOne has revealed that a China-nexus threat cluster dubbed **PurpleHaze** conducted reconnaissance attempts against its infrastructure and some of its high-value customers.

"We first became aware of this threat cluster during a 2024 intrusion conducted against an organization previously providing hardware logistics services for SentinelOne employees," security researchers Tom Hegel, Aleksandar Milenkoski, and Jim Walter [said](https://www.sentinelone.com/labs/top-tier-target-what-it-takes-to-defend-a-cybersecurity-company-from-todays-adversaries/) in an analysis published Monday.

PurpleHaze is assessed to be a hacking crew with loose ties to another state-sponsored group known as [APT15](https://thehackernews.com/2025/04/spynote-badbazaar-moonshine-malware.html), which is also tracked as Flea, Nylon Typhoon (formerly Nickel), Playful Taurus, Royal APT, and Vixen Panda.

The adversarial collective has also been observed targeting an unnamed South Asian government-supporting entity in October 2024, employing an operational relay box (ORB) network and a Windows backdoor dubbed GoReShell.

The implant, written in the Go programming language, repurposes an open-source tool called [reverse\_ssh](https://github.com/NHAS/reverse_ssh) to set up reverse SSH connections to endpoints under the attacker's control.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The use of ORB networks is a growing trend among these threat groups, since they can be rapidly expanded to create a dynamic and evolving infrastructure that makes tracking cyberespionage operations and their attribution challenging," the researchers pointed out.

Further analysis has determined that the same South Asian government entity was also targeted previously in June 2024 with ShadowPad (aka PoisonPlug), a known backdoor widely shared among China-nexus espionage groups. ShadowPad is considered to be a successor to another backdoor referred to as PlugX.

That said, with ShadowPad also being used as a conduit to [deliver ransomware](https://thehackernews.com/2025/02/chinese-linked-attackers-exploit-check.html) in recent months, the exact motivation behind the attack remains unclear. The ShadowPad artifacts have been found to be obfuscated using a bespoke compiler called [ScatterBrain](https://cloud.google.com/blog/topics/threat-intelligence/scatterbrain-unmasking-poisonplug-obfuscator).

The exact nature of the overlap between the June 2024 activity and the later PurpleHaze attacks is unknown as yet. However, it's believed that the same threat actor could be behind them.

The ScatterBrain-obfuscated ShadowPad is estimated to have been employed in intrusions targeting over 70 organizations spanning manufacturing, government, finance, telecommunications, and research sectors after [likely exploiting](https://thehackernews.com/2025/02/chinese-linked-attackers-exploit-check.html) an N-day vulnerability in Check Point gateway devices.

[![Chinese Espionage Campaign](data:image/png;base64... "Chinese Espionage Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9HX-1FJsseWNHJzJmPj7Yt8PDgfOx1qTSo480QhZOCpIakWSEmYhT6SSmheI4zPSYALIxBG6TSno3DwuOk9pfIVSuJY10X8xGrTx3lpq8DtAafZGcSAn7iMCP6zUNBzqEGh4Q_f4tL8ZeeNxo42A3IS2JcnTt2sAXZkACOU4gRqQboN-Ym8vcH8CoOYTi/s790-rw-e365/TopTierTarget_.jpg)

One among the victims of these attacks included the organization that was then responsible for managing hardware logistics for SentinelOne employees. However, the cybersecurity firm noted that it found no evidence of a secondary compromise.

It's not just China, for SentinelOne said it also observed attempts made by [North Korea-aligned IT workers](https://thehackernews.com/2025/04/north-korean-hackers-spread-malware-via.html) to secure jobs at the company, including its SentinelLabs intelligence engineering team, via approximately 360 fake personas and over 1,000 job applications.

Last but not least, ransomware operators have targeted SentinelOne and other enterprise-focused security platforms, attempting to gain access to their tools in order to evaluate the ability of their software to evade detection.

This is fuelled by an active underground economy that revolves around buying, selling, and renting access to such enterprise security offerings on messaging apps as well as forums like XSS[.]is, Exploit[.]in, and RAMP.

"Entire service offerings have emerged around this ecosystem, including 'EDR Testing-as-a-Service,' where actors can discreetly evaluate malware against various endpoint protection platforms," the researchers explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"While these testing services may not grant direct access to full-featured EDR consoles or agents, they do provide attackers with semi-private environments to fine-tune malicious payloads without the threat of exposure – dramatically improving the odds of success in real-world attacks."

One ransomware group that takes this threat to a whole new level is Nitrogen, which is believed to be run by a Russian national. Unlike typical approaches that involve approaching insiders or using legitimate credentials harvested from infostealer logs, Nitrogen adopts a different strategy by impersonating real companies.

This is achieved by setting up lookalike domains, spoofed emai...