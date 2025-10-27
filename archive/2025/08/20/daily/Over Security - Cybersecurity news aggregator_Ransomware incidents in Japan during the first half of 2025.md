---
title: Ransomware incidents in Japan during the first half of 2025
url: https://blog.talosintelligence.com/ransomware_incidents_in_japan_during_the_first_half_of_2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-20
fetch_date: 2025-10-07T00:49:47.591052
---

# Ransomware incidents in Japan during the first half of 2025

# Cisco Talos Blog

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

![](/content/images/2025/08/talos-evergreen-ransomware-2000x1000.jpg)

# Ransomware incidents in Japan during the first half of 2025

By
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/)

Tuesday, August 19, 2025 06:00

[ransomware](/category/ransomware/)
[Threat Spotlight](/category/threat-spotlight/)

* In the first half of 2025, the number of ransomware attacks in Japan increased by approximately 1.4 times compared to the previous year.
* Ransomware attackers continue to primarily target small and medium-sized enterprises in Japan. The most affected industry remains manufacturing, unchanged from last year.
* The ransomware group causing the most damage in Japan is "Qilin."
* In late June, a new ransomware group called "Kawa4096" emerged and might have attacked two Japanese companies.

## Victimized companies

Figure 1 summarizes the ransomware incidents involving Japanese domestic companies, including overseas branches and subsidiaries, from January 1 to June 30, 2025. According to the Cisco Talos investigation, there were 68 ransomware cases affecting organizations in Japan during this period. Sources include Cisco telemetry, official statements from affected companies, news reports and data from ransomware leak sites. Compared to 48 cases during the same period last year, this represents an approximately 1.4-fold increase. The number of incidents per month ranged from a minimum of 4 to a maximum of 16, with an average of about 11 ransomware attacks per month.

![](https://blog.talosintelligence.com/content/images/2025/08/japan-incidents-1.jpg)

**Figure 1. Ransomware incidents in Japan during the first half of 2025.**

The industries affected remain largely unchanged from the same period last year, with the manufacturing sector experiencing the highest number of incidents at 18.2%, followed by the automotive sector with 5 cases (5.7%), and trading companies, construction and transportation each reporting 4 cases (4.6%).

![](https://blog.talosintelligence.com/content/images/2025/08/japan-number.jpg)

**Figure 2. Number of victim organizations by industry.**

Regarding the size of the affected organizations, those with capital of less than 100 million yen (or ¥) accounted for the largest share at 38%, followed by those with capital from ¥100 million – 1 billion at 31%. In total, organizations with capital under ¥1 billion made up 69% of all cases, indicating that attackers continue to primarily target small and medium-sized enterprises (see Figure 3).

![](https://blog.talosintelligence.com/content/images/2025/08/japan-classification.jpg)

**Figure 3. Classification of victim organizations by capital size.**

## Types of ransomware most frequently involved in incidents

[LockBit](https://www.justice.gov/archives/opa/pr/us-and-uk-disrupt-lockbit-ransomware-variant) and [8base](https://www.europol.europa.eu/media-press/newsroom/news/key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown), which were among the most frequently observed ransomware groups in Japan during the first half of FY2024, ceased their activities following takedown operations by law enforcement in February 2024 and February 2025 respectively, as publicly announced in press releases. As a result, neither group has been observed in 2025.

RansomHub and Hunters International, which ranked among the top ransomware groups last year, are confirmed to still be active in Japan. Notably, the ransomware group Qilin, which had not been reported to have caused any damage in Japan in FY2024, emerged as the most active group in the first half of FY2025, with eight confirmed victim organizations in the country. Qilin has been active since [October 2022](https://www.theguardian.com/technology/article/2024/jun/05/who-are-qilin-the-cybercriminals-thought-behind-the-london-hospitals-hack) and is one of the ransomware groups exerting significant influence both domestically and internationally. The findings from this investigation further suggest that Qilin’s activity is intensifying, making it one of the most critical groups to watch.

Following Qilin, three groups — Lynx, Nightspire, and RansomHub — accounted for three incidents each. Regarding RansomHub, attacks targeting Japan were also confirmed around the same time in 2024. Groups such as Akira, Cicada3301, Gunra, Kawa4096 and Space Bears were each responsible for two incidents. In particular, Kawa4096, which began operations in late June 2025, has targeted Japan from the outset, warranting special attention.

Other groups with one confirmed incident each include Black Suit, CLOP, Devman, Fog and Play, among others.

![](https://blog.talosintelligence.com/content/images/2025/08/japan-types.jpg)

**Figure 4. Identified ransomware employed in attacks.**

## Spotlight: Kawa4096 ransomware group

Trustwave published a useful [analysis report](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/kawa4096s-ransomware-tide-rising-threat-with-borrowed-styles/) on Kawa4096 in July 2025.

The ransomware group first posted about a victim organization on its leak site, shown in Figure 5, on June 19, 2025. Subsequently, it disclosed information believed to pertain to attacks on two Japanese companies on June 26 and June 28.

![](https://blog.talosintelligence.com/content/images/2025/08/Kawa4096-leaksite-1.png)

**Figure 5. Kawa4096 leak site.**

## KaWaLocker ransomware deployed by Kawa4096

### Config File

The ransomware used by this group, shown in Figure 6, utilizes the FindResourceW API to load a configuration file from the resource section, as illustrated in Figure 7. The configuration file defines items such as file extensions, directories and specific folders to exclude from encryption; processes and services to terminate; and commands to execute. In the example c...