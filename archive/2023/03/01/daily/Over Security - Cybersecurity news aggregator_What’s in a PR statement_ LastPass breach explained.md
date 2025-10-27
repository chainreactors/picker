---
title: What’s in a PR statement: LastPass breach explained
url: https://palant.info/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:53.547216
---

# What’s in a PR statement: LastPass breach explained

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Whatâs in a PR statement: LastPass breach explained

2022-12-26
 [Lastpass](/categories/lastpass/)/[Security](/categories/security/)/[Password-Managers](/categories/password-managers/)
 10 mins
 [72 comments](/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/#comments)

Right before the holiday season, LastPass published an [update on their breach](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/). As people have speculated, this timing was likely not coincidental but rather intentional to keep the news coverage low. Security professionals werenât amused, this holiday season became a very busy time for them. LastPass likely could have prevented this if they were more concerned about keeping their users secure than about saving their face.

Their statement is also full of omissions, half-truths and outright lies. As I know that not everyone can see through all of it, I thought that I would pick out a bunch of sentences from this statement and give some context that LastPass didnât want to mention.

![Screenshot of the LastPass blog post: Update as of Thursday, December 22, 2022.Â To Our LastPass Community,â¯We recently notified you that an unauthorized party gained access to a third-party cloud-based storage service, which LastPass uses to store archived backups of our production data. In keeping with our commitment to transparency, we want to provide you with an update regarding our ongoing investigation.](/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/statement.png)

Letâs start with the very first paragraph:

> In keeping with our commitment to transparency, we want to provide you with an update regarding our ongoing investigation.

In fact, this has little to do with any commitment. LastPass is actually required by US law to immediately disclose a data breach. Weâll soon see how transparent they really are in their statement.

> While no customer data was accessed during the August 2022 incident, some source code and technical information were stolen from our development environment and used to target another employee, obtaining credentials and keys which were used to access and decrypt some storage volumes within the cloud-based storage service.

LastPass is trying to present the August 2022 incident and the data leak now as two separate events. But using information gained in the initial access in order to access more assets is actually a typical technique used by threat actors. It is called lateral movement.

So the more correct interpretation of events is: we do not have a new breach now, LastPass rather failed to contain the August 2022 breach. And because of that failure peopleâs data is now gone. Yes, this interpretation is far less favorable of LastPass, which is why they likely try to avoid it.

Note also how LastPass avoids mentioning when this âtarget another employeeâ happened. It likely did already before they declared victory in September 2022, which also sheds a bad light on them.

> The cloud storage service accessed by the threat actor is physically separate from our production environment.

Is that supposed to be reassuring, considering that the cloud storage in question apparently had a copy of all the LastPass data? Or is this maybe an attempt to shift the blame: âIt wasnât our servers that the data has been lifted fromâ?

> To date, we have determined that once the cloud storage access key and dual storage container decryption keys were obtained, the threat actor copied information from backup that contained basic customer account information and related metadata including company names, end-user names, billing addresses, email addresses, telephone numbers, and the IP addresses from which customers were accessing the LastPass service.

We learn here that LastPass was storing your IP addresses. And since they donât state how many they were storing, we have to assume: all of them. And if you are an active LastPass user, that data should be good enough to create a complete movement profile. Which is now in the hands of an unknown threat actor.

Of course, LastPass doesnât mention this implication, hoping that the less tech-savvy users wonât realize.

There is another interesting aspect here: how long did it take to copy the data for millions of users? Why didnât LastPass detect this *before* the attackers were done with it? We wonât learn that in their statement.

> The threat actor was also able to copy a backup of customer vault data from the encrypted storage container which is stored in a proprietary binary format that contains both unencrypted data, such as website URLs, as well as fully-encrypted sensitive fields such as website usernames and passwords, secure notes, and form-filled data.

Note how LastPass admits not encrypting website URLs but doesnât group it under âsensitive fields.â But website URLs are very much sensitive data. Threat actors would *love* to know what you have access to. Then they could produce well-targeted phishing emails just for the people who are worth their effort.

Never mind the fact that some of these URLs have parameters attached to them. For example, LastPass will sometimes save password reset URLs. And occasionally they will still be valid. Oopsâ¦

None of this is new of course. LastPass has been warned again and again that not encrypting URLs and metadata is a very bad idea. In [November 2015](https://www.blackhat.com/docs/eu-15/materials/eu-15-Vigo-Even-The-Lastpass-Will-Be-Stolen-deal-with-it.pdf) (page 67). In [January 2017](https://hackernoon.com/psa-lastpass-does-not-encrypt-everything-in-your-vault-8722d69b2032). In [July 2018](/2018/07/09/is-your-lastpass-data-really-safe-in-the-encrypted-online-vault/#the-encrypted-vault-myth). And thatâs only the instances I am aware of. They chose to ignore the issue, and they continue to downplay it.

> These encrypted fields remain secured with 256-bit AES encryption and can only be decrypted with a unique encryption key derived from each userâs master password using our Zero Knowledge architecture.

Lots of buzzwords here. 256-bit AES encryption, unique encryption key, Zero Knowledge architecture, all that sounds very reassuring. It masks over a simple fact: the only thing preventing the threat actors from decrypting your data is your master password. If they are able to guess it, the game is over.

> As a reminder, the master password is never known to LastPass and is not stored or maintained by LastPass.

Unless they (or someone compromising their servers) decide to store it. Because they absolutely could, and you wouldnât even notice. E.g. when you enter your master password into the login form on their web page.

But itâs not just that. Even if you use their browser extension consistently, it will [fall back to their website for a number of actions](/2019/03/18/should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server/). And when it does so, it will give the website your encryption key. For you, itâs impossible to tell whether this encryption key is subsequently stored somewhere.

None of this is news to LastPass. Itâs a risk they repeatedly chose to ignore. And that they keep negating in their official communication.

> Because of the hashing and encryption methods we use to protect our customers, it would be extremely difficult to attempt to brute force guess master passwords for those customers who follow our password best practices.

This prepares the ground for blaming the customers. LastPass should be aware that passwords *will* be decrypted for at least some of their customers. And they have a convenient explanation already: these customers clearly didnât follow their best practices.

Weâll see below what these best practices are and how LastPass is actually enforcing them.

> ...