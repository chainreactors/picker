---
title: TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen via Trivy-Linked Breach, Google GTIG Tracks TeamPCP as UNC6780, and CISA KEV Deadline Arrives with No Standalone Advisory, (Wed, Apr 8th)
url: https://isc.sans.edu/diary/rss/32880
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-08
fetch_date: 2026-04-09T04:32:24.706279
---

# TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen via Trivy-Linked Breach, Google GTIG Tracks TeamPCP as UNC6780, and CISA KEV Deadline Arrives with No Standalone Advisory, (Wed, Apr 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32878)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen via Trivy-Linked Breach, Google GTIG Tracks TeamPCP as UNC6780, and CISA KEV Deadline Arrives with No Standalone Advisory](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B007%2BCisco%2BSource%2BCode%2BStolen%2Bvia%2BTrivyLinked%2BBreach%2BGoogle%2BGTIG%2BTracks%2BTeamPCP%2Bas%2BUNC6780%2Band%2BCISA%2BKEV%2BDeadline%2BArrives%2Bwith%2BNo%2BStandalone%2BAdvisory/32880/)

**Published**: 2026-04-08. **Last Updated**: 2026-04-08 17:15:05 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B007%2BCisco%2BSource%2BCode%2BStolen%2Bvia%2BTrivyLinked%2BBreach%2BGoogle%2BGTIG%2BTracks%2BTeamPCP%2Bas%2BUNC6780%2Band%2BCISA%2BKEV%2BDeadline%2BArrives%2Bwith%2BNo%2BStandalone%2BAdvisory/32880/#comments)

This is the seventh update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). [Update 006](https://isc.sans.edu/diary/32864) covered developments through April 3, including the CERT-EU European Commission breach disclosure, ShinyHunters' confirmation of credential sharing, Sportradar breach details, and Mandiant's quantification of 1,000+ compromised SaaS environments. This update consolidates five days of intelligence from April 3 through April 8, 2026.

## HIGH: Cisco Development Environment Breached via Trivy Supply Chain, 300+ Repositories Stolen

[BleepingComputer reported](https://www.bleepingcomputer.com/news/security/cisco-source-code-stolen-in-trivy-linked-dev-environment-breach/) that threat actors leveraged credentials stolen through the Trivy supply chain compromise ([CVE-2026-33634](/vuln.html?cve=2026-33634)) to breach Cisco's internal development environment. The attackers gained access to build systems and developer workstations through a malicious GitHub Action plugin.

The breach scope is substantial:

* **Over 300 private GitHub repositories** containing Cisco source code were cloned, including code for AI-powered products and unreleased items
* **Customer repositories** belonging to banks, business process outsourcing firms, and US government agencies were among those exfiltrated
* **AWS keys** were stolen and used for unauthorized activities across Cisco's cloud accounts
* **Multiple threat actors** were reportedly involved in the Cisco CI/CD and AWS account breaches, "with varying degrees of activity"

ShinyHunters subsequently [expanded their claims](https://cybernews.com/security/hackers-blackmail-cisco-over-stolen-salesforce-data/) beyond the development environment, alleging access to 3 million or more Salesforce records, additional GitHub repositories, and AWS S3 buckets. The claimed dataset allegedly includes records tied to personnel at FBI, DHS, DISA, IRS, and NASA, as well as the Australian Ministry of Defense and Indian government agencies. These expanded claims have not been independently verified.

ShinyHunters set an extortion deadline of approximately April 3. As of April 8, no public data dump has materialized and Cisco has not issued a public statement specifically addressing the ShinyHunters extortion claim. The deadline passage without publication, combined with CipherForce's infrastructure outage documented below, represents the second data point suggesting potential friction in the campaign's monetization pipeline.

The Cisco breach is significant because it is the highest-profile technology company confirmed as a direct victim of the Trivy supply chain compromise. The involvement of multiple threat actors in a single victim's environment is consistent with the credential-sharing pattern documented in [Update 006](https://isc.sans.edu/diary/32864). The theft of customer source code repositories for banks and US government agencies creates secondary exposure obligations for downstream organizations.

**Recommended action:** Organizations that are Cisco customers or partners, particularly those with source code or build artifacts hosted in Cisco's development infrastructure, should contact Cisco to determine whether their repositories were among those exfiltrated. Organizations using Cisco AI products should monitor for unauthorized use of stolen source code.

## MEDIUM: Google GTIG Formally Designates TeamPCP as UNC6780

Google Threat Intelligence Group (GTIG) has assigned the formal tracking designation **UNC6780** to TeamPCP. The designation appeared in GTIG's [analysis of the axios npm supply chain attack](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package), which attributed that separate compromise to North Korean threat actor UNC1069. In distinguishing the two campaigns, GTIG identified TeamPCP/UNC6780 as the financially motivated group responsible for the Trivy, Checkmarx, LiteLLM, and Telnyx compromises. GTIG also named TeamPCP's credential stealer payload as **SANDCLOCK**.

The UNC6780 designation is significant for three reasons. First, it confirms Google is formally tracking TeamPCP as a distinct, persistent threat actor rather than treating the campaign as a series of unrelated incidents. Second, UNC (uncategorized) designations in Google's taxonomy indicate the threat actor does not yet map to a known state-sponsored cluster, reinforcing the financially motivated assessment from earlier reporting. Third, the designation provides a standardized reference for cross-vendor threat intelligence sharing as multiple organizations (Mandiant, Wiz, Unit 42, Elastic, Datadog) independently track overlapping aspects of the campaign.

The [Google Cloud Threat Horizons H1 2026](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026) report also covers UNC6780. Analysts assess the formal GTIG tracking designation, combined with Mandiant's engagement on the LiteLLM forensics and their quantification of 1,000+ compromised SaaS environments, indicates Google considers UNC6780 a top-tier financially motivated threat actor.

**Recommended action:** Organizations using Google Chronicle, VirusTotal, or Mandiant Advantage should search for UNC6780 indicators in their environments. The SANDCLOCK designation provides a specific malware family name for detection rule authoring.

## MEDIUM: CipherForce Leak Infrastructure Goes Dark as Sportradar Deadline Approaches

CipherForce's two known Tor-based leak sites remain unavailable, confirmed via [ransomware tracking services](https://www.ransomware.live/group/cipherforce). The group has not posted new victims since February 23, 2026 (a gap of 44 days). This infrastructure outage coincides with the approaching Sportradar AG data publication deadline (approximately April 10-11), which was set when CipherForce first claimed the Sportradar breach around March 26-27.

Analysts assess three possible explanations: (1) the outage may be related to the internal friction and "mole hunt" [reported in Update 006](https://isc.sans.edu/diary/32864), suggesting operational disruption within the TeamPCP ecosystem is affecting CipherForce's ability to maintain infrastructure; (2) the sites may have been deliberately taken offline as an operational security measure following increased law enforcement and researcher attention; or (3) the outage may be temporary and unrelated to operational factors.

The Sportradar deadline remains the key near-term indicator. If CipherForce's infrastructure returns online with published Sportradar data around Ap...