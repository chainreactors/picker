---
title: Russia Hacked Routers to Steal Microsoft Office Tokens
url: https://krebsonsecurity.com/2026/04/russia-hacked-routers-to-steal-microsoft-office-tokens/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:50.186919
---

# Russia Hacked Routers to Steal Microsoft Office Tokens

Advertisement

[![](/b-doppel/13.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

Advertisement

[![](/b-keeper/14.png)](https://www.keepersecurity.com/privileged-access-management/?utm_source=KrebsOnSecurity&utm_medium=Sponsored&utm_campaign=KrebsOnSecurity_020126&utm_id=Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Russia Hacked Routers to Steal Microsoft Office Tokens

April 7, 2026

[4 Comments](https://krebsonsecurity.com/2026/04/russia-hacked-routers-to-steal-microsoft-office-tokens/#comments)

Hackers linked to Russia’s military intelligence units are using known flaws in older Internet routers to mass harvest authentication tokens from **Microsoft Office** users, security experts warned today. The spying campaign allowed state-backed Russian hackers to quietly siphon authentication tokens from users on more than 18,000 networks without deploying any malicious software or code.

Microsoft said in [a blog post](https://www.microsoft.com/en-us/security/blog/2026/04/07/soho-router-compromise-leads-to-dns-hijacking-and-adversary-in-the-middle-attacks/) today it identified more than 200 organizations and 5,000 consumer devices that were caught up in a stealthy but remarkably simple spying network built by a Russia-backed threat actor known as “**Forest Blizzard**.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/04/lumen-forestblizzard.png)

Also known as [APT28](https://attack.mitre.org/groups/G0007/) and Fancy Bear, Forest Blizzard is attributed to the military intelligence units within Russia’s General Staff Main Intelligence Directorate (GRU). APT 28 famously compromised the Hillary Clinton campaign, the Democratic National Committee, and the Democratic Congressional Campaign Committee in 2016 in an attempt to interfere with the U.S. presidential election.

Researchers at **Black Lotus Labs**, a security division of the Internet backbone provider **Lumen**, found that at the peak of its activity in December 2025, Forest Blizzard’s surveillance dragnet ensnared more than 18,000 Internet routers that were mostly unsupported, end-of-life routers, or else far behind on security updates. A [new report](https://www.lumen.com/blog-and-news/en-us/frostarmada-forest-blizzard-dns-hijacking) from Lumen says the hackers primarily targeted government agencies—including ministries of foreign affairs, law enforcement, and third-party email providers.

Black Lotus Security Engineer **Ryan English** said the GRU hackers did not need to install malware on the targeted routers, which were mainly older **Mikrotik** and **TP-Link** devices marketed to the Small Office/Home Office (SOHO) market. Instead, they used known vulnerabilities to modify the Domain Name System (DNS) settings of the routers to include DNS servers controlled by the hackers.

As the U.K.’s **National Cyber Security Centre** (NCSC) notes in [a new advisory](https://www.ncsc.gov.uk/news/apt28-exploit-routers-to-enable-dns-hijacking-operations) detailing how Russian cyber actors have been compromising routers, DNS is what allows individuals to reach websites by typing familiar addresses, instead of associated IP addresses. In a DNS hijacking attack, bad actors interfere with this process to covertly send users to malicious websites designed to steal login details or other sensitive information.

English said the routers attacked by Forest Blizzard were reconfigured to use DNS servers that pointed to a handful of virtual private servers controlled by the attackers. Importantly, the attackers could then propagate their malicious DNS settings to all users on the local network, and from that point forward intercept any [OAuth authentication tokens](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) transmitted by those users.

![](https://krebsonsecurity.com/wp-content/uploads/2026/04/ms-dns-forestblizard.png)

DNS hijacking through router compromise. Image: Microsoft.

Because those tokens are typically transmitted only *after* the user has successfully logged in and gone through multi-factor authentication, the attackers could gain direct access to victim accounts without ever having to phish each user’s credentials and/or one-time codes.

“Everyone is looking for some sophisticated malware to drop something on your mobile devices or something,” English said. “These guys didn’t use malware. They did this in an old-school, graybeard way that isn’t really sexy but it gets the job done.”

Microsoft refers to the Forest Blizzard activity as using DNS hijacking “to support post-compromise adversary-in-the-middle (AiTM) attacks on Transport Layer Security (TLS) connections against Microsoft Outlook on the web domains.” The software giant said while targeting SOHO devices isn’t a new tactic, this is the first time Microsoft has seen Forest Blizzard using “DNS hijacking at scale to support AiTM of TLS connections after exploiting edge devices.”

Black Lotus Labs engineer **Danny Adamitis** said it will be interesting to see how Forest Blizzard reacts to today’s flurry of attention to their espionage operation, noting that the group immediately switched up its tactics in response to [a similar NCSC report](https://www.ncsc.gov.uk/sites/default/files/documents/ncsc-mar-authentic_antics.pdf) (PDF) in August 2025. At the time, Forest Blizzard was using malware to control a far more targeted and smaller group of compromised routers. But Adamitis said the day after the NCSC report, the group quickly ditched the malware approach in favor of mass-altering the DNS settings on thousands of vulnerable routers.

“Before the last NCSC report came out they used this capability in very limited instances,” Adamitis told KrebsOnSecurity. “After the report was released they implemented the capability in a more systemic fashion and used it to target everything that was vulnerable.”

TP-Link was among the router makers facing a complete ban in the United States. But on March 23, the **U.S. Federal Communications Commissio**n (FCC) took a much broader approach, [announcing](https://www.fcc.gov/document/fcc-updates-covered-list-include-foreign-made-consumer-routers) it would no longer certify consumer-grade Internet routers that are produced outside of the United States.

The FCC warned that foreign-made routers had become an untenable national security threat, and that poorly-secured routers present “a severe cybersecurity risk that could be leveraged to immediately and severely disrupt U.S. critical infrastructure and directly harm U.S. persons.”

Experts have countered that few new consumer-grade routers would be available for purchase under this new FCC policy (besides maybe Musk’s Starlink satellite Internet routers, which are produced in Texas). The FCC says router makers can apply for a special “conditional approval” from the Department of War or Department of Homeland Security, and that the new policy does not affect any previously-purchased consumer-grade routers.

*This entry was posted on Tuesday 7th of April 2026 01:02 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[APT 28](https://krebsonsecurity.com/tag/apt-28/) [Black Lotus Labs](https://krebsonsecurity.com/tag/black-lotus-labs/) [Danny Adamitis](https://krebsonsecurity.com/tag/danny-adamitis/) [Fancy...