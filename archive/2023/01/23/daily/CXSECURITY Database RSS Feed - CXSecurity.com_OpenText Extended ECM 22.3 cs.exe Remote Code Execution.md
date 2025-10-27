---
title: OpenText Extended ECM 22.3 cs.exe Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023010036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-23
fetch_date: 2025-10-04T04:35:25.126878
---

# OpenText Extended ECM 22.3 cs.exe Remote Code Execution

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
|  |  | |  | | --- | | **OpenText Extended ECM 22.3 cs.exe Remote Code Execution** **2023.01.22**  Credit:  **[Armin Stock](https://cxsecurity.com/author/Armin%2BStock/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45923](https://cxsecurity.com/cveshow/CVE-2022-45923/ "Click to see CVE-2022-45923")**  CWE: **N/A** | |

SEC Consult Vulnerability Lab Security Advisory < 20230117-0 >
=======================================================================
title: Pre-authenticated Remote Code Execution in cs.exe
product: OpenText™ Content Server component of OpenText™ Extended ECM
vulnerable version: 20.4 - 22.3
fixed version: 22.4
CVE number: CVE-2022-45923
impact: Critical
homepage: https://www.opentext.com/
found: 2022-09-16
by: Armin Stock (Atos)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"OpenText™ Extended ECM is an enterprise CMS platform that securely governs the
information lifecycle by integrating with leading enterprise applications, such
as SAP®, Microsoft® 365, Salesforce and SAP SuccessFactors®. Bringing content
and processes together, Extended ECM provides access to information when and
where it’s needed, improves decision-making and drives operational effectiveness."
Source: https://www.opentext.com/products/extended-ecm
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
Vulnerability overview/description:
-----------------------------------
1) Pre-authenticated Remote Code Execution in cs.exe (CVE-2022-45923)
The `Common Gateway Interface (CGI)` program `cs.exe` of the `Content Server`
has a vulnerability, which allows an attacker to increase/decrease an arbitrary
memory address by 1 and to trigger a call to a method of a `vftable` with a
`vftable pointer` value chosen by the attacker.
The `cs.exe` does de-serialize (crack) the user provided data in the `\_fInArgs`
parameter, if the parameter `\_ApiName` is set. During this de-serialization to
a `class KOSValue` object, the function `obj\_ref\_cracker` can be called. This
function tries to create a new `class KOSValue` object with an unknown class ID
of `3`.
As the class ID is unknown the function returns an object of type
`KOSValueBaseClass` instead of `KOSObjRefClass`, but the value of the
`class\_ptr` attribute of the new `class KOSValue` object is controlled by the
attacker. This new object can then be used to increase/decrease arbitrary
memory addresses and call methods of its `vftable` via the functions
`KOSValueBaseClass::AddReference` and `KOSValueBaseClass::ReleaseReference`.
Proof of concept:
-----------------
1) Pre-authenticated Remote Code Execution in cs.exe (CVE-2022-45923)
The following request crashes the `CGI` binary `cs.exe` with an `access
violation exception - 0xC0000005` trying to read memory from address
`0xAAAA+8`:
-------------------------------------------------------------------------------
[ PoC removed, will be published at a later date ]
-------------------------------------------------------------------------------
There are `.dll` files (`libaprutil-1` & `libapriconv-1.dll`) which are not
compiled with the security flag `Address Space Layout Randomization - ASLR`
enabled, which can be used to achieve remote code execution.
-------------------------------------------------------------------------------
.\winchecksec.exe --json (get-item C:\OPENTEXT-22\cgi\\*.dll) > .\checksec-results.json
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
cat checksec-results.json | jq -r '.[] | [.path, .mitigations.aslr.presence] | @csv'
"icudt69.dll","Present"
"icuin69.dll","Present"
"icuio69.dll","Present"
"icutu69.dll","Present"
"icuuc69.dll","Present"
"jsoncpp.dll","Present"
"libapr-1.dll","Present"
"libapriconv-1.dll","NotPresent"
"libaprutil-1.dll","NotPresent"
"libcrypto-1\_1-x64.dll","Present"
"libexpat.dll","Present"
"libssl-1\_1-x64.dll","Present"
"llcrypt.dll","Present"
"llisapi.dll","Present"
"llkernel.dll","Present"
"llresources.dll","Present"
"log4cxx.dll","Present"
"PocoFoundation.dll","Present"
-------------------------------------------------------------------------------
Vulnerable / tested versions:
-----------------------------
The following version has been tested:
\* 22.1 (16.2.19.1803)
The following versions are vulnerable according to the vendor:
\* 20.4 - 22.3
Vendor contact timeline:
------------------------
2022-10-07: Vendor contacted via security@opentext.com
2022-10-07: Vendor acknowledged the email and is reviewing the reports
2022-11-18: Vendor confirms all vulnerabilities and is working on a patch aimed to
be released in November
2022-11-24: Vendor delays the patch "few days/weeks into December"
2022-11-25: Requesting CVE numbers (Mitre)
2022-12-15: Vendor delays the patch and provides a release date: January 16th 2023
2023-01-17: Public release of security advisory
Solution:
---------
Upgrade to at least version 22.4 or apply hotfixes which can be downloaded at
the vendor's page:
https://support.opentext.com/csm?id=kb\_article\_view&sysparm\_article=KB0781429
Workaround:
-----------
None
Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SEC Consult Vulnerability Lab
SEC Consult, an Atos company
Europe | Asia | North America
About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos company. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulne...