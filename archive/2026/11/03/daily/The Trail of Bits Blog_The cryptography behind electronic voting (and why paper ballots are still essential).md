---
title: The cryptography behind electronic voting (and why paper ballots are still essential)
url: https://blog.trailofbits.com/2026/11/03/the-cryptography-behind-electronic-voting-and-why-paper-ballots-are-still-essential/
source: The Trail of Bits Blog
date: 2026-11-03
fetch_date: 2026-11-04T08:17:40.958923
---

# The cryptography behind electronic voting (and why paper ballots are still essential)

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The cryptography behind electronic voting (and why paper ballots are still essential)

[Fredrik Dahlgren](/authors/fredrik-dahlgren/)

November 03, 2026

[cryptography](/categories/cryptography/), [privacy](/categories/privacy/), [zero-knowledge](/categories/zero-knowledge/)

Page content

* [The challenges of electronic voting](#the-challenges-of-electronic-voting)
* [Inside the design and cryptographic safeguards of electronic voting systems](#inside-the-design-and-cryptographic-safeguards-of-electronic-voting-systems)
  + [Protecting voter privacy](#protecting-voter-privacy)
  + [Protecting against a compromised voting client](#protecting-against-a-compromised-voting-client)
  + [Protecting against a compromised backend](#protecting-against-a-compromised-backend)
  + [What cryptography solves that paper ballots can’t do alone: end-to-end verifiability](#what-cryptography-solves-that-paper-ballots-cant-do-alone-end-to-end-verifiability)
* [We won’t be replacing paper ballots any time soon](#we-wont-be-replacing-paper-ballots-any-time-soon)

As millions of Americans vote in today’s U.S. midterms, most will use paper ballots, which are protected by strict chain-of-custody protocols and, in some cases, statistical audits. You may wonder why we still use paper for our elections and voting systems when tasks like banking, tax filing, and document signing have moved away from paper-based legacy systems and become fully electronic. The short answer: security.

That may come as a surprise to some. After all, cryptography and other security advancements have enabled secure electronic systems for many applications. In fact, cryptography can be used to provide two essential safeguards in elections: keeping (1) individual votes secret while (2) making the final tally independently verifiable. This is exactly the approach of cryptographic protocols like [Helios](https://vote.heliosvoting.org/) and [ElectionGuard](https://electionguard.vote/). However, Helios intentionally targets lower-risk and lower-coercion settings rather than high-stakes public elections. ElectionGuard, by contrast, is intended for public elections, but not as a replacement for a paper-based system; it is used as a cryptographic layer integrated with traditional voting infrastructure.

In this blog post, we’ll explain how cryptographic techniques can help protect ballot secrecy and prevent manipulation in electronic voting systems, and explore the limitations of these systems. Although cryptography can strengthen election verifiability and have other strong security properties, it cannot fully replace the security and trust of existing paper ballot systems in general elections.

## The challenges of electronic voting

The National Academy of Sciences’ excellent [2018 report](https://www.nationalacademies.org/read/25120) on election security concludes that electronic ballot return (also known as online voting or internet voting) **should not be used in general elections**, since *“no known technology guarantees the secrecy, security, and verifiability of a marked ballot transmitted over the Internet.”*

The difficulty of this problem makes sense when you consider the strong security guarantees any election system requires:

1. Voter privacy must be maintained, even if a voter has a financial incentive to disclose their vote to a third party.
2. Ballot integrity must be maintained. This becomes especially challenging in the electronic setting because, in general, the voter does not hold a cryptographic identity and cannot sign their ballot cryptographically. Oh, and the electronic voting client and server may be compromised anyway.
3. Voters shouldn’t be able to vote more than once, but this is hard to verify without associating votes with their voters. This becomes even more challenging electronically when, again, voters often lack a digital cryptographic identity.
4. Everyone should be able to trust (and ideally verify) that the election result correctly reflects the voters’ intent.

Paper-based voting systems must solve these problems, too. The first three requirements are typically met through standard physical security measures you see in paper ballot election locations: voters identify themselves to polling workers (preventing multiple votes from one person), are given a ballot without their name on it and a secure location to fill it in (protecting voter privacy), and personally hand their ballot to a polling worker and watch as their ballot is submitted for counting (ballot integrity). As with any security controls, there are threats that can compromise these protections; however, compromising them at a nationwide scale is extremely expensive, difficult, and noisy (i.e., detectable) to election observers, making these controls especially effective for large national elections. The final requirement is the most difficult to achieve for paper-based systems, and voters typically have to trust that election workers compute the final tallies honestly, and that chain-of-custody controls coupled with post-election audits would detect any attempt to compromise the election outcome. Cryptography can be used in conjunction with paper-based systems to help strengthen the trust in this final requirement, using what’s known as end-to-end verifiability, as we will explore later in the post.

Electronic systems introduce an existentially dangerous failure mode not present in modern, sensible paper-based systems: a supply-chain or 0-day vulnerability that can scale across many voting machines and jurisdictions could allow one person to single-handedly control and influence the outcome of an election (and, depending on the system and exact vulnerability, possibly while evading detection). In traditional paper-based systems, this risk is sharply constrained by independent physical records and physical security controls. It’s much more difficult for a single person to meaningfully change an election’s outcome while evading detection in this system.

Software security alone is not enough to secure electronic voting systems, though; the key design principle is not only to implement robust security controls but also to design your system so that all failures of those controls are detectable. This can’t be solved only using software whose correctness must be trusted. This property is known as [software independence](https://en.wikipedia.org/wiki/Software_independence): changes in the election outcome caused by changes or errors (or vulnerabilities) in voting software must be detectable. In practice, this is typically achieved using evidence that can be verified independently of the voting software, such as a paper ballot audit trail.

## Inside the design and cryptographic safeguards of electronic voting systems

Now that we’ve introduced the challenges of electronic voting, let’s explore how modern system designs aim to address them. We will focus our discussion on two electronic voting systems in particular: Helios and ElectionGuard. Helios is a complete voting protocol that targets low-stakes elections where coercion is not a concern. Famously, it is used by the International Association for Cryptologic Research to [elect its board of directors](https://iacr.org/elections/). ElectionGuard aims to provide end-to-end verifiability on top of existing election infrastructure, and has been tested alongside systems based on paper ballots in [College Park Maryland](https://electionguard.vote/elections/College_Park_Maryland_2023/), [Preston Idaho](https://electionguard.vote/elections/Preston_Idaho_2022/), and [Fulton Wisconsin](https://electionguard.vote/elections/Fulton_Wisconsin_2020/). Let’s look at how these systems use cryptography to provide voter privacy, ballot integrity, and end-to-end verifiability.

### Protecting voter privacy

Encryption is a natural choice ...