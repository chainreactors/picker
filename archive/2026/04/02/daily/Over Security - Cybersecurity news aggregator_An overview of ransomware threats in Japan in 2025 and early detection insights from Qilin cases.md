---
title: An overview of ransomware threats in Japan in 2025 and early detection insights from Qilin cases
url: https://blog.talosintelligence.com/an-overview-of-ransomware-threats-in-japan-in-2025-and-early-detection-insights-from-qilin-cases/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:10.192127
---

# An overview of ransomware threats in Japan in 2025 and early detection insights from Qilin cases

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2026/03/qillin-1-.jpg)

# An overview of ransomware threats in Japan in 2025 and early detection insights from Qilin cases

By
[Azim Khodjibaev](https://blog.talosintelligence.com/author/azim/),
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/),
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Thursday, April 2, 2026 06:00

[ransomware](/category/ransomware/)

* In 2025, a total of 134 ransomware incidents were reported in Japan, marking a 17.5% increase compared to 2024. Among these, 22 incidents were attributed to Qilin, representing 16.4% of the total.
* In 2025, Qilin ransomware was highly active. Looking ahead to 2026, unless there is significant external pressure or disruption, it is likely to further increase its impact. While there are some variations in tactics across affiliates, operations are expected to become more automated, with fewer trial-and-error steps and increasingly refined tradecraft.
* Evidence suggests that some Qilin affiliates may have ties to countries in the post-Soviet region, including the Baltic states.
* Rather than focusing on post-ransomware execution, this blog examines detection opportunities during the pre-ransomware phase.

---

## Ransomware activity in Japan in 2025

In 2025, the number of ransomware incidents increased compared to 2024. Notably, it was a year in which attacks leveraging Qilin ransomware were observed most frequently. There were 134 ransomware incidents reported in Japan in 2025, representing a 17.5% year-over-year increase from 2024. Figure 1 presents the monthly number of ransomware incidents. The data was compiled based on information obtained from data leak sites, official disclosures by affected organizations, and publicly available media reports. On average, approximately 11 incidents were observed per month.

![](https://blog.talosintelligence.com/content/images/2026/03/japan-victim-counts.jpg)

Figure 1. Monthly victim counts in 2025.

Industry-based analysis, as shown in Figure 2, indicates that manufacturing accounts for the largest share of affected organizations (28%). This is followed by automotive-related industries (8%), trading companies (7%), IT (6%), and education (5%). The data suggests that manufacturing and automotive-related sectors continue to be heavily targeted, consistent with last year.

![](https://blog.talosintelligence.com/content/images/2026/03/japan-number.jpg)

Figure 2. Number of victim organizations by industry.

Small- and medium-sized enterprises (based on capital) remained the primary targets of ransomware attacks at 57% of victim organizations, compared to 17% for large enterprises (see Figure 3).

![](https://blog.talosintelligence.com/content/images/2026/03/japan-classification.jpg)

Figure 3. Classification of victim organizations by capital size.

Figure 4 highlights which ransomware groups targeted Japan in 2025. Qilin accounts for the largest share at 16.4% of all incidents, representing approximately four times the number of cases attributed to Lynx, the second most active group. While Qilin caused the highest number of incidents, the data also indicates that many other ransomware groups are actively targeting organizations in Japan.

![](https://blog.talosintelligence.com/content/images/2026/03/japan-types.jpg)

Figure 4. Types of ransomware employed in attacks.

## Factors behind Qilin’s growing attack activity

In 2025, Qilin became the ransomware group responsible for the highest number of victims worldwide. In October alone, the number of victim organizations listed on its leak site exceeded approximately 200 (see Figure 5).

![](https://blog.talosintelligence.com/content/images/2026/03/qilin-victims.jpg)

Figure 5. Number of victims listed on Qilin ransomware leak site.

Below, Talos examines the reasons behind Qilin’s significant increase in attack volume from three key perspectives.

First, Qilin primarily relies on stolen credentials to gain initial access. In the example shown in Figure 6, credentials were obtained through platforms such as Telegram, Breach Forums, and other online platforms. After successfully breaching a target environment, the group places considerable emphasis on post-compromise activities, allowing it to methodically expand its control and maximize impact.

![](https://blog.talosintelligence.com/content/images/2026/03/qilin-credential.jpg)

Figure 6. Credential exposure identified across multiple accounts.

![](https://blog.talosintelligence.com/content/images/2026/03/qilin-telegram.jpg)

Figure 7. Telegram post suggesting that an initial access broker (IAB) may be communicating with a Qilin affiliate.

Second, posts suggesting that the operators are mindful of penetration testers indicate a relatively high level of operational maturity. This awareness implies that Qilin likely maintains well-developed attack manuals that function as practical, step-by-step references for conducting intrusions efficiently.

![](https://blog.talosintelligence.com/content/images/2026/03/Post-by-Haise--one-of-Qilin---s-operators.png)

Figure 8. Post by Haise, one of Qilin’s operators.

Finally, 2025’s statistics show that Qilin most frequently targets industries such as manufacturing; professional, scientific, and technical services; wholesale trade; health care and social assistance; and construction. Among these, health care and social assistance stands out as a particular focus, suggesting that Qilin tends to prioritize sectors where ransomware-induced operational disruptions can cause especially severe consequences.

![](https://blog.talosintelligence.com/content/images/2026/03/qilin-sectors.jpg)

Figure 9. Sectors experiencing impact from Qilin.

## Qilin affiliate use of EDR killer malw...