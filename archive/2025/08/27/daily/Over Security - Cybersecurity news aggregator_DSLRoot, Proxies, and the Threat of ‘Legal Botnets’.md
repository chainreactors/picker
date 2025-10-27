---
title: DSLRoot, Proxies, and the Threat of ‘Legal Botnets’
url: https://krebsonsecurity.com/2025/08/dslroot-proxies-and-the-threat-of-legal-botnets/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:49:25.626795
---

# DSLRoot, Proxies, and the Threat of ‘Legal Botnets’

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# DSLRoot, Proxies, and the Threat of ‘Legal Botnets’

August 26, 2025

[24 Comments](https://krebsonsecurity.com/2025/08/dslroot-proxies-and-the-threat-of-legal-botnets/#comments)

The cybersecurity community on **Reddit** responded in disbelief this month when a self-described Air National Guard member with top secret security clearance began questioning the arrangement they’d made with company called **DSLRoot**, which was paying $250 a month to plug a pair of laptops into the Redditor’s high-speed Internet connection in the United States. This post examines the history and provenance of DSLRoot, one of the oldest “residential proxy” networks with origins in Russia and Eastern Europe.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/sacapoopiepost.png)

The query about DSLRoot came from a Reddit user “**Sacapoopie**,” who did not respond to questions. This user has since deleted the original question from their post, although some of their replies to other Reddit cybersecurity enthusiasts [remain in the thread](https://www.reddit.com/r/cybersecurity/comments/1mksa8q/hosting_residential_ip_network_nodes/). The original post was indexed [here by archive.is](https://archive.is/qsozu), and it began with a question:

“I have been getting paid 250$ a month by a residential IP network provider named DSL root to host devices in my home,” Sacapoopie wrote. “They are on a separate network than what we use for personal use. They have dedicated DSL connections (one per host) to the ISP that provides the DSL coverage. My family used Starlink. Is this stupid for me to do? They just sit there and I get paid for it. The company pays the internet bill too.”

Many Redditors said they assumed Sacapoopie’s post was a joke, and that nobody with a cybersecurity background and top-secret (TS/SCI) clearance would agree to let some shady residential proxy company introduce hardware into their network. Other readers pointed to a slew of posts from Sacapoopie in the Cybersecurity subreddit over the past two years about their work on cybersecurity for the Air National Guard.

When pressed for more details by fellow Redditors, Sacapoopie described the equipment supplied by DSLRoot as “just two laptops hardwired into a modem, which then goes to a dsl port in the wall.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/saca-twolaptops.png)

“When I open the computer, it looks like [they] have some sort of custom application that runs and spawns several cmd prompts,” the Redditor explained. “All I can infer from what I see in them is they are making connections.”

When asked how they became acquainted with DSLRoot, Sacapoopie told another user they discovered the company and reached out after viewing an advertisement on a social media platform.

“This was probably 5-6 years ago,” Sacapoopie wrote. “Since then I just communicate with a technician from that company and I help trouble shoot connectivity issues when they arise.”

Reached for comment, DSLRoot said its brand has been unfairly maligned thanks to that Reddit discussion. The unsigned email said DSLRoot is fully transparent about its goals and operations, adding that it operates under full consent from its “regional agents,” the company’s term for U.S. residents like Sacapoopie.

“As although we support honest journalism, we’re against of all kinds of ‘low rank/misleading Yellow Journalism’ done for the sake of cheap hype,” DSLRoot wrote in reply. “It’s obvious to us that whoever is doing this, is either lacking a proper understanding of the subject or doing it intentionally to gain exposure by misleading those who lack proper understanding,” DSLRoot wrote in answer to questions about the company’s intentions.

“We monitor our clients and prohibit any illegal activity associated with our residential proxies,” DSLRoot continued. “We honestly didn’t know that the guy who made the Reddit post was a military guy. Be it an African-American granny trying to pay her rent or a white kid trying to get through college, as long as they can provide an Internet line or host phones for us — we’re good.”

## WHAT IS DSLROOT?

DSLRoot is sold as a residential proxy service on the forum **BlackHatWorld** under the name DSLRoot and **GlobalSolutions**. The company is based in the Bahamas and was formed in 2012. The service is advertised to people who are not in the United States but who want to seem like they are. DSLRoot pays people in the United States to run the company’s hardware and software — including 5G mobile devices — and in return it rents those IP addresses as dedicated proxies to customers anywhere in the world — priced at $190 per month for unrestricted access to all locations.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/dslroot.png)

The GlobalSolutions account on BlackHatWorld lists a Telegram account and a WhatsApp number in Mexico. DSLRoot’s profile on the marketing agency digitalpoint.com from 2010 shows their previous username on the forum was “**Incorptoday**.” GlobalSolutions user accounts at bitcointalk[.]org and roclub[.]com include the email **clickdesk@instantvirtualcreditcards[.]com**.

Passive DNS records from **DomainTools.com** show instantvirtualcreditcards[.]com shared a host back then — 208.85.1.164 — with just a handful of domains, including dslroot[.]com, regacard[.]com, 4groot[.]com, residential-ip[.]com, 4gemperor[.]com, ip-teleport[.]com, **proxysource[.]net** and proxyrental[.]net.

Cyber intelligence firm **Intel 471** finds GlobalSolutions registered on BlackHatWorld in 2016 using the email address **prepaidsolutions@yahoo.com**. This user shared that their birthday is March 7, 1984.

Several negative reviews about DSLRoot on the forums noted that the service was operated by a BlackHatWorld user calling himself “**USProxyKing**.” Indeed, Intel 471 shows this user told fellow forum members in 2013 to contact him at the Skype username “dslroot.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/bhw-usproxyking.png)

USProxyKing on BlackHatWorld, soliciting installations of his adware via torrents and file-sharing sites.

USProxyKing had a reputation for spamming the forums with ads for his residential proxy service, and he ran a “[pay-per-install](https://krebsonsecurity.com/2011/06/pay-per-install-a-major-source-of-badness/)” program where he paid affiliates a small commission each time one of their websites resulted in the installation of his unspecified “adware” programs — presumably a program that turned host PCs into proxies. On the other end of the business, USProxyKing sold that pay-per-install access to others wishing to distribute questionable software — at $1 per installation.

Private messages indexed by Intel 471 show USProxyKing also raised money from nearly 20 different BlackHatWorld members who were promised shareholder positions in a new business that would offer robocalling services capable of placing 2,000 calls per minute.

**Constella Intelligence**, a platform that tracks data exposed in breaches, finds that same IP address GlobalSolutions used to register at BlackHatWorld was also used to create accounts at a handful of sites, including a GlobalSolutions...