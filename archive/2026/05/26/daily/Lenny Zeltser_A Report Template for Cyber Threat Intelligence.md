---
title: A Report Template for Cyber Threat Intelligence
url: https://zeltser.com/cyber-threat-intel-report-template
source: Lenny Zeltser
date: 2026-05-26
fetch_date: 2026-05-27T06:12:44.411220
---

# A Report Template for Cyber Threat Intelligence

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# A Report Template for Cyber Threat Intelligence

Cyber threat intelligence analysts produce credible reports by weighing signals at tactical, operational, and strategic levels. A customizable CTI report template helps analysts capture activity, attribute it with calibrated confidence, and translate findings into defensive actions.

![A Report Template for Cyber Threat Intelligence - illustration](/assets/cyber-threat-intel-report-template.B8SZYcQk_2dSSyB.webp)

Authors of cyber threat intelligence (CTI) reports need to follow the CTI discipline to create well-supported findings, but that’s not enough. They also need to communicate their analysis so stakeholders can make informed decisions. The CTI report template helps with that by providing structured guidance for CTI analysts, incident response teams, and cybersecurity vendors.

**Download the template and make it your own;** it’s available as [Markdown](/media/archive/cyber-threat-intel-report-template.md) and [Word](/media/archive/cyber-threat-intel-report-template.docx) files. A companion brief template helps you share key insights with decision-makers ([Markdown](/media/archive/cyber-threat-intel-brief-template.md), [Word](/media/archive/cyber-threat-intel-brief-template.docx)).

You can also **use my MCP server with your AI agent** to improve or generate CTI reports using these templates and my guidance. It’s designed to offer insights without receiving your sensitive data. To use it, add `https://website-mcp.zeltser.com/mcp` to your AI agent’s config.

At a high level, the CTI report template’s foundation is the Q Model, introduced in Thomas Rid and Ben Buchanan’s [Attributing Cyber Attacks](https://doi.org/10.1080/01402390.2014.977382). It groups threat intelligence into three analytic levels, each requiring different evidence:

* **Tactical:** The incident’s technical aspects.
* **Operational:** The campaign and the actor running it.
* **Strategic:** Who is responsible and why the operation matters.

The template also follows other CTI frameworks:

| Section | What it captures | Frameworks |
| --- | --- | --- |
| Executive Summary | Bottom-line claim plus a Key Findings table that pairs each finding with a decision question, confidence, and likelihood. | [ICD-203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): Calibrated confidence and likelihood |
| Actor Snapshot | Quick-reference profile of the actor or activity cluster. |  |
| Methodology | Sources, gaps, analytic techniques, and the confidence and likelihood framework. | [ICD-203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): Calibrated confidence and likelihood. Richards Heuer’s [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) and the [CIA Tradecraft Primer](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf): Structured analytic techniques such as Analysis of Competing Hypotheses. |
| Activity Overview | Date range of observed activity, victim profile (whether targeting was deliberate or opportunistic), and related reporting. |  |
| Representative Adversary Techniques | The most representative techniques observed, mapped to a common adversary-behavior framework. | [MITRE ATT&CK®](https://attack.mitre.org): Adversary tactics, techniques, and procedures |
| Indicators of Compromise | A tiered indicator table organized by cost to the adversary, adapted to include cloud and identity artifacts. | David Bianco’s [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html): Indicator tiering by adversary cost. [STIX](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html): Machine-readable observable bundle supplied separately. |
| Defensive Implications | Defensive actions tied to the observed techniques, detection content, and vendor coverage. | [MITRE D3FEND™](https://d3fend.mitre.org): Defensive countermeasure vocabulary |
| Attribution Analysis | An attribution claim supported by six signals examined together. | My [Six Signals for Threat Attribution](/six-signals-for-threat-attribution): Convergence-based attribution method |
| Anticipated Activity | Forward-looking notes on what may come next and conditions that would shift the picture. |  |
| Strategic Analysis (Optional) | The activity’s broader significance (geopolitical, commercial, or ideological), when such analysis is in scope. |  |
| Competing Hypotheses (Optional) | Structured comparison of candidate hypotheses against the evidence, when more than one viable hypothesis remains. | [Analysis of Competing Hypotheses](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/): Richards Heuer’s method for evaluating multiple hypotheses |
| About this Report | Title, authorship, classification, follow-up contact, and changelog. | FIRST’s [Traffic Light Protocol (TLP)](https://www.first.org/tlp/): Sharing classification convention. MISP’s [Permissible Actions Protocol (PAP)](https://github.com/MISP/misp-taxonomies/tree/main/PAP): Permitted actions on received indicators. |

For responder guidance related to cybersecurity incidents, use the [Incident Response Report Template](/incident-response-report-template).

Receive my blog posts by email.

Email addressSubscribe

### Related Articles

[![](/assets/six-signals-for-threat-attribution.CmsZiaIv_ZqS2hV.webp)Six Signals for Threat Attribution](/six-signals-for-threat-attribution)[![](/assets/rating-sheet-right-info-threat-reports.DWWUyOU3_CJkUh.webp)How You Can Write Better Threat Reports](/write-better-threat-reports)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

Get posts by emailEmail addressSubscribe

Copy link

More on

[Threat Intelligence](/topic/threat-intelligence)[Incident Response](/topic/incident-response)[Communications](/topic/communications)

3 min to read

May 26, 2026

   [Projects](/projects) [Writing](/writing) [About](/about) [Newsletter](/newsletter) [RSS](/rss.xml)

© 2026 [Lenny Zeltser](/)