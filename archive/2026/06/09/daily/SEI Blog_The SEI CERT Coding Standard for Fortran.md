---
title: The SEI CERT Coding Standard for Fortran
url: https://www.sei.cmu.edu/blog/the-sei-cert-coding-standard-for-fortran/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-06-09
fetch_date: 2026-06-10T06:17:11.632786
---

# The SEI CERT Coding Standard for Fortran

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. The SEI CERT Coding Standard for Fortran

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Svoboda, D., 2026: The SEI CERT Coding Standard for Fortran. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed June 9, 2026, https://doi.org/10.58012/w9t7-6y96.

Copy

APA Citation

Svoboda, D. (2026, June 9). The SEI CERT Coding Standard for Fortran. Retrieved June 9, 2026, from https://doi.org/10.58012/w9t7-6y96.

Copy

Chicago Citation

Svoboda, David. "The SEI CERT Coding Standard for Fortran." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, June 9, 2026. https://doi.org/10.58012/w9t7-6y96.

Copy

IEEE Citation

D. Svoboda, "The SEI CERT Coding Standard for Fortran," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 9-Jun-2026 [Online]. Available: https://doi.org/10.58012/w9t7-6y96. [Accessed: 9-Jun-2026].

Copy

BibTeX Code

@misc{svoboda\_2026,
author={Svoboda, David},
title={The SEI CERT Coding Standard for Fortran},
month={{Jun},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/w9t7-6y96},
note={Accessed: 2026-Jun-9}
}

Copy

# The SEI CERT Coding Standard for Fortran

![Headshot of David Svoboda.](/media/images/Svoboda_David_22_230926.360x360.max-180x180.format-webp.webp)

###### [David Svoboda](/authors/david-svoboda)

###### June 9, 2026

##### PUBLISHED IN

[Security Vulnerabilities](/blog/topics/security-vulnerabilities/)

##### CITE

<https://doi.org/10.58012/w9t7-6y96>

Get Citation

##### SHARE

*This blog post is coauthored by Manuel Arenaz, lead contributor of the Fortran standard.*

As security specialists, we are often asked to audit software and provide expertise on secure coding practices. Our research and efforts have produced several coding standards specifically dealing with security in popular programming languages, such as C, Java, and C++. This post describes our work on the [SEI CERT Fortran Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/), which provides a core of well-documented and enforceable coding guidelines for [Fortran](https://fortran-lang.org/).

## Fortran in the Modern Software Ecosystem

Fortran is one of the oldest high-level programming languages still in active use and remains a cornerstone of scientific, engineering, and high-performance computing (HPC) software. On the [TIOBE Index from May 2026](https://www.tiobe.com/tiobe-index/), Fortran was the 11th most-used programming language. Since the widely adopted Fortran 77 (F77) standard, the language has continuously evolved through major revisions, including Fortran 90, 95, 2003, 2008, 2018, and the recent Fortran 2023 standard, introducing modern features for modularity, interoperability, parallelism, and software engineering.

Fortran continues to power critical applications in areas such as climate and weather prediction, aerospace, nuclear energy, computational physics, and national security. Prominent Fortran-based applications include the [U.S. Navy’s NEPTUNE weather-prediction model](https://www.nrl.navy.mil/Portals/38/NRL%20Fact%20Sheet%20NEPTUNE%20dec2022.pdf), the [LS-DYNA finite-element solver](https://www.ansys.com/products/structures/ansys-ls-dyna) for structural and crash simulations, and [BLAS](https://www.netlib.org/blas/)/[LAPACK](https://www.netlib.org/lapack/) numerical linear algebra libraries widely used in scientific computing.

As these traditionally isolated scientific and HPC applications become increasingly integrated into modern, interconnected software ecosystems, the exposure of Fortran codebases to cybersecurity threats and software supply chain risks has significantly increased. In response, the Fortran community has shown growing interest in secure software development practices, vulnerability prevention, and secure coding standards. Recent efforts include the publication of [ISO/IEC TR 24772-8 on avoiding vulnerabilities in Fortran](https://j3-fortran.org/doc/year/23/23-241.pdf) and the emergence of static and software composition analysis tools targeting Fortran applications.

In addition, the recent emergence of specialized static analysis tools for Fortran now enables developers to provide an automated audit of a Fortran codebase by examining source code and producing diagnostic alerts that range from insecure coding practices and bugs to reliability and maintainability issues. These capabilities, comparable to those long available for C and C++, provide a practical foundation for modern secure software development in Fortran.

The SEI CERT Fortran Coding Standard is still young and growing. The C and Java standards each have more than 100 rules in over 15 sections. The Fortran standard currently has 25 guidelines, initially organized in several sections including:

* [Arrays (ARR)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/arrays-arr/)
* [Attribute Declarations and Specifications (ADS)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/attribute-declarations-and-specifications-ads/)
* [Concurrency (CON)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/concurrency-con/)
* [Types (TYP)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/types-typ/)
* [Procedures (PRC)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/procedures-prc/)
* [Scope, Association, and Definition (SAD)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/scope-association-and-definition-sad/)
* [Miscellaneous (MSC)](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/miscellaneous-msc/)

## **Addressing Security Vulnerabilities in Fortran**

Fortran shares many programming concepts and low-level capabilities with C and C++, including procedural programming, manual memory management, interoperability with external libraries, and performance-oriented design. At the same time, Fortran provides several features that are particularly well-suited for scientific and high-performance computing, including intrinsic multidimensional array operations, native array slicing and whole-array syntax, built-in support for numerical computation, explicit parallel programming constructs, and language-level facilities for efficient vectorization and mathematical optimization.

Historically, the [Fortran community](https://fortran-lang.org/) has focused on new features and improved performance rather than security. Our work on the [SEI CERT Fortran Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-fortran-coding-standard/) centers on Fortran language and library issues that specifically address security, such as implicit declaration of variables, use of uninitialized variables, undefined behavior, out-of-bounds memory accesses, and proper argument checking.

The SEI CERT Fortran Coding Standard leverages the team’s knowledge of Fortran and several sources to provide relevant material on security. These include online resources such as the security and reliability checkers documented in the [Codee Open Catalog](https://github.com/codee-com/open-catalog) and existing rules from the [SEI CERT C Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standa...