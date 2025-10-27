---
title: The end of PfP: Pain-free Passwords
url: https://palant.info/2023/03/20/the-end-of-pfp-pain-free-passwords/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-21
fetch_date: 2025-10-04T10:11:02.145966
---

# The end of PfP: Pain-free Passwords

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# The end of PfP: Pain-free Passwords

2023-03-20
 [Pfp](/categories/pfp/)/[Password-Managers](/categories/password-managers/)
 6 mins
 [2 comments](/2023/03/20/the-end-of-pfp-pain-free-passwords/#comments)

Seven years ago I [created a password manager](/2016/04/19/introducing-easy-passwords-the-new-best-way-to-juggle-all-those-passwords/). And a few days ago I pushed out the last release for it, notifying users that nothing else will come now. Yes, with the previous release being from 2019, this might have been obvious. Now itâs official however, PfP: Pain-free Passwords is no longer being developed.

![Screenshot of a message titled âPfP: Pain-free Passwords is being discontinued.â The text says: âAll good things must come to an end. It has been seven years since PfP was first introduced, back then under the name EasyPasswords. It has features that no other password manager can match, and I still like it. Unfortunately, developing a good password manager is lots of effort. I notice that Iâve been neglecting PfP, and this wonât change any more. So Iâm now making official what has been somewhat obvious already: PfP is no longer being developed. Does this mean that you can no longer use it? You can. But whatever breaks now stays broken. Sync to Google Drive in particular is already broken and non-trivial to fix unfortunately. What can you use instead? Not LastPass please. Maybe Bitwarden or 1Password. Definitely KeePass or a clone if you donât mind it being less intuitive. Personally, Iâll be using KeePassXC. How to get your passwords over? On the âAll Passwordsâ page, there is a new button for CSV export. It should be possible to import the resulting file into any password manager. In KeePassXC youâll need to check âFirst line has field names,â otherwise the default import settings will do.â](/2023/03/20/the-end-of-pfp-pain-free-passwords/discontinued.png)

I certainly learned a lot from this adventure, and I really like the product which came out of this. Unfortunately, a password manager is a rather time-consuming hobby, and my focus has been elsewhere for a while already.

This doesnât mean that PfP is going away. In fact, it will probably work well for quite a while until a browser change or something like that makes it unusable. Sync functionality in particular depends on third parties however, and this one already started falling apart.

#### Contents

* [Lessons learned](#lessons-learned)
* [The crux with password generators](#the-crux-with-password-generators)
* [The reason for giving up](#the-reason-for-giving-up)
* [Where to go from here](#where-to-go-from-here)

## Lessons learned

Back when I started this project, originally called EasyPasswords, I was still a cryptography newbie. So itâs not surprising that I made a bunch of questionable choices.

The first mistake was the choice of key derivation algorithm. PBKDF2 had the advantage of being supported natively by the browsers via the [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API), but otherwise itâs not a recommended choice.

The second mistake was focusing on password generation as protection mechanism and neglecting encryption. Encryption would only be used for the occasional stored password, while all the metadata stayed unencrypted.

As I said, I was new to cryptography. Not that there arenât âindustry leadersâ who made the exact same mistakes.

By 2018 Iâve [addressed both issues with PfP 2.0](/2018/02/07/easy-passwords-is-now-pfp-pain-free-passwords/) however. Encrypting all the data allowed [implementing secure sync functionality without relying on trusted storage](/2018/03/08/implementing-safe-sync-functionality-in-a-server-less-extension/). No, this isnât merely uploading an encrypted blob to some cloud storage, PfP sync is rather capable of merging concurrent changes from different PfP instances. Solving this was quite challenging, given that passwords can be locked during sync, in which case PfP wonât be able to decrypt its data.

At the current point I am still aware of two issues with the PfP design. One is the scrypt key derivation parameters being not quite optimal. The reason here is that I wanted for it to be usable on mobile devices, even though a mobile version of PfP never materialized.

As I pointed out myself not too long ago, you [compensate suboptimal key derivation by choosing a stronger password](/2023/01/30/password-strength-explained/). PfP doesnât offer sufficient guidance here however, and thatâs the second issue. There is a password strength indicator based on zxcvbn-ts, but it wonât necessarily flag weak passwords.

## The crux with password generators

PfP has been conceived as a password generator, a choice that looked very clever to me back in the day but seems rather questionable today. Yes, if passwords are being generated deterministically from website and user name, storing the password in the database is no longer necessary. But what difference does it make if all data is encrypted anyway?

In the end, the advantage of password generators is mostly password recovery. PfP allows creating secure paper backups which can be used to recover any password trivially as long as you still remember your master password. But even without the paper, remembering the generation parameters of a password (website and user name, optionally also a revision number and character sets used) is usually possible.

This advantage melted away partially when I designed a (somewhat less convenient) way for paper backups of stored passwords. And a paper backup for hundreds of passwords turned out simply impractical. In the end, what you need is a backup for a few most important passwords. And the rest of them will hopefully be recoverable via sync.

For the meager advantages, password generators have very clear disadvantages. The obvious one is complexity. While storing a password in the database is an intuitively understandable concept, setting up password generation parameters requires some explaining. And you cannot go away with stored passwords completely, so there will always be this âwhich one to choose?â

More importantly however, there is an attack scenario affecting only password generators but not conventional password managers. If you register at a website which is later compromised, your password for that website could be used to try guessing your master password. In case of success, this attack would compromise your passwords for other websites.

Iâve [recognized this threat early on](/2016/04/20/security-considerations-for-password-generators/) and mitigated it with a slow key derivation algorithm. Yet mitigating this attack scenario will always be worse than not having it at all.

## The reason for giving up

None of the issues are unsurmountable, and the security concerns donât even matter for a small niche solution like PfP. They are not the reason I am giving up on the project.

In fact, I had plenty of ideas for it. I created an [almost complete command-line version](https://github.com/palant/pfp-cli/) of PfP, written in Rust. The idea was that in future this well-tested library would be compiled into WebAssembly and used in the browser extensions as well.

There were also well thought-out ideas for user interface improvements, an Android app, password sharing. I merely lacked the time and the focus to finish any of it.

And thinking about it, I had to admit that things wonât change any more. As much as I like this product, I wouldnât be able to maintain it any more. There is always something thatâs more important.

## Where to go from here

Obviously, anyone is free to continue using PfP as they like. The fact that the extension isnât being developed doesnât mean that it wonât work. It already did pretty well without ...