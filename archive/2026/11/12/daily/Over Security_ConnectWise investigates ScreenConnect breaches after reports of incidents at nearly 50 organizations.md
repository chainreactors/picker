---
title: ConnectWise investigates ScreenConnect breaches after reports of incidents at nearly 50 organizations
url: https://therecord.media/connectwise-screenconnect-breaches-third-party-tool
source: Over Security
date: 2026-11-12
fetch_date: 2026-11-13T09:07:21.703559
---

# ConnectWise investigates ScreenConnect breaches after reports of incidents at nearly 50 organizations

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

![ConnectWise logo](https://cms.therecord.media/uploads/large_connectwise_logo_df3804ab18.jpg)

[Jonathan Greig](/author/jonathan-greig)November 12th, 2026

# ConnectWise investigates ScreenConnect breaches after reports of incidents at nearly 50 organizations

IT management software company ConnectWise said it is investigating reports of unauthorized access to its customers following reports from multiple cybersecurity firms that almost 50 organizations had been breached through the company’s ScreenConnect tool.

Late on Wednesday evening, ConnectWise said it believes the activity is related to the abuse of an independent third-party extension installed in customer environments. The tool, RMM+, is an extension for ConnectWise ScreenConnect that allows external management tools to automate and control remote sessions through an API.

“We identified approximately 400 partner environments with at least one independently developed third-party extension from the RMM+ family installed. Their presence alone does not establish compromise,” the company said.

“These extensions provide an API capable of executing remote commands. Access to that API is protected by a passphrase configured by the partner during setup.”

The Tampa-based company told customers that threat actors were deploying additional remote-access software and also saw “potential compromise of technician workstations during interactive connections to affected devices. “

The company disabled RMM+ in the 400 customer environments and urged customers with on-premises systems to disable it themselves because ConnectWise cannot do it for them. All customers should verify that RMM+ is disabled.

Customers should also be wary of any ScreenConnect connections to suspected compromised devices, ConnectWise added.

“Disabling extensions and resetting credentials alone may not remove unauthorized software, persistence mechanisms, or access already established on endpoints,” the company said, warning of unusual sign-ins and repeated login failures.

ConnectWise initially said it identified five different third-party extensions that may be associated with the malicious activity but later traced it back to RMM+.

## Compromised credentials?

The advisories that prompted ConnectWise to act came after cybersecurity firm Huntress [said](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect) it saw 288 affected endpoints across 48 organizations targeted within 90 minutes. Huntress incident responders found commands tied to RMM+ across several ScreenConnect systems and confirmed that ConnectWise disabled RMM+ alongside four other third-party extensions.

“Huntress hasn’t seen evidence of a new vulnerability, but it’s still unclear how the attacker got panel access. Current telemetry points to compromised credentials or hijacked operator sessions to gain initial access, but Huntress’ researchers will update when they know more,” a Huntress spokesperson said.

In several attacks, the threat actors used compromised systems to create persistent backdoors and used infected endpoints to spread malware throughout a network when a technician connected to that compromised endpoint.

ScreenConnect is used widely by managed service providers that run company IT infrastructure and end-user systems.

Huntress and several other researchers said the attack campaign may be tied to a ConnectWise vulnerability discovered in September — CVE-2026-84869. The Cybersecurity and Infrastructure Security Agency [warned](https://cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog) that it was being exploited in September.

Blackpoint Cyber researchers Sam Decker and Nevan Beal told Recorded Future News that they were able to reverse engineer the toolkit the attackers used in the recent ScreenConnect attacks and said it involves the exploitation of CVE-2026-84869.

Both researchers noted that they tested the toolkit against a fully patched ScreenConnect client and confirmed the patch works — meaning those exploited were likely unpatched.

“Our testing confirmed that the exploit targets CVE-2026-84869 and that the existing patch successfully blocks it,” Decker and Beal added.

“But the toolkit also includes capabilities to hijack authenticated operator sessions and use legitimate ScreenConnect management features to push malicious code. Patching addresses the known exploit, but it doesn't eliminate the risks associated with a compromised operator session. Organizations need to protect those sessions and put additional safeguards around high-impact administrative actions.”

ConnectWise has repeatedly faced attacks from both [nation-states](https://therecord.media/connectwise-nation-state-attack-targeted-some-customers) and [cybercriminals](https://therecord.media/connectwise-screenconnect-bug-cybercrime-exploitation) in recent years. Last month, Microsoft warned that a Chinese government-aligned hacking group used automated tools to carry out a [supply chain attack on ConnectWise](https://therecord.media/connectwise-screenconnect-bug-cybercrime-exploitation).

Chinese government groups have [repeatedly targeted ScreenConnect](https://therecord.media/chinese-government-hacker-exploiting-bugs-to-target-defense-government-sectors) since 2024 because of its widespread use across U.S. businesses and government agencies.

* [Technology](/news/technology)
* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Cybercrime](/news/cybercrime)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [United to block customers from using AI agents, citing cyber threats November 12th, 2026](/united-airlines-to-block-customers-using-ai-agents)
* [Data breach at hearing aid giant Amplifon impacts thousandsNovember 9th, 2026](/amplifon-hearing-aid-company-data-breach)
* [Certificate authority DigiCert reports data breach involving business customer infoNovember 6th, 2026](/digicert-certificate-authority-reports-data-breach)
* [Social media giants sue California to overturn law shielding kids 15 and under from compulsive useNovember 5th, 2026](/social-media-giants-sue-california-over-social-media-law)
* [Canadian extradited to US for allegedly hacking schools in at least four statesNovember 4th, 2026](/canadian-nationals-accused-us-education-hacks-cryptomining)
* [Ukrainian news outlet Kyiv Independent hit by suspected Russian cyberattackNovember 4th, 2026](/ukraine-kyiv-independent-cyberattack)
* [Largest crypto exchange in Brazil confirms cyberattack as millions flow out of platformNovember 2nd, 2026](/mercado-bitcoin-brazil-cryptocurrency-heist)
* [Mic...