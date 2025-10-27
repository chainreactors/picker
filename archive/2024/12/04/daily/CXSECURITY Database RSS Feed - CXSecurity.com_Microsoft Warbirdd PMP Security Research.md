---
title: Microsoft Warbirdd PMP Security Research
url: https://cxsecurity.com/issue/WLB-2024120004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-04
fetch_date: 2025-10-06T19:36:55.382132
---

# Microsoft Warbirdd PMP Security Research

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Microsoft Warbirdd PMP Security Research** **2024.12.03**  Credit:  **[Adam Gowdiak](https://cxsecurity.com/author/Adam%2BGowdiak/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

```
# Microsoft Warbird and PMP security research
# (c) Security Explorations 2008-2024 Poland
# (c) AG Security Research 2019-2024 Poland
```
"...If you decide to make it public..., stress the fact that it is not a
security issue in PlayReady or any Microsoft technology; it's a security
issue in the STB" - Microsoft, Nov 2022
# INTRODUCITON
This package presents security analysis conducted with respect to Microsoft
Warbird and Protected Media Path technologies.
A more general description of the results obtained and their impact is
described at project web page:
```
https://security-explorations.com/microsoft-warbird-pmp.html
```
This document provides a more in-depth technical explanation, illustration and
verification of discovered attacks along toolsets used for their implementation.
We hope this document provides both important contribution along a valuable
perspective on the state of the art / security provided by PlayReady content
security technology (vide the nature of the issues uncovered / verification of
vendor's claims).
For a more complete picture, you are encouraged to get familiar with our prior
PlayReady research from 2022 (along associated technical doc):
```
https://security-explorations.com/microsoft-playready.html
```
## DISCLAIMER
The goal of this research is not to promote PayTV or VOD content piracy in any
way. It is to both increase awareness and trigger more work at vendor's end to
make PayTV / content piracy harder to accomplish.
The results obtained indicate that there is much space for the improvement
through better technical means.
Information in this document is provided purely for educational purposes only.
It is expressly forbidden to use them for any purposes that would violate any
domestic or international laws.
## ON MICROSOFT / SHARING OF THE RESEARCH
We believe the following is worth to mention regarding Microsoft. Please, keep
in mind that we have 28 years of experience when it comes to dealing with
various SW / HW vendors over security issues.
- contact with Microsoft Security Response Center has been a questionable
experience:
\* all messages are signed semi-anonymously (as MSRC), as a result one has
the impression of no accountability and anonymity, the experience is more
like talking to a customer service of a big retailer, not security contact
of a major SW vendor (other vendors we dealt with used real names),
\* MSRC responses are not prompt, simple confirmation of a successful download
/ decryption of a research material takes ~3 days for the company, this
doesn't look like 24/7 global team operations, this doesn't look like "we
take security issues seriously"
\* MSRC can occasionally lose the topic (doesn't do the basic work that could
clarify the context of a given message such as to ask internally employees
CCed), this creates the impression that responses get redacted or are sent
in a hurry / without due care
\* in 2019, Microsoft didn't respond to our inquiry, we didn't assume this
was intentional until cease of a communication, which took place in early
2023 (as a follow up of our inquiries regarding PlayReady security, which
hasn't been answered btw.)
- Microsoft claims that it rewards security research, well the devil lies in a
detail, more specifically:
\* `Microsoft Bounty Terms and Conditions` implicate commercial use with
unknown payment terms, all non-negotiable and under Microsoft control
\* there are no categories for PlayReady / content protection (there has never
been such categories),
\* our research didn't need to rely on any privilege elevation/kernel exploit
(direct base for no bug stance)
\* Microsoft claimed no bug at its end in 2022 (with above, solid rationale
for similar evaluation in 2024)
\* the company hasn't expressed / signaled any interest to discuss access to
this research on a fair and commercial basis (regulating conditions of IP
/ know-how use, mutual agreement on a price, etc.) for the last 8 months,
the company was well aware of research impact (PlayReady for Windows being
broken to pieces) along the amount of work it required
- Microsoft sort of played with us in 2022, which is hard to perceive in other
terms than disrespect, company's claims regarding fixing and taking the issue
seriously didn't reflect the reality, it took nearly 2 years to have the cert
confirmed by Microsoft as compromised to be revoked, it's even hard to think
of this action as revocation as the service got simply shut down, the company
avoided to admit that PlayReady might provide little or no security upon
client compromise, not much security improvements has been noticed since 2022
when we signaled the need for it (this research sort of proves it), this all
built solid base for no trust to the company at our end.
We decided to give Microsoft (a company consisting of 100,000+ SW engineers,
with access to all the know-how, internal docs and source codes) approx. the
same amount of time to fix / address the issues as it took us (a 1 man shop
relying on binaries and public info only) to analyze and reverse engineer the
technology, discover the issues, develop illustrating POCs and dedicated
toolsets.
We finally provided Microsoft with access to the complete research package
comprising of a technical document, all toolsets with sources and test data
(285MB ZIP file) on Nov 18, 2024 and free of any charge (exactly two weeks
prior to the planned disclosure and as agreed with the company).
But, Microsoft is only partly the winner here as its engineers likely failed
to locate / address the root cause of the issues over the recent 8 months (no
fixes / mitigations observed). That's quite a shame in our opinion. The other
source for the shame lies in the nature of the issues and attacks described
in this doc.
## PACKAGE DESCRIPTION
The package comprises of the following tools:
- `Warbird Reverse Engineering toolkit`
S...