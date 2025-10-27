---
title: Hackers Steal Phone, SMS Records for Nearly All AT&T Customers
url: https://krebsonsecurity.com/2024/07/hackers-steal-phone-sms-records-for-nearly-all-att-customers/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-13
fetch_date: 2025-10-06T17:45:07.672326
---

# Hackers Steal Phone, SMS Records for Nearly All AT&T Customers

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Crooks Steal Phone, SMS Records for Nearly All AT&T Customers

July 12, 2024

[51 Comments](https://krebsonsecurity.com/2024/07/hackers-steal-phone-sms-records-for-nearly-all-att-customers/#comments)

**AT&T Corp.** disclosed today that a new data breach has exposed phone call and text message records for roughly 110 million people — nearly all of its customers. AT&T said it delayed disclosing the incident in response to “national security and public safety concerns,” noting that some of the records included data that could be used to determine where a call was made or text message sent. AT&T also acknowledged the customer records were exposed in a cloud database that was protected only by a username and password (no multi-factor authentication needed).

![](https://krebsonsecurity.com/wp-content/uploads/2023/03/attbldg.png)

In [a regulatory filing](https://www.sec.gov/Archives/edgar/data/732717/000073271724000046/t-20240506.htm) with the **U.S. Securities and Exchange Commission** today, AT&T said cyber intruders accessed an AT&T workspace on a third-party cloud platform in April, downloading files containing customer call and text interactions between May 1 and October 31, 2022, as well as on January 2, 2023.

The company said the stolen data includes records of calls and texts for mobile providers that resell AT&T’s service, but that it does not include the content of calls or texts, Social Security numbers, dates of birth, or any other personally identifiable information.

However, the company said a subset of stolen records included information about the location of cellular communications towers closest to the subscriber, data that could be used to determine the approximate location of the customer device initiating or receiving those text messages or phone calls.

“While the data does not include customer names, there are often ways, using publicly available online tools, to find the name associated with a specific telephone number,” AT&T allowed.

AT&T’s said it learned of the breach on April 19, but delayed disclosing it at the request of federal investigators. The company’s SEC disclosure says at least one individual has been detained by the authorities in connection with the breach.

In a written statement shared with KrebsOnSecurity, the FBI confirmed that it asked AT&T to delay notifying affected customers.

“Shortly after identifying a potential breach to customer data and before making its materiality decision, AT&T contacted the FBI to report the incident,” the FBI statement reads. “In assessing the nature of the breach, all parties discussed a potential delay to public reporting under Item 1.05(c) of the SEC Rule, due to potential risks to national security and/or public safety. AT&T, FBI, and DOJ worked collaboratively through the first and second delay process, all while sharing key threat intelligence to bolster FBI investigative equities and to assist AT&T’s incident response work.”

[Techcrunch](https://techcrunch.com/2024/07/12/att-phone-records-stolen-data-breach/?guccounter=1) quoted an AT&T spokesperson saying the customer data was stolen as a result of a still-unfolding data breach involving more than 160 customers of the cloud data provider **Snowflake**.

Earlier this year, malicious hackers figured out that many major companies have uploaded massive amounts of valuable and sensitive customer data to Snowflake servers, all the while protecting those Snowflake accounts with little more than a username and password.

[Wired reported](https://www.wired.com/story/epam-snowflake-ticketmaster-breach-shinyhunters/) last month how the hackers behind the Snowflake data thefts purchased stolen Snowflake credentials from dark web services that sell access to usernames, passwords and authentication tokens that are siphoned by information-stealing malware. For its part, Snowflake says it now requires all new customers to use multi-factor authentication.

Other companies with millions of customer records stolen from Snowflake servers include **Advance Auto Parts**, **Allstate**, **Anheuser-Busch**, **Los Angeles Unified**, **Mitsubishi**, **Neiman Marcus**, **Pure Storage**, **Santander Bank**, **State Farm**, and **Ticketmaster**.

Earlier this year, AT&T [reset passwords for millions of customers](https://techcrunch.com/2024/03/30/att-reset-account-passcodes-customer-data/) after the company [finally acknowledged a data breach from 2018](https://krebsonsecurity.com/2022/08/it-might-be-our-data-but-its-not-our-breach/) involving approximately 7.6 million current AT&T account holders and roughly 65.4 million former account holders.

**Mark Burnett** is an application security architect, consultant and author. Burnett said the only real use for the data stolen in the most recent AT&T breach is to know who is contacting whom and how many times.

“The most concerning thing to me about this AT&T breach of ALL customer call and text records is that this isn’t one of their main databases; it is metadata on who is contacting who,” Burnett [wrote](https://infosec.exchange/%40zcutlip%40hachyderm.io/112774443764622821) on Mastodon. “Which makes me wonder what would call logs without timestamps or names have been used for.”

It remains unclear why so many major corporations persist in the belief that it is somehow acceptable to store so much sensitive customer data with so few security protections. For example, Advance Auto Parts said the data exposed included full names, Social Security numbers, drivers licenses and government issued ID numbers on [2.3 million people](https://www.bleepingcomputer.com/news/security/advance-auto-parts-data-breach-impacts-23-million-people/) who were former employees or job applicants.

That may be because, apart from the class-action lawsuits that invariably ensue after these breaches, there is little holding companies accountable for sloppy security practices. AT&T told the SEC it does not believe this incident is likely to materially impact AT&T’s financial condition or results of operations. AT&T reported revenues of more than $30 billion in its most recent quarter.

*This entry was posted on Friday 12th of July 2024 02:12 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/)

[Advance Auto Parts](https://krebsonsecurity.com/tag/advance-auto-parts/) [Allstate](https://krebsonsecurity.com/tag/allstate/) [Anheuser-Busch](https://krebsonsecurity.com/tag/anheuser-busch/) [AT&T breach](https://krebsonsecurity.com/tag/att-breach/) [fbi](https://krebsonsecurity.com/tag/fbi/) [Los Angeles Unified](https://krebsonsecurity.com/tag/los-angeles-unified/) [Mitsubishi](https://krebsonsecurity.com/tag/mitsubishi/) [Neiman Marcus](https://krebsonsecurity.com/tag/neiman-marcus/) [Pure Storage](https://krebsonsecurity.com/tag/pure-storage/) [Santander Bank](https://krebsonsecurity.com/tag/santander-bank/) [Snowflake hack](https://krebsonsecurity.com/tag/snowflake-hack/) [State Farm](https://krebsonsecurity.com/tag/state-farm/) [Techcrunch](https://krebsonsecurity.com/tag/techcrunch/) [...