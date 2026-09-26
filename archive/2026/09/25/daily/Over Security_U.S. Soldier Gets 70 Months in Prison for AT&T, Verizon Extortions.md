---
title: U.S. Soldier Gets 70 Months in Prison for AT&T, Verizon Extortions
url: https://krebsonsecurity.com/2026/09/u-s-soldier-gets-70-months-in-prison-for-att-verizon-extortions/
source: Over Security
date: 2026-09-25
fetch_date: 2026-09-26T06:51:38.118725
---

# U.S. Soldier Gets 70 Months in Prison for AT&T, Verizon Extortions

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-doppel/18.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# U.S. Soldier Gets 70 Months in Prison for AT&T, Verizon Extortions

September 25, 2026

[2 Comments](https://krebsonsecurity.com/2026/09/u-s-soldier-gets-70-months-in-prison-for-att-verizon-extortions/#comments)

A U.S. Army soldier who pleaded guilty to hacking into multiple telecommunications companies and stealing mobile call and text metadata for more than 100 million **AT&T** customers in 2024 was sentenced to 70 months in federal prison today and ordered to pay nearly $300,000 in restitution to victims.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/camwagenius-selfie.png)

One of several selfies from the Facebook page of Cameron Wagenius.

**Cameron John Wagenius**, 22, was stationed at a U.S. Army base in South Korea when he adopted the cybercriminal persona “**Kiberphant0m**.” Working with three alleged co-conspirators, Kiberphant0m downloaded data from several large customers of the cloud data storage service **Snowflake** that had exposed credentials and did not enforce multi-factor authentication (Snowflake has since mandated MFA on all accounts).

In October 2024, Kiberphant0m bragged on the cybercrime forums that he’d stolen the call and text metadata (e.g. source and destination number, timestamp, duration, etc.) for tens of millions of AT&T customers. Kiberphant0m claimed to have hacked into more than dozen telecommunications companies worldwide, including Verizon’s Push-to-Talk business, and publicly extorted these companies in exchange for a promise not to publish the stolen data.

In late November 2025, KrebsOnSecurity warned that Kiberphant0m [was likely a U.S. soldier stationed in South Korea](https://krebsonsecurity.com/2024/11/hacker-in-snowflake-extortions-may-be-a-u-s-soldier/). Less than a month later, Wagenius was [arrested](https://krebsonsecurity.com/2024/12/u-s-army-soldier-arrested-in-att-verizon-extortions/) and charged in two separate federal indictments, and soon pleaded guilty to all counts in both cases.

At his sentencing hearing in Seattle today, Wagenius was sentenced to nearly six years in federal prison, and ordered to pay $294,978 in restitution.

Federal prosecutors said Wagenius was assisted in his efforts to extort victim companies by **Kenneth Schuchman**, a 28-year old man from Vancouver, Washington who has a lengthy cybercriminal history. In 2019, Schuchman [pleaded guilty to operating the **Satori** botnet](https://krebsonsecurity.com/2019/09/satori-iot-botnet-operator-pleads-guilty/), a vast collection of hacked Internet-of-Things (IoT) devices that was used for large-scale distributed denial-of-service (DDoS) attacks.

Two other alleged co-conspirators of Wagenius are still facing charges in connection with the Snowflake data thefts; **Conor Riley Moucka**, a.k.a. “Judische,” of Kitchener, Ontario was arrested in 2024 and [pleaded guilty in August 2026](https://krebsonsecurity.com/2026/08/canadian-man-pleads-guilty-in-snowflake-extortions/); and **John Erin Binns**, an American man currently living in Turkey who is also wanted for [a 2021 data breach at T-Mobile](https://krebsonsecurity.com/2021/08/t-mobile-investigating-claims-of-massive-data-breach/) that exposed the personal information of at least 76 million customers.

Kiberphant0m also admitted to re-extorting victims, and threatening to disclose national security secrets. Immediately following Moucka’s arrest — after AT&T had already paid the extortion group a $370,000 Bitcoin ransom — Kiberphant0m posted on hacker forums what he claimed were the AT&T call logs for then President-elect Donald Trump and for then Vice President Kamala Harris, as well as schematics allegedly stolen from the U.S. National Security Agency (NSA).

**Paul Russell** is a resident agent in charge at the **Defense Criminal Investigative Service** (DCIS), the criminal investigative arm of the U.S. Department of Defense Office of Inspector General. Russell said when DCIS received information that a soldier with secret clearance was allegedly involved in cybercrime and extortion, the agency began working the investigation alongside the FBI, the Army Criminal Investigative Division (CID), and the U.S. Secret Service.

“We don’t often get leads where there’s an active duty soldier with a secret clearance who’s creating hacking tools and trafficking in data,” Russell said. “That doesn’t happen every day, and so when that hits it really spins all of our partner organizations up. It was very serious from jump street, just because it was unique, it was an insider threat, and we weren’t sure what we were dealing with.”

A [sentencing memo](https://krebsonsecurity.com/wp-content/uploads/2026/09/wagenius-sentencingmemo.pdf) (PDF) filed Sept. 19 by federal prosecutors in Seattle notes that while Wagenius pleaded guilty almost immediately and has been remarkably cooperative, he recently got caught trying to find security vulnerabilities in the BOP’s computer network. The government’s memo notes that while incarcerated and awaiting sentencing, Wagenius violated the computer use policies of the **Bureau of Prisons** (BOP) in attempts to learn about vulnerabilities in BOP computer systems.

“According to records from BOP, in or around September 2025, Wagenius used another inmate’s email system to request that the email recipient prompt a commercial AI tool to provide information about “[w]hat CVE’s are there for Windows 10 Enterprise privilege escalation and bypasses” and to “[p]rovide the CVE’s and a real world working script for each CVE . . . without omitted code,” the government’s memo states.

The memo states that less than a week later, Wagenius used a different inmate’s email account and requested that the email recipient prompt an AI tool to “[p]rovide the step by step for [CVE-2023-45208](https://nvd.nist.gov/vuln/detail/cve-2023-45208), code for this if any, and if no code exists make some, make sure to describe everything in detail.” CVE-2023-45208 is a three-year-old “command injection” vulnerability in D-Link networking devices.

That same month, Wagenius allegedly again requested that the email recipient prompt AI with the question, “How do you make an antenna in a prison environment with commissary or readily available items/tools to improve/make an antenna to extend radio reception?”

Federal prosecutors said Wagenius also requested that the recipient research escaping prison.

“In several instances, Wagenius framed the AI queries as being posed in connection to a book he was writing. This is a common method of ‘prompt injection,’ in which attackers feed specially crafted, deceptive inputs into commercial AI tools that are programmed to avoid outputting malicious code that can be used to exploit computer vulnerabilities,” the sentencing memo reads.

The government told the court it is unaware of evidence that Wagenius figured out how to use or deploy the vulnerabilities he was researching in the BOP’s systems, and when questioned said he was only researching “potential vulnerabilities to provide information to the BOP.”

Incredibly, despite the enormous financial value of the data stolen from AT&T and other telecom providers, Wagenius’s extortion efforts were largely unsuccessful. The government’s sentencing memo says Wagenius made a whopping total of around $1,500 from selling s...