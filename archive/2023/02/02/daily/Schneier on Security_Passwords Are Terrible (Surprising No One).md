---
title: Passwords Are Terrible (Surprising No One)
url: https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html
source: Schneier on Security
date: 2023-02-02
fetch_date: 2025-10-04T05:31:13.697504
---

# Passwords Are Terrible (Surprising No One)

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

## Passwords Are Terrible (Surprising No One)

This is the [result](https://arstechnica.com/information-technology/2023/01/a-fifth-of-passwords-used-by-federal-agency-cracked-in-security-audit/#p3) of a security audit:

> More than a fifth of the passwords protecting network accounts at the US Department of the Interior—including Password1234, Password1234!, and ChangeItN0w!—were weak enough to be cracked using standard methods, a recently published security audit of the agency found.
>
> […]
>
> The results weren’t encouraging. In all, the auditors cracked 18,174—or 21 percent—­of the 85,944 cryptographic hashes they tested; 288 of the affected accounts had elevated privileges, and 362 of them belonged to senior government employees. In the first 90 minutes of testing, auditors cracked the hashes for 16 percent of the department’s user accounts.
>
> The audit uncovered another security weakness—the failure to consistently implement multi-factor authentication (MFA). The failure extended to 25—­or 89 percent—­of 28 high-value assets (HVAs), which, when breached, have the potential to severely impact agency operations.

Original [story](https://techcrunch.com/2023/01/10/interior-department-watchdog-passwords/):

> To make their point, the watchdog spent less than $15,000 on building a password-cracking rig—a setup of a high-performance computer or several chained together ­- with the computing power designed to take on complex mathematical tasks, like recovering hashed passwords. Within the first 90 minutes, the watchdog was able to recover nearly 14,000 employee passwords, or about 16% of all department accounts, including passwords like ‘Polar\_bear65’ and ‘Nationalparks2014!’.

Tags: [cracking](https://www.schneier.com/tag/cracking/), [national security policy](https://www.schneier.com/tag/national-security-policy/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on February 1, 2023 at 7:08 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html) •
[85 Comments](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html#comments)

### Comments

Ted •
[February 1, 2023 8:02 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416972)

People Are Terrible (Surprising Bruce Schneier)

Passwords, combined with 2FA, are great as long as you actually choose strong passwords. People will always be the weakest link in security, which is why phishing and other social engineering attacks are so successful. It doesn’t matter if you replace passwords with something else. Need to click a notification on your phone to login? People will simply be tricked into clicking the little notification thereby giving the hacker access to their accounts.

jbmartin6 •
[February 1, 2023 8:06 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416973)

16% crack rate on dumped NTLM hashes is fairly normal. According to the article, the point of the exercise was merely to counter claims by the DOI that it would take 100+ years to crack any of the hashes because of their password policy.

Ted •
[February 1, 2023 8:08 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416974)

The above @Ted is not me

The IG report: P@s$w0rds at the U.S. Department of the Interior

<https://www.doioig.gov/sites/default/files/2021-migration/Final%20Inspection%20Report_DOI%20Password_Public.pdf>

bert •
[February 1, 2023 8:15 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416975)

@Ted (the first one):

> Need to click a notification on your phone to login? People will simply be tricked into clicking the little notification thereby giving the hacker access to their accounts.

This is not true. Such an attack would be exponentially more difficult because today’s phone OSes are heavily sandboxed and you can’t just send a “notification to log in” if the user’s using passkeys.

Anonymous •
[February 1, 2023 8:17 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416976)

Worrying if they can break Polar\_bear65

Alan Kaminsky •
[February 1, 2023 8:22 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416977)

> In all, the auditors cracked 18,174—or 21 percent—­of the 85,944 cryptographic hashes they tested

In other words, the auditors failed to crack 67,770—or 79 percent—of the hashes they tested. Over three-quarters of the passwords were too difficult to crack with a dictionary of “over 1.5 billion words”. A goodly percentage of the accounts would appear to be using strong passwords.

Bob Easton •
[February 1, 2023 8:27 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416978)

Hmmmm… an easily found “Password Strength Meter” says it will take 5 years to break ‘Polar\_bear65’ while this article states less than 90 minutes. Something doesn’t compute.

Ted •
[February 1, 2023 8:33 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416979)

@bert

> This is not true. Such an attack would be exponentially more difficult because today’s phone OSes are heavily sandboxed and you can’t just send a “notification to log in” if the user’s using passkeys.

I was referring to so called “passwordless authentication”. I’ve seen a small number of websites that you can login to simply by clicking a notification on another device, or by typing in a short code you received via text or email. In other cases it may require a biometric factor, such as scanning your face or fingerprint. Point is, people will still be tricked into giving access to hackers, and it won’t require a password.

PHP •
[February 1, 2023 8:49 AM](https://www.schneier.com/blog/archives/2023/02/passwords-are-terrible-surprising-no-one.html/#comment-416980)

A standard old Nvidia 1080 graphics card can bruteforce NTLM hashes at a rate that allows me to try all possible upper/lower/numeric in less than an hour. Newer cards are way faster.

Now, when you have tried that, then hashcat supports rulesets, dictionaries etc, using that with a few dictionaries and rules describing different word separators, numeric postfix etc, then you can quickly geta bit further. And keep adding the found passwords to the new wordlist.

MFA works to some degree. Yubikeys are fine for admins – they ensure end to end validation.

But SMS, Authenticator App, Passwordless etc is pretty bad. Here a real-time Monkey in the middle phisher can do a login on the backside, and get access and renewal tokens that are valid for maybe 30 days – maybe even longer. And the user will not know.

If the hacke...