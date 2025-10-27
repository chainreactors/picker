---
title: Barracuda Urges Replacing — Not Patching — Its Email Security Gateways
url: https://krebsonsecurity.com/2023/06/barracuda-urges-replacing-not-patching-its-email-security-gateways/
source: Over Security - Cybersecurity news aggregator
date: 2023-06-09
fetch_date: 2025-10-04T11:48:29.395151
---

# Barracuda Urges Replacing — Not Patching — Its Email Security Gateways

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Barracuda Urges Replacing — Not Patching — Its Email Security Gateways

June 8, 2023

[41 Comments](https://krebsonsecurity.com/2023/06/barracuda-urges-replacing-not-patching-its-email-security-gateways/#comments)

It’s not often that a zero-day vulnerability causes a network security vendor to urge customers to physically remove and decommission an entire line of affected hardware — as opposed to just applying software updates. But experts say that is exactly what transpired this week with **Barracuda Networks**, as the company struggled to combat a sprawling malware threat which appears to have undermined its email security appliances in such a fundamental way that they can no longer be safely updated with software fixes.

![](https://krebsonsecurity.com/wp-content/uploads/2023/06/barracuda.png)

Campbell, Calif. based Barracuda said it hired incident response firm **Mandiant** on May 18 after receiving reports about unusual traffic originating from its **Email Security Gateway** (ESG) devices, which are designed to sit at the edge of an organization’s network and scan all incoming and outgoing email for malware.

On May 19, Barracuda identified that the malicious traffic was taking advantage of a previously unknown vulnerability in its ESG appliances, and on May 20 the company pushed a patch for the flaw to all affected appliances ([CVE-2023-2868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2868)).

In [its security advisory](https://www.barracuda.com/company/legal/esg-vulnerability), Barracuda said the vulnerability existed in the Barracuda software component responsible for screening attachments for malware. More alarmingly, the company said it appears attackers first started exploiting the flaw in October 2022.

But on June 6, Barracuda suddenly began urging its ESG customers to wholesale rip out and replace — not patch — affected appliances.

“Impacted ESG appliances must be immediately replaced regardless of patch version level,” the company’s advisory warned. “Barracuda’s recommendation at this time is full replacement of the impacted ESG.”

In a statement, Barracuda said it will be providing the replacement product to impacted customers at no cost, and that not all ESG appliances were compromised.

“No other Barracuda product, including our SaaS email solutions, were impacted by this vulnerability,” the company said. “If an ESG appliance is displaying a notification in the User Interface, the ESG appliance had indicators of compromise. If no notification is displayed, we have no reason to believe that the appliance has been compromised at this time.”

Nevertheless, the statement says that “out of an abundance of caution and in furtherance of our containment strategy, we recommend impacted customers replace their compromised appliance.”

“As of June 8, 2023, approximately 5% of active ESG appliances worldwide have shown any evidence of known indicators of compromise due to the vulnerability,” the statement continues. “Despite deployment of additional patches based on known IOCs, we continue to see evidence of ongoing malware activity on a subset of the compromised appliances. Therefore, we would like customers to replace any compromised appliance with a new unaffected device.”

**Rapid7**‘s **Caitlin Condon** called this remarkable turn of events “fairly stunning,” and said there appear to be roughly 11,000 vulnerable ESG devices still connected to the Internet worldwide.

“The pivot from patch to total replacement of affected devices is fairly stunning and implies the malware the threat actors deployed somehow achieves persistence at a low enough level that even wiping the device wouldn’t eradicate attacker access,” Condon [wrote](https://www.rapid7.com/blog/post/2023/06/08/etr-cve-2023-2868-total-compromise-of-physical-barracuda-esg-appliances/).

Barracuda said the malware was identified on a subset of appliances that allowed the attackers persistent backdoor access to the devices, and that evidence of data exfiltration was identified on some systems.

Rapid7 said it has seen no evidence that attackers are using the flaw to move laterally within victim networks. But that may be small consolation for Barracuda customers now coming to terms with the notion that foreign cyberspies probably have been hoovering up all their email for months.

**Nicholas Weaver**, a researcher at University of California, Berkeley’s [International Computer Science Institute](https://www.icsi.berkeley.edu/icsi/) (ICSI), said it is likely that the malware was able to corrupt the underlying firmware that powers the ESG devices in some irreparable way.

“One of the goals of malware is to be hard to remove, and this suggests the malware compromised the firmware itself to make it really hard to remove and really stealthy,” Weaver said. “That’s not a ransomware actor, that’s a state actor. Why? Because a ransomware actor doesn’t care about that level of access. They don’t need it. If they’re going for data extortion, it’s more like a smash-and-grab. If they’re going for data ransoming, they’re encrypting the data itself — not the machines.”

In addition to replacing devices, Barracuda says ESG customers should also rotate any credentials connected to the appliance(s), and check for signs of compromise dating back to at least October 2022 using the network and endpoint indicators the company has [released publicly](https://www.barracuda.com/company/legal/esg-vulnerability).

**Update, June 9, 11:55 a.m. ET:** Barracuda has issued an updated statement about the incident, portions of which are now excerpted above.

*This entry was posted on Thursday 8th of June 2023 04:17 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Barracuda Networks](https://krebsonsecurity.com/tag/barracuda-networks/) [Caitlin Condon](https://krebsonsecurity.com/tag/caitlin-condon/) [CVE-2023-2868](https://krebsonsecurity.com/tag/cve-2023-2868/) [Email Security Gateway](https://krebsonsecurity.com/tag/email-security-gateway/) [International Computer Science Institute](https://krebsonsecurity.com/tag/international-computer-science-institute/) [Mandiant](https://krebsonsecurity.com/tag/mandiant/) [Nicholas Weaver](https://krebsonsecurity.com/tag/nicholas-weaver/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/)

Post navigation

[← Service Rents Email Addresses for Account Signups](https://krebsonsecurity.com/2023/06/service-rents-email-addresses-for-account-signups/)
[Microsoft Patch Tuesday, June 2023 Edition →](https://krebsonsecurity.com/2023/06/microsoft-patch-tuesday-june-2023-edition/)

## 41 thoughts on “Barracuda Urges Replacing — Not Patching — Its Email Security Gateways”

1. Larry [June 8, 2023](https://krebsonsecurity.com/2023/06/barracuda-urges-replacing-not-patching-its-email-security-gateways/#comment-585569)

   Who will pay for the replacement hardware? I did not see in the announcement that Barracuda would replace the hardware at no charge to the customer, or that they would reimburse the labor costs required.

   1. White Hat Bob [June 8, 2023](https://krebsonsecurity.com/2023/06/barracuda-urges-replacing-not-patching-its-emai...