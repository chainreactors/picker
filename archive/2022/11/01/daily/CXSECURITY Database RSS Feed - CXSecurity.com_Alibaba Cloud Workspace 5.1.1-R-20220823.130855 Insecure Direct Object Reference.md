---
title: Alibaba Cloud Workspace 5.1.1-R-20220823.130855 Insecure Direct Object Reference
url: https://cxsecurity.com/issue/WLB-2022100073
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:41.113639
---

# Alibaba Cloud Workspace 5.1.1-R-20220823.130855 Insecure Direct Object Reference

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
|  |  | |  | | --- | | **Alibaba Cloud Workspace 5.1.1-R-20220823.130855 Insecure Direct Object Reference** **2022.10.31**  Credit:  **[Erwin Chan](https://cxsecurity.com/author/Erwin%2BChan/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Alibaba Cloud Workspace vulnerable to IDOR which lead to
account hijacking in a certain situation
# Date: 30/10/2022
# Exploit Author: Erwin Chan
# Vendor Homepage: https://www.alibabacloud.com/
# Software Link:
https://www.alibabacloud.com/product/cloud-desktop/download-client
# Version: Alibaba Cloud Workspace 5.1.1-R-20220823.130855
# Tested on: Windows 10
We found that Alibaba Cloud Workspace was vulnerable to insecure direct
object references ("IDOR") which lead to account hijacking in a certain
situation. Vender had confirmed that it was a "bug" instead of a
vulnerability and attempt to fix it in long term. Still, we considered that
this will introduce non-neglectable security ricks to end users. Hence, we
propose a measure to system admin in the following to mitigate the risk.
In Alibaba Cloud, end users could login to a workspace to control
corresponding cloud desktops. While a system admin could create various
workspaces, in their organization (or call it "tenant"), which allow users
login with different set of credentials and multi-factor authentication
("MFA"). We discovered that if different user accounts shared same username
(e.g., two accounts that share same username but different password,
different MFA and in different workspace), we could leverage one account
and alter the value of workspace ID in the traffic in order to hijack the
other account. The IDOR vulnerability allow an advisory who already
compromised one account of a workspace to further compromise an account
with same username of another workspace without knowing the password and
MFA verification.
Alibaba Cloud allow system admin to create workspace with enterprise AD
type. After a workspace of enterprise AD type was created, two domain
forests (i.e., “ecd.acs” and a domain setup by system admin ) and a domain
trust would be created and established respectively. It was observed that
“ecd.acs” may be used as management domain for system admin in some
enterprise. Thus, the IDOR vulnerability introduced a security risk which
allowing advisory to lateral move across different domains and potentially
escalate their privilege.
To mitigate the security risk that introduced by IDOR vulnerability, we
suggested system admin to create accounts with different username for each
workspaces. Vender had already plan to fix the bug in long term and may
consider to redact the domain “ecd.acs”.
Timeline:
Sep 16 2022 - we report the finding to Alibaba Cloud vender
Oct 12 2022 - Alibaba Cloud vender accept this as a bug instead of
vulnerability, and plan to fix it in long term

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100073)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top