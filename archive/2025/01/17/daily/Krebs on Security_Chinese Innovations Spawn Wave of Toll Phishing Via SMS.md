---
title: Chinese Innovations Spawn Wave of Toll Phishing Via SMS
url: https://krebsonsecurity.com/2025/01/chinese-innovations-spawn-wave-of-toll-phishing-via-sms/
source: Krebs on Security
date: 2025-01-17
fetch_date: 2025-10-06T20:23:29.461614
---

# Chinese Innovations Spawn Wave of Toll Phishing Via SMS

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Chinese Innovations Spawn Wave of Toll Phishing Via SMS

January 16, 2025

[34 Comments](https://krebsonsecurity.com/2025/01/chinese-innovations-spawn-wave-of-toll-phishing-via-sms/#comments)

Residents across the United States are being inundated with text messages purporting to come from toll road operators like **E-ZPass**, warning that recipients face fines if a delinquent toll fee remains unpaid. Researchers say the surge in SMS spam coincides with new features added to a popular commercial phishing kit sold in China that makes it simple to set up convincing lures spoofing toll road operators in multiple U.S. states.

Last week, the **Massachusetts Department of Transportation** (MassDOT) [warned residents](https://www.ezdrivema.com/About-EzdriveMA/Smishing-Alert) to be on the lookout for a new SMS phishing or “smishing” scam targeting users of **EZDriveMA**, MassDOT’s all electronic tolling program. Those who fall for the scam are asked to provide payment card data, and eventually will be asked to supply a one-time password sent via SMS or a mobile authentication app.

Reports of similar SMS phishing attacks against customers of other U.S. state-run toll facilities surfaced around the same time as the MassDOT alert. People in Florida reported receiving SMS phishing that spoofed **Sunpass**, Florida’s prepaid toll program.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/lighthouse-ezdrive.png)

In Texas, residents said they received text messages about unpaid tolls with the **North Texas Toll Authority**. Similar reports came from readers in California, Colorado, Connecticut, Minnesota, and Washington. This is by no means a comprehensive list.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/lighthouse-ntta.png)

In each case, the emergence of these SMS phishing attacks coincided with the release of new phishing kit capabilities that closely mimic these toll operator websites as they appear on mobile devices. Notably, none of the phishing pages will even load unless the website detects that the visitor is coming from a mobile device.

**Ford Merrill** works in security research at [SecAlliance](https://www.secalliance.com), a [CSIS Security Group](https://www.csis.com) company. Merrill said the volume of SMS phishing attacks spoofing toll road operators skyrocketed after the New Year, when at least one Chinese cybercriminal group known for selling sophisticated SMS phishing kits began offering new phishing pages designed to spoof toll operators in various U.S. states.

According to Merrill, multiple China-based cybercriminals are selling distinct SMS-based phishing kits that each have hundreds or thousands of customers. The ultimate goal of these kits, he said, is to phish enough information from victims that their payment cards can be added to mobile wallets and used to buy goods at physical stores, online, or to launder money through shell companies.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/lighthouse-tollroads.png)

Merrill said the different purveyors of these SMS phishing tools traditionally have impersonated shipping companies, customs authorities, and even governments with tax refund lures and visa or immigration renewal scams targeting people who may be living abroad or new to a country.

“What we’re seeing with these tolls scams is just a continuation of the Chinese smishing groups rotating from package redelivery schemes to toll road scams,” Merrill said. “Every one of us by now is sick and tired of receiving these package smishing attacks, so now it’s a new twist on an existing scam.”

In October 2023, KrebsOnSecurity wrote about [a massive uptick in SMS phishing scams targeting **U.S. Postal Service** customers](https://krebsonsecurity.com/2023/10/phishers-spoof-usps-12-other-natl-postal-services/). That story revealed the surge was tied to innovations introduced by “**Chenlun**,” a mainland China-based proprietor of a popular phishing kit and service. At the time, Chenlun had just introduced new phishing pages made to impersonate postal services in the United States and at least a dozen other countries.

SMS phishing kits are hardly new, but Merrill said Chinese smishing groups recently have introduced innovations in deliverability, by more seamlessly integrating their spam messages with Apple’s **iMessage** technology, and with [RCS](https://support.google.com/messages/answer/7189714?hl=en), the equivalent “rich text” messaging capability built into **Android** devices.

“While traditional smishing kits relied heavily on SMS for delivery, nowadays the actors make heavy use of iMessage and RCS because telecom operators can’t filter them and they likely have a higher success rate with these delivery channels,” he said.

It remains unclear how the phishers have selected their targets, or from where their data may be sourced. A notice from MassDOT cautions that “the targeted phone numbers seem to be chosen at random and are not uniquely associated with an account or usage of toll roads.”

Indeed, one reader shared on Mastodon yesterday that they’d received one of these SMS phishing attacks spoofing a local toll operator, when they didn’t even own a vehicle.

Targeted or not, these phishing websites are dangerous because they are operated dynamically in real-time by criminals. If you receive one of these messages, just ignore it or delete it, but please do not visit the phishing site. The FBI asks that before you bin the missives, consider filing a complaint with the agency’s [Internet Crime Complaint Center](https://www.ic3.gov) (IC3), including the phone number where the text originated, and the website listed within the text.

*This entry was posted on Thursday 16th of January 2025 04:18 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[@chenlun](https://krebsonsecurity.com/tag/chenlun/) [CSIS Security Group](https://krebsonsecurity.com/tag/csis-security-group/) [EZDriveMA](https://krebsonsecurity.com/tag/ezdrivema/) [fbi](https://krebsonsecurity.com/tag/fbi/) [Ford Merrill](https://krebsonsecurity.com/tag/ford-merrill/) [ic3](https://krebsonsecurity.com/tag/ic3/) [iMessage](https://krebsonsecurity.com/tag/imessage/) [Lighthouse](https://krebsonsecurity.com/tag/lighthouse/) [MassDOT](https://krebsonsecurity.com/tag/massdot/) [North Texas Toll Authority](https://krebsonsecurity.com/tag/north-texas-toll-authority/) [RCS](https://krebsonsecurity.com/tag/rcs/) [SecAlliance](https://krebsonsecurity.com/tag/secalliance/) [smishing](https://krebsonsecurity.com/tag/smishing/) [SMS phishing](https://krebsonsecurity.com/tag/sms-phishing/) [Sunpass](https://krebsonsecurity.com/tag/sunpass/) [The Toll Roads](https://krebsonsecurity.com/tag/the-toll-roads/)

Post navigation

[← Microsoft: Happy 2025. Here’s 161 Security Updates](https://krebsonsecurity.com/2025/01/microsoft-happy-2025-heres-161-security-updates/)
[MasterCard DNS Error Went Unnoticed for Years →](https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/)

## 34 thoughts...