---
title: Whistleblower: DOGE Siphoned NLRB Case Data
url: https://krebsonsecurity.com/2025/04/whistleblower-doge-siphoned-nlrb-case-data/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-23
fetch_date: 2025-10-06T22:08:59.018953
---

# Whistleblower: DOGE Siphoned NLRB Case Data

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Whistleblower: DOGE Siphoned NLRB Case Data

April 21, 2025

[88 Comments](https://krebsonsecurity.com/2025/04/whistleblower-doge-siphoned-nlrb-case-data/#comments)

A security architect with the **National Labor Relations Board** (NLRB) alleges that employees from **Elon Musk**‘s **Department of Government Efficiency** (DOGE) transferred gigabytes of sensitive data from agency case files in early March, using short-lived accounts configured to leave few traces of network activity. The NLRB whistleblower said the unusual large data outflows coincided with multiple blocked login attempts from an Internet address in Russia that tried to use valid credentials for a newly-created DOGE user account.

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/beruliscomplaint.png)

The allegations came in an April 14 letter to the Senate Select Committee on Intelligence, signed by **Daniel J. Berulis**, a 38-year-old security architect at the NLRB.

**NPR**, which was the [first to report](https://www.npr.org/2025/04/15/nx-s1-5355896/doge-nlrb-elon-musk-spacex-security) on Berulis’s whistleblower complaint, says NLRB is a small, independent federal agency that investigates and adjudicates complaints about unfair labor practices, and stores “reams of potentially sensitive data, from confidential information about employees who want to form unions to proprietary business information.”

The complaint documents a one-month period beginning March 3, during which DOGE officials reportedly demanded the creation of all-powerful “tenant admin” accounts in NLRB systems that were to be exempted from network logging activity that would otherwise keep a detailed record of all actions taken by those accounts.

Berulis said the new DOGE accounts had unrestricted permission to read, copy, and alter information contained in NLRB databases. The new accounts also could restrict log visibility, delay retention, route logs elsewhere, or even remove them entirely — top-tier user privileges that neither Berulis nor his boss possessed.

Berulis writes that on March 3, a black SUV accompanied by a police escort arrived at his building — the NLRB headquarters in Southeast Washington, D.C. The DOGE staffers did not speak with Berulis or anyone else in NLRB’s IT staff, but instead met with the agency leadership.

“Our acting chief information officer told us not to adhere to standard operating procedure with the DOGE account creation, and there was to be no logs or records made of the accounts created for DOGE employees, who required the highest level of access,” Berulis wrote of their instructions after that meeting.

“We have built in roles that auditors can use and have used extensively in the past but would not give the ability to make changes or access subsystems without approval,” he continued. “The suggestion that they use these accounts was not open to discussion.”

Berulis found that on March 3 one of the DOGE accounts created an opaque, virtual environment known as a “container,” which can be used to build and run programs or scripts without revealing its activities to the rest of the world. Berulis said the container caught his attention because he polled his colleagues and found none of them had ever used containers within the NLRB network.

Berulis said he also noticed that early the next morning — between approximately 3 a.m. and 4 a.m. EST on Tuesday, March 4  — there was a large increase in outgoing traffic from the agency. He said it took several days of investigating with his colleagues to determine that one of the new accounts had transferred approximately 10 gigabytes worth of data from the NLRB’s **NxGen** case management system.

Berulis said neither he nor his co-workers had the necessary network access rights to review which files were touched or transferred — or even where they went. But his complaint notes the NxGen database contains sensitive information on unions, ongoing legal cases, and corporate secrets.

“I also don’t know if the data was only 10gb in total or whether or not they were consolidated and compressed prior,” Berulis told the senators. “This opens up the possibility that even more data was exfiltrated. Regardless, that kind of spike is extremely unusual because data almost never directly leaves NLRB’s databases.”

Berulis said he and his colleagues grew even more alarmed when they noticed nearly two dozen login attempts from a Russian Internet address (83.149.30,186) that presented valid login credentials for a DOGE employee account — one that had been created just minutes earlier. Berulis said those attempts were all blocked thanks to rules in place that prohibit logins from non-U.S. locations.

“Whoever was attempting to log in was using one of the newly created accounts that were used in the other DOGE related activities and it appeared they had the correct username and password due to the authentication flow only stopping them due to our no-out-of-country logins policy activating,” Berulis wrote. “There were more than 20 such attempts, and what is particularly concerning is that many of these login attempts occurred within 15 minutes of the accounts being created by DOGE engineers.”

According to Berulis, the naming structure of one Microsoft user account connected to the suspicious activity suggested it had been created and later deleted for DOGE use in the NLRB’s cloud systems: “**DogeSA\_2d5c3e0446f9@nlrb.microsoft.com**.” He also found other new Microsoft cloud administrator accounts with nonstandard usernames, including “**Whitesox, Chicago M.**” and “**Dancehall, Jamaica R**.”

[![](https://krebsonsecurity.com/wp-content/uploads/2025/04/whitesoxchicago.png)](https://krebsonsecurity.com/wp-content/uploads/2025/04/whitesoxchicago.png)

A screenshot shared by Berulis showing the suspicious user accounts.

On March 5, Berulis documented that a large section of logs for recently created network resources were missing, and a network watcher in **Microsoft Azure** was set to the “off” state, meaning it was no longer collecting and recording data like it should have.

Berulis said he discovered someone had downloaded three external code libraries from **GitHub** that neither NLRB nor its contractors ever use. A “readme” file in one of the code bundles explained it was created to rotate connections through a large pool of cloud Internet addresses that serve “as a proxy to generate pseudo-infinite IPs for web scraping and brute forcing.” Brute force attacks involve automated login attempts that try many credential combinations in rapid sequence.

The complaint alleges that by March 17 it became clear the NLRB no longer had the resources or network access needed to fully investigate the odd activity from the DOGE accounts, and that on March 24, the agency’s associate chief information officer had agreed the matter should be reported to **US-CERT**. Operated by the Department of Homeland Security’s **Cybersecurity and Infrastructure Security Agency** (CISA), US-CERT provides on-site cyber incident response capabilities to federal and state agencies.

But Berulis said that between April 3 and 4, he and the associate CIO were informed that “instructions had come down to drop the US-CERT reporting and investigation and we were directed not to move forward or create...