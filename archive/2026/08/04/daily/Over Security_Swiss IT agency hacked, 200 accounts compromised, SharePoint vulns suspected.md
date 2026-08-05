---
title: Swiss IT agency hacked, 200 accounts compromised, SharePoint vulns suspected
url: https://therecord.media/swiss-bit-foitt-hacked-possibly-sharepoint-vulnerabilities
source: Over Security
date: 2026-08-04
fetch_date: 2026-08-05T04:59:54.680127
---

# Swiss IT agency hacked, 200 accounts compromised, SharePoint vulns suspected

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

![Swiss FOITT (BIT) buildings in Zollikofen](https://cms.therecord.media/uploads/large_FOITT_buildings_in_Zollikofen_2f35b57d71.jpg)

Federal Office of Information Technology, Systems and Telecommunication buildings in Zollikofen, Switzerland. Image: Wikimedia Commons / CC0 1.0

[Alexander Martin](/author/alexander-martin)August 4th, 2026

# Swiss IT agency hacked, 200 accounts compromised, SharePoint vulns suspected

Switzerland’s Federal Office for Information Technology and Communications (BIT) disclosed Tuesday that hackers had compromised approximately 200 accounts on its on-premises SharePoint servers.

The agency made the announcement a week after security specialists first detected anomalies on the on-premises Microsoft servers. It did not confirm how the hackers got in but acknowledged several vulnerabilities affecting SharePoint had been identified in July’s [Patch Tuesday](https://therecord.media/microsoft-vulnerabilities-patch-tuesday-release) release.

“The cyberattack was carried out by previously unknown actors, presumably by exploiting these vulnerabilities in the SharePoint software,” the Swiss agency said.

Several of the vulnerabilities have been added to the U.S. Cybersecurity and Infrastructure Security Agency’s Known Exploited Vulnerabilities catalog, although neither Microsoft nor CISA have publicly attributed the exploitations to any specific threat group.

The Swiss agency said its initial analyses “have shown no indication that any data beyond the compromised login credentials” was accessed, although it cautioned this analysis is ongoing. It added that “no confidential information or particularly sensitive personal data may be stored on the SharePoint platform.”

SharePoint is a prime target for both financially motivated hackers as well as state-sponsored groups seeking intelligence. The service — as well as often being used to store confidential documents — is deeply integrated with Microsoft’s authentication services, meaning skillful enough hackers could use a foothold there to burrow deeper into their victims’ networks.

Both user and technical accounts were compromised at the Swiss agency, which said that on the same day the anomalous access was detected, blocked internet access to SharePoint and patched the vulnerabilities.

Organizations in both the private and public sectors have issued alerts about July’s SharePoint issues. CERT-EU [stated](https://cert.europa.eu/publications/security-advisories/2026-009/): “Given the number of recent critical vulnerabilities affecting SharePoint, organizations should reconsider exposing any Microsoft SharePoint Server directly to the internet.”

CISA [warned](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations) that attackers exploiting the flaws were extracting machine keys from Microsoft's Internet Information Services (IIS) — the web server underpinning SharePoint — granting them the cryptographic secrets used to sign session tokens and establish persistence.

Once stolen, those keys let an attacker forge legitimate-looking requests that a fully patched server will still accept, meaning a credential leak on a SharePoint server can outlive the patch that closed the original hole.

CISA, CERT-EU and other national CERTs stressed the need to rotate machine keys and restart IIS rather than simply apply the patch. The BIT said it was reinstalling the affected SharePoint servers as a preventative measure.

* [Government](/news/government)
* [News](/)
* [Technology](/news/technology)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com?utm_source=therecord&utm_medium=referral&utm_content=display)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com?utm_source=therecord&utm_medium=referral&utm_content=display)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [Hackers steal 31,000 records identifying people behind Liechtenstein companies, foundationsAugust 3rd, 2026](/hackers-steal-records-liechtenstein-companies-foundations)
* [Biotech giant Amgen says patient data stolen from third-party cloud systemsAugust 3rd, 2026](/amgen-hackers-cyberattack-sec)
* [Semiconductor chip titan Analog Devices reports data breachJuly 30th, 2026](/analog-devices-semiconductor-company-data-breach)
* [Laundry Bear’s webmail hackers had more in store after February, report saysJuly 29th, 2026](/russia-hackers-outlook-webmail-malware)
* [Outdated VPNs should be purged from federal agencies, senator saysJuly 27th, 2026](/federal-purge-outdated-vpns-wyden-letter)
* [State Department imposes visa restrictions on foreign cyber scammersJuly 23rd, 2026](/visa-restrictions-cyber-scammers)
* [Major Australian energy supplier confirms customer data compromisedJuly 23rd, 2026](/australia-origin-energy-data-breach)
* [Swiss train maker Stadler refuses Everest $12 million ransomware demandJuly 22nd, 2026](/stadler-refuses-everest-ransom-demand)
* [Federal agencies broaden alert on Iran-linked OT attacksJuly 22nd, 2026](/federal-agencies-broaden-alert-on-iran-linked-ot-attacks)

[## Iran War’s Secondary Effects Shape 2026 US Violent Extremism

![Iran War’s Secondary Effects Shape 2026 US Violent Extremism](https://www.recordedfuture.com/research/media_1dcf334a3456dbd8cac9e92251d42bca36328dc3e.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/iran-violent-extremism-landscape)

[## TAG-195 Upgrades MaaS Ecosystem with Modular Tools

![TAG-195 Upgrades MaaS Ecosystem with Modular Tools](https://www.recordedfuture.com/research/media_108cee2fcb0c1792cbb340558328d069bb0036624.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/tag-195-evolves-maas-ecosystem)

[## AI Has Enhanced Iran’s Asymmetric Playbook During the 2026 Conflict

![AI Has Enhanced Iran’s Asymmetric Playbook During the 2026 Conflict](https://www.recordedfuture.com/research/media_1541a712e2eff6d3bec5ee1570a181ea75e5b0449.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/iran-ai-asymmetric-playbook)

[## Iran-Nexus TAG-182 Disseminates MarkiRAT Surveillance Tool

![Iran-Nexus TAG-182 Disseminates MarkiRAT Surveillance Tool](https://www.recordedfuture.com/research/media_11d60acbcd8901a8e5c5002f7f21ae6e799acee43.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/nexus-tag182-disseminates-markirat)

[## Evaluating Mexico’s New Cybersecurity Plan

![Evaluating Mexico’s New Cybersecurity Plan](https://www.recordedfuture.com/research/media_1b8b72fdb1296a02f886b14807628c7e71bb6f857.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/mexico-new-cybersecurity-plan-evaluation)

[![The Record from Recorded Future News](https://cms...