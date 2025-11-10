---
title: Drilling Down on Uncle Sam’s Proposed TP-Link Ban
url: https://krebsonsecurity.com/2025/11/drilling-down-on-uncle-sams-proposed-tp-link-ban/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-09
fetch_date: 2025-11-10T03:18:12.725678
---

# Drilling Down on Uncle Sam’s Proposed TP-Link Ban

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Drilling Down on Uncle Sam’s Proposed TP-Link Ban

November 9, 2025

[11 Comments](https://krebsonsecurity.com/2025/11/drilling-down-on-uncle-sams-proposed-tp-link-ban/#comments)

The U.S. government is reportedly preparing to ban the sale of wireless routers and other networking gear from **TP-Link Systems**, a tech company that currently enjoys an estimated 50% market share among home users and small businesses. Experts say while the proposed ban may have more to do with TP-Link’s ties to China than any specific technical threats, much of the rest of the industry serving this market also sources hardware from China and ships products that are insecure fresh out of the box.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/tplinkrouter.png)

**The Washington Post** recently [reported](https://www.washingtonpost.com/technology/2025/10/30/tp-link-proposed-ban-commerce-department/) that more than a half-dozen federal departments and agencies were backing a proposed ban on future sales of TP-Link devices in the United States. The story said **U.S. Department of Commerce** officials concluded TP-Link Systems products pose a risk because the U.S.-based company’s products handle sensitive American data and because the officials believe it remains subject to jurisdiction or influence by the Chinese government.

TP-Link Systems denies that, saying that it fully split from the Chinese TP-Link Technologies over the past three years, and that its critics have vastly overstated the company’s market share (TP-Link puts it at around 30 percent). TP-Link says it has headquarters in California, with a branch in Singapore, and that it manufactures in Vietnam. The company says it researches, designs, develops and manufactures everything except its chipsets in-house.

TP-Link Systems told The Post it has sole ownership of some engineering, design and manufacturing capabilities in China that were once part of China-based TP-Link Technologies, and that it operates them without Chinese government supervision.

“TP-Link vigorously disputes any allegation that its products present national security risks to the United States,” Ricca Silverio, a spokeswoman for TP-Link Systems, said in a statement. “TP-Link is a U.S. company committed to supplying high-quality and secure products to the U.S. market and beyond.”

Cost is a big reason TP-Link devices are so prevalent in the consumer and small business market: As [this February 2025 story](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.wired.com/story/tp-link-router-ban-investigation/&ved=2ahUKEwiVofql3OCQAxV7FFkFHVOHEAUQFnoECB0QAQ&usg=AOvVaw3r1EyJFoMB-2kJYtKQlvQB) from **Wired** observed regarding the proposed ban, TP-Link has long had a reputation for flooding the market with devices that are considerably cheaper than comparable models from other vendors. That price point (and consistently excellent performance ratings) has made TP-Link a favorite among Internet service providers (ISPs) that provide routers to their customers.

In August 2024, the chairman and the ranking member of the House Select Committee on the Strategic Competition Between the United States and the Chinese Communist Party called for an investigation into TP-Link devices, which they said were found on U.S. military bases and for sale at exchanges that sell them to members of the military and their families.

“TP-Link’s unusual degree of vulnerabilities and required compliance with PRC law are in and of themselves disconcerting,” the House lawmakers warned in [a letter](https://selectcommitteeontheccp.house.gov/sites/evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/2024-08-13%20Letter%20to%20Commerce%20re%20TP-Link%20%28filed%29.pdf) (PDF) to the director of the Commerce Department. “When combined with the PRC government’s common use of SOHO [small office/home office] routers like TP-Link to perpetrate extensive cyberattacks in the United States, it becomes significantly alarming.”

The letter cited [a May 2023 blog post](https://blog.checkpoint.com/security/check-point-research-reveals-a-malicious-firmware-implant-for-tp-link-routers-linked-to-chinese-apt-group/) by **Check Point Research** about a Chinese state-sponsored hacking group dubbed “**Camaro Dragon**” that used a malicious firmware implant for some TP-Link routers to carry out a sequence of targeted cyberattacks against European foreign affairs entities. Check Point said while it only found the malicious firmware on TP-Link devices, “the firmware-agnostic nature of the implanted components indicates that a wide range of devices and vendors may be at risk.”

In [a report](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/) published in October 2024, **Microsoft** said it was tracking a network of compromised TP-Link small office and home office routers that has been abused by multiple distinct Chinese state-sponsored hacking groups since 2021. Microsoft found the hacker groups were leveraging the compromised TP-Link systems to conduct “password spraying” attacks against Microsoft accounts. Password spraying involves rapidly attempting to access a large number of accounts (usernames/email addresses) with a relatively small number of commonly used passwords.

TP-Link rightly points out that most of its competitors likewise source components from China. The company also correctly notes that advanced persistent threat (APT) groups from China and other nations have leveraged vulnerabilities in products from their competitors, such as Cisco and Netgear.

But that may be cold comfort for TP-Link customers who are now wondering if it’s smart to continue using these products, or whether it makes sense to buy more costly networking gear that might only be marginally less vulnerable to compromise.

Almost without exception, the hardware and software that ships with most consumer-grade routers includes a number of default settings that need to be changed before the devices can be safely connected to the Internet. For example, bring a new router online without changing the default username and password and chances are it will only take a few minutes before it is probed and possibly compromised by some type of Internet-of-Things botnet. Also, it is incredibly common for the firmware in a brand new router to be dangerously out of date by the time it is purchased and unboxed.

Until quite recently, the idea that router manufacturers should make it easier for their customers to use these products safely was something of anathema to this industry. Consumers were largely left to figure that out on their own, with predictably disastrous results.

But over the past few years, many manufacturers of popular consumer routers have begun forcing users to perform basic hygiene — such as changing the default password and updating the internal firmware — before the devices can be used as a router. For example, most brands of “mesh” wireless routers — like Amazon’s Eero, Netgear’s Orbi series, or Asus’s ZenWifi — require online registration that automates these critical steps ...