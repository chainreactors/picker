---
title: Good Essay on the History of Bad Password Policies
url: https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html
source: Schneier on Security
date: 2024-11-16
fetch_date: 2025-10-06T19:20:18.883636
---

# Good Essay on the History of Bad Password Policies

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

## Good Essay on the History of Bad Password Policies

Stuart Schechter makes some [good points](https://stuartschechter.org/posts/password-history/) on the history of bad password policies:

> Morris and Thompson’s work brought much-needed data to highlight a problem that lots of people suspected was bad, but that had not been studied scientifically. Their work was a big step forward, if not for two mistakes that would impede future progress in improving passwords for decades.
>
> First, was Morris and Thompson’s confidence that their solution, a password policy, would fix the underlying problem of weak passwords. They incorrectly assumed that if they prevented the specific categories of weakness that they had noted, that the result would be something strong. After implementing a requirement that password have multiple characters sets or more total characters, they wrote:
>
> > These improvements make it exceedingly difficult to find any individual password. The user is warned of the risks and if he cooperates, he is very safe indeed.
>
> As should be obvious now, a user who chooses “p@ssword” to comply with policies such as those proposed by Morris and Thompson is not very safe indeed. Morris and Thompson assumed their intervention would be effective without testing its efficacy, considering its unintended consequences, or even defining a metric of success to test against. Not only did their hunch turn out to be wrong, but their second mistake prevented anyone from proving them wrong.

That second mistake was convincing sysadmins to hash passwords, so there was no way to evaluate how secure anyone’s password actually was. And it wasn’t until hackers started stealing and publishing large troves of actual passwords that we got the data: people are terrible at generating secure passwords, even with rules.

Tags: [hashes](https://www.schneier.com/tag/hashes/), [history of security](https://www.schneier.com/tag/history-of-security/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on November 15, 2024 at 7:05 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html) •
[22 Comments](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html#comments)

### Comments

Anonymous •
[November 15, 2024 7:34 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html/#comment-441682)

Well, I agree in part. Policies are a problem with people being people. But they can be improved with what we know now.

And the hashed databases can indeed be tested. The criminals do just that by hashing common variations.

The proposal to use public key crypto is likely to have many unintended consequences as well (making the protected file with the passwords a target, untrusted servers or employees on the hunt for password reuse…).

Anonymous •
[November 15, 2024 7:35 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html/#comment-441683)

Well, I agree in part. Policies are a problem with people being people. But they can be improved with what we know now.

And the hashed databases can indeed be tested. The criminals do just that by hashing common variations.

The proposal to use public key crypto is likely to have many unintended consequences as well (making the protected file with the passwords a target, untrusted servers or employees on the hunt for password reuse…).

Clive Robinson •
[November 15, 2024 9:17 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html/#comment-441687)

@ Bruce “Only”

The authors name sounded familiar so I “followed a trail” to,

<https://dicekeys.com>

Where under “leadership” I found two names well known to me, Joseph Bonneau and you.

I know this is only a “personal blog” not a Journal or other Academic Publication, but over the past decade with increasing “federalism” of “Social Media” and similar people are getting not just “Snarky” but are looking for “authors” to “Declare Interests” in things other than “Papers”.

So you might want to consider “staying ahead of the mob” and putting in a footer to mention close, business, etc associations when they arise.

Clive Robinson •
[November 15, 2024 9:22 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html/#comment-441689)

@ Bruce “Only”

The authors name sounded familiar so I “followed a trail” to,

<https://dicekeys.com>

Where under “leadership” I found two names well known to me, Joseph Bonneau and you.

I know this is only a “personal blog” not a Journal or other Academic Publication, but over the past decade with increasing “federalism” of “Social Media” and similar people are getting not just “Snarky” but are looking for “authors” to “Declare Interests” in things other than “Papers”.

So you might want to consider “staying ahead of the mob” and putting in a footer to mention close, business, etc associations when they arise.

Not Anonymouse •
[November 15, 2024 10:43 AM](https://www.schneier.com/blog/archives/2024/11/good-essay-on-the-history-of-bad-password-policies.html/#comment-441691)

But you can evaluate how secure everyone’s password is, even when it’s hashed… you just have to do it within the window of time before it’s stored at rest hashed. It is clear text at some point in memory, use that point.

In modern times more and more sites do it all the time: whenever a person sets or resets their password, we check it against Troy Hunt’s “Have I Been Pwned” service to see if it’s a bad password, if it’s in that database, we deny the user the ability to set their password to that bad password, and make them pick a better one first. Once this has been implemented in your code, we can nag and then finally force a one-time reset to bring everyone under this kind of policy, which is immensely better than requiring character classes. For those who never login after years and years eventually a user cleanup is in order.

Before anyone takes this to “horrors, checking an external service”… well, yes, you can download his whole database and do everything locally, if you have enough bandwidth and space and inkling to do so and keep it up to date. Or you can use his “k-anonymity model” and do it live as a service. Or you can roll your own by perusing “dark web” releases of troves of passwords yourself, duplicating his work. It’s your choice, depending on your threat model.

So I disagree that hashing is a mistake at all, it just makes you do your evaluation in a different way. But perhaps I am making your main point that the best success of implementing such evaluation (and fixing it too!) that we’ve seen so far actually depends on hacker releases of troves of data…

Joe D •
[November 15, 2024 10:58 AM](https://www.schneier.com/blo...