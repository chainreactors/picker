---
title: How Solid Protocol Restores Digital Agency
url: https://www.schneier.com/blog/archives/2025/07/how-solid-protocol-restores-digital-agency.html
source: Schneier on Security
date: 2025-07-25
fetch_date: 2025-10-06T23:52:23.134337
---

# How Solid Protocol Restores Digital Agency

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## How the Solid Protocol Restores Digital Agency

The current state of digital identity is a mess. Your personal information is scattered across hundreds of locations: social media companies, IoT companies, government agencies, websites you have accounts on, and data brokers you’ve never heard of. These entities collect, store, and trade your data, often without your knowledge or consent. It’s both redundant and inconsistent. You have hundreds, maybe thousands, of fragmented digital profiles that often contain contradictory or logically impossible information. Each serves its own purpose, yet there is no central override and control to serve you—as the identity owner.

We’re used to the massive security failures resulting from all of this data under the control of so many different entities. Years of privacy breaches have resulted in a multitude of laws—in US states, in the EU, elsewhere—and calls for even more stringent protections. But while these laws attempt to protect data confidentiality, there is nothing to protect data integrity.

In this context, data integrity refers to its accuracy, consistency, and reliability…throughout its lifecycle. It means ensuring that data is not only accurately recorded but also remains logically consistent across systems, is up-to-date, and can be verified as authentic. When data lacks integrity, it can contain contradictions, errors, or outdated information—problems that can have serious real-world consequences.

Without data integrity, someone could classify you as a teenager while simultaneously attributing to you three teenage children: a biological impossibility. What’s worse, you have no visibility into the data profiles assigned to your identity, no mechanism to correct errors, and no authoritative way to update your information across all platforms where it resides.

Integrity breaches don’t get the same attention that confidentiality breaches do, but the picture isn’t pretty. A 2017 write-up in *The Atlantic* found error rates [exceeding 50%](https://www.theatlantic.com/technology/archive/2017/06/online-data-brokers/529281/) in some categories of personal information. A 2019 audit of data brokers found at least 40% of data broker sourced user attributes are “[not at all](https://www.lix.polytechnique.fr/~goga/papers/databrokers-measurement_finalCameraReady.pdf)” accurate. In 2022, the Consumer Financial Protection Bureau [documented](https://web.archive.org/web/20250228230511/https%3A//www.consumerfinance.gov/about-us/newsroom/cfpb-takes-action-to-address-junk-data-in-credit-reports/) [thousands](https://web.archive.org/web/20250221180714/https%3A//files.consumerfinance.gov/f/documents/cfpb_fair-credit-reporting-facially-false-data_advisory-opinion_2022-10.pdf) of cases where consumers were denied housing, employment, or financial services based on logically impossible data combinations in their profiles. Similarly, the National Consumer Law Center report called “[Digital Denials](https://www.nclc.org/wp-content/uploads/2023/09/202309_Report_Digital-Denials.pdf)” showed inaccuracies in tenant screening data that blocked people from housing.

And integrity breaches can have significant effects on our lives. In one 2024 British case, two companies [blamed each other](https://www.theguardian.com/money/2024/oct/14/they-are-ruining-my-life-how-the-shadowy-world-of-debt-collection-can-wreck-your-finances) for the faulty debt information that caused catastrophic financial consequences for an innocent victim. [Breonna Taylor was killed in 2020](https://www.congress.gov/117/meeting/house/111301/documents/HHRG-117-JU08-20210311-SD011.pdf) during a police raid on her apartment in Louisville, Kentucky, when officers executed a “no-knock” warrant on the wrong house based on bad data. They had faulty intelligence connecting her address to a suspect who actually lived elsewhere.

In some instances, we have rights to view our data, and in others, rights to correct it, but these sorts of solutions have only limited value. When journalist Julia Angwin attempted to correct her information across major data brokers for her book [*Dragnet Nation*](https://juliaangwin.com/books/)*,* she found that even after submitting corrections through official channels, a significant number of errors reappeared within six months.

In some instances, we have the right to delete our data, but—again—this only has limited value. Some data processing is legally required, and some is necessary for services we truly want and need.

Our focus needs to shift from the binary choice of either concealing our data entirely or surrendering all control over it. Instead, we need solutions that prioritize integrity in ways that balance privacy with the benefits of data sharing.

It’s not as if we haven’t made progress in better ways to manage online identity. Over the years, numerous trustworthy systems have been developed that could solve many of these problems. For example, imagine digital verification that works like a locked mobile phone—it works when you’re the one who can unlock and use it, but not if someone else grabs it from you. Or consider a storage device that holds all your credentials, like your driver’s license, professional certifications, and healthcare information, and lets you selectively share one without giving away everything at once. Imagine being able to share just a single cell in a table or a specific field in a file. These technologies already exist, and they could let you securely prove specific facts about yourself without surrendering control of your whole identity. This isn’t just theoretically better than traditional usernames and passwords; the technologies represent a fundamental shift in how we think about digital trust and verification.

Standards to do all these things emerged during the Web 2.0 era. We mostly haven’t used them because platform companies have been more interested in building barriers around user data and identity. They’ve used control of user identity as a key to market dominance and monetization. They’ve treated data as a corporate asset, and resisted open standards that would democratize data ownership and access. Closed, proprietary systems have better served their purposes.

There is another way. The Solid protocol, invented by Sir Tim Berners-Lee, represents a radical reimagining of how data operates online. Solid stands for “SOcial LInked Data.” At its core, it decouples data from applications by storing personal information in user-controlled “data wallets”: secure, personal data stores that users can host anywhere they choose. Applications can access specific data within these wallets, but users maintain ownership and control.

Solid is more than distributed data storage. This architecture inverts the current data ownership model. Instead of companies owning user data, users maintain a single source of truth for their personal informa...