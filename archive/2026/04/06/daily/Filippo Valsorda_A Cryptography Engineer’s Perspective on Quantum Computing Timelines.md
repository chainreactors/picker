---
title: A Cryptography Engineer’s Perspective on Quantum Computing Timelines
url: https://words.filippo.io/crqc-timeline/
source: Filippo Valsorda
date: 2026-04-06
fetch_date: 2026-04-07T04:24:56.824336
---

# A Cryptography Engineer’s Perspective on Quantum Computing Timelines

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

6 Apr 2026

# A Cryptography Engineer’s Perspective on Quantum Computing Timelines

My position on the urgency of rolling out quantum-resistant cryptography has changed compared to just a few months ago. You might have heard this privately from me in the past weeks, but it’s time to signal and justify this change of mind publicly.

There had been rumors for a while of expected and unexpected progress towards cryptographically-relevant quantum computers, but over the last week we got two public instances of it.

First, [Google published a paper revising down dramatically the estimated number of logical qubits and gates required to break 256-bit elliptic curves](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) like NIST P-256 and secp256k1, which makes the attack doable in minutes on fast-clock architectures like superconducting qubits. They weirdly[1](#fn:goofy) frame it around cryptocurrencies and mempools and salvaged goods or something, but the far more important implication are practical WebPKI MitM attacks.

Shortly after, [a different paper came out from Oratomic showing 256-bit elliptic curves can be broken in as few as 10,000 physical qubits if you have non-local connectivity](https://arxiv.org/abs/2603.28627), like neutral atoms seem to offer, thanks to better error correction. This attack would be slower, but even a single broken key per month can be catastrophic.

They have this excellent graph on page 2 (*Babbush et al.* is the Google paper, which they presumably had preview access to):

![graph of physical qubit cost over time](https://assets.buttondown.email/images/c768727d-01a9-4f44-919b-bab3c84cb81d.png?w=960&fit=max)

Overall, it looks like everything is moving: the hardware is getting better, the algorithms are getting cheaper, the requirements for error correction are getting lower.

I’ll be honest, I don’t actually know what all the physics in those papers means. That’s not my job and not my expertise. My job includes risk assessment on behalf of the users that entrusted me with their safety. What I know is what at least some actual experts are telling us.

Heather Adkins and Sophie Schmieg [are telling us](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) that “quantum frontiers may be closer than they appear” and that **2029** is their deadline. That’s in 33 months, and no one had set such an aggressive timeline until this month.

Scott Aaronson [tells us](https://scottaaronson.blog/?p=9425) that the “clearest warning that [he] can offer in public right now about the urgency of migrating to post-quantum cryptosystems” is a vague parallel with how nuclear fission research stopped happening in public between 1939 and 1940.

The timelines presented at RWPQC 2026, just a few weeks ago, were much tighter than a couple years ago, and are already partially obsolete. The joke used to be that quantum computers have been 10 years out for 30 years now. Well, not true anymore, the timelines have started progressing.

If you are thinking “well, this could be bad, or it could be nothing!” I need you to recognize how **immediately dispositive** that is. The bet is not “are you 100% sure a CRQC will exist in 2030?”, the bet is “are you 100% sure a CRQC will NOT exist in 2030?” I simply don’t see how a non-expert can look at what the experts are saying, and decide “I know better, there is in fact < 1% chance.” Remember that you are betting with your users’ lives.[2](#fn:audience)

Put another way, even if the most likely outcome was no CRQC in our lifetimes, that would be completely irrelevant, because our users don’t want just better-than-even odds[3](#fn:odds) of being secure.

Sure, papers about an abacus and a dog are funny and can make you look smart and contrarian on forums. But that’s not the job, and those arguments [betray a lack of expertise](https://bas.westerbaan.name/notes/2026/04/02/factoring.html). As Scott Aaronson [said](https://scottaaronson.blog/?p=9665#comment-2029013):

> Once you understand quantum fault-tolerance, asking “so when are you going to factor 35 with Shor’s algorithm?” becomes sort of like asking the Manhattan Project physicists in 1943, “so when are you going to produce at least a small nuclear explosion?”

The job is not to be skeptical of things we’re not experts in, the job is to mitigate credible threats, and there are credible experts that are telling us about an imminent threat.

In summary, it might be that in 10 years the predictions will turn out to be wrong, but at this point they might also be right soon, and that risk is now unacceptable.

## Now what

Concretely, what does this mean? It means we need to ship.

Regrettably, we’ve got to roll out what we have.[4](#fn:lattices) That means **large ML-DSA signatures** shoved in places designed for small ECDSA signatures, like X.509, with the exception of Merkle Tree Certificates for the WebPKI, which is thankfully [far enough along](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html).

This is *not* the article I wanted to write. I’ve had a pending draft for months now explaining we should ship PQ key exchange now, but take the time we still have to adapt protocols to larger signatures, because they were all designed with the assumption that signatures are cheap. That other article is now wrong, alas: we don’t have the time if we need to be finished by 2029 instead of 2035.

For key exchange, the migration to ML-KEM is going well enough but:

1. Any **non-PQ key exchange** should now be considered a potential active compromise, worthy of warning the user [like OpenSSH does](https://www.openssh.org/pq.html), because it’s very hard to make sure all secrets transmitted over the connection or encrypted in the file have a shorter shelf life than three years.
2. We need to forget about **non-interactive key exchanges (NIKEs)** for a while; we only have KEMs (which are only unidirectionally authenticated without interactivity) in the PQ toolkit.

It makes no more sense to deploy **new schemes that are not post-quantum**. I know, pairings were nice. I know, everything PQ is annoyingly large. I know, we had basically *just* figured out how to do ECDSA over P-256 safely. I know, there might not be practical PQ equivalents for threshold signatures or identity-based encryption. Trust me, I know it stings. But it is what it is.

**Hybrid classic + post-quantum authentication makes no sense** to me anymore and will only slow us down; we should go straight to pure ML-DSA-44.[6](#fn:44) Hybrid key exchange is reasonably easy, with ephemeral keys that don’t even need a type or wire format for the composite private key, and a couple years ago it made sense to take the hedge. Authentication is not like that, and even with [draft-ietf-lamps-pq-composite-sigs-15](https://www.ietf.org/archive/id/draft-ietf-lamps-pq-composite-sigs-15.html) with its 18 composite key types nearing publication, we’d waste precious time collectively figuring out how to treat these composite keys and how to expose them to users. It’s also been two years since Kyber hybrids and we’ve gained significant confidence in the Module-Lattice schemes. Hybrid signatures cost time and complexity budget,[5](#fn:poor) and the only benefit is protection if ML-DSA is classically broken *before the CRQCs come*, which looks like the wrong tradeoff at this point.

In **symmetric encryption**, we don’t need to do anything, thankfully. There is a common misconception that protection from Grover requires 256-bit keys, but [that is based on an exceedingly simplified understanding of the algorithm](https://words.filippo.io/post-quantum-age/#128-bits-are-enough). A more accurate characterization is that with a circuit depth of 2⁶⁴ logical gates (the approximate num...