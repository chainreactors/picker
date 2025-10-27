---
title: Beyond Bcrypt
url: https://soatok.blog/2024/11/27/beyond-bcrypt/
source: Dhole Moments
date: 2024-11-28
fetch_date: 2025-10-06T19:20:09.796181
---

# Beyond Bcrypt

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/)

# Beyond Bcrypt

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [November 27, 2024](https://soatok.blog/2024/11/27/beyond-bcrypt/)

![Beyond Bcrypt](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/11/BlogHeader-2024-Bcrypt.png?fit=1200%2C675&ssl=1)

In 2010, Coda Hale wrote *[How To Safely Store A Password](https://codahale.com/how-to-safely-store-a-password/)* which began with the repeated phrase, “Use bcrypt”, where the word bcrypt was linked to a different implementation for various programming languages.

This had two effects on the technology blogosphere at the time:

1. It convinced a lot of people that bcrypt was the right answer for storing a password.
2. It created a meme for how technology bloggers recommend specific cryptographic algorithms when they want attention from Hacker News.

At the time, it was great advice!

![Drakeposting Yes Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-08.png?resize=512%2C512&ssl=1)

Credit: [CMYKat](https://cmykatgraphics.carrd.co/)

In 2010, bcrypt was the only clearly good answer for password hashing in most programming languages.

In the intervening *almost fifteen years*, we’ve learned a lot more about passwords, password cracking, authentication mechanism beyond passwords, and password-based cryptography.

> If you haven’t already [read my previous post about password-based cryptography](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/), you may want to give that one a once-over before you continue.

But we’ve also learned a lot more about bcrypt, its limitations, the various footguns involved with using it in practice, and even some cool shit you can build with it.

In light of a recent discussion about [switching WordPress’s password hashing algorithm](https://github.com/WordPress/wordpress-develop/pull/7333) from PHPass (which is based on MD5) to bcrypt, I feel now is the perfect time to dive into this algorithm and its implications on real-world cryptography.

## Understanding Bcrypt in 2024

Bcrypt is a password hashing function, but [not a password KDF](https://news.ycombinator.com/item?id=22028143) or general-purpose cryptographic hash function.

If you’re using a sane password storage API, such as [PHP’s password API](https://www.php.net/manual/en/function.password-hash.php), you don’t even need to think about salting your passwords, securely verifying passwords, or handling weird error conditions. Instead, you only need concern yourself with the “cost” factor, which exponentially increases the runtime of the algorithm.

There’s just one problem: **bcrypt silently truncates after 72 characters** (or rather, bytes, if you’re pedantic and assume non-ASCII passwords, such as emoji).

Here’s a quick script [you can run yourself](https://3v4l.org/cRhjD) to test this:

```
<?php
$example1 = str_repeat('A', 72);
$example2 = $example1 . 'B';

$hash = password_hash($example1, PASSWORD_BCRYPT);
var_dump(password_verify($example2, $hash));
```

This may sound ludicrous (“who uses 72 character passwords anyway?”) until you see security advisories like [this recent one from Okta](https://trust.okta.com/security-advisories/okta-ad-ldap-delegated-authentication-username/).

> The Bcrypt algorithm was used to generate the cache key where we hash a combined string of userId + username + password. Under a specific set of conditions, listed below, this could allow users to authenticate by providing the username with the stored cache key of a previous successful authentication.
>
> (…)
>
> * The username is 52 characters or longer

The other thing to consider is that many people use passphrases, such as those generated from Diceware, which produce longer strings with less entropy per character.

If you use bcrypt as-is, you will inevitably run into this truncation at some point.

### “Let’s pre-hash passwords!”

In response to this limitation, many developers will suggest pre-hashing the password with a general purpose cryptographic hash function, such as SHA-256.

And so, in pursuit of a way to avoid one footgun, developers introduced two more.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokGlitch.png?resize=512%2C445&ssl=1)

[AJ](https://bsky.app/profile/ajlovesdinos.bsky.social)

#### Truncation on NUL Bytes

If you use the raw binary output of a hash function as your password hash, be aware [that bcrypt will truncate on NUL (`0x00`) bytes](https://blog.ircmaxell.com/2015/03/security-issue-combining-bcrypt-with.html).

With respect to the WordPress issue linked above, the default for PHP’s hashing API is to output hexadecimal characters.

This is a bit wasteful. Base64 is preferable, although any isomorphism of the raw hash output that doesn’t include a `0x00` byte is safe from truncation.

#### Hash Shucking

When a system performs a migration from a cryptographic hash function (e.g., MD5) to bcrypt, they typically choose to re-hash the existing hash with bcrypt.

Because users typically reuse passwords, you can often take the fast, unsalted hashes from another breach and use it as your password dictionary for bcrypt.

If then you succeed in verifying the bcrypt password for a fast hash, you can then plug the fast hash into software like Hashcat, and then crack the actual password at a much faster rate (tens of billions of candidates/second, versus thousands per second).

This technique is called [hash shucking](https://youtu.be/OQD3qDYMyYQ?t=1462) (YouTube link).

You can avoid hash shucking by using HMAC with a static key–either universal for all deployments of your software, or unique per application.

It doesn’t really matter which you choose; all you really need from it is domain separation from naked hashes.

> I frequently see this referred to as “peppering”, but the term “pepper” isn’t rigidly defined anywhere.

One benefit of using a per-application HMAC secret does make your hashes harder to crack if you don’t know this secret.

For balance, one downside is that your hashes are no longer portable across applications without managing this static key.

### Disarming Bcrypt’s Footguns

Altogether, it’s quite straightforward to avoid bcrypt’s footguns, as [I had recommended to WordPress last week](https://github.com/WordPress/wordpress-develop/pull/7333#pullrequestreview-2449232465).

1. Pre-hash with HMAC-SHA512.
2. Ensure the output of step 1 is base64-encoded.
3. Pass the output of step 2 to PHP’s password API.

Easy, straightforward, and uncontroversial. Right?

#### Objections to Bcrypt Disarmament

The linked discussion was [tedious](https://github.com/WordPress/wordpress-develop/pull/7333#issuecomment-2499156613), so I will briefly describe the objections raised to my suggestion.

1. This is “rolling our own crypto”.
   * Answer: No, it’s a well-understood pattern that’s been discussed in the PHP community for well over a decade.
2. Passwords over 72 characters are rare and not worthy of our consideration.
   * Answer: No, this has bit people in unexpected ways before (see: Okta).

     When you develop a popular CMS, library, or framework, you cannot possibly know all the ways that your software will be used by others. It’s almost always better to be misuse-resistant.
3. Pre-hashing introduces a Denial-of-Service attack risk.
   * Answer: No. Bcrypt with a cost factor of 10 is about 100,000 times as expensive as SHA2.
4. ...