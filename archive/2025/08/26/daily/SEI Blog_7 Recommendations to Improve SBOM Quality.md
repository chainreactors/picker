---
title: 7 Recommendations to Improve SBOM Quality
url: https://www.sei.cmu.edu/blog/7-recommendations-to-improve-sbom-quality/
source: SEI Blog
date: 2025-08-26
fetch_date: 2025-10-07T00:49:22.457230
---

# 7 Recommendations to Improve SBOM Quality

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
4. 7 Recommendations to Improve SBOM Quality

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Tobar, D., Jamieson, J., Priest, M., and Fricke, J., 2025: 7 Recommendations to Improve SBOM Quality. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 3, 2025, https://doi.org/10.58012/mb9a-kk12.

Copy

APA Citation

Tobar, D., Jamieson, J., Priest, M., & Fricke, J. (2025, August 25). 7 Recommendations to Improve SBOM Quality. Retrieved October 3, 2025, from https://doi.org/10.58012/mb9a-kk12.

Copy

Chicago Citation

Tobar, David, Jessie Jamieson, Mark Priest, and Jason Fricke. "7 Recommendations to Improve SBOM Quality." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, August 25, 2025. https://doi.org/10.58012/mb9a-kk12.

Copy

IEEE Citation

D. Tobar, J. Jamieson, M. Priest, and J. Fricke, "7 Recommendations to Improve SBOM Quality," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 25-Aug-2025 [Online]. Available: https://doi.org/10.58012/mb9a-kk12. [Accessed: 3-Oct-2025].

Copy

BibTeX Code

@misc{tobar\_2025,
author={Tobar, David and Jamieson, Jessie and Priest, Mark and Fricke, Jason},
title={7 Recommendations to Improve SBOM Quality},
month={{Aug},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/mb9a-kk12},
note={Accessed: 2025-Oct-3}
}

Copy

# 7 Recommendations to Improve SBOM Quality

![David Tobar](/media/images/thumb_big_d-tobar_blog_authors_.max-180x180.format-webp.webp)
![Jessie Jamieson](/media/images/Jamieson_Jessie_010_240919.max-180x180.format-webp.webp)

###### [David Tobar](/authors/david-tobar), [Jessie Jamieson](/authors/jessie-jamieson), [Mark Priest](/authors/mark-priest), and [Jason Fricke](/authors/jason-fricke)

###### August 25, 2025

##### PUBLISHED IN

[Software Engineering Research and Development](/blog/topics/software-engineering-research-development/)

##### CITE

<https://doi.org/10.58012/mb9a-kk12>

Get Citation

##### SHARE

A software bill of materials (SBOM) provides transparency into the elements of an integrated software product. Such transparency is critical to identifying system vulnerabilities and thus mitigating potential security risks. There is growing interest in using SBOMs to support software supply chain risk management. In September 2024 Army leaders signed [a memorandum requiring SBOMs for vendor-supplied software](https://api.army.mil/e2/c/downloads/2024/09/26/36c0ec0e/asaalt-software-bill-of-materials-policy-signed.pdf). More recently, the Department of Defense (DoD) Chief Information Officer, through its Software Fast Track Program, is requiring [that software vendors submit their SBOMs, as well as those from third-party assessors](https://defensescoop.com/2025/06/09/katie-arrington-swft-software-fast-track/), to enable detection of variances between SBOMs for the same software.

Different SBOM tools should produce similar records for a piece of software at a given point in its lifecycle, but this is not always the case. The divergence of SBOMs for individual pieces of software can undermine confidence in these important documents for software quality and security. This blog post outlines our team’s recent findings on why SBOMs diverge and recommends seven ways to improve SBOM accuracy.

## **SBOM Harmonization Plugfest**

The SEI’s [2024 SBOM Harmonization Plugfest](https://resources.sei.cmu.edu/news-events/events/sbom/) project, sponsored by the Cybersecurity and Infrastructure Security Agency (CISA), aimed to uncover the root causes of SBOM divergence, such as imprecise definitions or standards, how uncertainty is addressed, or other implementation decisions. The SEI brought together SBOM tool vendors, standards producers, and others in the SBOM community to produce sample SBOMs for analysis. The recently released [*Software Bill of Materials (SBOM) Harmonization Plugfest 2024*](https://insights.sei.cmu.edu/documents/6302/SBOM_Harmonization_Plugfest_2024.pdf), on which this post is based, outlines our team’s findings, analysis, and recommendations to help SBOM producers generate more consistent and reliable SBOMs.

We asked Plugfest participants to generate and submit SBOMs based on nine software targets chosen as a representative sample of various programming languages as seen in Table 1 below.

[![table1_fifthtry_08252025](/media/images/table1_fifthtry_08252025.max-1280x720.format-webp.webp)](/media/images/table1_fifthtry_08252025.original.png)

The SEI gained approval from most participants to make their submissions public. Those SBOMs that were approved for release are [now available at SEI’s GitHub site](https://github.com/cmu-sei/sbom-plugfest-2024).

**Overview and Analysis of Submitted SBOMs**

We received 243 SBOMs from 21 Plugfest participants. To ensure anonymity and to prevent any bias in our review, we anonymized participant names by assigning alphanumeric codes to each. One participant, who was assigned the code Y2, submitted many more SBOMs (102) than all the others (Figure 1). Y2 generated and submitted SBOMs in every format their tool supported (i.e., source and binary analysis as well as enriched and non-enriched).

[![figure1_08252025](/media/images/figure1_08252025.max-1280x720.format-webp.webp)](/media/images/figure1_08252025.original.png)

Figure 1: SBOMs Submitted per Target

**Analysis**

To ensure an objective analysis, we first determined evaluation criteria for our review of the SBOMs. We then determined automated approaches to extract information from the SBOMs to facilitate our development of software tools for analysis as well as our generation of baseline SBOMs, which we used for comparison purposes.

**Evaluation Criteria**

Assessing the consistency of the minimum elements of the submitted SBOMs was a critical component in determining their completeness and accuracy. A list of minimum elements specifies the baseline SBOMs should meet and facilitates information sharing. The criteria we used for minimum elements are those required for documenting a software product’s primary component and its included components as outlined in CISA’s [*Framing Software Component Transparency: Establishing a Common Software Bill of Materials (SBOM)*](https://www.cisa.gov/sites/default/files/2024-10/SBOM%20Framing%20Software%20Component%20Transparency%202024.pdf):

* SBOM Author Name
* SBOM Timestamp
* SBOM Type
* SBOM Primary Component
* Component Name
* Component Version String
* Component Supplier Name
* Component Cryptographic Hash
* Component Unique Identifier
* Component Relationships
* Component License
* Component Copyright Holder

**Analysis Tools**

Due to the many submissions, we developed tools to automate ingesting and processing SBOMs to collect, collate, and export data about them. Participants submitted SBOMs in SPDX and CycloneDX formats in a variety of encodings including JSON, XML, and YML.

We wrote code for processing SBOMs using Python within Jupyter computational notebooks hosted on an SEI internal Bitbucket repository, which also contained a copy of SBOM Plugfest submissions. We used two primary notebooks for analyzing SBOM submissions: one for CycloneDX and one for SPDX. We sought to extract the following from each SBOM:

* information related to the presence or absence of minimum elements
* information about software components, including their relationships to one another and with the target software

In each notebook, we collected info...