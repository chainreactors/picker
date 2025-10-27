---
title: NationalPublicData.com Hack Exposes a Nation’s Data
url: https://krebsonsecurity.com/2024/08/nationalpublicdata-com-hack-exposes-a-nations-data/
source: Krebs on Security
date: 2024-08-16
fetch_date: 2025-10-06T18:18:54.956200
---

# NationalPublicData.com Hack Exposes a Nation’s Data

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# NationalPublicData.com Hack Exposes a Nation’s Data

August 15, 2024

[43 Comments](https://krebsonsecurity.com/2024/08/nationalpublicdata-com-hack-exposes-a-nations-data/#comments)

A great many readers this month reported receiving alerts that their Social Security Number, name, address and other personal information were exposed in a breach at a little-known but aptly-named consumer data broker called **NationalPublicData.com**. This post examines what we know about a breach that has exposed hundreds of millions of consumer records. We’ll also take a closer look at the data broker that got hacked — a background check company founded by an actor and retired sheriff’s deputy from Florida.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/nationalpublicdata-home.png)

On July 21, 2024, denizens of the cybercrime community **Breachforums** released more than 4 terabytes of data they claimed was stolen from nationalpublicdata.com, a Florida-based company that collects data on consumers and processes background checks.

The breach tracking service **HaveIBeenPwned.com** and the cybercrime-focused Twitter account [vx-underground](https://twitter.com/vxunderground) both concluded the leak is the same information first put up for sale in April 2024 by a prolific cybercriminal who goes by the name “**USDoD**.”

On April 7, USDoD posted a sales thread on Breachforums for four terabytes of data — 2.9 billion rows of records — they claimed was taken from nationalpublicdata.com. The snippets of stolen data that USDoD offered as teasers showed rows of names, addresses, phone numbers, and Social Security Numbers (SSNs). Their asking price? $3.5 million.

Many media outlets mistakenly reported that the National Public data breach affects 2.9 billion people (that figure actually refers to the number of rows in the leaked data sets). HaveIBeenPwned.com’s **Troy Hunt** [analyzed the leaked data](https://www.troyhunt.com/inside-the-3-billion-people-national-public-data-breach/) and found it is a somewhat disparate collection of consumer and business records, including the real names, addresses, phone numbers and SSNs of millions of Americans (both living and deceased), and 70 million rows from a database of U.S. criminal records.

Hunt said he found 137 million unique email addresses in the leaked data, but stressed that there were no email addresses in the files containing SSN records.

“If you find yourself in this data breach via HaveIBeenPwned.com, there’s no evidence your SSN was leaked, and if you’re in the same boat as me, the data next to your record may not even be correct.”

Nationalpublicdata.com publicly acknowledged a breach in [a statement on Aug. 12](https://nationalpublicdata.com/Breach.html), saying “there appears to have been a data security incident that may have involved some of your personal information. The incident appears to have involved a third-party bad actor that was trying to hack into data in late December 2023, with potential leaks of certain data in April 2024 and summer 2024.”

The company said the information “suspected of being breached” contained name, email address, phone number, social security number, and mailing address(es).

“We cooperated with law enforcement and governmental investigators and conducted a review of the potentially affected records and will try to notify you if there are further significant developments applicable to you,” the statement continues. “We have also implemented additional security measures in efforts to prevent the reoccurrence of such a breach and to protect our systems.”

Hunt’s analysis didn’t say how many unique SSNs were included in the leaked data. But according to researchers at **Atlas Data Privacy Corp.**, there are 272 million unique SSNs in the entire records set.

Atlas found most records have a name, SSN, and home address, and that approximately 26 percent of those records included a phone number. Atlas said they verified 5,000 addresses and phone numbers, and found the records pertain to people born before Jan. 1, 2002 (with very few exceptions).

If there is a tiny silver lining to the breach it is this: Atlas discovered that many of the records related to people who are now almost certainly deceased. They found the average age of the consumer in these records is 70, and fully two million records are related to people whose date of birth would make them more than 120 years old today.

## TWISTED HISTORY

Where did National Public Data get its consumer data? The company’s website doesn’t say, but it is operated by an entity in Coral Springs, Fla. called **Jerico Pictures Inc.** The website for Jerico Pictures is not currently responding. However, [cached versions of it at archive.org](https://web.archive.org/web/20230330052412/http%3A//www.jericopictures.com/) show it is a film studio with offices in Los Angeles and South Florida.

The Florida Secretary of State says Jerico Pictures is owned by **Salvatore (Sal) Verini Jr.**, a retired deputy with the Broward County Sheriff’s office. The Secretary of State also says Mr. Verini is or was a founder of several other Florida companies, including **National Criminal Data LLC**, **Twisted History LLC**, **Shadowglade LLC** and **Trinity Entertainment Inc.**, among others.

Mr. Verini did not respond to multiple requests for comment. Cached copies of Mr. Verini’s vanity domain [salvatoreverini.com](https://web.archive.org/web/20230323175843/http%3A//www.salvatoreverini.com/) recount his experience in acting (e.g. a role in a 1980s detective drama with Burt Reynolds) and more recently producing dramas and documentaries for several streaming channels.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/salverini-imdb.png)

Sal Verini’s profile page at imdb.com.

Pivoting on the email address used to register that vanity domain, **DomainTools.com** finds several other domains whose history offers a clearer picture of the types of data sources relied upon by National Public Data.

One of those domains is **recordscheck.net** (formerly **recordscheck.info**), which advertises “instant background checks, SSN traces, employees screening and more.” Another now-defunct business tied to Mr. Verini’s email — [publicrecordsunlimited.com](https://web.archive.org/web/20150110212648/http%3A//www.publicrecordsunlimited.com/products.html) — said it obtained consumer data from a variety of sources, including: birth, marriage and death records; voting records; professional licenses; state and federal criminal records.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/publicrecordsunlimited.png)

The homepage for publicrecordsunlimited.com, per archive.org circa 2017.

It remains unclear how thieves originally obtained these records from National Public Data. KrebsOnSecurity sought comment from USDoD, who is perhaps best known for [hacking into Infragard, an FBI program](https://krebsonsecurity.com/2022/12/fbis-vetted-info-sharing-network-infragard-hacked/) that facilitates information sharing about cyber and physical threats with vetted people in the private sector.

USDoD said they indeed sold the same data set that was leaked on Breachforums this past month, but that the person who leaked the data did not obtain it from them. USDoD said the data s...