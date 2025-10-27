---
title: U.S. Sanctions Cloud Provider ‘Funnull’ as Top Source of ‘Pig Butchering’ Scams
url: https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/
source: Krebs on Security
date: 2025-05-31
fetch_date: 2025-10-06T22:35:28.648777
---

# U.S. Sanctions Cloud Provider ‘Funnull’ as Top Source of ‘Pig Butchering’ Scams

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# U.S. Sanctions Cloud Provider ‘Funnull’ as Top Source of ‘Pig Butchering’ Scams

May 29, 2025

[14 Comments](https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/funnell-ss.png)

The U.S. government today imposed economic sanctions on **Funnull Technology Inc.**, a Philippines-based company that provides computer infrastructure for hundreds of thousands of websites involved in virtual currency investment scams known as “**pig butchering**.” In January 2025, KrebsOnSecurity detailed how Funnull was being used as a content delivery network that catered to cybercriminals seeking to route their traffic through U.S.-based cloud providers.

“Americans lose billions of dollars annually to these cyber scams, with revenues generated from these crimes rising to record levels in 2024,” reads [a statement](https://home.treasury.gov/news/press-releases/sb0149) from the **U.S. Department of the Treasury**, which sanctioned Funnull and its 40-year-old Chinese administrator **Liu Lizhi**. “Funnull has directly facilitated several of these schemes, resulting in over $200 million in U.S. victim-reported losses.”

The Treasury Department said Funnull’s operations are linked to the majority of virtual currency investment scam websites reported to the FBI. The agency said Funnull directly facilitated pig butchering and other schemes that resulted in more than $200 million in financial losses by Americans.

Pig butchering is a rampant form of fraud wherein people are lured by flirtatious strangers online into investing in fraudulent cryptocurrency trading platforms. Victims are coached to invest more and more money into what appears to be an extremely profitable trading platform, only to find their money is gone when they wish to cash out.

The scammers often insist that investors pay additional “taxes” on their crypto “earnings” before they can see their invested funds again (spoiler: they never do), and a shocking number of people [have lost six figures or more through these pig butchering scams](https://krebsonsecurity.com/2022/07/massive-losses-define-epidemic-of-pig-butchering/).

KrebsOnSecurity’s [January story on Funnull](https://krebsonsecurity.com/2025/01/infrastructure-laundering-blending-in-with-the-cloud/) was based on research from the security firm **Silent Push**, which discovered in October 2024 that a vast number of domains hosted via Funnull were promoting gambling sites that bore the logo of the **Suncity Group**, a Chinese entity named in [a 2024 UN report](https://www.unodc.org/roseap/uploads/documents/Publications/2024/Casino_Underground_Banking_Report_2024.pdf) (PDF) for laundering millions of dollars for the North Korean state-sponsored hacking group [Lazarus](https://en.wikipedia.org/wiki/Lazarus_Group).

Silent Push found Funnull was a criminal content delivery network (CDN) that carried a great deal of traffic tied to scam websites, funneling the traffic through a dizzying chain of auto-generated domain names and U.S.-based cloud providers before redirecting to malicious or phishous websites. The FBI has released a [technical writeup](https://www.ic3.gov/CSA/2025/250529.pdf) (PDF) of the infrastructure used to manage the malicious Funnull domains between October 2023 and April 2025.

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/funnull-network.png)

Silent Push [revisited Funnull’s infrastructure](https://www.silentpush.com/blog/infrastructure-laundering/) in January 2025 and found Funnull was still using many of the same **Amazon** and **Microsoft** cloud Internet addresses identified as malicious in its October report. Both Amazon and Microsoft pledged to rid their networks of Funnull’s presence following that story, but according to Silent Push’s **Zach Edwards** only one of those companies has followed through.

Edwards said Silent Push no longer sees Microsoft Internet addresses showing up in Funnull’s infrastructure, while Amazon continues to struggle with removing Funnull servers, including one that appears to have first materialized in 2023.

“Amazon is doing a terrible job — every day since they made those claims to you and us in our public blog they have had IPs still mapped to Funnull, including some that have stayed mapped for inexplicable periods of time,” Edwards said.

Amazon said its Amazon Web Services (AWS) hosting platform actively counters abuse attempts.

“We have stopped hundreds of attempts this year related to this group and we are looking into the information you shared earlier today,” reads a statement shared by Amazon. “If anyone suspects that AWS resources are being used for abusive activity, they can report it to AWS Trust & Safety using the report abuse form [here](https://support.aws.amazon.com/#/contacts/report-abuse).”

U.S. based cloud providers remain an attractive home base for cybercriminal organizations because many organizations will not be overly aggressive in blocking traffic from U.S.-based cloud networks, as doing so can result in blocking access to many legitimate web destinations that are also on that same shared network segment or host.

What’s more, funneling their bad traffic so that it appears to be coming out of U.S. cloud Internet providers allows cybercriminals to connect to websites from web addresses that are geographically close(r) to their targets and victims (to sidestep location-based security controls by your bank, for example).

Funnull is not the only cybercriminal infrastructure-as-a-service provider that was sanctioned this month: On May 20, 2025, the **European Union** [imposed sanctions](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500966) on **Stark Industries Solutions**, an ISP that materialized at the start of Russia’s invasion of Ukraine and has been used as a global proxy network that conceals the true source of cyberattacks and disinformation campaigns against enemies of Russia.

In May 2024, KrebsOnSecurity published [a deep dive on Stark Industries Solutions](https://krebsonsecurity.com/2024/05/stark-industries-solutions-an-iron-hammer-in-the-cloud/) that found much of the malicious traffic traversing Stark’s network (e.g. vulnerability scanning and password brute force attacks) was being bounced through U.S.-based cloud providers. My reporting showed how deeply Stark had penetrated U.S. ISPs, and that its co-founder for many years sold “bulletproof” hosting services that told Russian cybercrime forum customers they would proudly ignore any abuse complaints or police inquiries.

![](https://krebsonsecurity.com/wp-content/uploads/2024/05/stark-industries-solutions.png)

That story examined the history of Stark’s co-founders, Moldovan brothers **Ivan** and **Yuri Neculiti**, who each denied past involvement in cybercrime or any current involvement in assisting Russian disinformation efforts or cyberattacks. Nevertheless, the EU sanctioned both brothers as well.

The EU said Stark and the Neculti brothers “enabled various Russian state-sponsored and state-affiliated actors to conduct destabilising activities including coordinated information manipulation and interference and...