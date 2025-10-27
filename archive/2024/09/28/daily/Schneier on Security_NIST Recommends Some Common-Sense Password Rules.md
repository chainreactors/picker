---
title: NIST Recommends Some Common-Sense Password Rules
url: https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html
source: Schneier on Security
date: 2024-09-28
fetch_date: 2025-10-06T18:30:40.888030
---

# NIST Recommends Some Common-Sense Password Rules

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

## NIST Recommends Some Common-Sense Password Rules

NIST’s second draft of its “[SP 800-63-4](https://pages.nist.gov/800-63-4/sp800-63b.html)“—its digital identify guidelines—finally contains some really good rules about passwords:

> The following requirements apply to passwords:
>
> 1. lVerifiers and CSPs SHALL require passwords to be a minimum of eight characters in length and SHOULD require passwords to be a minimum of 15 characters in length.
> 2. Verifiers and CSPs SHOULD permit a maximum password length of at least 64 characters.
> 3. Verifiers and CSPs SHOULD accept all printing ASCII [RFC20] characters and the space character in passwords.
> 4. Verifiers and CSPs SHOULD accept Unicode [ISO/ISC 10646] characters in passwords. Each Unicode code point SHALL be counted as a signgle character when evaluating password length.
> 5. Verifiers and CSPs SHALL NOT impose other composition rules (e.g., requiring mixtures of different character types) for passwords.
> 6. Verifiers and CSPs SHALL NOT require users to change passwords periodically. However, verifiers SHALL force a change if there is evidence of compromise of the authenticator.
> 7. Verifiers and CSPs SHALL NOT permit the subscriber to store a hint that is accessible to an unauthenticated claimant.
> 8. Verifiers and CSPs SHALL NOT prompt subscribers to use knowledge-based authentication (KBA) (e.g., “What was the name of your first pet?”) or security questions when choosing passwords.
> 9. Verifiers SHALL verify the entire submitted password (i.e., not truncate it).

Hooray.

News [article](https://arstechnica.com/security/2024/09/nist-proposes-barring-some-of-the-most-nonsensical-password-rules/). Slashdot [thread](https://yro.slashdot.org/story/24/09/27/0021240/nist-proposes-barring-some-of-the-most-nonsensical-password-rules).

EDITED TO ADD (10/13): There are potential security issues with allowing arbitrary Unicode in passwords.

Tags: [NIST](https://www.schneier.com/tag/nist/), [passwords](https://www.schneier.com/tag/passwords/), [reports](https://www.schneier.com/tag/reports/)

[Posted on September 27, 2024 at 7:01 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html) •
[42 Comments](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html#comments)

### Comments

Alan •
[September 27, 2024 7:18 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440781)

Those all look good, except #5:

> 1. Verifiers and CSPs SHALL NOT impose other composition rules (e.g., requiring mixtures of different character types) for passwords.

I think it improves security to force users to pick strong passwords. Requiring a mixture of letters, numbers and punctuation means that the password cannot just be a dictionary word, and therefore I think it improves security.

What are your thoughts, Bruce?

md •
[September 27, 2024 7:46 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440782)

How about….

1. Verifiers and CSPs SHALL NOT disable the ability to paste passwords into form fields.

Pascal S. •
[September 27, 2024 8:40 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440783)

Excellent news.

I would just extend the 9th rule to not only forbide truncation but also transformation to e.g. upper or lower characters:

Rule 9 : Verifiers SHALL only accept the correct password and not derived passwords (e.g. truncated passwords or passwords that differ by case).

John Faber •
[September 27, 2024 8:49 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440784)

Is there a reason for requirement #5: “Verifiers and CSPs SHALL NOT impose other composition rules (e.g., requiring mixtures of different character types) for passwords.”

Wouldn’t requiring password complexity enforce a little more security by helping prevent password guessing from shoulder surfing? If making passwords have different types of characters limits the number of potential passwords is a concern, then NIST could address that risk by making requirement #1 for password length longer: “Verifiers and CSPs shall require passwords to be a minimum of twelve characters in length.”

austin •
[September 27, 2024 10:51 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440786)

That seems good. I am always mixed about composition rules. Many users have a very hard time with coming up with a password that meets complexity requirements.

Snarki, child of Loki •
[September 27, 2024 10:57 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440787)

The “no knowledge-based authentication” is going to run into problems with “I forgot my password/you bastids reset it on me” plus “my old email no longer works”.

Wayne •
[September 27, 2024 11:37 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440788)

Seems like reasonable guidelines, though I’m a little puzzled by #5. I’ll read the article and the /. later, and I’m sure Ars will also be discussing it.

I ran into #9 big time with a bank, and closed the account due to it. They changed their online banking system and I had to reset my password. So I did, and it took it. I did my online stuff, signed off, couldn’t sign on again. Called them up for a reset, rinse, repeat, can’t sign on again. This went back and forth a couple more times until the boffin asked how long my password was, and I told them. It was too long. It wasn’t ridiculously long, perhaps 13 or 14 characters, I don’t recall. But if it was too long, why was their entry screen accepting it?

I closed my account soon after.

There was also the little matter of their revealing what their back-end system was during a system crash and their ODBC connector string was revealed: it was Paradox. Not really an industrial-grade database.

Dr Wellington Yueh •
[September 27, 2024 11:42 AM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440789)

“Hooray.”

Agree.

This goes with something I was told a long time ago by my mentor: If you make the procedure for performing a task too difficult, a person will escape procedure to perform the task.

Vincent Archer •
[September 27, 2024 12:23 PM](https://www.schneier.com/blog/archives/2024/09/nist-recommends-some-common-sense-password-rules.html/#comment-440791)

People tend to focus on composition rules, but in my experience, they are trivially bypassed by people:
– You uppercase the first letter, so what?
– Replace a by 4, i by 1, e by 3, g by 9, done
– Tack a ...