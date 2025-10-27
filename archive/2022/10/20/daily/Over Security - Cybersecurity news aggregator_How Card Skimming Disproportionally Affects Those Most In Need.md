---
title: How Card Skimming Disproportionally Affects Those Most In Need
url: https://krebsonsecurity.com/2022/10/how-card-skimming-disproportionally-affects-those-most-in-need/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-20
fetch_date: 2025-10-03T20:25:22.021488
---

# How Card Skimming Disproportionally Affects Those Most In Need

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# How Card Skimming Disproportionally Affects Those Most In Need

October 18, 2022

[35 Comments](https://krebsonsecurity.com/2022/10/how-card-skimming-disproportionally-affects-those-most-in-need/#comments)

When people banking in the United States lose money because their payment card got [skimmed at an ATM](https://krebsonsecurity.com/?s=atm+skimmer), [gas pump](https://krebsonsecurity.com/?s=pump+skimmers) or [grocery store checkout terminal](https://krebsonsecurity.com/?s=checkout+skimmer+overlay), they may face hassles or delays in recovering any lost funds, but they are almost always made whole by their financial institution. Yet, one class of Americans — those receiving food assistance benefits via state-issued prepaid debit cards — are particularly exposed to losses from skimming scams, and usually have little recourse to do anything about it.

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/califebt.png)

Over the past several months, authorities in multiple U.S. states have reported rapid increases in skimming losses tied to people who receive assistance via Electronic Benefits Transfer (EBT), which allows a [Supplemental Nutrition Assistance Program](https://www.fns.usda.gov/snap/supplemental-nutrition-assistance-program) (SNAP) participant to pay for food using SNAP benefits.

When a participant uses a SNAP payment card at an authorized retail store, their SNAP EBT account is debited to reimburse the store for food that was purchased. EBT is used in all 50 states, the District of Columbia, Puerto Rico, the Virgin Islands, and Guam.

EBT cards work just like regular debit cards, in that they can be used along with a personal identification number (PIN) to pay for goods at participating stores, and to withdraw cash from an ATM.

However, EBT cards differ from debit cards issued to most Americans in two important ways. First, [most states](https://krebsonsecurity.com/2022/10/glut-of-fake-linkedin-profiles-pits-hr-against-the-bots/) do not equip EBT cards with smart chip technology, which can make payment cards much more difficult and expensive for skimming thieves to clone.

Alas, it is no accident that all of the states reporting recent spikes in fraud tied to EBT accounts — including [California](https://abc30.com/atm-skimmers-ebt-money-stolen-credit-card-theft-bank-of-america/11814857/), [Connecticut](https://www.nbcconnecticut.com/news/local/state-warns-residents-who-receive-snap-ebt-benefits-after-learning-about-skimming-phishing-incidents/2849775/), [Maryland](https://www.thebaltimorebanner.com/community/criminal-justice/one-womans-quest-for-justice-after-almost-3000-of-benefits-were-stolen-LHIKMQZSNJBULC7LXCEIE264OA/), [Pennsylvania](https://www.fox43.com/article/news/crime/york-county-ebt-card-cloning-thefts/521-64b60fbd-b4be-4fd9-8928-5c6ed8d45faa), [Tennessee](https://www.newschannel5.com/news/nashville-family-scammed-in-ebt-card-skimmer-scheme), and [Virginia](http://wtkr.com/news/chesapeake-mom-warns-others-of-ebt-scam-after-losing-benefits) appear to currently issue chip-less cards to their EBT recipients.

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/mass-dta.png)

In September, authorities in California arrested three men thought to be part of a skimming crew that specifically targeted EBT cards and balances. The men allegedly installed [deep insert skimmers](https://krebsonsecurity.com/2022/09/say-hello-to-crazy-thin-deep-insert-atm-skimmers/), and stole PINs using tiny hidden cameras.

“The arrests were the result of a joint investigation by the Sheriff’s Office and Bank of America corporate security,” reads [a September 2022 story](https://www.sacbee.com/news/local/crime/article265394781.html) from *The Sacramento Bee*. “The investigation focused on illegal skimming, particularly the high-volume cash-out sequence at ATMs near the start of each month when Electronic Benefits Transfer accounts are funded by California.”

Armed with a victim’s PIN along with stolen card data, thieves can clone the card onto anything with a magnetic stripe and use it at ATMs to withdraw cash, or as a payment instrument at any establishment that accepts EBT cards.

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/sacskims.png)

Although it may be shocking that California — one of America’s wealthiest states — still treats EBT recipients as second-class citizens by issuing them chip-less debit cards, California [behaves like most other states in this regard](https://foodstampsebt.com/category/ebt-card/ebt-card-balance/).

More critical, however, is the second way SNAP cards differ from regular debit cards: Recipients of SNAP benefits have little to no hope of recovering their funds when their EBT cards are copied by card-skimming devices and used for fraud.

That’s because in the SNAP program, federal law bars the states from replacing SNAP benefits using federal funds. And while some of these EBT cards have Visa or MasterCard logos on them, it is not up to those companies to replace funds in the event of fraud.

Victims are encouraged to report the theft to both their state agency and the local police, but many victims say they rarely receive updates on their cases from police, and, if they hear from the state, it’s usually the agency telling them it found no evidence of fraud.

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/md-ebt.png)

Maryland’s EBT card.

That’s according to **Brenna Smith**, a reporter at *The Baltimore Banner* who [recently wrote about](https://www.thebaltimorebanner.com/community/criminal-justice/one-womans-quest-for-justice-after-almost-3000-of-benefits-were-stolen-LHIKMQZSNJBULC7LXCEIE264OA/) the case of a Maryland mother of three who lost nearly $3,000 in SNAP benefits thanks to a skimmer installed at a local 7-Eleven. Maryland [Department of Human Services] spokesperson Katherine Morris told the Banner there was evidence of “a nationwide EBT card cloning scheme.”

The woman profiled in Smith’s story contacted all of the retailers where her EBT card was used to buy thousands of dollars worth of baby formula. Two of those retailers agreed to share video surveillance footage of the people making the purchases at the exact timestamps specified in her EBT account history: The videos clearly showed it was the same fraudster making both purchases with a cloned copy of her EBT card.

Even after the police officer assigned to the victim’s case confirmed they found a skimmer installed at the 7-Eleven store she frequented, her claim — which was denied — is still languishing in appeals months later.

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/ebt-skimscammer.png)

(Left) A video still showing a couple purchasing almost $1,200 in baby formula using SNAP benefits. (Right) A video still of a woman leaving from the CVS in Seat Pleasant. Image: The Baltimore Banner.

**The Center for Law and Social Policy** (CLASP) recently published [Five Ways State Agencies Can Support EBT Users at Risk of Skimming](https://www.clasp.org/blog/five-ways-state-agencies-can-support-ebt-users-at-risk-of-skimming/). CLASP says while it is true states can’t use federal funds to replace benefits unless the loss wa...