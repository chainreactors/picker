---
title: Modeling Services with Model-Based Systems Engineering (MBSE)
url: https://www.sei.cmu.edu/blog/modeling-services-with-model-based-systems-engineering-mbse/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-10-28
fetch_date: 2025-10-29T03:16:21.450802
---

# Modeling Services with Model-Based Systems Engineering (MBSE)

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. Modeling Services with Model-Based Systems Engineering (MBSE)

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Shevchenko, N., and Shevchenko, G., 2025: Modeling Services with Model-Based Systems Engineering (MBSE). Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 29, 2025, https://doi.org/10.58012/ypyv-8m83.

Copy

APA Citation

Shevchenko, N., & Shevchenko, G. (2025, October 28). Modeling Services with Model-Based Systems Engineering (MBSE). Retrieved October 29, 2025, from https://doi.org/10.58012/ypyv-8m83.

Copy

Chicago Citation

Shevchenko, Nataliya, and Grigoriy Shevchenko. "Modeling Services with Model-Based Systems Engineering (MBSE)." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, October 28, 2025. https://doi.org/10.58012/ypyv-8m83.

Copy

IEEE Citation

N. Shevchenko, and G. Shevchenko, "Modeling Services with Model-Based Systems Engineering (MBSE)," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 28-Oct-2025 [Online]. Available: https://doi.org/10.58012/ypyv-8m83. [Accessed: 29-Oct-2025].

Copy

BibTeX Code

@misc{shevchenko\_2025,
author={Shevchenko, Nataliya and Shevchenko, Grigoriy},
title={Modeling Services with Model-Based Systems Engineering (MBSE)},
month={{Oct},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/ypyv-8m83},
note={Accessed: 2025-Oct-29}
}

Copy

# Modeling Services with Model-Based Systems Engineering (MBSE)

![Nataliya Shevchenko](/media/images/thumb_big_n-shevchenko_blog_aut.max-180x180.format-webp.webp)
![Headshot of Greg Shevchenko](/media/images/Shevchenko_Greg_006_240919.max-180x180.format-webp.webp)

###### [Nataliya Shevchenko](/authors/nataliya-shevchenko) and [Greg Shevchenko](/authors/greg-shevchenko)

###### October 28, 2025

##### PUBLISHED IN

[Model-Based Systems Engineering](/blog/topics/model-based-systems-engineering/)

##### CITE

<https://doi.org/10.58012/ypyv-8m83>

Get Citation

##### SHARE

[Model-based systems engineering (MBSE)](/blog/an-introduction-to-model-based-systems-engineering-mbse/) continues to show [robust growth](https://www.businessresearchinsights.com/market-reports/model-based-systems-engineering-mbse-market-120951) in adoption driven by increased digital transformation efforts within our government as well as boosted adoption by [industry](https://www.globalgrowthinsights.com/market-reports/model-based-systems-engineering-mbse-tools-market-103917). One area specifically benefiting from MBSE adoption is enterprise architecture (EA). In a previous post, [*Modeling Capabilities with Model-Based Systems Engineering (MBSE)*](/blog/modeling-capabilities-with-model-based-systems-engineering-mbse/), we discussed one of the EA domains—capabilities, and the benefits of modeling them. In this blog post, we explore another domain of EA, the usage of services as an architectural concept that provides a method for successful alignment of business and IT entities.

Modeling services will help practicing business-, enterprise-, and solution-architects present groups of functionalities through the lens of a service-oriented architecture. System engineers can also use the concepts of services in their capabilities breakdown and further architectural analysis.

This post explores an approach to designing services using MBSE with [OMG’s](https://www.omg.org/) [Unified Architecture Framework (UAF)](https://www.omg.org/uaf/) in general and, in services modeling, with UAF’s Services Viewpoint. We show services as an abstraction layer that connects capabilities, operational activities, and underlying software solutions. Modeling the relationship between services and these types of objects may reveal the need for additional decomposition of the analyzed services, capabilities, and operational activities. Service modeling can lead to the discovery of existing functional gaps or duplication of the purchased and/or deployed software. In this post, we will demonstrate that a decomposition of services clearly distinguishes between service interfaces and functions.

## **The Role of Services in Architecture Decomposition**

UAF defines services as “specifications required and provided service levels of these specifications that exhibit a Capability or support an Operational Activity” (Figure 1).

[![Figure1_10282025](/media/images/Figure_1_kyx59fF.max-1280x720.format-webp.webp)](/media/images/Figure_1_kyx59fF.original.png)

Figure 1: UAFML Service Definition

Service specifications define objects that are able to perform specific business functions, processes, transactions, or operations. For example, a customer relationship management (CRM) tool can be modeled as a service responsible for managing customer profiles, contact management, customer behavior trending for sales campaigns, etc. The CRM service may assist in sending customized notes, play the role of a collaboration and communication tool for cross-functional teams, provide analytics on customer preferences, and many other ongoing activities.

[![figure2_10282025](/media/images/Figure_2_sHd23FU.max-1280x720.format-webp.webp)](/media/images/Figure_2_sHd23FU.original.png)

Figure 2: Customer Relationship Management Service

The CRM service shown in Figure 2 can perform “Send Customized Note” and “Provide Customer Preferences” activities that represent daily business operations and exhibits two capabilities. A real-world model would reveal more complex structure matching services to capabilities as well as business requirements.

[![Figure_3](/media/images/Figure_3_oP9skxw.max-1280x720.format-webp.webp)](/media/images/Figure_3_oP9skxw.original.png)

Figure 3: Matching CRM Service to Requirements

For example, as shown in Figure 3, service specifications can include high-level business requirements related to process automation, report generation, or access control. Now the CRM service can be traced to the business requirements it is supposed to satisfy, to ensure the completeness of the service specification using a dependency diagram, as shown in Figure 4 below.

[![Figure4_10282025](/media/images/Figure_4_Cfu59Qa.max-1280x720.format-webp.webp)](/media/images/Figure_4_Cfu59Qa.original.png)

Figure 4: CRM Service Requirements

Once the service is matched to the identified capabilities and known requirements, any existing systems or evaluated platforms can be brought into the models as resources implementing the service.

[![Figure5_10282025](/media/images/Figure_5.max-1280x720.format-webp.webp)](/media/images/Figure_5.original.png)

Figure 5: Tools and Platforms Implementing CRM Service

The CRM tool of choice may not include all required capabilities. It may be augmented with business intelligence systems, messaging services, planning tools, etc.

A dependency diagram, similar to Figure 6, can be built to trace the resources the service was related to. This type of diagram can demonstrate all services, including redundant platforms, as well as any gaps in the modeling or analysis. Figure 6 shows that Pipedrive and Salesflare have not been traced to the CRM service.

[![Figure6_10282025](/media/images/Figure_6.max-1280x720.format-webp.webp)](/media/images/Figure_6.original.png)

Figure 6: Resources Implementing the CRM Service

On the other hand, services may be implemented by more than one tool, and one tool may offer various capabilities...