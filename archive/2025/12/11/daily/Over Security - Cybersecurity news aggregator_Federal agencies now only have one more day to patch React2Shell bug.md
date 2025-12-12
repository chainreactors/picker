---
title: Federal agencies now only have one more day to patch React2Shell bug
url: https://therecord.media/react4shell-vulnerability-cisa-shortens-patch-deadline
source: Over Security - Cybersecurity news aggregator
date: 2025-12-11
fetch_date: 2025-12-12T03:22:39.692105
---

# Federal agencies now only have one more day to patch React2Shell bug

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

![CISA logo](https://cms.therecord.media/uploads/format_webp/large_cisa_4_3264a23d22.jpg)

[Jonathan Greig](/author/jonathan-greig)December 11th, 2025

# Federal agencies now only have one more day to patch React2Shell bug

The amount of time federal agencies have to patch the recent React2Shell vulnerability has decreased significantly.

The Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2025-55182 — a vulnerability impacting a popular open-source tool built into thousands of widely used digital products — to its [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog late last week, giving federal agencies until December 26 to patch the bug.

The date is now  Friday. A spokesperson for CISA confirmed the date change and noted that CISA wanted federal agencies to “check for signs of potential compromise on all internet accessible REACT instances after applying mitigations.”

CISA’s patch deadlines are often an indicator of a bug’s severity for the industry in general. React2Shell affects React Server Components, a tool originally created for Facebook and now embedded in 50 million websites and products built by countless major companies.

Since December 3, cybersecurity defenders [have scrambled to patch CVE-2025-55182](https://therecord.media/chinese-hackers-exploiting-react2shell-vulnerability-amazon) due to the wide use of React Server Components.

Over the last week, defenders have seen [government-backed hackers from China](https://therecord.media/researchers-track-dozens-react2shell-vuln) and North Korea exploiting the bug alongside an array of cybercriminal groups.

Palo Alto Networks’ Unit 42 published a new advisory on Wednesday evening showing more than 50 organizations have been impacted by breaches sourced back to CVE-2025-55182.

The impacted organizations are in the U.S. as well as Asia, South America and the Middle East. Hackers are targeting financial services institutions, higher education, the tech industry, all levels of government and media organizations.

Unit 42 added that in addition to previously identified Chinese malware strains like Snowlight and Vshell, they are now seeing other malware used including NoodlerRat, XMRIG, BPFDoor, Autocolor, Mirai and Supershell.

Justin Moore, a senior official at Unit 42, told Recorded Future News that researchers have confirmed cases where attackers used CVE-2025-55182 to breach networks.

“We have observed opportunistic targeting and automated scripts for the installation of cryptominers and botnets, targeting AWS configuration keys, and more targeted installation of numerous robust backdoors previously associated with nation state affiliated actors,” Moore said.

Unit 42 also confirmed previous [reporting](https://www.sysdig.com/blog/etherrat-dprk-uses-novel-ethereum-implant-in-react2shell-attacks) by cybersecurity firm Sysdig that North Korean hackers are exploiting the bug to deliver malware and facilitate cryptocurrency theft.

Unit 42 added that it observed some hackers exploiting the bug using BPFDoor, a Linux backdoor attributed to a China-linked threat group known as Red Menshen.

The group was [previously accused](https://malpedia.caad.fkie.fraunhofer.de/actor/red_menshen) of targeting the telecommunications, finance and retail sectors, with attacks observed in South Korea, Hong Kong, Myanmar, Malaysia and Egypt. Unit 42 tracked several other backdoors and strains of malware used in attacks.

Other incident responders said they are now seeing low-skill, opportunistic abuse of the vulnerability across a variety of sectors.

Christiaan Beek, senior director of threat intelligence at Rapid7, said the company is witnessing cryptocurrency miners and Mirai botnet deployments exploiting the bug. He added that there are indicators linking the vulnerability’s exploitation to tooling previously used by ransomware groups.

Researchers at CyCognito shared data that showed media organizations had an inordinate amount of externally exposed assets running vulnerable React Server Components affected by CVE-2025-55182.

The company said news outlets, broadcast television stations, cable and satellite companies and more were exposed, likely because most media organizations use React in their frontend stacks.

“They rely heavily on server-rendered frameworks such as Next.js to run public entry points like homepages, article and video pages, section fronts, search results and campaign microsites,” the company told Recorded Future News.

“In many of these applications, React Server Components are used for server side data fetching, layout composition and streaming partial page updates. That puts the vulnerable react-server-dom-\* packages directly in the request path on exposed web assets.”

The company also found the manufacturing, technology and hospitality industries as having significant exposure to CVE-2025-55182.

* [Technology](/news/technology)
* [Malware](/news/malware)
* [News](/)
* [Cybercrime](/news/cybercrime)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [Vulnerability](/tag/vulnerability)
* [CISA](/tag/cisa)
* [federal government](/tag/federal-government)
* [China](/tag/china)
* [North Korea](/tag/north-korea)
* [React2Shell](/tag/React2Shell)
* [CVE-2025-55182](/tag/cve-2025-55182)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [New 'DroidLock' malware demands a ransom, locks user out of deviceDecember 11th, 2025](/android-droidlock-malware-demands-ransom-locks-mobile-device)
* [Hackers reportedly breach developer involved with Russia’s military draft databaseDecember 11th, 2025](/hackers-reportedly-breach-developer-involved-in-russian-military-database)
* [UK fines LastPass £1.2 million for data breach affecting 1.6 million peopleDecember 11th, 2025](/uk-fines-lastpass-over-1-million-data-breach)
* [Lawmaker calls facial recognition on doorbell cameras a ‘privacy nightmare’December 10th, 2025](/lawmaker-calls-facial-recognition-doorbell-cameras-privacy-nightmare)
* [US extradites member of Russian hacktivist group involved in critical infrastructure attacksDecember 10th, 2025](/us-extradites-member-of-russian-hacking-groups-critical-infrastructure)
* [Teen who allegedly stole millions of personal data records arrested in Spain December 10th, 2025](/spain-arrests-teen-suspect-data-theft-and-sale)
* [Trump plans executive order curbing state AI lawsDecember 8th, 2025](/trump-plans-ai-exec-order-curbing-state-laws)
* [Meta proposal for less data sharing is approved by European CommissionD...