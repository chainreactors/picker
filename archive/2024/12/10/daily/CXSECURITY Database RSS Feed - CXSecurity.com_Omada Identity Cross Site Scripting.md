---
title: Omada Identity Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024120014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-10
fetch_date: 2025-10-06T19:33:44.912874
---

# Omada Identity Cross Site Scripting

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
|  |  | |  | | --- | | **Omada Identity Cross Site Scripting** **2024.12.09**  Credit:  **[Daniel Hirschberger](https://cxsecurity.com/author/Daniel%2BHirschberger/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-52951](https://cxsecurity.com/cveshow/CVE-2024-52951/ "Click to see CVE-2024-52951")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

SEC Consult Vulnerability Lab Security Advisory < 20241127-0 >
=======================================================================
title: Stored Cross-Site Scripting
product: Omada Identity
vulnerable version: <v15U1, <v14.14 hotfix #309
fixed version: v15U1, v14.14 hotfix #309
CVE number: CVE-2024-52951
impact: Medium
homepage: https://omadaidentity.com/products/omada-identity/
found: 2024-03-20
by: Daniel Hirschberger (Office Bochum)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Omada Identity is a modern, enterprise-ready IGA solution that is deployed
on-premises, giving you full control over your data and security. Our solution
is easy to use, highly customizable, and gives you complete visibility into your
environment without having to write a single line of code but is completely
customizable to address any requirement. With built-in automation features,
Omada Identity can help you streamline your workflows, improve efficiency, and
strengthen your security posture."
Source: https://omadaidentity.com/products/omada-identity/
Business recommendation:
------------------------
Upgrade to version v15U1 or install hotfix #309 for v14.14.
SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.
Vulnerability overview/description:
-----------------------------------
1) Stored Cross-Site Scripting (CVE-2024-52951)
An authenticated user can inject JavaScript in the "Request Reason". The
injected JavaScript code will be executed if another user looks at the "History"
of this access request. An attacker can then execute arbitrary JavaScript
in the browser of other users which could for example be used for phishing attacks.
Proof of concept:
-----------------
1) Stored Cross-Site Scripting (CVE-2024-52951)
An authenticated user can submit an access request and has to specify a reason why
the access should be provided.
<1-1\_request\_access.png>
This request has to be intercepted and modified, e.g.:
--------------------------------------------------------------------------------
POST /workitemdlg.aspx?ACTTEMP=XXX&RURLID=YYY HTTP/1.1
Host: $SERVER
Cookie: oissessionid=$MYSESSION
[...]
Content-Type: application/x-www-form-urlencoded
[...]
1000104=Need+hello+access+and+bigfun<iframe+src=javascript:alert(document.domain)></iframe>&1000102=I+would+like+to+request+access+to+%5Bspecify+system%5D+so+I+can+perform+my+%5Bspecify+duties%5D+duties+related+to+my+work+as+a+%5Bspecify+position%5D.
[...]
--------------------------------------------------------------------------------
Afterwards, anyone who reviews the "History" of this access request will be
affected by the stored JavaScript code. Users who review the history requests are
usually managers who have to approve this request, so this vulnerability allows
reliably affecting higher-privileged users.
<1-2\_trigger\_xss.png>
Vulnerable / tested versions:
-----------------------------
The following version of the on-prem solution has been tested which was the latest
version available at the time of the test:
\* 14.0.14.36
Previous versions of v14.14 hotfix #309 are affected according to the vendor, as
well as <v15U1.
Vendor contact timeline:
------------------------
2024-04-08: Contacting vendor through contract@omadaidentity.com; no response.
2024-04-24: Contacting vendor through contract@omadaidentity.com and
info@omadaidentity.com; no response.
2024-05-06: Contacting vendor through their "Contact Us" form;
We were contacted by Sales and forwarded the email to them.
2024-05-08: CISO contacts us, we sent the advisory via provided Sharepoint
link.
2024-05-13: Vendor confirms security issues. XSS is fixed now and hotfixes
are created for their releases.
Second finding was disputed and seems to be a misconfiguration.
Removed issue 2 from advisory.
2024-05-27: Asking for a status update regarding XSS hotfixes.
2024-05-27: Vendor: May cloud update is scheduled for 29th May. On-prem
release version v15U1 is planned for 12th June. Hot-fix for on-prem
version 14.14 is also planned for 12th June.
2024-06-17: Asking if Hotfix is released
2024-06-21: Vendor: Hotfix #309 for v14.14 is released
2024-06-24: Vendor: asks if we are satisfied with the follow-up
We agree and respect the wish to delay the publication of the
advisory for at least one month.
2024-10-08: Asking vendor regarding CVE assignment.
2024-10-11: Vendor is waiting for internal confirmation regarding next steps,
update hopefully next week.
2024-10-08: Asking for a status update, whether we should assign a CVE.
2024-10-31: Vendor responds with calculated CVSS vectors and asks for
our opinions;
We agree that the CVSS Base Score looks correct and ask to
clarify if they want to register the CVE themselves or if
we as a CNA should register it for them.
2024-11-18: Received CVE number from vendor;
We provide our CVE details to the vendor and ask them
to update the CVE entry.
2024-11-22: Vendor notifies us about the CVE update, gives us a
green light for the publication and thanks us for our
cooperation;
We mention that we will publish it in the following week
and also thank the vendor.
2024-11-27: Release of security advisory.
Solution:
---------
Upgrade to version v15U1 or install hotfix #309 for v14.14.
Workaround:
-----------
None
Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SEC Consult Vulnerability Lab
An integ...