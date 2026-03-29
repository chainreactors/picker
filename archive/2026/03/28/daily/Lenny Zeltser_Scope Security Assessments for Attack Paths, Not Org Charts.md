---
title: Scope Security Assessments for Attack Paths, Not Org Charts
url: https://zeltser.com/security-assessment-scope/
source: Lenny Zeltser
date: 2026-03-28
fetch_date: 2026-03-29T04:42:39.982517
---

# Scope Security Assessments for Attack Paths, Not Org Charts

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Scope Security Assessments for Attack Paths, Not Org Charts

When assessment scope follows organizational lines, gaps open where team boundaries meet and real attackers don't stop. Pulling adjacent teams into the scoping conversation and following attack logic closes those gaps.

![Scope Security Assessments for Attack Paths, Not Org Charts - illustration](/assets/boundary-rope.b99m14on_OcRka.webp)

If scoped correctly, pentests and other security assessments address compliance requirements and improve defenses. However, determining the project’s scope can be a challenge. If we define it too narrowly, we’ll miss vulnerabilities that a real attacker could’ve exploited. But if we go too broad, we inflate costs and put relationships at risk. These challenges intensify as organizations begin using AI for assessments, since agents can interpret rules of engagement more literally and operate faster than a human tester.

## See Where Scope Breaks Down

We often think of a security assessment in terms of an “application,” “infrastructure,” or “corporate” pentest because different teams maintain these resources. The funding comes from different budgets, and different people get stressed about the findings. As a result, our scoping decisions are anchored in “who’s responsible?” factors rather than “what can an attacker reach?”

Such constraints prevent the assessment from mimicking how real attackers operate. A pentest focused on corporate resources might target the identity management system. But it would stop short of following a weakly controlled admin account into the customer support environment, which is a different application, scoped for a separate pentest.

[Shared responsibility models](/distribute-cybersecurity-tasks) divide ownership across teams, so the assessment’s realistic scope spans multiple groups. Let’s say a pentest focused on a web application discovers that a service account has overly permissive cloud IAM permissions. This allows access to data stores, internal services, and production infrastructure well beyond the web app itself. Is that an application finding or a cloud infrastructure finding? The app team didn’t configure IAM, and the cloud team didn’t build the app. Which team might feel blamed for the issue? Which is responsible for getting it addressed?

A human tester who encounters ownership and scope uncertainties might take context into account and, when necessary, check with the client. An AI agent running the same assessment might push through the boundary or halt entirely, depending on how literally it interprets the scope statement. Either outcome creates problems that detailed upfront scoping could’ve prevented.

## Follow the Attack Logic

Political boundaries won’t disappear from security assessments scoped along budgetary or organizational lines. But with the right planning, we can still move the assessments closer to how attackers actually operate.

“Test what an attacker could reach starting from the web app” produces more realistic findings than “test the web app.” Attack-path language helps the assessment team flag what they discover at the edges, even when the formal scope can’t span every team’s resources.

Bring stakeholders from adjacent systems into the scoping conversation, not just the commissioning team and the provider. The scope doesn’t need to expand, but the people defining it should understand the systems the assessment might touch, so they aren’t surprised when findings reach their systems. These scoping conversations surface ownership disagreements before testing forces the issue, when they’re easier to resolve.

Upfront planning matters even more for AI-driven assessments. Technical boundaries such as systems, network segments, and data classifications translate into rules the agent can follow. Organizational boundaries, especially when they include political considerations, don’t. Agree on a plan with the teams involved, then translate it into operating procedures the AI agent can follow.

We can plan individual assessments across a year or multi-year cycle, so they collectively cover the threat model. Design intentional overlap where team boundaries meet. If the cloud infrastructure review examines the same service accounts a web app pentest touched, that overlap is a feature, not redundancy. Findings from one assessment inform the next one’s scope, building a feedback loop across engagements.

Assign a person or function to review findings across all assessments and route cross-boundary discoveries to the right teams. Without this, people will assume that someone else will handle them. These findings should trigger a defined workflow rather than an ad-hoc conversation about whose problem it is.

A scope statement is only as useful as the agreement behind it. Before your next security assessment, consider whether the people defining the scope understand what an attacker could reach, not just what the commissioning team owns. Shape that agreement around the attack paths, not the org chart.

More on

[Assessments](/topic/assessments)[Leadership](/topic/leadership)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm exploring what's next. As I work on independent projects, I'm open to CISO or security product leadership roles where technical depth enables business growth. To talk, reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name* at *my last name* dot com.

3 min to read

March 28, 2026

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

© 2026 Lenny Zeltser