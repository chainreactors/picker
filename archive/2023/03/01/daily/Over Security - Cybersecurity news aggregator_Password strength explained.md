---
title: Password strength explained
url: https://palant.info/2023/01/30/password-strength-explained/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:22:00.844116
---

# Password strength explained

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Password strength explained

2023-01-30
 [Security](/categories/security/)/[Password-Managers](/categories/password-managers/)
 9 mins
 [24 comments](/2023/01/30/password-strength-explained/#comments)

The conclusion of my blog posts [on the LastPass breach](/2022/12/23/lastpass-has-been-breached-what-now/) and [on Bitwardenâs design flaws](/2023/01/23/bitwarden-design-flaw-server-side-iterations/) is invariably: a strong master password is important. This is especially the case if you are a target somebody would throw considerable resources at. But everyone else might still get targeted due to flaws like password managers failing to keep everyone on current security settings.

There is lots of confusion about what constitutes a strong password however. How strong is my current password? Also, how strong is strong enough? These questions donât have easy answers. Iâll try my best to explain however.

If you are only here for recommendations on finding a good password, feel free to skip ahead to the [Choosing a truly strong password](#choosing-a-truly-strong-password) section.

#### Contents

* [Where strong passwords are crucial](#where-strong-passwords-are-crucial)
* [How password guessing works](#how-password-guessing-works)
* [The mathematics of guessing passwords](#the-mathematics-of-guessing-passwords)
* [Estimating the complexity of a given password](#estimating-the-complexity-of-a-given-password)
* [How strong are real passwords?](#how-strong-are-real-passwords)
* [Choosing a truly strong password](#choosing-a-truly-strong-password)

## Where strong passwords are crucial

First of all, password strength isnât always important. If your password is stolen as clear text via a [phishing attack](https://en.wikipedia.org/wiki/Phishing) or a compromised web server, a strong password wonât help you at all.

In order to reduce the damage from such attacks, itâs way more important that you do not reuse passwords â each web service should have its own unique password. If your login credentials for one web service get into the wrong hands, these shouldnât be usable to compromise all your other accounts e.g. by means of [credential stuffing](https://en.wikipedia.org/wiki/Credential_stuffing). And since you cannot possibly keep hundreds of unique passwords in your head, using a password manager (which can be the one built into your browser) is essential.

But this password manager becomes a single point of failure. Especially if you upload the password manager data to the web, be it to sync it between multiple devices or simply as a backup, there is always a chance that this data is stolen.

Of course, each password manager vendor will tell you that all the data is safely encrypted. And that you are the only one who can possibly decrypt it. Sometimes this is true. Often enough this is a lie however. And the truth is rather: nobody can decrypt your data as long as they are unable to guess your master password.

So that one password needs to be very hard to guess. A strong password.

Oh, and donât forget enabling [Multi-factor authentication (MFA)](https://en.wikipedia.org/wiki/Multi-factor_authentication) where possible regardless.

## How password guessing works

When someone has your encrypted data, guessing the password it is encrypted with is a fairly straightforward process.

![A flow chart starting with box 1 âProduce a password guess.â An arrow leads to a decision element 2 âDoes this password work?â An arrow titled âNoâ leads to the original box 1. An arrow titled âYesâ leads to box 3 âDecrypt passwords.â](/2023/01/30/password-strength-explained/password_guessing.png)

Ideally, your password manager made step 2 in the diagram above very slow. The recommendation for encryption is allowing at most 1,000 guesses per second on common hardware. This renders guessing passwords slow and expensive. Few password managers actually match this requirement however.

But password guesses will not be generated randomly. Passwords known to be commonly chosen like âPassword1â or âQwerty123â will be tested among the first ones. No amount of slowing down the guessing will prevent decryption of data if such an easy to guess password is used.

So the goal of choosing a strong password isnât choosing a password including as many character classes as possible. It isnât making the password *look* complex either. No, making it very long also wonât necessarily help. What matters is that this particular password comes up as far down as possible in the list of guesses.

## The mathematics of guessing passwords

A starting point for password guessing are always passwords known from previous data leaks. For example, security professionals often refer to `rockyou.txt`: a list with 14 million passwords leaked 2009 in the RockYou breach.

If your password is somewhere on this list, even at 1,000 guesses per second it will take at most 14,000 seconds (less than 4 hours) to find your password. This isnât exactly a long time, and thatâs already assuming that your password manager vendor has done their homework. As past experience shows, this isnât an assumption to be relied on.

Since we are talking about computers here, the âproperâ way to express large numbers is via powers of two. So we say: a password on the RockYou list has less than 24 bits of entropy, meaning that it will definitely be found after 224 (16,777,216) guesses. Each bit of entropy added to the password results in twice the guessing time.

But obviously the RockYou passwords are too primitive. Many of them wouldnât even be accepted by a modern password manager. What about using a phrase from a song? Shouldnât it be hard to guess because of its length already?

Somebody [calculated (and likely overestimated)](https://security.stackexchange.com/a/164874/4778) the number of available song phrases as 15 billion, so we are talking about at most 34 bits of entropy. This appears to raise the password guessing time to half a year.

Except: the song phrase you are going to choose wonât actually be at the bottom of any list. Thatâs already because you donât know all the 30 million songs out there. You only know the reasonably popular ones. In the end itâs only a few thousand songs you might reasonably choose, and your date of birth might help narrow down the selection. Each song has merely a few dozen phrases that you might pick. You are lucky if you get to 20 bits of entropy this way.

## Estimating the complexity of a given password

Now itâs hard to tell how quickly real password crackers will narrow down on a particular password. One can look at all the patterns however that went into a particular password and estimate how many bits these contribute to the result. Consider this XKCD comic:

![An XKCD comic comparing the complexity of the passwords âTr0ub4dor&3â and âcorrect horse battery stapleâ](/2023/01/30/password-strength-explained/xkcd_password_strength.png)

*Source: [XKCD 936](https://xkcd.com/936/)*

An uncommon base word chosen from a dictionary with approximately 50,000 words contributes 16 bits. The capitalization at the beginning of the word on the other hand contributes only one bit because there are only two options: capitalizing or not capitalizing. There are common substitutions and some junk added at the end contributing a few more bits. But the end result are rather unimpressive 28 bits, maybe a few more because the password creation scheme has to be guessed as well. So this is a password *looking* complex, it isnât actually strong however.

The (unmaintained) zxcvbn library tries to automate this process. You can try it out [on a webpage](https://lowe.github.io/tryzxcvbn/), it runs entirely in the browser and doesnât upload your password anywhere. The `guesses_log10` value in the result...