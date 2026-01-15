---
title: Microsoft disrupts RedVDS cybercrime platform behind $40 million in scam losses
url: https://therecord.media/microsoft-redvds-cybercrime-scam
source: Over Security - Cybersecurity news aggregator
date: 2026-01-14
fetch_date: 2026-01-15T03:31:49.533858
---

# Microsoft disrupts RedVDS cybercrime platform behind $40 million in scam losses

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![Padlock](https://cms.therecord.media/uploads/format_webp/large_Padlock_2_0f56155777.jpg)

Credit: Planet Volumes / Unsplash

[Jonathan Greig](/author/jonathan-greig)January 14th, 2026

# Microsoft disrupts RedVDS cybercrime platform behind $40 million in scam losses

A popular cybercriminal subscription service called RedVDS was taken down by Microsoft after the platform was used to enable more than $40 million in fraud losses in the United States alone.

RedVDS provided cybercriminals with disposable virtual computers that make fraud cheap, scalable and difficult to trace, according to Microsoft assistant general counsel Steven Masada.

Microsoft filed lawsuits in the U.S. and United Kingdom as part of a broader international law enforcement operation alongside Europol and German authorities.

The company worked with law enforcement to seize two domains that host the RedVDS marketplace and customer portal while also taking steps to identify the people behind the scheme. No suspects were publicly named.

German state criminal police seized a server used to power RedVDS, taking the marketplace offline.

“RedVDS is an online subscription service that is part of the growing cybercrime-as-a-service ecosystem where cybercriminals buy and sell services and tools to launch attacks at scale,” Masada said. “It provides access to cheap, effective, and disposable virtual computers running unlicensed software, including Windows, allowing criminals to operate quickly, anonymously, and across borders.”

Cybercriminals could pay just $24 per month for access to the platform and used it to send phishing emails, host scam infrastructure, and more. RedVDS has existed since 2019 and has been operating publicly through a fake company allegedly based in the Bahamas. Most customers purchased the site’s services with Bitcoin and other cryptocurrency.

Masada explained that in a single month, Microsoft saw more than 2,600 distinct RedVDS virtual machines send an average of one million phishing messages per day to Microsoft customers.

Most of the messages were blocked but a small amount likely reached their targets’ inbox, and since September RedVDS‑enabled attacks “have led to the compromise or fraudulent access of more than 191,000 Microsoft email accounts across over 130,000 organizations worldwide,” he added.

Microsoft filed civil actions to take the platforms down alongside two co‑plaintiffs: H2 Pharma, an Alabama-based pharmaceutical company, and Gatehouse Dock Condominium Association in Florida.

H2 Pharma saw cybercriminals use RedVDS to steal more than $7.3 million, while the condo association lost about $500,000 of funds contributed by residents and property owners for repairs.

## Real estate scams

Cybercriminals typically used RedVDS for payment diversion fraud, also known as business email compromise. The platform allowed threat actors to break into email accounts, monitor conversations and insert themselves into email chains in advance of payments or wire transfers.

By impersonating other actors in the email chain, hackers are able to divert funds in seconds, long before organizations realized money has been sent to the wrong place.

Masada noted that RedVDS has been a key player in the spread of real estate payment diversion scams — an issue [recently spotlighted by the Justice Department](https://therecord.media/nigeria-national-twenty-million-scams).

Cybercriminals are increasingly targeting realtors, escrow agents, or title companies, stealing millions of dollars sent by people who think they are putting down payments on homes.

“For families and first‑time homebuyers, the consequences can be devastating, with a single diverted payment wiping out life savings or derailing a home purchase altogether,” Masada said.

“Microsoft has observed RedVDS‑enabled activity affecting more than 9,000 customers in the real estate sector alone, with particularly severe impact in countries such as Canada and Australia. And the threat goes far beyond real estate. RedVDS‑enabled scams have hit construction, manufacturing, healthcare, logistics, education, legal services, and many other sectors — disrupting everything from production lines to patient care.”

Microsoft observed cybercriminals sending fake invoices or emails demanding payment account changes and using urgency to force victims into sending money as quickly as possible. In some cases they sent fake unpaid invoices demanding same-day debt payments.

RedVDS did not own physical data centers and instead rented servers from third-party hosting providers in the U.S., Canada, U.K., France and the Netherlands. This enabled cybercriminals to attack victims from IP addresses in locations close to their targets, allowing them to get around geolocation-based security filters.

Europol also assisted in disrupting a broader network of servers and payment networks that supported RedVDS customers.

## ‘Ready-made’

Microsoft said RedVDS was  a way for cybercriminals to get access to Windows-based Remote Desktop Protocol (RDP) servers with full administrator control and no usage limits.

The company eventually traced thousands of stolen credentials, invoices stolen from target organizations, mass mailers, and phish kits back to the platform.

The cybercriminals used several different tools to validate large databases of email addresses, sort and clean the email lists, and send bulk emails, all through RedVDS instances, and they used privacy-focused web browsers and VPNs to conceal their identities.

Some users deployed ChatGPT and other OpenAI tools to write convincing emails in English.

“Once provisioned, these cloned Windows hosts gave actors a ready‑made platform to research targets, stage phishing infrastructure, steal credentials, hijack mailboxes, and execute impersonation‑based financial fraud with minimal friction,” the researchers explained.

“Threat actors benefited from RedVDS’s unrestricted administrative access and negligible logging, allowing them to operate without meaningful oversight. The uniform, disposable nature of RedVDS servers allowed cybercriminals to rapidly iterate campaigns, automate delivery at scale, and move quickly from initial targeting to financial theft.”

Other platforms tied to RedVDS generate PDF or HTML lure attachments, automate email sending cycles and create phishing domains made to look like legitimate websites.

Over 30 days, Microsoft saw more than 7,300 IP addresses linked to RedVDS infrastructure that collectively hosted more than 3,700 domains made to impersonate legitimate platforms.

When victims entered their credentials into the websites, RedVDS facilitated the extraction of tokens or cookies, allowing cybercriminals to get around multifactor authentication.

Using the stolen information, users logged into mailboxes and searched for any conversations involving finances, invoices or suppliers.

Microsoft said this was the 35th civil action the company has taken to shut down cybercriminal infrastructure. In the fall of 2025, it took similar action to take down a popular service [called RaccoonO365](https://therecord.media/microsoft-cloudflare-disrupt-raccoono365-credential-stealing-tool) that was used by cybercriminals to steal usernames and passwords. At least one man in Nigeria [was arrested](https://therecord.media/nigeria-raccoon-developer-tip) for running the RaccoonO365 platform.

Many of the cybercriminals Microsoft observed using RacoonO365 phishing se...