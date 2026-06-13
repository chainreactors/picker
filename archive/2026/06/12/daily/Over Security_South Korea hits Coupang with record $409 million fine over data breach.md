---
title: South Korea hits Coupang with record $409 million fine over data breach
url: https://therecord.media/south-korea-data-breach-record-fine-coupang
source: Over Security
date: 2026-06-12
fetch_date: 2026-06-13T06:11:48.434369
---

# South Korea hits Coupang with record $409 million fine over data breach

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

![digital](https://cms.therecord.media/uploads/large_digital_hack_computer_data_breach_f97e2f823d.jpg)

Image: Allison Saeng via Unsplash

[Alexander Martin](/author/alexander-martin)June 12th, 2026

# South Korea hits Coupang with record $409 million fine over data breach

South Korea's data protection regulator has imposed a record 624.7 billion won ($409 million) fine on Coupang, the country's largest online retailer, after an investigation into a data breach that compromised the personal information of tens of millions of customers.

The Personal Information Protection Commission (PIPC) voted at a plenary session on Wednesday to sanction Coupang and its logistics subsidiary, Coupang Fulfillment Services, concluding that the breach stemmed not from sophisticated hacking but from “deficiencies in basic safety management.”

The penalty is the largest ever issued by the commission for a personal data breach, surpassing the record 134.8 billion won ($88.8 million) fine levied against [SK Telecom](https://therecord.media/data-breach-costs-lead-to-profit-decline-south-korea-telecom) earlier this year.

The breach [first became public in November](https://therecord.media/coupang-south-korea-data-breach) when Coupang said approximately 33.7 million customer accounts had been compromised — equivalent to around 65% of South Korea's entire population.

The PIPC's investigation confirmed that 33,222,472 registered members were affected, but also identified a category of victims the company had not previously acknowledged: at least 4,338,368 non-members whose names, phone numbers and addresses had been stored as delivery recipients by other customers, and who had no way of knowing their data was held by Coupang at all.

The regulator said it had formally urged the company four times, in December 2025 and January 2026, to notify those non-member victims. Coupang failed to do so each time.

The perpetrator, an unnamed Chinese national and former employee who left the company at the end of 2024, had himself developed Coupang's alternative authentication system while still employed and had stolen the signing key that underpinned it before he left.

He began with a test run in January 2025, using the stolen key on 95 accounts. From April, he systematically cycled through member ID numbers, hitting Coupang's delivery address page approximately 148 million times over two months to harvest names, phone numbers and addresses.

He then turned to the account edit page, accessing it nearly 35 million times between June and October to collect names and email addresses. A final phase added apartment entry codes and order histories.

The former employee later reassembled the data into individual customer profiles and sent two extortion emails — to members directly, and to Coupang — the second claiming to hold 120 million addresses, 560 million order records and more than 33 million email addresses, with sample data that included sensitive purchase histories.

The PIPC found that throughout the seven-month attack, traffic on the affected pages had spiked to many times their normal levels, and that tens of millions of access attempts had used non-existent member IDs. Coupang detected none of it until a customer forwarded one of the extortion emails.

The commission referred Coupang for criminal prosecution over the destruction of evidence. Regulators had ordered the preservation of access logs on November 21 — the day after Coupang filed its initial breach report, but six days later, the company manually deleted approximately six months of web access logs.

Coupang also failed to pause its routine policy of automatically deleting logs after six months, allowing further records to be wiped. Roughly 13% of the logs covering the attack period were lost, making it impossible to identify all affected victims.

Police separately [recovered a smashed laptop](https://therecord.media/coupang-recovers-smashed-laptop-data-breach) from a river during the investigation — a MacBook Air the alleged perpetrator had weighted with bricks in an apparent attempt to destroy evidence — which forensic teams from Mandiant, Palo Alto Networks and Ernst & Young were able to document before it was handed to authorities.

## Additional violations uncovered

The investigation, expanded in January 2026 following parliamentary hearings and media coverage, unearthed several violations separate from the breach itself.

Through its “Coupang Partners” affiliate marketing program, the company had covertly collected the third-party browsing activity of about 11.2 million users — URLs visited, app names, timestamps, IP addresses and device identifiers — without consent, linking the data to individual member accounts.

Coupang argued the information did not constitute personal data; the regulator disagreed, noting it was stored alongside member ID numbers and device identifiers. The commission imposed a further 201.1 billion won ($132 million) fine for this violation alone. Coupang deleted the records in April 2026 after investigators confronted the company.

Some advertising partners in the same program had also been running so-called “hijack ads” — redirecting users to Coupang without their consent, in some cases by covering the screen with a transparent button so that clicking anywhere triggered a redirect.

Coupang had been aware of the practice since 2022 but had failed to terminate the accounts of partners who met its own threshold for removal, and had in some cases paid them higher commissions after they were caught, the investigation found.

Coupang Fulfillment Services, the logistics subsidiary, was also found to have secretly added 71 police press-corps journalists — none of whom had ever worked at a Coupang warehouse — to an internal employment blacklist, citing “spreading false information,” without their knowledge or consent.

The subsidiary was also found to have submitted employees' weight data, collected for health management purposes, as evidence in an industrial accident lawsuit, without a separate legal basis.

The commission additionally found that when Coupang conducted its own internal investigation of the hacker in December 2025 — [drawing criticism from lawmakers and government officials at the time](https://therecord.media/coupang-acting-CEO-questioned-police-investigating-data-breach) — it had excluded its own chief privacy officer from the process entirely. Regulators treated this not as an internal communication failure but as a substantive violation of the legally mandated independence of the chief privacy officer’s role.

Acting CEO Harold Rogers, who was questioned by police in January as a suspect in an obstruction inquiry, had pledged full cooperation with authorities. The company said it regretted the PIPC's decision and reserved the right to challenge it through legal proceedings once it receives the formal written ruling.

Dispute mediation proceedings covering more than 2,500 individual and group claimants, which had been paused during the investigation, are set to resume on June 12. A class-action lawsuit in the United States also remains pending.

Coupang's shares have fallen around 35% since the start of the year. The company has warned that revenue growth could slow, and faces ongoing scrutiny from South Korean lawmakers over both the breach and its response to it.

* [Cybercrime](/news/cybercrime)
* [Government](/news/government)
* [News](/)

Get more insights...