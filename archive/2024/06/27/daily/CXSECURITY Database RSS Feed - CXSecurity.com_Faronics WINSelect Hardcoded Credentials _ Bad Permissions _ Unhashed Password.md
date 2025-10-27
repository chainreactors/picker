---
title: Faronics WINSelect Hardcoded Credentials / Bad Permissions / Unhashed Password
url: https://cxsecurity.com/issue/WLB-2024060063
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-27
fetch_date: 2025-10-06T16:54:23.380294
---

# Faronics WINSelect Hardcoded Credentials / Bad Permissions / Unhashed Password

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
|  |  | |  | | --- | | **Faronics WINSelect Hardcoded Credentials / Bad Permissions / Unhashed Password** **2024.06.26**  Credit:  **[Daniel Hirschberger](https://cxsecurity.com/author/Daniel%2BHirschberger/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-36497](https://cxsecurity.com/cveshow/CVE-2024-36497/ "Click to see CVE-2024-36497")** | **[CVE-2024-36495](https://cxsecurity.com/cveshow/CVE-2024-36495/ "Click to see CVE-2024-36495")** | **[CVE-2024-36496](https://cxsecurity.com/cveshow/CVE-2024-36496/ "Click to see CVE-2024-36496")**  CWE: **N/A** | |

SEC Consult Vulnerability Lab Security Advisory < 20240624-0 >
=======================================================================
title: Multiple Vulnerabilities allowing complete bypass
product: Faronics WINSelect (Standard + Enterprise)
vulnerable version: <8.30.xx.903
fixed version: 8.30.xx.903
CVE number: CVE-2024-36495, CVE-2024-36496, CVE-2024-36497
impact: high
homepage: https://www.faronics.com/products/winselect
found: 2024-02-01
by: Daniel Hirschberger (Office Bochum)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"WINSelect - Allows you to easily control your end-users' Windows Experience without
having to deal with GPOs.
Need to Prevent Data From Leaving?
Whether you're working on classified government files or the secret ingredient
for your famous lasagna, you need to protect your sensitive information from
walking out the door.
Faronics WINSelect offers the ability to disable USB ports and disk drives. Now
you can relax knowing your secrets won't be exported without your knowledge."
Source: https://www.faronics.com/products/winselect
Business recommendation:
------------------------
The vendor provides a patched version which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.
Vulnerability overview/description:
-----------------------------------
1) Read/Write Permissions for Everyone on Configuration File (CVE-2024-36495)
The application saves its configuration in an encrypted file which "Everyone" has
read and write access to.
2) Hardcoded Credentials (CVE-2024-36496)
The configuration file is encrypted with a static key derived from a static five-
character password which allows an attacker to decrypt this file.
3) Unhashed Storage of Password (CVE-2024-36497)
The decrypted configuration file contains the password in cleartext which is used
to configure WINSelect. It can be used to remove the existing restrictions and
disable WINSelect entirely.
By combining these issues any local attacker can disable WINSelect.
Proof of concept:
-----------------
1) Read/Write Permissions for Everyone on Configuration File (CVE-2024-36495)
WINSelect Standard saves its configuration in the following file:
C:\ProgramData\WINSelect\WINSelect.wsd
Every user has read and write permissions on this file by default:
<read\_write\_everyone.png>
The write permission is no problem as long as WINSelect is running, because it
is locked by the process WSEngine.exe.
For WINSelect Enterprise the path for the configuration file is:
C:\ProgramData\Faronics\StorageSpace\WS\WINSelect.wsd
2) Hardcoded Credentials (CVE-2024-36496)
By analyzing the application via the API Monitor tool, we found that the
application uses a hardcoded five letter password, hashes it with the outdated
and broken MD5 algorithm (no salt) and uses the first five bytes as the key
for RC4. The configuration file is then encrypted with these parameters.
After starting WINSelect.exe the MD5 and RC4 algorithms are requested:
<rc4\_md5.png>
When the login to the configuration of WINSelect is triggered via
CTRL+ALT+SHIFT+F8, the configuration file is decrypted.
<login.png>
The hardcoded password "Kunal" is hashed.
<hash\_input.png>
<hash\_output.png>
The first five bytes of the hash are used to instantiate a key object.
<key.png>
The configuration is then decrypted with this key.
<decrypted.jpeg>
To simplify this proof of concept the following python script was developed
which automatically decrypts an encrypted WINSelect.wsd:
<test.py>
3) Unhashed Storage of Password (CVE-2024-36497)
By decrypting the configuration file, the used password can be extracted at the
beginning of the file:
---
<?xml version="1.0"?>
<KIOSK>
<SECTIONS>
<SECTION>
<SID>194</SID><!--S\_ID\_ADMIN\_PASS-->
<RULES>
<RULE>
<ID>121</ID><!--R\_ID\_PROTECTION\_ON\_OFF-->
<ENABLED>1</ENABLED>
</RULE>
<RULE>
<ID>148</ID><!--R\_ID\_PROTECTION\_ON\_OFF\_ADMIN-->
<ENABLED>1</ENABLED>
</RULE>
<RULE>
<ID>116</ID><!--R\_ID\_ADMIN\_PASS-->
<ENABLED>1</ENABLED>
<DATA>
<PASSWORDSET>0</PASSWORDSET>
<ADMINPASSWORD>myadminpw</ADMINPASSWORD>
</DATA>
---
Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
\* 8.22.1112.886
Vendor contact timeline:
------------------------
2024-02-19: Contacting vendor through support@faronics.com and
customerservice@faronics.com
2024-02-20: Vendor responds with an email address to which we shall send the
advisory.
2024-02-20: Asking for encryption, vendor requests unencrypted communication,
submitting advisory.
2024-02-21: Vendor confirms receipt, engaged with product and development teams.
2024-02-27: Vendor introduces additional contact, will coordinate further responses.
2024-03-13: Additional contact apologizes for delayed response, vulnerabilities
already discussed internally. Asks for extension of release.
2024-03-14: Extending advisory release to coordinate with patch.
2024-04-10: Vendor has addressed the reported issues in a test build for the
standard version, enterprise fixes will be incorporated soon.
2024-04-18: Giving feedback that the issue is still exploitable, proposing a
better hash function and random UUID, linking to O...