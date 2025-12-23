---
title: Microsoft Is Finally Killing RC4
url: https://www.schneier.com/blog/archives/2025/12/microsoft-is-finally-killing-rc4.html
source: Schneier on Security
date: 2025-12-22
fetch_date: 2025-12-23T03:25:43.414304
---

# Microsoft Is Finally Killing RC4

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

## Microsoft Is *Finally* Killing RC4

After twenty-six years, Microsoft is [finally upgrading](https://arstechnica.com/security/2025/12/microsoft-will-finally-kill-obsolete-cipher-that-has-wreaked-decades-of-havoc/) the last remaining instance of the encryption algorithm RC4 in Windows.

> of the most visible holdouts in supporting RC4 has been Microsoft. Eventually, Microsoft upgraded Active Directory to support the much more secure AES encryption standard. But by default, Windows servers have continued to respond to RC4-based authentication requests and return an RC4-based response. The RC4 fallback has been a favorite weakness hackers have exploited to compromise enterprise networks. Use of RC4 played a [key role](https://arstechnica.com/security/2025/09/how-weak-passwords-and-other-failings-led-to-catastrophic-breach-of-ascension/) in last year’s breach of health giant Ascension. The breach caused life-threatening disruptions at 140 hospitals and put the medical records of 5.6 million patients into the hands of the attackers. US Senator Ron Wyden (D-Ore.) [in September](https://arstechnica.com/security/2025/09/senator-blasts-microsoft-for-making-default-windows-vulnerable-to-kerberoasting) called on the Federal Trade Commission to investigate Microsoft for “gross cybersecurity negligence,” citing the continued default support for RC4.
>
> Last week, Microsoft [said](https://www.microsoft.com/en-us/windows-server/blog/2025/12/03/beyond-rc4-for-windows-authentication) it was finally deprecating RC4 and cited its susceptibility to Kerberoasting, the form of attack, known since 2014, that was the root cause of the initial intrusion into Ascension’s network.

Fun fact: RC4 was a trade secret until I published the algorithm in the second edition of *[Applied Cryptography](https://www.schneier.com/books/applied-cryptography/)* in 1995.

Tags: [algorithms](https://www.schneier.com/tag/algorithms/), [Applied Cryptography](https://www.schneier.com/tag/applied-cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [Microsoft](https://www.schneier.com/tag/microsoft/), [RC4](https://www.schneier.com/tag/rc4/), [Windows](https://www.schneier.com/tag/windows/)

[Posted on December 22, 2025 at 12:05 PM](https://www.schneier.com/blog/archives/2025/12/microsoft-is-finally-killing-rc4.html) •
[4 Comments](https://www.schneier.com/blog/archives/2025/12/microsoft-is-finally-killing-rc4.html#comments)

### Comments

Ray Dillinger •
[December 22, 2025 1:45 PM](https://www.schneier.com/blog/archives/2025/12/microsoft-is-finally-killing-rc4.html/#comment-450852)

Finally. My condolences for the lasting pain of seeing your flawed work used by people to the point of damaging themselves and others. I am glad you have finally been relieved of this burden.

And yeah, it’s a burden. I’ve made some outright mistakes too, or failed to anticipate user assumptions and likely but mistaken uses. The repercussions and damage from some of them are still playing out decades later.

But we can only do our best. Whatever 20/20 hindsight we may apply later we act or create only on the basis of what we understand in the moment. We exercise restraint only on the basis of the consequences we can anticipate in the moment. Failure to act for fear that we might be making a mistake would prevent us from doing anything at all, including all the good we can do.

And failure to try to help would be worse, IMO, than trying and falling short.

So try not to be bitter about it. On bad-brain days, I’m kind of bitter about a few of mine. I know I should try not to be. I know it’s a symptom of having a bad-brain day. But it still happens.

Clive Robinson •
[December 22, 2025 6:16 PM](https://www.schneier.com/blog/archives/2025/12/microsoft-is-finally-killing-rc4.html/#comment-450856)

@ ALL,

**Oh the fun of naming an attack**

With regards,

> *Microsoft said it was finally deprecating RC4 and cited its susceptibility to Kerberoasting,*

This time it’s like barbequing a dog on a spit or griddle, I’ll let everyone make their own mind up as to who “the dog” is 😉

But if you want to know more about “griddling the dog”,

> **Kerberoasting, Microsoft, and a Senator**
>
> “*When I came up with Kerberoasting in 2014, I never thought it would live for more than a year or two. I (erroneously) thought that people would clean up the poor, dated credentials and move to more secure encryption. Here we are 11 years later, and unfortunately it still works more often than it should.*
>
> …
>
> The issue is any valid user (even a compromised one) can request a ticket for any server. This means an attacker can request and save tickets for any and all servers. With those tickets in hand, the attacker then makes a guess as to the server’s password and attempts to decrypt the tickets. Since the attack is offline, an attacker can attack the password as fast as their (often specialized) hardware will let them, up to billions of attempts per second. And with no lockout of the account due to the the attack being offline.

Tim Medin at,
<https://redsiege.com/blog/2025/09/kerberoasting-microsoft-and-a-senator/>

The thing is Microsoft’s “Active Directory”(AD) is one of it’s old “embrace and extend” policy ploys. Basically to take Open Standards and “add proprietary bits”. And yes it was a “dumb as duck 5h1t” thing to do, because it tied Microsoft’s hands rather more than it did their customers.

That is Microsoft had to support the lowest spec users and that costs mucho bucks in the long term[1].

Thus it’s trivial with AD for any person to request a ticket from “any server” and have the server claim it can only support RC4. Which makes the “offline cipher breaking” many times faster –getting on for a thousand times– than AES256.

Because Kerberos was designed at a time when the common idea was “be permissive” there was no black or white listing of users or servers or other security measures.

So the attack is fairly simple and I amongst others have been warning about “protocol ‘fall-back’ attacks” since you could do them via an easy plaintext “Man in The Middle”(MiTM) attack with just about every “protocol negotiation phase” in existence back last century…

As I’ve said before in many cases the lowest cipher is “plaintext” for “engineering test” but the software rarely if ever warns users it’s being used.

Because the prevailing view was, and in some cases still is,

“Don’t worry the user, they’ll phone tech-support and that will cost us big!”

But… Folks should look on this use of “Ron’s Code 4″(RC4) as a “back door gift” to various agencies and entities… Thus the question arising is,

“If Microsoft pulls this back door what is it going to do to ensure there is another back door for such agencies and entities?”

[1] Give you three guesses which clown came up with and pushed the ploy… a clue is “they must have been barmy”.

Clive Robinson •
[December 2...