---
title: IBM Security Verify Access Appliance Insecure Transit / Hardcoded Passwords
url: https://cxsecurity.com/issue/WLB-2024110009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-07
fetch_date: 2025-10-06T19:12:24.112691
---

# IBM Security Verify Access Appliance Insecure Transit / Hardcoded Passwords

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
|  |  | |  | | --- | | **IBM Security Verify Access Appliance Insecure Transit / Hardcoded Passwords** **2024.11.06**  Credit:  **[Pierre Kim](https://cxsecurity.com/author/Pierre%2BKim/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-31874](https://cxsecurity.com/cveshow/CVE-2024-31874/ "Click to see CVE-2024-31874")** | **[CVE-2024-31871](https://cxsecurity.com/cveshow/CVE-2024-31871/ "Click to see CVE-2024-31871")** | **[CVE-2024-31872](https://cxsecurity.com/cveshow/CVE-2024-31872/ "Click to see CVE-2024-31872")** | **[CVE-2024-31873](https://cxsecurity.com/cveshow/CVE-2024-31873/ "Click to see CVE-2024-31873")** | **[CVE-2023-25927](https://cxsecurity.com/cveshow/CVE-2023-25927/ "Click to see CVE-2023-25927")** | **[CVE-2023-38371](https://cxsecurity.com/cveshow/CVE-2023-38371/ "Click to see CVE-2023-38371")**  CWE: **N/A** | |

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512
## Advisory Information
Title: 4 vulnerabilities in ibmsecurity
Advisory URL: https://pierrekim.github.io/advisories/2024-ibmsecurity.txt
Blog URL: https://pierrekim.github.io/blog/2024-11-01-ibmsecurity-4-vulnerabilities.html
Date published: 2024-11-01
Vendors contacted: IBM
Release mode: Released
CVE: CVE-2024-31871, CVE-2024-31872, CVE-2024-31873, CVE-2024-31874
## Product description
> This repository contains Python code to manage IBM Security Appliances using their respective REST APIs. ISAM appliance has the most mature code.
>
> From https://github.com/IBM-Security/ibmsecurity
## Vulnerability Summary
Vulnerable versions: ibmsecurity < v2024.4.5.
The summary of the vulnerabilities is as follows:
1. CVE-2024-31871 - Insecure communications 1/2
2. CVE-2024-31872 - Insecure communications 2/2
3. CVE-2024-31873 - Hardcoded passwords
4. CVE-2024-31874 - Uninitialized variables
TL;DR: An attacker located on the network can MITM TLS connections to IBM Security Verify Access (ISVA) appliances, recover credentials and compromise the entire IBM Security Verify Access infrastructure. IBM Security Verify Access is a SSO solution mainly used by banks, Fortune 500 companies and governmental entities.
\_Miscellaneous notes\_:
The vulnerabilities were found in February 2023 and were communicated to IBM in March 2023. They ultimately were patched in April 2024 (after 13 months).
Communication with IBM was difficult. At first, IBM support had confirmed that they would patch the vulnerabilities found in the ibmsecurity library. Then, in April 2024, IBM advised that the only way to get security patches is to go Full-disclosure and open a github issue containing all technical details. Although this was unusual, I created a github issue, which was subsequently redacted by IBM - https://github.com/IBM-Security/ibmsecurity/issues/416.
\_Impacts\_
An attacker can compromise the entire authentication infrastructure based on IBM Security Verify Access by intercepting admin credentials on the network.
\_Recommendations\_
- - Apply security patches.
- - Enable certificate validation (not enabled by default).
## Details - Insecure communications 1/2
The ibmsecurity package has been partially audited as it provides the underlying Python APIs used to communicate with IBM Security Verify Access (ISVA).
Unfortunately, the security of the ibmsecurity package is very poor and, by default, all the SSL/TLS connections to the remote ISVA server are configured in an insecure way.
The latest version of the ibmsecurity library (`ibmsecurity-2022.8.22.0`) has been downloaded using pip in order for the source code to be reviewed:
kali% pip download ibmsecurity
Collecting ibmsecurity
Using cached ibmsecurity-2022.8.22.0-py3-none-any.whl (391 kB)
Collecting requests
Using cached requests-2.28.1-py3-none-any.whl (62 kB)
Collecting charset-normalizer<3,>=2
Using cached charset\_normalizer-2.1.1-py3-none-any.whl (39 kB)
Collecting urllib3<1.27,>=1.21.1
Using cached urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
Collecting certifi>=2017.4.17
Using cached certifi-2022.9.24-py3-none-any.whl (161 kB)
Collecting idna<4,>=2.5
Using cached idna-3.4-py3-none-any.whl (61 kB)
Saved ./ibmsecurity-2022.8.22.0-py3-none-any.whl
Saved ./requests-2.28.1-py3-none-any.whl
Saved ./certifi-2022.9.24-py3-none-any.whl
Saved ./charset\_normalizer-2.1.1-py3-none-any.whl
Saved ./idna-3.4-py3-none-any.whl
Saved ./urllib3-1.26.12-py2.py3-none-any.whl
Successfully downloaded ibmsecurity requests certifi charset-normalizer idna urllib3
kali%
The `invoke\_\*` functions in the ibmsecurity library will use by default the `\_suppress\_ssl\_warning()` method that will remove any security related to SSL/TLS.
For example, the method `invoke\_put()` is defined in the file `ibmsecurity/appliance/isamappliance.py`, as shown below on line 402:
Content of `ibmsecurity/appliance/isamappliance.py`:
[code:python]
...
3 from requests.packages.urllib3.exceptions import InsecureRequestWarning
...
17 class ISAMAppliance(IBMAppliance):
...
45 def \_suppress\_ssl\_warning(self):
46 # Disable https warning because of non-standard certs on appliance
47 try:
48 self.logger.debug("Suppressing SSL Warnings.")
49 requests.packages.urllib3.disable\_warnings(InsecureRequestWarning) # [1] <- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
50 except AttributeError:
51 self.logger.warning("load requests.packages.urllib3.disable\_warnings() failed")
...
402 def invoke\_put(self, description, uri, data, ignore\_error=False, requires\_modules=None, requires\_version=None,
403 warnings=[], requires\_model=None):
404 """
405 Send a PUT request to the LMI.
406 """
407
408 self.\_log\_request("PUT", uri, description)
409 response = self.\_invoke\_request(self.session.put, description, uri,
410 ignore\_error, data,
411 requires\_modules=requires\_modules, requires\_version=requires\_version,
412 requires\_model=requires\_model, warnings=warnings)
413 return response
...
[/code]
The method `\_invoke\_request()` called on line 409 inside the `invoke\_put()` method will disable any SSL/TLS security on line 334 by calling the method `\_suppress\_ssl\_warning()` previously defined on line 45:
Content of `ibmsecurity/appliance/isamapp...