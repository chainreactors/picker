---
title: Mobile Phishers Target Brokerage Accounts in ‘Ramp and Dump’ Cashout Scheme
url: https://krebsonsecurity.com/2025/08/mobile-phishers-target-brokerage-accounts-in-ramp-and-dump-cashout-scheme/
source: Krebs on Security
date: 2025-08-16
fetch_date: 2025-10-07T00:50:12.918796
---

# Mobile Phishers Target Brokerage Accounts in ‘Ramp and Dump’ Cashout Scheme

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-ninjio/10.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Mobile Phishers Target Brokerage Accounts in ‘Ramp and Dump’ Cashout Scheme

August 15, 2025

[18 Comments](https://krebsonsecurity.com/2025/08/mobile-phishers-target-brokerage-accounts-in-ramp-and-dump-cashout-scheme/#comments)

Cybercriminal groups peddling sophisticated phishing kits that convert stolen card data into mobile wallets have recently shifted their focus to targeting customers of brokerage services, new research shows. Undeterred by security controls at these trading platforms that block users from wiring funds directly out of accounts, the phishers have pivoted to using multiple compromised brokerage accounts in unison to manipulate the prices of foreign stocks.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/stockfall.png)

This so-called ‘**ramp and dump**‘ scheme borrows its name from age-old “pump and dump” scams, wherein fraudsters purchase a large number of shares in some penny stock, and then promote the company in a frenzied social media blitz to build up interest from other investors. The fraudsters dump their shares after the price of the penny stock increases to some degree, which usually then causes a sharp drop in the value of the shares for legitimate investors.

With ramp and dump, the scammers do not need to rely on ginning up interest in the targeted stock on social media. Rather, they will preposition themselves in the stock that they wish to inflate, using compromised accounts to purchase large volumes of it and then dumping the shares after the stock price reaches a certain value. In February 2025, the **FBI** said it was [seeking information from victims of this scheme](https://www.fbi.gov/how-we-can-help-you/victim-services/seeking-victim-information/seeking-victim-information-in-ramp-and-dump-investment-fraud-investigation).

“In this variation, the price manipulation is primarily the result of controlled trading activity conducted by the bad actors behind the scam,” reads [an advisory](https://www.finra.org/investors/insights/ramp-and-dump-schemes) from the **Financial Industry Regulatory Authority** (FINRA), a private, non-profit organization that regulates member brokerage firms. “Ultimately, the outcome for unsuspecting investors is the same—a catastrophic collapse in share price that leaves investors with unrecoverable losses.”

**Ford Merrill** is a security researcher at [SecAlliance](https://www.secalliance.com/), a [CSIS Security Group](https://www.csis.com/) company. Merrill said he has [tracked recent ramp-and-dump activity](https://podcasts.apple.com/dk/podcast/mnemonic-security-podcast/id1482626821?i=1000722355011) to a bustling Chinese-language community that is quite openly selling advanced mobile phishing kits on Telegram.

“They will often coordinate with other actors and will wait until a certain time to buy a particular Chinese IPO [initial public offering] stock or penny stock,” said Merrill, who has been chronicling the rapid maturation and growth of the China-based phishing community over the past three years.

“They’ll use all these victim brokerage accounts, and if needed they’ll liquidate the account’s current positions, and will preposition themselves in that instrument in some account they control, and then sell everything when the price goes up,” he said. “The victim will be left with worthless shares of that equity in their account, and the brokerage may not be happy either.”

Merrill said the early days of these phishing groups — between 2022 and 2024 — were typified by phishing kits that used text messages to spoof the **U.S. Postal Service** or some local toll road operator, warning about a delinquent shipping or toll fee that needed paying. Recipients who clicked the link and provided their payment information at a fake USPS or toll operator site were then asked to verify the transaction by sharing a one-time code sent via text message.

In reality, the victim’s bank is sending that code to the mobile number on file for their customer because the fraudsters have just attempted to enroll that victim’s card details into a mobile wallet. If the visitor supplies that one-time code, their payment card is then added to a new mobile wallet on an Apple or Google device that is physically controlled by the phishers.

The phishing gangs typically load multiple stolen cards to digital wallets on a single Apple or Android device, and then sell those phones in bulk to scammers who [use them for fraudulent e-commerce and tap-to-pay transactions](https://krebsonsecurity.com/2025/03/arrests-in-tap-to-pay-scheme-powered-by-phishing/).

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/phishingphones.png)

This China-based phishing collective exposed a major weakness common to many U.S.-based financial institutions that already require multi-factor authentication: The reliance on a single, phishable one-time token for provisioning mobile wallets. Happily, Merrill said many financial institutions that were caught flat-footed on this scam two years ago have since strengthened authentication requirements for onboarding new mobile wallets (such as requiring the card to be enrolled via the bank’s mobile app).

But just as squeezing one part of a balloon merely forces the air trapped inside to bulge into another area, fraudsters don’t go away when you make their current enterprise less profitable: They just shift their focus to a less-guarded area. And lately, that gaze has settled squarely on customers of the major brokerage platforms, Merrill said.

## THE OUTSIDER

Merrill pointed to several Telegram channels operated by some of the more accomplished phishing kit sellers, which are full of videos demonstrating how every feature in their kits can be tailored to the attacker’s target. The video snippet below comes from the Telegram channel of “**Outsider**,” a popular Mandarin-speaking phishing kit vendor whose latest offering includes a number of ready-made templates for using text messages to phish brokerage account credentials and one-time codes.

﻿

According to Merrill, Outsider is a woman who previously went by the handle “**Chenlun**.” KrebsOnSecurity profiled Chenlun’s phishing empire in [an October 2023 story](https://krebsonsecurity.com/2023/10/phishers-spoof-usps-12-other-natl-postal-services/) about a China-based group that was phishing mobile customers of more than a dozen postal services around the globe. In that case, the phishing sites were using a Telegram bot that sent stolen credentials to the “@chenlun” Telegram account.

Chenlun’s phishing lures are sent via Apple’s iMessage and Google’s RCS service and spoof one of the major brokerage platforms, warning that the account has been suspended for suspicious activity and that recipients should log in and verify some information. The missives include a link to a phishing page that collects the customer’s username and password, and then asks the user to enter a one-time code that will arrive via SMS.

The new phish kit videos on Outsider’s Telegram channel only feature templates for Schwab customers, but Merrill said the kit can easily be adapted to target other brokerage platforms. One reason the fraudsters are picking on brokerage firms, he said, has to do with the way they [handle multi-factor authentication](https://www.schwab.com/resource/how-to-set-up-two-factor-authentication).

Schwab cl...