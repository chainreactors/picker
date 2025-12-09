---
title: Researchers track dozens of organizations affected by React2Shell compromises tied to China’s MSS
url: https://therecord.media/researchers-track-dozens-react2shell-vuln
source: Over Security - Cybersecurity news aggregator
date: 2025-12-08
fetch_date: 2025-12-09T03:18:10.671988
---

# Researchers track dozens of organizations affected by React2Shell compromises tied to China’s MSS

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![united states](https://cms.therecord.media/uploads/format_webp/large_US_Nasa_9015078108.jpg)

Image: NASA

[Jonathan Greig](/author/jonathan-greig)December 8th, 2025

# Researchers track dozens of organizations affected by React2Shell compromises tied to China’s MSS

Organizations across multiple sectors are dealing with the fallout of the React2Shell bug that [emerged last Wednesday](https://therecord.media/chinese-hackers-exploiting-react2shell-vulnerability-amazon) and caused a global patching scramble.

Justin Moore, a member of the threat intel research team at Palo Alto Networks’ Unit 42, told Recorded Future News this weekend that they have confirmed more than 30 affected organizations.

“We have observed scanning for vulnerable RCE, reconnaissance activity, attempted theft of AWS configuration and credential files, as well installation of downloaders to retrieve payloads from attacker command and control infrastructure,” Moore said.

Unit 42 attributed the activity to an initial access broker “with ties to the Chinese Ministry of State Security.”

In the attacks tracked by Unit 42, the hackers used malware strains known as Snowlight and Vshell — malicious tools [previously tied](https://therecord.media/chinese-government-hacker-exploiting-bugs-to-target-defense-government-sectors) to a contractor for China's Ministry of State Security (MSS) by incident responders at Mandiant.

The Trump administration recently [announced](https://news.risky.biz/r/f9b0ed7f?m=86e27317-e8f0-4e77-9f64-f161aa79f6d4) plans to scupper sanctions on the MSS that were put in place following alleged hacks by the agency on at least nine of the largest telecommunications companies in the U.S. The hackers [used](https://therecord.media/eight-telcos-breached-salt-typhoon-nsc) their access to steal the correspondence of President Donald Trump and Vice President JD Vance last year.

![shadowserver](https://cms.therecord.media/uploads/format_webp/shadowserver_9973e543b3.jpg)

**A map of the tools connected to the internet that are potentially vulnerable to CVE-2025-55182, with dark red representing over 10,000. Image: Shadowserver Foundation**

## Widespread scanning

Unit 42’s findings come after experts from Amazon said last week that state-backed hackers in China are exploiting [CVE-2025-55182](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) — a vulnerability impacting a popular open-source tool built into thousands of widely-used digital products.

Referred to colloquially as React2Shell, the bug was reported by researcher Lachlan Davidson on November 29 and publicly disclosed on Wednesday, when a fix was rolled out. The vulnerability carries a “critical” severity score of 10 out of 10.

On Sunday, FBI Assistant Director Brett Leatherman [urged](https://www.linkedin.com/posts/bleatherman_fbicyber-share-7403622588662579200-GIel/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAE0IDMBNZ386Pa7hS3Mqbj38bdMYRgb9nM) IT teams to “prioritize an immediate upgrade to the latest patched versions, and consider targeted threat hunting for signs of compromise.”

“In many environments, teams inherit this exposure simply by adopting modern framework defaults - without explicitly enabling any special “server function” features. That means customer portals, SaaS front-ends, developer/admin consoles, and third-party services built on these stacks may all be in scope,” he explained.

“Where there are indications of successful exploitation - particularly in environments affecting critical services or large populations - please consider engaging your local FBI cyber team.:”

He urged defenders to look at advisories from Censys and GreyNoise for more technical guidance on how hackers are exploiting the bug.

According to Leatherman, current incident data shows “high-volume, automated exploitation attempts” and other evidence that gives defenders “concrete signals to monitor.”

Multiple organizations said they saw scanning by cybercriminals and nation-state actors growing as concern about the vulnerability evolved throughout the week.

The U.K.-based Shadowserver Foundation as well as Censys and GreyNoise all tracked widespread scanning and targeting of the bug.

Shadowsever [explained that](https://infosec.exchange/%40shadowserver/115672050969855947) more than 10,000 tools connected to the internet in the U.S. are vulnerable to CVE-2025-55182, with thousands more across Brazil, Russia, Germany, France, India and China.

Censys [said](https://censys.com/advisory/cve-2025-55182) it observed more than 2.15 million instances of internet facing services that may be affected by the vulnerability. GreyNoise [found](https://www.greynoise.io/blog/cve-2025-55182-react2shell-opportunistic-exploitation-in-the-wild-what-the-greynoise-observation-grid-is-seeing-so-far?ref=metacurity.com) much of the targeting to be “opportunistic and automated.”

The Cybersecurity and Infrastructure Security Agency [added](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) the bug to its Known Exploited Vulnerabilities catalog on Friday, giving federal agencies until December 26 to patch it.

* [Cybercrime](/news/cybercrime)
* [News](/)
* [Technology](/news/technology)
* [China](/news/china)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [China](/tag/china)
* [MSS](/tag/mss)
* [Palo Alto](/tag/palo-alto)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Trump plans executive order curbing state AI lawsDecember 8th, 2025](/trump-plans-ai-exec-order-curbing-state-laws)
* [Meta proposal for less data sharing is approved by European CommissionDecember 8th, 2025](/meta-less-data-sharing-european-commission)
* [India backs off mandatory 'cyber safety' app after surveillance backlashDecember 3rd, 2025](/india-drops-mandate-sanchar-saathi-app-privacy-surveillance)
* [Japan’s Askul resumes limited online sales 6 weeks after ransomware attackDecember 3rd, 2025](/askul-resumes-limited-ordering-following-ransomware-attack)
* [EU’s top court rules that online marketplaces are responsible for processing of data in adsDecember 2nd, 2025](/eu-top-court-rules-online-marketplaces-responsible-for-data-processing-ads)
* [Iran-linked hackers target Israeli, Egyptian critical infrastructure through phishing campaignDecember 2nd, 2025](/iran-linked-hackers-target-israel-egypt-phishing)
* [India faces backlash over government cyber safety app mandateDecember 2nd, 2025](/india-faces-backlash-cyber-safety-app-mandate)
* [Officials accuse North Korea’s Lazarus of...