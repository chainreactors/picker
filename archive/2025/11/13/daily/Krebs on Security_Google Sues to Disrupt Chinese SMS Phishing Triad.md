---
title: Google Sues to Disrupt Chinese SMS Phishing Triad
url: https://krebsonsecurity.com/2025/11/google-sues-to-disrupt-chinese-sms-phishing-triad/
source: Krebs on Security
date: 2025-11-13
fetch_date: 2025-11-14T03:13:41.566708
---

# Google Sues to Disrupt Chinese SMS Phishing Triad

Advertisement

[![](/b-knowbe4/44.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Google Sues to Disrupt Chinese SMS Phishing Triad

November 13, 2025

[10 Comments](https://krebsonsecurity.com/2025/11/google-sues-to-disrupt-chinese-sms-phishing-triad/#comments)

**Google** is suing more than two dozen unnamed individuals allegedly involved in peddling a popular China-based mobile phishing service that helps scammers impersonate hundreds of trusted brands, blast out text message lures, and convert phished payment card data into mobile wallets from Apple and Google.

In [a lawsuit](https://www.courtlistener.com/docket/71900274/1/google-llc-v-does-1-25/) filed in the Southern District of New York on November 12, Google sued to unmask and disrupt 25 “John Doe” defendants allegedly linked to the sale of **Lighthouse**, a sophisticated phishing kit that makes it simple for even novices to steal payment card data from mobile users. Google said Lighthouse has harmed more than a million victims across 120 countries.

![](https://krebsonsecurity.com/wp-content/uploads/2025/01/lighthouse-tollroads.png)

Lighthouse is one of several prolific phishing-as-a-service operations known as the “**Smishing Triad**,” and collectively they are responsible for sending [millions of text messages that spoof the U.S. Postal Service](https://krebsonsecurity.com/2025/01/chinese-innovations-spawn-wave-of-toll-phishing-via-sms/) to supposedly collect some outstanding delivery fee, or that pretend to be a local toll road operator warning of a delinquent toll fee. More recently, Lighthouse has been used to spoof e-commerce websites, [financial institutions](https://krebsonsecurity.com/2025/04/china-based-sms-phishing-triad-pivots-to-banks/) and [brokerage firms](https://krebsonsecurity.com/2025/08/mobile-phishers-target-brokerage-accounts-in-ramp-and-dump-cashout-scheme/).

Regardless of the text message lure used or brand used, the basic scam remains the same: After the visitor enters their payment information, the phishing site will automatically attempt to enroll the card as a mobile wallet from Apple or Google. The phishing site then tells the visitor that their bank is going to verify the transaction by sending a one-time code that needs to be entered into the payment page before the transaction can be completed.

If the recipient provides that one-time code, the scammers can [link the victim’s card data to a mobile wallet](https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/) on a device that they control. Researchers say the fraudsters usually load several stolen wallets onto each mobile device, and wait 7-10 days after that enrollment before selling the phones or using them for fraud.

Google called the scale of the Lighthouse phishing attacks “staggering.” A [May 2025 report](https://www.silentpush.com/blog/smishing-triad/) from **Silent Push** found the domains used by the Smishing Triad are rotated frequently, with approximately 25,000 phishing domains active during any 8-day period.

Google’s lawsuit alleges the purveyors of Lighthouse violated the company’s trademarks by including Google’s logos on countless phishing websites. The complaint says Lighthouse offers over 600 templates for phishing websites of more than 400 entities, and that Google’s logos were featured on at least a quarter of those templates.

Google is also pursuing Lighthouse under the [Racketeer Influenced and Corrupt Organizations (RICO) Act](https://en.wikipedia.org/wiki/Racketeer_Influenced_and_Corrupt_Organizations_Act), saying the Lighthouse phishing enterprise encompasses several connected threat actor groups that work together to design and implement complex criminal schemes targeting the general public.

According to Google, those threat actor teams include a “**developer group**” that supplies the phishing software and templates; a “**data broker group**” that provides a list of targets; a “**spammer group**” that provides the tools to send fraudulent text messages in volume; a “**theft group**,” in charge of monetizing the phished information; and an “**administrative group**,” which runs their Telegram support channels and discussion groups designed to facilitate collaboration and recruit new members.

“While different members of the Enterprise may play different roles in the Schemes, they all collaborate to execute phishing attacks that rely on the Lighthouse software,” Google’s complaint alleges. “None of the Enterprise’s Schemes can generate revenue without collaboration and cooperation among the members of the Enterprise. All of the threat actor groups are connected to one another through historical and current business ties, including through their use of Lighthouse and the online community supporting its use, which exists on both YouTube and Telegram channels.”

Silent Push’s May report observed that the Smishing Triad boasts it has “300+ front desk staff worldwide” involved in Lighthouse, staff that is mainly used to support various aspects of the group’s fraud and cash-out schemes.

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/phonesashtray.png)

Google alleges that in addition to blasting out text messages spoofing known brands, Lighthouse makes it easy for customers to mass-create fake e-commerce websites that are advertised using Google Ads accounts (and paid for with stolen credit cards). These phony merchants collect payment card information at checkout, and then prompt the customer to expect and share a one-time code sent from their financial institution.

Once again, that one-time code is being sent by the bank because the fake e-commerce site has just attempted to enroll the victim’s payment card data in a mobile wallet. By the time a victim understands they will likely never receive the item they just purchased from the fake e-commerce shop, the scammers have already run through hundreds of dollars in fraudulent charges, often at high-end electronics stores or jewelers.

**Ford Merrill** works in security research at [SecAlliance](https://www.secalliance.com/), a [CSIS Security Group](https://www.csis.com/) company, and he’s been tracking Chinese SMS phishing groups for several years. Merrill said many Lighthouse customers are now using the phishing kit to erect fake e-commerce websites that are advertised on Google and Meta platforms.

“You find this shop by searching for a particular product online or whatever, and you think you’re getting a good deal,” Merrill said. “But of course you never receive the product, and they will phish that one-time code at checkout.”

Merrill said some of the phishing templates include payment buttons for services like **PayPal**, and that victims who choose to pay through PayPal can also see their PayPal accounts hijacked.

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/paypalsmish.png)

A fake e-commerce site from the Smishing Triad spoofing PayPal on a mobile device.

“The main advantage of the fake e-commerce site is that it doesn’t require them to send out message lures,” Merrill said, noting that the fake vendor sites have more staying power than traditional phishing sites because it takes far longer for them to be flagged for fraud.

Merrill said Google’s legal action may temporarily disrupt the Lighthouse operators, and could make it easier for U.S...