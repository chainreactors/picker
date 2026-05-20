---
title: From PDB strings to MaaS: Tracking a commodity BadIIS ecosystem used by Chinese-speaking threat
url: https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/
source: Over Security
date: 2026-05-19
fetch_date: 2026-05-20T06:05:11.142766
---

# From PDB strings to MaaS: Tracking a commodity BadIIS ecosystem used by Chinese-speaking threat

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/Badlls-03.jpg)

# From PDB strings to MaaS: Tracking a commodity BadIIS ecosystem used by Chinese-speaking threat

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Tuesday, May 19, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos has uncovered a BadIIS variant — identifiable by its embedded "demo.pdb" strings — that functions as commodity malware. This variant is likely sold or shared among multiple Chinese-speaking cybercrime groups that operate under a [malware-as-a-service (MaaS)](https://blog.talosintelligence.com/need-to-know-commodity-malware/) model for continuous monetization.
* Analysis of program database (PDB) file paths reveals a sustained, multi-year development effort by an author operating under the alias “lwxat”, spanning from at least September 2021 through January 2026, with evidence of rapid iterative updates, feature branching, and reactive evasion tactics targeting specific security vendors such as Norton.
* Talos recovered a dedicated builder tool that allows threat actors to generate configuration files, customize payloads, and inject parameters into BadIIS binaries — enabling capabilities including traffic redirection to illicit sites, reverse proxying for search engine crawler manipulation, content hijacking, and backlink injection for malicious search engine optimization (SEO) fraud.
* Beyond BadIIS, the same author has developed a suite of auxiliary tools — including service-based installers, droppers, and persistence mechanisms that automate deployment, ensure survivability across IIS server restarts, and evade detection through custom Base64 encoding and obfuscation techniques.

---

## Mystery BadIIS containing “demo.pdb”

Since 2024, Talos has investigated numerous attacks across the Asia-Pacific region (along with a few in South Africa, Europe and North America) that utilize a specific variant of BadIIS characterized by "demo.pdb" strings. While multiple security vendors are tracking the global spread of these variants, Talos' observed tactics, techniques, and procedures (TTPs) show notable divergences from those documented by other vendors like [Trend Micro](https://www.trendmicro.com/en_us/research/25/b/chinese-speaking-group-manipulates-seo-with-badiis.html), [Ahnlab](https://asec.ahnlab.com/jp/65289/), VNPT, and [Elastic](https://www.elastic.co/security-labs/badiis-to-the-bone-new-insights-to-global-seo-poisoning-campaign). Consequently, it is difficult to attribute these attacks to a single threat actor. However, we assess with moderate confidence that the "demo.pdb" BadIIS variant is a commodity tool utilized by multiple Chinese-speaking cybercrime groups.

## Insights from embedded PDB strings

Although the core functionality of this BadIIS variant is largely limited to SEO fraud, content injection, and proxy‑based traffic manipulation, our investigation pivoted toward the malware’s embedded PDB strings. The consistent PDB path pattern offers much more intelligence value than the generic “demo.pdb” filename. The combination of a stable “Administrator\Desktop” build environment, Chinese-language folder names, and date-based versioning creates a highly reliable fingerprint for tracking and clustering this BadIIS version toolset. Beyond reinforcing our assessment that this is a commodity IIS malware family, the PDB paths enabled attribution to a possible customer name alias “x神” (“xshen”). Furthermore, the PDB artifacts reveal the existence of customized builds, some explicitly tailored to:

* Bypass specific antivirus products, such as Norton
* Perform site‑wide hijacking
* Redirect users conditionally based on browser language or environment

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/fig1.png)

Figure 1. “Custom site hijacking: redirect based on browser language” version.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/fig2-1.png)![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/fig2-2.png)

Figure 2. PDB with 过诺顿 (bypass Norton antivirus) version.

Prompted by these initial discoveries, Talos expanded our threat hunting efforts to identify similar PDB strings associated with this author with high confidence. The PDB paths extracted from these BadIIS variants reveal a sustained, multi-year development effort spanning from at least September 2021 to January 2026. By analyzing the developer's folder naming conventions, we can accurately map the malware's evolutionary trajectory, feature branching, and commercialization model.

### Timeline and iterative maintenance

Talos observed that the earliest explicit timestamp in the PDB paths is Sept. 30, 2021, indicating that the development of this specific toolset began on or before this date. The naming conventions observed in folders such as “dll0217”, “dll0301”, and “dll0315” (likely representing February 17, March 1, and March 15) demonstrate periods of rapid, sprint-like updates. Additionally, the “dll-no503” directory is particularly notable; it likely represents a troubleshooting build designed to resolve an issue where the malware caused IIS to throw "503 Service Unavailable" errors, which would otherwise alert server administrators to the infection. Finally, the latest observed compilation date, “dll20260106” (Jan. 6, 2026), confirms that this toolset remains actively maintained and deployed in the wild as of early 2026.

### Feature branching and evasion tactics

Talos also observed that the folder “兼容百度浏览器+劫持robots.txt” (“Compatible with Baidu browser + hijacking robots.txt”) explicitly confirms the malware's role in malicious SEO campaigns, specifically targeting the ...