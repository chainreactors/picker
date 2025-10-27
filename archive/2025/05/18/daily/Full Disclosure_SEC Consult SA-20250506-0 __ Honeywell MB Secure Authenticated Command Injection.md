---
title: SEC Consult SA-20250506-0 :: Honeywell MB Secure Authenticated Command Injection
url: https://seclists.org/fulldisclosure/2025/May/19
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:39.476866
---

# SEC Consult SA-20250506-0 :: Honeywell MB Secure Authenticated Command Injection

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250506-0 :: Honeywell MB Secure Authenticated Command Injection

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 8 May 2025 08:58:56 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250507-0 >
=======================================================================
              title: Authenticated Command Injection
            product: Honeywell MB-Secure
 vulnerable version: MB-Secure versions from V11.04 and prior to V12.53,
MB-Secure PRO versions from V01.06 and prior to V03.09
      fixed version: MB-Secure v12.53, MB-Secure PRO v03.09
         CVE number: CVE-2025-2605
             impact: critical
           homepage:
https://buildings.honeywell.com/de/en/brands/our-brands/security/news/mb-secure
              found: 2024-11-04
                 by: Lukas Donaubauer (Office Munich)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"The MB-Secure is a high level security solution that offers more than just
security for buildings.
Thanks to its Touch & Go function, many building functions can be managed
easily. [...]
Our MB Secure alarm control panels set a new standard. It provides all the
power, capacity and
versatility needed to meet virtually any installation requirement from a
single platform. [...]
MB-Secure combines hardware, firmware, licensing and future security in one
platform.
Forward-looking technology allows the configuration to be tailored to just a
few users or large
integrated systems."

Source: https://www.security.honeywell.de/en/news/mb-secure/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the
product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Authenticated Command Injection (CVE-2025-2605)
The MB-Secure device provides a web interface for configuration which is
enabled by default.

An authenticated attacker in the web GUI is able to execute any OS
command by abusing the ping functionality at /si/ping. Roles which don't show
the ping interface
in the GUI can still reach and exploit this interface by directly opening the
URL.

By putting a semicolon and the desired command followed by another semicolon
into the interface
field and pressing the "Ping" button, the command gets executed on OS level.
The OS commands
are executed with the permissions of the "root" user hence an attacker can
completely
compromise the device.

Proof of concept:
-----------------
1) Authenticated Command Injection (CVE-2025-2605)
The affected lua file implements the ping function and executes it directly in
the OS via
the popen command without filtering or sanitizing the arguments.

Excerpt from nginx/lua/test/conf_panel_services.lua:
 [...]
        elseif ngx.var.arg_cmd == "ping" then

                local host = ngx.var.arg_host
                local intf = ngx.var.arg_interface or "eth0"
                local wait = ngx.var.arg_wait or 1
        local pingCnt = ngx.var.arg_count or 3
        local repeations = ngx.var.arg_repeations or 3
                local cmd
                local response
                if not host then
                        response = "No host"
                else

            cmd = "ping -W "..wait.." -c "..repeations.." -I "..intf.."
"..host

Excerpt from linuxCommand(cmd, ms, cb) function:
[...]
                local handler = io.popen(cmd)
[...]

This allows an authenticated attacker to browse to the /si/ping path, insert
the desired
command together with semicolons to break up the ping command on OS level and
execute
the command.

The "id" command has been executed as a proof of concept and shows that the
commands are
executed with permissions of the "root" user, see figure 1:

[code exec.png]

Vulnerable / tested versions:
-----------------------------
MB-Secure versions from V11.04 and prior to V12.53, MB-Secure PRO versions
from V01.06 and prior to V03.09

Vendor contact timeline:
------------------------
2024-12-04: Contacting vendor
2024-12-05: Answer from vendor with tracking number for future reference
2025-01-29: Contacting vendor again and asking for current status
2025-01-29: Answer from vendor, that patch will be released in 1-2 weeks,
security
            note is being worked on and a CVE will be assigned.
2025-01-30: Contacting vendor to ask for a notification 1-2 days before
release
            to be able to coordinate public release of advisory and
affected/fixed
            version numbers.
2025-01-31: Vendor informs us that patches have been released and security
notice
            will be distributed in two months to give customers enough
patching time.
2025-04-29: Vendor releases the Security Notice
2025-05-06: SEC Consult publishes advisory

Solution:
---------
The vulnerability has been remediated in MB-Secure release V12.53 and
MB-Secure PRO release
V03.09. Honeywell strongly recommends that users upgrade to MB-Secure release
V12.53 and
MB-Secure PRO release V03.09, respectively.
Source:
https://www.honeywell.com/content/dam/honeywellbt/en/documents/downloads/product-security/security-notification/hon-corp-os-command-injection-honeywell-mb-secure-2025-05-01-01.pdf

Workaround:
-----------

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Eviden business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your application https://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local offices https://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mail: security-research at sec-consult dot com
Web: https://www.sec-consult.com
Blog: https://blog.sec-consult.com
Twitter: https://twitter.com/sec_consult

EOF Lukas Donaubauer / @2025
```

**Attachment:
[smime.p7s](att-19/smime_p7s.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure ...