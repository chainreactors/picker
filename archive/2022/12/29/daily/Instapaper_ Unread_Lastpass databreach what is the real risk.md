---
title: Lastpass databreach what is the real risk
url: https://andreafortuna.org/2022/12/25/lastpass-databreach-what-is-the-real-risk
source: Instapaper: Unread
date: 2022-12-29
fetch_date: 2025-10-04T02:42:28.649561
---

# Lastpass databreach what is the real risk

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Lastpass databreach: what is the actual risk?

Dec 25, 2022

LastPass, a password management software used by over 33 million people and 100,000 businesses worldwide, has revealed that customer vault data was stolen after the company’s cloud storage was breached earlier this year.

## What happened?

The attacker gained access to the cloud storage using stolen “cloud storage access key and dual storage container decryption keys” and copied basic customer information, as well as customer vault data, which is stored in a proprietary binary format containing both unencrypted and encrypted data.

> The threat actor was also able to copy a backup of customer vault data from the encrypted storage container which is stored in a proprietary binary format that contains both unencrypted data, such as website URLs, as well as fully-encrypted sensitive fields such as website usernames and passwords, secure notes, and form-filled data.

![lastpass](https://media.licdn.com/dms/image/C5622AQH_JZ7gUrmINw/feedshare-shrink_1280/0/1671912165559?e=1674691200&v=beta&t=MHYj8ngkuYsr2CifRSRDnc9eXc1za_3bB7jtqY3lUk0)

The encrypted data can only be decrypted with a unique key derived from each user’s master password, which LastPass does not store or maintain.

> These encrypted fields remain secured with 256-bit AES encryption and can only be decrypted with a unique encryption key derived from each user’s master password using our Zero Knowledge architecture. As a reminder, the master password is never known to LastPass and is not stored or maintained by LastPass.
> ***The encryption and decryption of data is performed only on the local LastPass client.***

## What is the real risk?

According to [official press release](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/),

> The threat actor may attempt to use brute force to guess your master password and decrypt the copies of vault data they took. Because of the hashing and encryption methods we use to protect our customers, it would be extremely difficult to attempt to brute force guess master passwords for those customers who follow our password [best practices](https://support.lastpass.com/help/what-is-the-lastpass-master-password-lp070014). We routinely test the latest password cracking technologies against our algorithms to keep pace with and improve upon our cryptographic controls. *The threat actor may also target customers with phishing attacks, credential stuffing, or other brute force attacks against online accounts associated with your LastPass vault.*

This is the second security incident disclosed by LastPass this year, following a breach in August in which the company’s developer environment was accessed using a compromised developer account and proprietary technical information and source code were stolen.

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

## Andrea Fortuna

* Andrea Fortuna
* andrea@andreafortuna.org

* [andreafortuna](https://github.com/andreafortuna)
* [andreafortunaig](https://instagram.com/andreafortunaig)
* [andrea-fortuna](https://www.linkedin.com/in/andrea-fortuna)
* [andrea](https://social.privacytools.click/%40andrea)
* [andreafortunatw](https://www.twitter.com/andreafortunatw)

Cybersecurity expert, software developer, experienced digital forensic analyst, musician