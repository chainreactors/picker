---
title: Thomas Fitzsimmons: Thunderbird and OpenPGP
url: https://www.fitzsim.org/blog/?p=477
source: Planet Classpath
date: 2022-12-08
fetch_date: 2025-10-04T00:52:30.833323
---

# Thomas Fitzsimmons: Thunderbird and OpenPGP

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Thunderbird and OpenPGP

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [December 6, 2022December 6, 2022](https://www.fitzsim.org/blog/?p=477)
[1 Comment on Thunderbird and OpenPGP](https://www.fitzsim.org/blog/?p=477#comments)

I recently helped some friends set up Thunderbird and OpenPGP; the combination is much more user-friendly now.

OpenPGP is end-to-end encryption for email. Each user generates a private and public key. Each user imports a copy of the other user’s public key in their Thunderbird setup (they can copy the keys onto a USB drive or even email them to each other). Then when they select the “Encrypt” button during message composition, Thunderbird does the rest: no one on the Internet can read the message body. (The message metadata, like the subject line and the fact that the users are emailing each other, is still visible to Internet mail server administrators.)

The OpenPGP + Thunderbird user experience in 2022 is quite straightforward! I was worried I would need to use add-ons and external programs, but nope, it’s all built-in, including keypair generation. Public key import/export via the key manager is simple. OpenPGP is also nicely integrated into the reading and composition interfaces, which clearly indicate message signing and encryption status. Nice work by the Thunderbird team!

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[December 6, 2022December 6, 2022](https://www.fitzsim.org/blog/?p=477)Posted in[Uncategorized](https://www.fitzsim.org/blog/?cat=1)Tags: [email](https://www.fitzsim.org/blog/?tag=email)

## Post navigation

[Previous Post Previous post:
Mastodon and HTML](https://www.fitzsim.org/blog/?p=465)

[Next Post Next post:
whisper.cpp and POWER9](https://www.fitzsim.org/blog/?p=484)

## Join the Conversation

1. ![](https://secure.gravatar.com/avatar/5f7283e8b1c35bda22c348b2170da193430a966b7a93c53c9a4982a3b4e02195?s=60&d=mm&r=g)

1 Comment

1. ![](https://secure.gravatar.com/avatar/5f7283e8b1c35bda22c348b2170da193430a966b7a93c53c9a4982a3b4e02195?s=60&d=mm&r=g)**Tegel-bot** says:

   [December 7, 2022 at 6:35 am](https://www.fitzsim.org/blog/?p=477#comment-45642)

   @fitzsim is right that this is a fantastic, user-friendly tool for end-to-end encryption. After the public key has been added to the Thunderbird setup, the rest of the process is seamless as @fitzsim has described here. Bravo Thunderbird and OpenPGP!

   [Reply](https://www.fitzsim.org/blog/?p=477&replytocom=45642#respond)

## Leave a comment

### [Cancel reply](/blog/?p=477#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)