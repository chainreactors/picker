---
title: Infrastructure Laundering: Blending in with the Cloud
url: https://krebsonsecurity.com/2025/01/infrastructure-laundering-blending-in-with-the-cloud/
source: Krebs on Security
date: 2025-01-31
fetch_date: 2025-10-06T20:16:06.378517
---

# Infrastructure Laundering: Blending in with the Cloud

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Infrastructure Laundering: Blending in with the Cloud

January 30, 2025

[9 Comments](https://krebsonsecurity.com/2025/01/infrastructure-laundering-blending-in-with-the-cloud/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/funnell-ss.png)

In an effort to blend in and make their malicious traffic tougher to block, hosting firms catering to cybercriminals in China and Russia increasingly are funneling their operations through major U.S. cloud providers. Research published this week on one such outfit — a sprawling network tied to Chinese organized crime gangs and aptly named “**Funnull**” — highlights a persistent whac-a-mole problem facing cloud services.

In October 2024, the security firm **Silent Push** published a [lengthy analysis](https://www.silentpush.com/blog/triad-nexus-funnull/) of how **Amazon AWS** and **Microsoft Azure** were providing services to Funnull, a two-year-old Chinese content delivery network that hosts a wide variety of fake trading apps, [pig butchering scams](https://krebsonsecurity.com/2022/07/massive-losses-define-epidemic-of-pig-butchering/), gambling websites, and retail phishing pages.

Funnull made headlines last summer after it acquired the domain name **polyfill[.]io**, previously the home of a widely-used open source code library that allowed older browsers to handle advanced functions that weren’t natively supported. There were still tens of thousands of legitimate domains linking to the Polyfill domain at the time of its acquisition, and Funnull soon after [conducted a supply-chain attack that redirected visitors to malicious sites](https://arstechnica.com/security/2024/07/384000-sites-link-to-code-library-caught-performing-supply-chain-attack/).

Silent Push’s October 2024 report found a vast number of domains hosted via Funnull promoting gambling sites that bear the logo of the **Suncity Group**, a Chinese entity named in [a 2024 UN report](https://www.unodc.org/roseap/uploads/documents/Publications/2024/Casino_Underground_Banking_Report_2024.pdf) (PDF) for laundering millions of dollars for the North Korean [Lazarus Group](https://en.wikipedia.org/wiki/Lazarus_Group).

In 2023, Suncity’s CEO was [sentenced to 18 years in prison](https://www.smh.com.au/business/companies/ex-suncity-boss-alvin-chau-jailed-for-18-years-in-macau-20230118-p5cdmj.html) on charges of fraud, illegal gambling, and “[triad](https://en.wikipedia.org/wiki/Triad_%28organized_crime%29) offenses,” i.e. working with Chinese transnational organized crime syndicates. Suncity is alleged to have built an underground banking system that [laundered billions of dollars for criminals](https://macaonews.org/news/city/former-suncity-boss-alvin-chau-sentenced-to-18-years-in-prison/).

It is likely the gambling sites coming through Funnull are abusing top casino brands as part of their money laundering schemes. In reporting on Silent Push’s October report, *TechCrunch* [obtained](https://techcrunch.com/2024/10/22/researchers-link-polyfill-supply-chain-attack-to-huge-network-of-copycat-gambling-sites/) a comment from Bwin, one of the casinos being advertised en masse through Funnull, and Bwin said those websites did not belong to them.

Gambling is illegal in China except in Macau, a special administrative region of China. Silent Push researchers say Funnull may be helping online gamblers in China evade the Communist party’s “Great Firewall,” which blocks access to gambling destinations.

Silent Push’s **Zach Edwards** said that upon [revisiting Funnull’s infrastructure again this month](https://www.silentpush.com/blog/infrastructure-laundering/), they found dozens of the same Amazon and Microsoft cloud Internet addresses still forwarding Funnull traffic through a dizzying chain of auto-generated domain names before redirecting malicious or phishous websites.

Edwards said Funnull is a textbook example of an increasing trend Silent Push calls “infrastructure laundering,” wherein crooks selling cybercrime services will relay some or all of their malicious traffic through U.S. cloud providers.

“It’s crucial for global hosting companies based in the West to wake up to the fact that extremely low quality and suspicious web hosts based out of China are deliberately renting IP space from multiple companies and then mapping those IPs to their criminal client websites,” Edwards told KrebsOnSecurity. “We need these major hosts to create internal policies so that if they are renting IP space to one entity, who further rents it to host numerous criminal websites, all of those IPs should be reclaimed and the CDN who purchased them should be banned from future IP rentals or purchases.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/suncity-funnull.png)

Reached for comment, Amazon referred this reporter to a statement Silent Push included in [a report released today](https://www.silentpush.com/blog/infrastructure-laundering). Amazon said AWS was already aware of the Funnull addresses tracked by Silent Push, and that it had suspended all known accounts linked to the activity.

Amazon said that contrary to implications in the Silent Push report, it has every reason to aggressively police its network against this activity, noting the accounts tied to Funnull used “fraudulent methods to temporarily acquire infrastructure, for which it never pays. Thus, AWS incurs damages as a result of the abusive activity.”

“When AWS’s automated or manual systems detect potential abuse, or when we receive reports of potential abuse, we act quickly to investigate and take action to stop any prohibited activity,” Amazon’s statement continues. “In the event anyone suspects that AWS resources are being used for abusive activity, we encourage them to report it to AWS Trust & Safety using the [report abuse form](https://support.aws.amazon.com/#/contacts/report-abuse). In this case, the authors of the report never notified AWS of the findings of their research via our easy-to-find security and abuse reporting channels. Instead, AWS first learned of their research from a journalist to whom the researchers had provided a draft.”

Microsoft likewise said it takes such abuse seriously, and encouraged others to report suspicious activity found on its network.

“We are committed to protecting our customers against this kind of activity and actively enforce acceptable use policies when violations are detected,” Microsoft said in a written statement. “We encourage [reporting](https://protect.checkpoint.com/v2/r01/___https%3A//msrc.microsoft.com/report/___.YzJ1OndlY29tbXVuaWNhdGlvbnM6YzpvOjQwMWQyNWE1OWIxMDNiNWUyZGQ5ZmY2MmZiYTMxMTNiOjc6NDRlNzoyZDg4NzY5MmI4MGVmYWY2M2NmZWVjOGMxMjhkNTRhYjhmODc4Mzk3MjJkYjdkMTEzMjk0MDdmMzA4NDUxNDczOmg6VDpG) suspicious activity to Microsoft so we can investigate and take appropriate actions.”

**Richard Hummel** is threat intelligence lead at **NETSCOUT**. Hummel said it used to be that “noisy” and frequently disruptive malicious traffic — such as automated application layer attacks, and “brute force” efforts to crack passwords or find vulnerabilities in websites — came mostly from botnets, or large collections of hacked devices.

But he said the vast ma...