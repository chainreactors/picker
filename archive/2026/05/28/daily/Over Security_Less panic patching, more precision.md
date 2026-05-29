---
title: Less panic patching, more precision
url: https://blog.talosintelligence.com/less-panic-patching-more-precision/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:05:56.382215
---

# Less panic patching, more precision

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

# Less panic patching, more precision

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, May 28, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week's edition of the Threat Source newsletter.

Recently, Martin closed his introduction with a [warning](https://blog.talosintelligence.com/the-time-of-much-patching-is-coming/): Ready or not, the time of much patching is coming. I've been chewing on that one for a while because I'm rethinking my own enrichment pipelines along these lines, and the questions Martin raised are the ones I keep running into — with one or two ideas on what practitioners can actually do about it.

Honestly speaking, most of us are still prioritising the wrong way. CVSS has been the default for over a decade — but it only answers one question: How bad could this be in theory? It's a severity score, not a risk score. A CVSS 9.8 on something nobody is exploiting (and nobody ever will) is a very different problem from a CVSS 7.2 that's being weaponised in the wild this morning. If your patch queue is sorted purely by CVSS, you'respending finite operations capacity on hypotheticals.

This is where [EPSS](https://www.first.org/epss/) (Exploit Prediction Scoring System) earns its place next to CVSS. EPSS is a probability — between 0 and 1 — that a given CVE will be exploited in the next 30 days, based on real-world signals. The two answer different questions:

|  |  |  |
| --- | --- | --- |
| Feature | CVSS | EPSS |
| Focus | Severity (impact) | Risk (likelihood of exploitation) |
| Nature | Static (usually) | Dynamic (updated daily) |
| Output | 0.0 to 10.0 score | 0.0 to 1.0 probability |
| Primary use | Assesses technical impact | Prioritizes remediation |

CVSS tells you how bad it would be if exploited. EPSS tells you how likely it is to actually happen to you soon. Used together, a high CVSS and a high EPSS is your "drop everything" pile, while a high CVSS and a very lowEPSS can probably wait behind a medium with an EPSS of 0.7. That single change in triage logic can meaningfully shrink the patch backlog without weakening your posture.

The second ingredient is knowing what is actually being exploited — and here, many teams default to CISA's KEV catalog. KEV is excellent, and I've quoted KEV numbers in this newsletter more times than I can count. CISA contributes as an Authorized Data Publisher (ADP) in the CVE Program, [enriching records](https://github.com/cisagov/vulnrichment) alongside the original CNA's data. That model works well, but it's also why KEV is structurally centralized, conservative in what it admits, and naturally scoped to what U.S. federal visibility surfaces. For a global practitioner — and writing this from Germany, I notice — "Is this being exploited?" deserves a broader lens.

That broader lens is starting to take shape with [GCVE](https://gcve.eu/) (Global CVE), a decentralized approach to vulnerability identification and enrichment. Two properties matter for the surge that's coming:

1. **Speed of enrichment.** Because GCVE is decentralized, enrichment data — references, affected products, exploit indicators — doesn't have to wait in a single queue. In practice, actionable context arrives meaningfully faster than the traditional NVD pipeline, which has visibly struggled with backlog over the past two years.
2. **Broader exploitation signal.** Rather than a single authoritative list of what is being exploited, GCVE makes room for multiple sources of exploitation evidence to surface against the same identifier. That gives defenders outside the U.S. (and frankly, inside it too) a more complete picture than KEV alone.

Pair that with EPSS on top of CVSS, and you end up with a triage stack that is faster, broader, and probability-informed rather than only severity.

None of this removes the patching workload that is coming, but it does change which patches you sprint on at 2:00 a.m. and which ones can ride the normal cycle. Before the surge arrives, that's a worthwhile thing to get right.

## The one big thing

Cisco Talos released [EvidenceForge](https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/), a new open-source tool designed to generate highly realistic, correlated synthetic security logs. This tool solves the chronic shortage of high-quality, labeled datasets needed to train threat hunters and validate detection logic. By using a single canonical event model and AI-assisted scenario authoring, EvidenceForge ensures causal and temporal consistency across more than 20 log formats.

### Why do I care?

Relying on heavily scrubbed public datasets or red team engagements often leaves security teams with incomplete telemetry. While most synthetic generators spit out independent events that fail to tell a coherent story, EvidenceForge injects realistic background noise, red herrings, and proper causal sequencing into the mix. This allows your team to work with synchronized datasets that (more) accurately mimic real-world network visibility without the compliance headaches of using production data.

### So now what?

Security teams can head over to GitHub to clone the EvidenceForge repository and use its guided conversation feature to build custom attack scenarios. Defenders can then use these newly generated datasets to build robust SOC analyst training programs, stress-test a new SIEM, and validate detection pipelines before they touch a production environment. You can find the full details and the link to the open-source repository in the [blog post](https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/).

## Top security headlines of the week

**Lawmakers demand answers as C...