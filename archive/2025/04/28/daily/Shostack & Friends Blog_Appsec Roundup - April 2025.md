---
title: Appsec Roundup - April 2025
url: https://shostack.org/blog/appsec-roundup-april/
source: Shostack & Friends Blog
date: 2025-04-28
fetch_date: 2025-10-06T22:04:52.036695
---

# Appsec Roundup - April 2025

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
3. Appsec Roundup - April 2025

Shostack + Friends Blog

# Appsec Roundup - April 2025

Threat modeling. So much threat modeling, and so much more, including foreshadowing of new rules from FDA.
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-feb-25-1000w.png)

### Threat Modeling

* Threat Modeling Connect has [new in person groups](https://www.threatmodelingconnect.com/).
* There’s a new human harms focused threat modeling approach, covered in an academic paper, [Threat Me Right: A Human HARMS Threat Model for Technical Systems](https://arxiv.org/html/2502.07116v1).
* Linwood Jones and Pawan Suresh blogged about [Scaling Your Threat Modeling Program using GenAI](https://medium.com/adobetech/scaling-your-threat-modeling-program-using-genai-934160279889) at Adobe. I’d appreciate hearing about ‘what could go wrong’ and ‘what they did about those things.’
  (From September, but I’d missed it.)
* In January, CISA (along with DARPA, NSA and DoD) released [Closing the Software Understanding Gap](https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-closing-the-software-understanding-gap-508c.pdf). “Understanding” is interesting as a framing, but I think some of what they want is ‘understand the software’ and another part is ‘control what the software can do,’ and they might do well by reducing that ambiguity.
* The UK’s Ministry of Defense released a [Secure by Design Problem Book](https://www.gov.uk/government/publications/secure-by-design-problem-book) (The [announcement](https://www.gov.uk/government/publications/secure-by-design-problem-book) has context.)
* Matt Blaze testified about [CALEA and Salt Typhoon](https://oversight.house.gov/wp-content/uploads/2025/04/Blaze-Written-Testimony.pdf). He says “while the legally-mandated CALEA capability requirements have changed little over the last three decades, the infrastructure that must implement and protect it has changed radically.” This is useful as a lens into “keeping threat models up to date.” The changes happened over *decades*. Most of our processes aren’t designed to work on those sorts of scales: we rely on people and their memories.

### Appsec

* Lauren Zabierek and Bob Lord have both left CISA. I appreciate all the hard work they did, and hope that the incredible international team they built continues the important work. (Posts on Linkedin from [Lauren](https://www.linkedin.com/posts/laurenz1010_after-an-incredible-journey-at-cisa-i-have-activity-7320101011182800896-3c8B), [Bob](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7320094582770216960/).)
* [SOSecure: Safer Code Generation with RAG and StackOverflow Discussions](https://arxiv.org/abs/2503.13654) is an academic paper that builds a security knowledgebase from Stack Overflow, and delivers fix rates from 71% to 96%, depending on the evaluation.

### LLM Security

* [Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) is a fascinating paper by a team from Google and ETH Zurich. [Simon Willison has a good discussion](https://simonwillison.net/2025/Apr/11/camel/). I agree with Simon, this is a very important development. I have lots of questions about completeness of coverage, what security properties we can expect, and impact on LLM quality for metrics other than security, but none of those take away from the fact that this is the first time someone has published a principled way to address code/data confusion in LLMs.

### Regulation

* According to Estee Orani, [FDA has made a major announcement](https://www.linkedin.com/posts/esteeorani_medcon-medicaldevices-fdacompliance-activity-7321528786380902400-6mQy?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAABXB8Bi8nzcKtYJy26uPQJtELAN8sgDB4) that “Quality System Inspection Technique (QSIT) - that trusted roadmap for FDA inspections since 1999 - will be retired completely. No "QSIT 2.0" is coming. Instead, inspection processes aligned with ISO 13485:2016” will be rolled out. (FDA often previews plans like this before formal announcements, I don’t have a perspective on how official this might be, and there’s no skepticism in thread.)

### Shostack + Associates updates

* Adam will be co-presenting with Tanya Janca at RSA: [Red Teaming AI: 50 Years of Failure, But This Time, For Sure! - [IAIS-R03]](https://path.rsaconference.com/flow/rsac/us25/FullAgenda/page/catalog/session/1726704719721001RWjL).
* Adam and Erik will be training at [OWASP Global Appsec Barcelona](https://owasp.glueup.com/event/owasp-global-appsec-eu-2025-123983/training.html) (May 27-28), and seats are roughly half-gone.
* Adam will be giving the opening talk at [ThreatModCon Barcelona](https://www.threatmodelingconnect.com/events/threatmodcon-2025-barcelona), right after OWASP Global Appsec.* Adam will be training at Blackhat USA, [Aug 2-3](https://www.blackhat.com/us-25/training/schedule/#adam-shostacks-threat-modeling-intensive-44283) and [4-5](https://www.blackhat.com/us-25/training/schedule/#adam-shostacks-threat-modeling-intensive-442831736891193).

![A training card for Barcelona](/images/blog/img/2025/appsec-bcn-scotty-640w.png)

Image by Midjourney: “a photograph of a robot, sitting in a library, working on a jigsaw puzzle”

Originally published by Adam on 27 Apr 2025

Categories:
  [application security](/blog/category/application-security)
  [software engineering](/blog/category/software-engineering)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-aug-2025-175w.png)](/blog/appsec-roundup-sept-2025/)

### [Secure By Design roundup - September 2025](/blog/appsec-roundup-sept-2025/)

01 Oct 2025

The secret service, the CSRB, the CMMC, Sept was pretty busy in government. Plus Apple's Memory Integrity and a nice short paper on prompt-based attacks.

[![Thumbnail for podcast episode](/im...