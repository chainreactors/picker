---
title: 2022 Year in Review
url: https://thedfirreport.com/2023/03/06/2022-year-in-review/
source: The DFIR Report
date: 2023-03-07
fetch_date: 2025-10-04T08:47:50.611835
---

# 2022 Year in Review

[Skip to content](#content)

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[The DFIR Report](https://thedfirreport.com/)

Real Intrusions by Real Attackers, The Truth Behind the Intrusion

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Saturday, October 04, 2025

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[Year in Review](https://thedfirreport.com/category/year-in-review/)

# 2022 Year in Review

[March 6, 2023](https://thedfirreport.com/2023/03/06/2022-year-in-review/)

As we move into the new year, it’s important to reflect on some of the key changes and developments we observed and reported on in 2022. This year’s year-in-review report looks at the types of intrusions that have been most prevalent and the malware we have come across. We’ll also look at some of the most commonly used tactics, techniques, and procedures threat actors use to infiltrate networks, and provide predictions on what we expect to see in the coming year based on data-driven analysis.

This report contains aggregate data from all of our public reporting for the year 2022. Although we have taken precautions and have done our best to remain unbiased, we acknowledge that summary reports such as this may include potential sources of bias that might have been introduced during data collection and only serve as a sample of the wider threat landscape.

Analysis and reporting by [@iiamaleks](https://twitter.com/iiamaleks), [@kostastsale](https://twitter.com/Kostastsale), & [@samaritan\_o](https://twitter.com/samaritan_o)
Reviewed by [@svch0st](https://twitter.com/svch0st) & UC1

## [Services](#services)

We offer multiple services including a [Threat Feed](https://thedfirreport.com/services/) service which tracks Command and Control frameworks such as Cobalt Strike, Metasploit, Empire, PoshC2, etc. More information on this service can be found [here](https://thedfirreport.com/services/).

Our [All Intel](https://thedfirreport.com/services/) service includes long term infrastructure tracking, clustering, C2 configs, and other curated intel, including non-public case data.

If you are interested in hearing more about our services, our would like to talk about a free trial, please reach out to us using the [Contact Us](https://thedfirreport.com/contact/) page. We look forward to hearing from you.

## Intrusion statistics aligned to the MITRE ATT&CK

## [Initial Access](#initial-access)

Over the past year, we have observed multiple intrusions with a majority acting as the entry point for data exfiltration and cyber extortion operations. Most of our cases that result in public reporting focus on ransomware operations and the malware they leverage to attain access. The numbers below do not account for the various RDP brute forces and exploit cases that did not make it to public reporting.

The following summarizes the various initial access techniques observed in our cases:

[![](https://thedfirreport.com/wp-content/uploads/2023/03/2022-001.png)](https://thedfirreport.com/wp-content/uploads/2023/03/2022-001.png)

Similar to 2021, in 2022, a majority of our cases originated from mass email campaigns that aim to spread malware to various organizations. However, one of the biggest shifts in this space has been the discontinuance of Macro usage in Word and Excel files due to [Microsoft’s decision](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked) to disable macros on files downloaded from the internet.

[![](https://thedfirreport.com/wp-content/uploads/2023/03/2022-002.png)](https://thedfirreport.com/wp-content/uploads/2023/03/2022-002.png)

Threat actors quickly reacted and began shifting to the usage of ISO and ZIP files containing LNK shortcuts to execute initial payloads. We have observed a declining usage of Word and Excel files, however, we observed some malware families delivering Word documents weaponized with exploits such as [CVE-2022-30190](https://nvd.nist.gov/vuln/detail/cve-2022-30190). Many malware families that previously relied on macros have begun to migrate over to ISO and ZIP files packaging malicious LNK or script files.

[![](https://thedfirreport.com/wp-content/uploads/2023/03/2022-003.png)](https://thedfirreport.com/wp-content/uploads/2023/03/2022-003.png)

The below graphic displays the tools/methods used by threat actors after getting initial access via the initial access malware listed above.

[![](https://thedfirreport.com/wp-content/uploads/2023/03/2022-54.png)](https://thedfirreport.com/wp-content/uploads/2023/03/2022-54.png)

On the other hand, a few of our cases focused on non-phishing related initial access vectors. One of the most notable is [Gootloader,](https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/) which infects users via compromised websites that are infected to boost rankings on search...