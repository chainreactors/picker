---
title: SEC Consult SA-20260218-0 :: Multiple Critical Vulnerabilities in NesterSoft WorkTime (on-prem/cloud)
url: https://seclists.org/fulldisclosure/2026/Feb/31
source: Full Disclosure
date: 2026-02-22
fetch_date: 2026-02-23T04:20:23.592556
---

# SEC Consult SA-20260218-0 :: Multiple Critical Vulnerabilities in NesterSoft WorkTime (on-prem/cloud)

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260218-0 :: Multiple Critical Vulnerabilities in NesterSoft WorkTime (on-prem/cloud)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 18 Feb 2026 11:52:03 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260218-0 >
=======================================================================
             title: Multiple Critical Vulnerabilities
           product: NesterSoft WorkTime (on-prem/cloud)
vulnerable version: <= 11.8.8
     fixed version: No patch available, vendor unresponsive.
        CVE number: CVE-2025-15563, CVE-2025-15562, CVE-2025-15561
                    CVE-2025-15560, CVE-2025-15559
            impact: Critical
          homepage:https://www.worktime.com/
             found: 2025-05-22
                by: Tobias Niemann (Office Bochum)
                    Daniel Hirschberger
                    Thorger Jansen (Office Bochum)
                    Marius Renner (Office Berlin)
                    SEC Consult Vulnerability Lab

                    An integrated part of SEC Consult, an Atos business
                    Europe | Asia

                    https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"WorkTime is a green employee monitoring software with a primary focus on
monitoring employees' productivity. It is a non-invasive, transparent, safe,
and socially responsible technology. WorkTime offers a safe replacement for
every invasive function."

Source:https://www.worktime.com/employee-monitoring

Business recommendation:
------------------------
The vendor did not respond to our communication attempts anymore. It is currently
unclear, whether a patch is available. Please contact the vendor to request a
patch for the identified critical security issues.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Unauthenticated OS Command Injection (CVE-2025-15559)
An unauthenticated attacker can inject OS commands when calling a server API
endpoint. This allows an attacker to execute arbitrary commands on the
WorkTime server as NT Authority\SYSTEM with the highest privileges. Attackers
are able to access or manipulate sensitive data and take over the whole
server.

2) SQL Injection (MSSQL/Firebird Backend) (CVE-2025-15560)
An authenticated attacker with minimal permissions can exploit a SQL injection
in a WorkTime server API endpoint to inject SQL queries. If the Firebird
backend is used, attackers are able to retrieve all data from the database backend.
If the MSSQL backend is used the attacker can execute arbitrary SQL statements
on the database backend and gain access to sensitive data.

3) Local Privilege Escalation (CVE-2025-15561)
An attacker can exploit the update behavior of the WorkTime monitoring daemon
to elevate privileges on the local system to NT Authority\SYSTEM.

4) Reflected Cross-Site Scripting (XSS) (CVE-2025-15562)
A server API endpoint reflects received data into the HTML response without
applying proper encoding or filtering. This allows an attacker to execute
arbitrary JavaScript in the victim's browser if the victim opens a URL prepared
by the attacker.

5) Broken Access Control results in Denial of Service (CVE-2025-15563)
Any unauthenticated user can reset the WorkTime on-prem database configuration
by sending a specific HTTP request to the WorkTime server. No authorization check is
applied here.

Proof of concept:
-----------------
1) Unauthenticated OS Command Injection (CVE-2025-15559)
The server API call to generate and download the WorkTime client from the
WorkTime server is vulnerable against OS command injection in the "guid"
parameter. For this proof of concept the following OS command is injected:
--------------------------------------------------------------------------------
whoami > C:\secwashere
--------------------------------------------------------------------------------
The HTTP request is shown below:
--------------------------------------------------------------------------------
< PoC removed >
--------------------------------------------------------------------------------

The injected command is executed on the server as NT Authority\SYSTEM:
<command_injection.png>

2) SQL Injection (MSSQL/Firebird Backend) (CVE-2025-15560)
The following authenticated "widget" API endpoint is vulnerable. Minimal
permissions are required to access the server endpoint.
--------------------------------------------------------------------------------
POST /api/widget HTTP/1.1
Host: <server_hostname>:8080
Content-Type: multipart/form-data; boundary=---------------------------295635091325610060643320064167
Content-Length: [...]
-----------------------------295635091325610060643320064167
< removed >
-----------------------------295635091325610060643320064167--
--------------------------------------------------------------------------------

Note that the request requires a token value in the request body.
Any user that has access to the WorkTime server in any role has access to a
valid token. The three parameters employee, computer and department are injectable.
If the Firebird database backend is configured, the injection can be exploited
using the following sqlmap command:
--------------------------------------------------------------------------------
< PoC removed >
--------------------------------------------------------------------------------

If the MSSQL backend is used the following sqlmap command can be used
with the request from above:
--------------------------------------------------------------------------------
< PoC removed >
--------------------------------------------------------------------------------

Depending on the used MSSQL database user and the database configuration
the injection can also be exploited to execute OS commands on the server.

3) Local Privilege Escalation (CVE-2025-15561)
To exploit the vulnerability, the attacker must first create an executable that
should be executed with elevated privileges. For this proof of concept the
following C code was used.
--------------------------------------------------------------------------------
< PoC removed >
--------------------------------------------------------------------------------

It is required to add versioning information during the linking process.
Otherwise WorkTime will not execute the created binary. Any resource file can be
used:
--------------------------------------------------------------------------------
1 VERSIONINFO
FILEVERSION 1,0,0,0
PRODUCTVERSION 1,0,0,0
FILEFLAGSMASK 0x3f
FILEFLAGS 0x0
FILEOS 0x40004
FILETYPE 0x1
FILESUBTYPE 0x0
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904b0"  // Language and code page
        BEGIN
            VALUE "CompanyName", "Your Company"
            VALUE "FileDescription", "Your Application Description"
            VALUE "FileVersion", "1.0.0.0"
            VALUE "InternalName", "YourApp"
            VALUE "OriginalFilename", "YourAp...