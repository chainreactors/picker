---
title: Internet voting is insecure and should not be used in public elections
url: https://blog.citp.princeton.edu/2026/01/16/internet-voting-is-insecure-and-should-not-be-used-in-public-elections/
source: Instapaper: Unread
date: 2026-01-20
fetch_date: 2026-01-21T03:33:12.283445
---

# Internet voting is insecure and should not be used in public elections

[![](https://blog.citp.princeton.edu/wp-content/uploads/sites/952/2024/07/Group-3.png)](https://citp.princeton.edu)
[![CITP Blog - Formerly Freedom to Tinker](https://blog.citp.princeton.edu/wp-content/uploads/sites/952/2024/07/Group-2-1-300x102.png)](https://blog.citp.princeton.edu/)

[Log in](https://blog.citp.princeton.edu/wp-login.php?redirect_to=https%3A%2F%2Fblog.citp.princeton.edu%2F2026%2F01%2F16%2Finternet-voting-is-insecure-and-should-not-be-used-in-public-elections%2F)

Subscribe

Search

# Internet voting is insecure and should not be used in public elections

January 16, 2026

– by

[Andrew Appel](https://blog.citp.princeton.edu/author/andrew-appel/ "Posts by Andrew Appel")

[Comments](#respond)

[Voting](https://blog.citp.princeton.edu/category/voting/)

*Signed by a group of 21 computer scientists expert in election security*

## Executive summary

Scientists have understood for many years that internet voting is insecure and that there is no known or foreseeable technology that can make it secure. Still, vendors of internet voting keep claiming that, somehow, their new system is different, or the insecurity doesn’t matter. Bradley Tusk and his Mobile Voting Foundation keep touting internet voting to journalists and election administrators; this whole effort is misleading and dangerous.

**Part I.**  All internet voting systems are insecure. The insecurity is worse than a well-run conventional paper ballot system, because a very small number of people may have the power to change any (or all) votes that go through the system, without detection. This insecurity has been known for years; every internet voting system yet proposed suffers from it, for basic reasons that cannot be fixed with existing technology.

**Part II.** Internet voting systems known as “End-to-End Verifiable Internet Voting” are also insecure, in their own special ways.

**Part III.**  Recently, Tusk announced an E2E-VIV system called “VoteSecure.”  It suffers from all the same insecurities.  Even its developers admit that in their development documents.  Furthermore, VoteSecure isn’t a complete, usable product, it’s just a “cryptographic core” that someone might someday incorporate into a usable product.

**Conclusion.**  Recent announcements by Bradley Tusks’s Mobile Voting Foundation suggest that the development of VoteSecure somehow makes internet voting safe and appropriate for use in public elections.  This is untrue and dangerous.  All deployed Internet voting systems are unsafe, VoteSecure is unsafe and isn’t even a deployed voting  system, and there is no known (or foreseeable) technology that can make Internet voting safe.

## Part I.  All internet voting systems are insecure

Internet voting systems (including vote-by-smartphone) have three very serious weaknesses:

1. Malware on the voter’s phone (or computer) can transmit different votes than the voter selected and reviewed. Voters use a variety of devices (Android, iPhone, Windows, Mac) which are constantly being attacked by malware.
2. Malware (or insiders) at the server can change votes. Internet servers are constantly being hacked from all over the world, often with serious results.
3. Malware at the county election office can change votes (in those systems where the internet ballots are printed in the county office for scanning). County election computers are not more secure than other government or commercial servers, which are regularly hacked with disastrous results.

Although conventional ballots (marked on paper with a pen) are not perfectly secure either, the problem with internet ballots is the ability for a single attacker (from anywhere in the world) to alter a very large number of ballots with a single scaled-up attack.  That’s much harder to do with hand-marked paper ballots; occasionally people try large-scale absentee ballot fraud, typically resulting in their being caught, prosecuted, and convicted.

## Part II.  E2E-VIV internet voting systems are also insecure

Years ago, the concept of “End-to-End Verifiable Internet Voting” (E2E-VIV) was proposed, which was supposed to remedy some of these weaknesses by allowing voters to check that their vote was recorded and counted correctly.  Unfortunately, all E2E-VIV systems suffer from one or more of the following weaknesses:

1. Voters must rely on a computer app to do the checking, and the checking app (if infected by malware) could lie to them.
2. Voters should not be able to prove to anyone else how they voted – the technical term is “receipt-free” – otherwise an attacker could build an automated system of mass vote-buying via the internet. But receipt-free E2E-VIV systems are complicated and counterintuitive for people to use.
3. It’s difficult to make an E2E-VIV checking app that’s both trustworthy and receipt-free. The best solutions known allow checking only of votes that will be discarded, and casting of votes that haven’t been checked; this is highly counterintuitive for most voters!
4. The checking app must be separate from the voting app, otherwise it doesn’t add any malware-resistance at all.  But human nature being what it is, only a tiny fraction of voters will do the extra steps to run the checking protocol.  If hardly anyone uses the checker, then the checker is largely ineffective.
5. Even if some voters do run the checking app, if those voters detect that the system is cheating (which is the purpose of the checking app), there’s no way the voters can prove that to election officials.  That is, there is no “dispute resolution” protocol that could effectively work.

Thus, the problem with all known E2E-VIV systems proposed to date is that the “verification” part doesn’t add any useful security: if a few percent of voters use the checking protocol and see that the system is sometimes cheating, the system can still steal the votes of all the voters that don’t use the checking protocol. And you might think, “well, if some voters catch the system cheating, then election administrators can take appropriate action”, but no appropriate action is possible: the election administrator can’t cancel the election just because a few voters claim (without proof) that the system is cheating!  That’s what it means to have no dispute resolution protocol.

All of this is well understood in the scientific consensus. The insecurity of non-E2E-VIV systems has been documented for decades.  For a survey of those results, see “[Is Internet Voting Trustworthy? The Science and the Policy Battles](https://scholars.unh.edu/unh_lr/vol21/iss2/9/)”. The lack of dispute resolution in E2E-VIV systems has been [known for many years as well](http://www2.seas.gwu.edu/~poorvi/Audiotegrity.pdf).

## Part III. VoteSecure is insecure

Bradley Tusk’s [Mobile Voting Foundation](https://www.mobilevoting.org/) contracted with the R&D company [Free and Fair](https://freeandfair.us/about/) to develop internet voting software. Their [press release of November 14, 2025](https://www.prnewswire.com/news-releases/the-mobile-voting-foundation-and-free--fair-release-votesecure-the-first-software-development-kit-for-secure-transparent-and-verifiable-mobile-voting-302615896.html) announced the release of an [open-source “Software Development Kit”](https://github.com/FreeAndFair/VoteSecure) and claimed “This technology milestone means that secure and verifiable mobile voting is within reach.”

After [some computer scientists examined](https://github.com/FreeAndFair/VoteSecure/issues/2#issue-3629697747) the open-source VoteSecure and [described serious flaws in its security](https://blog.citp.princeton.edu/2025/12/16/mobile-voting-projects-vote-by-smartphone-has-real-security-gaps/), Dr. Joe Kiniry and Dr. Daniel Zimmerman of Free and Fair responded. They say, in effect, that all the critiques are accurate, but they don’t know a way to do any better: “[We share many of [the critique’s] core goals, including voter confidence, election integrity, and resistance to coercion. Where we...