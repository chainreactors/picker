---
title: CISA releases warning about Windows Server Update Service bug, orders agencies to patch
url: https://therecord.media/wsus-vulnerability-cisa-late-friday-warning
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:08:50.122591
---

# CISA releases warning about Windows Server Update Service bug, orders agencies to patch

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

![CISA](https://cms.therecord.media/uploads/format_webp/large_cisa_code_background_cdd6a475aa.jpg)

[Jonathan Greig](/author/jonathan-greig)October 27th, 2025

# CISA releases warning about Windows Server Update Service bug, orders agencies to patch

Federal agencies and businesses are being urged to immediately patch a vulnerability affecting a widely used Windows update tool after experts warned that it is being exploited by hackers.

The Cybersecurity and Infrastructure Security Agency (CISA) sent out an urgent [alert](https://www.cisa.gov/news-events/alerts/2025/10/24/microsoft-releases-out-band-security-update-mitigate-windows-server-update-service-vulnerability-cve) on Friday evening about CVE-2025-59287 — a vulnerability Microsoft included in its monthly set of security updates about two weeks ago.

The vulnerability affects the Windows Server Update Service (WSUS) in Windows Server versions 2012, 2016, 2019, 2022 and 2025. CISA said a “prior update did not fully mitigate” the vulnerability, which carries a severity score of 9.8 out of 10.

WSUS is used by IT teams to manage updates for Microsoft products, offering users a way to distribute updates published through Microsoft Update.

Nick Andersen, executive assistant director for the cybersecurity division at CISA, said that while there is no evidence of compromise within federal networks, “the threat from these actors is real.”

“Organizations should immediately apply Microsoft’s out-of-band patch and follow mitigation guidance to protect their systems,” he said in a statement on Saturday.

Cybersecurity expert Benjamin Harris told Recorded Future News on Friday that his team at security firm watchTowr was seeing “indiscriminate, in-the-wild exploitation” of the bug. Incident responders at [Huntress](https://www.huntress.com/blog/exploitation-of-windows-server-update-services-remote-code-execution-vulnerability) and [Palo Alto Network’s Unit42](https://x.com/Unit42_Intel/status/1981878899878285561) also confirmed that they have seen exploitation of the bug.

On October 14, Microsoft [said](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-59287) the bug had not been exploited but put “exploitation more likely” in the advisory. The company updated the page on Friday, providing guidance for how customers can patch the vulnerability.

Microsoft noted that it updated parts of the advisory “after confirming the availability of publicly disclosed [proof of concept] code for this CVE.” A Microsoft spokesperson said the company “re-released this CVE after identifying that the initial update did not fully mitigate the issue.”

CISA [ordered](https://www.cisa.gov/news-events/alerts/2025/10/24/cisa-adds-two-known-exploited-vulnerabilities-catalog) all federal agencies to patch the bug by November 14 but said in the Friday advisory that it “strongly urges organizations to implement Microsoft’s updated [Windows Server Update Service (WSUS) Remote Code Execution Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59287) guidance, or risk an unauthenticated actor achieving remote code execution with system privileges.”

CISA also said organizations with affected products should take several immediate actions including identifying servers that may be vulnerable to exploitation, applying updates and rebooting the servers.

For organizations that cannot apply the update immediately, they should block inbound traffic to certain ports.

Harris said on Friday that exploitation of the bug has been indiscriminate so far.

“If an unpatched WSUS instance is online, at this stage it has likely already been compromised. There really is no legitimate reason in 2025 to have WSUS accessible from the Internet — any organization in that situation likely needs guidance to understand how they ended up in this position,” he said.

He added that he has seen thousands of instances exposed to the internet, including several “extremely sensitive, high-value organizations.”

“This isn’t limited to low-risk environments – some of the affected entities are exactly the types of targets attackers prioritize,” he said.

Huntress published a [blog post](https://www.huntress.com/blog/exploitation-of-windows-server-update-services-remote-code-execution-vulnerability) on Friday that said at least four of its customers were attacked through the vulnerability after exploitation attempts began on Thursday evening.

Two weeks ago, Immersive’s senior director of threat research, Kev Breen, [warned](https://www.immersivelabs.com/resources/blog/patch-tuesday-october-2025) that WSUS is a trusted Windows service that is designed to update files across the file system. The bug would allow an attacker to “have free rein over the operating system and could potentially bypass some [endpoint detection and response] detections that ignore or exclude the WSUS service.”

“Whilst not being actively exploited in the wild, one for patching sooner rather than later is,  ironically, the Windows update service (WSUS) itself,” he said at the time.

* [Government](/news/government)
* [Industry](/)
* [News](/)
* [Technology](/news/technology)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [Windows](/tag/windows)
* [Vulnerability](/tag/vulnerability)
* [patch](/tag/patch)
* [CISA](/tag/cisa)
* [Windows Server](/tag/windows-server)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Sweden’s power grid operator confirms data breach claimed by ransomware gangOctober 27th, 2025](/sweden-power-grid-operator-data)
* [Cyberattack on Russia’s food safety agency reportedly disrupts product shipmentsOctober 24th, 2025](/russia-food-safety-agency-rosselkhoznadzor-ddos-attack)
* [Tinder to expand face verification tech to more statesOctober 23rd, 2025](/tinder-face-check-tool-expanding-to-more-states)
* [Former Polish official indicted over spyware purchaseOctober 23rd, 2025](/former-polish-official-indicted-spyware-probe)
* [Phishing campaign across Mideast, North Africa is attributed to Iranian groupOctober 23rd, 2025](/iran-muddywater-phishing-campaign-north-africa-middle-east)
* [State attorneys general stepping up privacy enforcement, watchdog findsOctober 22nd, 2025](/state-ags-enforcement-privacy-law)
* [Jaguar Land Rover cyberattack cost $2.5 billion, says monitoring groupOctober 22nd, 2025](/jaguar-land-rover-cyberattack-economic-impact)
* [Google finds Russian state hackers replacing burned malware with new toolsOctober 21st, 2025](/coldriver-callisto-russia-hackers-new-malware-google)
* [Japanes...