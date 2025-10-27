---
title: How Phished Data Turns into Apple & Google Wallets
url: https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-19
fetch_date: 2025-10-06T20:48:22.209003
---

# How Phished Data Turns into Apple & Google Wallets

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# How Phished Data Turns into Apple & Google Wallets

February 18, 2025

[35 Comments](https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/#comments)

Carding — the underground business of stealing, selling and swiping stolen payment card data — has long been the dominion of Russia-based hackers. Happily, the broad deployment of more secure chip-based payment cards in the United States has weakened the carding market. But a flurry of innovation from cybercrime groups in China is breathing new life into the carding industry, by turning phished card data into mobile wallets that can be used online and at main street stores.

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/tollpassphishing.png)

If you own a mobile phone, the chances are excellent that at some point in the past two years it has received at least one phishing message that spoofs the **U.S. Postal Service** to supposedly collect some outstanding delivery fee, or an SMS that pretends to be a local toll road operator warning of a delinquent toll fee.

These messages are being sent through sophisticated phishing kits sold by several cybercriminals based in mainland China. And they are not traditional SMS phishing or “**smishing**” messages, as they bypass the mobile networks entirely. Rather, the missives are sent through the **Apple iMessage** service and through [RCS](https://en.wikipedia.org/wiki/Rich_Communication_Services), the functionally equivalent technology on **Google** phones.

People who enter their payment card data at one of these sites will be told their financial institution needs to verify the small transaction by sending a one-time passcode to the customer’s mobile device. In reality, that code will be sent by the victim’s financial institution to verify that the user indeed wishes to link their card information to a mobile wallet.

If the victim then provides that one-time code, the phishers will link the card data to a new mobile wallet from Apple or Google, loading the wallet onto a mobile phone that the scammers control.

## CARDING REINVENTED

**Ford Merrill** works in security research at [SecAlliance](https://www.secalliance.com/), a [CSIS Security Group](https://www.csis.com/) company. Merrill has been studying the evolution of several China-based smishing gangs, and found that most of them feature helpful and informative video tutorials in their sales accounts on Telegram. Those videos show the thieves are loading multiple stolen digital wallets on a single mobile device, and then selling those phones in bulk for hundreds of dollars apiece.

“Who says carding is dead?,” said Merrill, who presented about his findings at the [M3AAWG](https://www.m3aawg.org/upcoming-meetings) security conference in Lisbon earlier today. “This is the best mag stripe cloning device ever. This threat actor is saying you need to buy at least 10 phones, and they’ll air ship them to you.”

One promotional video shows stacks of milk crates stuffed full of phones for sale. A closer inspection reveals that each phone is affixed with a handwritten notation that typically references the date its mobile wallets were added, the number of wallets on the device, and the initials of the seller.

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/phishingphones.png)

Merrill said one common way criminal groups in China are cashing out with these stolen mobile wallets involves setting up fake e-commerce businesses on **Stripe** or **Zelle** and running transactions through those entities — often for amounts totaling between $100 and $500.

Merrill said that when these phishing groups first began operating in earnest two years ago, they would wait between 60 to 90 days before selling the phones or using them for fraud. But these days that waiting period is more like just seven to ten days, he said.

“When they first installed this, the actors were very patient,” he said. “Nowadays, they only wait like 10 days before [the wallets] are hit hard and fast.”

## GHOST TAP

Criminals also can cash out mobile wallets by obtaining real point-of-sale terminals and using tap-to-pay on phone after phone. But they also offer a more cutting-edge mobile fraud technology: Merrill found that at least one of the Chinese phishing groups sells an Android app called “**ZNFC**” that can relay a valid NFC transaction to anywhere in the world. The user simply waves their phone at a local payment terminal that accepts Apple or Google pay, and the app relays an NFC transaction over the Internet from a phone in China.

“The software can work from anywhere in the world,” Merrill said. “These guys provide the software for $500 a month, and it can relay both NFC enabled tap-to-pay as well as any digital wallet. They even have 24-hour support.”

The rise of so-called “ghost tap” mobile software was [first documented in November 2024](https://www.threatfabric.com/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay) by security experts at **ThreatFabric**. **Andy Chandler**, the company’s chief commercial officer, said their researchers have since identified a number of criminal groups from different regions of the world latching on to this scheme.

Chandler said those include organized crime gangs in Europe that are using similar mobile wallet and NFC attacks to take money out of ATMs made to work with smartphones.

“No one is talking about it, but we’re now seeing ten different methodologies using the same modus operandi, and none of them are doing it the same,” Chandler said. “This is much bigger than the banks are prepared to say.”

A November 2024 story in the Singapore daily *The Straits Times* [reported](https://www.straitstimes.com/singapore/scam-syndicates-sending-foreigners-into-singapore-to-cheat-retailers-like-apple-store-and-best-denki) authorities there arrested three foreign men who were recruited in their home countries via social messaging platforms, and given ghost tap apps with which to purchase expensive items from retailers, including mobile phones, jewelry, and gold bars.

“Since Nov 4, at least 10 victims who had fallen for e-commerce scams have reported unauthorised transactions totaling more than $100,000 on their credit cards for purchases such as electronic products, like iPhones and chargers, and jewelry in Singapore,” *The Straits Times* wrote, noting that in another case with a similar modus operandi, the police arrested a Malaysian man and woman on Nov 8.

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/thestraitstimes.png)

Three individuals charged with using ghost tap software at an electronics store in Singapore. Image: The Straits Times.

## ADVANCED PHISHING TECHNIQUES

According to Merrill, the phishing pages that spoof the USPS and various toll road operators are powered by several innovations designed to maximize the extraction of victim data.

For example, a would-be smishing victim might enter their personal and financial information, but then decide the whole thing is scam before actually submitting the data. In this case, anything typed into the data fields of the phishing page will be captured in real time, regardless of whether the visitor actually clicks the “submit” button.

Merrill said people who submit payment card data to these phishing sites often ar...