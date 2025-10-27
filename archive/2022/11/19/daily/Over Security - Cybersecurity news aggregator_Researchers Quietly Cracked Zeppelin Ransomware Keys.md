---
title: Researchers Quietly Cracked Zeppelin Ransomware Keys
url: https://krebsonsecurity.com/2022/11/researchers-quietly-cracked-zeppelin-ransomware-keys/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-19
fetch_date: 2025-10-03T23:14:45.005537
---

# Researchers Quietly Cracked Zeppelin Ransomware Keys

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Researchers Quietly Cracked Zeppelin Ransomware Keys

November 17, 2022

[14 Comments](https://krebsonsecurity.com/2022/11/researchers-quietly-cracked-zeppelin-ransomware-keys/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2022/11/zeppransom.png)

Peter is an IT manager for a technology manufacturer that got hit with a Russian ransomware strain called “**Zeppelin**” in May 2020. He’d been on the job less than six months, and because of the way his predecessor architected things, the company’s data backups also were encrypted by Zeppelin. After two weeks of stalling their extortionists, Peter’s bosses were ready to capitulate and pay the ransom demand. Then came the unlikely call from an FBI agent. “Don’t pay,” the agent said. “We’ve found someone who can crack the encryption.”

Peter, who spoke candidly about the attack on condition of anonymity, said the FBI told him to contact a cybersecurity consulting firm in New Jersey called [Unit 221B](https://www.unit221b.com), and specifically its founder — **Lance James**. Zeppelin [sprang onto the crimeware scene in December 2019](https://blogs.blackberry.com/en/2019/12/zeppelin-russian-ransomware-targets-high-profile-users-in-the-us-and-europe), but it wasn’t long before James discovered multiple vulnerabilities in the malware’s encryption routines that allowed him to brute-force the decryption keys in a matter of hours, using nearly 100 cloud computer servers.

In an interview with KrebsOnSecurity, James said Unit 221B was wary of advertising its ability to crack Zeppelin ransomware keys because it didn’t want to tip its hand to Zeppelin’s creators, who were likely to modify their file encryption approach if they detected it was somehow being bypassed.

This is not an idle concern. There are multiple examples of ransomware groups doing just that after security researchers crowed about finding vulnerabilities in their ransomware code.

“The minute you announce you’ve got a decryptor for some ransomware, they change up the code,” James said.

But he said the Zeppelin group appears to have stopped spreading their ransomware code gradually over the past year, possibly because Unit 221B’s referrals from the FBI let them quietly help nearly two dozen victim organizations recover without paying their extortionists.

In a blog post published today to coincide with [a Black Hat talk](https://blackhatmea.com/node/727) on their discoveries, James and co-author **Joel Lathrop** said they were motivated to crack Zeppelin after the ransomware gang started attacking nonprofit and charity organizations.

“What motivated us the most during the leadup to our action was the targeting of homeless shelters, nonprofits and charity organizations,” the two wrote. “These senseless acts of targeting those who are unable to respond are the motivation for this research, analysis, tools, and blog post. A general Unit 221B rule of thumb around our offices is: Don’t [REDACTED] with the homeless or sick! It will simply trigger our ADHD and we will get into that hyper-focus mode that is good if you’re a good guy, but not so great if you are an \*\*\*hole.”

The researchers said their break came when they understood that while Zeppelin used three different types of encryption keys to encrypt files, they could undo the whole scheme by factoring or computing just one of them: An ephemeral RSA-512 public key that is randomly generated on each machine it infects.

“If we can recover the RSA-512 Public Key from the registry, we can crack it and get the 256-bit AES Key that encrypts the files!” they wrote. “The challenge was that they delete the [public key] once the files are fully encrypted. Memory analysis gave us about a 5-minute window after files were encrypted to retrieve this public key.”

Unit 221B ultimately built a “Live CD” version of Linux that victims could run on infected systems to extract that RSA-512 key. From there, they would load the keys into a cluster of 800 CPUs donated by hosting giant **Digital Ocean** that would then start cracking them. The company also used that same donated infrastructure to help victims decrypt their data using the recovered keys.

![](https://krebsonsecurity.com/wp-content/uploads/2022/11/zeppelin-note.png)

Jon is another grateful Zeppelin ransomware victim who was aided by Unit 221B’s decryption efforts. Like Peter, Jon asked that his last name and that of his employer be omitted from the story, but he’s in charge of IT for a mid-sized managed service provider that got hit with Zeppelin in July 2020.

The attackers that savaged Jon’s company managed to phish credentials and a multi-factor authentication token for some tools the company used to support customers, and in short order they’d seized control over the servers and backups for a healthcare provider customer.

Jon said his company was reluctant to pay a ransom in part because it wasn’t clear from the hackers’ demands whether the ransom amount they demanded would provide a key to unlock all systems, and that it would do so safely.

“They want you to unlock your data with their software, but you can’t trust that,” Jon said. “You want to use your own software or someone else who’s trusted to do it.”

In August 2022, the FBI and the Cybersecurity & Infrastructure Security Agency (CISA) [issued a joint warning on Zeppelin](https://www.cisa.gov/uscert/ncas/alerts/aa22-223a), saying the FBI had “observed instances where Zeppelin actors executed their malware multiple times within a victim’s network, resulting in the creation of different IDs or file extensions, for each instance of an attack; this results in the victim needing several unique decryption keys.”

The advisory says Zeppelin has attacked “a range of businesses and critical infrastructure organizations, including defense contractors, educational institutions, manufacturers, technology companies, and especially organizations in the healthcare and medical industries. Zeppelin actors have been known to request ransom payments in Bitcoin, with initial amounts ranging from several thousand dollars to over a million dollars.”

The FBI and CISA say the Zeppelin actors gain access to victim networks by exploiting weak Remote Desktop Protocol (RDP) credentials, exploiting SonicWall firewall vulnerabilities, and phishing campaigns. Prior to deploying Zeppelin ransomware, actors spend one to two weeks mapping or enumerating the victim network to identify data enclaves, including cloud storage and network backups, the alert notes.

Jon said he felt so lucky after connecting with James and hearing about their decryption work, that he toyed with the idea of buying a lottery ticket that day.

“This just doesn’t usually happen,” Jon said. “It’s 100 percent like winning the lottery.”

By the time Jon’s company got around to decrypting their data, they were forced by regulators to prove that no patient data had been exfiltrated from their systems. All told, it took his employer two months to fully recover from the attack.

“I definitely feel like I was ill-prepared for this attack,” Jon said. “One of the things I’ve learned from this is the importance of forming your core team and having those people wh...