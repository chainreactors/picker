---
title: UK Cybercrime Journal: Arup Group Breached by FulcrumSec
url: https://blog.bushidotoken.net/2026/06/uk-cybercrime-journal-arup-group.html
source: Over Security
date: 2026-06-10
fetch_date: 2026-06-11T06:36:34.535080
---

# UK Cybercrime Journal: Arup Group Breached by FulcrumSec

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: Arup Group Breached by FulcrumSec

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[June 10, 2026](https://blog.bushidotoken.net/2026/06/uk-cybercrime-journal-arup-group.html "permanent link")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiyov70-0z4GV7kgk9TPpSNvd33IpB2ZMS7dYLj_E8LCfrM1dgwgK-NLwdhtkvz9IlTPfzBzNFxy94ypz9dVBUrkN_iTfFVmrUtw_Ga4AsG3JYkYSbGRogD7vwaHbBQwDR4Ip6SOl7IoYnoG3fW5vgkxTZHGA4hmv1472tBsDpC_-wTPQhuZX0dkbmOSFN-=w640-h414)](https://blogger.googleusercontent.com/img/a/AVvXsEiyov70-0z4GV7kgk9TPpSNvd33IpB2ZMS7dYLj_E8LCfrM1dgwgK-NLwdhtkvz9IlTPfzBzNFxy94ypz9dVBUrkN_iTfFVmrUtw_Ga4AsG3JYkYSbGRogD7vwaHbBQwDR4Ip6SOl7IoYnoG3fW5vgkxTZHGA4hmv1472tBsDpC_-wTPQhuZX0dkbmOSFN-)

What Happened:

* On 10 May 2026, the UK-based firm Arup Group was listed as a victim on the Tor data leak site of FulcrumSec.
* On their Tor data leak site, FulcrumSec stated that they have exposed 700GB of GitHub repos and 2TB of Azure and AWS S3 cloud, plus database backups.
* Other types of data the adversary claims to have stolen includes Neuron BMS client databases, Odoo ERP data, A66 landowner files, Apple code-signing certificates with plaintext passwords, a Google Cloud Platform (GCP) project with production payment gateway credentials, and the source code of ArupCompute and Oasys.
* The FulcrumSec operators also claimed to have spent over half a year analysing the data and went through “email correspondence” with the company before publishing the stolen data.
* On the victim post, FulcrumSec wrote a detailed incident breakdown. In it, they stated they gained initial access in September 2025 via a GitHub personal access token found hardcoded in a JavaScript file on a forgotten subdomain, which provided access to over 10,000 private GitHub repositories belonging to Arup Group.
* From there, they scanned the repositories and found additional hardcoded tokens, API keys, and passwords for AWS, Azure, and databases.
* The adversary stated that Arup detected the Github and Azure Storage intrusions approximately six weeks after they happened and rotated the credentials, but it was too late as the data had been exfiltrated.
* FulcrumSec also stated they pivoted into the AWS infrastructure using keys they had found belonging to Arup’s subsidiary Neuron.
* FulcrumSec allegedly waited until April 2026 to contact their victim, Arup Group, due to the time it took to analyse the vast amounts of stolen data.
* Impacted client organisations of Arup Group were also mentioned in the post, such as Disney and several other Hong Kong companies. The adversary reportedly uncovered Amazon data center seismic fragility data, British Petroleum (BP) site selection coordinates, and Queensferry Crossing internal documents as well.
* Critically for the UK, the breached data exposed up to 62 HS2 related GitHub repositories. This involved Euston Station pile design files, ground movement assessments, over 14,000 sensor monitoring records, 48 archaeological site GPS coordinates (including Jones Hill Wood, a sensitive site for environmentalists), as well as confidential documents.

Analyst Comment:

Arup Group is a large multinational architectural design and engineering firm based in London who has been involved in constructing the Wembley Football Stadium in London, the HS1 Channel Tunnel Rail Link network, and the Eden Project in Cornwall, among other significant international construction projects.

Active since September 2025, FulcrumSec is a financially motivated data-theft-extortion group that specialises in rapid exfiltration of cloud-hosted databases by exploiting unrotated API keys and misconfigured cloud permissions.

This attack was noteworthy due to its highly targeted nature. FulcrumSec claimed they had access to Arup Group’s data for seven months and they clearly invested significant time to analyse the documents and spent weeks negotiating over email. Plus, to find initial access they also would have had to spend time checking Arup’s domains and Internet-facing assets to eventually find a single leaked credential to exploit. These types of targeted intrusions often only happen to large companies. This is because for it to be worth the cybercriminal’s time, effort, and risk to their freedom they will want a large ransom payment that only rich companies can typically afford.

FulcrumSec is an adversary worth monitoring due to the effort they put into their intrusions compared to other smash-and-grab ransomware campaigns. In October 2025, in a case [documented](https://x.com/vxunderground/status/1975629199323853027) by VX-Underground, FulcrumSec emailed detailed information about the breach they conducted with the aim of those details getting published and exert additional pressure on the victim.

Interestingly, FulcrumSec said the ransom they demanded was less than 1% of Arup’s annual revenue and was less than how much Arup lost to the deepfake fraudsters. This is a reference to Arup [reportedly](https://www.theguardian.com/technology/article/2024/may/17/uk-engineering-arup-deepfake-scam-hong-kong-ai-video) lost over £20 million pounds in 2024 after one of their Hong Kong employees was duped into sending cash to cybercriminals using an AI-generated video call. The fact Arup became publicly known for falling victim to a large scam potentially contributed to the adversary’s decision to select and focus them for this attack.

Defensive Takeaways:

* Asset Inventory and Shadow IT Audits: Identifying the outdated unused domains with hardcoded credentials is standard best practices. All organisations must have processes in place to catalog and retire systems to avoid incidents like this.
* Hardcoded Credentials in Code: They way FulcrumSec gained access demonstrates the importance of using secret environment variables and features like GitHub Secret Scanning.
* Implement Incident Response Procedures: Importantly, Arup detect the activity too late and it took them a staggering six weeks to rotate credentials (according to the adversary), which shows why having automated systems to check for unauthorised usage and reset tokens and all accounts is crucial to respond to such attacks.
* GitHub Activity Monitoring: The adversary claimed they were able to clone thousands of GitHub repositories containing sensitive data without being detected. These types of activities are available to monitor and detect in GitHub Audit Logs. It’s also important to have a plan in place when suspicious activities are detected.
* Third-Party Risk Management Programs: This incident also had some notable downstream impact. It shows why client organisations of another company’s services need to know what data and how much data is stored by third-parties for when such breaches occur. Knowing what’s potentially exposed will streamline the response to the incident.
* Deception Tech: Arup could have implemented a boobytraps for the adversary such as the use of [CanaryTokens](https://canarytokens.org/nest/) inside sensitive documents. As the adversary spent time analysing the Arup’s documents before contacting them, if they open a boobytrapped document, then the incident could been detected much earlier and the damages could have been reduced.

Relevant Sources:

1. [https://x.com/darkwebinformer/status/2053281385582891437](https://x.com/darkwebinformer/status/2053281385582891437?s=46&t=-dkNDSDHEzyAagaVN0SDgA)
2. <https://www.ransomware.live/id/QXJ1cCBHcm91cEBmdWxjcnVtc2Vj>
3. <https://en.wikipedia.org/wiki/Arup_Group>
4. <https://www.theguardian.com/technology/article/2024/may/17/uk-engineering-arup-deepfake-scam-hong-kong-ai-video>

Relevant CTI Resources:

1. <https://www.ransomware.live/group/fulcrumsec>
2. [https://x.com/vxunderground/status/1975629199323853027](https://x.com/vxunderground/status/1975629199323853027?s=46&t=-dkNDSDHEzyAagaVN0SDgA)
3. <https:/...