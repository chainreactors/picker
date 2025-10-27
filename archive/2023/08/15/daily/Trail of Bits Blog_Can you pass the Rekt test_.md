---
title: Can you pass the Rekt test?
url: https://blog.trailofbits.com/2023/08/14/can-you-pass-the-rekt-test/
source: Trail of Bits Blog
date: 2023-08-15
fetch_date: 2025-10-04T12:01:54.672344
---

# Can you pass the Rekt test?

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Can you pass the Rekt test?

Trail of Bits

August 14, 2023

[blockchain](/categories/blockchain/), [conferences](/categories/conferences/), [guides](/categories/guides/), [policy](/categories/policy/)

One of the biggest challenges for blockchain developers is objectively assessing their security posture and measuring how it progresses. To address this issue, a working group of Web3 security experts, led by Trail of Bits CEO Dan Guido, met earlier this year to create a simple test for profiling the security of blockchain teams. We call it the Rekt Test.

The Rekt Test is modeled after [The Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/). Developed 25 years ago by software developer Joel Spolsky, The Joel Test replaced a Byzantine process for determining the maturity and quality of a software team with 12 simple yes-or-no questions. The blockchain industry needs something similar because today’s complex guidance does more to frustrate than to inform.

The Rekt Test focuses on the simplest, most universally applicable security controls to help teams assess security posture and measure progress. The more an organization can answer “yes” to these questions, the more they can trust the quality of their operations. This is not a definitive checklist for blockchain security teams, but it’s a way to start an informed discussion about important security controls.

At the Gathering of Minds conference earlier this year, a group of industry leaders were challenged to address the lack of cybersecurity standards in the blockchain ecosystem. One of these discussions was led by [Dan Guido](https://www.linkedin.com/in/danguido/), CEO of Trail of Bits. Other participants included [Nathan McCauley](https://www.linkedin.com/in/nathanmccauley/) (Anchorage Digital), [Lee Mount](https://www.linkedin.com/in/lee-mount-843541a9/) (Euler Labs), [Shahar Madar](https://www.linkedin.com/in/shahar-madar/) (Fireblocks), [Mitchell Amador](https://www.linkedin.com/in/mitchell-amador-a37683227/) (Immunefi), [Nick Shalek](https://www.linkedin.com/in/nickshalek/) (Ribbit Capital), and others. Through their discussions, the Rekt Test was created:

## **The Rekt Test**

1. *Do you have all actors, roles, and privileges documented?*
2. *Do you keep documentation of all the external services, contracts, and oracles you rely on?*
3. *Do you have a written and tested incident response plan?*
4. *Do you document the best ways to attack your system?*
5. *Do you perform identity verification and background checks on all employees?*
6. *Do you have a team member with security defined in their role?*
7. *Do you require hardware security keys for production systems?*
8. *Does your key management system require multiple humans and physical steps?*
9. *Do you define key invariants for your system and test them on every commit?*
10. *Do you use the best automated tools to discover security issues in your code?*
11. *Do you undergo external audits and maintain a vulnerability disclosure or bug bounty program?*
12. *Have you considered and mitigated avenues for abusing users of your system?*

The landscape of blockchain technology is diverse, extending beyond blockchains to include decentralized protocols, wallets, custody systems, and more, each with unique security nuances. The subsequent explanations of the Rekt Test questions reflect the consensus of best practices agreed to by this group, and are by no means exhaustive or absolute. The intent of the Rekt Test is not to establish rigid benchmarks but to stimulate meaningful conversations about security in the blockchain community. Thus, consider this interpretation as a stepping stone in this critical dialogue.

**1. Do you have all actors, roles, and privileges documented?**

Comprehensive documentation of all actors, roles, and privileges affecting the blockchain product is crucial, as this clarifies who can access system resources and what actions they are authorized to perform. Actors refer to entities interacting with the system; roles are predefined sets of permissions assigned to actors or groups; and privileges define specific rights and permissions.

Thorough documentation of these entities facilitates comprehensive testing, allowing developers (and external auditors) to identify security gaps, improper access controls, the degree of decentralization, and potential exposure in specific compromise scenarios. Addressing these issues enhances the overall security and integrity of the system. The documentation also serves as a reference point for auditors to compare the actual access privileges with the documented ones, identify any discrepancies, and investigate potential security risks.

**2. Do you keep documentation of all the external services, contracts, and oracles you rely on?**

Interactions with external smart contracts, oracles, and bridges are fundamental to many key functionalities expected from blockchain applications. A new blockchain application or service may also rely on the assumed security posture of a financial token developed outside of your organization, which increases its complexity and attack surface. As a result, even organizations that integrate the best security procedures into their software development process can fall victim to a destructive security incident.

It is crucial to document all external services (like cloud hosting services and wallet providers), contracts (like DeFi protocols), and oracles (like pricing information) used by a blockchain system in order to identify risk exposure and mitigate incident impact. Doing so will help you answer the following essential questions:

* How will we know when an external dependency suffers a security incident?
* What are the specific conditions under which we declare a security incident?
* What steps will we take when we detect one?

Answering these questions will help you be prepared when, inevitably, a security incident affects a dependency outside of your control. You should be able to notice any change, innocuous or not, in a dependency’s output, interface, or assumed program state; assess it for security impact; and take the necessary next steps. This will limit the security impact on your system and help ensure its uninterrupted operation.

**3. Do you have a written and tested incident response plan?**

While security in the blockchain space differs from traditional product security (where more centralized or closed systems may be easier to control), both require an effective incident response plan to help remain resilient in the face of a security incident. The plan should include steps to identify, contain, and remediate the incident through automated and manual procedures. An organization should provide training to ensure that all team members are familiar with the plan, and it should include steps for communicating incidents over internal *and* out-of-band channels. This plan should be regularly tested to ensure it is up-to-date and effective, especially given how quickly the blockchain security world can change. You should create your own incident response (IR) plan, and can use [this Trail of Bits guide](https://secure-contracts.com/development-guidelines/incident_response.html) as a resource.

For blockchain systems, it is especially important that IR plans mitigate key person risk by ensuring the organization is not overly reliant on any single individual. The plan should anticipate scenarios where key personnel may be unavailable or coerced, and outline steps to ensure continuity of operations. Developers should consider decentralizing access controls, implementing quorum-based approvals, and documenting procedures so that multiple team members are prepared to respond.

For blockchain systems, it is especially important that incident response be proactive, not only ...