---
title: LastPass breach update: The few additional bits of information
url: https://palant.info/2023/02/28/lastpass-breach-update-the-few-additional-bits-of-information/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:51.143533
---

# LastPass breach update: The few additional bits of information

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# LastPass breach update: The few additional bits of information

2023-02-28
 [Lastpass](/categories/lastpass/)/[Security](/categories/security/)/[Password-Managers](/categories/password-managers/)
 8 mins
 [3 comments](/2023/02/28/lastpass-breach-update-the-few-additional-bits-of-information/#comments)

Half a year after the LastPass breach started in August 2022, information on it remains sparse. It took until December 2022 for LastPass to admit losing their usersâ partially encrypted vault data. This statement was [highly misleading](/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/), e.g. making wrong claims about the protection level provided by the encryption. Some of the failures to protect users only became apparent after some time, such as [many accounts configured with a dangerously low password iterations setting](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/), the company hasnât admitted them to this day.

![Screenshot of an email with the LastPass logo. The text: Dear LastPass Customer,â¯We recently notified you that an unauthorized party was able to gain access to a third-party cloud-based storage service which is used by LastPass to store backups. Earlier today, we posted an update to our blog with important information about our ongoing investigation. This update includes details regarding our findings to date, recommended actions for our customers, as well as the actions we are currently taking.](/2023/02/28/lastpass-breach-update-the-few-additional-bits-of-information/email.png)

Despite many questions being raised, LastPass maintained strict radio silence since December. Until yesterday they published [an article with details of the breach](https://support.lastpass.com/help/incident-2-additional-details-of-the-attack). If you were hoping to get answers: nope. If you look closely, the article again carefully avoids making definitive statements. There is very little to learn here.

TL;DR: The breach was helped by a lax security policy, an employee was accessing critical company data from their home computer. Also, contrary to what LastPass claimed originally, business customers using Federated Login Services are very much affected by this breach. In fact, the attackers might be able to decrypt company data without using any computing resources on bruteforcing master passwords.

**Update** (2023-02-28): I found additional information finally explaining the timeline here. So the breach affects LastPass users who had an active LastPass account between August 20 and September 16, 2022. The âTimeline of the breachâ section has been rewritten accordingly.

#### Contents

* [The compromised senior DevOps engineer](#the-compromised-senior-devops-engineer)
* [Timeline of the breach](#timeline-of-the-breach)
* [Bad news for business customers](#bad-news-for-business-customers)
* [Any security improvements?](#any-security-improvements)

## The compromised senior DevOps engineer

According to LastPass, only four DevOps engineers had access to the keys required to download and decrypt LastPass backup data from Amazon Web Services (AWS). These keys were stored in the LastPassâ own corporate LastPass vault, with only these four people having access.

The attackers learned about that when they initially compromised LastPass in August 2022. So they specifically targeted one of these DevOps engineers and infected their home computer with a keylogger. Once this engineer used their home computer to log into the corporate LastPass vault, the attackers were able to access all the data.

While LastPass makes it sound like the employeeâs fault, one has to ask: what kind of security policies allowed an employee to access highly critical company assets from their home computer? Was this kind of access sanctioned by the company? And if yes, e.g. as part of the Bring Your Own Device (BYOD) policy â what kind of security measures were in place to prevent compromise?

Also, in another transparent attempt to shift blame LastPass mentions a vulnerability in a third-party media software which was supposedly used for this compromise. LastPass does not mention either the software or the vulnerability, yet I highly doubt that the attackers burned a zero-day vulnerability. LastPass would certainly mention it if they did, as it supports their case of being overrun by highly sophisticated attackers.

However, [Ars Technica quotes an anonymous source](https://arstechnica.com/information-technology/2023/02/lastpass-hackers-infected-employees-home-computer-and-stole-corporate-vault/) claiming that the software in question was Plex media server. Plex has two known vulnerabilities potentially allowing remote code execution: CVE-2019-19141 and CVE-2018-13415. The former is unlikely to have been exploited because it requires an authenticated attacker, which leaves us with a vulnerability from 2018.

And that certainly explains why LastPass wouldnât mention the specific vulnerability used. Yes, allowing an employee to access company secrets from a computer where they also run an at least four years old Plex version that is directly accessible from the internet â thatâs pretty damning.

**Update** (2023-03-02): Dan Goodin, the journalist behind the article above, [got a definitive statement from LastPass confirming my speculations](https://infosec.exchange/%40dangoodin/109950447675626971):

> We can confirm that the engineer was running an earlier, unpatched version of Plex Media Server on the engineerâs home computer. This was not a zero-day attack.

**Update** (2023-03-05): [According to PCMag](https://www.pcmag.com/news/lastpass-employee-couldve-prevented-hack-with-a-software-update), Plex learned that the vulnerability abused here was actually [CVE-2020-5741](https://forums.plex.tv/t/security-regarding-cve-2020-5741/586819) from 2020. That would mean that the attackers already had admin access to the media server. How they gained admin access is unknown.

## Timeline of the breach

Other than that, we learn fairly little from the LastPass statement. In particular, this doesnât really help understand the timeline:

> the threat actor [â¦] was actively engaged in a new series of reconnaissance, enumeration, and exfiltration activities aligned to the cloud storage environment spanning from August 12, 2022 to October 26, 2022.

As it turns out, [another recently published document](https://support.lastpass.com/help/what-data-was-accessed) is more specific:

> The threat actor was able to copy five of the Binary Large Objects (BLOBs) database shards that were dated: August 20, 2022, August 30, 2022, August 31, 2022, September 8, 2022, and September 16, 2022. This took place between September 8 - 22, 2022. LastPass accounts created after these dates are not affected.

So in the initial breach in August 2022 the attackers compromised an employeeâs company laptop to steal some source code and internal information. They used the information to compromise the aforementioned senior DevOps engineerâs home computer. This way they gained access to LastPassâ backup storage, and between September 8 and 22 theyâve been copying data.

And we finally know which users are affected: the ones who had active LastPass accounts between August 20 and September 16, 2022. Anyone who deleted their account before that time span or created their account after it isnât affected.

Thatâs finally something specific. Too bad that it took almost half a year to get there.

## Bad news for business customers

Back in December, LastPass had good news for business customers:

> The threat actor did not have access to the key fragments stored in customer Identity Providerâs or LastPassâ infrastructure and they were not included in the backups that were copied that contained customer vaults. Therefore, i...