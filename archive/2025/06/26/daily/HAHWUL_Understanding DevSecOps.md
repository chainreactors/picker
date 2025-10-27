---
title: Understanding DevSecOps
url: https://www.hahwul.com/sec/secure-sdlc/devsecops/
source: HAHWUL
date: 2025-06-26
fetch_date: 2025-10-06T22:52:53.084736
---

# Understanding DevSecOps

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/secure-sdlc/devsecops/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/secure-sdlc/devsecops/)

[한국어](https://www.hahwul.com/ko/sec/secure-sdlc/devsecops/)

JUNE 25, 2025

# Understanding DevSecOps

Sharing thoughts and approaches on DevSecOps, which integrates development (Dev), security (Sec), and operations (Ops) to embed security throughout the development lifecycle.

## What is DevSecOps?

DevSecOps is a culture and methodology that integrates security throughout the entire development cycle while maintaining DevOps speed. As a Red Team, the most ideal scenario is a service built securely from the start, with no vulnerabilities to exploit. DevSecOps offers a practical solution to achieve this.

In the past, security was often applied after development was complete, creating inefficiencies similar to tearing down walls in a finished building. DevSecOps solves this problem through the 'Shift Left' concept, moving security activities to earlier stages of development.

```
 graph TD
    A[Plan] --> B(Code);
    B --> C{Build};
    C --> D[Test];
    D --> E(Release);
    E --> F[Deploy];
    F --> G(Operate);
    G --> H{Monitor};
    H --> A;

    subgraph Security in All Phases
        direction LR
        S1[Threat Modeling] -- in --> A;
        S2[SAST / SCA] -- in --> B;
        S3[SAST] -- in --> C;
        S4[DAST / IAST] -- in --> D;
        S5[Config Scan] -- in --> F;
        S6[Runtime Security] -- in --> G;
    end
```

The key is automating and integrating security into every phase, from threat modeling at the planning stage to SAST during coding and DAST during testing.

## Why DevSecOps?

Speed is the essence. In CI/CD environments with multiple deployments per day, security performed after development completion becomes a bottleneck. DevSecOps automates security verification and integrates it into the pipeline, maintaining development speed while ensuring security. Here are examples of security activities and tools that can be applied at each SDLC stage:

* **Design**: Threat modeling (e.g., OWASP Threat Dragon)
* **Develop**: Real-time IDE scanning (e.g., SonarLint)
* **Build**: SAST (Static Analysis), SCA (Open Source Analysis) (e.g., SonarQube, dependency-check)
* **Test**: DAST (Dynamic Analysis) (e.g., OWASP ZAP)
* **Deploy**: IaC and container image scanning (e.g., Trivy, tfsec)

## How to measure maturity?

After implementing DevSecOps, measuring maturity and continuously improving is essential. The [OWASP DevSecOps Verification Standard (DSOVS)](https://github.com/OWASP/www-project-devsecops-verification-standard) provides a useful framework for this purpose.

DSOVS offers specific maturity assessment criteria across various domains including organization, design, and implementation, helping to diagnose current levels and design improvement roadmaps. For example, you can check items like:

* Do all team members receive regular security training? (ORG-002)
* Are security requirements defined and tracked during feature development? (REQ-002)
* Is threat modeling performed during architectural changes? (DES-002)
* Are security scans automated in the CI/CD pipeline? (IMP-003)
* Are penetration tests conducted regularly? (VER-002)

## Resources

![](/projects/devsecops/devsecops.jpg)
*I maintain the [hahwul/DevSecOps](https://github.com/hahwul/DevSecOps) project to organize and manage various related materials for personal reference.*

## Conclusion

The success of DevSecOps goes beyond tool adoption; it depends on cultural change. True value emerges when security becomes a shared responsibility of everyone creating the product, not just the job of a specific team.

The offensive perspective of a Red Team and the defensive approach of DevSecOps ultimately converge toward the same goal: creating secure services. I hope this article provides a small help in starting your DevSecOps journey.

[#devsecops](https://www.hahwul.com/tags/devsecops/)
[#security](https://www.hahwul.com/tags/security/)
[#devops](https://www.hahwul.com/tags/devops/)
[#automation](https://www.hahwul.com/tags/automation/)

[ ]

[ ]

### Table of Contents

[What is DevSecOps?](https://www.hahwul.com/sec/secure-sdlc/devsecops/#what-is-devsecops)

[Why DevSecOps?](https://www.hahwul.com/sec/secure-sdlc/devsecops/#why-devsecops)

[How to measure maturity?](https://www.hahwul.com/sec/secure-sdlc/devsecops/#how-to-measure-maturity)

[Resources](https://www.hahwul.com/sec/secure-sdlc/devsecops/#resources)

[Conclusion](https://www.hahwul.com/sec/secure-sdlc/devsecops/#conclusion)

[Next

Threat Modeling](https://www.hahwul.com/sec/secure-sdlc/threat-modeling/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/sec/secure-sdlc/devsecops/)
  + [한국어](https://www.hahwul.com/ko/sec/secure-sdlc/devsecops/)