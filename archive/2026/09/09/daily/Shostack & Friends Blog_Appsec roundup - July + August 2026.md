---
title: Appsec roundup - July + August 2026
url: https://shostack.org/blog/appsec-roundup-july-aug-2026/
source: Shostack & Friends Blog
date: 2026-09-09
fetch_date: 2026-09-10T06:51:36.936276
---

# Appsec roundup - July + August 2026

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Appsec roundup - July + August 2026

Shostack + Friends Blog

# Appsec roundup - July + August 2026

The CRA, how AI is showing up in security requirements, threat modeling, bug fixing and inventing biases in its spare time. Also, a lot of cool books by other authors.
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot holds up the jigsaw puzzle, and snow is falling inside the library](/images/blog/img/2025/appsec-roundup-aug-2025-1000w.png)

This end of summer edition leads off with the EU’s release of
 [83
pages of guidance for the CRA](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation):
> Article 26(1) of the CRA requires the Commission to publish guidance to assist
> economic operators in applying the Regulation, with a particular focus on facilitating
> compliance by microenterprises and small and medium-sized enterprises (SMEs).
> Article 26(2) sets out minimum aspects that should be addressed in the guidance.
> These include: (i) the scope of the CRA (particularly remote data processing solutions
> and free and open-source software); (ii) the notion of ‘support periods’; (iii) the
> interplay between the CRA and other EU legislation; and (iv) the concept of
> ‘substantial modification.’

### Threat Modeling

* In [Trust Boundary Semantic Gaps: A Multi-dimensional
  Analysis and Mitigation for Security-by-Design](https://arxiv.org/abs/2607.01711), Doyeon Kim,
  Jin-Young Choi, Junghee Lee propose a set of analyses modules,
  including Identity, Spatial, Temporal, and Interpretation. The
  work is thought provoking. (I would have liked for them to have
  stayed away from the math long enough to distinguish the types of
  artifacts they mention, including software packages which are not like
  inputs, messages or tokens, none of which are expected to be executed.)
* In [An Empirical Evaluation of Generative AI in Security Requirements Engineering and Threat Modeling](https://www.semanticscholar.org/paper/An-Empirical-Evaluation-of-Generative-AI-in-and-Martins-Venson/6346903d3a9e236bedb9f060bd57e75625746cb7), F. Martins and Elaine Venson discuss how to use generative AI
  to support requirements engineering.

### Appsec

* Google released a blog post [How we’re making Chrome and the web safer in the AI Era](https://blog.google/security/chrome-stronger-with-every-update/),
  which includes, but isn’t limited to threat modeling, still done
  by humans and recorded in security.md files.
* In [Overhead of Recording Feature Locations with
  Embedded Annotations](https://se.rub.de/wp-content/uploads/2026/07/2026-variability-overhead.pdf), Johan Martinson, Kevin Hermann,
  and Thorsten Berger show that lightweight annotations that define
  where features are help find feature-related code. (There’s security
  relevance in knowing where your security features show up in the code.)

### AI

* In [AI is more likely than humans to form biases when hiring](https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/),
  Michelle Kim reports on a study that shows LLM hiring agents can
  literally invent new biases.
* In an April pre-print, Nicholas Sofroniew and colleagues of
  Anthropic report on [Emotion Concepts and their Function in a Large Language
  Model](https://arxiv.org/abs/2604.07729). Do you really want to spend the tokens they sell you
  on that, or have your outputs impacted by it?
* Dan Goodin has a story, [Mythos attack on
  3rd-round PQC algorithm candidate puts
  it out of commission](https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/). Key facts
  include 60 hours of work and $100,000
  of tokens. (It's unclear if that was
  the only work that was done, or if
  there were other, unsuccessful
  experiments, which would change the
  token cost, perhaps
  dramatically.) Cryptographer Matt
  Green has good analysis in [Some thoughts about Anthropic’s new cryptanalysis results](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/).* Axel Mierczuk, Spencer Michaels and Keith Hoodlet of
    1Password’s new Off-by-1 Labs released [Frontier Models’ Vulnerability Patches are Often
    F.L.A.W.E.D.](https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf). This study is pretty devastating to the hope that
    LLMs can fix the deluge of vulns they discover. Adrian Sanabria
    has a great summary in [Reviewing initial research on using AI for
    vulnerability remediation](https://www.defendersinitiative.com/p/reviewing-initial-research-on-using?r=74yjk&utm_campaign=post&utm_medium=web&triedRedirect=true). Contrast with Google’s opinion in
    [Stronger with every update: How we’re making
    Chrome and the web safer in the AI Era](https://blog.google/security/chrome-stronger-with-every-update/), and note the
    important words “At this point, we have LLMs generating
    *candidate fixes for most vulnerabilities*, dramatically
    increasing the rate of security fixes in recent Chrome
    releases” (emphasis added).
  * I covered the [OpenAI/HuggingFace incident](https://shostack.org/blog/lessons-from-openai-huggingface-ai-security/) separately.

### Operations

* In [Disasters for Small Teams](https://third-bit.com/2026/07/25/disaster/), Dr. Greg Wilson presents
  reasonably compact advice on disaster planning.

### Regulation

* Christian Espinosa has a good article [Your Penetration Test Can Pass And Still Fail FDA Review](https://www.forbes.com/councils/forbestechcouncil/2026/07/27/your-penetration-test-can-pass-and-still-fail-fda-review/) on
  the importance of testing the right things for FDA review. I
  think his points will generalize to other testing such as CRA.

---

### Books and Games Received

![books and games received](/images/blog/img/2026/appsec-roundup-july-aug-books-games-700w.png)

* [The C4 Model: Visualizing Software Architecture](https://www.amazon.com/gp/product/B0GC5YKYFD) by Simon
  Brown
* [The Psychology of Software Teams](https://www.amazon.com/Psychology-Software-Teams-Cat-Hicks/dp/1032963387) by Cat Hicks
* [Building Safer Technology: A Field Guide to Failing Well](https://www.amazon.com/Building-Safer-Technology-Field-Failing/dp/0135589320)
  by
  Yonatan Zunger, Lea Kissner, Neil Coles, Juan Hernandez, Harmony
  Mabrey, and Phillip Misner.
* [Threat-Driven Software Development: Defending
  online services from modern threat actors](https://www.amazon.com/Threat-Driven-Software-Development-Defending-services/dp/0135567386)  by Michael Howard,
  Lee Holmes, Sherrod DeGrippo, and Shawn
  Hernan. (Purchased as ebook).
* [The vCISO Playbook: How Virtual CISOs Deliver Enterprise-Grade
  Cybersecurity to Small and Medium Businesses (SMBs)](https://www.amazon.com/vCISO-Playbook-Enterprise-Grade-Cybersecurity-Businesses/dp/1966415044)  by Peter
  Green and Jan Ross.
* [Cards Against Vulnerabilities](https://www.appsecvillage.com/events/dc-2026/cards-against-vulnerabilities-1276050) by Patrick
  Smyth of Chainguard.
* The second version of Bob Lord’s Secure by Design storyca...