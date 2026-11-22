---
title: CTO of ‘RansomwareHelp’ Indicted for Wire Fraud
url: https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/
source: Over Security
date: 2026-11-21
fetch_date: 2026-11-22T09:02:46.658238
---

# CTO of ‘RansomwareHelp’ Indicted for Wire Fraud

Advertisement

[![](/b-spycloud/1.png)](https://spycloud.com/check-your-exposure/?utm_medium=paid-ads&utm_source=third-party&utm_term=banner&utm_campaign=ads-cye-krebs-2026&cid=701UM00000o23RgYAI)

Advertisement

[![](/b-spycloud/2.png)](https://spycloud.com/check-your-exposure/?utm_medium=paid-ads&utm_source=third-party&utm_term=banner&utm_campaign=ads-cye-krebs-2026&cid=701UM00000o23RgYAI)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# CTO of ‘RansomwareHelp’ Indicted for Wire Fraud

November 20, 2026

[7 Comments](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/#comments)

The chief technology officer and co-founder of **ransomwarehelp.com**, a six year old Florida business that claimed to use “advanced cryptographic tools” to restore data locked by ransomware, has been charged with wire fraud after an FBI sting operation found the company was simply paying the attackers for a decryption key and charging victims a markup for work that was never performed.

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/ransomwarehelp.png)

A portion of the now-defunct website ransomwarehelp.com.

The website RansomwareHelp urged victims “Do not pay the ransom!,” claiming its advanced cryptographic tools could restore 100 percent of data, servers, and systems to their original format, and that there was no need to give in to extortion demands.

“Our cryptography experts use proprietary tools and algorithms to achieve 100% data recovery, all backed by a success rate of over 99%,” the website enthused, claiming the company had over 28 years of experience and a team of 80 experts in cryptography, cybersecurity, forensic analysis and reverse engineering. “We never promote, intermediate or pay ransom to threat actors on behalf of our clients.”

But according to [an indictment](https://krebsonsecurity.com/wp-content/uploads/2026/11/palacio.pdf) (PDF) returned this week in Rhode Island, the company’s co-founder — 52-year-old **Juan Ricardo Palacio Escobar** of Miami and Medellin, Colombia — routinely paid ransomware groups for a decryption key to unlock victim data, and then charged those victims well above what he’d secretly paid the threat actors [Palacio’s indictment was reported earlier this week by [404 Media](https://www.404media.co/ransomware-fraud-attack-fbi-indictment/), but for some reason that story did not name the defendant’s company].

The indictment says the FBI set up a sting operation in which the feds were posing both as a ransomware victim company and as a fictitious ransomware group. Pretending to be victims of a cyberattack, investigators contacted RansomwareHelp and supplied the company with a copy of a phony ransomware note, saying they did not wish to pay a ransom. RansomwareHelp replied by reiterating its policy against negotiating with or making ransom payments to threat actors.

The government said Palacio soon after contacted the fake ransomware group run by the FBI and requested the lowest possible price for the decryptor. FBI investigators responded with a price of .2 bitcoin, or around $13,000 at the time. Less than 48 hours later, Palacio allegedly told agents acting as the victim company that the diagnostic assessment was successful and that the cost of decrypting the files would be $13,260.

The following day, the government alleges, Palacio messaged the fictitious ransomware group operated by the feds and asked to reduce the ransom demand to $4,000 for the purchase of a decryption tool. The indictment states that the agreed upon price was around $6,000 in bitcoin, and that Palacio charged the FBI’s fake victim firm $16,010, including an initial $2,750 diagnostic fee and the full fee of $13,260.

**Paul Ihme** is co-founder of the security firm **Soteria**. Ihme told KrebsOnSecurity that in 2024 he heard from a small accounting firm that had paid RansomwareHelp a diagnostic fee to help recover from a Lockbit ransomware infection that had locked all of their company and client data.

Ihme said RansomwareHelp sent a proposal to the victim with a recovery price of $438,880, which it claimed included “professional configuration of forensic servers,” “expert engineering hours of programming to configure decryption algorithms,” and “eight (6-hour processing cycles) related to the decryption process.”

[![](https://krebsonsecurity.com/wp-content/uploads/2026/11/ransomwarehelpproposal.png)](https://krebsonsecurity.com/wp-content/uploads/2026/11/ransomwarehelpproposal.png)

A portion of the proposal that RansomwareHelp sent to a victim accounting firm in March 2024. Click to enlarge.

The proposal stated that the recovery process involved reverse engineering the ransomware encryption using “510 preconfigured forensic servers of the maximum quantitative capacity located in different parts of the world.”

“Our programmers will inject randomly the encryption codes extracted during the forensic and cryptographic analysis using brute force processes,” the proposal claimed.

Ihme said RansomwareHelp insisted that they be allowed unrestricted remote access into the victim’s network to run their diagnostic checks and analyses, using an Anydesk remote desktop software installer. Ihme believes RansomwareHelp insisted on that remote access in part so that the company could delete all copies of the ransomware notes left by the attackers on the victim’s network.

A typical ransomware note is a plain text file that introduces the ransomware group and lays out their demands, and it includes a way to contact them — often an email address or a live chat session on a darknet website. In most cases, the attackers will leave a copy of the ransom note on every system on the victim network that gets locked.

But Ihme said a review of the company’s network at the time found only one copy of the ransom note, which was unearthed from a backup snapshot on one of the infected computers. When they connected to the Lockbit chat server with the provided user ID, they discovered that someone had already been negotiating with the Lockbit extortionists for several days.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/11/lockbit-ransomwarehelp1.png)](https://krebsonsecurity.com/wp-content/uploads/2026/11/lockbit-ransomwarehelp1.png)

A screenshot of a 2024 conversation between Lockbit and RansomwareHelp, which was secretly negotiating with the extortion group. Click to enlarge.

“The charitable view would be to say that they were using Anydesk so they could grab the stuff they needed without having to walk the client through downloading and uploading a bunch of stuff,” Ihme said. “A legitimate firm would say, ‘Hey, send us a copy of the ransom note,’ which will have a link or URL to go to and chat with the threat actors. What they were doing is using that access to delete ransomware notes off the systems. The only reason they would do that is to prevent the victim from jumping into that chat itself.”

Indeed, RansomwareHelp pleaded with the Lockbit group throughout the chat not to reveal to the victim that they were negotiating. However, Lockbit quickly grew annoyed with the length of the negotiations, replying that the victims had waited too long and that the ransom demand would increase by $100,000 for every day they dithered further.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/11/lockbit-ransomwarehelp2.png)](https://krebsonsecurity.com/wp-content/uploads/2026/11/lockbit-ransomwarehelp2.png)

The Lockbit representative starts raising the ransom demand after multiple negotiators begin interacting with the threat actors. Click to enlarge.

In the end, the accounting firm took Ihme’s advice and went with a m...