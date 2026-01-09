---
title: Who Benefited from the Aisuru and Kimwolf Botnets?
url: https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-08
fetch_date: 2026-01-09T03:31:38.622032
---

# Who Benefited from the Aisuru and Kimwolf Botnets?

Advertisement

[![](/b-ninjio/9.png)](https://ninjio.com/lp46d-krebs/)

Advertisement

[![](/b-ninjio/10.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who Benefited from the Aisuru and Kimwolf Botnets?

January 8, 2026

[0 Comments](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/#respond)

Our [first story of 2026](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) revealed how a destructive new botnet called **Kimwolf** has infected more than two million devices by mass-compromising a vast number of unofficial **Android TV streaming boxes**. Today, we’ll dig through digital clues left behind by the hackers, network operators and services that appear to have benefitted from Kimwolf’s spread.

On Dec. 17, 2025, the Chinese security firm **XLab** published [a deep dive on Kimwolf](jsalton%40keepersecurity.com), which forces infected devices to participate in distributed denial-of-service (DDoS) attacks and to relay abusive and malicious Internet traffic for so-called “residential proxy” services.

The software that turns one’s device into a residential proxy is often quietly bundled with mobile apps and games. Kimwolf specifically targeted residential proxy software that is factory installed on [more than a thousand different models](https://github.com/synthient/public-research/blob/main/2026/01/kimwolf/product_devices.csv) of unsanctioned Android TV streaming devices. Very quickly, the residential proxy’s Internet address starts funneling traffic that is linked to ad fraud, account takeover attempts and mass content scraping.

The XLab report explained its researchers found “definitive evidence” that the same cybercriminal actors and infrastructure were used to deploy both Kimwolf and the **Aisuru botnet** — an earlier version of Kimwolf that also enslaved devices for use in DDoS attacks and proxy services.

XLab said it suspected since October that Kimwolf and Aisuru had the same author(s) and operators, based in part on shared code changes over time. But it said those suspicions were confirmed on December 8 when it witnessed both botnet strains being distributed by the same Internet address at **93.95.112[.]59**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/XLab-resito.png)

## RESI RACK

Public records show the Internet address range flagged by XLab is assigned to Lehi, Utah-based **Resi Rack LLC**. Resi Rack’s website bills the company as a “Premium Game Server Hosting Provider.” Meanwhile, Resi Rack’s ads on the Internet moneymaking forum **BlackHatWorld** refer to it as a “Premium Residential Proxy Hosting and Proxy Software Solutions Company.”

Resi Rack co-founder **Cassidy Hales** told KrebsOnSecurity his company received a notification on December 10 about Kimwolf using their network “that detailed what was being done by one of our customers leasing our servers.”

“When we received this email we took care of this issue immediately,” Hales wrote in response to an email requesting comment. “This is something we are very disappointed is now associated with our name and this was not the intention of our company whatsoever.”

The Resi Rack Internet address cited by XLab on December 8 came onto KrebsOnSecurity’s radar more than two weeks before that. **Benjamin Brundage** is founder of [Synthient](https://synthient.com), a startup that tracks proxy services. In late October 2025, Brundage shared that the people selling various proxy services which benefitted from the Aisuru and Kimwolf botnets were doing so at a new Discord server called **resi[.]to**.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/01/resito-93-95-112-53.png)](https://krebsonsecurity.com/wp-content/uploads/2026/01/resito-93-95-112-53.png)

On November 24, 2025, a member of the resi-dot-to Discord channel shares an IP address responsible for proxying traffic over Android TV streaming boxes infected by the Kimwolf botnet.

When KrebsOnSecurity joined the resi[.]to Discord channel in late October as a silent lurker, the server had fewer than 150 members, including “**Shox**” — the nickname used by Resi Rack’s co-founder Mr. Hales — and his business partner “**Linus**,” who did not respond to requests for comment.

Other members of the resi[.]to Discord channel would periodically [post new IP addresses](https://krebsonsecurity.com/wp-content/uploads/2026/01/resito-hackerpakistan.png) that were responsible for proxying traffic over the Kimwolf botnet. As the screenshot from resi[.]to above shows, that Resi Rack Internet address flagged by XLab was used by Kimwolf to direct proxy traffic as far back as November 24, if not earlier. All told, Synthient said it tracked at least seven static Resi Rack IP addresses connected to Kimwolf proxy infrastructure between October and December 2025.

Neither of Resi Rack’s co-owners responded to follow-up questions. Both have been active in selling proxy services via Discord for nearly two years. According to a review of Discord messages indexed by the cyber intelligence firm **Flashpoint**, Shox and Linus spent much of 2024 selling static “ISP proxies” by routing various Internet address blocks at major U.S. Internet service providers.

In February 2025, AT&T [announced](https://serviceguidenew.att.com/sg_CustomPreviewer?attachmentId=00PPV00001Jf2Qf2AJ) that effective July 31, 2025, it would no longer originate routes for network blocks that are not owned and managed by AT&T (other major ISPs have since made similar moves). Less than a month later, Shox and Linus told customers they would soon cease offering static ISP proxies as a result of these policy changes.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/shox-linus-static-att.png)

## DORT & SNOW

The stated owner of the resi[.]to Discord server went by the abbreviated username “D.” That initial appears to be short for the hacker handle “**Dort**,” a name that was invoked frequently throughout these Discord chats.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/resito-d-profile.png)

Dort’s profile on resi dot to.

This “Dort” nickname came up in KrebsOnSecurity’s recent conversations with “[**Forky**](https://krebsonsecurity.com/tag/forky/),” a Brazilian man who [acknowledged](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/) being involved in the marketing of the Aisuru botnet at its inception in late 2024. But Forky vehemently denied having anything to do with [a series of massive and record-smashing DDoS attacks](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/) in the latter half of 2025 that were blamed on Aisuru, saying the botnet by that point had been taken over by rivals.

Forky asserts that Dort is a resident of Canada and one of at least two individuals currently in control of the Aisuru/Kimwolf botnet. The other individual Forky named as an Aisuru/Kimwolf botmaster goes by the nickname “**Snow**.”

On January 2 — just hours after our story on Kimwolf was published — the historical chat records on resi[.]to were erased without warning and replaced by [a profanity-laced message](https://krebsonsecurity.com/wp-content/uploads/2026/01/fsckben.png) for Synthient’s founder. Minutes after that, the entire server disappeared.

Later that same day, several of the more active members of the now-defunct resi[.]to Discord server moved to a Telegram channel where they posted Brundage’s personal information, and generally complained about being unable to find reliable “bulletproof” hosting for their botnet.

Hilariously, a user by the name “Richard Re...