---
title: A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems
url: https://insights.sei.cmu.edu/blog/a-5-stage-process-for-automated-testing-and-delivery-of-complex-software-systems/
source: SEI Blog
date: 2025-05-22
fetch_date: 2025-10-06T22:32:04.937103
---

# A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Milne, C., and Hughes, L., 2025: A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 4, 2025, https://doi.org/10.58012/mgfq-db98.

Copy

APA Citation

Milne, C., & Hughes, L. (2025, May 21). A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems. Retrieved October 4, 2025, from https://doi.org/10.58012/mgfq-db98.

Copy

Chicago Citation

Milne, Caden, and Lyndsi Hughes. "A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, May 21, 2025. https://doi.org/10.58012/mgfq-db98.

Copy

IEEE Citation

C. Milne, and L. Hughes, "A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 21-May-2025 [Online]. Available: https://doi.org/10.58012/mgfq-db98. [Accessed: 4-Oct-2025].

Copy

BibTeX Code

@misc{milne\_2025,
author={Milne, Caden and Hughes, Lyndsi},
title={A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems},
month={{May},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/mgfq-db98},
note={Accessed: 2025-Oct-4}
}

Copy

# A 5-Stage Process for Automated Testing and Delivery of Complex Software Systems

![Caden Milne](/media/images/cmilne.max-180x180.format-webp.webp)
![Headshot of Lyndsi Hughes](/media/images/lahughes.max-180x180.format-webp.webp)

###### [Caden Milne](/authors/caden-milne) and [Lyndsi A. Hughes](/authors/lyndsi-hughes)

###### May 21, 2025

##### PUBLISHED IN

[Continuous Deployment of Capability](/blog/topics/continuous-deployment-capability/)

##### CITE

<https://doi.org/10.58012/mgfq-db98>

Get Citation

##### SHARE

Managing and maintaining deployments of complex software present engineers with a multitude of challenges: security vulnerabilities, outdated dependencies, and unpredictable and asynchronous vendor release cadences, to name a few.

We describe here an approach to automating key activities in the software operations process, with focus on the setup and testing of updates to third-party code. A key benefit is that engineers can more quickly and confidently deploy the latest versions of software. This allows a team to more easily and safely stay up to date on software releases, both to support client needs and to stay current on security patches.

We illustrate this approach with a software engineering process platform managed by our team of researchers in the Applied Systems Group of the SEI’s CERT Division. This platform is designed to be compliant with the requirements of the [Cybersecurity Maturity Model Certification (CMMC)](https://insights.sei.cmu.edu/library/cybersecurity-maturity-model-certification-cmmc/) and [NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final). Each of the challenges above present risks to the stability and security compliance of the platform, and addressing these issues demands time and effort.

When system deployment is done without automation, system administrators must spend time manually downloading, verifying, installing, and configuring each new release of any particular software tool. Additionally, this process must first be done in a test environment to ensure the software and all its dependencies can be integrated successfully and that the upgraded system is fully functional. Then the process is done again in the production environment.

When an engineer’s time is freed up by automation, more effort can be allocated to delivering new capabilities to the warfighter, with more efficiency, higher quality, and less risk of security vulnerabilities. [Continuous deployment of capability](https://insights.sei.cmu.edu/continuous-deployment-capability/) describes a set of principles and practices that provide faster delivery of secure software capabilities by improving the collaboration and communication that links software development teams with IT operations and security staff, as well as with acquirers, suppliers, and other system stakeholders.

While this approach benefits software development generally, we suggest that it is especially important in high-stakes software for national security missions.

In this post, we describe our approach to using DevSecOps tools for automating the delivery of third-party software to development teams using CI/CD pipelines. This approach is targeted to software systems that are container compatible.

**Building an Automated Configuration Testing Pipeline**

Not every team in a software-oriented organization is focused specifically on the engineering of the software product. Our team bears responsibility for two sometimes competing tasks:

* Delivering valuable technology, such as tools for automated testing, to software engineers that enables them to perform product development and
* Deploying security updates to the technology.

In other words, delivery of value in the continuous deployment of capability may often not be directly focused on the development of any specific [product](https://cmu-sei.github.io/DevSecOps-Model/#Glossary__7478e27e-c57d-4bb6-8a57-445f662a7f55). Other dimensions of value include “[the people, processes, and technology necessary to build, deploy, and operate the enterprise’s products. In general, this business concern consists of the software factory and product operational environments; however, it does not consist of the products](https://insights.sei.cmu.edu/library/using-model-based-systems-engineering-mbse-to-assure-a-devsecops-pipeline-is-sufficiently-secure/).”

To improve our ability to complete these tasks, we designed and implemented a custom pipeline that was a variation of the traditional continuous integration/continuous deployment (CI/CD) pipeline found in many traditional DevSecOps workflows as shown below.

[![figure1_05202025](/media/images/figure1_05202025.max-1280x720.format-webp.webp)](/media/images/figure1_05202025.original.png)

Figure 1: The DevSecOps Infinity diagram, which represents the continuous integration/continuous deployment (CI/CD) pipeline found in many traditional DevSecOps workflows.

The main difference between our pipeline and a traditional CI/CD pipeline is that we are not developing the application that is being deployed; the software is typically provided by a third-party vendor. Our focus is on delivering it to our environment, deploying it onto our information systems, operating it, and monitoring it for proper functionality.

Automation can yield terrific benefits in productivity, efficiency, and security throughout an organization. This means that engineers can keep their systems more secure and address vulnerabilities more quickly and without human intervention, with the effect that systems are more readily kept compliant, stable, and secure. In other words, automation of the relevant pipeline processes can increase our team’s productivity, enforce security compliance, and improve the user experience for our software engineers.

There are, however, some potential negative outcomes when it is done incorrectly. It is important to recognize that because automation allows for many actions to be performed in quick succession, there is ...