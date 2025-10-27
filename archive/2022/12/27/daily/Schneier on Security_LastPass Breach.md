---
title: LastPass Breach
url: https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html
source: Schneier on Security
date: 2022-12-27
fetch_date: 2025-10-04T02:33:34.602509
---

# LastPass Breach

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## LastPass Breach

Last August, LastPass [reported](https://www.schneier.com/blog/archives/2022/12/lastpass-security-breach.html) a security breach, saying that no customer information—or passwords—were compromised. Turns out the full story [is worse](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/):

> While no customer data was accessed during the August 2022 incident, some source code and technical information were stolen from our development environment and used to target another employee, obtaining credentials and keys which were used to access and decrypt some storage volumes within the cloud-based storage service.
>
> […]
>
> To date, we have determined that once the cloud storage access key and dual storage container decryption keys were obtained, the threat actor copied information from backup that contained basic customer account information and related metadata including company names, end-user names, billing addresses, email addresses, telephone numbers, and the IP addresses from which customers were accessing the LastPass service.
>
> The threat actor was also able to copy a backup of customer vault data from the encrypted storage container which is stored in a proprietary binary format that contains both unencrypted data, such as website URLs, as well as fully-encrypted sensitive fields such as website usernames and passwords, secure notes, and form-filled data.

That’s bad. It’s not an epic disaster, though.

> These encrypted fields remain secured with 256-bit AES encryption and can only be decrypted with a unique encryption key derived from each user’s master password using our Zero Knowledge architecture. As a reminder, the master password is never known to LastPass and is not stored or maintained by LastPass.

So, according to the company, if you chose a strong master password—here’s [my advice](https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html) on how to do it—your passwords are safe. That is, you are secure as long as your password is resilient to a brute-force attack. (That they lost customer data is another story….)

Fair enough, as far as it goes. My guess is that many LastPass users do *not* have strong master passwords, even though the compromise of your encrypted password file should be part of your threat model. But, even so, note [this](https://twitter.com/cryptopathic/status/1606416137771782151?s=46&t=OZ7adijGdDvE7lUyGPBaJQ) unverified tweet:

> I think the situation at @LastPass may be worse than they are letting on. On Sunday the 18th, four of my wallets were compromised. The losses are not significant. Their seeds were kept, encrypted, in my lastpass vault, behind a 16 character password using all character types.

If that’s true, it means that LastPass has some backdoor—possibly unintentional—into the password databases that the hackers are accessing. (Or that @Cryptopathic’s “16 character password using all character types” is something like “P@ssw0rdP@ssw0rd.”)

My guess is that we’ll learn more during the coming days. But this should serve as a cautionary tale for anyone who is using the cloud: the cloud is another name for “someone else’s computer,” and you need to understand how much or how little you trust that computer.

If you’re changing password managers, look at my own [Password Safe](https://www.schneier.com/academic/passsafe/). Its main downside is that you can’t synch between devices, but that’s because I don’t use the cloud for anything.

[News](https://www.bleepingcomputer.com/news/security/lastpass-hackers-stole-customer-vault-data-in-cloud-storage-breach/) [articles](https://arstechnica.com/information-technology/2022/12/lastpass-says-hackers-have-obtained-vault-data-and-a-wealth-of-customer-info/). Slashdot [thread](https://hardware.slashdot.org/story/22/12/22/2345231/lastpass-hackers-stole-customer-vault-data-in-cloud-storage-breach).

EDITED TO ADD: People choose [lousy master passwords](https://mastodon.social/%40MildlyAggrievedScientist/109570065394823161).

Tags: [breaches](https://www.schneier.com/tag/breaches/), [cloud computing](https://www.schneier.com/tag/cloud-computing/), [data breaches](https://www.schneier.com/tag/data-breaches/), [Password Safe](https://www.schneier.com/tag/password-safe/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on December 26, 2022 at 7:06 AM](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html) •
[50 Comments](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html#comments)

### Comments

iAPX •
[December 26, 2022 7:57 AM](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html/#comment-414519)

> that’s because I don’t use the cloud for anything.

Et voilà!

But for many convenience trump security…

Doug •
[December 26, 2022 8:09 AM](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html/#comment-414520)

For those of us who do use cloud based systems, is there any way to mass import logins into password safe from other systems? The idea of manually moving hundreds of logins is daunting.

Robin •
[December 26, 2022 8:48 AM](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html/#comment-414521)

@iAPX and all: “Limiting attack surface by not pushing critical informations (passwords, token, etc.) to the cloud, this is exactly how I do with my password manager.”
Yes, I try to, but not always easy and in fact passwords are almost by definition, things that get sent over the internet to “somebody else’s computer”. Secure in theory …

But as a matter of interest, if my PasswordSafe database file were to fall into the wrong hands, in reality how safe is it? My password is 15 characters all char types and no silliness like “pAssw0rd”.

Michael •
[December 26, 2022 9:26 AM](https://www.schneier.com/blog/archives/2022/12/lastpass-breach.html/#comment-414522)

The most damning revelation of this latest LastPass hack is that not everything in your “LastPass vault” is encrypted, including websites, URLs, and all timestamps. While usernames, passwords, and “secure notes” are encrypted, a lot can be inferred from the unencrypted info. First of all, the hackers now have a full list of websites that you have accounts for. Second, the hackers will likely be able to gain access to a small number of websites which put sensitive info in the URL. Third, it’s opening the door for phishing attacks.

The tweet saying “four of my wallets were compromised” is too likely to just be a coincidence. There’s no evidence that these accounts were compromised through his LastPass vault, as the hackers could have gained access in many other ways (despite his reassurance), and the timing of the hacks could be pure coincidence.

> My password is 15 characters all char types and no silliness like “pAssw0rd”.

That’s a very secure password. Nobody is ever going to brute force your password. If your LastPass vault...