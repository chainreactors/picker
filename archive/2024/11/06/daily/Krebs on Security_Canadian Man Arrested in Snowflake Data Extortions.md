---
title: Canadian Man Arrested in Snowflake Data Extortions
url: https://krebsonsecurity.com/2024/11/canadian-man-arrested-in-snowflake-data-extortions/
source: Krebs on Security
date: 2024-11-06
fetch_date: 2025-10-06T19:27:50.729122
---

# Canadian Man Arrested in Snowflake Data Extortions

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Canadian Man Arrested in Snowflake Data Extortions

November 5, 2024

[22 Comments](https://krebsonsecurity.com/2024/11/canadian-man-arrested-in-snowflake-data-extortions/#comments)

A 25-year-old man in Ontario, Canada has been arrested for allegedly stealing data from and extorting more than 160 companies that used the cloud data service **Snowflake**.

![](https://krebsonsecurity.com/wp-content/uploads/2024/11/snowflaking.png)

On October 30, Canadian authorities arrested **Alexander Moucka,** a.k.a. **Connor Riley Moucka** of Kitchener, Ontario, on a provisional arrest warrant from the United States. Bloomberg first [reported](https://www.bloomberg.com/news/articles/2024-11-05/hacker-said-to-be-behind-breach-of-snowflake-customers-arrested?embedded-checkout=true) Moucka’s alleged ties to the Snowflake hacks on Monday.

At the end of 2023, malicious hackers learned that many large companies had uploaded huge volumes of sensitive customer data to Snowflake accounts that were protected with little more than a username and password (no multi-factor authentication required). After scouring darknet markets for stolen Snowflake account credentials, the hackers began raiding the data storage repositories used by some of the world’s largest corporations.

Among those was **AT&T**, which [disclosed in July](https://krebsonsecurity.com/2024/07/hackers-steal-phone-sms-records-for-nearly-all-att-customers/) that cybercriminals had stolen personal information and phone and text message records for roughly 110 million people — nearly all of its customers. **Wired.com** [reported in July](https://www.wired.com/story/atandt-paid-hacker-300000-to-delete-stolen-call-records/) that AT&T paid a hacker $370,000 to delete stolen phone records.

A report on the extortion attacks from the incident response firm **Mandiant** notes that Snowflake victim companies were privately approached by the hackers, who demanded a ransom in exchange for a promise not to sell or leak the stolen data. All told, more than 160 Snowflake customers were relieved of data, including **TicketMaster**, **Lending Tree**, **Advance Auto Parts** and **Neiman Marcus**.

Moucka is alleged to have used the hacker handles **Judische** and **Waifu**, among many others. These monikers correspond to a prolific cybercriminal whose exploits were the subject of [a recent story published here](https://krebsonsecurity.com/2024/09/the-dark-nexus-between-harm-groups-and-the-com) about the overlap between Western, English-speaking cybercriminals and extremist groups that harass and extort minors into harming themselves or others.

On May 2, 2024, Judische claimed on the fraud-focused Telegram channel **Star Chat** that they had hacked **Santander Bank**, one of the first known Snowflake victims. Judische would repeat that claim in Star Chat on May 13 — the day before Santander publicly disclosed a data breach — and would periodically blurt out the names of other Snowflake victims before their data even went up for sale on the cybercrime forums.

404 Media [reports](https://www.404media.co/alleged-snowflake-hacker-appears-in-court-says-prison-in-lockdown/) that at a court hearing in Ontario this morning, Moucka called in from a prison phone and said he was seeking legal aid to hire an attorney.

## TELECOM DOMINOES

Mandiant has attributed the Snowflake compromises to a group it calls “**UNC5537**,” with members based in North America and [Turkey](https://krebsonsecurity.com/2021/08/t-mobile-investigating-claims-of-massive-data-breach/). Sources close to the investigation tell KrebsOnSecurity the UNC5537 member in Turkey is **John Erin Binns**, an elusive American man indicted by the **U.S. Department of Justice** (DOJ) for [a 2021 breach at T-Mobile](https://krebsonsecurity.com/2021/08/t-mobile-investigating-claims-of-massive-data-breach/) that exposed the personal information of at least 76.6 million customers.

**Update**: The Justice Department has [unsealed an indictment](https://krebsonsecurity.com/wp-content/uploads/2024/11/1.pdf) (PDF) against Moucka and Binns, charging them with one count of conspiracy; 10 counts of wire fraud; four counts of computer fraud and abuse; two counts of extortion in relation to computer fraud; and two counts aggravated identity theft.

In a statement on Moucka’s arrest, Mandiant said UNC5537 aka Alexander ‘Connor’ Moucka has proven to be one of the most consequential threat actors of 2024.

“In April 2024, UNC5537 launched a campaign, systematically compromising misconfigured SaaS instances across over a hundred organizations,” wrote **Austin Larsen**, Mandiant’s senior threat analyst. “The operation, which left organizations reeling from significant data loss and extortion attempts, highlighted the alarming scale of harm an individual can cause using off-the-shelf tools.”

Sources involved in the investigation said UNC5537 has focused on hacking into telecommunications companies around the world. Those sources told KrebsOnSecurity that Binns and Judische are suspected of [stealing data from India’s largest state-run telecommunications firm](https://economictimes.indiatimes.com/tech/technology/bsnl-suffers-second-data-breach-in-six-months/articleshow/111264707.cms?from=mdr) **Bharat Sanchar Nigam Ltd** (BNSL), and that the duo even bragged about being able to intercept or divert phone calls and text messages for a large portion of the population of India.

Judische appears to have outsourced the sale of databases from victim companies who refuse to pay, delegating some of that work to a cybercriminal who uses the nickname **Kiberphant0m** on multiple forums. In late May 2024, Kiberphant0m began advertising the sale of hundreds of gigabytes of data stolen from BSNL.

“Information is worth several million dollars but I’m selling for pretty cheap,” Kiberphant0m wrote of the BSNL data in a post on the English-language cybercrime community **Breach Forums**. “Negotiate a deal in Telegram.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/10/kiberphant0m-bf.png)

Also in May 2024, Kiberphant0m took to the Russian-language hacking forum **XSS** to sell more than 250 gigabytes of data stolen from an unnamed mobile telecom provider in Asia, including a database of all active customers and software allowing the sending of text messages to all customers.

On September 3, 2024, Kiberphant0m posted a sales thread on XSS titled “Selling American Telecom Access (100B+ Revenue).” Kiberphant0m’s asking price of $200,000 was apparently too high because they reposted the sales thread on Breach Forums a month later, with a headline that more clearly explained the data was stolen from **Verizon**‘s “push-to-talk” (PTT) customers — primarily U.S. government agencies and first responders.

[404Media reported recently](https://www.404media.co/hackers-advertise-stolen-verizon-push-to-talk-call-logs/) that the breach does not appear to impact the main consumer Verizon network. Rather, the hackers broke into a third party provider and stole data on Verizon’s PTT systems, which are a separate product marketed towards public sector agencies, enterprises, and small businesses to communicate internally.

## INTERVIEW WITH JUDISCHE

Investigators say Moucka shared a home in Kitchener with other tenants, but not his fa...