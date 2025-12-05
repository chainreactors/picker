---
title: SMS Phishers Pivot to Points, Taxes, Fake Retailers
url: https://krebsonsecurity.com/2025/12/sms-phishers-pivot-to-points-taxes-fake-retailers/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-04
fetch_date: 2025-12-05T03:18:39.997404
---

# SMS Phishers Pivot to Points, Taxes, Fake Retailers

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# SMS Phishers Pivot to Points, Taxes, Fake Retailers

December 4, 2025

[4 Comments](https://krebsonsecurity.com/2025/12/sms-phishers-pivot-to-points-taxes-fake-retailers/#comments)

China-based phishing groups blamed for non-stop scam SMS messages about a supposed wayward package or unpaid toll fee are promoting a new offering, just in time for the holiday shopping season: Phishing kits for mass-creating fake but convincing e-commerce websites that convert customer payment card data into mobile wallets from Apple and Google. Experts say these same phishing groups also are now using SMS lures that promise unclaimed tax refunds and mobile rewards points.

Over the past week, thousands of domain names were registered for scam websites that purport to offer **T-Mobile** customers the opportunity to claim a large number of rewards points. The phishing domains are being promoted by scam messages sent via Apple’s iMessage service or the functionally equivalent RCS messaging service built into Google phones.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/tmobpoints-smish.png)

The website scanning service **urlscan.io** [shows](http://urlscan.io/result/019a609e-8dda-7612-a4b1-a6fe2c0bff6d) thousands of these phishing domains have been deployed in just the past few days alone. The phishing websites will only load if the recipient visits with a mobile device, and they ask for the visitor’s name, address, phone number and payment card data to claim the points.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/tmob-points-site.png)

If card data is submitted, the site will then prompt the user to share a one-time code sent via SMS by their financial institution. In reality, the bank is sending the code because the fraudsters have just attempted to enroll the victim’s phished card details in a mobile wallet from Apple or Google. If the victim also provides that one-time code, the phishers can then [link the victim’s card to a mobile device that they physically control](https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/).

Pivoting off these T-Mobile phishing domains in urlscan.io reveals a similar scam targeting **AT&T** customers:

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/att-smish.png)

**Ford Merrill** works in security research at [SecAlliance](https://www.secalliance.com/), a [CSIS Security Group](https://www.csis.com/) company. Merrill said multiple China-based cybercriminal groups that sell phishing-as-a-service platforms have been using the mobile points lure for some time, but the scam has only recently been pointed at consumers in the United States.

“These points redemption schemes have not been very popular in the U.S., but have been in other geographies like EU and Asia for a while now,” Merrill said.

A review of other domains flagged by urlscan.io as tied to this Chinese SMS phishing syndicate shows they are also spoofing U.S. state tax authorities, telling recipients they have an unclaimed tax refund. Again, the goal is to phish the user’s payment card information and one-time code.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/dctaxphish.png)

A text message that spoofs the District of Columbia’s Office of Tax and Revenue.

## CAVEAT EMPTOR

Many SMS phishing or “smishing” domains are quickly flagged by browser makers as malicious. But Merrill said one burgeoning area of growth for these phishing kits — fake e-commerce shops — can be far harder to spot because they do not call attention to themselves by spamming the entire world.

Merrill said the same Chinese phishing kits used to blast out package redelivery message scams are equipped with modules that make it simple to quickly deploy a fleet of fake but convincing e-commerce storefronts. Those phony stores are typically advertised on **Google** and **Facebook**, and consumers usually end up at them by searching online for deals on specific products.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/fake-ecom.png)

A machine-translated screenshot of an ad from a China-based phishing group promoting their fake e-commerce shop templates.

With these fake e-commerce stores, the customer is supplying their payment card and personal information as part of the normal check-out process, which is then punctuated by a request for a one-time code sent by your financial institution. The fake shopping site claims the code is required by the user’s bank to verify the transaction, but it is sent to the user because the scammers immediately attempt to enroll the supplied card data in a mobile wallet.

According to Merrill, it is only during the check-out process that these fake shops will fetch the malicious code that gives them away as fraudulent, which tends to make it difficult to locate these stores simply by mass-scanning the web. Also, most customers who pay for products through these sites don’t realize they’ve been snookered until weeks later when the purchased item fails to arrive.

“The fake e-commerce sites are tough because a lot of them can fly under the radar,” Merrill said. “They can go months without being shut down, they’re hard to discover, and they generally don’t get flagged by safe browsing tools.”

Happily, reporting these SMS phishing lures and websites is one of the fastest ways to get them properly identified and shut down. **Raymond Dijkxhoorn** is the CEO and a founding member of [SURBL](https://www.surbl.org/), a widely-used blocklist that flags domains and IP addresses known to be used in unsolicited messages, phishing and malware distribution. SURBL has created a website called [smishreport.com](https://smishreport.com) that asks users to forward a screenshot of any smishing message(s) received.

“If [a domain is] unlisted, we can find and add the new pattern and kill the rest” of the matching domains, **Dijkxhoorn** said. “Just make a screenshot and upload. The tool does the rest.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/smishreport.png)

The SMS phishing reporting site smishreport.com.

Merrill said the last few weeks of the calendar year typically see a big uptick in smishing — particularly package redelivery schemes that spoof the **U.S. Postal Service** or commercial shipping companies.

“Every holiday season there is an explosion in smishing activity,” he said. “Everyone is in a bigger hurry, frantically shopping online, paying less attention than they should, and they’re just in a better mindset to get phished.”

## SHOP ONLINE LIKE A SECURITY PRO

As we can see, adopting a shopping strategy of simply buying from the online merchant with the lowest advertised prices can be a bit like playing Russian Roulette with your wallet. Even people who shop mainly at big-name online stores [can get scammed](https://krebsonsecurity.com/2017/04/how-cybercrooks-put-the-beatdown-on-my-beats/) if they’re not wary of too-good-to-be-true offers (think third-party sellers on these platforms).

If you don’t know much about the online merchant that has the item you wish to buy, take a few minutes to investigate its reputation. If you’re buying from an online store that is brand new, the risk that you will get scammed increases sig...