---
title: Bitwarden design flaw: Server side iterations
url: https://palant.info/2023/01/23/bitwarden-design-flaw-server-side-iterations/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-25
fetch_date: 2025-10-04T04:45:04.383961
---

# Bitwarden design flaw: Server side iterations

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Bitwarden design flaw: Server side iterations

2023-01-23
 [Bitwarden](/categories/bitwarden/)/[Security](/categories/security/)/[Password-Managers](/categories/password-managers/)/[Lastpass](/categories/lastpass/)
 7 mins
 [39 comments](/2023/01/23/bitwarden-design-flaw-server-side-iterations/#comments)

In the aftermath of the LastPass breach it became increasingly clear that LastPass didnât protect their users as well as they should have. When people started looking for alternatives, two favorites emerged: 1Password and Bitwarden. But do these do a better job at protecting sensitive data?

For 1Password, this question could be answered fairly easily. The [secret key functionality](https://blog.1password.com/what-the-secret-key-does/) decreases usability, requiring the secret key to be moved to each new device used with the account. But the fact that this random value is required to decrypt the data means that the encrypted data on 1Password servers is almost useless to potential attackers. It cannot be decrypted even for weak master passwords.

As to Bitwarden, the media mostly repeated their claim that the data is protected with 200,001 PBKDF2 iterations: 100,001 iterations on the client side and another 100,000 on the server. This being twice the default protection offered by LastPass, it doesnât sound too bad. Except: as it turns out, the server-side iterations are designed in such a way that they donât offer any security benefit. What remains are 100,000 iterations performed on the client side, essentially the same protection level as for LastPass.

Mind you, LastPass isnât only being criticized for using a default iterations count that is three time lower than the [current OWASP recommendation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2). LastPass also [failed to encrypt all data](/2022/12/24/what-data-does-lastpass-encrypt/), a flaw that Bitwarden doesnât seem to share. LastPass also [kept the iterations count for older accounts dangerously low](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/), something that Bitwarden hopefully didnât do either (**Edit**: yes, they [did this](#c000002), some accounts have considerably lower iteration count). LastPass also [chose to downplay the breach instead of suggesting meaningful mitigation steps](/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/), something that Bitwarden hopefully wouldnât do in this situation. Still, the protection offered by Bitwarden isnât exactly optimal either.

**Edit** (2023-01-23): Bitwarden increased the default client-side iterations to 350,000 a few days ago. So far this change only applies to new accounts, and it is unclear whether they plan to upgrade existing accounts automatically. And today OWASP changed their recommendation to 600,000 iterations, it has been adjusted to current hardware.

**Edit** (2023-01-24): I realized that some of my concerns were already voiced in Bitwardenâs [2018 Security Assessment](https://cure53.de/pentest-report_bitwarden.pdf). Linked to it in the respective sections.

#### Contents

* [How Bitwarden protects usersâ data](#how-bitwarden-protects-users-data)
* [What this means for decrypting the data](#what-this-means-for-decrypting-the-data)
* [What this means for you](#what-this-means-for-you)
* [Is Bitwarden as bad as LastPass?](#is-bitwarden-as-bad-as-lastpass)
* [How server-side iterations could have been designed](#how-server-side-iterations-could-have-been-designed)

## How Bitwarden protects usersâ data

Like most password managers, Bitwarden uses a single master password to protect usersâ data. The Bitwarden server isnât supposed to know this password. So two different values are being derived from it: a master password hash, used to verify that the user is allowed to log in, and a key used to encrypt/decrypt the data.

![A schema showing the master password being hashed with PBKDF2-SHA256 and 100,000 iterations into a master key. The master key is further hashed on the server side before being stored in the database. The same master key is turned into a stretched master key used to encrypt the encryption key, here no additional PBKDF2 is applied on the server side.](/2023/01/23/bitwarden-design-flaw-server-side-iterations/bitwarden-password-hashing-key-derivation-encryption.jpg)

*Bitwarden password hashing, key derivation, and encryption. Source: [Bitwarden security whitepaper](https://bitwarden.com/images/resources/security-white-paper-download.pdf)*

If we look at how Bitwarden describes the process in their [security whitepaper](https://bitwarden.com/images/resources/security-white-paper-download.pdf), there is an obvious flaw: the 100,000 PBKDF2 iterations on the server side are only applied to the master password hash, not to the encryption key. This is pretty much the same flaw that I [discovered in LastPass in 2018](/2018/07/09/is-your-lastpass-data-really-safe-in-the-encrypted-online-vault/#cracking-the-encryption).

## What this means for decrypting the data

So what happens if some malicious actor happens to get a copy of the data, like it happened with LastPass? They will need to decrypt it. And for that, they will have to guess the master password. PBKDF2 is meant to slow down verifying whether a guess is correct.

Testing the guesses against the master password hash would be fairly slow: 200,001 PBKDF2 iterations here. But the attackers wouldnât waste time doing that of course. Instead, for each guess they would derive an encryption key (100,000 PBKDF2 iterations) and check whether this one can decrypt the data.

This simple tweak removes all the protection granted by the server-side iterations and speeds up master password guessing considerably. Only the client-side iterations really matter as protection.

## What this means for you

The default protection level of LastPass and Bitwarden is identical. This means that you need a strong master password. And the only real way to get there is generating your password randomly. For example, you could generate a random passphrase using the [diceware approach](https://en.wikipedia.org/wiki/Diceware).

Using a dictionary for 5 dice (7776 dictionary words) and picking out four random words, you get a password with slightly over 50 bits of entropy. Iâve done the [calculations for guessing such passwords](/2022/12/28/lastpass-breach-the-significance-of-these-password-iterations/#what-is-this-setting-about): approximately 200 years on a single graphics card or $1,500,000.

This should be a security level sufficient for most regular users. If you are guarding valuable secrets or are someone of interest for state-level actors, you might want to consider a stronger password. Adding one more word to your passphrase increases the cost of guessing your password by factor 7776. So a passphrase with five words is already almost unrealistic to guess even for state-level actors.

All of this assumes that your [KDF iterations setting](https://bitwarden.com/help/what-encryption-is-used/#changing-kdf-iterations) is set to the default 100,000. Bitwarden will allow you to set this value as low as 5,000 without even warning you. This was mentioned as BWN-01-009 in Bitwardenâs [2018 Security Assessment](https://cure53.de/pentest-report_bitwarden.pdf), yet there we are five years later. Should your setting be too low, I recommend fixing it immediately. Reminder: [current OWASP recommendation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2) is 310,000.

## Is Bitwarden as bad as LastPass?

So as it turns out, with the default settings Bitwarden provides exactly the same protection level as LastPass. This is only part of the story however.

One question is how many accounts have a protection level below the de...