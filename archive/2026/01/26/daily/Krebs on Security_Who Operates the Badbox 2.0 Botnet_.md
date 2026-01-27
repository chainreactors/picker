---
title: Who Operates the Badbox 2.0 Botnet?
url: https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/
source: Krebs on Security
date: 2026-01-26
fetch_date: 2026-01-27T03:39:38.978394
---

# Who Operates the Badbox 2.0 Botnet?

Advertisement

[![](/b-knowbe4/44.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[![](/b-knowbe4/45.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who Operates the Badbox 2.0 Botnet?

January 26, 2026

[0 Comments](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#respond)

The cybercriminals in control of **Kimwolf** — a disruptive botnet that has infected more than 2 million devices — recently shared a screenshot indicating they’d compromised the control panel for **Badbox 2.0**, a vast China-based botnet powered by malicious software that comes pre-installed on many Android TV streaming boxes. Both the FBI and Google say they are hunting for the people behind Badbox 2.0, and thanks to bragging by the Kimwolf botmasters we may now have a much clearer idea about that.

Our first story of 2026, [The Kimwolf Botnet is Stalking Your Local Network](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/), detailed the unique and highly invasive methods Kimwolf uses to spread. The story warned that the vast majority of Kimwolf infected systems were unofficial Android TV boxes that are typically marketed as a way to watch unlimited (pirated) movie and TV streaming services for a one-time fee.

Our January 8 story, [Who Benefitted from the Aisuru and Kimwolf Botnets?](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/), cited multiple sources saying the current administrators of Kimwolf went by the nicknames “**Dort**” and “**Snow**.” Earlier this month, a close former associate of Dort and Snow shared what they said was a screenshot the Kimwolf botmasters had taken while logged in to the Badbox 2.0 botnet control panel.

That screenshot, a portion of which is shown below, shows seven authorized users of the control panel, including one that doesn’t quite match the others: According to my source, the account — “**ABCD**” (the account that is logged in and listed in the top right of the screenshot) — belongs to Dort, who somehow figured out how to add their email address as a valid user of the Badbox 2.0 botnet.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/01/badboxpanel.png)](https://krebsonsecurity.com/wp-content/uploads/2026/01/badboxpanel.png)

The control panel for the Badbox 2.0 botnet lists seven authorized users and their email addresses. Click to enlarge.

Badbox has a storied history that well predates Kimwolf’s rise in October 2025. In July 2025, Google filed a “John Doe” [lawsuit](https://storage.courtlistener.com/recap/gov.uscourts.nysd.643466/gov.uscourts.nysd.643466.22.0.pdf) (PDF) against 25 unidentified defendants accused of operating Badbox 2.0, which Google described as a botnet of over ten million unsanctioned Android streaming devices engaged in advertising fraud. Google said Badbox 2.0, in addition to compromising multiple types of devices prior to purchase, also can infect devices by requiring the download of malicious apps from unofficial marketplaces.

Google’s lawsuit came on the heels of a [June 2025 advisory](https://www.ic3.gov/PSA/2025/PSA250605) from the **Federal Bureau of Investigation** (FBI), which warned that cyber criminals were gaining unauthorized access to home networks by either configuring the products with malware prior to the user’s purchase, or infecting the device as it downloads required applications that contain backdoors — usually during the set-up process.

The FBI said Badbox 2.0 was discovered after [the original Badbox campaign](https://www.humansecurity.com/learn/blog/trojans-all-the-way-down-badbox-and-peachpit/) was disrupted in 2024. The original Badbox was identified in 2023, and primarily consisted of Android operating system devices (TV boxes) that were compromised with backdoor malware prior to purchase.

KrebsOnSecurity was initially skeptical of the claim that the Kimwolf botmasters had hacked the Badbox 2.0 botnet. That is, until we began digging into the history of the qq.com email addresses in the screenshot above.

## CATHEAD

An online search for the address **34557257@qq.com** (pictured in the screenshot above as the user “**Chen**“) shows it is listed as a point of contact for a number of China-based technology companies, including:

–**Beijing Hong Dake Wang Science & Technology Co Ltd.**
–**Beijing Hengchuang Vision Mobile Media Technology Co. Ltd.**
–**Moxin Beijing Science and Technology Co. Ltd.**

The website for Beijing Hong Dake Wang Science is **asmeisvip[.]net**, a domain that was flagged in a [March 2025 report](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/) by **HUMAN Security** as one of several dozen sites tied to the distribution and management of the Badbox 2.0 botnet. Ditto for **moyix[.]com**, a domain associated with Beijing Hengchuang Vision Mobile.

A search at the breach tracking service **Constella Intelligence** finds 34557257@qq.com at one point used the password “**cdh76111**.” Pivoting on that password in Constella shows it is known to have been used by just two other email accounts: **daihaic@gmail.com** and **cathead@gmail.com**.

Constella found cathead@gmail.com registered an account at jd.com (China’s largest online retailer) in 2021 under the name “陈代海,” which translates to “**Chen Daihai**.” According to **DomainTools.com**, the name Chen Daihai is present in the original registration records (2008) for moyix[.]com, along with the email address **cathead@astrolink[.]cn**.

Incidentally, astrolink[.]cn also is among the Badbox 2.0 domains identified in [HUMAN Security’s 2025 report](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/). DomainTools finds cathead@astrolink[.]cn was used to register more than a dozen domains, including **vmud[.]net**, yet another Badbox 2.0 domain tagged by HUMAN Security.

## XAVIER

A cached copy of astrolink[.]cn preserved at archive.org shows the website belongs to a mobile app development company whose full name is **Beijing Astrolink Wireless Digital Technology Co. Ltd**. The archived website reveals [a “Contact Us” page](https://web.archive.org/web/20070317191651/http%3A//www.astrolink.cn/contact/index.htm) that lists a Chen Daihai as part of the company’s technology department. The other person featured on that contact page is **Zhu Zhiyu**, and their email address is listed as **xavier@astrolink[.]cn**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/beijingastrolink.png)

A Google-translated version of Astrolink’s website, circa 2009. Image: archive.org.

Astute readers will notice that the user **Mr.Zhu** in the Badbox 2.0 panel used the email address **xavierzhu@qq.com**. Searching this address in Constella reveals a jd.com account registered in the name of Zhu Zhiyu. A rather unique password used by this account matches the password used by the address **xavierzhu@gmail.com**, which DomainTools finds was the original registrant of astrolink[.]cn.

## ADMIN

The very first account listed in the Badbox 2.0 panel — “admin,” registered in November 2020 — used the email address **189308024@qq.com**. DomainTools shows this email is found in the 2022 registration records for the domain **guilincloud[.]cn**, which includes the registrant name “**Huang Guilin**.”

Constella finds 189308024@qq.com is associated with the China phone number **18681627767**. The breach tracking service **osint.industries** re...