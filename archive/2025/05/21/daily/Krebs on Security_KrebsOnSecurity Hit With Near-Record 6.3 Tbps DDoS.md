---
title: KrebsOnSecurity Hit With Near-Record 6.3 Tbps DDoS
url: https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/
source: Krebs on Security
date: 2025-05-21
fetch_date: 2025-10-06T22:32:29.575220
---

# KrebsOnSecurity Hit With Near-Record 6.3 Tbps DDoS

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-ninjio/7.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# KrebsOnSecurity Hit With Near-Record 6.3 Tbps DDoS

May 20, 2025

[46 Comments](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/#comments)

KrebsOnSecurity last week was hit by a near record distributed denial-of-service (DDoS) attack that clocked in at more than 6.3 terabits of data per second (a terabit is one trillion bits of data). The brief attack appears to have been a test run for a massive new Internet of Things (IoT) botnet capable of launching crippling digital assaults that few web destinations can withstand. Read on for more about the botnet, the attack, and the apparent creator of this global menace.

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/ddosbomb.png)

For reference, the 6.3 Tbps attack last week was ten times the size of the assault launched against this site in 2016 by the **Mirai** IoT botnet, which [held KrebsOnSecurity offline for nearly four days](https://krebsonsecurity.com/2016/09/the-democratization-of-censorship/). The 2016 assault was so large that **Akamai** – which was providing pro-bono DDoS protection for KrebsOnSecurity at the time — asked me to leave their service because the attack was causing problems for their paying customers.

Since the Mirai attack, KrebsOnSecurity.com has been behind the protection of **Project Shield**, a free DDoS defense service that **Google** provides to websites offering news, human rights, and election-related content. Google Security Engineer **Damian Menscher** told KrebsOnSecurity the May 12 attack was the largest Google has ever handled. In terms of sheer size, it is second only to a very similar attack that **Cloudflare** mitigated and [wrote about in April](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#hyper-volumetric-attacks-continue-spill-into-q2).

After comparing notes with Cloudflare, Menscher said the botnet that launched both attacks bears the fingerprints of **Aisuru**, a digital siege machine that first surfaced less than a year ago. Menscher said the attack on KrebsOnSecurity lasted less than a minute, hurling [large UDP data packets](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/udp-reflection-attacks.html) at random ports *at a rate of approximately 585 million data packets per second*.

“It was the type of attack normally designed to overwhelm network links,” Menscher said, referring to the throughput connections between and among various Internet service providers (ISPs). “For most companies, this size of attack would kill them.”

[![](https://krebsonsecurity.com/wp-content/uploads/2025/05/cf-6.5ddos.png)](https://krebsonsecurity.com/wp-content/uploads/2025/05/cf-6.5ddos.png)

A graph depicting the 6.5 Tbps attack mitigated by Cloudflare in April 2025. Image: Cloudflare.

The Aisuru botnet comprises a globally-dispersed collection of hacked IoT devices, including routers, digital video recorders and other systems that are commandeered via default passwords or software vulnerabilities. As [documented](https://blog.xlab.qianxin.com/large-scale-botnet-airashi-en/) by researchers at **QiAnXin XLab**, the botnet was first identified in an August 2024 attack on a large gaming platform.

Aisuru reportedly went quiet after that exposure, only to reappear in November with even more firepower and software exploits. In a [January 2025 report](https://blog.xlab.qianxin.com/large-scale-botnet-airashi-en/), XLab found the new and improved Aisuru (a.k.a. “**Airashi**“) had incorporated a previously unknown zero-day vulnerability in Cambium Networks cnPilot routers.

## NOT FORKING AROUND

The people behind the Aisuru botnet have been peddling access to their DDoS machine in public **Telegram** chat channels that are closely monitored by multiple security firms. In August 2024, the botnet was rented out in subscription tiers ranging from $150 per day to $600 per week, offering attacks of up to two terabits per second.

“You may not attack any measurement walls, healthcare facilities, schools or government sites,” read a notice posted on Telegram by the Aisuru botnet owners in August 2024.

Interested parties were told to contact the Telegram handle “**@yfork**” to purchase a subscription. The account @yfork previously used the nickname “**Forky**,” an identity that has been posting to public DDoS-focused Telegram channels since 2021.

According to the FBI, Forky’s DDoS-for-hire domains have been seized in multiple law enforcement operations over the years. Last year, Forky said on Telegram he was selling the domain **stresser[.]best**, which saw its servers seized by the FBI in 2022 as part of an ongoing international law enforcement effort aimed at diminishing the supply of and demand for DDoS-for-hire services.

“The operator of this service, who calls himself ‘Forky,’ operates a Telegram channel to advertise features and communicate with current and prospective DDoS customers,” reads [an FBI seizure warrant](https://krebsonsecurity.com/wp-content/uploads/2025/05/Booter-seizure-warrant-Tucows-2.pdf) (PDF) issued for stresser[.]best. The FBI warrant stated that on the same day the seizures were announced, Forky posted [a link to a story on this blog](https://krebsonsecurity.com/2022/12/six-charged-in-mass-takedown-of-ddos-for-hire-sites/) that detailed the domain seizure operation, adding the comment, “We are buying our new domains right now.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/stresserbest.png)

Approximately ten hours later, Forky posted again, including a screenshot of the stresser[.]best user dashboard, instructing customers to use their saved passwords for the old website on the new one.

A review of Forky’s posts to public Telegram channels — as indexed by the cyber intelligence firms **Unit 221B** and **Flashpoint** — reveals a 21-year-old individual who claims to reside in Brazil [full disclosure: Flashpoint is currently an advertiser on this blog].

Since late 2022, Forky’s posts have frequently promoted a DDoS mitigation company and ISP that he operates called **botshield[.]io**. The Botshield website is connected to a business entity registered in the United Kingdom called [Botshield LTD](https://find-and-update.company-information.service.gov.uk/officers/krPZ3H9McgoRJbksmVWst3yc9G0/appointments), which lists a 21-year-old woman from Sao Paulo, Brazil as the director. Internet routing records indicate Botshield ([AS213613](https://ipinfo.io/AS213613)) currently controls several hundred Internet addresses that were allocated to the company earlier this year.

**Domaintools.com** reports that botshield[.]io was registered in July 2022 to a **Kaike Southier Leite** in Sao Paulo. A [LinkedIn profile](https://www.linkedin.com/in/kaike-southier-5074b82b6/) by the same name says this individual is a network specialist from Brazil who works in “the planning and implementation of robust network infrastructures, with a focus on security, DDoS mitigation, colocation and cloud server services.”

## MEET FORKY

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/forky.png)

Image: Jaclyn Vernace / Shutterstock.com.

In his posts to public Telegram chat channels, Forky has hardly attempted to conceal his whereabouts or identity. In countless chat conversations indexed by Unit 221B, Forky could be seen talking about everyday life ...