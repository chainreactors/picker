---
title: Risk Management and Threat Modeling
url: https://shostack.org/blog/risk-management-and-threat-modeling/
source: Shostack & Friends Blog
date: 2025-07-22
fetch_date: 2025-10-06T23:28:54.194910
---

# Risk Management and Threat Modeling

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
3. Risk Management and Threat Modeling

Shostack + Friends Blog

# Risk Management and Threat Modeling

Threat modeling finds threats; risk management helps us deal with the tricky ones.
![a diagram showing that threat modeling leads to risk management when threats aren’t easily addressed.](/images/blog/img/2025/risk-management-and-threat-modeling@2x-1600w.png)

One the most common questions I’m asked is “what’s the relationship of
threat modeling to risk management?” The simple answer is that
threat modeling always precedes and sometimes feeds into risk
management. Let me offer simple definitions: A threat is a
possible future problem; a risk is a quantified threat. That
quantification often applies to likelihood or impact. “The bully
threatened to beat him up.” “There’s a 90% chance you’ll lose all
your money in this startup investment.”

In traditional risk management, the risks are known:
fire, flood, etc. That’s not the case with technical systems. We need ways
to figure out what the issues are, and frequently, the ‘thing we do about
them’ is to prevent them. We add defensive code and features to
make them less likely. For example, we add TLS to prevent
information disclosure in network flows, we add authentication
factors to bolster authentication. Many technical threats are
handled in normal engineering without needing formal risk
quantification.

Fire and flood have two other noteworthy properties. They’re
broader than many technical threats. We insure fire risk, not “you’re
using a penny in the fuse box.” Second, there’s usually a direct line
from those bad operational or design choices to the broadly-defined
risk. That line is easy to understand, and is covered in crisp
standards. In contrast, many threats go through a relatively abstract
“run code” stage and give attackers freedom to act. Both breadth and
direct relationships to outcomes are contributing factors to the
complex relationship between threats and risk, but for simplicity and
length, I’ll take them up another time.

We generally focus our engineering on making it impossible for
threats to manifest. This is
similar to how we build bridges. Bridge building doesn’t start
from risk management, but rather, we design a bridge that can
handle the anticipated loads and conditions, and then ensure that
“anticipated” is not constrained to “normal.” We do the same with
cars: We anticipate threats like collisions, turning too fast, and
we engineer them to be reasonably safe in those circumstances.

It’s common advice to develop risk assessments for executives, but
that’s a bad model of how decisions are made, which has the impact
that our risk work doesn’t help resolve debate about what to do.

### A model of executive decision making

Executives make decisions about how to best serve customers.
Different firms will frame this on profit, stock price, or other
value that comes from serving customers. Each of
their choices comes with uncertainty about the
likelihood and magnitude of the outcome.

When the investment is to secure things, those investments can
involve both foregone alternatives, and specific staff with
unique capabilities. Even there, the delivery risks (cost and
predictability of the engineering work) are often a larger
driver than cybersecurity risk.

Executive decision making is less “do this or nothing,” and more “do A or
B?” Those choices are dominated by what’s going to serve
customers. Passionate objections that executives ought to care about
risk don’t work, and that frustrates the bejeezus out of a lot of
security people.

This isn’t to say that executives won’t take security into account,
it’s to say that neither the language of risk or the work to quantify
risk will drive them. Making it inexpensive, including by reducing
re-work and interruption, can be more effective than saying “this is a
CVSS 9.4.”

### Risk matters when decisions are hard

Many threats are addressed as part of good engineering, but some
edge cases may need a formal risk approach to inform trade-offs.
When decisions are hard, executives may want more information
about “how likely is that,” or “how bad could it be?” Mature
companies have processes for risk assessment and risk management. I’ve
designed my threat modeling approaches to be neutral and feed into
those risk management methods,
whatever they are. Threat modeling feeds into risk, however your
organizations defines it. This is simple utilitarianism: The less we
change, the easier it can be to change.

Executives often want more information, and decision science
teaches us to estimate how sensitive the decision is (will it make a
difference?) and to assess how hard it is to gather.

Even when we gather some data, there are important limits to risk
management today. Both likelihood and impact assessments tend to
be contentious. [Update: and estimating, justifying or
debating cost both time and possibly goodwill.] It’s hard to link specific technical dangers to
eventual business outcomes.

### Risk matters when threats are unavoidable

There are a subset of threats that can’t be addressed fully
by engineering work. In a whitepaper, I described inherent threats,
and there are also threats where we want to take a “wait and see”
approach because addressing them may be expensive.

Even though it may be hard to assess likelihood or impact, making a
decision about an inherent risk is something executives will need
to do.

### Risk matters to regulators

All this said, the terms “cybersecurity” and “risk management” are
deeply intertwined. For example, one explanation of the [Cyber Resilience Act](https://www.cyberresilienceact.eu/compliance-matrix/) says:

> Manufacturers shall undertake an assessment of the
> cybersecurity risks associated with a product with digital
> elements and take the outcome of that assessment into account
> during the planning, design, development, production, delivery
> and maintenance phases of the product with digital elements
> with a view to minimising cybersecurity risks, preventing
> incidents and minimising their impact, including in relation
> to the health and safety of users.

The only way I see to “undertake an assessment of the
cybersecurity risks” is to create an “all up” threat
model. There really aren’t other ways to address planning and
design. Similarly, how are you going to take the outcomes into account without
additional threat modeling of features as you build them?

In closing, threat modeling helps us handle the everyday threats through
engineering and gives us the insight of when risk management may be helpful.

[Update, July 25: clarified that doing work is not free.]

Originally published by Adam on 21 Jul 2025

Last updated on 25 Jul 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
  [risk](/blog/category/risk)
  [science of risk management](/blog/category/science-of-risk-management)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/ca...