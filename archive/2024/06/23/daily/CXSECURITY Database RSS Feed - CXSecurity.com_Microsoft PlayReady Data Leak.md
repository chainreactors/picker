---
title: Microsoft PlayReady Data Leak
url: https://cxsecurity.com/issue/WLB-2024060048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-23
fetch_date: 2025-10-06T16:54:43.700934
---

# Microsoft PlayReady Data Leak

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
|  |  | |  | | --- | | **Microsoft PlayReady Data Leak** **2024.06.22**  Credit:  **[Adam Gowdiak](https://cxsecurity.com/author/Adam%2BGowdiak/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Hello All,
On Jun 11, 2024 Microsoft engineer posted on a public forum
information about a crash experienced with Apple TV service on a
Surface Pro 9 device [1].
The post had an attachment - a 771MB file (4GB unpacked), which leaked
internal code (260+ files [2]) pertaining to Microsoft PlayReady such
as the following:
- Warbird configuration for building PlayReady library
- Warbird library implementing code obfuscation functionality
- static libraries with symbolic information either required or
related to PlayReady client library building, this includes OEM,
crypto, ARM TEE / HW related libs a preprocessed C++ header file with
PlayReady constants, unpublished classes and their methods declaration
In general the above leaked key information related to PlayReady
internals and implementation. Leaked data should be sufficient to
completely reverse engineer Microsoft PlayReady operation (HW based
one in particular).
As such, on Jun 12, 2024 we notified Microsoft PlayReady and MSRC
about the leak shortly following its discovery.
We verified that it is possible to build
Windows.Media.Protection.PlayReady.dll library (debug build and
without Warbird encryption / obfuscation) from the leaked code. A
follow up post by another Microsoft engineer provided guidelines on
how to proceed with the building process [4] (this post has been also
removed).
We also verified that Microsoft Symbol Server didn’t block request for
PDB file corresponding to Microsoft internal warbird.dll binary
(another leak / bug at Microsoft end).
The leak violated Microsoft's own guidelines [5] for posting link
repro information in public. These guidlines clearly state the
following among others:
- "All information in reports and any comments and replies are
publicly visible by default"
- "Don't put anything you want to keep private in the title or content
of the initial report, which is public"
- "To maintain your privacy and keep your sensitive information out of
public view, be careful"
The described leaks are yet another manifestation of what we have been
already aware of - the problems and inconsistencies observed at
Microsoft end with respect to PlayReady security and the way secrecy
of the implementation is implemented and/or maintained by the company.
While Microsoft removed the post (within 12 hours from the
notification), the company hasn't removed the leak itself so far [3].
There are some chances this post is to put Microsoft to action though...
Thank you.
Best Regards,
Adam Gowdiak
----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
References:
[1] MSPR leak (screenshot 1)
https://security-explorations.com/samples/mspr\_leak\_screenshot.png
[2] MSPR leak (files list)
https://security-explorations.com/samples/mspr\_leak\_files.txt
[3] MSPR leak (screenshot 2)
https://security-explorations.com/samples/mspr\_leak\_screenshot2.png
[4] MSPR leak (screenshot 3)
https://security-explorations.com/samples/mspr\_leak\_screenshot3.png
[5] How to report a problem with the Microsoft C++ toolset or
documentation (Reports and privacy)
https://learn.microsoft.com/en-us/cpp/overview/how-to-report-a-problem-with-the-visual-cpp-toolset?view=msvc-170#reports-and-privacy

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060048)

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