---
title: China-based SMS Phishing Triad Pivots to Banks
url: https://krebsonsecurity.com/2025/04/china-based-sms-phishing-triad-pivots-to-banks/
source: Krebs on Security
date: 2025-04-11
fetch_date: 2025-10-06T22:17:03.926853
---

# China-based SMS Phishing Triad Pivots to Banks

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# China-based SMS Phishing Triad Pivots to Banks

April 10, 2025

[27 Comments](https://krebsonsecurity.com/2025/04/china-based-sms-phishing-triad-pivots-to-banks/#comments)

China-based purveyors of SMS phishing kits are enjoying remarkable success converting phished payment card data into mobile wallets from **Apple** and **Google**. Until recently, the so-called “**Smishing Triad**” mainly impersonated toll road operators and shipping companies. But experts say these groups are now directly targeting customers of international financial institutions, while dramatically expanding their cybercrime infrastructure and support staff.

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/wall-o-phones.png)

If you own a mobile device, the chances are excellent that at some point in the past two years you’ve received at least one instant message that warns of a delinquent toll road fee, or a wayward package from the **U.S. Postal Service** (USPS). Those who click the promoted link are brought to a website that spoofs the USPS or a local toll road operator and asks for payment card information.

The site will then complain that the visitor’s bank needs to “verify” the transaction by sending a one-time code via SMS. In reality, the bank is sending that code to the mobile number on file for their customer because the fraudsters have just attempted to enroll that victim’s card details into a mobile wallet.

If the visitor supplies that one-time code, their payment card is then added to a new mobile wallet on an Apple or Google device that is physically controlled by the phishers. The phishing gangs typically load [multiple stolen cards to digital wallets on a single Apple or Android device](https://krebsonsecurity.com/wp-content/uploads/2025/02/phishingphones.png), and then sell those phones in bulk to scammers who use them for fraudulent e-commerce and tap-to-pay transactions.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/04/mobwalletimage.png)](https://krebsonsecurity.com/wp-content/uploads/2025/04/mobwalletimage.png)

A screenshot of the administrative panel for a smishing kit. On the left is the (test) data entered at the phishing site. On the right we can see the phishing kit has superimposed the supplied card number onto an image of a payment card. When the phishing kit scans that created card image into Apple or Google Pay, it triggers the victim’s bank to send a one-time code. Image: Ford Merrill.

The moniker “Smishing Triad” comes from **Resecurity**, which was among [the first to report in August 2023](https://www.resecurity.com/blog/article/smishing-triad-targeted-usps-and-us-citizens-for-data-theft) on the emergence of three distinct mobile phishing groups based in China that appeared to share some infrastructure and innovative phishing techniques. But it is a bit of a misnomer because the phishing lures blasted out by these groups are not SMS or text messages in the conventional sense.

Rather, they are sent via **iMessage** to **Apple** device users, and via RCS on **Google Android** devices. Thus, the missives bypass the mobile phone networks entirely and enjoy near 100 percent delivery rate (at least until Apple and Google suspend the spammy accounts).

In [a report](https://catalyst.prodaft.com/public/report/lucid/overview) published on March 24, the Swiss threat intelligence firm **Prodaft** detailed the rapid pace of innovation coming from the Smishing Triad, which it characterizes as a loosely federated group of Chinese phishing-as-a-service operators with names like **Darcula**, **Lighthouse**, and the **Xinxin Group**.

Prodaft said they’re seeing a significant shift in the underground economy, particularly among Chinese-speaking threat actors who have historically operated in the shadows compared to their Russian-speaking counterparts.

“Chinese-speaking actors are introducing innovative and cost-effective systems, enabling them to target larger user bases with sophisticated services,” Prodaft wrote. “Their approach marks a new era in underground business practices, emphasizing scalability and efficiency in cybercriminal operations.”

A [new report](https://www.silentpush.com/blog/smishing-triad/) from researchers at the security firm **SilentPush** finds the Smishing Triad members have expanded into selling mobile phishing kits targeting customers of global financial institutions like **CitiGroup**, **MasterCard**, **PayPal**, **Stripe**, and **Visa**, as well as banks in Canada, Latin America, Australia and the broader Asia-Pacific region.

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/paypalsmish.png)

Phishing lures from the Smishing Triad spoofing PayPal. Image: SilentPush.

SilentPush found the Smishing Triad now spoofs recognizable brands in a variety of industry verticals across at least 121 countries and a vast number of industries, including the postal, logistics, telecommunications, transportation, finance, retail and public sectors.

According to SilentPush, the domains used by the Smishing Triad are rotated frequently, with approximately 25,000 phishing domains active during any 8-day period and a majority of them sitting at two Chinese hosting companies: **Tencent** (AS132203) and **Alibaba** (AS45102).

“With nearly two-thirds of all countries in the world targeted by [the] Smishing Triad, it’s safe to say they are essentially targeting every country with modern infrastructure outside of Iran, North Korea, and Russia,” SilentPush wrote. “Our team has observed some potential targeting in Russia (such as domains that mentioned their country codes), but nothing definitive enough to indicate Russia is a persistent target. Interestingly, even though these are Chinese threat actors, we have seen instances of targeting aimed at Macau and Hong Kong, both special administrative regions of China.”

SilentPush’s **Zach Edwards** said his team found a vulnerability that exposed data from one of the Smishing Triad’s phishing pages, which revealed the number of visits each site received each day across thousands of phishing domains that were active at the time. Based on that data, SilentPush estimates those phishing pages received well more than a million visits within a 20-day time span.

The report notes the Smishing Triad boasts it has “300+ front desk staff worldwide” involved in one of their more popular phishing kits — Lighthouse — staff that is mainly used to support various aspects of the group’s fraud and cash-out schemes.

The Smishing Triad members maintain their own Chinese-language sales channels on Telegram, which frequently offer videos and photos of their staff hard at work. Some of those images include massive walls of phones used to send phishing messages, with human operators seated directly in front of them ready to receive any time-sensitive one-time codes.

As noted in February’s story [How Phished Data Turns Into Apple and Google Wallets](https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/), one of those cash-out schemes involves an Android app called **Z-NFC**, which can relay a valid NFC transaction from one of these compromised digital wallets to anywhere in the world. For a $500 month subscription, the customer can wave their phone at any payment terminal that accepts A...