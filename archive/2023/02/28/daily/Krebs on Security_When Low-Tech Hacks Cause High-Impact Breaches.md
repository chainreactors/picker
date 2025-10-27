---
title: When Low-Tech Hacks Cause High-Impact Breaches
url: https://krebsonsecurity.com/2023/02/when-low-tech-hacks-cause-high-impact-breaches/
source: Krebs on Security
date: 2023-02-28
fetch_date: 2025-10-04T08:16:32.691713
---

# When Low-Tech Hacks Cause High-Impact Breaches

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# When Low-Tech Hacks Cause High-Impact Breaches

February 26, 2023

[12 Comments](https://krebsonsecurity.com/2023/02/when-low-tech-hacks-cause-high-impact-breaches/#comments)

Web hosting giant **GoDaddy** made headlines this month when it disclosed that a multi-year breach allowed intruders to steal company source code, siphon customer and employee login credentials, and foist malware on customer websites. Media coverage understandably focused on GoDaddy’s admission that it suffered three different cyberattacks over as many years at the hands of the same hacking group.  But it’s worth revisiting how this group typically got in to targeted companies: By calling employees and tricking them into navigating to a phishing website.

![](https://krebsonsecurity.com/wp-content/uploads/2018/09/cell8.png)

In [a filing](https://www.sec.gov/ix?doc=/Archives/edgar/data/1609711/000160971123000031/gddy-20221231.htm) with the **U.S. Securities and Exchange Commission** (SEC), GoDaddy said it determined that the same “sophisticated threat actor group” was responsible for three separate intrusions, including:

**-March 2020:** A spear-phishing attack on a GoDaddy employee compromised the hosting login credentials of approximately 28,000 GoDaddy customers, as well as login credentials for a small number employees;

**-November 2021:** A compromised GoDaddy password let attackers steal source code and information tied to 1.2 million customers, including website administrator passwords, sFTP credentials, and private SSL keys;

**-December 2022:** Hackers gained access to and installed malware on GoDaddy’s cPanel hosting servers that “intermittently redirected random customer websites to malicious sites.”

“Based on our investigation, we believe these incidents are part of a multi-year campaign by a sophisticated threat actor group that, among other things, installed malware on our systems and obtained pieces of code related to some services within GoDaddy,” the company stated in its SEC filing.

What else do we know about the cause of these incidents? We don’t know much about the source of the November 2021 incident, other than GoDaddy’s statement that it involved a compromised password, and that it took about two months for the company to detect the intrusion. GoDaddy has not disclosed the source of the breach in December 2022 that led to malware on some customer websites.

But we do know the March 2020 attack was precipitated by [a spear-phishing attack against a GoDaddy employee](https://krebsonsecurity.com/2020/03/phish-of-godaddy-employee-jeopardized-escrow-com-among-others/). GoDaddy described the incident at the time in general terms as a social engineering attack, but one of its customers affected by that March 2020 breach actually spoke to one of the hackers involved.

The hackers were able to change the Domain Name System (DNS) records for the transaction brokering site **escrow.com** so that it pointed to an address in Malaysia that was host to just a few other domains, including the [then brand-new phishing domain](https://urlscan.io/result/d6de464d-f30d-4350-8324-d0f8997daf38/) **servicenow-godaddy[.]com**.

The general manager of Escrow.com found himself on the phone with one of the GoDaddy hackers, after someone who claimed they worked at GoDaddy called and said they needed him to authorize some changes to the account.

In reality, the caller had just tricked a GoDaddy employee into giving away their credentials, and he could see from the employee’s account that Escrow.com required a specific security procedure to complete a domain transfer.

The general manager of Escrow.com said he suspected the call was a scam, but decided to play along for about an hour — all the while recording the call and coaxing information out of the scammer.

“This guy had access to the notes, and knew the number to call,” to make changes to the account, the CEO of Escrow.com told KrebsOnSecurity. “He was literally reading off the tickets to the notes of the admin panel inside GoDaddy.”

About halfway through this conversation — after being called out by the general manager as an imposter — the hacker admitted that he was not a GoDaddy employee, and that he was in fact part of a group that enjoyed repeated success with social engineering employees at targeted companies over the phone.

Absent from GoDaddy’s SEC statement is another spate of attacks in November 2020, in which unknown intruders [redirected email and web traffic for multiple cryptocurrency services](https://krebsonsecurity.com/2020/11/godaddy-employees-used-in-attacks-on-multiple-cryptocurrency-services/) that used GoDaddy in some capacity.

It is possible this incident was not mentioned because it was the work of yet another group of intruders. But in response to questions from KrebsOnSecurity at the time, GoDaddy said that incident also stemmed from a “limited” number of GoDaddy employees falling for a sophisticated social engineering scam.

“As threat actors become increasingly sophisticated and aggressive in their attacks, we are constantly educating employees about new tactics that might be used against them and adopting new security measures to prevent future attacks,” GoDaddy said in a written statement back in 2020.

Voice phishing or “vishing” attacks typically target employees who work remotely. The phishers will usually claim that they’re calling from the employer’s IT department, supposedly to help troubleshoot some issue. The goal is to convince the target to enter their credentials at a website set up by the attackers that mimics the organization’s corporate email or VPN portal.

Experts interviewed for an [August 2020 story on a steep rise in successful voice phishing attacks](https://krebsonsecurity.com/2020/08/voice-phishers-targeting-corporate-vpns/) said there are generally at least two people involved in each vishing scam: One who is social engineering the target over the phone, and another co-conspirator who takes any credentials entered at the phishing page — including multi-factor authentication codes shared by the victim — and quickly uses them to log in to the company’s website.

The attackers are usually careful to do nothing with the phishing domain until they are ready to initiate a vishing call to a potential victim. And when the attack or call is complete, they disable the website tied to the domain.

This is key because many domain registrars will only respond to external requests to take down a phishing website if the site is live at the time of the abuse complaint. This tactic also can stymie efforts by companies that focus on identifying newly-registered phishing domains before they can be used for fraud.

![](https://krebsonsecurity.com/wp-content/uploads/2014/10/yubikey.png)

GoDaddy’s latest SEC filing indicates the company had nearly 7,000 employees as of December 2022. In addition, GoDaddy contracts with another 3,000 people who work full-time for the company via business process outsourcing companies based primarily in India, the Philippines and Colombia.

Many companies now require employees to supply a one-time password — such as one sent via SMS or produced by a mobile authenticator app — in addition to their username and pass...