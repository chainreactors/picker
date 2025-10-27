---
title: Microsoft Still Uses RC4
url: https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html
source: Schneier on Security
date: 2025-09-17
fetch_date: 2025-10-02T20:16:13.201159
---

# Microsoft Still Uses RC4

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

## Microsoft Still Uses RC4

Senator Ron Wyden has [asked](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf) the Federal Trade Commission to [investigate](https://cybersecuritynews.com/microsofts-use-of-outdated-rc4-encryption/) Microsoft over its continued use of the RC4 encryption algorithm. The letter talks about a hacker technique called [Kerberoasting](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/kerberoasting/), that exploits the Kerberos authentication system.

Tags: [algorithms](https://www.schneier.com/tag/algorithms/), [Microsoft](https://www.schneier.com/tag/microsoft/), [ransomware](https://www.schneier.com/tag/ransomware/), [RC4](https://www.schneier.com/tag/rc4/)

[Posted on September 16, 2025 at 7:06 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html) •
[11 Comments](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html#comments)

### Comments

Wayne •
[September 16, 2025 9:47 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447988)

I was reading about this last week and was quite surprised. Kind of amusing that the world is underpinned by MS, and it turns out it’s a deck of cards. I think a lot of us if asked in the ’90s about something like this, we might have said ‘Yeah, probably.’

Microsoft’s fix timetable really needs to be faster, now that this little disaster is known widely. I wonder what, if any, mitigations can be taken to defend against it.

Will Fiveash •
[September 16, 2025 10:11 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447989)

Dealing with a crypto algorithm used by Kerberos and found to be weak, as is the case with RC4 (or single DES, etc…), is non-trivial. Kerberos is used in widely deployed scenarios with a potential mix of OS’s (Solaris, Linux, Windows, macOS, etc…) which makes seamless migration of weak Kerberos enctypes (the crypto used by Kerberos) to stronger enctypes a real pain. If you get it wrong, authentication stops working and soon the sysadmins are hearing from all kinds of folks because they can’t get work done. I don’t envy MS software engineers working on these issues.

TimH •
[September 16, 2025 10:31 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447991)

Microsoft has form in allowing weaker encryptions. For Bitlocker, they removed the Elephant Diffuser PRNG, and the default is AES-128. Who’d know to change to AES-256 before FDE?

JR •
[September 16, 2025 11:13 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447994)

RC4, wow. They had an SSL cert that was signed with RC3 just a few years ago. It was used in their waagent that runs on Linux systems in Azure. Note there are several Azure environments. The env I was using was meant to be secure, but was the last to get any updates. They fixed the Cert in the public Azure and kept tellings us we were wrong,. Their agent wasn’t working correctly when the Linux machines where in FIPS mode.

Wannabe Techguy •
[September 16, 2025 11:48 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447995)

Why would any IT pro be surprised by anything M.S. does? With all the issues with Windoze updates,I’m not surprised with their low quality work(laziness?). And yet, people still trust them.

Clive Robinson •
[September 16, 2025 12:09 PM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-447996)

@ ALL,

Just a point to note…

RC4 is still a usable algorithm for a number of things including “Communications Whitening”(generating noise) and “for simulation”(like O’l Montie).

However RC4 has like many “simple card shuffling algorithms” passed beyond the point where it can be considered cryptographically secure even for you little sisters diary, now she keeps it on a computer…

I think it safe to say that all crypto algorithms outside of a special class will fall to this issue.

It’s just a matter of when not if.

Which of course brings up the issue of “embedded” and “grid” systems I’ve been mentioning for many years now…

KC •
[September 16, 2025 3:47 PM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-448004)

From the man who coined the term Kerberoasting in 2014, Tim Medin also responded to Wyden’s letter and gave Microsoft’s response a little undressing.

As Clive mentioned, AES-based Kerberos tickets are still susceptible to Kerberoasting. According to a benchmark that Tim ran, it was just that AES128 and AES256 tickets were approximately 350 and 700 times slower to crack.

<https://redsiege.com/blog/2025/09/kerberoasting-microsoft-and-a-senator/>

Blaziken •
[September 16, 2025 10:15 PM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-448017)

@Clive

> RC4 is still a usable algorithm for a number of things …

Agreed.

Similarly SHA-1 will always live on courtesy of Section 4.2.1.2 of RFC5280, but this should not pose a security issue as a hash collision could only cause trust path construction to fail and should not lead to incorrect certificate validation except in the most broken implementations.

Clive Robinson •
[September 17, 2025 4:42 AM](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html/#comment-448022)

@ KC, ALL,

With regards,

> “AES-based Kerberos tickets are still susceptible to Kerberoasting.”

And as far as I can work out it should actually be,

**“All ways will be…”**

This is due to fundamentals in the design (that also effect so many other systems[1]).

But consider, if you change those fundamentals then two things,

1, Not only will it not be Kerberos any more, it won’t be compatible.

These are things even technical people don’t want to talk about in what is one of the more widely deployed systems of it’s type in the world…

[1] It’s odd that I should be talking about this twice in as many days, but they do say,

“Random things tend to clump”

(Or is it humans 😉

People have to learn a number of painful exercises or suffer the potential consequences.

One such which comes up all to often is “Off line authentication”. The bottom line is to do any type of authentication you need a unique and unforgeable ID-Verifier pair so we have one variety we all know and hate, the all to recognisable “Username and password” and like bank card numbers and verifiers and the PIN number etc etc.

Whilst the ID can be public and often is the verifier should always be a,

“A shared secret”

And this implies not just that it should be unique and unforgeable, but importantly also held private from all but the necessary verification process.

If it’s not then,

“It’s game over.”

So, consider an actually quite common situation of...