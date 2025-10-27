---
title: 4 vulnerabilities in ibmsecurity
url: https://seclists.org/fulldisclosure/2024/Nov/1
source: Full Disclosure
date: 2024-11-04
fetch_date: 2025-10-06T19:15:44.085206
---

# 4 vulnerabilities in ibmsecurity

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# 4 vulnerabilities in ibmsecurity

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Fri, 1 Nov 2024 15:18:06 -0400

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "4 vulnerabilities in ibmsecurity" is posted here:
  https://pierrekim.github.io/blog/2024-11-01-ibmsecurity-4-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2024-ibmsecurity.txt

=== text-version of the advisory  ===

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
```

> ```
> This repository contains Python code to manage IBM Security Appliances using their respective REST APIs. ISAM
> appliance has the most mature code.
>
> From https://github.com/IBM-Security/ibmsecurity
> ```

```
## Vulnerability Summary

Vulnerable versions: ibmsecurity < v2024.4.5.

The summary of the vulnerabilities is as follows:

1. CVE-2024-31871 - Insecure communications 1/2
2. CVE-2024-31872 - Insecure communications 2/2
3. CVE-2024-31873 - Hardcoded passwords
4. CVE-2024-31874 - Uninitialized variables

TL;DR: An attacker located on the network can MITM TLS connections to
IBM Security Verify Access (ISVA) appliances, recover credentials and
compromise the entire IBM Security Verify Access infrastructure. IBM
Security Verify Access is a SSO solution mainly used by banks, Fortune
500 companies and governmental entities.

_Miscellaneous notes_:

The vulnerabilities were found in February 2023 and were communicated
to IBM in March 2023. They ultimately were patched in April 2024
(after 13 months).

Communication with IBM was difficult. At first, IBM support had
confirmed that they would patch the vulnerabilities found in the
ibmsecurity library. Then, in April 2024, IBM advised that the only
way to get security patches is to go Full-disclosure and open a github
issue containing all technical details. Although this was unusual, I
created a github issue, which was subsequently redacted by IBM -
https://github.com/IBM-Security/ibmsecurity/issues/416.

_Impacts_

An attacker can compromise the entire authentication infrastructure
based on IBM Security Verify Access by intercepting admin credentials
on the network.

_Recommendations_

- - Apply security patches.
- - Enable certificate validation (not enabled by default).

## Details - Insecure communications 1/2

The ibmsecurity package has been partially audited as it provides the
underlying Python APIs used to communicate with IBM Security Verify
Access (ISVA).

Unfortunately, the security of the ibmsecurity package is very poor
and, by default, all the SSL/TLS connections to the remote ISVA server
are configured in an insecure way.

The latest version of the ibmsecurity library
(`ibmsecurity-2022.8.22.0`) has been downloaded using pip in order for
the source code to be reviewed:

    kali% pip download ibmsecurity
    Collecting ibmsecurity
    Using cached ibmsecurity-2022.8.22.0-py3-none-any.whl (391 kB)
    Collecting requests
    Using cached requests-2.28.1-py3-none-any.whl (62 kB)
    Collecting charset-normalizer<3,>=2
    Using cached charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
    Collecting urllib3<1.27,>=1.21.1
    Using cached urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
    Collecting certifi>=2017.4.17
    Using cached certifi-2022.9.24-py3-none-any.whl (161 kB)
    Collecting idna<4,>=2.5
    Using cached idna-3.4-py3-none-any.whl (61 kB)
    Saved ./ibmsecurity-2022.8.22.0-py3-none-any.whl
    Saved ./requests-2.28.1-py3-none-any.whl
    Saved ./certifi-2022.9.24-py3-none-any.whl
    Saved ./charset_normalizer-2.1.1-py3-none-any.whl
    Saved ./idna-3.4-py3-none-any.whl
    Saved ./urllib3-1.26.12-py2.py3-none-any.whl
    Successfully downloaded ibmsecurity requests certifi
charset-normalizer idna urllib3
    kali%

The `invoke_*` functions in the ibmsecurity library will use by
default the `_suppress_ssl_warning()` method that will remove any
security related to SSL/TLS.

For example, the method `invoke_put()` is defined in the file
`ibmsecurity/appliance/isamappliance.py`, as shown below on line 402:

Content of `ibmsecurity/appliance/isamappliance.py`:

[code:python]
...
  3 from requests.packages.urllib3.exceptions import InsecureRequestWarning
...
 17 class ISAMAppliance(IBMAppliance):
...
 45     def _suppress_ssl_warning(self):
 46         # Disable https warning because of non-standard certs on appliance
 47         try:
 48             self.logger.debug("Suppressing SSL Warnings.")
 49
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #
[1] <- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 50         except AttributeError:
 51             self.logger.warning("load
requests.packages.urllib3.disable_warnings() failed")
...
402     def invoke_put(self, description, uri, data,
ignore_error=False, requires_modules=None, requires_version=None,
403                    warnings=[], requires_model=None):
404         """
405         Send a PUT request to the LMI.
406         """
407
408         self._log_request("PUT", uri, description)
409         response = self._invoke_request(self.session.put, description, uri,
410                                         ignore_error, data,
411
requires_modules=requires_modules, requires_version=requires_version,
412
requires_model=requires_model, warnings=warnings)
413         return response
...
[/code]

The method `_invoke_request()` called on line 409 inside the
`invoke_put()` method will disable any SSL/TLS security on line 334 by
calling the method `_suppress_ssl_warning()` previously defined on
line 45:

Content of `ibmsecurity/appliance/isamappliance.py`:

[code:python]
...
305     def _invoke_request(self, func, description, uri,
ignore_error, data={}, requires_modules=None,
306                         requires_version=None, warnings=[],
requires_model=None):
307         """
308         Send a request to the LMI.  This function is private and
should not be
309         used directly.  The invoke_get/invoke_put/etc functions
should be used instead.
310         """
...
334         self._suppress_ssl_warning() # <- insecure SSL/TLS
connection to the remote ISVA instance
...
336         try:
337             if func == self.session.get or func == self.session.delete:
338
339                 if data != {}:
340                     r = func(url=self._url(uri), data=json_data,
verify=False, headers=headers)
341                 else:
342                     r = func(url=self._url(uri), verify=False,
headers=headers)
343             else:
344                 r = func(url=self._url(uri), data=json_data,
345                          verify=False, headers=headers)
346
347             if func != self.session.get:
348                 return_obj['changed'] = True  # Anything but GET
should result in change
349
350             self._process_respons...