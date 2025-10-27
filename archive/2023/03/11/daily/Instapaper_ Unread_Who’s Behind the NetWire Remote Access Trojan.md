---
title: Who’s Behind the NetWire Remote Access Trojan
url: https://krebsonsecurity.com/2023/03/whos-behind-the-netwire-remote-access-trojan/
source: Instapaper: Unread
date: 2023-03-11
fetch_date: 2025-10-04T09:18:59.261041
---

# Who’s Behind the NetWire Remote Access Trojan

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who’s Behind the NetWire Remote Access Trojan?

March 9, 2023

[29 Comments](https://krebsonsecurity.com/2023/03/whos-behind-the-netwire-remote-access-trojan/#comments)

A Croatian national has been arrested for allegedly operating **NetWire**, a Remote Access Trojan (RAT) marketed on cybercrime forums since 2012 as a stealthy way to spy on infected systems and siphon passwords. The arrest coincided with a seizure of the NetWire sales website by the **U.S. Federal Bureau of Investigation** (FBI). While the defendant in this case hasn’t yet been named publicly, the NetWire website has been leaking information about the likely true identity and location of its owner for the past 11 years.

![](https://krebsonsecurity.com/wp-content/uploads/2023/03/wwls.png)

Typically installed by [booby-trapped Microsoft Office documents](https://unit42.paloaltonetworks.com/guloader-installing-netwire-rat/) and distributed via email, **NetWire** is a multi-platform threat that is capable of targeting not only **Microsoft Windows** machines but also **Android**, **Linux** and **Mac** systems.

NetWire’s reliability and relatively low cost ($80-$140 depending on features) has made it an extremely popular RAT on the cybercrime forums for years, and NetWire infections consistently rank among the [top 10 most active RATs in use](https://decoded.avast.io/threatresearch/avast-q4-2022-threat-report/).

NetWire has been sold openly on the same website since 2012: **worldwiredlabs[.]com**. That website now features a seizure notice from the **U.S. Department of Justice** (DOJ), which says the domain was taken as part of “a coordinated law enforcement action taken against the NetWire Remote Access Trojan.”

“As part of this week’s law enforcement action, authorities in Croatia on Tuesday arrested a Croatian national who allegedly was the administrator of the website,” reads [a statement](https://www.justice.gov/usao-cdca/pr/federal-authorities-seize-internet-domain-selling-malware-used-illegally-control-and) by the DOJ today. “This defendant will be prosecuted by Croatian authorities. Additionally, law enforcement in Switzerland on Tuesday seized the computer server hosting the NetWire RAT infrastructure.”

Neither the DOJ’s statement nor [a press release](https://www-index-hr.translate.goog/vijesti/clanak/kod-zagreba-uhicen-haker-hrvatskoj-policiji-u-istrazi-pomogao-fbi/2445145.aspx?index_tid=328489&index_ref=naslovnica_vijesti_ostalo_d&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) on the operation published by Croatian authorities mentioned the name of the accused. But it’s fairly remarkable that it has taken so long for authorities in the United States and elsewhere to move against NetWire and its alleged proprietor, given that the RAT’s author apparently did very little to hide his real-life identity.

The WorldWiredLabs website first came online in February 2012 using a dedicated host with no other domains. The site’s true WHOIS registration records have always been hidden by privacy protection services, but there are plenty of clues in historical Domain Name System (DNS) records for WorldWiredLabs that point in the same direction.

In October 2012, the WorldWiredLabs domain moved to another dedicated server at the Internet address 198.91.90.7, which was home to just one other domain: **printschoolmedia[.]org**, also registered in 2012.

According to [DomainTools.com](https://www.domaintools.com), printschoolmedia[.]org was registered to a **Mario Zanko** in Zapresic, Croatia, and to the email address **zankomario@gmail.com**. DomainTools further shows this email address was used to register one other domain in 2012: **wwlabshosting[.]com**, also registered to Mario Zanko from Croatia.

A review of DNS records for both printschoolmedia[.]org and wwlabshosting[.]com shows that while these domains were online they both used the DNS name server **ns1.worldwiredlabs[.]com**. No other domains have been recorded using that same name server.

![](https://krebsonsecurity.com/wp-content/uploads/2023/03/wwl2013.png)

The WorldWiredLabs website, in 2013. Source: Archive.org.

DNS records for worldwiredlabs[.]com also show the site forwarded incoming email to the address **tommaloney@ruggedinbox.com**. [Constella Intelligence](https://www.constellaintelligence.com), a service that indexes information exposed by public database leaks, shows this email address was used to register an account at the clothing retailer romwe.com, using the password “**123456xx**.”

Running a reverse search on this password in Constella Intelligence shows there are more than 450 email addresses known to have used this credential, and two of those are **zankomario@gmail.com** and **zankomario@yahoo.com**.

A search on zankomario@gmail.com in **Skype** returns three results, including the account name “Netwire” and the username “**Dugidox**,” and another for a Mario Zanko (username zanko.mario).

![](https://krebsonsecurity.com/wp-content/uploads/2023/03/zankomarioskype.png)Dugidox corresponds to the hacker handle most frequently associated with NetWire sales and support discussion threads on multiple cybercrime forums over the years.

Constella ties dugidox@gmail.com to a number of website registrations, including the Dugidox handle on BlackHatWorld and HackForums, and to IP addresses in Croatia for both. Constella also shows the email address zankomario@gmail.com used the password “dugidox2407.”

In 2010, someone using the email address dugidox@gmail.com registered the domain **dugidox[.]com**. The WHOIS registration records for that domain list a “Senela Eanko” as the registrant, but the address used was the same street address in Zapresic that appears in the WHOIS records for printschoolmedia[.]org, which is registered in Mr. Zanco’s name.

Prior to the demise of **Google+**, the email address dugidox@gmail.com mapped to an account with the nickname “**Netwire wwl**.” The dugidox email also was tied to a Facebook account (**mario.zanko3**), which featured check-ins and photos from various places in Croatia.

That Facebook profile is no longer active, but back in January 2017, the administrator of WorldWiredLabs posted that he was considering adding certain Android mobile functionality to his service. Three days after that, the Mario.Zank3 profile posted a photo saying he was selected for an Android instruction course — with his dugidox email in the photo, naturally.

Incorporation records from the U.K.’s Companies House show that in 2017 Mr. Zanko became an officer in a company called **Godbex Solutions LTD**. A [Youtube video](https://www.youtube.com/watch?v=jO_qmXaiJ98) invoking this corporate name describes Godbex as a “next generation platform” for exchanging gold and cryptocurrencies.

The U.K. Companies House records show Godbex was dissolved in 2020. It also says Mr. Zanko was born in July 1983, and lists his occupation as “electrical engineer.”

A statement from the Croatian police about the NetWire takedown is [here](https://policija.gov.hr/vijesti/u-sklopu-medjunarodne-policijske-akcije-hrvatska-policija-uhitila-hakera-s-podrucja-zagrebacke-zupanije/6944).

**Update, Oct. 26, 11:11 a.m. ET:** Mario Zanko...