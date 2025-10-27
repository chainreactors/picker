---
title: Threat Modeling the Genomic Data Sequencing Workflow (Threat Model Thursday)
url: https://shostack.org/blog/threat-modeling-the-genetic-sequencing-workflow/
source: Shostack & Friends Blog
date: 2025-02-14
fetch_date: 2025-10-06T20:36:01.683366
---

# Threat Modeling the Genomic Data Sequencing Workflow (Threat Model Thursday)

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Threat Modeling the Genomic Data Sequencing Workflow (Threat Model Thursday)

Shostack + Friends Blog

# Threat Modeling the Genomic Data Sequencing Workflow (Threat Model Thursday)

An exciting new sample TM from MITRE
![A subsection of a dataflow diagram](/images/blog/img/2025/threat-modeling-the-genetic-sequencing-workflow-1000w.png)

For Threat Model Thursday, I want to provide some comments on [NIST CSWP 35 ipd, Cybersecurity Threat Modeling the Genomic Data Sequencing Workflow (Initial Public Draft)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.35.ipd.pdf). As always, my goal is to offer helpful feedback.

This is a big, complex document. It’s 50 pages of real content with 13 listed authors, and is a subset of [a larger project](https://www.nccoe.nist.gov/projects/cybersecurity-and-privacy-genomic-data). The official goal is to “demonstrate how to conduct cybersecurity threat modeling...(L148; In this post, I’ll use L to refer to lines, and § to refer to sections.) The draft officially follows the Four Question Framework, and is.. big and maybe intimidating. One question I had is “is NIST setting the bar for a published threat model too high?” In other words, could a simpler threat model serve some of the same purposes? The apparent complexity is exacerbated by the intermingling of ‘how to conduct’ with ‘sample output’ and perhaps the document might be improved by breaking it into two: a ‘how to’ guide and a ‘sample output’ document or documents. Overall, this is one of the more interesting public threat modeling documents.

I’m concerned that this threat modeling is implicitly operationally focused, essentially taking as given many development and operational choices that may have been made at this point. I don’t see, for example, an evaluation of the security of two different sequencing machines and a choice being made, or a consideration of alternatives to ‘Globus’ for file transfer. This may be realistic, but is a choice that should be discussed.

### Context

I believe that the “we” in this document is generally a “Genomic Sequencing Lab” and the “research partners” are the lab’s untrusted and untrustworthy customers, but I’m not sure.

The document has an interesting mix of a lot of detail, and a lot of references which imply “we could have done more.” What makes this level of detail right for this document? I’d like to see an explicit discussion, and statements that much lighter threat modeling could be appropriate.

* Why do “organizations” need to ‘select appropriate cyber capabilities’ (L207)? Why aren’t those built-in, and why are the sequencers not secure by design?
* How should organizations go about considering its goals and priorities (L209)? There’s a set of objectives in Table 1, why can’t an organization just use those? Please give specific advice (there is some, perhaps call forward to it.)
* How should the organization periodically assess its cyber posture (L211)? How does that activity differ from what’s in this guide?
* The discussion of threats, risks and how those apply to specific organizations (§ 1.3) is **excellent**. The example of a dos threat being high impact for a disease surveillance lab, and low impact to an agricultural researcher is great.
* Building on that, the need to publish threat models so organizations can manage risks (L247-249) reminds me of Loren Kohnfelder’s recent essay, [Flaunt Your Threat Models](https://designingsecuresoftware.com/writings/flaunt/), and I think what the authors here are saying is that full threat models need to be either shared with prospects or published.
* I think reference 7 is pointing to the wrong thing; the best cite is [11]. (L253)
* The relationship between threats, risks, and possible mitigations as described starting at L272 is really good, it could be even better if the guide (or a related document) assessed how it does in relation to the needs of various stakeholders.

### What are we working on

Generally, the set of diagrams doesn’t match the FDA
pre-market’s Guidance, which requires a multi-patient harm view and security
use case view(s). I think there’s a case that there’s no need for
a multi-patient harm view, but the absence should be discussed. I’m unsure
if any of the diagrams are intended to act as security use case views.

* When discussing how “answering question 1 helps teams identify activities and language (L297),” I have several comments:
  + There’s an interplay of journey and reward here, perhaps separate them?
  + Perhaps start from the concrete. “When we answer question 1, we create models, in the forms of diagrams and explanatory or contextualizing text..”
  + The language in L298-300 assumes that threat modeling is done on a completed system, not as part of creating it.
  + That para also seems to imply that threat modeling is done by outsiders to the system.
* The idea of High Value Dataflows (L305) is fascinating. At first introduction, I noted “bad — assumes answers.” This is partially addressed in §2.1.3, with a specific list of reasons things are highlighted. There’s an implicit leap to ‘these things can go wrong,’ which is not bad, sometimes we know, but does marking these take attention away from other subsystems?
* Table 2 should show the HVD dataflow element, and the doc should show an example of a HVD right there. The next diagram (Figure 3) doesn’t use HVDs, which led me to wonder if there lines were sufficiently differentiated.
* Please also add stick figure external entities to Table 2 since they’re used in Fig 4 and beyond.
* I find Figure 3 hard to read. The elements are all differently sized, there’s no apparent rationale to placement, and I don’t know what the SaaS/PaaS components mean. I’d like to see the lab components grouped on the left in a labeled “lab” boundary. (We read both text and diagrams left to right and top to bottom.)
* In general, the diagrams are not easy to read. Elements move around arbitrarily between diagrams (for example, in Fig 3, Manufacturers are at 11 o’Clock relative to the wet lab, but when that diagram is expanded (without any ‘See Figure 4’ in Fig 3), it’s now at 2 o’clock.
* The discussion of trust in external entities (L412-421) is interesting, but what should the reader do with that information?
* The process description at L495 could be substantially more secure. Consider changing it to an outbound request to the manufacturer, and having the binary file be signed and the signature validated.
* L582, if Globus treats encryption as optional in the year 2025, NIST should select a more secure example to reference, such as scp.

### What can go wrong

* The discussion of STRIDE at L613 is good, but somewhat contradicted by the decision (L637) to categorize each threat, a step which I don’t see as worth the effort. A very small nit, I might call it “A STRIDE methodology,” since there are several, such as STRIDE per element or the EoP deck.
* L624 discusses “improving brainstorming.” I consider brainstorming to be unstructured, and so thinking that STRIDE improves things confuses things by breaking an inherent property of brainstorming.
* I like the table in Figure 16, and often use similar ones, with th...