---
title: Phishers Target Aviation Execs to Scam Customers
url: https://krebsonsecurity.com/2025/07/phishers-target-aviation-execs-to-scam-customers/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-25
fetch_date: 2025-10-06T23:50:04.641747
---

# Phishers Target Aviation Execs to Scam Customers

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Phishers Target Aviation Execs to Scam Customers

July 24, 2025

[10 Comments](https://krebsonsecurity.com/2025/07/phishers-target-aviation-execs-to-scam-customers/#comments)

KrebsOnSecurity recently heard from a reader whose boss’s email account got phished and was used to trick one of the company’s customers into sending a large payment to scammers. An investigation into the attacker’s infrastructure points to a long-running Nigerian cybercrime ring that is actively targeting established companies in the transportation and aviation industries.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/shutterstock-airplanes.png)

A reader who works in the transportation industry sent a tip about a recent successful phishing campaign that tricked an executive at the company into entering their credentials at a fake Microsoft 365 login page. From there, the attackers quickly mined the executive’s inbox for past communications about invoices, copying and modifying some of those messages with new invoice demands that were sent to some of the company’s customers and partners.

Speaking on condition of anonymity, the reader said the resulting phishing emails to customers came from a newly registered domain name that was remarkably similar to their employer’s domain, and that at least one of their customers fell for the ruse and paid a phony invoice. They said the attackers had spun up a look-alike domain just a few hours after the executive’s inbox credentials were phished, and that the scam resulted in a customer suffering a six-figure financial loss.

The reader also shared that the email addresses in the registration records for the imposter domain — **roomservice801@gmail.com** — is tied to many such phishing domains. Indeed, a search on this email address at **DomainTools.com** finds it is associated with at least 240 domains registered in 2024 or 2025. Virtually all of them mimic legitimate domains for companies in the aerospace and transportation industries worldwide.

An Internet search for this email address reveals [a humorous blog post from 2020](https://web.archive.org/web/20220514070749/https%3A//hackware.ru/?p=12106) on the Russian forum hackware[.]ru, which found roomservice801@gmail.com was tied to a phishing attack that used the lure of phony invoices to trick the recipient into logging in at a fake Microsoft login page. We’ll come back to this research in a moment.

## JUSTY JOHN

DomainTools shows that some of the early domains registered to roomservice801@gmail.com in 2016 include other useful information. For example, the WHOIS records for **alhhomaidhicentre[.]biz** reference the technical contact of “**Justy John**” and the email address **justyjohn50@yahoo.com**.

A search at DomainTools found justyjohn50@yahoo.com has been registering one-off phishing domains since at least 2012. At this point, I was convinced that some security company surely had already published an analysis of this particular threat group, but I didn’t yet have enough information to draw any solid conclusions.

DomainTools says the Justy John email address is tied to more than two dozen domains registered since 2012, but we can find hundreds more phishing domains and related email addresses simply by pivoting on details in the registration records for these Justy John domains. For example, the street address used by the Justy John domain **axisupdate[.]net** — 7902 Pelleaux Road in Knoxville, TN — also appears in the registration records for accountauthenticate[.]com, acctlogin[.]biz, and loginaccount[.]biz, all of which at one point included the email address **rsmith60646@gmail.com**.

That Rsmith Gmail address is connected to the 2012 phishing domain alibala[.]biz (one character off of the Chinese e-commerce giant alibaba.com, with a different top-level domain of .biz). A search in DomainTools on the phone number in those domain records — 1.7736491613 — reveals even more phishing domains as well as the Nigerian phone number “2348062918302” and the email address **michsmith59@gmail.com**.

DomainTools shows michsmith59@gmail.com appears in the registration records for the domain **seltrock[.]com**, which was used in the phishing attack documented in [the 2020 Russian blog post](https://web.archive.org/web/20220514070749/https%3A//hackware.ru/?p=12106) mentioned earlier. At this point, we are just two steps away from identifying the threat actor group.

The same Nigerian phone number shows up in dozens of domain registrations that reference the email address **sebastinekelly69@gmail.com**, including **26i3[.]net**, **costamere[.]com**, **danagruop[.]us**, and **dividrilling[.]com**. A Web search on any of those domains finds they were indexed in [an “indicator of compromise” list on GitHub](https://github.com/pan-unit42/iocs/blob/master/silverterrier/domains.csv) maintained by **Palo Alto Networks**‘ **Unit 42** research team.

## SILVERTERRIER

According to Unit 42, the domains are the handiwork of a vast cybercrime group based in Nigeria that it dubbed “**SilverTerrier**” back in 2014. In [an October 2021 report](https://unit42.paloaltonetworks.com/silverterrier-nigerian-business-email-compromise/), Palo Alto said SilverTerrier excels at so-called “**business e-mail compromise**” or **BEC** scams, which target legitimate business email accounts through social engineering or computer intrusion activities. BEC criminals use that access to initiate or redirect the transfer of business funds for personal gain.

Palo Alto says SilverTerrier encompasses hundreds of BEC fraudsters, some of whom have been arrested in various international law enforcement operations by **Interpol**. In 2022, Interpol and the Nigeria Police Force [arrested 11 alleged SilverTerrier members](https://www.interpol.int/en/News-and-Events/News/2022/Nigerian-cybercrime-fraud-11-suspects-arrested-syndicate-busted), including [a prominent SilverTerrier leader](https://unit42.paloaltonetworks.com/operation-delilah-business-email-compromise-actor/) who’d been flaunting his wealth on social media for years. Unfortunately, the lure of easy money, endemic poverty and corruption, and low barriers to entry for cybercrime in Nigeria conspire to provide a constant stream of new recruits.

BEC scams were the 7th most reported crime tracked by the FBI’s **Internet Crime Complaint Center** (IC3) in 2024, generating more than 21,000 complaints. However, BEC scams were the second most costly form of cybercrime reported to the feds last year, with *nearly $2.8 billion in claimed losses*. In its [2025 Fraud and Control Survey Report](https://www.afponline.org/training-resources/resources/survey-research-economic-data/Details/payments-fraud), the **Association for Financial Professionals** found 63 percent of organizations experienced a BEC last year.

Poking at some of the email addresses that spool out from this research reveals a number of Facebook accounts for people residing in Nigeria or in the United Arab Emirates, many of whom do not appear to have tried to mask their real-life identities. Palo Alto’s Unit 42 researchers reached a similar conclusion, noting that although a small subset of these crooks went to great lengths to conceal their identities, it was usually simple to learn their identities on social media acc...