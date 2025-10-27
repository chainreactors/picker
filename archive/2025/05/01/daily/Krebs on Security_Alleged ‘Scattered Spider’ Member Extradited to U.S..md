---
title: Alleged ‘Scattered Spider’ Member Extradited to U.S.
url: https://krebsonsecurity.com/2025/04/alleged-scattered-spider-member-extradited-to-u-s/
source: Krebs on Security
date: 2025-05-01
fetch_date: 2025-10-06T22:34:06.059947
---

# Alleged ‘Scattered Spider’ Member Extradited to U.S.

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/41.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Alleged ‘Scattered Spider’ Member Extradited to U.S.

April 30, 2025

[19 Comments](https://krebsonsecurity.com/2025/04/alleged-scattered-spider-member-extradited-to-u-s/#comments)

A 23-year-old Scottish man thought to be a member of the prolific **Scattered Spider** cybercrime group was extradited last week from Spain to the United States, where he is facing charges of wire fraud, conspiracy and identity theft. U.S. prosecutors allege **Tyler Robert Buchanan** and co-conspirators hacked into dozens of companies in the United States and abroad, and that he personally controlled more than $26 million stolen from victims.

Scattered Spider is a loosely affiliated criminal hacking group whose members have broken into and stolen data from some of the world’s largest technology companies. Buchanan was arrested in Spain last year on a warrant from the FBI, which wanted him in connection with a series of SMS-based phishing attacks in the summer of 2022 that led to intrusions at Twilio, LastPass, DoorDash, Mailchimp, and many other tech firms.

![](https://krebsonsecurity.com/wp-content/uploads/2024/06/tylerb.png)

As [first reported](https://krebsonsecurity.com/2024/06/alleged-boss-of-scattered-spider-hacking-group-arrested/) by KrebsOnSecurity, Buchanan (a.k.a. “tylerb”) fled the United Kingdom in February 2023, after a rival cybercrime gang hired thugs to invade his home, assault his mother, and threaten to burn him with a blowtorch unless he gave up the keys to his cryptocurrency wallet. Buchanan was arrested in June 2024 at the airport in Palma de Mallorca while trying to board a flight to Italy. His extradition to the United States was [first reported](https://www.bloomberg.com/news/articles/2025-04-24/scattered-spider-hacking-suspect-extradited-to-us-from-spain) last week by **Bloomberg**.

Members of Scattered Spider have been [tied](https://cyberscoop.com/youth-hacking-ring-at-the-center-of-cybercrime-spree/) to the 2023 ransomware attacks against **MGM** and **Caesars** casinos in Las Vegas, but it remains unclear whether Buchanan was implicated in that incident. The Justice Department’s complaint against Buchanan makes no mention of the 2023 ransomware attack.

Rather, the investigation into Buchanan appears to center on the SMS phishing campaigns from 2022, and on [SIM-swapping attacks](https://krebsonsecurity.com/category/sim-swapping/) that siphoned funds from individual cryptocurrency investors. In a SIM-swapping attack, crooks transfer the target’s phone number to a device they control and intercept any text messages or phone calls to the victim’s device — including one-time passcodes for authentication and password reset links sent via SMS.

In August 2022, KrebsOnSecurity [reviewed data harvested in a months-long cybercrime campaign by Scattered Spider](https://krebsonsecurity.com/2022/08/how-1-time-passcodes-became-a-corporate-liability/) involving countless SMS-based phishing attacks against employees at major corporations. The security firm **Group-IB** called them by a different name — **0ktapus**, because the group typically spoofed the identity provider **Okta** in their phishing messages to employees at targeted firms.

![](https://krebsonsecurity.com/wp-content/uploads/2022/08/twiliophish.png)

A Scattered Spider/0Ktapus SMS phishing lure sent to Twilio employees in 2022.

The [complaint against Buchanan](https://krebsonsecurity.com/wp-content/uploads/2025/04/tylerb-complaint.pdf) (PDF) says the FBI tied him to the 2022 SMS phishing attacks after discovering the same username and email address was used to register numerous Okta-themed phishing domains seen in the campaign. The domain registrar **NameCheap** found that less than a month before the phishing spree, the account that registered those domains logged in from an Internet address in the U.K. FBI investigators said the Scottish police told them the address was leased to Buchanan from January 26, 2022 to November 7, 2022.

Authorities seized at least 20 digital devices when they raided Buchanan’s residence, and on one of those devices they found usernames and passwords for employees of three different companies targeted in the phishing campaign.

“The FBI’s investigation to date has gathered evidence showing that Buchanan and his co-conspirators targeted at least 45 companies in the United States and abroad, including Canada, India, and the United Kingdom,” the FBI complaint reads. “One of Buchanan’s devices contained a screenshot of Telegram messages between an account known to be used by Buchanan and other unidentified co-conspirators discussing dividing up the proceeds of SIM swapping.”

U.S. prosecutors allege that records obtained from Discord showed the same U.K. Internet address was used to operate a Discord account that specified a cryptocurrency wallet when asking another user to send funds. The complaint says the publicly available transaction history for that payment address shows approximately 391 bitcoin was transferred in and out of this address between October 2022 and
February 2023; 391 bitcoin is presently worth more than $26 million.

In November 2024, federal prosecutors in Los Angeles [unsealed criminal charges against Buchanan](https://krebsonsecurity.com/2024/11/feds-charge-five-men-in-scattered-spider-roundup/) and four other alleged Scattered Spider members, including **Ahmed Elbadawy**, 23, of College Station, Texas; **Joel Evans**, 25, of Jacksonville, North Carolina; **Evans Osiebo**, 20, of Dallas; and [**Noah Urban**](https://krebsonsecurity.com/2024/01/fla-man-charged-in-sim-swapping-spree-is-key-suspect-in-hacker-groups-oktapus-scattered-spider/), 20, of Palm Coast, Florida. KrebsOnSecurity [reported last year](https://krebsonsecurity.com/2024/09/the-dark-nexus-between-harm-groups-and-the-com/) that another suspected Scattered Spider member — a 17-year-old from the United Kingdom — was arrested as part of a joint investigation with the FBI into the MGM hack.

Mr. Buchanan’s court-appointed attorney did not respond to a request for comment. The accused faces charges of wire fraud conspiracy, conspiracy to obtain information by computer for private financial gain, and aggravated identity theft. Convictions on the latter charge carry a minimum sentence of two years in prison.

Documents from the U.S. District Court for the Central District of California indicate Buchanan is being held without bail pending trial. A preliminary hearing in the case is slated for May 6.

*This entry was posted on Wednesday 30th of April 2025 05:54 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/) [Ransomware](https://krebsonsecurity.com/category/ransomware/) [SIM Swapping](https://krebsonsecurity.com/category/sim-swapping/)

[0ktapus](https://krebsonsecurity.com/tag/0ktapus/) [Ahmed Elbadawy](https://krebsonsecurity.com/tag/ahmed-elbadawy/) [Caesars](https://krebsonsecurity.com/tag/caesars/) [DoorDash](https://krebsonsecurity.com/tag/doordash/) [Evans Osiebo](https://krebsonsecurity.com/tag/evans-osiebo/) [Group-IB](https://krebsonsecurity.com/tag/group-ib/) [Joel Evans](https://krebsonsecurity.com/tag/joel-evans/) [lastpass](https://krebsonsecurity.com/tag/lastpass/) [Mailchimp](https://krebsonse...