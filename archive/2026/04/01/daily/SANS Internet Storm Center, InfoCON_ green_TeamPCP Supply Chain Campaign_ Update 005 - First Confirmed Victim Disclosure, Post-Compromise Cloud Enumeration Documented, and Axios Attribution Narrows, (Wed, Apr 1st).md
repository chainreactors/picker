---
title: TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim Disclosure, Post-Compromise Cloud Enumeration Documented, and Axios Attribution Narrows, (Wed, Apr 1st)
url: https://isc.sans.edu/diary/rss/32856
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-01
fetch_date: 2026-04-02T04:31:30.640080
---

# TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim Disclosure, Post-Compromise Cloud Enumeration Documented, and Axios Attribution Narrows, (Wed, Apr 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32854)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim Disclosure, Post-Compromise Cloud Enumeration Documented, and Axios Attribution Narrows](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B005%2BFirst%2BConfirmed%2BVictim%2BDisclosure%2BPostCompromise%2BCloud%2BEnumeration%2BDocumented%2Band%2BAxios%2BAttribution%2BNarrows/32856/)

**Published**: 2026-04-01. **Last Updated**: 2026-04-01 13:08:26 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B005%2BFirst%2BConfirmed%2BVictim%2BDisclosure%2BPostCompromise%2BCloud%2BEnumeration%2BDocumented%2Band%2BAxios%2BAttribution%2BNarrows/32856/#comments)

This is the fifth update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). Update 004 covered developments through March 30, including the Databricks investigation, dual ransomware operations, and AstraZeneca data release. This update consolidates two days of intelligence through April 1, 2026.

## HIGH: Mercor AI Confirms Breach Tied to LiteLLM Supply Chain Compromise - First Official Victim Disclosure

AI recruiting startup Mercor has publicly confirmed it was breached as a direct consequence of the LiteLLM supply chain compromise, making it the **first organization to officially acknowledge being victimized** through the TeamPCP campaign. [TechCrunch](https://techcrunch.com/2026/03/31/mercor-says-it-was-hit-by-cyberattack-tied-to-compromise-of-open-source-litellm-project/) reported on March 31 that LAPSUS$ claims to have exfiltrated approximately 4TB of data, including 939GB of source code, a 211GB user database, and 3TB of video interviews and identity verification documents (passports). Initial access was reportedly via a compromised Tailscale VPN credential.

Mercor stated it was "one of thousands of companies" affected by the LiteLLM compromise. The nature of the claimed exfiltrated data -- which includes biometric identity verification materials -- raises significant privacy and regulatory implications under GDPR, CCPA, and potentially HIPAA depending on the contents.

This is operationally significant because it moves the campaign's downstream impact from theoretical to confirmed. Prior victim claims (AstraZeneca, Databricks) remain unconfirmed by the named organizations. Mercor's public acknowledgment validates what analysts have assessed since Update 002: the credential trove harvested during the supply chain phase is being actively exploited for data theft and extortion.

**Recommended action:** Organizations that used LiteLLM v1.82.7 or v1.82.8 should treat this as confirmation that credential exploitation is actively underway. If you have not completed credential rotation, the Mercor disclosure demonstrates the consequence of delay. VPN credentials, cloud access tokens, and API keys accessible in compromised environments should be prioritized for rotation.

## HIGH: Wiz Documents TeamPCP Post-Compromise AWS and Cloud Enumeration in the Wild

[SecurityWeek](https://www.securityweek.com/teampcp-moves-from-oss-to-aws-environments/) reported on March 31 that Wiz's Cloud Incident Response Team (CIRT) has published detailed findings on TeamPCP's post-compromise cloud operations in ["Tracking TeamPCP: Investigating Post-Compromise Attacks Seen in the Wild"](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild). This is the first detailed public documentation of what TeamPCP does after obtaining stolen credentials.

Key findings from the Wiz CIRT investigation:

* **Credential validation via TruffleHog:** TeamPCP uses the open-source secret scanning tool TruffleHog to programmatically verify that stolen AWS access keys, Azure application secrets, and SaaS tokens are still valid and in use.
* **24-hour operational tempo:** Within 24 hours of validating stolen secrets, the group transitions to discovery operations in compromised AWS environments.
* **AWS enumeration focus:** Discovery operations enumerate IAM roles, EC2 instances, Lambda functions, RDS databases, S3 buckets, and ECS clusters, with particular focus on container infrastructure where the group maps clusters and task definitions.
* **Bold operational signatures:** The group uses conspicuous resource names including "pawn" and "massive-exfil" -- analysts assess this indicates either operational carelessness or deliberate intimidation, consistent with their public Telegram messaging.

The Wiz findings also contextualize the Flare threat intelligence report, which found that TeamPCP's cloud infrastructure targeting breaks down as Azure (61%) and AWS (36%), accounting for 97% of compromised servers.

**Recommended action:** Organizations should search cloud audit logs for unauthorized IAM enumeration, EC2/ECS/Lambda discovery calls, and S3 listing operations originating from unfamiliar principals. TruffleHog validation attempts may appear as rapid sequential API calls testing credential validity across multiple services. Search for resources with names containing "pawn", "massive-exfil", or similar conspicuous strings.

**Note for threat hunters:** The [full Wiz CIRT report](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild) contains extensively documented indicators of compromise including specific AWS API call patterns, resource naming conventions, and infrastructure fingerprints observed in the wild. Threat hunters and SOC teams should review the Wiz report in detail for actionable detection content.

## MEDIUM: Axios npm Compromise Attributed to North Korean UNC1069 - Not TeamPCP, but Credential Source Remains Open

The axios npm compromise (March 30-31, malicious versions 1.14.1 and 0.30.4) has received formal attribution. [Elastic Security Labs](https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all) published a detailed analysis identifying the macOS Mach-O binary payload as overlapping with WAVESHAPER, a C++ backdoor that Mandiant attributes to **UNC1069, a suspected North Korean threat actor**. [Google's Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) published a companion analysis confirming the DPRK attribution.

This narrows the assessment from Update 004's "credential provenance raises TeamPCP questions" to a more specific picture: analysts assess with high confidence that **a different threat actor executed the axios attack**, but the question of how the maintainer's npm token was originally obtained remains unanswered. The token was a long-lived classic npm access token -- exactly the type that TeamPCP's CanisterWorm `findNpmTokens()` function harvests from CI/CD environments. The timing aligns with TeamPCP's monetization phase and the BreachForums credential distribution to approximately 300,000 users.

The SANS ISC Stormcast for [April 1, 2026](https://isc.sans.edu/podcastdetail/9874) noted: "Given that TeamPCP recently collected so many developer credentials, it's very possible that they were involved in the Axios compromise, though the follow-up compromise doesn't look like TeamPCP, as the techniques look a little bit different."

Singapore's Cyber Security Agency has issued a second advisory, [AD-2026-002](https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-002/), specifically addressing the axios supply chain attack -- making Singapore the only gov...