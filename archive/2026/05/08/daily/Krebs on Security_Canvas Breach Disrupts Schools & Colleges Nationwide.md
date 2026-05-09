---
title: Canvas Breach Disrupts Schools & Colleges Nationwide
url: https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/
source: Krebs on Security
date: 2026-05-08
fetch_date: 2026-05-09T05:09:08.197780
---

# Canvas Breach Disrupts Schools & Colleges Nationwide

Advertisement

[![](/b-doppel/13.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

Advertisement

[![](/b-doppel/14.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Canvas Breach Disrupts Schools & Colleges Nationwide

May 7, 2026

[36 Comments](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/#comments)

An ongoing data extortion attack targeting the widely-used education technology platform **Canvas** disrupted classes and coursework at school districts and universities across the United States today, after a cybercrime group defaced the service’s login page with a ransom demand that threatened to leak data from 275 million students and faculty across nearly 9,000 educational institutions.

![](https://krebsonsecurity.com/wp-content/uploads/2026/05/shinyhunters-instructure-canvas.png)

Canvas parent firm **Instructure** responded to today’s defacement attacks by disabling the platform, which is used by thousands of schools, universities and businesses to manage coursework and assignments, and to communicate with students.

Instructure acknowledged a data breach earlier this week, after the cybercrime group **ShinyHunters** claimed responsibility and said they would leak data on tens of millions of students and faculty unless paid a ransom. The stated deadline for payment was initially set at May 6, but it was later pushed back to May 12.

In [a statement](https://status.instructure.com/incidents/9wm4knj2r64z) on May 6, Instructure said the investigation so far shows the stolen information includes “certain identifying information of users at affected institutions, such as names, email addresses, and student ID numbers, as well as as messages among users.” The company said it found no evidence the breached data included more sensitive information, such as passwords, dates of birth, government identifiers or financial information.

The May 6 update stated that Canvas was fully operational, and that Instructure was not seeing any ongoing unauthorized activity on their platform. “At this stage, we believe the incident has been contained,” Instructure wrote.

However, by mid-day on Thursday, May 7, students and faculty at dozens of schools and universities were flooding social media sites with comments saying that a ransom demand from ShinyHunters had replaced the usual Canvas login page. Instructure responded by pulling Canvas offline and replacing the portal with the message, “Canvas is currently undergoing scheduled maintenance. Check back soon.”

“We anticipate being up soon, and will provide updates as soon as possible,” reads the current message on Instructure’s [status page](https://status.instructure.com/incidents/m88d7ymwpzpy).

While the data stolen by ShinyHunters may or may not contain particularly sensitive information (ShinyHunters claims it includes several billion private messages among students and teachers, as well as names, phone numbers and email addresses), this attack could hardly have come at a worse time for Instructure: Many of the affected schools and universities are in the middle of final exams, and a prolonged outage could be highly damaging for the company.

The extortion message that greeted countless Canvas users today advised the affected schools to negotiate their own ransom payments to prevent the publication of their data — regardless of whether Instructure decides to pay.

“ShinyHunters has breached Instructure (again),” the extortion message read. “Instead of contacting us to resolve it they ignored us and did some ‘security patches.'”

A source close to the investigation who was not authorized to speak to the press told KrebsOnSecurity that a number of universities have already approached the cybercrime group about paying. The same source also pointed out that the ShinyHunters data leak blog no longer lists Instructure among its current extortion victims, and that the samples of data stolen from Canvas customers were removed as well. Data extortion groups like ShinyHunters will typically only remove victims from their leak sites after receiving an extortion payment or after a victim agrees to negotiate.

**Dipan Mann**, founder and CEO of the security firm **Cloudskope**, slammed Instructure for referring to today’s outage as a “scheduled maintenance” event on its status page. Mann said Shiny Hunters first demonstrated they’d breached Instructure on May 1, prompting Instructure’s Chief Information Security Officer **Steve Proud** to declare the following day that the incident had been contained. But Mann said today’s attack is at least the third time in the past eight months that Instructure has been breached by ShinyHunters.

In a blog post today, Mann noted that in September 2025, ShinyHunters released thousands of internal University of Pennsylvania files — donor records, internal memos, and other confidential materials — through what the Daily Pennsylvanian and other outlets later determined was, in part, a Canvas/Instructure-mediated access path.

“Penn was the named victim,” Mann [wrote](https://www.cloudskope.com/insights/post/instructure-canvas-ransomware-attack-hits-universities-2026). “Instructure was the mechanism. The incident was treated as a Penn-specific story by most of the national press and quietly handled by Instructure as a customer-specific matter. That framing was wrong then. It is dramatically more wrong in light of the May 2026 events, which now look like the planned escalation of an attack pattern that ShinyHunters had been working against Instructure’s environment for at least eight months prior. The September 2025 Penn breach was the proof of concept. The May 1, 2026 incident was the production run. The May 7, 2026 recompromise was ShinyHunters demonstrating publicly that the May 2 ‘containment’ did not happen.”

In February, a ShinyHunters spokesperson told *The Daily Pennsylvanian* that Penn [failed to pay a $1 million ransom demand](https://www.thedp.com/article/2026/02/penn-hack-donor-data-ransom-one-million-shinyhunters-gse-emai). On March 5, ShinyHunters published 461 megabytes worth of data stolen from Penn, including thousands of files such as donor records and internal memos.

ShinyHunters is a prolific and fluid cybercriminal group that specializes in data theft and extortion. They typically gain access to companies through voice phishing and social engineering attacks that often involve impersonating IT personnel or other trusted members of a targeted organization.

Last month, ShinyHunters relieved the home security giant **ADT** of personal information on 5.5 million customers. The extortion group [told BleepingComputer](https://www.bleepingcomputer.com/news/security/home-security-giant-adt-data-breach-affects-55-million-people/) they breached the company by compromising an employee’s Okta single sign-on account in a voice phishing attack that enabled access to ADT’s Salesforce instance. BleepingComputer says ShinyHunters recently has taken credit for a number of extortion attacks against high-profile organizations, including Medtronic, Rockstar Games, McGraw Hill, 7-Eleven and the cruise line operator Carnival.

The attack on Canvas customers is just one of several major cybercrime campaigns being launched by ShinyHunters at the moment, said **Charles Carmakal**, chief technology officer at the Google-owned **Mandiant Consulting**. Carmakal declined to comment specifically on the Canvas breach, but said “there are multiple concurr...